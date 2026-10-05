import type { Diagram } from "./diagram-schema";
import type { FRQ, Question, Unit } from "./schema";

export interface Problem {
  message: string;
}

const EXPECTED_LABELS = ["A", "B", "C", "D", "E"];

// Pure checks, no file I/O -- scripts/validate-content.ts does the directory
// walking and calls these. Kept separate so the rules themselves are unit-testable.

export function validateUnit(unit: Unit): Problem[] {
  const problems: Problem[] = [];

  if (unit.weightingMin > unit.weightingMax) {
    problems.push({
      message: `weightingMin (${unit.weightingMin}) > weightingMax (${unit.weightingMax})`,
    });
  }

  const seenTopicSlugs = new Set<string>();
  for (const topic of unit.topics) {
    if (seenTopicSlugs.has(topic.slug)) {
      problems.push({ message: `duplicate topic slug "${topic.slug}" in unit "${unit.slug}"` });
    }
    seenTopicSlugs.add(topic.slug);
  }

  return problems;
}

export function validateQuestion(question: Question, courseSlug: string, knownTopicKeys: Set<string>): Problem[] {
  const problems: Problem[] = [];

  if (!knownTopicKeys.has(`${question.unit}/${question.topic}`)) {
    problems.push({ message: `unit/topic "${question.unit}/${question.topic}" is not defined for this course` });
  }

  const correctCount = question.choices.filter((choice) => choice.isCorrect).length;
  if (correctCount !== 1) {
    problems.push({ message: `expected exactly 1 correct choice, found ${correctCount}` });
  }

  const expectedLabels = EXPECTED_LABELS.slice(0, question.choices.length);
  const actualLabels = question.choices.map((choice) => choice.label);
  if (JSON.stringify(actualLabels) !== JSON.stringify(expectedLabels)) {
    problems.push({
      message: `choice labels should be ${expectedLabels.join(", ")} in order, got ${actualLabels.join(", ")}`,
    });
  }

  const expectedConceptLink = `${courseSlug}/${question.unit}/${question.topic}`;
  if (question.conceptLink !== expectedConceptLink) {
    problems.push({ message: `conceptLink "${question.conceptLink}" should be "${expectedConceptLink}"` });
  }

  problems.push(...checkMarkdownBalance(question.stem, "stem"));
  if (question.diagram) {
    problems.push(...validateDiagram(question.diagram));
  }

  return problems;
}

export function validateFRQ(frq: FRQ, knownTopicKeys: Set<string>, examSectionTypes?: readonly string[]): Problem[] {
  const problems: Problem[] = [];

  const type = frq.type ?? "FRQ";
  if (examSectionTypes && !examSectionTypes.includes(type)) {
    problems.push({
      message: `type "${type}" is not a section of this course's exam (${examSectionTypes.filter((t) => t !== "MCQ").join(", ")}); set "type" on the prompt`,
    });
  }

  if (!knownTopicKeys.has(`${frq.unit}/${frq.topic}`)) {
    problems.push({ message: `unit/topic "${frq.unit}/${frq.topic}" is not defined for this course` });
  }

  const rubricSum = frq.rubric.reduce((sum, line) => sum + line.points, 0);
  if (rubricSum !== frq.pointValue) {
    problems.push({ message: `rubric points sum to ${rubricSum}, expected pointValue ${frq.pointValue}` });
  }

  problems.push(...checkMarkdownBalance(frq.prompt, "prompt"));
  if (frq.diagram) {
    problems.push(...validateDiagram(frq.diagram));
  }

  return problems;
}

export function validateDiagram(diagram: Diagram): Problem[] {
  const problems: Problem[] = [];

  if (diagram.type === "xy-graph") {
    for (const series of diagram.series) {
      for (const point of series.points) {
        if (point.x < diagram.xMin || point.x > diagram.xMax) {
          problems.push({
            message: `xy-graph: point x=${point.x} is outside [xMin=${diagram.xMin}, xMax=${diagram.xMax}]`,
          });
        }
        if (point.y < diagram.yMin || point.y > diagram.yMax) {
          problems.push({
            message: `xy-graph: point y=${point.y} is outside [yMin=${diagram.yMin}, yMax=${diagram.yMax}]`,
          });
        }
      }
    }
  }

  if (diagram.type === "force-diagram") {
    const seenLabels = new Set<string>();
    for (const vector of diagram.vectors) {
      if (seenLabels.has(vector.label)) {
        problems.push({ message: `force-diagram: duplicate vector label "${vector.label}"` });
      }
      seenLabels.add(vector.label);
    }
  }

  return problems;
}

// Naive but effective: catches the most common authoring slip (an unclosed
// $...$ or ```...``` block), which would otherwise render as garbled markdown.
export function checkMarkdownBalance(text: string, fieldName: string): Problem[] {
  const problems: Problem[] = [];

  const dollarCount = (text.match(/\$/g) ?? []).length;
  if (dollarCount % 2 !== 0) {
    problems.push({ message: `${fieldName}: odd number of "$" -- likely unclosed LaTeX` });
  }

  const fenceCount = (text.match(/```/g) ?? []).length;
  if (fenceCount % 2 !== 0) {
    problems.push({ message: `${fieldName}: odd number of "\`\`\`" -- unclosed code fence` });
  }

  return problems;
}

// Every non-multiple-choice exam section must have at least as many prompts of its type as it asks
// for, or the exam simulator would hand out a short exam without anyone noticing.
export function checkExamSupply(sections: readonly { type: string; questionCount: number }[], promptTypes: readonly string[]): Problem[] {
  const problems: Problem[] = [];
  for (const section of sections) {
    if (section.type === "MCQ") continue;
    const have = promptTypes.filter((t) => t === section.type).length;
    if (have < section.questionCount) {
      problems.push({ message: `exam section ${section.type} needs ${section.questionCount} prompt(s) of that type, but the course has ${have}` });
    }
  }
  return problems;
}
