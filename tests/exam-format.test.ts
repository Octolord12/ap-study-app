import { describe, expect, it } from "vitest";
import { describeExamFormat, formatDuration } from "@/lib/content/exam-format";

describe("describeExamFormat", () => {
  it("counts MCQ and FRQ sections", () => {
    expect(
      describeExamFormat({
        totalDurationMinutes: 190,
        sections: [
          { type: "MCQ", questionCount: 42 },
          { type: "FRQ", questionCount: 6 },
        ],
      }),
    ).toBe("42 multiple choice, 6 free response");
  });

  it("names the World History item types without printing their slot counts", () => {
    expect(
      describeExamFormat({
        totalDurationMinutes: 195,
        sections: [
          { type: "MCQ", questionCount: 55 },
          { type: "SAQ", questionCount: 1 },
          { type: "DBQ", questionCount: 1 },
          { type: "LEQ", questionCount: 1 },
        ],
      }),
    ).toBe("55 multiple choice, short answer, document-based question, long essay");
  });
});

describe("formatDuration", () => {
  it("formats hours and minutes", () => {
    expect(formatDuration(190)).toBe("3 h 10 min");
    expect(formatDuration(180)).toBe("3 h");
    expect(formatDuration(45)).toBe("45 min");
  });
});
