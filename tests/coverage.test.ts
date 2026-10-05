import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";

const mocks = vi.hoisted(() => ({
  total: 300,
  rows: [] as { questionId: string; _min: { createdAt: Date | null } }[],
  db: { question: { count: vi.fn() }, questionAttempt: { groupBy: vi.fn() } },
}));
mocks.db.question.count.mockImplementation(async () => mocks.total);
mocks.db.questionAttempt.groupBy.mockImplementation(async () => mocks.rows);
vi.mock("@/lib/db", () => ({ getDb: () => mocks.db }));

import { getCourseCoverage } from "@/lib/study/coverage";

const NOW = new Date("2026-10-05T12:00:00Z").getTime();
const DAY = 86_400_000;
const row = (id: string, firstTriedDaysAgo: number | null) => ({ questionId: id, _min: { createdAt: firstTriedDaysAgo === null ? null : new Date(NOW - firstTriedDaysAgo * DAY) } });

describe("getCourseCoverage", () => {
  beforeEach(() => {
    vi.useFakeTimers();
    vi.setSystemTime(NOW);
    mocks.total = 300;
    mocks.rows = [];
  });
  afterEach(() => vi.useRealTimers());

  it("reports the course size, how many questions were tried, and the new-per-day rate over the last week", async () => {
    // Tried for the first time 1, 3 and 6 days ago (this week), and 8 and 40 days ago (earlier).
    mocks.rows = [row("a", 1), row("b", 3), row("c", 6), row("d", 8), row("e", 40)];
    expect(await getCourseCoverage("u1", "c1")).toEqual({ total: 300, tried: 5, newPerDayLast7: 3 / 7 });
  });

  it("asks only about this student's attempts in this course", async () => {
    await getCourseCoverage("u1", "c1");
    expect(mocks.db.question.count).toHaveBeenCalledWith({ where: { courseId: "c1" } });
    expect(mocks.db.questionAttempt.groupBy).toHaveBeenCalledWith(expect.objectContaining({ where: { userId: "u1", question: { courseId: "c1" } } }));
  });

  it("counts a question by when it was first tried, so re-answering an old one is not 'new'", async () => {
    // First tried 30 days ago; whatever was answered since, its earliest attempt is what counts.
    mocks.rows = [row("a", 30)];
    expect((await getCourseCoverage("u1", "c1")).newPerDayLast7).toBe(0);
  });

  it("handles a student who has tried nothing, and tolerates a missing timestamp", async () => {
    expect(await getCourseCoverage("u1", "c1")).toEqual({ total: 300, tried: 0, newPerDayLast7: 0 });
    mocks.rows = [row("a", null)];
    expect(await getCourseCoverage("u1", "c1")).toMatchObject({ tried: 1, newPerDayLast7: 0 });
  });
});
