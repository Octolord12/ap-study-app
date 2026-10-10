import { beforeEach, describe, expect, it, vi } from "vitest";

// blockClassMember, unblockClassMember and joinClass against an in-memory store that honors every part of a query and supports transactions
// (a throw inside one rolls every write back), so the tests show who can NOT block, that blocking is atomic, and that a blocked person really
// cannot join. The fake throws on a filter it does not understand, so a new condition can't be silently ignored.

type Member = { classId: string; userId: string; role: "OWNER" | "MEMBER" };
type Ban = { classId: string; userId: string };

const mocks = vi.hoisted(() => {
  const state = {
    userId: "owner1" as string | null,
    owners: {} as Record<string, string>,
    codes: {} as Record<string, string>, // invite code -> class id
    members: [] as { classId: string; userId: string; role: "OWNER" | "MEMBER" }[],
    bans: [] as { classId: string; userId: string }[],
    failOn: null as string | null,
  };
  type Where = { classId?: string; userId?: string; role?: string; class?: { ownerId?: string } };
  const ok = (w: Where, extra: string[] = []) => {
    for (const k of Object.keys(w)) if (!["classId", "userId", "role", "class", ...extra].includes(k)) throw new Error(`fake does not understand where.${k}`);
  };
  const m = (r: { classId: string; userId: string; role?: string }, w: Where) =>
    (w.classId === undefined || r.classId === w.classId) &&
    (w.userId === undefined || r.userId === w.userId) &&
    (w.role === undefined || r.role === w.role) &&
    (w.class?.ownerId === undefined || state.owners[r.classId] === w.class.ownerId);
  const db: Record<string, unknown> = {
    class: { findUnique: vi.fn(async ({ where }: { where: { inviteCode: string } }) => (state.codes[where.inviteCode] ? { id: state.codes[where.inviteCode] } : null)) },
    classMembership: {
      deleteMany: vi.fn(async ({ where }: { where: Where }) => {
        ok(where);
        const before = state.members.length;
        state.members = state.members.filter((r) => !m(r, where));
        return { count: before - state.members.length };
      }),
      upsert: vi.fn(async ({ create }: { create: { classId: string; userId: string; role: "MEMBER" } }) => {
        if (!state.members.some((r) => r.classId === create.classId && r.userId === create.userId)) state.members.push(create);
        return create;
      }),
    },
    classBan: {
      upsert: vi.fn(async ({ where, create }: { where: { classId_userId: Ban }; create: Ban }) => {
        if (state.failOn === "classBan.upsert") throw new Error("boom");
        if (!state.bans.some((b) => b.classId === where.classId_userId.classId && b.userId === where.classId_userId.userId)) state.bans.push(create);
        return create;
      }),
      findUnique: vi.fn(async ({ where }: { where: { classId_userId: Ban } }) => state.bans.find((b) => b.classId === where.classId_userId.classId && b.userId === where.classId_userId.userId) ?? null),
      deleteMany: vi.fn(async ({ where }: { where: Where }) => {
        ok(where);
        const before = state.bans.length;
        state.bans = state.bans.filter((r) => !m(r, where));
        return { count: before - state.bans.length };
      }),
    },
    $transaction: vi.fn(async (cb: (tx: unknown) => Promise<unknown>) => {
      const before = { members: state.members.map((x) => ({ ...x })), bans: state.bans.map((x) => ({ ...x })) };
      try {
        return await cb(db);
      } catch (e) {
        state.members = before.members;
        state.bans = before.bans;
        throw e;
      }
    }),
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

import { blockClassMember, joinClass, unblockClassMember } from "@/lib/social/actions";

const memberIds = (classId: string) => mocks.state.members.filter((r: Member) => r.classId === classId).map((r: Member) => r.userId).sort();
const banIds = (classId: string) => mocks.state.bans.filter((b: Ban) => b.classId === classId).map((b: Ban) => b.userId).sort();
async function join(code: string) {
  const f = new FormData();
  f.set("inviteCode", code);
  try {
    await joinClass(f);
  } catch (e) {
    return (e as Error).message;
  }
  return "no redirect";
}

beforeEach(() => {
  vi.clearAllMocks();
  mocks.state.userId = "owner1";
  mocks.state.failOn = null;
  mocks.state.owners = { c1: "owner1", c2: "owner2" };
  mocks.state.codes = { AAAAAA: "c1", BBBBBB: "c2" };
  mocks.state.members = [
    { classId: "c1", userId: "owner1", role: "OWNER" },
    { classId: "c1", userId: "alice", role: "MEMBER" },
    { classId: "c1", userId: "bob", role: "MEMBER" },
    { classId: "c2", userId: "owner2", role: "OWNER" },
    { classId: "c2", userId: "alice", role: "MEMBER" },
  ];
  mocks.state.bans = [];
});

describe("blockClassMember", () => {
  it("removes the member and blocks them", async () => {
    await blockClassMember("c1", "alice");
    expect(memberIds("c1")).toEqual(["bob", "owner1"]);
    expect(banIds("c1")).toEqual(["alice"]);
  });

  it("touches only that class and that person", async () => {
    await blockClassMember("c1", "alice");
    expect(memberIds("c2")).toEqual(["alice", "owner2"]); // alice is still in the other class
    expect(banIds("c2")).toEqual([]);
    expect(memberIds("c1")).toContain("bob");
  });

  it("does nothing for someone who is not the class's owner (a member, another class's owner, a stranger)", async () => {
    for (const who of ["bob", "owner2", "stranger"]) {
      mocks.state.userId = who;
      await blockClassMember("c1", "alice");
    }
    expect(memberIds("c1")).toEqual(["alice", "bob", "owner1"]);
    expect(banIds("c1")).toEqual([]);
  });

  it("can't block the owner themselves, nor someone who isn't a member (no pre-emptive blocks)", async () => {
    await blockClassMember("c1", "owner1");
    await blockClassMember("c1", "stranger");
    expect(memberIds("c1")).toEqual(["alice", "bob", "owner1"]);
    expect(banIds("c1")).toEqual([]);
  });

  it("is all or nothing: if recording the block fails, the member is not left removed", async () => {
    mocks.state.failOn = "classBan.upsert";
    await expect(blockClassMember("c1", "alice")).rejects.toThrow("boom");
    expect(memberIds("c1")).toEqual(["alice", "bob", "owner1"]);
    expect(banIds("c1")).toEqual([]);
  });

  it("is harmless to repeat", async () => {
    await blockClassMember("c1", "alice");
    await blockClassMember("c1", "alice");
    expect(banIds("c1")).toEqual(["alice"]);
  });

  it("refreshes the class page and the list, and refuses when signed out", async () => {
    await blockClassMember("c1", "alice");
    expect(mocks.revalidatePath).toHaveBeenCalledWith("/classes/c1");
    expect(mocks.revalidatePath).toHaveBeenCalledWith("/classes");
    mocks.state.userId = null;
    await expect(blockClassMember("c1", "bob")).rejects.toThrow("Not authenticated");
    expect(memberIds("c1")).toContain("bob");
  });
});

describe("a blocked person and the invite code", () => {
  it("cannot rejoin: they get the same answer as a wrong code, and no membership is created", async () => {
    await blockClassMember("c1", "alice");
    mocks.state.userId = "alice";
    expect(await join("AAAAAA")).toBe("redirect:/classes?error=not-found");
    expect(await join("ZZZZZZ")).toBe("redirect:/classes?error=not-found"); // identical to a code that does not exist
    expect(memberIds("c1")).not.toContain("alice");
  });

  it("can still join other classes, and everyone else can still join this one", async () => {
    await blockClassMember("c1", "alice");
    mocks.state.userId = "alice";
    expect(await join("BBBBBB")).toBe("redirect:/classes/c2");
    mocks.state.userId = "carol";
    expect(await join("AAAAAA")).toBe("redirect:/classes/c1");
    expect(memberIds("c1")).toContain("carol");
  });

  it("a plain removal (no block) leaves them free to rejoin", async () => {
    mocks.state.members = mocks.state.members.filter((r: Member) => !(r.classId === "c1" && r.userId === "alice"));
    mocks.state.userId = "alice";
    expect(await join("AAAAAA")).toBe("redirect:/classes/c1");
  });

  it("a new invite code does not lift the block (the block is on the person, not the code)", async () => {
    await blockClassMember("c1", "alice");
    mocks.state.codes = { NEWCDE: "c1" };
    mocks.state.userId = "alice";
    expect(await join("NEWCDE")).toBe("redirect:/classes?error=not-found");
  });
});

describe("unblockClassMember", () => {
  beforeEach(() => {
    mocks.state.owners.c3 = "owner1"; // a second class the same owner runs, where alice is blocked too
    mocks.state.bans = [
      { classId: "c1", userId: "alice" },
      { classId: "c2", userId: "alice" },
      { classId: "c3", userId: "alice" },
    ];
    mocks.state.members = mocks.state.members.filter((r: Member) => !(r.classId === "c1" && r.userId === "alice"));
  });

  it("lets the person join again, but does not add them back", async () => {
    await unblockClassMember("c1", "alice");
    expect(banIds("c1")).toEqual([]);
    expect(memberIds("c1")).not.toContain("alice");
    mocks.state.userId = "alice";
    expect(await join("AAAAAA")).toBe("redirect:/classes/c1");
  });

  it("leaves the same person's block in other classes alone, including another class the same owner runs", async () => {
    await unblockClassMember("c1", "alice");
    expect(banIds("c2")).toEqual(["alice"]);
    expect(banIds("c3")).toEqual(["alice"]);
  });

  it("does nothing for anyone but the class's owner, including the blocked person themselves", async () => {
    for (const who of ["alice", "bob", "owner2"]) {
      mocks.state.userId = who;
      await unblockClassMember("c1", "alice");
    }
    expect(banIds("c1")).toEqual(["alice"]);
  });

  it("refuses when signed out", async () => {
    mocks.state.userId = null;
    await expect(unblockClassMember("c1", "alice")).rejects.toThrow("Not authenticated");
    expect(banIds("c1")).toEqual(["alice"]);
  });
});
