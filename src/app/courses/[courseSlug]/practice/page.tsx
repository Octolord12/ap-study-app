import Link from "next/link";
import { notFound } from "next/navigation";
import { requireUserId } from "@/lib/auth/session";
import { getDb } from "@/lib/db";
import { getDueWeakSpotQuestionIds, hasCompletedDailyChallengeToday } from "@/lib/study/queries";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

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
    <div className="mx-auto w-full max-w-2xl px-6 py-10">
      <p className="mb-1 text-sm text-muted-foreground">
        <Link href={`/courses/${course.slug}`} className="hover:text-foreground">
          {course.name}
        </Link>
      </p>
      <h1 className="mb-6 text-2xl font-bold tracking-tight">Practice</h1>

      <div className="space-y-3">
        <Link href={`/courses/${course.slug}/daily`}>
          <Card className="transition-colors hover:border-foreground/30">
            <CardHeader>
              <CardTitle className="text-base">Daily challenge</CardTitle>
            </CardHeader>
            <CardContent>
              <p className="text-sm text-muted-foreground">
                {dailyDone ? "Done for today -- come back tomorrow" : "A short set to keep your streak going"}
              </p>
            </CardContent>
          </Card>
        </Link>

        <Link href={`/courses/${course.slug}/practice/weak-spot`}>
          <Card className="transition-colors hover:border-foreground/30">
            <CardHeader>
              <CardTitle className="text-base">Weak-spot review</CardTitle>
            </CardHeader>
            <CardContent>
              <p className="text-sm text-muted-foreground">
                {dueIds.length > 0
                  ? `${dueIds.length} question${dueIds.length === 1 ? "" : "s"} due for review`
                  : "Nothing due right now -- keep practicing to build up a review queue"}
              </p>
            </CardContent>
          </Card>
        </Link>

        <Link href={`/courses/${course.slug}/practice/custom`}>
          <Card className="transition-colors hover:border-foreground/30">
            <CardHeader>
              <CardTitle className="text-base">Custom quiz</CardTitle>
            </CardHeader>
            <CardContent>
              <p className="text-sm text-muted-foreground">Pick units, difficulty, and length</p>
            </CardContent>
          </Card>
        </Link>

        <Link href={`/courses/${course.slug}/exam`}>
          <Card className="transition-colors hover:border-foreground/30">
            <CardHeader>
              <CardTitle className="text-base">Exam simulation</CardTitle>
            </CardHeader>
            <CardContent>
              <p className="text-sm text-muted-foreground">Timed, full-length, no explanations until the end</p>
            </CardContent>
          </Card>
        </Link>
      </div>
    </div>
  );
}
