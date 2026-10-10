import { beforeEach, describe, expect, it, vi } from "vitest";

const mocks = vi.hoisted(() => ({ findUnique: vi.fn(), findFirst: vi.fn(), updateMany: vi.fn() }));
vi.mock("@/lib/db", () => ({ getDb: () => ({ parentShare: mocks }) }));

import { findUsableShare, getActiveParentShare, recordShareView } from "@/lib/share/queries";
import { hashShareToken, newShareToken } from "@/lib/share/token";

const now = new Date("2026-10-09T12:00:00Z");
const row = (over: Partial<{ revokedAt: Date | null; expiresAt: Date }> = {}) => ({
  id: "s1",
  expiresAt: new Date(now.getTime() + 86_400_000),
  revokedAt: null,
  user: { id: "u1", username: "alice" },
  ...over,
});

describe("findUsableShare", () => {
  beforeEach(() => vi.clearAllMocks());

  it("finds a live link by the hash of its secret and returns only the owner's id and username", async () => {
    const { token } = newShareToken();
    mocks.findUnique.mockResolvedValue(row());
    const share = await findUsableShare(token, now);
    expect(share).toEqual({ id: "s1", expiresAt: row().expiresAt, userId: "u1", username: "alice" });
    expect(mocks.findUnique.mock.calls[0][0].where).toEqual({ tokenHash: hashShareToken(token) });
    expect(mocks.findUnique.mock.calls[0][0].select.user).toEqual({ select: { id: true, username: true } }); // never email or name
  });

  it("is null for a revoked link, an expired one and an unknown one: all the same to the visitor", async () => {
    const { token } = newShareToken();
    mocks.findUnique.mockResolvedValue(row({ revokedAt: new Date(now.getTime() - 1000) }));
    expect(await findUsableShare(token, now)).toBeNull();
    mocks.findUnique.mockResolvedValue(row({ expiresAt: new Date(now.getTime() - 1) }));
    expect(await findUsableShare(token, now)).toBeNull();
    mocks.findUnique.mockResolvedValue(null);
    expect(await findUsableShare(token, now)).toBeNull();
  });

  it("does not touch the database for a malformed token", async () => {
    for (const bad of ["", "abc", "../x", "a".repeat(44)]) expect(await findUsableShare(bad, now)).toBeNull();
    expect(mocks.findUnique).not.toHaveBeenCalled();
  });
});

describe("getActiveParentShare", () => {
  beforeEach(() => vi.clearAllMocks());

  it("asks for this student's newest link that is neither revoked nor expired, and reads no secret (none is stored)", async () => {
    mocks.findFirst.mockResolvedValue(null);
    await getActiveParentShare("u1", now);
    const args = mocks.findFirst.mock.calls[0][0];
    expect(args.where).toEqual({ userId: "u1", revokedAt: null, expiresAt: { gt: now } });
    expect(args.orderBy).toEqual({ createdAt: "desc" });
    expect(Object.keys(args.select).sort()).toEqual(["createdAt", "expiresAt", "lastViewedAt"]);
  });
});

describe("recordShareView", () => {
  beforeEach(() => vi.clearAllMocks());

  it("writes at most once an hour: only when never viewed or last viewed over an hour ago", async () => {
    await recordShareView("s1", now);
    const args = mocks.updateMany.mock.calls[0][0];
    expect(args.where.id).toBe("s1");
    expect(args.where.OR).toEqual([{ lastViewedAt: null }, { lastViewedAt: { lt: new Date(now.getTime() - 3_600_000) } }]);
    expect(args.data).toEqual({ lastViewedAt: now });
  });
});
