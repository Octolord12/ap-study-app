import { describe, expect, it } from "vitest";
import { describeExamFormat, formatDuration, frqTitle } from "@/lib/content/exam-format";

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

  it("counts every World History section, now that the simulator uses the counts", () => {
    expect(
      describeExamFormat({
        totalDurationMinutes: 195,
        sections: [
          { type: "MCQ", questionCount: 55 },
          { type: "SAQ", questionCount: 3 },
          { type: "DBQ", questionCount: 1 },
          { type: "LEQ", questionCount: 1 },
        ],
      }),
    ).toBe("55 multiple choice, 3 short answer, 1 document-based question, 1 long essay");
  });
});

describe("frqTitle", () => {
  it("names each free-response kind and falls back to plain free response", () => {
    expect(frqTitle("SAQ")).toBe("Short answer");
    expect(frqTitle("DBQ")).toBe("Document-based question");
    expect(frqTitle("LEQ")).toBe("Long essay");
    expect(frqTitle("FRQ")).toBe("Free response");
    expect(frqTitle("anything else")).toBe("Free response");
  });
});

describe("formatDuration", () => {
  it("formats hours and minutes", () => {
    expect(formatDuration(190)).toBe("3 h 10 min");
    expect(formatDuration(180)).toBe("3 h");
    expect(formatDuration(45)).toBe("45 min");
  });
});
