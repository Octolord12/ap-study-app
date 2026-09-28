import { describe, expect, it } from "vitest";
import { checkMarkdownBalance, validateFRQ, validateQuestion, validateUnit } from "@/lib/content/validate";
import type { Choice, FRQ, Question, Unit } from "@/lib/content/schema";

function makeChoice(overrides: Partial<Choice>): Choice {
  return { label: "A", text: "text", isCorrect: false, explanation: "why", ...overrides };
}

function makeQuestion(overrides: Partial<Question> = {}): Question {
  return {
    id: "q1",
    unit: "unit-1",
    topic: "topic-1",
    difficulty: "easy",
    stem: "What is 1 + 1?",
    choices: [
      makeChoice({ label: "A", isCorrect: false }),
      makeChoice({ label: "B", isCorrect: true }),
      makeChoice({ label: "C", isCorrect: false }),
      makeChoice({ label: "D", isCorrect: false }),
    ],
    explanation: "2 is correct",
    conceptLink: "ap-csa/unit-1/topic-1",
    reviewed: false,
    ...overrides,
  };
}

const KNOWN_TOPICS = new Set(["unit-1/topic-1"]);

describe("validateQuestion", () => {
  it("passes a well-formed question", () => {
    expect(validateQuestion(makeQuestion(), "ap-csa", KNOWN_TOPICS)).toEqual([]);
  });

  it("flags zero correct choices", () => {
    const question = makeQuestion({
      choices: [
        makeChoice({ label: "A", isCorrect: false }),
        makeChoice({ label: "B", isCorrect: false }),
        makeChoice({ label: "C", isCorrect: false }),
        makeChoice({ label: "D", isCorrect: false }),
      ],
    });
    const problems = validateQuestion(question, "ap-csa", KNOWN_TOPICS);
    expect(problems.some((p) => p.message.includes("exactly 1 correct choice"))).toBe(true);
  });

  it("flags two correct choices", () => {
    const question = makeQuestion({
      choices: [
        makeChoice({ label: "A", isCorrect: true }),
        makeChoice({ label: "B", isCorrect: true }),
        makeChoice({ label: "C", isCorrect: false }),
        makeChoice({ label: "D", isCorrect: false }),
      ],
    });
    const problems = validateQuestion(question, "ap-csa", KNOWN_TOPICS);
    expect(problems.some((p) => p.message.includes("exactly 1 correct choice"))).toBe(true);
  });

  it("flags a concept link that doesn't match unit/topic", () => {
    const question = makeQuestion({ conceptLink: "ap-csa/wrong-unit/wrong-topic" });
    const problems = validateQuestion(question, "ap-csa", KNOWN_TOPICS);
    expect(problems.some((p) => p.message.includes("conceptLink"))).toBe(true);
  });

  it("flags a unit/topic that isn't defined for the course", () => {
    const question = makeQuestion({ unit: "unit-9", topic: "topic-9", conceptLink: "ap-csa/unit-9/topic-9" });
    const problems = validateQuestion(question, "ap-csa", KNOWN_TOPICS);
    expect(problems.some((p) => p.message.includes("is not defined for this course"))).toBe(true);
  });
});

describe("validateFRQ", () => {
  function makeFRQ(overrides: Partial<FRQ> = {}): FRQ {
    return {
      id: "frq1",
      unit: "unit-1",
      topic: "topic-1",
      prompt: "Write a method.",
      pointValue: 3,
      rubric: [
        { id: "r1", points: 1, description: "a" },
        { id: "r2", points: 2, description: "b" },
      ],
      sampleResponse: "code",
      reviewed: false,
      ...overrides,
    };
  }

  it("passes when rubric points sum to pointValue", () => {
    expect(validateFRQ(makeFRQ(), KNOWN_TOPICS)).toEqual([]);
  });

  it("flags a rubric that doesn't sum to pointValue", () => {
    const frq = makeFRQ({ pointValue: 5 });
    const problems = validateFRQ(frq, KNOWN_TOPICS);
    expect(problems.some((p) => p.message.includes("rubric points sum to"))).toBe(true);
  });
});

describe("checkMarkdownBalance", () => {
  it("passes balanced $ and code fences", () => {
    expect(checkMarkdownBalance("The sum $x + y$ and ```code```", "stem")).toEqual([]);
  });

  it("flags an unclosed LaTeX delimiter", () => {
    const problems = checkMarkdownBalance("The sum $x + y is odd", "stem");
    expect(problems.some((p) => p.message.includes("LaTeX"))).toBe(true);
  });

  it("flags an unclosed code fence", () => {
    const problems = checkMarkdownBalance("```java\nint x = 1;", "stem");
    expect(problems.some((p) => p.message.includes("code fence"))).toBe(true);
  });
});

describe("validateUnit", () => {
  function makeUnit(overrides: Partial<Unit> = {}): Unit {
    return {
      slug: "unit-1",
      order: 1,
      name: "Unit 1",
      weightingMin: 2,
      weightingMax: 8,
      topics: [{ slug: "topic-1", order: 1, name: "Topic 1" }],
      ...overrides,
    };
  }

  it("passes a well-formed unit", () => {
    expect(validateUnit(makeUnit())).toEqual([]);
  });

  it("flags weightingMin greater than weightingMax", () => {
    const problems = validateUnit(makeUnit({ weightingMin: 10, weightingMax: 5 }));
    expect(problems.some((p) => p.message.includes("weightingMin"))).toBe(true);
  });

  it("flags duplicate topic slugs", () => {
    const problems = validateUnit(
      makeUnit({
        topics: [
          { slug: "topic-1", order: 1, name: "Topic 1" },
          { slug: "topic-1", order: 2, name: "Topic 1 Again" },
        ],
      }),
    );
    expect(problems.some((p) => p.message.includes("duplicate topic slug"))).toBe(true);
  });
});
