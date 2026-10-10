import { beforeEach, describe, expect, it, vi } from "vitest";

// createParentShare and revokeParentShare against an in-memory table that honors the query's meaning and supports transactions (a throw inside
// one rolls every write back). The fake throws on a filter it does not understand, so a new condition can't be silently ignored.

type Row = { id: string; userId: string; tokenHash: string; expiresAt: Date; revokedAt: Date | null };

const mocks = vi.hoisted(() => {
  const state = { userId: "u1" as string | null, rows: [] as { id: string; userId: string; tokenHash: string; expiresAt: Date; revokedAt: Date | null }[], failOnCreate: false, seq: 0 };
  type Where = { userId?: string; revokedAt?: null };
  const parentShare = {
      updateMany: vi.fn(async ({ where, data }: { where: Where; data: { revokedAt: Date } }) => {
        for (const k of Object.keys(where)) if (k !== "userId" && k !== "revokedAt") throw new Error(`fake does not understand where.${k}`);
        let count = 0;
        for (const r of state.rows) {
          if ((where.userId !== undefined && r.userId !== where.userId) || (where.revokedAt === null && r.revokedAt !== null)) continue;
          r.revokedAt = data.revokedAt;
          count++;
        }
        return { count };
      }),
      create: vi.fn(async ({ data }: { data: { userId: string; tokenHash: string; expiresAt: Date } }) => {
        if (state.failOnCreate) throw new Error("boom");
        state.rows.push({ id: `s${++state.seq}`, revokedAt: null, ...data });
        return data;
      }),
  };
  const db: Record<string, unknown> = {
    parentShare,
    $transaction: vi.fn(async (cb: (tx: unknown) => Promise<unknown>) => {
      const before = state.rows.map((r) => ({ ...r }));
      try {
        return await cb(db);
      } catch (e) {
        state.rows = before;
        throw e;
      }
    }),
  };
  return { state, db, parentShare, revalidatePath: vi.fn() };
});

vi.mock("@/lib/db", () => ({ getDb: () => mocks.db }));
vi.mock("@/lib/auth/config", () => ({ auth: async () => (mocks.state.userId ? { user: { id: mocks.state.userId } } : null) }));
vi.mock("next/cache", () => ({ revalidatePath: mocks.revalidatePath }));
vi.mock("@/lib/email/config", () => ({ siteUrl: () => "https://study.example" }));

import { createParentShare, revokeParentShare } from "@/lib/share/actions";
import { hashShareToken } from "@/lib/share/token";

const live = (userId: string) => mocks.state.rows.filter((r: Row) => r.userId === userId && r.revokedAt === null);

beforeEach(() => {
  vi.clearAllMocks();
  mocks.state.userId = "u1";
  mocks.state.failOnCreate = false;
  mocks.state.seq = 0;
  mocks.state.rows = [];
});

describe("createParentShare", () => {
  it("makes a link on the configured address, whose secret hashes to the stored row", async () => {
    const { url } = await createParentShare();
    expect(url).toMatch(/^https:\/\/study\.example\/share\/[A-Za-z0-9_-]{43}$/);
    const token = url.split("/share/")[1];
    expect(live("u1")).toHaveLength(1);
    expect(live("u1")[0].tokenHash).toBe(hashShareToken(token));
  });

  it("never stores the secret itself, only its hash", async () => {
    const { url } = await createParentShare();
    const token = url.split("/share/")[1];
    expect(JSON.stringify(mocks.state.rows)).not.toContain(token);
    expect(JSON.stringify(mocks.parentShare.create.mock.calls)).not.toContain(token);
  });

  it("expires the link in 90 days", async () => {
    const before = Date.now();
    await createParentShare();
    const days = (live("u1")[0].expiresAt.getTime() - before) / 86_400_000;
    expect(days).toBeGreaterThan(89.99);
    expect(days).toBeLessThan(90.01);
  });

  it("turns the earlier link off, so there is only ever one live link", async () => {
    const first = (await createParentShare()).url;
    const second = (await createParentShare()).url;
    expect(first).not.toBe(second);
    expect(live("u1")).toHaveLength(1);
    expect(live("u1")[0].tokenHash).toBe(hashShareToken(second.split("/share/")[1]));
    expect(mocks.state.rows).toHaveLength(2); // the old row is kept, revoked
  });

  it("leaves other students' links alone", async () => {
    mocks.state.userId = "u2";
    await createParentShare();
    mocks.state.userId = "u1";
    await createParentShare();
    expect(live("u2")).toHaveLength(1);
    expect(live("u1")).toHaveLength(1);
  });

  it("is all or nothing: if making the new link fails, the old one is still on", async () => {
    await createParentShare();
    const old = live("u1")[0].tokenHash;
    mocks.state.failOnCreate = true;
    await expect(createParentShare()).rejects.toThrow("boom");
    expect(live("u1")).toHaveLength(1);
    expect(live("u1")[0].tokenHash).toBe(old);
  });

  it("refreshes Settings, and refuses when nobody is signed in", async () => {
    await createParentShare();
    expect(mocks.revalidatePath).toHaveBeenCalledWith("/settings");
    mocks.state.userId = null;
    await expect(createParentShare()).rejects.toThrow("Not authenticated");
    expect(mocks.state.rows).toHaveLength(1);
  });
});

describe("revokeParentShare", () => {
  it("turns the student's link off", async () => {
    await createParentShare();
    await revokeParentShare();
    expect(live("u1")).toHaveLength(0);
    expect(mocks.revalidatePath).toHaveBeenCalledWith("/settings");
  });

  it("only ever touches the signed-in student's own links", async () => {
    mocks.state.userId = "u2";
    await createParentShare();
    mocks.state.userId = "u1";
    await createParentShare();
    await revokeParentShare();
    expect(live("u1")).toHaveLength(0);
    expect(live("u2")).toHaveLength(1);
  });

  it("is harmless with no link, and refuses when signed out", async () => {
    await expect(revokeParentShare()).resolves.toBeUndefined();
    mocks.state.userId = null;
    await expect(revokeParentShare()).rejects.toThrow("Not authenticated");
  });
});
