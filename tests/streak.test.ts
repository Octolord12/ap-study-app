import { describe, expect, it } from "vitest";
import { displayStreak, updateStreakOnActivity, wasActiveToday, type StreakState } from "@/lib/gamification/streak";

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

describe("displayStreak", () => {
  const run = (lastActiveDate: Date | null, streakFreezesAvailable = 1): StreakState => ({
    currentStreak: 12,
    longestStreak: 12,
    lastActiveDate,
    streakFreezesAvailable,
  });

  it("shows the stored streak on the day of activity and the day after", () => {
    expect(displayStreak(run(day(5)), day(5))).toBe(12);
    expect(displayStreak(run(day(5)), day(6))).toBe(12);
  });

  it("keeps showing the streak across a single missed day only while a freeze is left", () => {
    expect(displayStreak(run(day(5), 1), day(7))).toBe(12);
    expect(displayStreak(run(day(5), 0), day(7))).toBe(0);
  });

  it("shows nothing once the run is broken, even though the stored value is unchanged", () => {
    expect(displayStreak(run(day(5)), day(9))).toBe(0);
  });

  it("shows nothing for a student who never started", () => {
    expect(displayStreak(FRESH, day(1))).toBe(0);
    expect(displayStreak({ ...FRESH, currentStreak: 3 }, day(1))).toBe(0);
  });
});

describe("wasActiveToday", () => {
  it("is true only for the same calendar day", () => {
    expect(wasActiveToday(day(5), day(5))).toBe(true);
    expect(wasActiveToday(day(5), day(6))).toBe(false);
    expect(wasActiveToday(null, day(6))).toBe(false);
  });
});
