// The exam date and the study plan built from it. Dates are plain "YYYY-MM-DD"
// strings and day counts use UTC calendar arithmetic, so a daylight-saving change
// or the server's timezone can't make a day appear or vanish. "Today" is the
// viewer's own local date, supplied by the browser.

export type IsoDate = string;

export const PLAN_SECONDS_PER_QUESTION = 90; // answering plus reading the explanation
export const CRAM_HINT_DAYS = 14;
export const MAX_EXAM_DATE_DAYS_AHEAD = 800;

const ISO = /^(\d{4})-(\d{2})-(\d{2})$/;

export function parseIsoDate(value: unknown): { y: number; m: number; d: number } | null {
  if (typeof value !== "string") return null;
  const match = ISO.exec(value);
  if (!match) return null;
  const [y, m, d] = [Number(match[1]), Number(match[2]), Number(match[3])];
  const date = new Date(Date.UTC(y, m - 1, d));
  // Rejects 2027-02-30 and the like: JS would roll it over into March.
  if (date.getUTCFullYear() !== y || date.getUTCMonth() !== m - 1 || date.getUTCDate() !== d) return null;
  return { y, m, d };
}

const dayNumber = (iso: IsoDate) => {
  const p = parseIsoDate(iso)!;
  return Date.UTC(p.y, p.m - 1, p.d) / 86_400_000;
};

export function daysBetween(fromIso: IsoDate, toIso: IsoDate): number {
  return Math.round(dayNumber(toIso) - dayNumber(fromIso));
}

export function toIsoDate(date: Date, mode: "local" | "utc" = "local"): IsoDate {
  const [y, m, d] = mode === "local" ? [date.getFullYear(), date.getMonth() + 1, date.getDate()] : [date.getUTCFullYear(), date.getUTCMonth() + 1, date.getUTCDate()];
  return `${String(y).padStart(4, "0")}-${String(m).padStart(2, "0")}-${String(d).padStart(2, "0")}`;
}

export function formatExamDate(iso: IsoDate): string {
  const p = parseIsoDate(iso);
  if (!p) return iso;
  return new Date(Date.UTC(p.y, p.m - 1, p.d)).toLocaleDateString("en-US", { weekday: "long", month: "long", day: "numeric", year: "numeric", timeZone: "UTC" });
}

export type ExamDateCheck = { ok: true; iso: IsoDate } | { ok: false; error: string };

// The server doesn't know the student's timezone, so "not in the past" is checked
// against UTC today minus a day: a date that is today for the student is never refused.
export function validateExamDate(input: unknown, todayUtcIso: IsoDate): ExamDateCheck {
  if (typeof input !== "string" || input.trim() === "") return { ok: false, error: "Pick a date." };
  const iso = input.trim();
  if (!parseIsoDate(iso)) return { ok: false, error: "That isn't a real date." };
  const fromToday = daysBetween(todayUtcIso, iso);
  if (fromToday < -1) return { ok: false, error: "That date has already passed." };
  if (fromToday > MAX_EXAM_DATE_DAYS_AHEAD) return { ok: false, error: "Pick a date within the next two years." };
  return { ok: true, iso };
}

export interface PlanInput {
  examDateIso: IsoDate;
  todayIso: IsoDate;
  totalQuestions: number;
  triedQuestions: number;
  // New (never-tried) questions per day over the last week, from the student's own history.
  newPerDayLast7: number;
}

export type StudyPlan =
  | { kind: "passed"; daysAgo: number }
  | { kind: "exam-day" }
  | { kind: "covered"; daysLeft: number }
  | {
      kind: "plan";
      daysLeft: number;
      untried: number;
      perDay: number;
      minutesPerDay: number;
      pacePerDay: number;
      // "not-started": nothing tried yet, so there is no pace to judge.
      pace: "not-started" | "on-pace" | "behind";
      cramHint: boolean;
    };

export function buildStudyPlan({ examDateIso, todayIso, totalQuestions, triedQuestions, newPerDayLast7 }: PlanInput): StudyPlan {
  const daysLeft = daysBetween(todayIso, examDateIso);
  if (daysLeft < 0) return { kind: "passed", daysAgo: -daysLeft };
  if (daysLeft === 0) return { kind: "exam-day" };

  const untried = Math.max(0, totalQuestions - triedQuestions);
  if (untried === 0) return { kind: "covered", daysLeft };

  // Today counts as a study day; the exam day itself does not.
  const perDay = Math.ceil(untried / daysLeft);
  const pacePerDay = Math.max(0, newPerDayLast7);
  const pace = triedQuestions === 0 ? "not-started" : pacePerDay * daysLeft >= untried ? "on-pace" : "behind";

  return {
    kind: "plan",
    daysLeft,
    untried,
    perDay,
    minutesPerDay: Math.ceil((perDay * PLAN_SECONDS_PER_QUESTION) / 60),
    pacePerDay,
    pace,
    cramHint: daysLeft <= CRAM_HINT_DAYS,
  };
}

// What the exam-date form hands back to the page.
export interface ExamDateState {
  error?: string;
  message?: string;
}
