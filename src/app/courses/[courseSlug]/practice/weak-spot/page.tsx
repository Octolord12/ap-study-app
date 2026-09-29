import Link from "next/link";
import { notFound } from "next/navigation";
import { requireUserId } from "@/lib/auth/session";
import { getDb } from "@/lib/db";
import { getDueWeakSpotQuestionIds } from "@/lib/study/queries";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

export default async function WeakSpotReviewPage({ params }: { params: Promise<{ courseSlug: string }> }) {
  const { courseSlug } = await params;
  const userId = await requireUserId();

  const course = await getDb().course.findUnique({ where: { slug: courseSlug } });
  if (!course) notFound();

  const dueIds = await getDueWeakSpotQuestionIds(userId, course.id);

  const params2 = new URLSearchParams({
    ids: dueIds.join(","),
    source: "WEAK_SPOT",
    back: `/courses/${course.slug}/practice`,
    backLabel: "Back to practice",
  });

  return (
    <div className="mx-auto w-full max-w-2xl px-6 py-10">
      <Card>
        <CardHeader>
          <CardTitle>Weak-spot review</CardTitle>
        </CardHeader>
        <CardContent className="space-y-4">
          {dueIds.length === 0 ? (
            <p className="text-sm text-muted-foreground">
              Nothing&apos;s due for review right now. Questions show up here after you miss them, based on a
              spaced-repetition schedule -- keep practicing and they&apos;ll surface when it&apos;s time to revisit them.
            </p>
          ) : (
            <>
              <p className="text-sm text-muted-foreground">
                {dueIds.length} question{dueIds.length === 1 ? "" : "s"} due for review, picked from questions you&apos;ve
                missed before.
              </p>
              <Button render={<Link href={`/courses/${course.slug}/quiz?${params2.toString()}`} />} nativeButton={false}>
                Start review
              </Button>
            </>
          )}
        </CardContent>
      </Card>
    </div>
  );
}
