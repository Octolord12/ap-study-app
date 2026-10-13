import { describe, expect, it } from "vitest";
import { drawableTypes, examDraws, frqSupplyShort } from "@/lib/content/exam-sections";
import { frqTitle } from "@/lib/content/exam-format";
import { CourseSchema, ExamSectionSchema, FRQSchema } from "@/lib/content/schema";
import { checkExamSupply, validateFRQ } from "@/lib/content/validate";
import { pickExamFrqIds, unitWeightsFrom } from "@/lib/study/exam-selection";

const KINDS = ["RESULTS", "RESULTS_GRAPH", "INVESTIGATION", "CONCEPT", "MODEL", "DATA"] as const;
const bio = [
  { type: "MCQ", questionCount: 60 },
  { type: "FRQ", questionCount: 6, kinds: KINDS },
];

// 8 units, 6 prompts of each kind spread over them (kind k lives in units k..k+5 mod 8), like a real bank would be
const prompts = KINDS.flatMap((type, k) => Array.from({ length: 6 }, (_, i) => ({ id: `${type}-${i}`, type, unitId: `u${((k + i) % 8) + 1}` })));
const weights = unitWeightsFrom(Array.from({ length: 8 }, (_, i) => ({ id: `u${i + 1}`, weightingMin: 8 + i, weightingMax: 12 + i })));

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

describe("examDraws", () => {
  it("turns a section with kinds into one draw per kind, in order, and a plain section into one draw", () => {
    expect(examDraws(bio).map((d) => [d.type, d.count])).toEqual(KINDS.map((k) => [k, 1]));
    expect(examDraws([{ type: "MCQ", questionCount: 55 }, { type: "SAQ", questionCount: 3 }, { type: "DBQ", questionCount: 1 }]).map((d) => [d.type, d.count])).toEqual([["SAQ", 3], ["DBQ", 1]]);
  });

  it("only spreads units for a section made of kinds", () => {
    expect(examDraws(bio).every((d) => d.spreadUnits)).toBe(true);
    expect(examDraws([{ type: "FRQ", questionCount: 6 }]).every((d) => !d.spreadUnits)).toBe(true);
  });

  it("lists the types a course can draw: the kinds, not the section's own name", () => {
    expect(drawableTypes(bio)).toEqual([...KINDS]);
    expect(drawableTypes(bio)).not.toContain("FRQ");
    expect(drawableTypes([{ type: "MCQ", questionCount: 40 }, { type: "FRQ", questionCount: 4 }])).toEqual(["FRQ"]);
  });
});

describe("the section schema", () => {
  const section = { type: "FRQ", questionCount: 6, durationMinutes: 90, scoreWeight: 0.5, kinds: [...KINDS] };
  it("accepts kinds that match the question count", () => {
    expect(ExamSectionSchema.safeParse(section).success).toBe(true);
  });
  it("rejects kinds on the multiple-choice section, a count that disagrees, repeated kinds, and an unknown kind", () => {
    expect(ExamSectionSchema.safeParse({ ...section, type: "MCQ" }).success).toBe(false);
    expect(ExamSectionSchema.safeParse({ ...section, questionCount: 5 }).success).toBe(false);
    expect(ExamSectionSchema.safeParse({ ...section, kinds: ["DATA", "DATA", "MODEL", "CONCEPT", "RESULTS", "INVESTIGATION"] }).success).toBe(false);
    expect(ExamSectionSchema.safeParse({ ...section, kinds: ["DATA", "ESSAY", "MODEL", "CONCEPT", "RESULTS", "INVESTIGATION"] }).success).toBe(false);
  });
  it("leaves every existing section valid (no kinds)", () => {
    expect(ExamSectionSchema.safeParse({ type: "SAQ", questionCount: 3, durationMinutes: 40, scoreWeight: 0.2 }).success).toBe(true);
  });
  it("is part of a course's exam format as written in course.json", () => {
    const course = { slug: "ap-bio", name: "AP Biology", description: "d", colorTheme: "green", examFormat: { totalDurationMinutes: 180, sections: [{ type: "MCQ", questionCount: 60, durationMinutes: 90, scoreWeight: 0.5 }, section] } };
    const parsed = CourseSchema.safeParse(course);
    expect(parsed.success && parsed.data.examFormat.sections[1].kinds).toEqual([...KINDS]);
  });
});

