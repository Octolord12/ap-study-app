import { describe, expect, it } from "vitest";
import { examWeakUnits, type ExamQuestionResult } from "@/lib/study/exam-breakdown";

const r = (id: string, unit: number, state: "right" | "wrong" | "skipped"): ExamQuestionResult => ({
  questionId: id,
  unitSlug: `unit-${unit}`,
  unitName: `Unit ${unit}`,
  unitOrder: unit,
  answered: state !== "skipped",
  correct: state === "right",
});

describe("examWeakUnits", () => {
  it("ranks units by how many questions were missed", () => {
    const out = examWeakUnits([r("a", 1, "wrong"), r("b", 1, "right"), r("c", 5, "wrong"), r("d", 5, "wrong"), r("e", 5, "wrong"), r("f", 2, "right")]);
    expect(out.map((u) => u.unitSlug)).toEqual(["unit-5", "unit-1"]);
    expect(out[0]).toMatchObject({ total: 3, missed: 3, missedIds: ["c", "d", "e"] });
  });

  it("counts a skipped question as missed", () => {
    expect(examWeakUnits([r("a", 3, "skipped"), r("b", 3, "right")])[0]).toMatchObject({ missed: 1, missedIds: ["a"] });
  });

  it("leaves out units with nothing missed", () => {
    expect(examWeakUnits([r("a", 1, "right"), r("b", 2, "right")])).toEqual([]);
  });

  it("breaks a tie on count by the worse share, then by unit order", () => {
    const out = examWeakUnits([r("a", 4, "wrong"), r("b", 4, "right"), r("c", 4, "right"), r("d", 2, "wrong"), r("e", 2, "right"), r("f", 3, "wrong"), r("g", 3, "right")]);
    // Each missed one: unit 2 and 3 (1 of 2) are worse than unit 4 (1 of 3); between 2 and 3 the earlier unit wins.
    expect(out.map((u) => u.unitSlug)).toEqual(["unit-2", "unit-3", "unit-4"]);
  });

  it("caps the list and handles an empty exam", () => {
    const many = Array.from({ length: 8 }, (_, i) => r(`q${i}`, i + 1, "wrong"));
    expect(examWeakUnits(many)).toHaveLength(5);
    expect(examWeakUnits([])).toEqual([]);
  });
});
