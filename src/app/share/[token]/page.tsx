import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { loadProgressCore, describeCourseAccuracy } from "@/lib/study/progress-data";
import { findUsableShare, recordShareView } from "@/lib/share/queries";
import { UnitMasteryList } from "@/components/study/unit-mastery-list";
import { WeakTopicsList } from "@/components/study/weak-topics-list";
import { WeekActivity } from "@/components/study/week-activity";
import { XpBar } from "@/components/ui/meter";
import { Page, PageHeader, Section } from "@/components/ui/page";

// The address is the secret: keep it out of search results and out of the Referer header of anything this page links to.
export const metadata: Metadata = { title: "Shared progress", robots: { index: false, follow: false }, referrer: "no-referrer" };
export const dynamic = "force-dynamic";

const formatDate = (d: Date) => d.toLocaleDateString("en-US", { month: "long", day: "numeric", year: "numeric", timeZone: "UTC" });

// What a parent sees through a link the student made (src/lib/share): study activity only, read-only, and no account needed. The owner's
// username is the only identity shown. Anything that is not a live link (malformed, unknown, revoked, expired) is the same 404.
export default async function SharedProgressPage({ params }: { params: Promise<{ token: string }> }) {
  const { token } = await params;
  const share = await findUsableShare(token);
  if (!share) notFound();

  // Best effort: a failed write must not stop a parent seeing the page.
  await recordShareView(share.id).catch(() => undefined);
  const { stats, weekEntries, weakest, courses } = await loadProgressCore(share.userId);

  return (
    <Page>
      <PageHeader
        eyebrow="Shared progress"
        title={`Progress for ${share.username}`}
        description={`A read-only summary that ${share.username} chose to share. It shows study activity only, never a name, email or answers. This link works until ${formatDate(share.expiresAt)}, or sooner if ${share.username} turns it off.`}
      />

      <Section label="Level" note="XP comes from answering questions.">
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

      <Section label="Streak" note="Days in a row with some study.">
        <div className="flex flex-wrap items-baseline gap-x-8 gap-y-2">
          <p className="numeral text-[5rem]">{stats.currentStreak}</p>
          <div>
            <p className="heading text-xl">{stats.currentStreak === 1 ? "day in a row" : "days in a row"}</p>
            <p className="eyebrow mt-2">Longest {stats.longestStreak}</p>
          </div>
        </div>
      </Section>

      <Section label="Last 7 days" note="Days follow the clock of the device you are using.">
        <WeekActivity entries={weekEntries} forParent />
      </Section>

      <Section label="Weakest topics" note="Judged on the latest answer to each question.">
        <WeakTopicsList topics={weakest} links={false} />
      </Section>

      {courses.length === 0 ? (
        <Section label="Courses">
          <p className="reading">No course started yet.</p>
        </Section>
      ) : (
        courses.map((course) => (
          <Section key={course.id} label={course.name} note={describeCourseAccuracy(course.totalCorrect, course.totalAttempted)}>
            <UnitMasteryList courseSlug={course.slug} units={course.units} links={false} />
          </Section>
        ))
      )}
    </Page>
  );
}
