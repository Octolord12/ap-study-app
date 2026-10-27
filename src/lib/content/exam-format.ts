// Plain-language description of a course's examFormat JSON (the same data the
// exam simulator reads), for course lists and the landing page.
interface ExamFormatLike {
  totalDurationMinutes: number;
  sections: { type: string; questionCount: number }[];
}

export const SECTION_NAMES: Record<string, string> = {
  MCQ: "multiple choice",
  FRQ: "free response",
  SAQ: "short answer",
  DBQ: "document-based question",
  LEQ: "long essay",
};

export type FrqKind =
  | "FRQ"
  | "SAQ"
  | "DBQ"
  | "LEQ"
  | "RESULTS"
  | "RESULTS_GRAPH"
  | "INVESTIGATION"
  | "CONCEPT"
  | "MODEL"
  | "DATA"
  | "COLLECT_DATA"
  | "ANALYZE_DATA"
  | "INFERENCE"
  | "MULTI_FOCUS";

// AP Biology's six free-response kinds use the College Board's own names; AP Statistics' four are described by what
// each question assesses (the College Board calls them "Multi-Focus on Practices 1 and 2", "3 and 4", "Inference", and "2, 3, and 4").
const FRQ_TITLES: Record<FrqKind, string> = {
  FRQ: "Free response",
  SAQ: "Short answer",
  DBQ: "Document-based question",
  LEQ: "Long essay",
  RESULTS: "Interpreting and evaluating experimental results",
  RESULTS_GRAPH: "Interpreting and evaluating experimental results with graphing",
  INVESTIGATION: "Scientific investigation",
  CONCEPT: "Conceptual analysis",
  MODEL: "Analyzing a model or visual representation",
  DATA: "Analyzing data",
  COLLECT_DATA: "Formulating questions and collecting data",
  ANALYZE_DATA: "Analyzing data and interpreting results",
  INFERENCE: "Inference",
  MULTI_FOCUS: "Multi-focus: collecting, analyzing and interpreting",
};

export function frqTitle(type: string): string {
  return FRQ_TITLES[type as FrqKind] ?? "Free response";
}

export function describeExamFormat(format: ExamFormatLike): string {
  return format.sections.map((s) => `${s.questionCount} ${SECTION_NAMES[s.type] ?? s.type}`).join(", ");
}

export function formatDuration(minutes: number): string {
  const h = Math.floor(minutes / 60);
  const m = minutes % 60;
  if (h === 0) return `${m} min`;
  return m === 0 ? `${h} h` : `${h} h ${m} min`;
}
