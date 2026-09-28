import { describe, expect, it } from "vitest";
import { xpForCorrectAnswer } from "@/lib/gamification/xp";

describe("xpForCorrectAnswer", () => {
  it("awards more XP for harder questions", () => {
    const easy = xpForCorrectAnswer("EASY");
    const medium = xpForCorrectAnswer("MEDIUM");
    const hard = xpForCorrectAnswer("HARD");

    expect(easy).toBeLessThan(medium);
    expect(medium).toBeLessThan(hard);
  });
});
