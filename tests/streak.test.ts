import { describe, expect, it } from "vitest";
import { updateStreakOnActivity, type StreakState } from "@/lib/gamification/streak";

const day = (n: number) => new Date(`2026-01-${String(n).padStart(2, "0")}T12:00:00Z`);

const FRESH: StreakState = { currentStreak: 0, longestStreak: 0, lastActiveDate: null, streakFreezesAvailable: 1 };

describe("updateStreakOnActivity", () => {
  it("starts a streak at 1 on first-ever activity", () => {
    const result = updateStreakOnActivity(FRESH, day(1));
    expect(result.currentStreak).toBe(1);
    expect(result.longestStreak).toBe(1);
    expect(result.freezeUsed).toBe(false);
  });

  it("is a no-op for a second activity on the same day", () => {
    const afterDay1 = updateStreakOnActivity(FRESH, day(1));
    const result = updateStreakOnActivity(afterDay1, day(1));
    expect(result.currentStreak).toBe(1);
    expect(result.freezeUsed).toBe(false);
  });

  it("extends the streak on a consecutive day", () => {
    const afterDay1 = updateStreakOnActivity(FRESH, day(1));
    const result = updateStreakOnActivity(afterDay1, day(2));
    expect(result.currentStreak).toBe(2);
    expect(result.longestStreak).toBe(2);
  });

  it("bridges a single missed day with a freeze, consuming it", () => {
    const afterDay1 = updateStreakOnActivity(FRESH, day(1));
    const result = updateStreakOnActivity(afterDay1, day(3)); // day 2 skipped
    expect(result.currentStreak).toBe(2);
    expect(result.freezeUsed).toBe(true);
    expect(result.streakFreezesAvailable).toBe(0);
  });

  it("breaks the streak on a single missed day with no freeze available", () => {
    const noFreezeState: StreakState = { ...FRESH, streakFreezesAvailable: 0 };
    const afterDay1 = updateStreakOnActivity(noFreezeState, day(1));
    const result = updateStreakOnActivity(afterDay1, day(3));
    expect(result.currentStreak).toBe(1);
    expect(result.freezeUsed).toBe(false);
  });

  it("breaks the streak on a 2+ day gap even with a freeze available", () => {
    const afterDay1 = updateStreakOnActivity(FRESH, day(1));
    const result = updateStreakOnActivity(afterDay1, day(5));
    expect(result.currentStreak).toBe(1);
    expect(result.streakFreezesAvailable).toBe(1); // untouched
  });

  it("preserves the longest streak after a break", () => {
    let state = updateStreakOnActivity(FRESH, day(1));
    state = updateStreakOnActivity(state, day(2));
    state = updateStreakOnActivity(state, day(3)); // streak of 3
    state = updateStreakOnActivity({ ...state, streakFreezesAvailable: 0 }, day(10)); // big gap, breaks
    expect(state.currentStreak).toBe(1);
    expect(state.longestStreak).toBe(3);
  });
});
