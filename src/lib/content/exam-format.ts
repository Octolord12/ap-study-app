// Plain-language description of a course's examFormat JSON (the same data the
// exam simulator reads), for course lists and the landing page. Only MCQ and
// FRQ sections get a count: for the World History item types (SAQ/DBQ/LEQ)
// the count in the data is a slot count, not something worth printing.
interface ExamFormatLike {
  totalDurationMinutes: number;
  sections: { type: string; questionCount: number }[];
}

const NAMES: Record<string, string> = {
  MCQ: "multiple choice",
  FRQ: "free response",
  SAQ: "short answer",
  DBQ: "document-based question",
  LEQ: "long essay",
};

export function describeExamFormat(format: ExamFormatLike): string {
  return format.sections
    .map((s) => (s.type === "MCQ" || s.type === "FRQ" ? `${s.questionCount} ${NAMES[s.type]}` : (NAMES[s.type] ?? s.type)))
    .join(", ");
}

export function formatDuration(minutes: number): string {
  const h = Math.floor(minutes / 60);
  const m = minutes % 60;
  if (h === 0) return `${m} min`;
  return m === 0 ? `${h} h` : `${h} h ${m} min`;
}
