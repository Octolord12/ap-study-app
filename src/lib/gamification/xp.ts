import type { Difficulty } from "@/generated/prisma/client";

const BASE_XP_BY_DIFFICULTY: Record<Difficulty, number> = {
  EASY: 10,
  MEDIUM: 15,
  HARD: 25,
};

// The base award for a correct answer, before streak/boss-battle bonuses
// (added in Milestone 5). Kept separate from the write path (route handlers
// in lib/db) so it stays a pure, easily-tested function.
export function xpForCorrectAnswer(difficulty: Difficulty): number {
  return BASE_XP_BY_DIFFICULTY[difficulty];
}
