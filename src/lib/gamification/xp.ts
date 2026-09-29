import type { Difficulty } from "@/generated/prisma/client";

const BASE_XP_BY_DIFFICULTY: Record<Difficulty, number> = {
  EASY: 10,
  MEDIUM: 15,
  HARD: 25,
};

const MAX_STREAK_BONUS = 10;

// Base award scales with difficulty; the streak bonus rewards showing up
// daily (capped so a 100-day streak doesn't dwarf the difficulty itself).
// Kept separate from the write path (src/lib/study/actions.ts) so it stays a
// pure, easily-tested function -- the write path is what makes this
// un-fakeable, by always computing correctness and streak server-side.
export function xpForCorrectAnswer(difficulty: Difficulty, currentStreak = 0): number {
  return BASE_XP_BY_DIFFICULTY[difficulty] + Math.min(currentStreak, MAX_STREAK_BONUS);
}

const XP_PER_FRQ_POINT = 5;

// Only called for pointsAwarded > 0 -- an empty/zero-credit response
// shouldn't earn XP or streak credit (see the call site in study/actions.ts).
export function xpForFrqPoints(pointsAwarded: number, currentStreak = 0): number {
  return pointsAwarded * XP_PER_FRQ_POINT + Math.min(currentStreak, MAX_STREAK_BONUS);
}
