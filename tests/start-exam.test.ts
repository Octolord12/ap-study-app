import { beforeEach, describe, expect, it, vi } from "vitest";

// startExam with the database faked. The fake returns only the columns a query selects, so a query that forgets to ask for a
// question's unit gets no unit back, which is what makes the weighting silently turn into a uniform draw.

const mocks = vi.hoisted(() => {
  type Row = Record<string, unknown>;
  const state = {
    userId: "user-1",
    course: { id: "c1", examFormat: {} as unknown },
    units: [] as Row[],
    questions: [] as Row[],
    prompts: [] as Row[],
    created: [] as Row[],
  };
  const project = (rows: Row[], select?: Record<string, boolean>) =>
    rows.map((row) => (select ? Object.fromEntries(Object.keys(select).filter((k) => select[k]).map((k) => [k, row[k]])) : row));
  const db = {
    course: { findUnique: vi.fn(async () => state.course) },
    question: { findMany: vi.fn(async ({ select }: { select?: Record<string, boolean> }) => project(state.questions, select)) },
    fRQPrompt: { findMany: vi.fn(async ({ select }: { select?: Record<string, boolean> }) => project(state.prompts, select)) },
    unit: { findMany: vi.fn(async ({ select }: { select?: Record<string, boolean> }) => project(state.units, select)) },
    examAttempt: {
      create: vi.fn(async ({ data }: { data: Row }) => {
        state.created.push(data);
        return { id: "attempt-1" };
      }),
    },
  };
  return { state, db, redirect: vi.fn() };
});

vi.mock("@/lib/db", () => ({ getDb: () => mocks.db }));
vi.mock("@/lib/auth/config", () => ({ auth: async () => ({ user: { id: mocks.state.userId } }) }));
vi.mock("@/lib/gamification/badges", () => ({ checkAndAwardBadges: vi.fn(async () => []) }));
vi.mock("@/lib/gamification/activity", () => ({ grantXpForActivity: vi.fn() }));
vi.mock("next/cache", () => ({ revalidatePath: vi.fn() }));
vi.mock("next/navigation", () => ({ redirect: mocks.redirect }));

import { startExam } from "@/lib/study/actions";

const rows = (unitId: string, prefix: string, n: number, extra: Record<string, unknown> = {}) =>
  Array.from({ length: n }, (_, i) => ({ id: `${prefix}${i}`, unitId, ...extra }));

describe("startExam", () => {
  beforeEach(() => {
    vi.clearAllMocks();
    mocks.state.created = [];
    mocks.state.course = {
      id: "c1",
      examFormat: { sections: [{ type: "MCQ", questionCount: 12 }, { type: "FRQ", questionCount: 2 }] },
    };
    // Unit A is 10-20% (weight 30), unit B 5-5% (weight 10): three quarters of an exam, then, comes from A.
    mocks.state.units = [{ id: "A", weightingMin: 10, weightingMax: 20 }, { id: "B", weightingMin: 5, weightingMax: 5 }];
    mocks.state.questions = [...rows("A", "qa", 40), ...rows("B", "qb", 40)];
    mocks.state.prompts = [...rows("A", "fa", 5, { type: "FRQ" }), ...rows("B", "fb", 5, { type: "FRQ" })];
  });

  it("stores an exam whose units follow the unit weightings, not the size of each unit's bank", async () => {
    // Unit B has as many questions as A, so a uniform draw would give about 6 and 6.
    for (let run = 0; run < 40; run++) {
      mocks.state.created = [];
      await startExam("c1", "some-course");
      const { questionIds } = mocks.state.created[0] as { questionIds: string[] };
      expect(questionIds).toHaveLength(12);
      expect(questionIds.filter((id) => id.startsWith("qa"))).toHaveLength(9);
      expect(questionIds.filter((id) => id.startsWith("qb"))).toHaveLength(3);
    }
  });

  it("weights the free-response prompts too: 1.5 of 2 from the heavier unit, so one or two", async () => {
    const fromA = new Set<number>();
    for (let run = 0; run < 80; run++) {
      mocks.state.created = [];
      await startExam("c1", "some-course");
      const { frqPromptIds } = mocks.state.created[0] as { frqPromptIds: string[] };
      expect(frqPromptIds).toHaveLength(2);
      fromA.add(frqPromptIds.filter((id) => id.startsWith("fa")).length);
    }
    expect([...fromA].sort()).toEqual([1, 2]);
  });

  it("sends the student to the exam it created", async () => {
    await startExam("c1", "some-course");
    expect(mocks.redirect).toHaveBeenCalledWith("/courses/some-course/exam/attempt-1");
  });

  it("still builds an exam when no unit has a weighting", async () => {
    mocks.state.units = [{ id: "A", weightingMin: 0, weightingMax: 0 }, { id: "B", weightingMin: 0, weightingMax: 0 }];
    await startExam("c1", "some-course");
    const { questionIds, frqPromptIds } = mocks.state.created[0] as { questionIds: string[]; frqPromptIds: string[] };
    expect(questionIds).toHaveLength(12);
    expect(new Set(questionIds).size).toBe(12);
    expect(frqPromptIds).toHaveLength(2);
  });

  it("gives a short exam rather than an error when the bank is smaller than the format", async () => {
    mocks.state.questions = [...rows("A", "qa", 4), ...rows("B", "qb", 3)];
    await startExam("c1", "some-course");
    expect((mocks.state.created[0] as { questionIds: string[] }).questionIds).toHaveLength(7);
  });
});
