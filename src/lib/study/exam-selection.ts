export interface ExamSectionLike {
  type: string;
  questionCount: number;
}

export interface FrqCandidate {
  id: string;
  type: string;
}

// Uniform (Fisher-Yates). `sort(() => Math.random() - 0.5)` looks the same but is biased, and an exam
// draws 55 of ~400 questions, where the bias shows.
export function shuffled<T>(items: readonly T[], random: () => number = Math.random): T[] {
  const result = [...items];
  for (let i = result.length - 1; i > 0; i--) {
    const j = Math.floor(random() * (i + 1));
    [result[i], result[j]] = [result[j], result[i]];
  }
  return result;
}

// One draw per non-multiple-choice section, in the order the exam format lists them, each from the prompts
// of that section's type. If a type has fewer prompts than the section asks for, the exam gets fewer rather
// than failing (validate-content checks the shipped courses never are short). A section with no matching
// type draws nothing: before this existed, a course with no plain "FRQ" section (World History) got
// *every* free-response prompt it had.
export function pickExamFrqIds(sections: readonly ExamSectionLike[], prompts: readonly FrqCandidate[], random: () => number = Math.random): string[] {
  const picked: string[] = [];
  const used = new Set<string>();
  for (const section of sections) {
    if (section.type === "MCQ") continue;
    const pool = prompts.filter((p) => p.type === section.type && !used.has(p.id));
    for (const prompt of shuffled(pool, random).slice(0, section.questionCount)) {
      picked.push(prompt.id);
      used.add(prompt.id);
    }
  }
  return picked;
}
