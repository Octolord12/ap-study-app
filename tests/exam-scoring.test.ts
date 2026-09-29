import { describe, expect, it } from "vitest";
import { estimateApScoreRange } from "@/lib/study/exam-scoring";

describe("estimateApScoreRange", () => {
  it("maps high accuracy to the top range", () => {
    expect(estimateApScoreRange(0.95)).toBe("4-5");
    expect(estimateApScoreRange(0.85)).toBe("4-5");
  });

  it("maps low accuracy to the bottom range", () => {
    expect(estimateApScoreRange(0.1)).toBe("1-2");
    expect(estimateApScoreRange(0)).toBe("1-2");
  });

  it("is monotonic -- higher accuracy never produces a lower-labeled range", () => {
    const points = [0, 0.2, 0.4, 0.55, 0.7, 0.85, 1];
    const ranges = points.map(estimateApScoreRange);
    const order = ["1-2", "2-3", "3", "3-4", "4-5"];
    let lastIndex = -1;
    for (const range of ranges) {
      const index = order.indexOf(range);
      expect(index).toBeGreaterThanOrEqual(lastIndex);
      lastIndex = index;
    }
  });
});
