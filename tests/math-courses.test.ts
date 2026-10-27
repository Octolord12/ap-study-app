import { describe, expect, it } from "vitest";
import { isMathCourse } from "@/lib/content/math-courses";
import { isPaperLinedCourse } from "@/lib/content/paper-lined";
import { normalizePlainMath } from "@/lib/content/plain-math";

describe("which courses count as math courses", () => {
  it("includes both calculus courses, Physics 1 and Statistics, so they get the notebook-paper cards and the math typesetting", () => {
    for (const slug of ["ap-calc", "ap-calc-bc", "ap-physics-1", "ap-statistics"]) {
      expect(isMathCourse(slug), slug).toBe(true);
      expect(isPaperLinedCourse(slug), slug).toBe(true);
    }
  });

  it("leaves out the programming and history courses, where an underscore or an arrow is not math", () => {
    for (const slug of ["ap-csa", "ap-world", "ap-us-history", "ap-calc-bc-typo", ""]) {
      expect(isMathCourse(slug), slug).toBe(false);
    }
  });

  it("BC gets the same plain-text math typesetting as AB (e^(2x) becomes real math)", () => {
    const text = "the derivative of e^(2x) is 2e^(2x)";
    expect(normalizePlainMath(text, { mathCourse: isMathCourse("ap-calc-bc") })).toBe(normalizePlainMath(text, { mathCourse: isMathCourse("ap-calc") }));
    expect(normalizePlainMath(text, { mathCourse: isMathCourse("ap-calc-bc") })).toContain("$");
  });
});
