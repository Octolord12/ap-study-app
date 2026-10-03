import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { requireUserId } from "@/lib/auth/session";
import { getDb } from "@/lib/db";
import { getDueWeakSpotQuestionIds, hasCompletedDailyChallengeToday } from "@/lib/study/queries";
import { Button } from "@/components/ui/button";
import { ActionRow, Breadcrumb, Page, PageHeader, Section } from "@/components/ui/page";

export const metadata: Metadata = { title: "Practice" };

export default async function PracticeHubPage({ params }: { params: Promise<{ courseSlug: string }> }) {
  const { courseSlug } = await params;
  const userId = await requireUserId();

  const course = await getDb().course.findUnique({ where: { slug: courseSlug } });
  if (!course) notFound();

  const [dueIds, dailyDone] = await Promise.all([
    getDueWeakSpotQuestionIds(userId, course.id),
    hasCompletedDailyChallengeToday(userId, course.id),
  ]);

  return (
    <Page>
      <PageHeader
        eyebrow={<Breadcrumb items={[{ label: course.name, href: `/courses/${course.slug}` }, { label: "Practice" }]} />}
        title="Practice"
        description="Short on time, do the daily challenge. Otherwise pick how you want to work."
      />

      <Section label="Daily challenge" note="Keeps the streak going.">
        <ActionRow
          action={
            <Button render={<Link href={`/courses/${course.slug}/daily`} />} nativeButton={false} size="lg" variant={dailyDone ? "outline" : "default"}>
              {dailyDone ? "See today's result" : "Start"}
            </Button>
          }
        >
          <p className="reading">
            {dailyDone
              ? "Done for today. A new set opens tomorrow."
              : "Five questions. Any reviews that are due come first, then new ones fill the rest."}
          </p>
        </ActionRow>
      </Section>

      <Section label="Weak spots" note="Spaced repetition.">
        <ActionRow
          action={
            <Button render={<Link href={`/courses/${course.slug}/practice/weak-spot`} />} nativeButton={false} size="lg" variant="outline">
              {dueIds.length > 0 ? "Review" : "Details"}
            </Button>
          }
        >
          <p className="reading">
            {dueIds.length > 0
              ? `${dueIds.length} question${dueIds.length === 1 ? " is" : "s are"} due for review.`
              : "Nothing is due. Answered questions come back on a schedule, sooner when you miss one."}
          </p>
        </ActionRow>
      </Section>

      <Section label="Custom quiz">
        <ActionRow
          action={
            <Button render={<Link href={`/courses/${course.slug}/practice/custom`} />} nativeButton={false} size="lg" variant="outline">
              Build a quiz
            </Button>
          }
        >
          <p className="reading">Choose the units, the difficulty and how many questions.</p>
        </ActionRow>
      </Section>

      <Section label="Exam simulation">
        <ActionRow
          action={
            <Button render={<Link href={`/courses/${course.slug}/exam`} />} nativeButton={false} size="lg" variant="outline">
              Set up an exam
            </Button>
          }
        >
          <p className="reading">Timed and full length. No explanations until you submit.</p>
        </ActionRow>
      </Section>
    </Page>
  );
}
