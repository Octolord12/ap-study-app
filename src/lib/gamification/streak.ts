export interface StreakState {
  currentStreak: number;
  longestStreak: number;
  lastActiveDate: Date | null;
  streakFreezesAvailable: number;
}

export interface StreakUpdate extends StreakState {
  freezeUsed: boolean;
}

function daysBetween(a: Date, b: Date): number {
  const msPerDay = 24 * 60 * 60 * 1000;
  const utcA = Date.UTC(a.getFullYear(), a.getMonth(), a.getDate());
  const utcB = Date.UTC(b.getFullYear(), b.getMonth(), b.getDate());
  return Math.round((utcB - utcA) / msPerDay);
}

// Called once per day's first activity (not on every question answered --
// callers should skip this if daysBetween(lastActiveDate, today) === 0).
// A single skipped day auto-consumes a streak freeze if one's available;
// anything longer breaks the streak. This updates state incrementally
// rather than recomputing from full history, so there's no ambiguity about
// which past gap a freeze already covered -- see the gotcha in CLAUDE.md.
export function updateStreakOnActivity(state: StreakState, today: Date): StreakUpdate {
  if (!state.lastActiveDate) {
    return {
      currentStreak: 1,
      longestStreak: Math.max(state.longestStreak, 1),
      lastActiveDate: today,
      streakFreezesAvailable: state.streakFreezesAvailable,
      freezeUsed: false,
    };
  }

  const gap = daysBetween(state.lastActiveDate, today);

  if (gap <= 0) {
    // Same day (or a clock going backwards, which we treat as a no-op).
    return { ...state, freezeUsed: false };
  }

  if (gap === 1) {
    const currentStreak = state.currentStreak + 1;
    return {
      currentStreak,
      longestStreak: Math.max(state.longestStreak, currentStreak),
      lastActiveDate: today,
      streakFreezesAvailable: state.streakFreezesAvailable,
      freezeUsed: false,
    };
  }

  if (gap === 2 && state.streakFreezesAvailable > 0) {
    const currentStreak = state.currentStreak + 1;
    return {
      currentStreak,
      longestStreak: Math.max(state.longestStreak, currentStreak),
      lastActiveDate: today,
      streakFreezesAvailable: state.streakFreezesAvailable - 1,
      freezeUsed: true,
    };
  }

  return {
    currentStreak: 1,
    longestStreak: state.longestStreak,
    lastActiveDate: today,
    streakFreezesAvailable: state.streakFreezesAvailable,
    freezeUsed: false,
  };
}

// What to *show* as the streak right now. currentStreak is only rewritten
// when the student next does something, so after a long gap it still holds
// the old run -- showing it would claim a streak that the next activity is
// about to reset. Mirrors updateStreakOnActivity: a one-day gap continues the
// run, and a two-day gap continues it only if a freeze is available to spend.
export function displayStreak(state: StreakState, now: Date): number {
  if (!state.lastActiveDate || state.currentStreak <= 0) return 0;
  const gap = daysBetween(state.lastActiveDate, now);
  if (gap <= 1) return state.currentStreak;
  if (gap === 2 && state.streakFreezesAvailable > 0) return state.currentStreak;
  return 0;
}

export function wasActiveToday(lastActiveDate: Date | null, now: Date): boolean {
  return lastActiveDate !== null && daysBetween(lastActiveDate, now) === 0;
}
