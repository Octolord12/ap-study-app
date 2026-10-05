import { describe, expect, it } from "vitest";
import { displayLabelMap, remapChoiceLetters, shuffleChoices } from "@/lib/study/shuffle-choices";

// Small seeded PRNG so the distribution tests are deterministic.
function mulberry32(seed: number) {
  return () => {
    seed |= 0;
    seed = (seed + 0x6d2b79f5) | 0;
    let t = Math.imul(seed ^ (seed >>> 15), 1 | seed);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

const four = [
  { label: "A", text: "first", isCorrect: true },
  { label: "B", text: "second", isCorrect: false },
  { label: "C", text: "third", isCorrect: false },
  { label: "D", text: "fourth", isCorrect: false },
];

describe("shuffleChoices", () => {
  it("returns the same choices, each exactly once, with their data intact", () => {
    const out = shuffleChoices(four, mulberry32(1));
    expect(out).toHaveLength(4);
    expect([...out].map((c) => c.label).sort()).toEqual(["A", "B", "C", "D"]);
    for (const c of out) expect(c).toMatchObject(four.find((f) => f.label === c.label)!);
  });

  it("labels the slots A, B, C, D in order, whatever order the choices land in", () => {
    const out = shuffleChoices(four, mulberry32(7));
    expect(out.map((c) => c.displayLabel)).toEqual(["A", "B", "C", "D"]);
  });

  it("handles five choices", () => {
    const five = [...four, { label: "E", text: "fifth", isCorrect: false }];
    expect(shuffleChoices(five, mulberry32(3)).map((c) => c.displayLabel)).toEqual(["A", "B", "C", "D", "E"]);
  });

  it("does not mutate its input", () => {
    const copy = JSON.parse(JSON.stringify(four));
    shuffleChoices(four, mulberry32(2));
    expect(four).toEqual(copy);
  });

  it("puts the authored-first (correct) choice in every slot about equally often", () => {
    const random = mulberry32(2026);
    const slots = { A: 0, B: 0, C: 0, D: 0 } as Record<string, number>;
    const runs = 8000;
    for (let i = 0; i < runs; i++) {
      const correct = shuffleChoices(four, random).find((c) => c.isCorrect)!;
      slots[correct.displayLabel]++;
    }
    // Uniform is 25% each; allow generous slack (expected sd is ~1.5 points).
    for (const slot of Object.keys(slots)) {
      expect(slots[slot] / runs).toBeGreaterThan(0.22);
      expect(slots[slot] / runs).toBeLessThan(0.28);
    }
  });

  it("produces different orders on different calls", () => {
    const random = mulberry32(99);
    const orders = new Set(Array.from({ length: 50 }, () => shuffleChoices(four, random).map((c) => c.label).join("")));
    expect(orders.size).toBeGreaterThan(10);
  });

  it("is a no-op on a single choice and on none", () => {
    expect(shuffleChoices([{ label: "A" }], mulberry32(1))).toEqual([{ label: "A", displayLabel: "A" }]);
    expect(shuffleChoices([], mulberry32(1))).toEqual([]);
  });
});

describe("remapChoiceLetters", () => {
  // authored A, B, C, D now shown as C, A, D, B
  const map = { A: "C", B: "A", C: "D", D: "B" };

  it("rewrites a reference to a choice by letter to the letter now shown", () => {
    expect(remapChoiceLetters("This runs about n / 2 times, even fewer than option A.", map)).toBe(
      "This runs about n / 2 times, even fewer than option C.",
    );
    expect(remapChoiceLetters("Choice B is a trap, and Answer D is too.", map)).toBe("Choice A is a trap, and Answer B is too.");
    expect(remapChoiceLetters("Compare with (option C) here", map)).toBe("Compare with (option D) here");
  });

  it("leaves math, code and ordinary prose alone", () => {
    for (const text of [
      "f(a) = f(b) and f'(c) = 0",
      "System.out.println(a.equals(b));",
      "an option for A and B in the plan",
      "Option pricing, an answer to the question, a choice of 5",
      "$\\int_a^b f(x)\\,dx = F(b) - F(a)$",
    ]) {
      expect(remapChoiceLetters(text, map)).toBe(text);
    }
  });

  it("leaves a letter with no mapping unchanged", () => {
    expect(remapChoiceLetters("option E", map)).toBe("option E");
  });
});

describe("displayLabelMap", () => {
  it("maps each authored label to the slot letter it landed in", () => {
    const shuffled = shuffleChoices(four, mulberry32(5));
    const map = displayLabelMap(shuffled);
    shuffled.forEach((c) => expect(map[c.label]).toBe(c.displayLabel));
  });
});
