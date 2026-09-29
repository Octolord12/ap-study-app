export interface ReviewState {
  easeFactor: number;
  intervalDays: number;
  lapses: number;
}

export interface NextReview extends ReviewState {
  dueAt: Date;
}

const MIN_EASE_FACTOR = 1.3;
const MAX_EASE_FACTOR = 2.5;

// Simplified SM-2: a miss resets the interval to 1 day and softens the ease
// factor (so a shaky question comes back sooner every time it's missed again);
// a hit grows the interval by the ease factor and nudges it back up. Good
// enough for "resurface what you're weak on" -- not aiming for SM-2's full
// fidelity here.
export function computeNextReview(current: ReviewState, correct: boolean, now: Date = new Date()): NextReview {
  if (!correct) {
    const easeFactor = Math.max(MIN_EASE_FACTOR, current.easeFactor - 0.2);
    const intervalDays = 1;
    return {
      easeFactor,
      intervalDays,
      lapses: current.lapses + 1,
      dueAt: addDays(now, intervalDays),
    };
  }

  const easeFactor = Math.min(MAX_EASE_FACTOR, current.easeFactor + 0.1);
  const intervalDays = Math.max(1, Math.round(current.intervalDays * easeFactor));
  return {
    easeFactor,
    intervalDays,
    lapses: current.lapses,
    dueAt: addDays(now, intervalDays),
  };
}

function addDays(date: Date, days: number): Date {
  const result = new Date(date);
  result.setDate(result.getDate() + days);
  return result;
}
