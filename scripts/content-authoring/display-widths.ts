// Renders every refresher of a course through the real pipeline and writes the HTML to public/__tmp-displays.json, so the widths
// of its display equations can be measured in the browser:
// start the dev server, open any page that loads the global CSS (such as /privacy), fetch /__tmp-displays.json, put each refresher's HTML
// into a 343px `.reading.prose` box (the text column of a 375px phone) and compare each `.katex-display`'s scrollWidth with 343.
// Delete public/__tmp-displays.json afterwards (the repo has no public/ folder otherwise).
// Usage: npx tsx scripts/content-authoring/display-widths.ts ap-calc-bc
import { mkdirSync, readFileSync, readdirSync, writeFileSync } from "node:fs";
import path from "node:path";
import { renderContentToHtml } from "../../src/lib/content/render";

const COURSE = process.argv[2];
if (!COURSE) throw new Error("usage: display-widths.ts <course-slug>");
const ROOT = path.join(__dirname, "../../content", COURSE, "refreshers");

async function main() {
  const out: { label: string; html: string }[] = [];
  for (const file of readdirSync(ROOT).filter((f) => f.endsWith(".json"))) {
    for (const r of JSON.parse(readFileSync(path.join(ROOT, file), "utf-8"))) out.push({ label: `${r.unit}/${r.topic}`, html: await renderContentToHtml(r.body, COURSE) });
  }
  mkdirSync(path.join(__dirname, "../../public"), { recursive: true });
  writeFileSync(path.join(__dirname, "../../public/__tmp-displays.json"), JSON.stringify(out));
  console.log(`${out.length} rendered refreshers written to public/__tmp-displays.json`);
}
main();
