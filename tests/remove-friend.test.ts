import { beforeEach, describe, expect, it, vi } from "vitest";

// removeFriend against an in-memory friendship table that honors the query's meaning (status plus the either-direction OR), so the tests
// show what it can NOT remove as well as what it does: only the signed-in user's own accepted friendship with that person.

type Row = { requesterId: string; addresseeId: string; status: "PENDING" | "ACCEPTED" | "BLOCKED" };

const mocks = vi.hoisted(() => {
  const state = { userId: "me" as string | null, rows: [] as Row[] };
  type Where = { status?: string; OR?: { requesterId: string; addresseeId: string }[] };
  const matches = (r: Row, where: Where) => (!where.status || r.status === where.status) && (!where.OR || where.OR.some((c) => r.requesterId === c.requesterId && r.addresseeId === c.addresseeId));
  const db = {
    friendship: {
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

import { removeFriend } from "@/lib/social/actions";

const pair = (r: Row) => `${r.requesterId}>${r.addresseeId}:${r.status}`;
const remaining = () => mocks.state.rows.map(pair).sort();

describe("removeFriend", () => {
  beforeEach(() => {
    vi.clearAllMocks();
    mocks.state.userId = "me";
    mocks.state.rows = [
      { requesterId: "me", addresseeId: "alice", status: "ACCEPTED" },
      { requesterId: "bob", addresseeId: "me", status: "ACCEPTED" },
      { requesterId: "alice", addresseeId: "bob", status: "ACCEPTED" },
      { requesterId: "me", addresseeId: "carol", status: "PENDING" },
      { requesterId: "dave", addresseeId: "me", status: "PENDING" },
      { requesterId: "me", addresseeId: "erin", status: "BLOCKED" },
    ];
  });

  it("removes a friendship the signed-in user sent", async () => {
    await removeFriend("alice");
    expect(remaining()).not.toContain("me>alice:ACCEPTED");
    expect(mocks.state.rows).toHaveLength(5);
  });

  it("removes a friendship the other person sent", async () => {
    await removeFriend("bob");
    expect(remaining()).not.toContain("bob>me:ACCEPTED");
    expect(mocks.state.rows).toHaveLength(5);
  });

  it("never touches other people's friendships", async () => {
    await removeFriend("alice");
    await removeFriend("bob");
    expect(remaining()).toContain("alice>bob:ACCEPTED");
  });

  it("does not cancel a pending request, in either direction (declining has its own action)", async () => {
    await removeFriend("carol");
    await removeFriend("dave");
    expect(remaining()).toContain("me>carol:PENDING");
    expect(remaining()).toContain("dave>me:PENDING");
  });

  it("does not remove a blocked row", async () => {
    await removeFriend("erin");
    expect(remaining()).toContain("me>erin:BLOCKED");
  });

  it("does nothing, without an error, for someone who is not a friend or for oneself", async () => {
    const before = remaining();
    await expect(removeFriend("nobody")).resolves.toBeUndefined();
    await expect(removeFriend("me")).resolves.toBeUndefined();
    expect(remaining()).toEqual(before);
  });

  it("refreshes the friends page", async () => {
    await removeFriend("alice");
    expect(mocks.revalidatePath).toHaveBeenCalledWith("/friends");
  });

  it("refuses when nobody is signed in, and deletes nothing", async () => {
    mocks.state.userId = null;
    await expect(removeFriend("alice")).rejects.toThrow("Not authenticated");
    expect(mocks.db.friendship.deleteMany).not.toHaveBeenCalled();
    expect(mocks.state.rows).toHaveLength(6);
  });
});
