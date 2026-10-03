import Link from "next/link";
import { getUserGamificationStats } from "@/lib/gamification/queries";
import { getTodayOverview } from "@/lib/study/today";
import { listCourses } from "@/lib/study/queries";
import { Button } from "@/components/ui/button";
import { XpBar } from "@/components/ui/meter";
import { Page, PageHeader, RuledList, Section } from "@/components/ui/page";
import { Tally } from "@/components/ui/tally";

function headline(streak: number, studiedToday: boolean) {
  if (studiedToday) return streak > 1 ? `You've studied today. That's ${streak} days in a row.` : "You've studied today. The streak has started.";
  if (streak > 0) return `Study today to keep your ${streak}-day streak.`;
  return "Answer one question to start a streak.";
}

// The signed-in home page: what is worth doing right now, in order. Reads the
// same daily-challenge and due-review queries the practice hub uses.
export async function TodayScreen({ userId }: { userId: string }) {
  const [stats, overview] = await Promise.all([getUserGamificationStats(userId), getTodayOverview(userId)]);
  const { courses, lastUnit } = overview;

  if (courses.length === 0) {
    const catalog = await listCourses();
    return (
      <Page>
        <PageHeader eyebrow="Today" title="Pick your first course." description="Choose the exam you're studying for. You can add the others later." />
        <Section label="Courses">
          <RuledList>
            {catalog.map((course) => (
              <li key={course.id} className="flex items-center justify-between gap-4 py-4">
                <span className="heading text-xl">{course.name}</span>
                <Button render={<Link href={`/courses/${course.slug}`} />} nativeButton={false} variant="outline" size="sm">
                  Open
                </Button>
              </li>
            ))}
          </RuledList>
        </Section>
      </Page>
    );
  }

  const totalDue = courses.reduce((sum, c) => sum + c.dueCount, 0);

  return (
    <Page>
      <PageHeader
        eyebrow="Today"
        title={headline(stats.currentStreak, stats.studiedToday)}
        description={stats.currentStreak > 0 ? <Tally count={stats.currentStreak} className="mt-1 h-8 w-auto" /> : undefined}
      />

      <Section label="Daily challenge" note="Five questions. Reviews that are due come first.">
        <RuledList>
          {courses.map((course) => (
            <li key={course.id} className="flex flex-wrap items-center justify-between gap-x-6 gap-y-2 py-4">
              <div>
                <p className="heading text-xl">{course.name}</p>
                <p className="mt-0.5 text-sm text-muted-foreground">
                  {course.dailyDone ? "Done for today. A new set opens tomorrow." : "Five questions, about five minutes."}
                </p>
              </div>
              <Button
                render={<Link href={`/courses/${course.slug}/daily`} />}
                nativeButton={false}
                variant={course.dailyDone ? "outline" : "default"}
              >
                {course.dailyDone ? "Do another set" : "Start"}
              </Button>
            </li>
          ))}
        </RuledList>
      </Section>

      <Section label="Due for review" note="Questions you missed return on a schedule.">
        {totalDue === 0 ? (
          <p className="reading max-w-[52ch]">
            Nothing is due. When you miss a question it lands here a day or so later, so the reviews fit around the new work.
          </p>
        ) : (
          <RuledList>
            {courses
              .filter((c) => c.dueCount > 0)
              .map((course) => (
                <li key={course.id} className="flex flex-wrap items-center justify-between gap-x-6 gap-y-2 py-4">
                  <div>
                    <p className="heading text-xl">{course.name}</p>
                    <p className="mt-0.5 text-sm text-muted-foreground">
                      {course.dueCount} question{course.dueCount === 1 ? "" : "s"} due
                    </p>
                  </div>
                  <Button render={<Link href={`/courses/${course.slug}/practice/weak-spot`} />} nativeButton={false} variant="outline">
                    Review
                  </Button>
                </li>
              ))}
          </RuledList>
        )}
      </Section>

      {lastUnit ? (
        <Section label="Pick up where you left off">
          <div className="flex flex-wrap items-center justify-between gap-x-6 gap-y-3">
            <div>
              <p className="heading text-xl">{lastUnit.unitName}</p>
              <p className="mt-0.5 text-sm text-muted-foreground">{lastUnit.courseName}</p>
            </div>
            <Button render={<Link href={`/courses/${lastUnit.courseSlug}/units/${lastUnit.unitSlug}`} />} nativeButton={false} variant="outline">
              Open unit
            </Button>
          </div>
        </Section>
      ) : null}

      <Section label="Level">
        <div className="flex max-w-md items-end gap-4">
          <span className="numeral text-6xl">{stats.level}</span>
          <div className="min-w-0 flex-1 pb-1.5">
            <p className="mb-2 text-sm text-muted-foreground">
              {stats.xpIntoLevel} of {stats.xpForNextLevel} XP to level {stats.level + 1}
            </p>
            <XpBar value={stats.xpIntoLevel} max={stats.xpForNextLevel} label={`${stats.xpIntoLevel} of ${stats.xpForNextLevel} XP`} />
          </div>
        </div>
      </Section>
    </Page>
  );
}
