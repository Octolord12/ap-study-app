// How an exam's free-response sections turn into draws. A section is normally one type and a count ("3 SAQ"). A
// section with `kinds` is one stretch of the exam made of several different kinds of question, one prompt of each
// in the order listed (AP Biology's six free-response questions are six different kinds): its prompts are typed
// with the kinds, and the section's own `type` is only the name the exam intro shows.
export interface ExamSectionShape {
  type: string;
  questionCount: number;
  kinds?: readonly string[];
}

export interface ExamDraw {
  type: string;
  count: number;
  // Prefer a unit this section has not used yet (the real exam puts each short question in a different unit).
  spreadUnits: boolean;
}

export function examDraws(sections: readonly ExamSectionShape[]): ExamDraw[] {
  return sections
    .filter((s) => s.type !== "MCQ")
    .flatMap((s): ExamDraw[] =>
      s.kinds?.length ? s.kinds.map((type) => ({ type, count: 1, spreadUnits: true })) : [{ type: s.type, count: s.questionCount, spreadUnits: false }],
    );
}

// The prompt types a course can draw, for checking that every prompt has a place on the exam.
export function drawableTypes(sections: readonly ExamSectionShape[]): string[] {
  return examDraws(sections).map((d) => d.type);
}

// True when the prompts a course has cannot fill its free-response sections (so the exam intro warns that the
// simulation will be short). Supply is counted per prompt type and checked against the draws, not the section's
// own `type`, because a section with `kinds` is made of prompts typed with the kinds.
export function frqSupplyShort(sections: readonly ExamSectionShape[], supplyByType: ReadonlyMap<string, number>): boolean {
  const needed = new Map<string, number>();
  for (const draw of examDraws(sections)) needed.set(draw.type, (needed.get(draw.type) ?? 0) + draw.count);
  return [...needed].some(([type, count]) => (supplyByType.get(type) ?? 0) < count);
}
