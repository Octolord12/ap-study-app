// "Last 7 days" on the Progress page: what was done, and when. Pure so the
// day-bucketing can be tested; the page hands the raw timestamps to the browser
// and the browser buckets them, because "today" is the student's local day, not
// the server's (a student studying at 9pm Pacific is already "tomorrow" in UTC).

export interface ActivityEntry {
  at: number; // ms since epoch
  kind: "question" | "frq" | "exam";
  correct?: boolean; // question only
  ms?: number; // time spent: per question answered, or the length of a completed exam
}

export interface LocalDate {
  y: number;
  m: number; // 0-11
  d: number;
  dow: number; // 0 = Sunday
}

export const MAX_ANSWER_MS = 10 * 60 * 1000;
const WEEKDAYS = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];

export function browserLocalDate(ms: number): LocalDate {
  const date = new Date(ms);
  return { y: date.getFullYear(), m: date.getMonth(), d: date.getDate(), dow: date.getDay() };
}

const key = (l: { y: number; m: number; d: number }) => l.y * 10000 + (l.m + 1) * 100 + l.d;

export interface DayActivity {
  label: string;
  isToday: boolean;
  questions: number;
  active: boolean;
}

export interface WeekSummary {
  days: DayActivity[]; // oldest first, today last
  daysStudied: number;
  questions: number;
  correct: number;
  accuracyPercent: number | null;
  minutes: number;
}

export function summarizeWeek(entries: ActivityEntry[], nowMs: number, localDate: (ms: number) => LocalDate = browserLocalDate): WeekSummary {
  const today = localDate(nowMs);
  // Calendar arithmetic on a noon-UTC date, so a daylight-saving change can't skip or repeat a day.
  const days = Array.from({ length: 7 }, (_, i) => {
    const back = 6 - i;
    const cal = new Date(Date.UTC(today.y, today.m, today.d - back, 12));
    return { y: cal.getUTCFullYear(), m: cal.getUTCMonth(), d: cal.getUTCDate(), dow: cal.getUTCDay() };
  });
  const index = new Map(days.map((day, i) => [key(day), i]));

  const out: DayActivity[] = days.map((day, i) => ({ label: WEEKDAYS[day.dow], isToday: i === 6, questions: 0, active: false }));
  let questions = 0;
  let correct = 0;
  let ms = 0;

  for (const entry of entries) {
    if (entry.at > nowMs) continue;
    const i = index.get(key(localDate(entry.at)));
    if (i === undefined) continue;
    out[i].active = true;
    if (entry.kind === "question") {
      out[i].questions++;
      questions++;
      if (entry.correct) correct++;
    }
    if (entry.ms && entry.ms > 0) ms += entry.kind === "question" ? Math.min(entry.ms, MAX_ANSWER_MS) : entry.ms;
  }

  return {
    days: out,
    daysStudied: out.filter((d) => d.active).length,
    questions,
    correct,
    accuracyPercent: questions > 0 ? Math.round((correct / questions) * 100) : null,
    minutes: Math.round(ms / 60000),
  };
}

// An exam is auto-submitted at its time limit, so a longer gap means it sat open.
export const MAX_EXAM_MS = 4 * 60 * 60 * 1000;

export function toActivityEntries(records: {
  questions: { createdAt: Date; correct: boolean; timeSpentMs: number }[];
  frqs: { createdAt: Date }[];
  exams: { startedAt: Date; completedAt: Date }[];
}): ActivityEntry[] {
  return [
    ...records.questions.map((q): ActivityEntry => ({ at: q.createdAt.getTime(), kind: "question", correct: q.correct, ms: q.timeSpentMs })),
    ...records.frqs.map((f): ActivityEntry => ({ at: f.createdAt.getTime(), kind: "frq" })),
    ...records.exams.map(
      (e): ActivityEntry => ({
        at: e.completedAt.getTime(),
        kind: "exam",
        ms: Math.min(Math.max(0, e.completedAt.getTime() - e.startedAt.getTime()), MAX_EXAM_MS),
      }),
    ),
  ];
}

// Kept out of components: they must not call Date.now() while rendering.
export function daysAgo(days: number): Date {
  return new Date(Date.now() - days * 24 * 60 * 60 * 1000);
}
