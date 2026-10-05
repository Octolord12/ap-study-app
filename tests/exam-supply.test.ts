import fs from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import { pickExamFrqIds } from "@/lib/study/exam-selection";

// The shipped content, not a fixture: every course must be able to build the exam its examFormat describes.

interface Frq {
  id: string;
  type?: string;
  prompt: string;
}
interface Section {
  type: string;
  questionCount: number;
}

const root = path.resolve(import.meta.dirname, "../content");
const courses = fs.readdirSync(root, { withFileTypes: true }).filter((d) => d.isDirectory()).map((d) => d.name);

function frqsOf(course: string): Frq[] {
  const dir = path.join(root, course, "frqs");
  return fs.readdirSync(dir).filter((f) => f.endsWith(".json")).flatMap((f) => JSON.parse(fs.readFileSync(path.join(dir, f), "utf8")) as Frq[]);
}
const sectionsOf = (course: string): Section[] => JSON.parse(fs.readFileSync(path.join(root, course, "course.json"), "utf8")).examFormat.sections;

describe.each(courses)("%s exam", (course) => {
  const sections = sectionsOf(course);
  const prompts = frqsOf(course).map((f) => ({ id: f.id, type: f.type ?? "FRQ" }));

  it("builds exactly the free-response items its exam format asks for", () => {
    const wanted = sections.filter((s) => s.type !== "MCQ").reduce((n, s) => n + s.questionCount, 0);
    const picked = pickExamFrqIds(sections, prompts);
    expect(picked).toHaveLength(wanted);
    const byId = new Map(prompts.map((p) => [p.id, p.type]));
    const order = picked.map((id) => byId.get(id));
    expect(order).toEqual(sections.filter((s) => s.type !== "MCQ").flatMap((s) => Array(s.questionCount).fill(s.type)));
  });

  it("has no prompt whose type is not one of its exam sections", () => {
    const allowed = new Set(sections.map((s) => s.type));
    expect(prompts.filter((p) => !allowed.has(p.type)).map((p) => p.id)).toEqual([]);
  });
});

describe("ap-world prompt types match what the prompts say", () => {
  const frqs = frqsOf("ap-world");
  it("types every prompt as the kind its text and id show", () => {
    for (const f of frqs) {
      const expected = /^\s*\*\*Long Essay Question\*\*/.test(f.prompt) ? "LEQ" : /^\s*\*\*Document-Based Question\*\*/.test(f.prompt) ? "DBQ" : "SAQ";
      expect({ id: f.id, type: f.type }).toEqual({ id: f.id, type: expected });
    }
  });
});
