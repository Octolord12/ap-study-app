import { beforeEach, describe, expect, it, vi } from "vitest";

// regenerateInviteCode against an in-memory class table that honors the query's meaning (the class id AND its owner; lookups by code), so
// the tests show who can NOT change a code as well as who can, and that the old code really stops working in the join flow. The fake throws
// on a filter it does not understand, so a new condition can't be silently ignored.

type Where = { id?: string; ownerId?: string; inviteCode?: string };

const mocks = vi.hoisted(() => {
  const state = {
    userId: "owner1" as string | null,
    rows: [] as { id: string; ownerId: string; inviteCode: string }[],
    generated: [] as string[],
  };
  const check = (where: Where) => {
    for (const key of Object.keys(where)) if (!["id", "ownerId", "inviteCode"].includes(key)) throw new Error(`fake does not understand where.${key}`);
  };
  const matches = (r: { id: string; ownerId: string; inviteCode: string }, where: Where) =>
    (where.id === undefined || r.id === where.id) && (where.ownerId === undefined || r.ownerId === where.ownerId) && (where.inviteCode === undefined || r.inviteCode === where.inviteCode);
  const db = {
    class: {
      findUnique: vi.fn(async ({ where }: { where: Where }) => {
        check(where);
        return state.rows.find((r) => matches(r, where)) ?? null;
      }),
      updateMany: vi.fn(async ({ where, data }: { where: Where; data: { inviteCode: string } }) => {
        check(where);
        let count = 0;
        for (const r of state.rows) {
          if (!matches(r, where)) continue;
          r.inviteCode = data.inviteCode;
          count++;
        }
        return { count };
      }),
    },
    classMembership: { upsert: vi.fn(async () => ({})) },
    classBan: { findUnique: vi.fn(async () => null) }, // joinClass checks the block list; nobody is blocked in these tests
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
vi.mock("@/lib/social/invite-code", async (importOriginal) => ({
  ...(await importOriginal<typeof import("@/lib/social/invite-code")>()),
  generateInviteCode: () => {
    const next = mocks.state.generated.shift();
    if (next === undefined) throw new Error("test ran out of generated codes");
    return next;
  },
}));

import { joinClass, regenerateInviteCode } from "@/lib/social/actions";

const codes = () => Object.fromEntries(mocks.state.rows.map((r) => [r.id, r.inviteCode]));
const join = async (code: string) => {
  const f = new FormData();
  f.set("inviteCode", code);
  try {
    await joinClass(f);
  } catch (e) {
    return (e as Error).message;
  }
  return "no redirect";
};

describe("regenerateInviteCode", () => {
  beforeEach(() => {
    vi.clearAllMocks();
    mocks.state.userId = "owner1";
    mocks.state.generated = ["NEWCDE"];
    mocks.state.rows = [
      { id: "c1", ownerId: "owner1", inviteCode: "OLDAAA" },
      { id: "c2", ownerId: "owner2", inviteCode: "OTHER2" },
      { id: "c3", ownerId: "owner1", inviteCode: "THIRD3" },
    ];
  });

  it("gives a class the signed-in user owns a new code", async () => {
    await regenerateInviteCode("c1");
    expect(codes().c1).toBe("NEWCDE");
  });

  it("changes only that class: another class the same owner runs, and other owners' classes, keep their codes", async () => {
    await regenerateInviteCode("c1");
    expect(codes()).toEqual({ c1: "NEWCDE", c2: "OTHER2", c3: "THIRD3" });
  });

  it("makes the old code stop working for joining, and the new one work", async () => {
    await regenerateInviteCode("c1");
    expect(await join("OLDAAA")).toBe("redirect:/classes?error=not-found");
    expect(mocks.db.classMembership.upsert).not.toHaveBeenCalled();
    expect(await join("newcde")).toBe("redirect:/classes/c1");
    expect(mocks.db.classMembership.upsert).toHaveBeenCalledTimes(1);
  });

  it("does nothing to a class someone else owns (a member, or a stranger who guessed the id)", async () => {
    await regenerateInviteCode("c2");
    expect(codes().c2).toBe("OTHER2");
  });

  it("does nothing, without an error, for a class that does not exist", async () => {
    await expect(regenerateInviteCode("nope")).resolves.toBeUndefined();
    expect(codes()).toEqual({ c1: "OLDAAA", c2: "OTHER2", c3: "THIRD3" });
  });

  it("skips a candidate that another class already uses, and takes the next", async () => {
    mocks.state.generated = ["OTHER2", "THIRD3", "FRESH4"];
    await regenerateInviteCode("c1");
    expect(codes().c1).toBe("FRESH4");
  });

  it("gives up after five collisions and changes nothing", async () => {
    mocks.state.generated = ["OTHER2", "OTHER2", "OTHER2", "OTHER2", "OTHER2"];
    await expect(regenerateInviteCode("c1")).rejects.toThrow("Could not generate a unique invite code");
    expect(codes().c1).toBe("OLDAAA");
  });

  it("refreshes the class page", async () => {
    await regenerateInviteCode("c1");
    expect(mocks.revalidatePath).toHaveBeenCalledWith("/classes/c1");
  });

  it("refuses when nobody is signed in, and changes nothing", async () => {
    mocks.state.userId = null;
    await expect(regenerateInviteCode("c1")).rejects.toThrow("Not authenticated");
    expect(mocks.db.class.updateMany).not.toHaveBeenCalled();
    expect(codes().c1).toBe("OLDAAA");
  });
});
