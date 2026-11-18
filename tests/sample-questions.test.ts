import { readdirSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import { SAMPLE_QUESTIONS } from "@/lib/marketing/sample-question";

const courseSlugs = readdirSync(path.resolve(import.meta.dirname, "../content"), { withFileTypes: true })
  .filter((entry) => entry.isDirectory())
  .map((entry) => entry.name);

describe("the landing page's sample questions", () => {
  it("has one for every course, so every tab of the binder has a question behind it", () => {
    expect(SAMPLE_QUESTIONS.map((q) => q.courseSlug).sort()).toEqual([...courseSlugs].sort());
  });

  it("has four choices labelled A to D with exactly one right answer, each with its reason", () => {
    for (const q of SAMPLE_QUESTIONS) {
      expect(q.choices.map((c) => c.label), q.course).toEqual(["A", "B", "C", "D"]);
      expect(q.choices.filter((c) => c.isCorrect), q.course).toHaveLength(1);
      for (const c of q.choices) expect(c.explanation.length, `${q.course} ${c.label}`).toBeGreaterThan(20);
    }
  });

  it("never refers to a choice by letter, because the choices are shuffled on every visit", () => {
    const pointer = /\b(choices?|options?|answers?|responses?|statements?|letter)\s+\(?[A-E]\)?(?![A-Za-z0-9_(])/i;
    for (const q of SAMPLE_QUESTIONS) {
      const texts = [q.stem, q.explanation, ...q.choices.flatMap((c) => [c.text, c.explanation])];
      for (const t of texts) expect(t, q.course).not.toMatch(pointer);
    }
  });

  it("does not let the right answer be the longest choice more often than chance", () => {
    const plain = (s: string) => s.replace(/\$[^$]*\$/g, "");
    const longest = SAMPLE_QUESTIONS.filter((q) => {
      const lengths = q.choices.map((c) => plain(c.text).length);
      const right = plain(q.choices.find((c) => c.isCorrect)!.text).length;
      return lengths.filter((n) => n >= right).length === 1 && Math.max(...lengths) >= 30;
    });
    expect(longest.length).toBeLessThanOrEqual(3);
  });
});
