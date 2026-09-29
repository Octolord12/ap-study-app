import { describe, expect, it } from "vitest";
import { computeLevel } from "@/lib/gamification/level";

describe("computeLevel", () => {
  it("starts at level 1 with 0 XP", () => {
    const result = computeLevel(0);
    expect(result.level).toBe(1);
    expect(result.xpIntoLevel).toBe(0);
    expect(result.xpForNextLevel).toBe(100);
  });

  it("reaches level 2 at exactly 100 XP", () => {
    expect(computeLevel(99).level).toBe(1);
    expect(computeLevel(100).level).toBe(2);
  });

  it("tracks progress within a level", () => {
    const result = computeLevel(150);
    expect(result.level).toBe(2);
    expect(result.xpIntoLevel).toBe(50);
    expect(result.xpForNextLevel).toBe(200); // level 2->3 costs 200
  });

  it("never regresses for increasing XP", () => {
    let lastLevel = 1;
    for (let xp = 0; xp <= 5000; xp += 137) {
      const level = computeLevel(xp).level;
      expect(level).toBeGreaterThanOrEqual(lastLevel);
      lastLevel = level;
    }
  });
});
