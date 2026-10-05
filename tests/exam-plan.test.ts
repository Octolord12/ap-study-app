import { describe, expect, it } from "vitest";
import {
  CRAM_HINT_DAYS,
  MAX_EXAM_DATE_DAYS_AHEAD,
  PLAN_SECONDS_PER_QUESTION,
  buildStudyPlan,
  daysBetween,
  formatExamDate,
  parseIsoDate,
  toIsoDate,
  validateExamDate,
} from "@/lib/study/exam-plan";

describe("dates", () => {
  it("accepts real dates and rejects everything else", () => {
    expect(parseIsoDate("2027-05-03")).toEqual({ y: 2027, m: 5, d: 3 });
    for (const bad of ["2027-02-30", "2027-13-01", "2027-5-3", "05/03/2027", "", "tomorrow", null, undefined, 20270503, "2027-05-03T00:00"]) {
      expect(parseIsoDate(bad)).toBeNull();
    }
    expect(parseIsoDate("2028-02-29")).not.toBeNull(); // a leap day
    expect(parseIsoDate("2027-02-29")).toBeNull();
  });

  it("counts calendar days, across month ends, leap years and daylight-saving changes", () => {
    expect(daysBetween("2026-10-05", "2026-10-06")).toBe(1);
    expect(daysBetween("2026-10-05", "2027-05-03")).toBe(210);
    expect(daysBetween("2028-02-28", "2028-03-01")).toBe(2);
    expect(daysBetween("2026-11-01", "2026-11-02")).toBe(1); // clocks go back that night
    expect(daysBetween("2027-03-14", "2027-03-15")).toBe(1); // clocks go forward
    expect(daysBetween("2026-10-05", "2026-10-05")).toBe(0);
    expect(daysBetween("2026-10-05", "2026-10-01")).toBe(-4);
  });

  it("formats a date the same way wherever the server or browser is", () => {
    expect(formatExamDate("2027-05-03")).toBe("Monday, May 3, 2027");
  });

  it("builds an ISO date from either the local or the UTC calendar", () => {
    const d = new Date(2026, 9, 5, 23, 30);
    expect(toIsoDate(d, "local")).toBe("2026-10-05");
  });
});

describe("validateExamDate", () => {
  const TODAY = "2026-10-05";

  it("accepts a future date, today, and yesterday (a student ahead of the server's timezone)", () => {
    expect(validateExamDate("2027-05-03", TODAY)).toEqual({ ok: true, iso: "2027-05-03" });
    expect(validateExamDate("2026-10-05", TODAY).ok).toBe(true);
    expect(validateExamDate("2026-10-04", TODAY).ok).toBe(true);
  });

  it("refuses a date that has really passed", () => {
    expect(validateExamDate("2026-10-03", TODAY)).toEqual({ ok: false, error: "That date has already passed." });
  });

  it("refuses a date too far ahead, and nonsense", () => {
    expect(validateExamDate("2030-01-01", TODAY)).toEqual({ ok: false, error: "Pick a date within the next two years." });
    expect(validateExamDate("2026-10-05", "2024-01-01").ok).toBe(false);
    expect(validateExamDate("2027-02-30", TODAY)).toEqual({ ok: false, error: "That isn't a real date." });
    for (const empty of ["", "   ", null, undefined, 5]) expect(validateExamDate(empty, TODAY)).toEqual({ ok: false, error: "Pick a date." });
  });

  it("allows exactly the maximum horizon and not a day more", () => {
    const edge = new Date(Date.UTC(2026, 9, 5) + MAX_EXAM_DATE_DAYS_AHEAD * 86_400_000).toISOString().slice(0, 10);
    const over = new Date(Date.UTC(2026, 9, 5) + (MAX_EXAM_DATE_DAYS_AHEAD + 1) * 86_400_000).toISOString().slice(0, 10);
    expect(validateExamDate(edge, TODAY).ok).toBe(true);
    expect(validateExamDate(over, TODAY).ok).toBe(false);
  });
});

describe("buildStudyPlan", () => {
  const base = { todayIso: "2026-10-05", totalQuestions: 300, triedQuestions: 0, newPerDayLast7: 0 };

  it("says the date has passed, and that it is exam day", () => {
    expect(buildStudyPlan({ ...base, examDateIso: "2026-10-01" })).toEqual({ kind: "passed", daysAgo: 4 });
    expect(buildStudyPlan({ ...base, examDateIso: "2026-10-05" })).toEqual({ kind: "exam-day" });
  });

  it("says everything is covered once every question has been tried", () => {
    expect(buildStudyPlan({ ...base, examDateIso: "2027-05-03", triedQuestions: 300 })).toEqual({ kind: "covered", daysLeft: 210 });
  });

  it("works out questions and minutes per day to try everything once before the exam", () => {
    const plan = buildStudyPlan({ ...base, examDateIso: "2026-11-04", triedQuestions: 60 }); // 30 days left, 240 untried
    expect(plan).toMatchObject({ kind: "plan", daysLeft: 30, untried: 240, perDay: 8 });
    // 8 questions at 90 seconds each = 12 minutes
    expect(plan.kind === "plan" && plan.minutesPerDay).toBe((8 * PLAN_SECONDS_PER_QUESTION) / 60);
  });

  it("rounds the daily number up, so the plan never falls short", () => {
    const plan = buildStudyPlan({ ...base, examDateIso: "2026-10-12", totalQuestions: 20, triedQuestions: 0 }); // 7 days, 20 questions
    expect(plan.kind === "plan" && plan.perDay).toBe(3);
  });

  it("counts today as a study day but not the exam day", () => {
    const plan = buildStudyPlan({ ...base, examDateIso: "2026-10-06", totalQuestions: 10, triedQuestions: 0 }); // exam tomorrow
    expect(plan).toMatchObject({ kind: "plan", daysLeft: 1, perDay: 10 });
  });

  it("does not judge the pace of a student who has not started", () => {
    expect(buildStudyPlan({ ...base, examDateIso: "2027-05-03" })).toMatchObject({ pace: "not-started" });
  });

  it("is on pace when the last week's rate would finish in time, behind when it would not", () => {
    // 240 untried, 30 days left: needs 8 a day.
    const input = { ...base, examDateIso: "2026-11-04", triedQuestions: 60 };
    expect(buildStudyPlan({ ...input, newPerDayLast7: 8 })).toMatchObject({ pace: "on-pace" });
    expect(buildStudyPlan({ ...input, newPerDayLast7: 20 })).toMatchObject({ pace: "on-pace" });
    expect(buildStudyPlan({ ...input, newPerDayLast7: 7.9 })).toMatchObject({ pace: "behind" });
    expect(buildStudyPlan({ ...input, newPerDayLast7: 0 })).toMatchObject({ pace: "behind", pacePerDay: 0 });
  });

  it("suggests cram mode in the last two weeks only", () => {
    const at = (days: number) => {
      const d = new Date(Date.UTC(2026, 9, 5) + days * 86_400_000).toISOString().slice(0, 10);
      return buildStudyPlan({ ...base, examDateIso: d, triedQuestions: 10 });
    };
    expect(at(CRAM_HINT_DAYS)).toMatchObject({ cramHint: true });
    expect(at(CRAM_HINT_DAYS + 1)).toMatchObject({ cramHint: false });
  });

  it("never reports a negative number of untried questions", () => {
    expect(buildStudyPlan({ ...base, examDateIso: "2027-05-03", totalQuestions: 100, triedQuestions: 150 })).toMatchObject({ kind: "covered" });
  });
});
