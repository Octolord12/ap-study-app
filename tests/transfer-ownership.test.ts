import { beforeEach, describe, expect, it, vi } from "vitest";

// transferClassOwnership against an in-memory class and membership table that honors the query's meaning and supports transactions (a throw
// inside one rolls every write back), so the tests show who can NOT hand a class over, that the roles swap, and that a failure half-way leaves
// the class as it was. The fake throws on a filter it does not understand, so a new condition can't be silently ignored.

const mocks = vi.hoisted(() => {
  const state = {
    userId: "owner1" as string | null,
    classes: [] as { id: string; ownerId: string }[],
    members: [] as { classId: string; userId: string; role: "OWNER" | "MEMBER" }[],
    failOn: null as string | null,
  };
  type ClassWhere = { id?: string; ownerId?: string; memberships?: { some: { userId?: string; role?: string } } };
  type MemberWhere = { classId?: string; userId?: string };
  const classMatches = (c: { id: string; ownerId: string }, w: ClassWhere) => {
    for (const k of Object.keys(w)) if (!["id", "ownerId", "memberships"].includes(k)) throw new Error(`fake does not understand class where.${k}`);
    if (w.memberships) for (const k of Object.keys(w.memberships)) if (k !== "some") throw new Error(`fake does not understand memberships.${k}`);
    return (
      (w.id === undefined || c.id === w.id) &&
      (w.ownerId === undefined || c.ownerId === w.ownerId) &&
      (w.memberships === undefined ||
        state.members.some((m) => m.classId === c.id && (w.memberships!.some.userId === undefined || m.userId === w.memberships!.some.userId) && (w.memberships!.some.role === undefined || m.role === w.memberships!.some.role)))
    );
  };
  const memberMatches = (m: { classId: string; userId: string }, w: MemberWhere) => {
    for (const k of Object.keys(w)) if (!["classId", "userId"].includes(k)) throw new Error(`fake does not understand membership where.${k}`);
    return (w.classId === undefined || m.classId === w.classId) && (w.userId === undefined || m.userId === w.userId);
  };
  const db: Record<string, unknown> = {
    class: {
      updateMany: vi.fn(async ({ where, data }: { where: ClassWhere; data: { ownerId: string } }) => {
        if (state.failOn === "class.updateMany") throw new Error("boom");
        let count = 0;
        for (const c of state.classes) {
          if (!classMatches(c, where)) continue;
          c.ownerId = data.ownerId;
          count++;
        }
        return { count };
      }),
    },
    classMembership: {
      updateMany: vi.fn(async ({ where, data }: { where: MemberWhere; data: { role: "OWNER" | "MEMBER" } }) => {
        const target = `membership.updateMany:${data.role}`;
        if (state.failOn === target) throw new Error("boom");
        let count = 0;
        for (const m of state.members) {
          if (!memberMatches(m, where)) continue;
          m.role = data.role;
          count++;
        }
        return { count };
      }),
    },
    // Real transactions are all-or-nothing: copy the state first, put it back if the callback throws.
    $transaction: vi.fn(async (cb: (tx: unknown) => Promise<unknown>) => {
      const before = { classes: state.classes.map((c) => ({ ...c })), members: state.members.map((m) => ({ ...m })) };
      try {
        return await cb(db);
      } catch (e) {
        state.classes = before.classes;
        state.members = before.members;
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

import { transferClassOwnership } from "@/lib/social/actions";

const owner = (id: string) => mocks.state.classes.find((c) => c.id === id)?.ownerId;
const roles = (classId: string) => Object.fromEntries(mocks.state.members.filter((m) => m.classId === classId).map((m) => [m.userId, m.role]));

describe("transferClassOwnership", () => {
  beforeEach(() => {
    vi.clearAllMocks();
    mocks.state.userId = "owner1";
    mocks.state.failOn = null;
    mocks.state.classes = [
      { id: "c1", ownerId: "owner1" },
      { id: "c2", ownerId: "owner2" },
    ];
    mocks.state.members = [
      { classId: "c1", userId: "owner1", role: "OWNER" },
      { classId: "c1", userId: "alice", role: "MEMBER" },
      { classId: "c1", userId: "bob", role: "MEMBER" },
      { classId: "c2", userId: "owner2", role: "OWNER" },
      { classId: "c2", userId: "carol", role: "MEMBER" },
      { classId: "c2", userId: "alice", role: "MEMBER" },
    ];
  });

  it("hands the class to a member: the class's owner and both roles swap", async () => {
    await transferClassOwnership("c1", "alice");
    expect(owner("c1")).toBe("alice");
    expect(roles("c1")).toEqual({ owner1: "MEMBER", alice: "OWNER", bob: "MEMBER" });
  });

  it("leaves everything else alone: the other member, and every other class", async () => {
    await transferClassOwnership("c1", "alice");
    expect(roles("c1").bob).toBe("MEMBER");
    expect(owner("c2")).toBe("owner2");
    expect(roles("c2")).toEqual({ owner2: "OWNER", carol: "MEMBER", alice: "MEMBER" });
  });

  it("does nothing when the signed-in user does not own the class (a member, or someone owning another class)", async () => {
    mocks.state.userId = "bob";
    await transferClassOwnership("c1", "alice");
    mocks.state.userId = "owner2";
    await transferClassOwnership("c1", "alice");
    expect(owner("c1")).toBe("owner1");
    expect(roles("c1")).toEqual({ owner1: "OWNER", alice: "MEMBER", bob: "MEMBER" });
  });

  it("does nothing for someone who is not a member of that class, even if they are in another class of the same owner", async () => {
    await transferClassOwnership("c1", "carol");
    await transferClassOwnership("c1", "nobody");
    expect(owner("c1")).toBe("owner1");
    expect(roles("c1")).toEqual({ owner1: "OWNER", alice: "MEMBER", bob: "MEMBER" });
  });

  it("does nothing, without an error, when handing the class to oneself", async () => {
    await expect(transferClassOwnership("c1", "owner1")).resolves.toBeUndefined();
    expect(mocks.db.$transaction).not.toHaveBeenCalled();
    expect(owner("c1")).toBe("owner1");
  });

  it("does nothing, without an error, for a class that does not exist", async () => {
    await expect(transferClassOwnership("nope", "alice")).resolves.toBeUndefined();
    expect(owner("c1")).toBe("owner1");
  });

  it("is all or nothing: if the second write fails, the class is not left with a changed owner", async () => {
    mocks.state.failOn = "membership.updateMany:MEMBER";
    await expect(transferClassOwnership("c1", "alice")).rejects.toThrow("boom");
    expect(owner("c1")).toBe("owner1");
    expect(roles("c1")).toEqual({ owner1: "OWNER", alice: "MEMBER", bob: "MEMBER" });
  });

  it("is all or nothing when the first membership write fails too", async () => {
    mocks.state.failOn = "membership.updateMany:OWNER";
    await expect(transferClassOwnership("c1", "alice")).rejects.toThrow("boom");
    expect(owner("c1")).toBe("owner1");
    expect(roles("c1")).toEqual({ owner1: "OWNER", alice: "MEMBER", bob: "MEMBER" });
  });

  it("after the swap the former owner can no longer do owner things, and the new one can hand it back", async () => {
    await transferClassOwnership("c1", "alice");
    mocks.state.userId = "owner1";
    await transferClassOwnership("c1", "bob"); // no longer the owner: nothing happens
    expect(owner("c1")).toBe("alice");
    mocks.state.userId = "alice";
    await transferClassOwnership("c1", "owner1");
    expect(owner("c1")).toBe("owner1");
    expect(roles("c1")).toEqual({ owner1: "OWNER", alice: "MEMBER", bob: "MEMBER" });
  });

  it("refreshes the class page and the class list", async () => {
    await transferClassOwnership("c1", "alice");
    expect(mocks.revalidatePath).toHaveBeenCalledWith("/classes/c1");
    expect(mocks.revalidatePath).toHaveBeenCalledWith("/classes");
  });

  it("refuses when nobody is signed in, and changes nothing", async () => {
    mocks.state.userId = null;
    await expect(transferClassOwnership("c1", "alice")).rejects.toThrow("Not authenticated");
    expect(mocks.db.$transaction).not.toHaveBeenCalled();
    expect(owner("c1")).toBe("owner1");
  });
});
