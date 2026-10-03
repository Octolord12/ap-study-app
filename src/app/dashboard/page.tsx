import type { Metadata } from "next";
import Link from "next/link";
import { requireUserId } from "@/lib/auth/session";
import { getDb } from "@/lib/db";
import { computeUnitMastery } from "@/lib/study/mastery";
import { getAllBadgeStatuses, getUserGamificationStats } from "@/lib/gamification/queries";
import { Bubbles, XpBar } from "@/components/ui/meter";
import { Page, PageHeader, RuledList, Section } from "@/components/ui/page";
import { BadgeStamp } from "@/components/ui/stamp";
import { Tally } from "@/components/ui/tally";

export const metadata: Metadata = { title: "Progress" };

export default async function DashboardPage() {
  const userId = await requireUserId();
  const db = getDb();

  const [enrollments, attempts, stats, badges] = await Promise.all([
    db.enrollment.findMany({
      where: { userId },
      include: { course: { include: { units: { orderBy: { order: "asc" } } } } },
    }),
    db.questionAttempt.findMany({
      where: { userId },
      select: { questionId: true, correct: true, createdAt: true, question: { select: { unitId: true } } },
    }),
    getUserGamificationStats(userId),
    getAllBadgeStatuses(userId),
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
    <Page>
      <PageHeader eyebrow="Progress" title="Your progress" />

      <Section label="Level">
        <div className="flex max-w-lg items-end gap-5">
          <span className="numeral text-[5rem]">{stats.level}</span>
          <div className="min-w-0 flex-1 pb-2">
            <p className="mb-2 text-sm text-muted-foreground">
              {stats.xpIntoLevel} of {stats.xpForNextLevel} XP to level {stats.level + 1}
            </p>
            <XpBar value={stats.xpIntoLevel} max={stats.xpForNextLevel} label={`${stats.xpIntoLevel} of ${stats.xpForNextLevel} XP to the next level`} />
            <p className="eyebrow mt-2">{stats.totalXp} XP total</p>
          </div>
        </div>
      </Section>

      <Section label="Streak" note="A streak freeze covers one missed day.">
        <div className="flex flex-wrap items-center gap-x-8 gap-y-4">
          <p className="numeral text-[5rem]">{stats.currentStreak}</p>
          <div>
            <p className="heading text-xl">{stats.currentStreak === 1 ? "day in a row" : "days in a row"}</p>
            {stats.currentStreak > 0 ? <Tally count={stats.currentStreak} className="mt-3 h-8 w-auto" /> : null}
            <p className="eyebrow mt-3">
              Longest {stats.longestStreak} · {stats.streakFreezesAvailable} freeze{stats.streakFreezesAvailable === 1 ? "" : "s"} left
            </p>
          </div>
        </div>
      </Section>

      <Section label="Badges">
        <ul className="grid grid-cols-2 gap-x-6 gap-y-8 sm:grid-cols-3">
          {badges.map((badge) => (
            <li key={badge.slug} className="flex items-start gap-3">
              <BadgeStamp slug={badge.slug} earned={badge.earned} className="size-14 shrink-0" />
              <div className="min-w-0">
                <p className="text-sm font-semibold">{badge.name}</p>
                <p className="mt-0.5 text-xs leading-snug text-muted-foreground">{badge.description}</p>
                {!badge.earned ? <p className="eyebrow mt-1">Locked</p> : null}
              </div>
            </li>
          ))}
        </ul>
      </Section>

      {enrollments.length === 0 ? (
        <Section label="Courses">
          <p className="reading">
            You haven&apos;t started a course yet.{" "}
            <Link href="/courses" className="font-semibold underline underline-offset-4 hover:bg-mark hover:text-on-mark hover:no-underline">
              Browse courses
            </Link>
            .
          </p>
        </Section>
      ) : (
        enrollments.map(({ course }) => {
          const totalAttempted = course.units.reduce(
            (sum, u) => sum + (masteryByUnitId.get(u.id)?.questionsAttempted ?? 0),
            0,
          );
          const totalCorrect = course.units.reduce(
            (sum, u) => sum + (masteryByUnitId.get(u.id)?.questionsCorrect ?? 0),
            0,
          );

          return (
            <Section
              key={course.id}
              label={course.name}
              note={
                totalAttempted > 0
                  ? `${Math.round((totalCorrect / totalAttempted) * 100)}% correct across ${totalAttempted} question${totalAttempted === 1 ? "" : "s"}.`
                  : "No questions attempted yet."
              }
            >
              <RuledList>
                {course.units.map((unit) => {
                  const m = masteryByUnitId.get(unit.id);
                  const attempted = m?.questionsAttempted ?? 0;
                  const pct = m && attempted > 0 ? Math.round((m.questionsCorrect / attempted) * 100) : null;

                  return (
                    <li key={unit.id}>
                      <Link
                        href={`/courses/${course.slug}/units/${unit.slug}`}
                        className="group grid gap-x-6 gap-y-2 py-3 sm:grid-cols-[minmax(0,1fr)_auto_6.5rem] sm:items-center"
                      >
                        <span className="text-sm font-medium underline-offset-4 decoration-2 group-hover:underline">{unit.name}</span>
                        <Bubbles percent={pct} />
                        <span className="eyebrow sm:text-right">{pct !== null ? `${pct}% of ${attempted}` : "Not started"}</span>
                      </Link>
                    </li>
                  );
                })}
              </RuledList>
            </Section>
          );
        })
      )}
    </Page>
  );
}
