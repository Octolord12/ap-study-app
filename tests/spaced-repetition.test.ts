import { describe, expect, it } from "vitest";
import { computeNextReview } from "@/lib/study/spaced-repetition";

const NOW = new Date("2026-01-01T00:00:00Z");

describe("computeNextReview", () => {
  it("schedules a miss for tomorrow and softens the ease factor", () => {
    const result = computeNextReview({ easeFactor: 2.5, intervalDays: 6, lapses: 0 }, false, NOW);
    expect(result.intervalDays).toBe(1);
    expect(result.easeFactor).toBeCloseTo(2.3);
    expect(result.lapses).toBe(1);
    expect(result.dueAt.toISOString()).toBe("2026-01-02T00:00:00.000Z");
  });

  it("never drops the ease factor below the floor", () => {
    const result = computeNextReview({ easeFactor: 1.35, intervalDays: 1, lapses: 3 }, false, NOW);
    expect(result.easeFactor).toBeCloseTo(1.3);
  });

  it("grows the interval and ease factor on a hit", () => {
    const result = computeNextReview({ easeFactor: 2.0, intervalDays: 4, lapses: 1 }, true, NOW);
    expect(result.intervalDays).toBe(8); // round(4 * 2.0)
    expect(result.easeFactor).toBeCloseTo(2.1);
    expect(result.lapses).toBe(1); // unchanged on a hit
  });

  it("never grows the ease factor past the ceiling", () => {
    const result = computeNextReview({ easeFactor: 2.45, intervalDays: 2, lapses: 0 }, true, NOW);
    expect(result.easeFactor).toBeCloseTo(2.5);
  });

  it("always produces at least a 1-day interval on a hit from a fresh question", () => {
    const result = computeNextReview({ easeFactor: 2.5, intervalDays: 1, lapses: 0 }, true, NOW);
    expect(result.intervalDays).toBeGreaterThanOrEqual(1);
  });
});
