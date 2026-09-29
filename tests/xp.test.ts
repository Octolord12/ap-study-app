import { describe, expect, it } from "vitest";
import { xpForCorrectAnswer, xpForFrqPoints } from "@/lib/gamification/xp";

describe("xpForCorrectAnswer", () => {
  it("awards more XP for harder questions", () => {
    const easy = xpForCorrectAnswer("EASY");
    const medium = xpForCorrectAnswer("MEDIUM");
    const hard = xpForCorrectAnswer("HARD");

    expect(easy).toBeLessThan(medium);
    expect(medium).toBeLessThan(hard);
  });

  it("adds a bonus for an active streak", () => {
    const noStreak = xpForCorrectAnswer("EASY", 0);
    const fiveDayStreak = xpForCorrectAnswer("EASY", 5);
    expect(fiveDayStreak).toBe(noStreak + 5);
  });

  it("caps the streak bonus", () => {
    const cappedStreak = xpForCorrectAnswer("EASY", 10);
    const hugeStreak = xpForCorrectAnswer("EASY", 500);
    expect(hugeStreak).toBe(cappedStreak);
  });
});

describe("xpForFrqPoints", () => {
  it("scales with points awarded", () => {
    expect(xpForFrqPoints(1)).toBeLessThan(xpForFrqPoints(3));
  });

  it("adds the same capped streak bonus as MCQs", () => {
    expect(xpForFrqPoints(2, 5)).toBe(xpForFrqPoints(2, 0) + 5);
    expect(xpForFrqPoints(2, 500)).toBe(xpForFrqPoints(2, 10));
  });
});
