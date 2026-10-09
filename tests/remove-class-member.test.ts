import { beforeEach, describe, expect, it, vi } from "vitest";

// removeClassMember against an in-memory membership table that honors every part of the query (class, person, role, and "the class's
// owner is the signed-in user"), so the tests show what it can NOT remove as well as what it does. The fake throws on a filter it does
// not understand, so a new condition can't be silently ignored by the test.

type Row = { classId: string; userId: string; role: "OWNER" | "MEMBER" };
type Where = { classId?: string; userId?: string; role?: string; class?: { ownerId?: string } };

const mocks = vi.hoisted(() => {
  const state = {
    userId: "owner1" as string | null,
    owners: {} as Record<string, string>,
    rows: [] as { classId: string; userId: string; role: "OWNER" | "MEMBER" }[],
  };
  const KNOWN = new Set(["classId", "userId", "role", "class"]);
  const matches = (r: Row, where: Where) => {
    for (const key of Object.keys(where)) if (!KNOWN.has(key)) throw new Error(`fake does not understand where.${key}`);
    if (where.class) for (const key of Object.keys(where.class)) if (key !== "ownerId") throw new Error(`fake does not understand where.class.${key}`);
    return (
      (where.classId === undefined || r.classId === where.classId) &&
      (where.userId === undefined || r.userId === where.userId) &&
      (where.role === undefined || r.role === where.role) &&
      (where.class?.ownerId === undefined || state.owners[r.classId] === where.class.ownerId)
    );
  };
  const db = {
    classMembership: {
      deleteMany: vi.fn(async ({ where }: { where: Where }) => {
        const before = state.rows.length;
        state.rows = state.rows.filter((r) => !matches(r, where));
        return { count: before - state.rows.length };
      }),
    },
  };
  return { state, db, revalidatePath: vi.fn() };
});

vi.mock("@/lib/db", () => ({ getDb: () => mocks.db }));
vi.mock("@/lib/auth/config", () => ({ auth: async () => (mocks.state.userId ? { user: { id: mocks.state.userId } } : null) }));
vi.mock("next/cache", () => ({ revalidatePath: mocks.revalidatePath }));
vi.mock("next/navigation", () => ({
  redirect: (to: string) => {
    throw new Error(`redirect:${to}`);
  },
}));

import { removeClassMember } from "@/lib/social/actions";

const key = (r: Row) => `${r.classId}/${r.userId}:${r.role}`;
const remaining = () => mocks.state.rows.map(key).sort();

describe("removeClassMember", () => {
  beforeEach(() => {
    vi.clearAllMocks();
    mocks.state.userId = "owner1";
    mocks.state.owners = { c1: "owner1", c2: "owner2", c3: "owner1" };
    mocks.state.rows = [
      { classId: "c1", userId: "owner1", role: "OWNER" },
      { classId: "c1", userId: "alice", role: "MEMBER" },
      { classId: "c1", userId: "bob", role: "MEMBER" },
      { classId: "c2", userId: "owner2", role: "OWNER" },
      { classId: "c2", userId: "alice", role: "MEMBER" },
      { classId: "c2", userId: "owner1", role: "MEMBER" },
      { classId: "c3", userId: "owner1", role: "OWNER" },
      { classId: "c3", userId: "alice", role: "MEMBER" },
    ];
  });

  it("removes a member from a class the signed-in user owns", async () => {
    await removeClassMember("c1", "alice");
    expect(remaining()).not.toContain("c1/alice:MEMBER");
    expect(mocks.state.rows).toHaveLength(7);
  });

  it("removes only that person: the other members, the owner and other classes are untouched", async () => {
    await removeClassMember("c1", "alice");
    expect(remaining()).toEqual(["c1/bob:MEMBER", "c1/owner1:OWNER", "c2/alice:MEMBER", "c2/owner1:MEMBER", "c2/owner2:OWNER", "c3/alice:MEMBER", "c3/owner1:OWNER"]);
  });

  it("removes them from that class only, not from another class the same owner runs", async () => {
    await removeClassMember("c1", "alice");
    expect(remaining()).toContain("c3/alice:MEMBER");
  });

  it("does not let the owner remove their own owner row", async () => {
    await removeClassMember("c1", "owner1");
    expect(remaining()).toContain("c1/owner1:OWNER");
  });

  it("does nothing when the signed-in user is only a member of that class", async () => {
    mocks.state.userId = "bob";
    await removeClassMember("c1", "alice");
    expect(remaining()).toContain("c1/alice:MEMBER");
    expect(mocks.state.rows).toHaveLength(8);
  });

  it("does nothing in a class owned by someone else, even where the signed-in user is a member", async () => {
    await removeClassMember("c2", "alice");
    expect(remaining()).toContain("c2/alice:MEMBER");
  });

  it("does nothing when someone who is not in the class at all tries", async () => {
    mocks.state.userId = "stranger";
    await removeClassMember("c1", "alice");
    await removeClassMember("c1", "bob");
    expect(mocks.state.rows).toHaveLength(8);
  });

  it("does nothing, without an error, for someone who is not in the class", async () => {
    const before = remaining();
    await expect(removeClassMember("c1", "nobody")).resolves.toBeUndefined();
    expect(remaining()).toEqual(before);
  });

  it("refreshes the class page and the class list", async () => {
    await removeClassMember("c1", "alice");
    expect(mocks.revalidatePath).toHaveBeenCalledWith("/classes/c1");
    expect(mocks.revalidatePath).toHaveBeenCalledWith("/classes");
  });

  it("refuses when nobody is signed in, and deletes nothing", async () => {
    mocks.state.userId = null;
    await expect(removeClassMember("c1", "alice")).rejects.toThrow("Not authenticated");
    expect(mocks.db.classMembership.deleteMany).not.toHaveBeenCalled();
    expect(mocks.state.rows).toHaveLength(8);
  });
});
