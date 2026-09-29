import Link from "next/link";
import { notFound } from "next/navigation";
import { requireUserId } from "@/lib/auth/session";
import { getDb } from "@/lib/db";
import { hasCompletedDailyChallengeToday, pickDailyChallengeQuestionIds } from "@/lib/study/queries";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

export default async function DailyChallengePage({ params }: { params: Promise<{ courseSlug: string }> }) {
  const { courseSlug } = await params;
  const userId = await requireUserId();

  const course = await getDb().course.findUnique({ where: { slug: courseSlug } });
  if (!course) notFound();

  const done = await hasCompletedDailyChallengeToday(userId, course.id);

  if (done) {
    const startOfToday = new Date();
    startOfToday.setHours(0, 0, 0, 0);
    const todaysAttempts = await getDb().questionAttempt.findMany({
      where: { userId, source: "DAILY", createdAt: { gte: startOfToday }, question: { courseId: course.id } },
    });
    const correctCount = todaysAttempts.filter((a) => a.correct).length;

    return (
      <div className="mx-auto w-full max-w-2xl px-6 py-10">
        <Card>
          <CardHeader>
            <CardTitle>Daily challenge</CardTitle>
          </CardHeader>
          <CardContent className="space-y-4">
            <p className="text-sm text-muted-foreground">
              Done for today: {correctCount} / {todaysAttempts.length} correct. Come back tomorrow for a new set.
            </p>
            <Button render={<Link href={`/courses/${course.slug}/practice`} />} nativeButton={false} variant="outline">
              Back to practice
            </Button>
          </CardContent>
        </Card>
      </div>
    );
  }

  const ids = await pickDailyChallengeQuestionIds(userId, course.id);

  if (ids.length === 0) {
    return (
      <div className="mx-auto w-full max-w-2xl px-6 py-10">
        <Card>
          <CardHeader>
            <CardTitle>Daily challenge</CardTitle>
          </CardHeader>
          <CardContent>
            <p className="text-sm text-muted-foreground">
              No questions available yet for this course&apos;s daily challenge.
            </p>
          </CardContent>
        </Card>
      </div>
    );
  }

  const quizParams = new URLSearchParams({
    ids: ids.join(","),
    source: "DAILY",
    back: `/courses/${course.slug}/practice`,
    backLabel: "Back to practice",
  });

  return (
    <div className="mx-auto w-full max-w-2xl px-6 py-10">
      <Card>
        <CardHeader>
          <CardTitle>Daily challenge</CardTitle>
        </CardHeader>
        <CardContent className="space-y-4">
          <p className="text-sm text-muted-foreground">
            Today&apos;s set: {ids.length} questions, prioritizing what you&apos;re due to review.
          </p>
          <Button render={<Link href={`/courses/${course.slug}/quiz?${quizParams.toString()}`} />} nativeButton={false}>
            Start today&apos;s challenge
          </Button>
        </CardContent>
      </Card>
    </div>
  );
}
