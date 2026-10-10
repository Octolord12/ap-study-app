import { getDb } from "@/lib/db";
import { getUserGamificationStats } from "@/lib/gamification/queries";
import { computeUnitMastery } from "@/lib/study/mastery";
import { daysAgo, toActivityEntries } from "@/lib/study/week-activity";
import { weakTopics } from "@/lib/study/weak-topics";

// The numbers behind the student's Progress page, in one place so the page a student sees and the read-only page a parent sees (src/app/share)
// are built from the same loader and cannot drift apart. Study activity only: no name, email, answers' text, friends or classes.
export async function loadProgressCore(userId: string) {
  const db = getDb();

  // Eight days back, so the browser can pick out its own last seven local days.
  const since = daysAgo(8);
  const [enrollments, attempts, stats, weekQuestions, weekFrqs, weekExams] = await Promise.all([
    db.enrollment.findMany({
      where: { userId },
      include: {
        course: { include: { units: { orderBy: { order: "asc" }, include: { _count: { select: { questions: true } } } } } },
      },
    }),
    db.questionAttempt.findMany({
      where: { userId },
      select: {
        questionId: true,
        correct: true,
        createdAt: true,
        question: {
          select: {
            unitId: true,
            topic: { select: { id: true, name: true, slug: true } },
            unit: { select: { slug: true, name: true, course: { select: { slug: true, name: true } } } },
          },
        },
      },
    }),
    getUserGamificationStats(userId),
    db.questionAttempt.findMany({ where: { userId, createdAt: { gte: since } }, select: { createdAt: true, correct: true, timeSpentMs: true } }),
    db.fRQAttempt.findMany({ where: { userId, createdAt: { gte: since } }, select: { createdAt: true } }),
    db.examAttempt.findMany({ where: { userId, completedAt: { gte: since } }, select: { startedAt: true, completedAt: true } }),
  ]);

  const weekEntries = toActivityEntries({
    questions: weekQuestions,
    frqs: weekFrqs,
    exams: weekExams.flatMap((e) => (e.completedAt ? [{ startedAt: e.startedAt, completedAt: e.completedAt }] : [])),
  });

  const weakest = weakTopics(
    attempts.map((a) => ({
      questionId: a.questionId,
      topicId: a.question.topic.id,
      topicName: a.question.topic.name,
      topicSlug: a.question.topic.slug,
      unitSlug: a.question.unit.slug,
      unitName: a.question.unit.name,
      courseSlug: a.question.unit.course.slug,
      courseName: a.question.unit.course.name,
      correct: a.correct,
      createdAt: a.createdAt,
    })),
  );

  const mastery = computeUnitMastery(
    attempts.map((a) => ({ questionId: a.questionId, unitId: a.question.unitId, correct: a.correct, createdAt: a.createdAt })),
  );
  const masteryByUnitId = new Map(mastery.map((m) => [m.unitId, m]));

  const courses = enrollments.map(({ course }) => {
    const units = course.units.map((unit) => ({
      id: unit.id,
      slug: unit.slug,
      name: unit.name,
      total: unit._count.questions,
      attempted: masteryByUnitId.get(unit.id)?.questionsAttempted ?? 0,
      correct: masteryByUnitId.get(unit.id)?.questionsCorrect ?? 0,
    }));
    return {
      id: course.id,
      slug: course.slug,
      name: course.name,
      units,
      totalAttempted: units.reduce((sum, u) => sum + u.attempted, 0),
      totalCorrect: units.reduce((sum, u) => sum + u.correct, 0),
    };
  });

  return { stats, weekEntries, weakest, courses };
}

export type ProgressCore = Awaited<ReturnType<typeof loadProgressCore>>;
export type ProgressCourse = ProgressCore["courses"][number];

// "62% correct across 80 questions." / "No questions attempted yet." The same sentence on both pages.
export function describeCourseAccuracy(totalCorrect: number, totalAttempted: number): string {
  return totalAttempted > 0
    ? `${Math.round((totalCorrect / totalAttempted) * 100)}% correct across ${totalAttempted} question${totalAttempted === 1 ? "" : "s"}.`
    : "No questions attempted yet.";
}
