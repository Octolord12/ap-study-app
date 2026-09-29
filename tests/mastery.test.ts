import { describe, expect, it } from "vitest";
import { computeUnitMastery, type AttemptRecord } from "@/lib/study/mastery";

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
