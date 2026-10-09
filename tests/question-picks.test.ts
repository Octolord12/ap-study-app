import { beforeEach, describe, expect, it, vi } from "vitest";

// The two places that draw a random set of questions: a custom quiz, and the daily challenge's filler after the due reviews. They used to
// shuffle with sort(() => Math.random() - 0.5), which is not uniform (at 360 questions and a 20-question quiz it picked the first ones about 1.75x
// as often as it should), so these tests run many draws against a faked database and require every question to be about equally likely.

const mocks = vi.hoisted(() => ({
  questions: [] as { id: string }[],
  due: [] as { questionId: string }[],
  db: {
    question: { findMany: vi.fn() },
    spacedRepetitionState: { findMany: vi.fn() },
  },
}));

vi.mock("@/lib/db", () => ({ getDb: () => mocks.db }));

import { pickDailyChallengeQuestionIds, pickQuestionIdsForCustomQuiz } from "@/lib/study/queries";

const ids = (n: number) => Array.from({ length: n }, (_, i) => ({ id: `q${String(i + 1).padStart(2, "0")}` }));

// Draw `trials` times and return how often each id was picked.
async function tally(pick: () => Promise<string[]>, trials: number) {
  const counts = new Map<string, number>();
  for (let t = 0; t < trials; t++) for (const id of await pick()) counts.set(id, (counts.get(id) ?? 0) + 1);
  return counts;
}

function expectFlat(counts: Map<string, number>, population: number, expected: number) {
  expect(counts.size).toBe(population); // nothing is never picked
  // With these sizes the standard deviation is about 30, so 15% (150) is five sigma; the old shuffle was off by 50% to 190% here.
  for (const [id, n] of counts) expect(Math.abs(n - expected) / expected, id).toBeLessThan(0.15);
}

describe("pickQuestionIdsForCustomQuiz", () => {
  beforeEach(() => {
    vi.clearAllMocks();
    mocks.questions = ids(60);
    mocks.db.question.findMany.mockImplementation(async () => mocks.questions);
  });

  const filter = { courseId: "c1", unitIds: ["u1", "u2"], length: 10 };

  it("returns the asked-for number of distinct questions from those that match", async () => {
    const picked = await pickQuestionIdsForCustomQuiz(filter);
    expect(picked).toHaveLength(10);
    expect(new Set(picked).size).toBe(10);
    for (const id of picked) expect(mocks.questions.map((q) => q.id)).toContain(id);
  });

  it("returns every match when fewer match than were asked for", async () => {
    mocks.questions = ids(4);
    expect([...(await pickQuestionIdsForCustomQuiz(filter))].sort()).toEqual(["q01", "q02", "q03", "q04"]);
  });

  it("asks the database only for this course's questions in the chosen units, narrowed by difficulty when one is given", async () => {
    await pickQuestionIdsForCustomQuiz({ ...filter, difficulty: "HARD" });
    expect(mocks.db.question.findMany.mock.calls[0][0].where).toEqual({ courseId: "c1", unitId: { in: ["u1", "u2"] }, difficulty: "HARD" });
  });

  it("makes every matching question about equally likely, not the first ones in the list", async () => {
    const counts = await tally(() => pickQuestionIdsForCustomQuiz(filter), 6000);
    expectFlat(counts, 60, (6000 * 10) / 60);
  });
});

describe("pickDailyChallengeQuestionIds", () => {
  beforeEach(() => {
    vi.clearAllMocks();
    mocks.questions = ids(60);
    mocks.due = [];
    mocks.db.question.findMany.mockImplementation(async () => mocks.questions);
    mocks.db.spacedRepetitionState.findMany.mockImplementation(async () => mocks.due);
  });

  it("fills a set of five from the course's questions when nothing is due", async () => {
    const picked = await pickDailyChallengeQuestionIds("u", "c1");
    expect(picked).toHaveLength(5);
    expect(new Set(picked).size).toBe(5);
  });

  it("puts the due reviews first and fills only the rest, never repeating a due question", async () => {
    mocks.due = [{ questionId: "dueA" }, { questionId: "dueB" }];
    mocks.db.question.findMany.mockImplementation(async ({ where }: { where: { id: { notIn: string[] } } }) => mocks.questions.filter((q) => !where.id.notIn.includes(q.id)));
    const picked = await pickDailyChallengeQuestionIds("u", "c1");
    expect(picked.slice(0, 2)).toEqual(["dueA", "dueB"]);
    expect(picked).toHaveLength(5);
    expect(mocks.db.question.findMany.mock.calls[0][0].where.id).toEqual({ notIn: ["dueA", "dueB"] });
  });

  it("does not draw filler at all when five are already due", async () => {
    mocks.due = ["a", "b", "c", "d", "e"].map((questionId) => ({ questionId }));
    expect(await pickDailyChallengeQuestionIds("u", "c1")).toEqual(["a", "b", "c", "d", "e"]);
    expect(mocks.db.question.findMany).not.toHaveBeenCalled();
  });

  it("makes every candidate about equally likely to fill the set", async () => {
    const counts = await tally(() => pickDailyChallengeQuestionIds("u", "c1"), 12000);
    expectFlat(counts, 60, (12000 * 5) / 60);
  });
});
