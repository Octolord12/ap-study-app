import { describe, expect, it } from "vitest";
import { checkExamSupply, checkMarkdownBalance, validateDiagram, validateFRQ, validateQuestion, validateUnit } from "@/lib/content/validate";
import type { Choice, FRQ, Question, Unit } from "@/lib/content/schema";
import type { ForceDiagram, XYGraphDiagram } from "@/lib/content/diagram-schema";

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

  it("treats a missing type as FRQ and accepts it where the exam has a free-response section", () => {
    expect(validateFRQ(makeFRQ(), KNOWN_TOPICS, ["MCQ", "FRQ"])).toEqual([]);
  });

  it("flags an untyped prompt in a course whose exam has only SAQ, DBQ and LEQ sections", () => {
    const problems = validateFRQ(makeFRQ(), KNOWN_TOPICS, ["MCQ", "SAQ", "DBQ", "LEQ"]);
    expect(problems.some((p) => p.message.includes('type "FRQ" is not a section'))).toBe(true);
  });

  it("accepts a typed prompt that matches a section and flags one that does not", () => {
    expect(validateFRQ(makeFRQ({ type: "SAQ" }), KNOWN_TOPICS, ["MCQ", "SAQ", "LEQ"])).toEqual([]);
    expect(validateFRQ(makeFRQ({ type: "DBQ" }), KNOWN_TOPICS, ["MCQ", "FRQ"]).length).toBe(1);
  });
});

describe("checkExamSupply", () => {
  const sections = [
    { type: "MCQ", questionCount: 55 },
    { type: "SAQ", questionCount: 3 },
    { type: "LEQ", questionCount: 1 },
  ];

  it("passes when every non-MCQ section has enough prompts of its type", () => {
    expect(checkExamSupply(sections, ["SAQ", "SAQ", "SAQ", "SAQ", "LEQ"])).toEqual([]);
  });

  it("flags a section that has too few prompts, naming the type", () => {
    const problems = checkExamSupply(sections, ["SAQ", "SAQ", "FRQ"]);
    expect(problems.map((p) => p.message)).toEqual([
      "exam section SAQ needs 3 prompt(s) of that type, but the course has 2",
      "exam section LEQ needs 1 prompt(s) of that type, but the course has 0",
    ]);
  });

  it("does not count multiple choice, which is not drawn from the prompts", () => {
    expect(checkExamSupply([{ type: "MCQ", questionCount: 40 }], [])).toEqual([]);
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

describe("validateDiagram", () => {
  function makeXYGraph(overrides: Partial<XYGraphDiagram> = {}): XYGraphDiagram {
    return {
      type: "xy-graph",
      xLabel: "t (s)",
      yLabel: "v (m/s)",
      xMin: 0,
      xMax: 10,
      yMin: 0,
      yMax: 10,
      series: [{ points: [{ x: 0, y: 0 }, { x: 5, y: 5 }], color: "blue" }],
      ...overrides,
    };
  }

  function makeForceDiagram(overrides: Partial<ForceDiagram> = {}): ForceDiagram {
    return {
      type: "force-diagram",
      vectors: [
        { label: "Weight", angleDegrees: 270, magnitude: 5, color: "red" },
        { label: "Normal", angleDegrees: 90, magnitude: 5, color: "blue" },
      ],
      ...overrides,
    };
  }

  it("passes a well-formed xy-graph", () => {
    expect(validateDiagram(makeXYGraph())).toEqual([]);
  });

  it("flags a series point outside the x range", () => {
    const diagram = makeXYGraph({ series: [{ points: [{ x: 0, y: 0 }, { x: 15, y: 5 }], color: "blue" }] });
    const problems = validateDiagram(diagram);
    expect(problems.some((p) => p.message.includes("outside [xMin"))).toBe(true);
  });

  it("flags a series point outside the y range", () => {
    const diagram = makeXYGraph({ series: [{ points: [{ x: 0, y: 0 }, { x: 5, y: -5 }], color: "blue" }] });
    const problems = validateDiagram(diagram);
    expect(problems.some((p) => p.message.includes("outside [yMin"))).toBe(true);
  });

  it("passes a well-formed force-diagram", () => {
    expect(validateDiagram(makeForceDiagram())).toEqual([]);
  });

  it("flags duplicate vector labels", () => {
    const diagram = makeForceDiagram({
      vectors: [
        { label: "Weight", angleDegrees: 270, magnitude: 5, color: "red" },
        { label: "Weight", angleDegrees: 90, magnitude: 5, color: "blue" },
      ],
    });
    const problems = validateDiagram(diagram);
    expect(problems.some((p) => p.message.includes("duplicate vector label"))).toBe(true);
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
