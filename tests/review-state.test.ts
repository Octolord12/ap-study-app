import { describe, expect, it } from "vitest";
import { frqContentChanged, nextRefresherState, nextReviewedFlag, questionContentChanged, type StoredFrq, type StoredQuestion } from "@/lib/content/review-state";
import type { FRQ, Question } from "@/lib/content/schema";

const question: Question = {
  id: "q1",
  unit: "u1",
  topic: "t1",
  difficulty: "hard",
  stem: "What is $x$?",
  choices: [
    { label: "A", text: "one", isCorrect: true, explanation: "because" },
    { label: "B", text: "two", isCorrect: false, explanation: "no" },
    { label: "C", text: "three", isCorrect: false, explanation: "no" },
    { label: "D", text: "four", isCorrect: false, explanation: "no" },
  ],
  explanation: "It is one.",
  conceptLink: "c/u1/t1",
  reviewed: false,
  diagram: { type: "xy-graph", altText: "a", xLabel: "x", yLabel: "y", xMin: 0, xMax: 1, yMin: 0, yMax: 1, series: [] } as Question["diagram"],
};

// What the database hands back: enum upper-cased, choices in any order, jsonb with its own key order.
function stored(overrides: Partial<StoredQuestion> = {}): StoredQuestion {
  return {
    difficulty: "HARD",
    stem: question.stem,
    explanation: question.explanation,
    conceptLink: question.conceptLink,
    diagram: { yMax: 1, yMin: 0, xMax: 1, xMin: 0, type: "xy-graph", series: [], altText: "a", yLabel: "y", xLabel: "x" },
    reviewed: true,
    choices: [...question.choices].reverse(),
    ...overrides,
  };
}

describe("questionContentChanged", () => {
  it("is false for the same content despite enum case, choice order and jsonb key order", () => {
    expect(questionContentChanged(stored(), question)).toBe(false);
  });

  it.each([
    ["stem", { stem: "Different" }],
    ["explanation", { explanation: "Different" }],
    ["difficulty", { difficulty: "EASY" }],
    ["conceptLink", { conceptLink: "c/u2/t1" }],
    ["diagram", { diagram: null }],
  ] as const)("is true when the %s changes", (_name, change) => {
    expect(questionContentChanged(stored(change as Partial<StoredQuestion>), question)).toBe(true);
  });

  it("is true when a choice's text, correctness or explanation changes", () => {
    const edit = (patch: Partial<StoredQuestion["choices"][number]>) => stored({ choices: question.choices.map((c, i) => (i === 1 ? { ...c, ...patch } : c)) });
    expect(questionContentChanged(edit({ text: "deux" }), question)).toBe(true);
    expect(questionContentChanged(edit({ isCorrect: true }), question)).toBe(true);
    expect(questionContentChanged(edit({ explanation: "changed" }), question)).toBe(true);
  });

  it("is true when a choice is added or removed", () => {
    expect(questionContentChanged(stored({ choices: question.choices.slice(0, 3) }), question)).toBe(true);
  });
});

const frq: FRQ = {
  id: "f1",
  unit: "u1",
  topic: "t1",
  type: "SAQ",
  prompt: "Answer parts A, B and C.",
  pointValue: 3,
  rubric: [
    { id: "r1", points: 1, description: "a" },
    { id: "r2", points: 2, description: "b" },
  ],
  sampleResponse: "sample",
  reviewed: false,
};

function storedFrq(overrides: Partial<StoredFrq> = {}): StoredFrq {
  return {
    type: "SAQ",
    prompt: frq.prompt,
    pointValue: 3,
    rubric: [
      { points: 1, id: "r1", description: "a" },
      { points: 2, id: "r2", description: "b" },
    ],
    sampleResponse: "sample",
    diagram: null,
    reviewed: true,
    ...overrides,
  };
}

describe("frqContentChanged", () => {
  it("is false for the same prompt despite jsonb key order and a missing diagram", () => {
    expect(frqContentChanged(storedFrq(), frq)).toBe(false);
  });

  it("treats a missing type as FRQ", () => {
    expect(frqContentChanged(storedFrq({ type: "FRQ" }), { ...frq, type: undefined })).toBe(false);
    expect(frqContentChanged(storedFrq({ type: "SAQ" }), { ...frq, type: undefined })).toBe(true);
  });

  it.each([
    ["prompt", { prompt: "Other" }],
    ["pointValue", { pointValue: 4 }],
    ["sampleResponse", { sampleResponse: "other" }],
    ["rubric", { rubric: [{ points: 3, id: "r1", description: "a" }] }],
  ] as const)("is true when the %s changes", (_name, change) => {
    expect(frqContentChanged(storedFrq(change as Partial<StoredFrq>), frq)).toBe(true);
  });
});

describe("nextReviewedFlag", () => {
  it("keeps an approval while the content is unchanged", () => {
    expect(nextReviewedFlag({ reviewed: true }, false, false)).toBe(true);
  });
  it("takes an approval back when the content changed", () => {
    expect(nextReviewedFlag({ reviewed: true }, true, false)).toBe(false);
  });
  it("leaves an unreviewed item unreviewed", () => {
    expect(nextReviewedFlag({ reviewed: false }, false, false)).toBe(false);
  });
  it("starts a new item at the file's flag", () => {
    expect(nextReviewedFlag(null, false, false)).toBe(false);
    expect(nextReviewedFlag(null, false, true)).toBe(true);
  });
  it("lets a file that says reviewed: true win", () => {
    expect(nextReviewedFlag({ reviewed: false }, true, true)).toBe(true);
  });
});

describe("nextRefresherState", () => {
  const file = { body: "The idea.", reviewed: false };

  it("a refresher the database has not seen starts unreviewed", () => {
    expect(nextRefresherState(null, file)).toEqual({ refresher: "The idea.", refresherReviewed: false });
    expect(nextRefresherState({ refresher: null, refresherReviewed: false }, file)).toEqual({ refresher: "The idea.", refresherReviewed: false });
  });

  it("keeps an approval while the text is exactly what was approved", () => {
    expect(nextRefresherState({ refresher: "The idea.", refresherReviewed: true }, file)).toEqual({ refresher: "The idea.", refresherReviewed: true });
  });

  it("sends an approved refresher back for review when the text changes", () => {
    expect(nextRefresherState({ refresher: "An older idea.", refresherReviewed: true }, file)).toEqual({ refresher: "The idea.", refresherReviewed: false });
  });

  it("a file that says reviewed: true always wins", () => {
    expect(nextRefresherState({ refresher: "Older.", refresherReviewed: false }, { ...file, reviewed: true })).toEqual({ refresher: "The idea.", refresherReviewed: true });
  });

  it("clears a stored refresher the files no longer have", () => {
    expect(nextRefresherState({ refresher: "The idea.", refresherReviewed: true }, null)).toEqual({ refresher: null, refresherReviewed: false });
  });
});
