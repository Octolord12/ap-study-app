import { describe, expect, it, vi } from "vitest";

const findMany = vi.hoisted(() => vi.fn((args: { where: unknown; select: unknown }) => Promise.resolve(args && [])));
vi.mock("@/lib/db", () => ({ getDb: () => ({ classBan: { findMany } }) }));

import { getClassBans } from "@/lib/social/queries";

describe("getClassBans", () => {
  it("asks only for blocks in that class, and only when the person asking owns it, so anyone else gets an empty list", async () => {
    await getClassBans("c1", "owner1");
    expect(findMany.mock.calls[0][0].where).toEqual({ classId: "c1", class: { ownerId: "owner1" } });
  });

  it("reads usernames only, never email or display name", async () => {
    await getClassBans("c1", "owner1");
    expect(findMany.mock.calls[0][0].select).toEqual({ userId: true, bannedAt: true, user: { select: { username: true } } });
  });
});
