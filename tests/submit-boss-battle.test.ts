import { beforeEach, describe, expect, it, vi } from "vitest";

// submitBossBattle with the database and session faked. The point is the
// security property: the result comes from stored, server-graded attempts, and
// nothing the browser claims about its own score can change it.

const mocks = vi.hoisted(() => {
  const state = {
    userId: "user-1",
    questionIds: [] as string[],
    attempts: [] as { userId: string; questionId: string; correct: boolean; createdAt: Date }[],
    existing: null as null | { passed: boolean; attemptsCount: number; bestScore: number },
    unitOrder: 2,
  };
  const db = {
    question: { findMany: vi.fn(async () => state.questionIds.map((id) => ({ id }))) },
    questionAttempt: {
      findMany: vi.fn(async ({ where }: { where: { userId: string; questionId: { in: string[] }; createdAt: { gte: Date } } }) =>
        state.attempts.filter(
          (a) => a.userId === where.userId && where.questionId.in.includes(a.questionId) && a.createdAt >= where.createdAt.gte,
        ),
      ),
    },
    bossBattleAttempt: { findUnique: vi.fn(async () => state.existing), upsert: vi.fn(async () => ({})) },
    unit: { findUnique: vi.fn(async () => ({ order: state.unitOrder })) },
  };
  return { state, db, checkAndAwardBadges: vi.fn(async () => []) };
});

vi.mock("@/lib/db", () => ({ getDb: () => mocks.db }));
vi.mock("@/lib/auth/config", () => ({ auth: async () => ({ user: { id: mocks.state.userId } }) }));
vi.mock("@/lib/gamification/badges", () => ({ checkAndAwardBadges: mocks.checkAndAwardBadges }));
vi.mock("@/lib/gamification/activity", () => ({ grantXpForActivity: vi.fn() }));
vi.mock("next/cache", () => ({ revalidatePath: vi.fn() }));
vi.mock("next/navigation", () => ({ redirect: vi.fn() }));

process.env.AUTH_SECRET = "test-secret-not-a-real-one";

import { submitBossBattle } from "@/lib/study/actions";
import { signBossBattle } from "@/lib/study/boss-battle-token";

const SECRET = "test-secret-not-a-real-one";
const QUESTIONS = Array.from({ length: 30 }, (_, i) => `q${i + 1}`);

function tokenFor(overrides: { userId?: string; unitId?: string; startedAtMs?: number } = {}) {
  return signBossBattle({ userId: "user-1", unitId: "unit-1", startedAtMs: Date.now() - 60_000, ...overrides }, SECRET);
}

function answered(correctCount: number, when = new Date()) {
  return QUESTIONS.map((id, i) => ({ userId: "user-1", questionId: id, correct: i < correctCount, createdAt: when }));
}

describe("submitBossBattle", () => {
  beforeEach(() => {
    vi.clearAllMocks();
    mocks.state.userId = "user-1";
    mocks.state.questionIds = QUESTIONS;
    mocks.state.attempts = [];
    mocks.state.existing = null;
  });

  it("scores a battle nobody played as 0, however the request is dressed up", async () => {
    // The old API took { unitId, correctCount, total } from the browser. Send exactly that.
    const forged = { battleToken: tokenFor(), unitId: "unit-1", correctCount: 30, total: 30 } as unknown as { battleToken: string };
    const result = await submitBossBattle(forged);

    expect(result).toMatchObject({ status: "ok", passed: false, correctCount: 0, total: 30, newTitle: null });
    expect(mocks.db.bossBattleAttempt.upsert).toHaveBeenCalledWith(
      expect.objectContaining({ create: expect.objectContaining({ passed: false, bestScore: 0 }) }),
    );
    expect(mocks.checkAndAwardBadges).not.toHaveBeenCalled();
  });

  it("passes on answers the server graded correct during the battle, and awards the title once", async () => {
    mocks.state.attempts = answered(21);
    const result = await submitBossBattle({ battleToken: tokenFor() });

    expect(result).toMatchObject({ status: "ok", passed: true, correctCount: 21, total: 30 });
    expect(result.status === "ok" && result.newTitle).toEqual({ title: "Unit 2 Conqueror", unitNumber: 2 });
    expect(mocks.checkAndAwardBadges).toHaveBeenCalledTimes(1);
  });

  it("fails one answer short of the threshold", async () => {
    mocks.state.attempts = answered(20);
    expect(await submitBossBattle({ battleToken: tokenFor() })).toMatchObject({ status: "ok", passed: false, correctCount: 20 });
  });

  it("does not count answers given before the battle started (earlier practice)", async () => {
    mocks.state.attempts = answered(30, new Date(Date.now() - 3600_000));
    expect(await submitBossBattle({ battleToken: tokenFor({ startedAtMs: Date.now() - 60_000 }) })).toMatchObject({
      status: "ok",
      passed: false,
      correctCount: 0,
    });
  });

  it("does not count someone else's answers", async () => {
    mocks.state.attempts = answered(30).map((a) => ({ ...a, userId: "user-2" }));
    expect(await submitBossBattle({ battleToken: tokenFor() })).toMatchObject({ status: "ok", correctCount: 0, passed: false });
  });

  it("refuses another user's token", async () => {
    mocks.state.attempts = answered(30);
    expect(await submitBossBattle({ battleToken: tokenFor({ userId: "user-2" }) })).toEqual({ status: "invalid" });
    expect(mocks.db.bossBattleAttempt.upsert).not.toHaveBeenCalled();
  });

  it("refuses a forged, edited or expired token and writes nothing", async () => {
    mocks.state.attempts = answered(30);
    const [payload, signature] = tokenFor().split(".");
    const edited = JSON.parse(Buffer.from(payload, "base64url").toString());
    edited.t = 0;
    const earlierStart = `${Buffer.from(JSON.stringify(edited)).toString("base64url")}.${signature}`;
    const expired = tokenFor({ startedAtMs: Date.now() - 5 * 3600_000 });

    expect(await submitBossBattle({ battleToken: "garbage" })).toEqual({ status: "invalid" });
    expect(await submitBossBattle({ battleToken: earlierStart })).toEqual({ status: "invalid" });
    expect(await submitBossBattle({ battleToken: expired })).toEqual({ status: "expired" });
    expect(mocks.db.bossBattleAttempt.upsert).not.toHaveBeenCalled();
  });

  it("keeps a conquered unit conquered after a failed rematch, with no new title", async () => {
    mocks.state.existing = { passed: true, attemptsCount: 1, bestScore: 25 };
    mocks.state.attempts = answered(5);
    const result = await submitBossBattle({ battleToken: tokenFor() });

    expect(result).toMatchObject({ status: "ok", passed: false, correctCount: 5, newTitle: null });
    expect(mocks.db.bossBattleAttempt.upsert).toHaveBeenCalledWith(
      expect.objectContaining({ update: expect.objectContaining({ passed: true, bestScore: 25, attemptsCount: 2 }) }),
    );
  });
});
