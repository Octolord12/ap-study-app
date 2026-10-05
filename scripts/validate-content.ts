import { existsSync, readdirSync, readFileSync } from "node:fs";
import path from "node:path";
import { CourseSchema, FRQSchema, QuestionSchema, UnitSchema } from "../src/lib/content/schema";
import { checkExamSupply, validateFRQ, validateQuestion, validateUnit } from "../src/lib/content/validate";

const CONTENT_DIR = path.join(__dirname, "../content");

interface Report {
  file: string;
  message: string;
}

const report: Report[] = [];

function fail(file: string, message: string) {
  report.push({ file, message });
}

function loadJson(filePath: string): unknown {
  return JSON.parse(readFileSync(filePath, "utf-8"));
}

function formatZodError(error: { issues: { path: PropertyKey[]; message: string }[] }): string {
  return error.issues.map((issue) => `${issue.path.join(".") || "(root)"}: ${issue.message}`).join("; ");
}

function validateCourse(courseSlug: string) {
  const courseDir = path.join(CONTENT_DIR, courseSlug);
  const courseFile = path.join(courseDir, "course.json");

  if (!existsSync(courseFile)) {
    fail(courseFile, "missing course.json");
    return;
  }

  const courseResult = CourseSchema.safeParse(loadJson(courseFile));
  if (!courseResult.success) {
    fail(courseFile, formatZodError(courseResult.error));
    return;
  }
  if (courseResult.data.slug !== courseSlug) {
    fail(courseFile, `slug "${courseResult.data.slug}" doesn't match folder name "${courseSlug}"`);
  }

  // --- units ---
  const unitSlugs = new Set<string>();
  const topicKeys = new Set<string>(); // "<unitSlug>/<topicSlug>"
  const unitsDir = path.join(courseDir, "units");

  if (!existsSync(unitsDir)) {
    fail(unitsDir, "missing units/ directory");
  } else {
    for (const file of readdirSync(unitsDir)) {
      const filePath = path.join(unitsDir, file);
      const result = UnitSchema.safeParse(loadJson(filePath));
      if (!result.success) {
        fail(filePath, formatZodError(result.error));
        continue;
      }
      const unit = result.data;

      if (unitSlugs.has(unit.slug)) fail(filePath, `duplicate unit slug "${unit.slug}"`);
      unitSlugs.add(unit.slug);
      for (const topic of unit.topics) topicKeys.add(`${unit.slug}/${topic.slug}`);

      for (const problem of validateUnit(unit)) fail(filePath, problem.message);
    }
  }

  // --- questions ---
  const seenIds = new Set<string>();
  const questionsDir = path.join(courseDir, "questions");

  if (existsSync(questionsDir)) {
    for (const file of readdirSync(questionsDir)) {
      const filePath = path.join(questionsDir, file);
      const raw = loadJson(filePath);
      if (!Array.isArray(raw)) {
        fail(filePath, "expected a JSON array of questions");
        continue;
      }
      raw.forEach((entry, index) => {
        const result = QuestionSchema.safeParse(entry);
        if (!result.success) {
          fail(filePath, `question[${index}]: ${formatZodError(result.error)}`);
          return;
        }
        const question = result.data;
        const label = `${filePath} (${question.id})`;

        if (seenIds.has(question.id)) fail(label, `duplicate id "${question.id}"`);
        seenIds.add(question.id);

        for (const problem of validateQuestion(question, courseSlug, topicKeys)) fail(label, problem.message);
      });
    }
  }

  // --- FRQs ---
  const frqsDir = path.join(courseDir, "frqs");
  const examFormat = courseResult.data.examFormat;
  const sectionTypes = examFormat.sections.map((s) => s.type);
  const promptTypes: string[] = [];

  if (existsSync(frqsDir)) {
    for (const file of readdirSync(frqsDir)) {
      const filePath = path.join(frqsDir, file);
      const raw = loadJson(filePath);
      if (!Array.isArray(raw)) {
        fail(filePath, "expected a JSON array of FRQ prompts");
        continue;
      }
      raw.forEach((entry, index) => {
        const result = FRQSchema.safeParse(entry);
        if (!result.success) {
          fail(filePath, `frq[${index}]: ${formatZodError(result.error)}`);
          return;
        }
        const frq = result.data;
        const label = `${filePath} (${frq.id})`;

        if (seenIds.has(frq.id)) fail(label, `duplicate id "${frq.id}" (MCQs and FRQs share one id space)`);
        seenIds.add(frq.id);

        promptTypes.push(frq.type ?? "FRQ");

        for (const problem of validateFRQ(frq, topicKeys, sectionTypes)) fail(label, problem.message);
      });
    }
  }

  for (const problem of checkExamSupply(examFormat.sections, promptTypes)) fail(courseFile, problem.message);
}

function main() {
  if (!existsSync(CONTENT_DIR)) {
    console.error(`No content directory at ${CONTENT_DIR}`);
    process.exit(1);
  }

  const courseSlugs = readdirSync(CONTENT_DIR, { withFileTypes: true })
    .filter((entry) => entry.isDirectory())
    .map((entry) => entry.name);

  for (const slug of courseSlugs) validateCourse(slug);

  if (report.length === 0) {
    console.log(`✓ Validated ${courseSlugs.length} course(s) in /content -- no problems found.`);
    return;
  }

  console.error(`✗ Found ${report.length} problem(s) in /content:\n`);
  for (const { file, message } of report) {
    console.error(`  ${file}\n    ${message}\n`);
  }
  process.exit(1);
}

main();
