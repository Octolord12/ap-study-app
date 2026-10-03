import { getDb } from "@/lib/db";
import { hasCompletedDailyChallengeToday } from "@/lib/study/queries";

export interface TodayCourse {
  id: string;
  slug: string;
  name: string;
  dailyDone: boolean;
  dueCount: number;
}

export interface TodayOverview {
  courses: TodayCourse[];
  lastUnit: { courseSlug: string; courseName: string; unitSlug: string; unitName: string } | null;
}

// Everything the Today screen needs beyond the XP/streak stats, assembled from
// the same queries the practice hub already uses (daily-challenge status, the
// due weak-spot queue) so the two can never disagree.
export async function getTodayOverview(userId: string): Promise<TodayOverview> {
  const db = getDb();
  const now = new Date();

  const [enrollments, lastAttempt] = await Promise.all([
    db.enrollment.findMany({
      where: { userId },
      select: { course: { select: { id: true, slug: true, name: true } } },
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
      .map((e) => e.course)
      .sort((a, b) => a.name.localeCompare(b.name))
      .map(async (course) => ({
        ...course,
        dailyDone: await hasCompletedDailyChallengeToday(userId, course.id),
        dueCount: await db.spacedRepetitionState.count({
          where: { userId, dueAt: { lte: now }, question: { courseId: course.id } },
        }),
      })),
  );

  const unit = lastAttempt?.question.unit;
  return {
    courses,
    lastUnit: unit
      ? { courseSlug: unit.course.slug, courseName: unit.course.name, unitSlug: unit.slug, unitName: unit.name }
      : null,
  };
}
