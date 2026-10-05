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

export type FrqKind = "FRQ" | "SAQ" | "DBQ" | "LEQ";

const FRQ_TITLES: Record<FrqKind, string> = {
  FRQ: "Free response",
  SAQ: "Short answer",
  DBQ: "Document-based question",
  LEQ: "Long essay",
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