describe("prompt types and supply for a course with kinds", () => {
  const frq = (type: string) => FRQSchema.parse({ id: "x", unit: "u", topic: "t", type, prompt: "p", pointValue: 4, rubric: [{ id: "r", points: 4, description: "d" }], sampleResponse: "s", reviewed: false });
  const known = new Set(["u/t"]);

  it("accepts a prompt of each kind and rejects an untyped one (it would never be drawn)", () => {
    for (const kind of KINDS) expect(validateFRQ(frq(kind), known, drawableTypes(bio))).toEqual([]);
    const untyped = FRQSchema.parse({ id: "x", unit: "u", topic: "t", prompt: "p", pointValue: 4, rubric: [{ id: "r", points: 4, description: "d" }], sampleResponse: "s", reviewed: false });
    expect(validateFRQ(untyped, known, drawableTypes(bio))[0].message).toMatch(/type "FRQ" is not a section/);
  });

  it("needs a prompt of every kind", () => {
    expect(checkExamSupply(bio, KINDS.flatMap((k) => [k, k]))).toEqual([]);
    const problems = checkExamSupply(bio, ["RESULTS", "RESULTS_GRAPH", "INVESTIGATION", "CONCEPT", "MODEL"]);
    expect(problems.map((p) => p.message)).toEqual(["exam section DATA needs 1 prompt(s) of that type, but the course has 0"]);
  });

  it("titles each kind with the College Board's name", () => {
    expect(frqTitle("RESULTS")).toBe("Interpreting and evaluating experimental results");
    expect(frqTitle("RESULTS_GRAPH")).toBe("Interpreting and evaluating experimental results with graphing");
    expect(frqTitle("INVESTIGATION")).toBe("Scientific investigation");
    expect(frqTitle("CONCEPT")).toBe("Conceptual analysis");
    expect(frqTitle("MODEL")).toBe("Analyzing a model or visual representation");
    expect(frqTitle("DATA")).toBe("Analyzing data");
  });
});

describe("pickExamFrqIds for a section with kinds", () => {
  it("gives one prompt of each kind, in the listed order", () => {
    const random = seeded(1);
    const byId = new Map(prompts.map((p) => [p.id, p.type]));
    for (let run = 0; run < 200; run++) {
      const picked = pickExamFrqIds(bio, prompts, random, weights);
      expect(picked.map((id) => byId.get(id))).toEqual([...KINDS]);
    }
  });

  it("puts every prompt of the exam in a different unit when the bank allows it", () => {
    const random = seeded(2);
    const unitOf = new Map(prompts.map((p) => [p.id, p.unitId]));
    for (let run = 0; run < 500; run++) {
      const units = pickExamFrqIds(bio, prompts, random, weights).map((id) => unitOf.get(id));
      expect(new Set(units).size).toBe(6);
    }
  });

  it("also spreads units without weights", () => {
    const random = seeded(3);
    const unitOf = new Map(prompts.map((p) => [p.id, p.unitId]));
    for (let run = 0; run < 200; run++) expect(new Set(pickExamFrqIds(bio, prompts, random).map((id) => unitOf.get(id))).size).toBe(6);
  });

  it("repeats a unit rather than dropping a kind when the bank cannot spread them", () => {
    const oneUnit = prompts.map((p) => ({ ...p, unitId: "u1" }));
    const picked = pickExamFrqIds(bio, oneUnit, seeded(4), weights);
    expect(picked).toHaveLength(6);
    expect(new Set(picked).size).toBe(6);
  });

  it("gives a short exam, not an error, when a kind has no prompts", () => {
    const picked = pickExamFrqIds(bio, prompts.filter((p) => p.type !== "MODEL"), seeded(5), weights);
    expect(picked).toHaveLength(5);
  });

  it("does not change how a section without kinds is drawn", () => {
    const frqs = Array.from({ length: 10 }, (_, i) => ({ id: `f${i}`, type: "FRQ", unitId: "u1" }));
    // all ten are in one unit: a plain section draws six anyway, where a section of kinds would have to repeat the unit
    const picked = pickExamFrqIds([{ type: "FRQ", questionCount: 6 }], frqs, seeded(6));
    expect(picked).toHaveLength(6);
    expect(new Set(picked).size).toBe(6);
    expect(picked.every((id) => frqs.some((f) => f.id === id))).toBe(true);
  });
});

describe("frqSupplyShort", () => {
  const supply = (entries: [string, number][]) => new Map(entries);
  const full = KINDS.map((k): [string, number] => [k, 8]);

  it("is false when every kind has a prompt, although no prompt is typed with the section's own name", () => {
    expect(frqSupplyShort(bio, supply(full))).toBe(false);
  });

  it("is true when one kind has no prompts", () => {
    expect(frqSupplyShort(bio, supply(full.filter(([k]) => k !== "MODEL")))).toBe(true);
  });

  it("checks a plain section against its own type and count", () => {
    const world = [{ type: "MCQ", questionCount: 55 }, { type: "SAQ", questionCount: 3 }, { type: "DBQ", questionCount: 1 }];
    expect(frqSupplyShort(world, supply([["SAQ", 36], ["DBQ", 4]]))).toBe(false);
    expect(frqSupplyShort(world, supply([["SAQ", 2], ["DBQ", 4]]))).toBe(true);
    expect(frqSupplyShort(world, supply([["SAQ", 36]]))).toBe(true);
  });
});
