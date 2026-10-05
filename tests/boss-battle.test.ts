import { describe, expect, it } from "vitest";
import { bossBattleNeeded, hasPassedBossBattle, scoreBossBattle, type ScoredAttempt } from "@/lib/study/boss-battle-rules";
import { BOSS_BATTLE_TOKEN_TTL_MS, signBossBattle, verifyBossBattle } from "@/lib/study/boss-battle-token";

const SECRET = "test-secret-not-a-real-one";
const T0 = Date.UTC(2026, 9, 4, 12, 0, 0);
const start = { userId: "user-1", unitId: "unit-1", startedAtMs: T0 };

describe("pass rule", () => {
  it("needs 70% of the questions, rounded up, with no floating-point surprises", () => {
    expect(bossBattleNeeded(30)).toBe(21);
    expect(bossBattleNeeded(10)).toBe(7);
    expect(bossBattleNeeded(7)).toBe(5);
    expect(bossBattleNeeded(1)).toBe(1);
  });

  it("passes at the threshold and fails one below it", () => {
    expect(hasPassedBossBattle(21, 30)).toBe(true);
    expect(hasPassedBossBattle(20, 30)).toBe(false);
    expect(hasPassedBossBattle(30, 30)).toBe(true);
    expect(hasPassedBossBattle(0, 30)).toBe(false);
  });

  it("never passes a battle with no questions", () => {
    expect(hasPassedBossBattle(0, 0)).toBe(false);
  });
});

describe("scoreBossBattle", () => {
  const ids = ["q1", "q2", "q3"];
  const at = (ms: number) => new Date(T0 + ms);
  const a = (questionId: string, correct: boolean, ms: number): ScoredAttempt => ({ questionId, correct, createdAt: at(ms) });

  it("counts the correct answers given during the battle", () => {
    expect(scoreBossBattle(ids, [a("q1", true, 1000), a("q2", true, 2000), a("q3", false, 3000)], T0)).toBe(2);
  });

  it("counts unanswered questions as not correct", () => {
    expect(scoreBossBattle(ids, [a("q1", true, 1000)], T0)).toBe(1);
    expect(scoreBossBattle(ids, [], T0)).toBe(0);
  });

  it("ignores answers given before the battle started", () => {
    expect(scoreBossBattle(ids, [a("q1", true, -1), a("q2", true, -60_000), a("q3", true, -3_600_000)], T0)).toBe(0);
  });

  it("counts an answer given exactly at the start", () => {
    expect(scoreBossBattle(ids, [a("q1", true, 0)], T0)).toBe(1);
  });

  it("uses only the latest answer on each question", () => {
    expect(scoreBossBattle(ids, [a("q1", true, 1000), a("q1", false, 2000)], T0)).toBe(0);
    expect(scoreBossBattle(ids, [a("q1", false, 1000), a("q1", true, 2000)], T0)).toBe(1);
  });

  it("is not order-dependent", () => {
    expect(scoreBossBattle(ids, [a("q1", false, 2000), a("q1", true, 1000)], T0)).toBe(0);
  });

  it("ignores questions that are not part of the battle", () => {
    expect(scoreBossBattle(ids, [a("other", true, 1000), a("q1", true, 2000)], T0)).toBe(1);
  });
});

describe("boss battle token", () => {
  const now = T0 + 10 * 60 * 1000;

  it("round-trips a battle start", () => {
    const check = verifyBossBattle(signBossBattle(start, SECRET), SECRET, now);
    expect(check).toEqual({ ok: true, start });
  });

  it("rejects a token signed with a different secret", () => {
    expect(verifyBossBattle(signBossBattle(start, "another-secret"), SECRET, now)).toEqual({ ok: false, reason: "invalid" });
  });

  it("rejects a token whose payload was edited (e.g. to move the start time earlier)", () => {
    const [payload, signature] = signBossBattle(start, SECRET).split(".");
    const edited = JSON.parse(Buffer.from(payload, "base64url").toString());
    edited.t = T0 - 24 * 3600 * 1000;
    const forged = `${Buffer.from(JSON.stringify(edited)).toString("base64url")}.${signature}`;
    expect(verifyBossBattle(forged, SECRET, now)).toEqual({ ok: false, reason: "invalid" });
  });

  it("rejects a token whose signature was edited, truncated or removed", () => {
    const token = signBossBattle(start, SECRET);
    const [payload, signature] = token.split(".");
    for (const bad of [`${payload}.${signature.slice(0, -2)}AA`, `${payload}.${signature.slice(0, 10)}`, `${payload}.`, payload, ""]) {
      expect(verifyBossBattle(bad, SECRET, now)).toEqual({ ok: false, reason: "invalid" });
    }
  });

  it("rejects things that are not tokens", () => {
    for (const bad of [undefined, null, 42, {}, "a.b.c", "not a token"]) {
      expect(verifyBossBattle(bad, SECRET, now)).toEqual({ ok: false, reason: "invalid" });
    }
  });

  it("expires after the time limit", () => {
    const token = signBossBattle(start, SECRET);
    expect(verifyBossBattle(token, SECRET, T0 + BOSS_BATTLE_TOKEN_TTL_MS).ok).toBe(true);
    expect(verifyBossBattle(token, SECRET, T0 + BOSS_BATTLE_TOKEN_TTL_MS + 1)).toEqual({ ok: false, reason: "expired" });
  });

  it("rejects a start time far in the future, but tolerates a little clock skew", () => {
    const future = signBossBattle({ ...start, startedAtMs: T0 + 10 * 60 * 1000 }, SECRET);
    expect(verifyBossBattle(future, SECRET, T0)).toEqual({ ok: false, reason: "invalid" });
    const skewed = signBossBattle({ ...start, startedAtMs: T0 + 30 * 1000 }, SECRET);
    expect(verifyBossBattle(skewed, SECRET, T0).ok).toBe(true);
  });
});
