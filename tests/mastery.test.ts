import { describe, expect, it } from "vitest";
import { computeUnitMastery, rateUnitMastery, type AttemptRecord } from "@/lib/study/mastery";

function attempt(overrides: Partial<AttemptRecord>): AttemptRecord {
  return { questionId: "q1", unitId: "u1", correct: true, createdAt: new Date("2026-01-01"), ...overrides };
}

describe("computeUnitMastery", () => {
  it("counts a single attempt", () => {
    const result = computeUnitMastery([attempt({ correct: true })]);
    expect(result).toEqual([{ unitId: "u1", questionsAttempted: 1, questionsCorrect: 1 }]);
  });

  it("only counts the latest attempt per question", () => {
    const result = computeUnitMastery([
      attempt({ questionId: "q1", correct: false, createdAt: new Date("2026-01-01") }),
      attempt({ questionId: "q1", correct: true, createdAt: new Date("2026-01-02") }),
    ]);
    expect(result).toEqual([{ unitId: "u1", questionsAttempted: 1, questionsCorrect: 1 }]);
  });

  it("does not let an earlier correct attempt mask a later miss", () => {
    const result = computeUnitMastery([
      attempt({ questionId: "q1", correct: true, createdAt: new Date("2026-01-01") }),
      attempt({ questionId: "q1", correct: false, createdAt: new Date("2026-01-02") }),
    ]);
    expect(result).toEqual([{ unitId: "u1", questionsAttempted: 1, questionsCorrect: 0 }]);
  });

  it("groups by unit", () => {
    const result = computeUnitMastery([
      attempt({ questionId: "q1", unitId: "u1", correct: true }),
      attempt({ questionId: "q2", unitId: "u2", correct: false }),
    ]);
    expect(result).toHaveLength(2);
    expect(result).toContainEqual({ unitId: "u1", questionsAttempted: 1, questionsCorrect: 1 });
    expect(result).toContainEqual({ unitId: "u2", questionsAttempted: 1, questionsCorrect: 0 });
  });

  it("returns an empty array for no attempts", () => {
    expect(computeUnitMastery([])).toEqual([]);
  });
});

describe("rateUnitMastery", () => {
  it("is not started with no attempts", () => {
    expect(rateUnitMastery({ total: 30, attempted: 0, correct: 0 })).toEqual({
      level: "not-started",
      accuracyPercent: null,
      coveragePercent: 0,
      correctPercent: 0,
    });
  });

  it("is proficient at 80% accuracy over half the unit", () => {
    const r = rateUnitMastery({ total: 30, attempted: 15, correct: 12 });
    expect(r.level).toBe("proficient");
    expect(r.accuracyPercent).toBe(80);
    expect(r.coveragePercent).toBe(50);
    expect(r.correctPercent).toBe(40);
  });

  it("is still building when accuracy is high but little of the unit has been tried", () => {
    expect(rateUnitMastery({ total: 30, attempted: 2, correct: 2 }).level).toBe("building");
  });

  it("is still building when the whole unit is tried but accuracy is below 80%", () => {
    expect(rateUnitMastery({ total: 30, attempted: 30, correct: 23 }).level).toBe("building");
  });

  it("judges on the rounded percentage the student sees", () => {
    // 79.6% shows as 80%, so it must count as proficient.
    expect(rateUnitMastery({ total: 10, attempted: 10, correct: 8 }).level).toBe("proficient");
    expect(rateUnitMastery({ total: 500, attempted: 250, correct: 199 }).accuracyPercent).toBe(80);
    expect(rateUnitMastery({ total: 500, attempted: 250, correct: 199 }).level).toBe("proficient");
  });

  it("does not divide by zero for a unit with no questions", () => {
    expect(rateUnitMastery({ total: 0, attempted: 0, correct: 0 })).toEqual({
      level: "not-started",
      accuracyPercent: null,
      coveragePercent: 0,
      correctPercent: 0,
    });
  });
});
