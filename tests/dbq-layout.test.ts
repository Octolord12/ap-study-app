import fs from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import { renderContentToHtml } from "@/lib/content/render";

// Written as three consecutive lines ("**Document 1**", "Source: ...", the quotation), markdown joins a DBQ document into
// one paragraph, so the label, source and quotation ran together on screen. Every document must be label, Source and a
// blockquoted quotation, each separated by a blank line (scripts/content-authoring/dbq-layout/apply.py puts a prompt in that form).

interface Frq {
  id: string;
  type?: string;
  prompt: string;
}

const root = path.resolve(import.meta.dirname, "../content");
const dbqs: { course: string; frq: Frq }[] = fs.readdirSync(root).flatMap((course) => {
  const dir = path.join(root, course, "frqs");
  if (!fs.existsSync(dir)) return [];
  return fs
    .readdirSync(dir)
    .filter((f) => f.endsWith(".json"))
    .flatMap((f) => (JSON.parse(fs.readFileSync(path.join(dir, f), "utf8")) as Frq[]).filter((x) => x.type === "DBQ").map((frq) => ({ course, frq })));
});

const DOCUMENT = /\*\*Document (\d+)\*\*\n\nSource: [^\n]+\n\n> "[^\n]+/g;

describe("DBQ document layout", () => {
  it("finds the document-based questions it is meant to guard", () => {
    expect(dbqs.length).toBeGreaterThanOrEqual(8);
  });

  it.each(dbqs.map((d) => [d.frq.id, d] as const))("%s: every document is a label, a source line and a blockquote, on separate lines", (_id, { frq }) => {
    const labels = frq.prompt.match(/\*\*Document \d+\*\*/g) ?? [];
    expect(labels.length).toBeGreaterThan(0);
    const wellFormed = frq.prompt.match(DOCUMENT) ?? [];
    expect(wellFormed).toHaveLength(labels.length);
    expect(frq.prompt).not.toMatch(/\*\*Document \d+\*\*\nSource:/);
    expect(frq.prompt).not.toMatch(/\nSource: [^\n]*\n"/);
  });

  it("renders each document as its own label, source and blockquote", async () => {
    const { course, frq } = dbqs[0];
    const html = await renderContentToHtml(frq.prompt, course);
    const count = (frq.prompt.match(/\*\*Document \d+\*\*/g) ?? []).length;
    expect(html.match(/<blockquote>/g)).toHaveLength(count);
    expect(html.match(/<p>Source: /g)).toHaveLength(count);
    expect(html).not.toMatch(/<strong>Document \d+<\/strong> Source:/);
  });
});
