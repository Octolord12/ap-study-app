export interface AttemptRecord {
  questionId: string;
  unitId: string;
  correct: boolean;
  createdAt: Date;
}

export interface UnitMastery {
  unitId: string;
  questionsAttempted: number;
  questionsCorrect: number;
}

// Mastery reflects current understanding, not history: a question counts as
// "correct" if the student's most recent attempt at it was correct, even if
// they missed it before. Multiple attempts at the same question count once.
export function computeUnitMastery(attempts: AttemptRecord[]): UnitMastery[] {
  const latestByQuestion = new Map<string, AttemptRecord>();
  for (const attempt of attempts) {
    const existing = latestByQuestion.get(attempt.questionId);
    if (!existing || attempt.createdAt > existing.createdAt) {
      latestByQuestion.set(attempt.questionId, attempt);
    }
  }

  const byUnit = new Map<string, UnitMastery>();
  for (const attempt of latestByQuestion.values()) {
    const entry = byUnit.get(attempt.unitId) ?? { unitId: attempt.unitId, questionsAttempted: 0, questionsCorrect: 0 };
    entry.questionsAttempted += 1;
    if (attempt.correct) entry.questionsCorrect += 1;
    byUnit.set(attempt.unitId, entry);
  }

  return Array.from(byUnit.values());
}
