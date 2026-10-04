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

// "Proficient" needs both: a high score on what the student has tried, and
// enough of the unit tried that the score means something (100% on two
// questions is a start, not mastery). Compared on the rounded percentages the
// student sees, so a unit never reads "80%" and yet is not proficient.
export const PROFICIENT_MIN_ACCURACY = 80;
export const PROFICIENT_MIN_COVERAGE = 50;

export type MasteryLevel = "not-started" | "building" | "proficient";

export interface UnitMasteryTotals {
  total: number; // questions in the unit
  attempted: number; // questions tried at least once
  correct: number; // of those, currently answered correctly
}

export interface UnitMasteryRating {
  level: MasteryLevel;
  accuracyPercent: number | null; // correct / attempted
  coveragePercent: number; // attempted / total
  correctPercent: number; // correct / total: how much of the unit is currently solid
}

const pct = (part: number, whole: number) => (whole > 0 ? Math.round((part / whole) * 100) : 0);

export function rateUnitMastery({ total, attempted, correct }: UnitMasteryTotals): UnitMasteryRating {
  const accuracyPercent = attempted > 0 ? pct(correct, attempted) : null;
  const coveragePercent = pct(attempted, total);
  const correctPercent = pct(correct, total);

  let level: MasteryLevel = "building";
  if (attempted === 0) level = "not-started";
  else if (accuracyPercent !== null && accuracyPercent >= PROFICIENT_MIN_ACCURACY && coveragePercent >= PROFICIENT_MIN_COVERAGE) level = "proficient";

  return { level, accuracyPercent, coveragePercent, correctPercent };
}
