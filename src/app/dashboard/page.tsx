import Link from "next/link";
import { requireUserId } from "@/lib/auth/session";
import { getDb } from "@/lib/db";
import { computeUnitMastery } from "@/lib/study/mastery";

export default async function DashboardPage() {
  const userId = await requireUserId();
  const db = getDb();

  const [enrollments, attempts] = await Promise.all([
    db.enrollment.findMany({
      where: { userId },
      include: { course: { include: { units: { orderBy: { order: "asc" } } } } },
    }),
    db.questionAttempt.findMany({
      where: { userId },
      select: { questionId: true, correct: true, createdAt: true, question: { select: { unitId: true } } },
    }),
  ]);

  const mastery = computeUnitMastery(
    attempts.map((a) => ({
      questionId: a.questionId,
      unitId: a.question.unitId,
      correct: a.correct,
      createdAt: a.createdAt,
    })),
  );
  const masteryByUnitId = new Map(mastery.map((m) => [m.unitId, m]));

  return (
    <div className="mx-auto w-full max-w-3xl px-6 py-10">
      <h1 className="mb-6 text-2xl font-bold tracking-tight">Dashboard</h1>

      {enrollments.length === 0 ? (
        <p className="text-muted-foreground">
          You haven&apos;t started any courses yet.{" "}
          <Link href="/courses" className="underline underline-offset-4">
            Browse courses
          </Link>
          .
        </p>
      ) : (
        <div className="space-y-8">
          {enrollments.map(({ course }) => {
            const totalAttempted = course.units.reduce(
              (sum, u) => sum + (masteryByUnitId.get(u.id)?.questionsAttempted ?? 0),
              0,
            );
            const totalCorrect = course.units.reduce(
              (sum, u) => sum + (masteryByUnitId.get(u.id)?.questionsCorrect ?? 0),
              0,
            );

            return (
              <section key={course.id}>
                <h2 className="mb-1 text-lg font-semibold">
                  <Link href={`/courses/${course.slug}`} className="hover:underline">
                    {course.name}
                  </Link>
                </h2>
                <p className="mb-3 text-sm text-muted-foreground">
                  {totalAttempted > 0
                    ? `${Math.round((totalCorrect / totalAttempted) * 100)}% accuracy across ${totalAttempted} question${totalAttempted === 1 ? "" : "s"} attempted`
                    : "No questions attempted yet"}
                </p>
                <div className="space-y-2">
                  {course.units.map((unit) => {
                    const m = masteryByUnitId.get(unit.id);
                    const attempted = m?.questionsAttempted ?? 0;
                    const pct = m && attempted > 0 ? Math.round((m.questionsCorrect / attempted) * 100) : null;

                    return (
                      <div key={unit.id} className="flex items-center gap-3 text-sm">
                        <span className="w-48 shrink-0 truncate">{unit.name}</span>
                        <div className="h-2 flex-1 overflow-hidden rounded-full bg-muted">
                          {pct !== null ? <div className="h-full bg-primary" style={{ width: `${pct}%` }} /> : null}
                        </div>
                        <span className="w-28 shrink-0 text-right text-muted-foreground">
                          {pct !== null ? `${pct}% (${attempted})` : "Not started"}
                        </span>
                      </div>
                    );
                  })}
                </div>
              </section>
            );
          })}
        </div>
      )}
    </div>
  );
}
