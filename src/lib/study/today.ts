import { getDb } from "@/lib/db";
import { getCramQuestionIds, hasCompletedDailyChallengeToday } from "@/lib/study/queries";
import { getCourseCoverage, type CourseCoverage } from "@/lib/study/coverage";
import { toIsoDate } from "@/lib/study/exam-plan";

export interface TodayCourse {
  id: string;
  slug: string;
  name: string;
  dailyDone: boolean;
  dueCount: number;
  examDateIso: string | null;
  coverage: CourseCoverage;
}

export interface TodayOverview {
  cram: boolean;
  courses: TodayCourse[];
  lastUnit: { courseSlug: string; courseName: string; unitSlug: string; unitName: string } | null;
}

// Everything the Today screen needs beyond the XP/streak stats, assembled from
// the same queries the practice hub already uses (daily-challenge status, the
// due weak-spot queue) so the two can never disagree.
export async function getTodayOverview(userId: string, cram: boolean): Promise<TodayOverview> {
  const db = getDb();
  const now = new Date();

  const [enrollments, lastAttempt] = await Promise.all([
    db.enrollment.findMany({
      where: { userId },
      select: { examDate: true, course: { select: { id: true, slug: true, name: true } } },
    }),
    db.questionAttempt.findFirst({
      where: { userId },
      orderBy: { createdAt: "desc" },
      select: {
        question: {
          select: {
            unit: { select: { slug: true, name: true, course: { select: { slug: true, name: true } } } },
          },
        },
      },
    }),
  ]);

  const courses = await Promise.all(
    enrollments
      .map((e) => ({ ...e.course, examDateIso: e.examDate ? toIsoDate(e.examDate, "utc") : null }))
      .sort((a, b) => a.name.localeCompare(b.name))
      .map(async (course) => ({
        ...course,
        coverage: await getCourseCoverage(userId, course.id),
        dailyDone: await hasCompletedDailyChallengeToday(userId, course.id),
        // In cram mode the review button starts the cram queue, so that is the number to show.
        dueCount: cram
          ? (await getCramQuestionIds(userId, course.id)).length
          : await db.spacedRepetitionState.count({
              where: { userId, dueAt: { lte: now }, question: { courseId: course.id } },
            }),
      })),
  );

  const unit = lastAttempt?.question.unit;
  return {
    cram,
    courses,
    lastUnit: unit
      ? { courseSlug: unit.course.slug, courseName: unit.course.name, unitSlug: unit.slug, unitName: unit.name }
      : null,
  };
}
