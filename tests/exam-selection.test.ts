import { describe, expect, it } from "vitest";
import { pickExamFrqIds, shuffled } from "@/lib/study/exam-selection";

const world = [
  { type: "MCQ", questionCount: 55 },
  { type: "SAQ", questionCount: 3 },
  { type: "DBQ", questionCount: 1 },
  { type: "LEQ", questionCount: 1 },
];

const worldPrompts = [
  ...Array.from({ length: 36 }, (_, i) => ({ id: `saq-${i}`, type: "SAQ" })),
  ...Array.from({ length: 4 }, (_, i) => ({ id: `dbq-${i}`, type: "DBQ" })),
  ...Array.from({ length: 13 }, (_, i) => ({ id: `leq-${i}`, type: "LEQ" })),
];

describe("pickExamFrqIds", () => {
  it("gives a World History exam 3 SAQs, 1 DBQ and 1 LEQ, in that order, not every prompt", () => {
    const ids = pickExamFrqIds(world, worldPrompts);
    expect(ids).toHaveLength(5);
    expect(ids.slice(0, 3).every((id) => id.startsWith("saq-"))).toBe(true);
    expect(ids[3]).toMatch(/^dbq-/);
    expect(ids[4]).toMatch(/^leq-/);
    expect(new Set(ids).size).toBe(5);
  });

  it("for a course with a single free-response section, draws that many of type FRQ", () => {
    const prompts = Array.from({ length: 50 }, (_, i) => ({ id: `f${i}`, type: "FRQ" }));
    const ids = pickExamFrqIds([{ type: "MCQ", questionCount: 42 }, { type: "FRQ", questionCount: 6 }], prompts);
    expect(ids).toHaveLength(6);
    expect(ids.every((id) => id.startsWith("f"))).toBe(true);
  });

  it("is the regression for the old fallback: no section of a prompt's type means it is never picked", () => {
    expect(pickExamFrqIds(world, worldPrompts.filter((p) => p.type === "SAQ")).every((id) => id.startsWith("saq-"))).toBe(true);
    expect(pickExamFrqIds([{ type: "MCQ", questionCount: 5 }], worldPrompts)).toEqual([]);
  });

  it("gives a short exam rather than failing when a type has too few prompts", () => {
    const ids = pickExamFrqIds(world, [{ id: "saq-0", type: "SAQ" }, { id: "leq-0", type: "LEQ" }]);
    expect(ids).toEqual(["saq-0", "leq-0"]);
  });

  it("does not hand the same prompt to two sections of the same type", () => {
    const ids = pickExamFrqIds(
      [{ type: "FRQ", questionCount: 2 }, { type: "FRQ", questionCount: 2 }],
      [1, 2, 3].map((n) => ({ id: `f${n}`, type: "FRQ" })),
    );
    expect(ids).toHaveLength(3);
    expect(new Set(ids).size).toBe(3);
  });

  it("varies which prompts it picks", () => {
    const seen = new Set<string>();
    for (let i = 0; i < 200; i++) pickExamFrqIds(world, worldPrompts).forEach((id) => seen.add(id));
    expect(seen.size).toBeGreaterThan(40);
  });
});

describe("shuffled", () => {
  it("returns a permutation and leaves its input alone", () => {
    const input = [1, 2, 3, 4, 5, 6];
    const out = shuffled(input);
    expect(input).toEqual([1, 2, 3, 4, 5, 6]);
    expect([...out].sort()).toEqual(input);
  });

  it("is uniform: each of 3 items lands in each slot about a third of the time", () => {
    const counts = [0, 0, 0];
    const runs = 6000;
    for (let i = 0; i < runs; i++) counts[shuffled(["a", "b", "c"]).indexOf("a")]++;
    for (const c of counts) expect(Math.abs(c / runs - 1 / 3)).toBeLessThan(0.04);
  });
});
