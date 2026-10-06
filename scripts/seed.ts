import { existsSync, readdirSync, readFileSync } from "node:fs";
import path from "node:path";
import { getDb } from "../src/lib/db";
import { Prisma, type Difficulty } from "../src/generated/prisma/client";
import { CourseSchema, FRQSchema, QuestionSchema, UnitSchema } from "../src/lib/content/schema";
import { frqContentChanged, nextReviewedFlag, questionContentChanged } from "../src/lib/content/review-state";

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

  // Approvals made in /admin/review live only in the database, so a re-seed has to look at what is
  // stored: an approved item stays approved unless this seed would change its content.
  const storedQuestions = new Map(
    (await db.question.findMany({ where: { courseId: dbCourse.id }, include: { choices: true } })).map((q) => [q.id, q]),
  );
  const storedFrqs = new Map((await db.fRQPrompt.findMany({ where: { courseId: dbCourse.id } })).map((f) => [f.id, f]));
  let approvalsKept = 0;
  let approvalsReset = 0;

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

        const stored = storedQuestions.get(q.id) ?? null;
        const reviewed = nextReviewedFlag(stored, stored ? questionContentChanged(stored, q) : false, q.reviewed);
        if (stored?.reviewed) {
          if (reviewed) approvalsKept++;
          else approvalsReset++;
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
            diagram: q.diagram ?? undefined,
            reviewed,
            choices: { create: choiceData },
          },
          update: {
            unitId,
            topicId,
            difficulty: q.difficulty.toUpperCase() as Difficulty,
            stem: q.stem,
            explanation: q.explanation,
            conceptLink: q.conceptLink,
            diagram: q.diagram ?? Prisma.JsonNull,
            reviewed,
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

        const storedFrq = storedFrqs.get(frq.id) ?? null;
        const frqReviewed = nextReviewedFlag(storedFrq, storedFrq ? frqContentChanged(storedFrq, frq) : false, frq.reviewed);
        if (storedFrq?.reviewed) {
          if (frqReviewed) approvalsKept++;
          else approvalsReset++;
        }

        await db.fRQPrompt.upsert({
          where: { id: frq.id },
          create: {
            id: frq.id,
            courseId: dbCourse.id,
            unitId,
            topicId,
            type: frq.type ?? "FRQ",
            prompt: frq.prompt,
            pointValue: frq.pointValue,
            rubric: frq.rubric,
            sampleResponse: frq.sampleResponse,
            diagram: frq.diagram ?? undefined,
            reviewed: frqReviewed,
          },
          update: {
            unitId,
            topicId,
            type: frq.type ?? "FRQ",
            prompt: frq.prompt,
            pointValue: frq.pointValue,
            rubric: frq.rubric,
            sampleResponse: frq.sampleResponse,
            diagram: frq.diagram ?? Prisma.JsonNull,
            reviewed: frqReviewed,
          },
        });
        frqCount++;
      }
    }
  }

  console.log(
    `✓ ${course.name}: ${unitIdBySlug.size} units, ${topicIdByKey.size} topics, ${questionCount} questions, ${frqCount} FRQs` +
      (approvalsKept + approvalsReset > 0 ? ` (approvals kept: ${approvalsKept}, reset because the content changed: ${approvalsReset})` : ""),
  );
}

async function main() {
  const allSlugs = readdirSync(CONTENT_DIR, { withFileTypes: true })
    .filter((entry) => entry.isDirectory())
    .map((entry) => entry.name);

  // `npm run content:seed -- ap-us-history` seeds just that course (the whole bank takes 10+ minutes
  // and rewrites rows that did not change); with no arguments every course is seeded.
  const requested = process.argv.slice(2).filter((arg) => !arg.startsWith("-"));
  const unknown = requested.filter((slug) => !allSlugs.includes(slug));
  if (unknown.length > 0) {
    throw new Error(`No such course folder in /content: ${unknown.join(", ")} (have: ${allSlugs.join(", ")})`);
  }
  const courseSlugs = requested.length > 0 ? allSlugs.filter((slug) => requested.includes(slug)) : allSlugs;

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
