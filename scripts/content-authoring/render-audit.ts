// Renders every string of a course's *-hard.json and *-bc.json files (every file, for a course that is wholly new: AP Biology), and every topic refresher, through the real content pipeline
// and reports KaTeX errors and raw LaTeX left visible.  Usage: npx tsx scripts/content-authoring/render-audit.ts ap-physics-1
import { existsSync, readFileSync, readdirSync } from "node:fs";
import path from "node:path";
import { renderChoiceTextToHtml, renderContentToHtml } from "../../src/lib/content/render";

const COURSE = process.argv[2];
if (!COURSE) throw new Error("usage: render-audit.ts <course-slug>");
const ROOT = path.join(__dirname, "../../content", COURSE);
const WHOLLY_NEW_COURSES = ["ap-biology"];

async function main() {
  const files = ["questions", "frqs"].flatMap((dir) =>
    readdirSync(path.join(ROOT, dir))
      .filter((f) => f.endsWith(".json") && (WHOLLY_NEW_COURSES.includes(COURSE) || f.endsWith("-hard.json") || f.endsWith("-bc.json")))
      .map((f) => path.join(ROOT, dir, f)),
  );
  let strings = 0;
  const bad: string[] = [];
  const check = async (label: string, md: string, choice = false) => {
    strings++;
    const html = choice ? await renderChoiceTextToHtml(md, COURSE) : await renderContentToHtml(md, COURSE);
    if (html.includes("katex-error")) bad.push(`KATEX ${label}: ${md.slice(0, 120)}`);
    const visible = html.replace(/<annotation[\s\S]*?<\/annotation>/g, "");
    if (/\\(frac|dfrac|sqrt|int|lim|cdot|le|ge|circ|times)\b/.test(visible) || /\$[^<]*\$/.test(visible)) bad.push(`RAW ${label}: ${md.slice(0, 120)}`);
  };
  for (const file of files) {
    for (const q of JSON.parse(readFileSync(file, "utf-8"))) {
      if (q.stem !== undefined) {
        await check(`${q.id} stem`, q.stem);
        await check(`${q.id} explanation`, q.explanation);
        for (const c of q.choices) {
          await check(`${q.id} ${c.label} text`, c.text, true);
          await check(`${q.id} ${c.label} expl`, c.explanation);
        }
      } else {
        await check(`${q.id} prompt`, q.prompt);
        await check(`${q.id} sample`, q.sampleResponse);
        for (const r of q.rubric) await check(`${q.id} ${r.id}`, r.description);
      }
    }
  }
  const refresherDir = path.join(ROOT, "refreshers");
  if (existsSync(refresherDir)) {
    for (const f of readdirSync(refresherDir).filter((name) => name.endsWith(".json"))) {
      files.push(path.join(refresherDir, f));
      for (const r of JSON.parse(readFileSync(path.join(refresherDir, f), "utf-8"))) await check(`${r.unit}/${r.topic} refresher`, r.body);
    }
  }
  console.log(JSON.stringify({ course: COURSE, files: files.length, strings, problems: bad.length }));
  for (const b of bad.slice(0, 40)) console.log(b);
}
main();
