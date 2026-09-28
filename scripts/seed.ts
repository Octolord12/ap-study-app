import { existsSync, readdirSync, readFileSync } from "node:fs";
import path from "node:path";
import { getDb } from "../src/lib/db";
import type { Difficulty } from "../src/generated/prisma/client";
import { CourseSchema, FRQSchema, QuestionSchema, UnitSchema } from "../src/lib/content/schema";

const CONTENT_DIR = path.join(__dirname, "../content");

function loadJson(filePath: string): unknown {
  return JSON.parse(readFileSync(filePath, "utf-8"));
}

// Content is validated separately by validate-content.ts (run that first, or
// via `npm run db:seed` which chains them). This script trusts its shape and
// upserts everything, so re-running it after editing content is safe.
async function seedCourse(courseSlug: string) {
  const db = getDb();
  const courseDir = path.join(CONTENT_DIR, courseSlug);

  const course = CourseSchema.parse(loadJson(path.join(courseDir, "course.json")));

  const dbCourse = await db.course.upsert({
    where: { slug: course.slug },
    create: {
      slug: course.slug,
      name: course.name,
      description: course.description,
      colorTheme: course.colorTheme,
      examFormat: course.examFormat,
    },
    update: {
      name: course.name,
      description: course.description,
      colorTheme: course.colorTheme,
      examFormat: course.examFormat,
    },
  });

  const unitIdBySlug = new Map<string, string>();
  const topicIdByKey = new Map<string, string>(); // "<unitSlug>/<topicSlug>" -> id

  const unitFiles = readdirSync(path.join(courseDir, "units")).sort();
  for (const file of unitFiles) {
    const unit = UnitSchema.parse(loadJson(path.join(courseDir, "units", file)));

    const dbUnit = await db.unit.upsert({
      where: { courseId_slug: { courseId: dbCourse.id, slug: unit.slug } },
      create: {
        courseId: dbCourse.id,
        slug: unit.slug,
        name: unit.name,
        order: unit.order,
        weightingMin: unit.weightingMin,
        weightingMax: unit.weightingMax,
      },
      update: {
        name: unit.name,
        order: unit.order,
        weightingMin: unit.weightingMin,
        weightingMax: unit.weightingMax,
      },
    });
    unitIdBySlug.set(unit.slug, dbUnit.id);

    for (const topic of unit.topics) {
      const dbTopic = await db.topic.upsert({
        where: { unitId_slug: { unitId: dbUnit.id, slug: topic.slug } },
        create: { unitId: dbUnit.id, slug: topic.slug, name: topic.name, order: topic.order },
        update: { name: topic.name, order: topic.order },
      });
      topicIdByKey.set(`${unit.slug}/${topic.slug}`, dbTopic.id);
    }
  }

  let questionCount = 0;
  const questionsDir = path.join(courseDir, "questions");
  if (existsSync(questionsDir)) {
    for (const file of readdirSync(questionsDir)) {
      const questions = QuestionSchema.array().parse(loadJson(path.join(questionsDir, file)));

      for (const q of questions) {
        const unitId = unitIdBySlug.get(q.unit);
        const topicId = topicIdByKey.get(`${q.unit}/${q.topic}`);
        if (!unitId || !topicId) {
          throw new Error(`${file}: question ${q.id} references unknown unit/topic "${q.unit}/${q.topic}"`);
        }

        const choiceData = q.choices.map((c) => ({
          label: c.label,
          text: c.text,
          isCorrect: c.isCorrect,
          explanation: c.explanation,
        }));

        await db.question.upsert({
          where: { id: q.id },
          create: {
            id: q.id,
            courseId: dbCourse.id,
            unitId,
            topicId,
            difficulty: q.difficulty.toUpperCase() as Difficulty,
            stem: q.stem,
            explanation: q.explanation,
            conceptLink: q.conceptLink,
            reviewed: q.reviewed,
            choices: { create: choiceData },
          },
          update: {
            unitId,
            topicId,
            difficulty: q.difficulty.toUpperCase() as Difficulty,
            stem: q.stem,
            explanation: q.explanation,
            conceptLink: q.conceptLink,
            reviewed: q.reviewed,
            choices: { deleteMany: {}, create: choiceData },
          },
        });
        questionCount++;
      }
    }
  }

  let frqCount = 0;
  const frqsDir = path.join(courseDir, "frqs");
  if (existsSync(frqsDir)) {
    for (const file of readdirSync(frqsDir)) {
      const frqs = FRQSchema.array().parse(loadJson(path.join(frqsDir, file)));

      for (const frq of frqs) {
        const unitId = unitIdBySlug.get(frq.unit);
        const topicId = topicIdByKey.get(`${frq.unit}/${frq.topic}`);
        if (!unitId || !topicId) {
          throw new Error(`${file}: FRQ ${frq.id} references unknown unit/topic "${frq.unit}/${frq.topic}"`);
        }

        await db.fRQPrompt.upsert({
          where: { id: frq.id },
          create: {
            id: frq.id,
            courseId: dbCourse.id,
            unitId,
            topicId,
            prompt: frq.prompt,
            pointValue: frq.pointValue,
            rubric: frq.rubric,
            sampleResponse: frq.sampleResponse,
            reviewed: frq.reviewed,
          },
          update: {
            unitId,
            topicId,
            prompt: frq.prompt,
            pointValue: frq.pointValue,
            rubric: frq.rubric,
            sampleResponse: frq.sampleResponse,
            reviewed: frq.reviewed,
          },
        });
        frqCount++;
      }
    }
  }

  console.log(
    `✓ ${course.name}: ${unitIdBySlug.size} units, ${topicIdByKey.size} topics, ${questionCount} questions, ${frqCount} FRQs`,
  );
}

async function main() {
  const courseSlugs = readdirSync(CONTENT_DIR, { withFileTypes: true })
    .filter((entry) => entry.isDirectory())
    .map((entry) => entry.name);

  for (const slug of courseSlugs) {
    await seedCourse(slug);
  }
}

main()
  .catch((error) => {
    console.error(error);
    process.exitCode = 1;
  })
  .finally(async () => {
    await getDb().$disconnect();
  });
