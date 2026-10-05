import type { Metadata } from "next";
import Link from "next/link";
import { notFound, redirect } from "next/navigation";
import { requireUserId } from "@/lib/auth/session";
import { getDb } from "@/lib/db";
import { hasCompletedDailyChallengeToday, pickDailyChallengeQuestionIds } from "@/lib/study/queries";
import { Button } from "@/components/ui/button";
import { ActionRow, Breadcrumb, Page, PageHeader, Section } from "@/components/ui/page";

export const metadata: Metadata = { title: "Daily challenge" };

export default async function DailyChallengePage({ params }: { params: Promise<{ courseSlug: string }> }) {
  const { courseSlug } = await params;
  const userId = await requireUserId();

  const course = await getDb().course.findUnique({ where: { slug: courseSlug } });
  if (!course) notFound();

  const header = (
    <PageHeader
      eyebrow={
        <Breadcrumb
          items={[
            { label: course.name, href: `/courses/${course.slug}` },
            { label: "Practice", href: `/courses/${course.slug}/practice` },
            { label: "Daily challenge" },
          ]}
        />
      }
      title="Daily challenge"
    />
  );
  const backButton = (
    <Button render={<Link href={`/courses/${course.slug}/practice`} />} nativeButton={false} variant="outline" size="lg">
      Back to practice
    </Button>
  );

  const done = await hasCompletedDailyChallengeToday(userId, course.id);

  if (done) {
    const startOfToday = new Date();
    startOfToday.setHours(0, 0, 0, 0);
    const todaysAttempts = await getDb().questionAttempt.findMany({
      where: { userId, source: "DAILY", createdAt: { gte: startOfToday }, question: { courseId: course.id } },
    });
    const correctCount = todaysAttempts.filter((a) => a.correct).length;

    return (
      <Page>
        {header}
        <Section label="Today's result">
          <ActionRow action={backButton}>
            <p className="numeral text-6xl">
              {correctCount} / {todaysAttempts.length}
            </p>
            <p className="reading mt-2">correct. Come back tomorrow for a new set.</p>
          </ActionRow>
        </Section>
      </Page>
    );
  }

  const ids = await pickDailyChallengeQuestionIds(userId, course.id);

  if (ids.length === 0) {
    return (
      <Page>
        {header}
        <Section>
          <ActionRow action={backButton}>
            <p className="reading">This course has no questions for a daily set yet.</p>
          </ActionRow>
        </Section>
      </Page>
    );
  }

  const quizParams = new URLSearchParams({
    ids: ids.join(","),
    source: "DAILY",
    back: `/courses/${course.slug}/practice`,
    backLabel: "Back to practice",
  });

  // "Start" goes straight into the questions: a page that only said "5 questions"
  // and asked for a second click added nothing.
  redirect(`/courses/${course.slug}/quiz?${quizParams.toString()}`);
}
