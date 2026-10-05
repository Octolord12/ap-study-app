// Pure rules for scoring a boss battle. The score is never taken from the
// browser: it is counted from the stored, server-graded QuestionAttempt rows
// (see submitBossBattle in actions.ts). No server-only imports here, so the
// client runner can share the pass threshold.

export const BOSS_BATTLE_PASS_PERCENT = 70;

export function bossBattleNeeded(total: number): number {
  // Integer math: total * 0.7 can land a hair above a whole number in floating point.
  return Math.ceil((total * BOSS_BATTLE_PASS_PERCENT) / 100);
}

export function hasPassedBossBattle(correct: number, total: number): boolean {
  return total > 0 && correct >= bossBattleNeeded(total);
}

export interface ScoredAttempt {
  questionId: string;
  correct: boolean;
  createdAt: Date;
}

// How many of the battle's questions the student currently has right *in this
// battle*: the latest attempt on each question, at or after the moment the
// battle started. Earlier practice doesn't count, an unanswered question counts
// as not correct, and a later wrong answer replaces an earlier right one.
export function scoreBossBattle(questionIds: string[], attempts: ScoredAttempt[], startedAtMs: number): number {
  const inBattle = new Set(questionIds);
  const latest = new Map<string, ScoredAttempt>();
  for (const attempt of attempts) {
    if (!inBattle.has(attempt.questionId) || attempt.createdAt.getTime() < startedAtMs) continue;
    const seen = latest.get(attempt.questionId);
    if (!seen || attempt.createdAt > seen.createdAt) latest.set(attempt.questionId, attempt);
  }
  let correct = 0;
  for (const attempt of latest.values()) if (attempt.correct) correct++;
  return correct;
}
