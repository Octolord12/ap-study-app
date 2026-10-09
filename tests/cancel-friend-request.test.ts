import { beforeEach, describe, expect, it, vi } from "vitest";

// cancelFriendRequest against an in-memory friendship table that honors the query's meaning, so the tests show what it can NOT remove:
// only a PENDING request the signed-in user sent.

type Row = { requesterId: string; addresseeId: string; status: "PENDING" | "ACCEPTED" | "BLOCKED" };

const mocks = vi.hoisted(() => {
  const state = { userId: "me" as string | null, rows: [] as Row[] };
  type Where = { status?: string; requesterId?: string; addresseeId?: string };
  const matches = (r: Row, w: Where) => (!w.status || r.status === w.status) && (!w.requesterId || r.requesterId === w.requesterId) && (!w.addresseeId || r.addresseeId === w.addresseeId);
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

import { cancelFriendRequest as cancelAction } from "@/lib/social/actions";

// The action ends in redirect("/friends"), which the mocked redirect above turns into a thrown error; swallow exactly that one.
async function cancelFriendRequest(addresseeId: string) {
  try {
    await cancelAction(addresseeId);
  } catch (error) {
    if (!(error instanceof Error) || error.message !== "redirect:/friends") throw error;
  }
}

const pair = (r: Row) => `${r.requesterId}>${r.addresseeId}:${r.status}`;
const remaining = () => mocks.state.rows.map(pair).sort();

describe("cancelFriendRequest", () => {
  beforeEach(() => {
    vi.clearAllMocks();
    mocks.state.userId = "me";
    mocks.state.rows = [
      { requesterId: "me", addresseeId: "carol", status: "PENDING" },
      { requesterId: "dave", addresseeId: "me", status: "PENDING" },
      { requesterId: "me", addresseeId: "alice", status: "ACCEPTED" },
      { requesterId: "me", addresseeId: "erin", status: "BLOCKED" },
      { requesterId: "bob", addresseeId: "carol", status: "PENDING" },
    ];
  });

  it("cancels a pending request the signed-in user sent", async () => {
    await cancelFriendRequest("carol");
    expect(remaining()).not.toContain("me>carol:PENDING");
    expect(mocks.state.rows).toHaveLength(4);
  });

  it("does not cancel a request someone else sent to the user (declining has its own action)", async () => {
    await cancelFriendRequest("dave");
    expect(remaining()).toContain("dave>me:PENDING");
  });

  it("does not remove an accepted friendship or a blocked row", async () => {
    await cancelFriendRequest("alice");
    await cancelFriendRequest("erin");
    expect(remaining()).toContain("me>alice:ACCEPTED");
    expect(remaining()).toContain("me>erin:BLOCKED");
  });

  it("never touches other people's requests, even to the same person", async () => {
    await cancelFriendRequest("carol");
    expect(remaining()).toContain("bob>carol:PENDING");
  });

  it("does nothing, without an error, when there is no such request", async () => {
    const before = remaining();
    await expect(cancelFriendRequest("nobody")).resolves.toBeUndefined();
    expect(remaining()).toEqual(before);
  });

  it("refreshes the friends page and sends the person to the bare URL, so a stale 'Friend request sent.' does not stay up", async () => {
    await expect(cancelAction("carol")).rejects.toThrow("redirect:/friends");
    expect(mocks.revalidatePath).toHaveBeenCalledWith("/friends");
  });

  it("refuses when nobody is signed in, and deletes nothing", async () => {
    mocks.state.userId = null;
    await expect(cancelAction("carol")).rejects.toThrow("Not authenticated");
    expect(mocks.db.friendship.deleteMany).not.toHaveBeenCalled();
    expect(mocks.state.rows).toHaveLength(5);
  });
});
