import { getDb } from "@/lib/db";
import { daysAgo } from "@/lib/study/week-activity";

export interface CourseCoverage {
  total: number; // questions in the course
  tried: number; // of those, tried at least once
  newPerDayLast7: number; // questions tried for the first time in the last week, per day
}

// What the study plan needs to know about a student's progress through a course.
export async function getCourseCoverage(userId: string, courseId: string): Promise<CourseCoverage> {
  const db = getDb();
  const [total, firstAttempts] = await Promise.all([
    db.question.count({ where: { courseId } }),
    db.questionAttempt.groupBy({ by: ["questionId"], where: { userId, question: { courseId } }, _min: { createdAt: true } }),
  ]);
  const since = daysAgo(7);
  const newThisWeek = firstAttempts.filter((row) => row._min.createdAt !== null && row._min.createdAt >= since).length;
  return { total, tried: firstAttempts.length, newPerDayLast7: newThisWeek / 7 };
}
