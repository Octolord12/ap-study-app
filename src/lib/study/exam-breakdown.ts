export interface ExamQuestionResult {
  questionId: string;
  unitSlug: string;
  unitName: string;
  unitOrder: number;
  answered: boolean;
  correct: boolean;
}

export interface ExamWeakUnit {
  unitSlug: string;
  unitName: string;
  unitOrder: number;
  total: number;
  missed: number; // wrong, plus skipped
  missedIds: string[];
}

// Where an exam's multiple-choice points went: units ranked by how many of their
// questions were missed or skipped. Only units with something missed are listed.
export function examWeakUnits(results: ExamQuestionResult[], limit = 5): ExamWeakUnit[] {
  const byUnit = new Map<string, ExamWeakUnit>();
  for (const r of results) {
    const unit = byUnit.get(r.unitSlug) ?? { unitSlug: r.unitSlug, unitName: r.unitName, unitOrder: r.unitOrder, total: 0, missed: 0, missedIds: [] };
    unit.total++;
    if (!r.answered || !r.correct) {
      unit.missed++;
      unit.missedIds.push(r.questionId);
    }
    byUnit.set(r.unitSlug, unit);
  }
  return [...byUnit.values()]
    .filter((u) => u.missed > 0)
    .sort((a, b) => b.missed - a.missed || b.missed / b.total - a.missed / a.total || a.unitOrder - b.unitOrder)
    .slice(0, limit);
}
