import fs from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";

// Choices are shuffled, so any text that points at a choice by letter has to go
// through remapChoiceLetters. That only understands "choice/option/answer/...
// X". This audit makes sure no authored text uses a form it can't fix, and that
// every letter it does reference exists on that question.

interface Q {
  id: string;
  stem: string;
  explanation: string;
  choices: { label: string; text: string; explanation: string }[];
}

const root = path.resolve(import.meta.dirname, "../content");
const questions: Q[] = fs
  .readdirSync(root)
  .flatMap((course) => {
    const dir = path.join(root, course, "questions");
    return fs.existsSync(dir) ? fs.readdirSync(dir).filter((f) => f.endsWith(".json")).flatMap((f) => JSON.parse(fs.readFileSync(path.join(dir, f), "utf8")) as Q[]) : [];
  });

const fieldsOf = (q: Q) => [q.stem, q.explanation, ...q.choices.flatMap((c) => [c.text, c.explanation])];

const SUPPORTED = /\b(?:[Cc]hoices?|[Oo]ptions?|[Aa]nswers?|[Rr]esponses?|[Ss]tatements?|[Ll]etter)\s+\(?([A-E])\)?(?![A-Za-z0-9_(]|\.[A-Za-z0-9_])/g;
// Forms that would also point at a choice but that remapChoiceLetters leaves alone.
const UNSUPPORTED = [/(?<![\w(])\([A-E]\)(?![\w(])/, /\b(?:both|either|neither)\s+[A-E]\b/, /\b(?:all|none) of the above\b/i];

describe("authored text and shuffled choices", () => {
  it("has questions to audit", () => {
    expect(questions.length).toBeGreaterThan(1000);
  });

  it("only refers to choices in the form the renderer rewrites", () => {
    const offenders: string[] = [];
    for (const q of questions) {
      for (const text of fieldsOf(q)) {
        for (const re of UNSUPPORTED) if (re.test(text)) offenders.push(`${q.id}: ${text.slice(0, 80)}`);
      }
    }
    expect(offenders).toEqual([]);
  });

  it("only refers to letters that exist on that question", () => {
    const offenders: string[] = [];
    for (const q of questions) {
      const labels = new Set(q.choices.map((c) => c.label));
      for (const text of fieldsOf(q)) {
        for (const m of text.matchAll(SUPPORTED)) if (!labels.has(m[1])) offenders.push(`${q.id}: ${m[0]}`);
      }
    }
    expect(offenders).toEqual([]);
  });
});
