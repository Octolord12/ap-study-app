import type { CladogramNode, Diagram } from "./diagram-schema";
import { validateBoxplot, validateDensityCurve, validateDotplot, validateHistogram, validateScatterplot } from "./validate-stats-diagrams";
import { examDraws } from "./exam-sections";
import type { FRQ, Question, Refresher, Unit } from "./schema";

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

// A refresher is read in a minute or two: long enough to teach something, short enough that a student
// who just missed a question will actually read it. The page already shows the topic name as its title,
// so the body must not start its own top-level headings.
export const REFRESHER_MIN_CHARS = 400;
export const REFRESHER_MAX_CHARS = 3500;

export function validateRefresher(refresher: Refresher, knownTopicKeys: Set<string>): Problem[] {
  const problems: Problem[] = [];

  if (!knownTopicKeys.has(`${refresher.unit}/${refresher.topic}`)) {
    problems.push({ message: `unit/topic "${refresher.unit}/${refresher.topic}" is not defined for this course` });
  }

  const length = refresher.body.trim().length;
  if (length < REFRESHER_MIN_CHARS) {
    problems.push({ message: `body is ${length} characters; a refresher needs at least ${REFRESHER_MIN_CHARS}` });
  }
  if (length > REFRESHER_MAX_CHARS) {
    problems.push({ message: `body is ${length} characters; keep a refresher under ${REFRESHER_MAX_CHARS}` });
  }
  if (/^#{1,2}\s/m.test(refresher.body)) {
    problems.push({ message: 'body starts a "#" or "##" heading; use "###" (the page already has the topic name as its title)' });
  }

  // The markdown pipeline has no table support, so a table would show as rows of pipe characters.
  if (/^\s*\|.*\|\s*$/m.test(refresher.body)) {
    problems.push({ message: "body has a markdown table; tables are not supported, use a list or a sentence" });
  }

  problems.push(...checkMarkdownBalance(refresher.body, "body"));
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

  if (diagram.type === "data-table") {
    diagram.rows.forEach((row, r) => {
      if (row.length !== diagram.columns.length) {
        problems.push({ message: `data-table: row ${r + 1} has ${row.length} cell(s) but there are ${diagram.columns.length} column(s)` });
      }
    });
  }

  if (diagram.type === "bar-graph") problems.push(...validateBarGraph(diagram));

  if (diagram.type === "cladogram") problems.push(...validateCladogram(diagram.root));

  if (diagram.type === "histogram") problems.push(...validateHistogram(diagram));
  if (diagram.type === "boxplot") problems.push(...validateBoxplot(diagram));
  if (diagram.type === "dotplot") problems.push(...validateDotplot(diagram));
  if (diagram.type === "scatterplot") problems.push(...validateScatterplot(diagram));
  if (diagram.type === "density-curve") problems.push(...validateDensityCurve(diagram));

  return problems;
}

function validateBarGraph(diagram: Extract<Diagram, { type: "bar-graph" }>): Problem[] {
  const problems: Problem[] = [];
  if (!(diagram.yMax > diagram.yMin)) problems.push({ message: `bar-graph: yMax (${diagram.yMax}) must be greater than yMin (${diagram.yMin})` });
  if (new Set(diagram.categories).size !== diagram.categories.length) problems.push({ message: "bar-graph: duplicate category name" });
  diagram.series.forEach((series, si) => {
    const name = series.label ?? `series ${si + 1}`;
    if (diagram.series.length > 1 && !series.label) problems.push({ message: `bar-graph: series ${si + 1} needs a label (the legend names them)` });
    if (series.values.length !== diagram.categories.length) {
      problems.push({ message: `bar-graph: ${name} has ${series.values.length} value(s) for ${diagram.categories.length} categories` });
    }
    if (series.errors && series.errors.length !== diagram.categories.length) {
      problems.push({ message: `bar-graph: ${name} has ${series.errors.length} error value(s) for ${diagram.categories.length} categories` });
    }
    series.values.forEach((value, ci) => {
      const error = series.errors?.[ci] ?? 0;
      if (value - error < diagram.yMin || value + error > diagram.yMax) {
        problems.push({ message: `bar-graph: ${name}, ${diagram.categories[ci] ?? `category ${ci + 1}`}: ${value}${error ? ` ± ${error}` : ""} does not fit in [${diagram.yMin}, ${diagram.yMax}]` });
      }
    });
  });
  return problems;
}

export const CLADOGRAM_MAX_TIPS = 12;
export const CLADOGRAM_MAX_DEPTH = 6;

function validateCladogram(root: CladogramNode): Problem[] {
  const problems: Problem[] = [];
  if (!root.children?.length) problems.push({ message: "cladogram: the root needs branches (children)" });
  const tips: string[] = [];
  const marks: string[] = [];
  let deepest = 0;
  const visit = (node: CladogramNode, depth: number) => {
    deepest = Math.max(deepest, depth);
    if (node.mark) marks.push(node.mark);
    if (node.children?.length) {
      if (node.label) problems.push({ message: `cladogram: "${node.label}" labels a branching point; only tips have labels` });
      node.children.forEach((child) => visit(child, depth + 1));
    } else if (node.label) {
      tips.push(node.label);
    } else if (node !== root) {
      problems.push({ message: "cladogram: a tip has no label" });
    }
  };
  visit(root, 0);
  if (tips.length > CLADOGRAM_MAX_TIPS) problems.push({ message: `cladogram: ${tips.length} tips; the most drawn is ${CLADOGRAM_MAX_TIPS}` });
  if (deepest > CLADOGRAM_MAX_DEPTH) problems.push({ message: `cladogram: ${deepest} levels deep; the most drawn is ${CLADOGRAM_MAX_DEPTH}` });
  if (new Set(tips).size !== tips.length) problems.push({ message: "cladogram: two tips have the same label" });
  if (new Set(marks).size !== marks.length) problems.push({ message: "cladogram: two nodes have the same mark" });
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
export function checkExamSupply(sections: readonly { type: string; questionCount: number; kinds?: readonly string[] }[], promptTypes: readonly string[]): Problem[] {
  const problems: Problem[] = [];
  for (const draw of examDraws(sections)) {
    const have = promptTypes.filter((t) => t === draw.type).length;
    if (have < draw.count) {
      problems.push({ message: `exam section ${draw.type} needs ${draw.count} prompt(s) of that type, but the course has ${have}` });
    }
  }
  return problems;
}
