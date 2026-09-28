import { describe, expect, it } from "vitest";
import { SelfGradingStrategy, type GradingInput } from "@/lib/scoring/grading";

const rubric: GradingInput["rubric"] = [
  { id: "r1", points: 1, description: "Identifies the correct variable" },
  { id: "r2", points: 2, description: "Explains the mechanism correctly" },
  { id: "r3", points: 1, description: "Draws a valid conclusion" },
];

describe("SelfGradingStrategy", () => {
  it("sums points only for checked rubric lines", async () => {
    const strategy = new SelfGradingStrategy();

    const result = await strategy.grade(
      { responseText: "student response", rubric, maxPoints: 4 },
      { checkedLineIds: ["r1", "r3"] },
    );

    expect(result.pointsAwarded).toBe(2);
    expect(result.maxPoints).toBe(4);
    expect(result.perLineFeedback).toEqual([
      { ruleId: "r1", awarded: true },
      { ruleId: "r2", awarded: false },
      { ruleId: "r3", awarded: true },
    ]);
  });

  it("awards zero when nothing is checked", async () => {
    const strategy = new SelfGradingStrategy();

    const result = await strategy.grade(
      { responseText: "", rubric, maxPoints: 4 },
      { checkedLineIds: [] },
    );

    expect(result.pointsAwarded).toBe(0);
  });
});
