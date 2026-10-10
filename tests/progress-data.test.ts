import { beforeEach, describe, expect, it, vi } from "vitest";

// loadProgressCore feeds both the student's Progress page and the parent's page. This runs it against a fake database holding known answers,
// so a wiring slip (the wrong unit, the wrong user, the wrong week) shows up here, not as wrong numbers on someone's screen.

const DAY = 86_400_000;
const mocks = vi.hoisted(() => ({
  enrollmentFindMany: vi.fn(),
  attemptFindMany: vi.fn(),
  frqFindMany: vi.fn(),
  examFindMany: vi.fn(),
  stats: vi.fn(),
}));

vi.mock("@/lib/db", () => ({
  getDb: () => ({
    enrollment: { findMany: mocks.enrollmentFindMany },
    questionAttempt: { findMany: mocks.attemptFindMany },
    fRQAttempt: { findMany: mocks.frqFindMany },
    examAttempt: { findMany: mocks.examFindMany },
  }),
}));
vi.mock("@/lib/gamification/queries", () => ({ getUserGamificationStats: mocks.stats }));

import { describeCourseAccuracy, loadProgressCore } from "@/lib/study/progress-data";

const topic = { id: "t1", name: "Limits at Infinity", slug: "limits-at-infinity" };
const unit1 = { slug: "unit-1", name: "Limits and Continuity", course: { slug: "ap-calc", name: "AP Calculus AB" } };
const attempt = (questionId: string, correct: boolean, daysAgo: number) => ({
  questionId,
  correct,
  createdAt: new Date(Date.now() - daysAgo * DAY),
  timeSpentMs: 20_000,
  question: { unitId: "u1", topic, unit: unit1 },
});

describe("loadProgressCore", () => {
  beforeEach(() => {
    vi.clearAllMocks();
    mocks.stats.mockResolvedValue({ level: 3, totalXp: 250, currentStreak: 2 });
    mocks.enrollmentFindMany.mockResolvedValue([
      {
        course: {
          id: "c1",
          slug: "ap-calc",
          name: "AP Calculus AB",
          units: [
            { id: "u1", slug: "unit-1", name: "Limits and Continuity", _count: { questions: 30 } },
            { id: "u2", slug: "unit-2", name: "Differentiation", _count: { questions: 45 } },
          ],
        },
      },
    ]);
    const all = [attempt("q1", true, 20), attempt("q2", false, 20), attempt("q3", false, 1), attempt("q4", true, 1)];
    // The loader asks twice: for every attempt (no date filter) and for the last 8 days (with one).
    mocks.attemptFindMany.mockImplementation(async ({ where }: { where: { createdAt?: { gte: Date } } }) =>
      where.createdAt ? all.filter((a) => a.createdAt >= where.createdAt!.gte) : all,
    );
    mocks.frqFindMany.mockResolvedValue([{ createdAt: new Date(Date.now() - DAY) }]);
    mocks.examFindMany.mockResolvedValue([{ startedAt: new Date(Date.now() - 2 * DAY), completedAt: new Date(Date.now() - 2 * DAY + 600_000) }]);
  });

  it("asks only for this student's rows, in every query", async () => {
    await loadProgressCore("u-7");
    expect(mocks.enrollmentFindMany.mock.calls[0][0].where).toEqual({ userId: "u-7" });
    for (const call of mocks.attemptFindMany.mock.calls) expect(call[0].where.userId).toBe("u-7");
    expect(mocks.frqFindMany.mock.calls[0][0].where.userId).toBe("u-7");
    expect(mocks.examFindMany.mock.calls[0][0].where.userId).toBe("u-7");
    expect(mocks.stats).toHaveBeenCalledWith("u-7");
  });

  it("builds each course's unit rows from the attempts: tried and correct per unit, with the unit's question total", async () => {
    const { courses } = await loadProgressCore("u1");
    expect(courses).toHaveLength(1);
    expect(courses[0].units).toEqual([
      { id: "u1", slug: "unit-1", name: "Limits and Continuity", total: 30, attempted: 4, correct: 2 },
      { id: "u2", slug: "unit-2", name: "Differentiation", total: 45, attempted: 0, correct: 0 },
    ]);
    expect(courses[0].totalAttempted).toBe(4);
    expect(courses[0].totalCorrect).toBe(2);
  });

  it("lists a topic as weak when it was tried enough and is under the proficiency line", async () => {
    const { weakest } = await loadProgressCore("u1");
    expect(weakest).toHaveLength(1);
    expect(weakest[0]).toMatchObject({ topicId: "t1", topicName: "Limits at Infinity", unitName: "Limits and Continuity", courseName: "AP Calculus AB", accuracyPercent: 50 });
  });

  it("includes only the last week's activity in the week entries (question, free-response and exam)", async () => {
    const { weekEntries } = await loadProgressCore("u1");
    expect(weekEntries.length).toBe(2 /* q3, q4 */ + 1 /* frq */ + 1 /* exam */);
  });

  it("passes the gamification stats through unchanged", async () => {
    expect((await loadProgressCore("u1")).stats).toEqual({ level: 3, totalXp: 250, currentStreak: 2 });
  });

  it("handles a student who has started nothing", async () => {
    mocks.enrollmentFindMany.mockResolvedValue([]);
    mocks.attemptFindMany.mockResolvedValue([]);
    mocks.frqFindMany.mockResolvedValue([]);
    mocks.examFindMany.mockResolvedValue([]);
    const core = await loadProgressCore("u1");
    expect(core.courses).toEqual([]);
    expect(core.weakest).toEqual([]);
    expect(core.weekEntries).toEqual([]);
  });
});

describe("describeCourseAccuracy", () => {
  it("states the percentage and the count, or that nothing has been attempted", () => {
    expect(describeCourseAccuracy(7, 10)).toBe("70% correct across 10 questions.");
    expect(describeCourseAccuracy(1, 1)).toBe("100% correct across 1 question.");
    expect(describeCourseAccuracy(0, 0)).toBe("No questions attempted yet.");
  });
});
