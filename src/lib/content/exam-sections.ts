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
