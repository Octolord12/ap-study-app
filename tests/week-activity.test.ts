import { describe, expect, it } from "vitest";
import { MAX_ANSWER_MS, MAX_EXAM_MS, summarizeWeek, toActivityEntries, type ActivityEntry, type LocalDate } from "@/lib/study/week-activity";

const HOUR = 3_600_000;
const DAY = 24 * HOUR;
// A viewer whose local time is UTC-7 (e.g. Pacific daylight time), fixed so tests don't depend on this machine.
const pacific = (ms: number): LocalDate => {
  const d = new Date(ms - 7 * HOUR);
  return { y: d.getUTCFullYear(), m: d.getUTCMonth(), d: d.getUTCDate(), dow: d.getUTCDay() };
};
const utc = (ms: number): LocalDate => pacific(ms + 7 * HOUR);

// Monday 2026-10-05, 20:00 Pacific (= Tuesday 03:00 UTC)
const NOW = Date.UTC(2026, 9, 6, 3, 0, 0);
const q = (at: number, correct = true, ms = 20_000): ActivityEntry => ({ at, kind: "question", correct, ms });

describe("summarizeWeek", () => {
  it("lists seven days oldest first, ending today, labelled by weekday", () => {
    const w = summarizeWeek([], NOW, pacific);
    expect(w.days.map((d) => d.label)).toEqual(["Tue", "Wed", "Thu", "Fri", "Sat", "Sun", "Mon"]);
    expect(w.days.map((d) => d.isToday)).toEqual([false, false, false, false, false, false, true]);
  });

  it("is empty with no activity", () => {
    expect(summarizeWeek([], NOW, pacific)).toMatchObject({ daysStudied: 0, questions: 0, correct: 0, accuracyPercent: null, minutes: 0 });
  });

  it("counts a late-evening answer on the student's own day, not the server's", () => {
    // 9:30pm Monday Pacific is already Tuesday in UTC. For the student it is still Monday.
    const at = Date.UTC(2026, 9, 6, 4, 30, 0);
    const local = summarizeWeek([q(at)], at + 60_000, pacific);
    expect(local.days[6]).toMatchObject({ label: "Mon", questions: 1, active: true });
    const server = summarizeWeek([q(at)], at + 60_000, utc);
    expect(server.days[6]).toMatchObject({ label: "Tue", questions: 1 });
  });

  it("totals days studied, questions, accuracy and minutes", () => {
    const w = summarizeWeek([q(NOW - 1000, true, 60_000), q(NOW - 2000, false, 60_000), q(NOW - DAY, true, 60_000), q(NOW - 3 * DAY, true, 60_000)], NOW, pacific);
    expect(w.daysStudied).toBe(3);
    expect(w.questions).toBe(4);
    expect(w.correct).toBe(3);
    expect(w.accuracyPercent).toBe(75);
    expect(w.minutes).toBe(4);
  });

  it("ignores anything older than seven local days, or in the future", () => {
    const w = summarizeWeek([q(NOW - 7 * DAY), q(NOW - 30 * DAY), q(NOW + HOUR)], NOW, pacific);
    expect(w.questions).toBe(0);
  });

  it("includes the oldest day of the window", () => {
    const w = summarizeWeek([q(NOW - 6 * DAY)], NOW, pacific);
    expect(w.days[0].questions).toBe(1);
  });

  it("caps one answer's time, so a tab left open doesn't count as hours of study", () => {
    const w = summarizeWeek([q(NOW - 1000, true, 5 * HOUR)], NOW, pacific);
    expect(w.minutes).toBe(Math.round(MAX_ANSWER_MS / 60000));
  });

  it("counts a completed exam's length as time, and a free-response answer as a studied day, without touching accuracy", () => {
    const w = summarizeWeek(
      [
        { at: NOW - 1000, kind: "exam", ms: 95 * 60_000 },
        { at: NOW - 2 * DAY, kind: "frq" },
      ],
      NOW,
      pacific,
    );
    expect(w.minutes).toBe(95);
    expect(w.daysStudied).toBe(2);
    expect(w.questions).toBe(0);
    expect(w.accuracyPercent).toBeNull();
  });

  it("does not skip or repeat a day across a daylight-saving change", () => {
    // 2026-11-01 is when US clocks go back. Seven days ending Monday 2026-11-02 must still be seven distinct dates.
    const now = Date.UTC(2026, 10, 3, 3, 0, 0);
    const w = summarizeWeek([], now, (ms) => {
      const offset = ms < Date.UTC(2026, 10, 1, 9, 0, 0) ? 7 : 8;
      const d = new Date(ms - offset * HOUR);
      return { y: d.getUTCFullYear(), m: d.getUTCMonth(), d: d.getUTCDate(), dow: d.getUTCDay() };
    });
    expect(w.days.map((d) => d.label)).toEqual(["Tue", "Wed", "Thu", "Fri", "Sat", "Sun", "Mon"]);
  });
});

describe("toActivityEntries", () => {
  it("turns stored records into entries, using the exam's completion time and length", () => {
    const entries = toActivityEntries({
      questions: [{ createdAt: new Date(1000), correct: true, timeSpentMs: 5000 }],
      frqs: [{ createdAt: new Date(2000) }],
      exams: [{ startedAt: new Date(10_000), completedAt: new Date(70_000) }],
    });
    expect(entries).toEqual([
      { at: 1000, kind: "question", correct: true, ms: 5000 },
      { at: 2000, kind: "frq" },
      { at: 70_000, kind: "exam", ms: 60_000 },
    ]);
  });

  it("caps an exam that sat open, and ignores a negative length", () => {
    const [capped, negative] = toActivityEntries({
      questions: [],
      frqs: [],
      exams: [
        { startedAt: new Date(0), completedAt: new Date(100 * HOUR) },
        { startedAt: new Date(5000), completedAt: new Date(1000) },
      ],
    });
    expect(capped.ms).toBe(MAX_EXAM_MS);
    expect(negative.ms).toBe(0);
  });
});
