import fs from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import { allocateByWeight, pickByUnitWeight, pickExamFrqIds, pickExamMcqIds, unitWeightsFrom } from "@/lib/study/exam-selection";

// A seeded generator, so every run draws the same exams: the tolerances below are checked once, not left to luck.
function seeded(seed: number): () => number {
  let a = seed >>> 0;
  return () => {
    a = (a + 0x6d2b79f5) >>> 0;
    let t = a;
    t = Math.imul(t ^ (t >>> 15), t | 1);
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

const units = (weights: number[], capacity = 100) => weights.map((weight, i) => ({ key: `u${i + 1}`, weight, capacity }));

describe("allocateByWeight", () => {
  it("gives every unit the floor or the ceiling of its exact share, and the counts add up to the total", () => {
    const weights = [22, 22, 22, 25, 33, 37, 18, 25];
    const sum = weights.reduce((a, b) => a + b, 0);
    const random = seeded(1);
    for (let run = 0; run < 3000; run++) {
      const counts = allocateByWeight(42, units(weights), random);
      expect([...counts.values()].reduce((a, b) => a + b, 0)).toBe(42);
      weights.forEach((w, i) => {
        const exact = (42 * w) / sum;
        const n = counts.get(`u${i + 1}`)!;
        expect(n === Math.floor(exact) || n === Math.ceil(exact)).toBe(true);
      });
    }
  });

  it("averages each unit's exact share over many draws, so rounding favors no unit", () => {
    const weights = [22, 22, 22, 25, 33, 37, 18, 25];
    const sum = weights.reduce((a, b) => a + b, 0);
    const random = seeded(2);
    const totals = new Map<string, number>();
    const runs = 20000;
    for (let run = 0; run < runs; run++) for (const [k, n] of allocateByWeight(42, units(weights), random)) totals.set(k, (totals.get(k) ?? 0) + n);
    weights.forEach((w, i) => expect(totals.get(`u${i + 1}`)! / runs).toBeCloseTo((42 * w) / sum, 1));
  });

  it("gives the same split every time when the shares come out whole", () => {
    const random = seeded(3);
    for (let run = 0; run < 200; run++) {
      const counts = allocateByWeight(4, units([1, 1, 2]), random);
      expect([counts.get("u1"), counts.get("u2"), counts.get("u3")]).toEqual([1, 1, 2]);
    }
  });

  it("lets two neighbouring units both appear when their shares add to less than one", () => {
    // 6 of BC's free-response: units 1 and 2 are 0.43 each. In a fixed order they could never both be drawn.
    const weights = [15, 15, 15, 15, 25, 35, 15, 15, 25, 35];
    const random = seeded(4);
    let both = 0;
    for (let run = 0; run < 3000; run++) {
      const counts = allocateByWeight(6, units(weights), random);
      if (counts.get("u1") === 1 && counts.get("u2") === 1) both++;
    }
    expect(both).toBeGreaterThan(100);
  });

  it("pins a unit at its capacity and splits the rest among the others", () => {
    const random = seeded(5);
    for (let run = 0; run < 500; run++) {
      const counts = allocateByWeight(10, [{ key: "a", weight: 90, capacity: 2 }, { key: "b", weight: 5, capacity: 50 }, { key: "c", weight: 5, capacity: 50 }], random);
      expect(counts.get("a")).toBe(2);
      expect(counts.get("b")! + counts.get("c")!).toBe(8);
      expect(counts.get("b")).toBe(4);
    }
  });

  it("returns every unit's capacity when the whole bank is smaller than the total", () => {
    const counts = allocateByWeight(10, [{ key: "a", weight: 1, capacity: 2 }, { key: "b", weight: 3, capacity: 3 }], seeded(6));
    expect([counts.get("a"), counts.get("b")]).toEqual([2, 3]);
  });

  it("ignores a unit with no weight or no questions", () => {
    const counts = allocateByWeight(5, [{ key: "a", weight: 0, capacity: 50 }, { key: "b", weight: 4, capacity: 0 }, { key: "c", weight: 1, capacity: 50 }], seeded(7));
    expect([counts.get("a"), counts.get("b"), counts.get("c")]).toEqual([0, 0, 5]);
  });
});

describe("pickByUnitWeight", () => {
  const items = Array.from({ length: 30 }, (_, i) => ({ id: `q${i}`, unitId: i < 10 ? "a" : i < 20 ? "b" : "c" }));

  it("follows the weights, with distinct items", () => {
    const weights = new Map([["a", 1], ["b", 1], ["c", 2]]);
    const random = seeded(8);
    for (let run = 0; run < 200; run++) {
      const picked = pickByUnitWeight(items, 8, weights, random);
      expect(new Set(picked.map((p) => p.id)).size).toBe(8);
      expect(picked.filter((p) => p.unitId === "c")).toHaveLength(4);
      expect(picked.filter((p) => p.unitId === "a")).toHaveLength(2);
    }
  });

  it("falls back to a plain uniform draw when there are no weights, an item has no unit, or a unit has no weight", () => {
    const random = seeded(9);
    for (const weights of [undefined, new Map([["a", 1], ["b", 1]]), new Map([["a", 1], ["b", 1], ["c", 0]]), new Map([["a", 1], ["b", 1], ["c", Number.NaN]])]) {
      const picked = pickByUnitWeight(items, 8, weights, random);
      expect(picked).toHaveLength(8);
      expect(new Set(picked.map((p) => p.id)).size).toBe(8);
    }
    expect(pickByUnitWeight([{ id: "x" }, { id: "y" }, { id: "z" }], 2, new Map([["a", 1]]), random)).toHaveLength(2);
  });

  it("gives everything, shuffled, when the bank is no bigger than the count, and nothing for a count of zero", () => {
    expect(pickByUnitWeight(items.slice(0, 5), 8, new Map([["a", 1]]), seeded(10)).map((p) => p.id).sort()).toEqual(["q0", "q1", "q2", "q3", "q4"]);
    expect(pickByUnitWeight(items, 0, new Map([["a", 1]]))).toEqual([]);
  });

  it("does not return an order grouped by unit", () => {
    const weights = new Map([["a", 1], ["b", 1], ["c", 1]]);
    const random = seeded(11);
    let grouped = 0;
    for (let run = 0; run < 200; run++) {
      const units = pickByUnitWeight(items, 9, weights, random).map((p) => p.unitId);
      if (units.join("") === [...units].sort().join("")) grouped++;
    }
    expect(grouped).toBeLessThan(5);
  });
});

describe("unitWeightsFrom", () => {
  it("uses min + max, so a 15-20% unit counts for 35 and a 5-10% unit for 15", () => {
    expect(unitWeightsFrom([{ id: "a", weightingMin: 15, weightingMax: 20 }, { id: "b", weightingMin: 5, weightingMax: 10 }])).toEqual(new Map([["a", 35], ["b", 15]]));
  });
});

// The shipped content, not a fixture.
interface UnitFile {
  slug: string;
  weightingMin: number;
  weightingMax: number;
}
interface Item {
  id: string;
  unit: string;
  type?: string;
}
const root = path.resolve(import.meta.dirname, "../content");
const courses = fs.readdirSync(root, { withFileTypes: true }).filter((d) => d.isDirectory()).map((d) => d.name);
const readDir = <T>(course: string, sub: string): T[] => {
  const dir = path.join(root, course, sub);
  return fs.readdirSync(dir).filter((f) => f.endsWith(".json")).flatMap((f) => JSON.parse(fs.readFileSync(path.join(dir, f), "utf8")) as T[]);
};
const readUnitFiles = (course: string): UnitFile[] => {
  const dir = path.join(root, course, "units");
  return fs.readdirSync(dir).filter((f) => f.endsWith(".json")).map((f) => JSON.parse(fs.readFileSync(path.join(dir, f), "utf8")) as UnitFile);
};

describe.each(courses)("%s weighted exam", (course) => {
  const unitFiles = readUnitFiles(course);
  const weights = unitWeightsFrom(unitFiles.map((u) => ({ id: u.slug, weightingMin: u.weightingMin, weightingMax: u.weightingMax })));
  const sum = [...weights.values()].reduce((a, b) => a + b, 0);
  const questions = readDir<Item>(course, "questions").map((q) => ({ id: q.id, unitId: q.unit }));
  const prompts = readDir<Item>(course, "frqs").map((f) => ({ id: f.id, type: f.type ?? "FRQ", unitId: f.unit }));
  const sections = JSON.parse(fs.readFileSync(path.join(root, course, "course.json"), "utf8")).examFormat.sections as { type: string; questionCount: number }[];
  const mcqCount = sections.find((s) => s.type === "MCQ")!.questionCount;

  it("draws the multiple-choice count, and every unit gets the floor or ceiling of its weighted share", () => {
    const random = seeded(100);
    const unitOf = new Map(questions.map((q) => [q.id, q.unitId]));
    for (let run = 0; run < 300; run++) {
      const ids = pickExamMcqIds(questions, mcqCount, weights, random);
      expect(ids).toHaveLength(mcqCount);
      expect(new Set(ids).size).toBe(mcqCount);
      const perUnit = new Map<string, number>();
      for (const id of ids) perUnit.set(unitOf.get(id)!, (perUnit.get(unitOf.get(id)!) ?? 0) + 1);
      for (const [unit, weight] of weights) {
        const exact = (mcqCount * weight) / sum;
        const n = perUnit.get(unit) ?? 0;
        expect(n === Math.floor(exact) || n === Math.ceil(exact), `${unit}: ${n} vs ${exact}`).toBe(true);
      }
    }
  });

  it("builds the free-response items its exam format asks for, in section order", () => {
    const wanted = sections.filter((s) => s.type !== "MCQ").flatMap((s) => Array(s.questionCount).fill(s.type));
    const byId = new Map(prompts.map((p) => [p.id, p.type]));
    const random = seeded(101);
    for (let run = 0; run < 200; run++) {
      const picked = pickExamFrqIds(sections, prompts, random, weights);
      expect(picked.map((id) => byId.get(id))).toEqual(wanted);
      expect(new Set(picked).size).toBe(picked.length);
    }
  });
});

describe("what the weighting does for the courses it was written for", () => {
  const load = (course: string) => {
    const unitFiles = readUnitFiles(course);
    const weights = unitWeightsFrom(unitFiles.map((u) => ({ id: u.slug, weightingMin: u.weightingMin, weightingMax: u.weightingMax })));
    const prompts = readDir<Item>(course, "frqs").map((f) => ({ id: f.id, type: f.type ?? "FRQ", unitId: f.unit }));
    const sections = JSON.parse(fs.readFileSync(path.join(root, course, "course.json"), "utf8")).examFormat.sections as { type: string; questionCount: number }[];
    const unitOfPrompt = new Map(prompts.map((p) => [p.id, p.unitId]));
    return { unitFiles, weights, prompts, sections, unitOfPrompt };
  };

  it("gives every Calculus BC exam a series question and a parametric, polar or vector one at least sometimes, never none from Units 9 and 10", () => {
    const { unitFiles, weights, prompts, sections, unitOfPrompt } = load("ap-calc-bc");
    const slugOf = (n: number) => unitFiles.find((u) => u.slug.startsWith(`unit-${n}-`))!.slug;
    const random = seeded(200);
    let unit9 = 0;
    const runs = 4000;
    for (let run = 0; run < runs; run++) {
      const units = pickExamFrqIds(sections, prompts, random, weights).map((id) => unitOfPrompt.get(id));
      expect(units.filter((u) => u === slugOf(10))).toHaveLength(1);
      expect(units.filter((u) => u === slugOf(6))).toHaveLength(1);
      if (units.includes(slugOf(9))) unit9++;
    }
    // 25 / 210 of 6 prompts is 0.714: a Unit 9 prompt in about 71% of exams.
    expect(unit9 / runs).toBeGreaterThan(0.68);
    expect(unit9 / runs).toBeLessThan(0.75);
  });

  it("puts Calculus BC's Units 9 and 10 at 12% and 17% of the multiple choice, and Unit 6 at 17%", () => {
    const { unitFiles, weights } = load("ap-calc-bc");
    const questions = readDir<Item>("ap-calc-bc", "questions").map((q) => ({ id: q.id, unitId: q.unit }));
    const unitOf = new Map(questions.map((q) => [q.id, q.unitId]));
    const ids = pickExamMcqIds(questions, 42, weights, seeded(201));
    const count = (n: number) => ids.filter((id) => unitOf.get(id) === unitFiles.find((u) => u.slug.startsWith(`unit-${n}-`))!.slug).length;
    expect([count(9), count(10), count(6)]).toEqual([5, 7, 7]);
  });

  it.each(["ap-world", "ap-us-history"])("draws the three short answers of a %s exam from three different units", (course) => {
    const { weights, prompts, sections, unitOfPrompt } = load(course);
    const random = seeded(202);
    for (let run = 0; run < 1000; run++) {
      const picked = pickExamFrqIds(sections, prompts, random, weights);
      const saqUnits = picked.slice(0, 3).map((id) => unitOfPrompt.get(id));
      expect(new Set(saqUnits).size).toBe(3);
    }
  });
});
