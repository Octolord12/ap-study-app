import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { requireUserId } from "@/lib/auth/session";
import { getDb } from "@/lib/db";
import { getDueWeakSpotQuestionIds } from "@/lib/study/queries";
import { Button } from "@/components/ui/button";
import { ActionRow, Breadcrumb, Page, PageHeader, Section } from "@/components/ui/page";

export const metadata: Metadata = { title: "Weak-spot review" };

export default async function WeakSpotReviewPage({ params }: { params: Promise<{ courseSlug: string }> }) {
  const { courseSlug } = await params;
  const userId = await requireUserId();

  const course = await getDb().course.findUnique({ where: { slug: courseSlug } });
  if (!course) notFound();

  const dueIds = await getDueWeakSpotQuestionIds(userId, course.id);

  const quizParams = new URLSearchParams({
    ids: dueIds.join(","),
    source: "WEAK_SPOT",
    back: `/courses/${course.slug}/practice`,
    backLabel: "Back to practice",
  });

  return (
    <Page>
      <PageHeader
        eyebrow={
          <Breadcrumb
            items={[
              { label: course.name, href: `/courses/${course.slug}` },
              { label: "Practice", href: `/courses/${course.slug}/practice` },
              { label: "Weak spots" },
            ]}
          />
        }
        title="Weak-spot review"
        description="Questions you missed come back on a schedule, so you see them again right when they start to fade."
      />
      <Section>
        {dueIds.length === 0 ? (
          <ActionRow
            action={
              <Button render={<Link href={`/courses/${course.slug}/practice`} />} nativeButton={false} variant="outline" size="lg">
                Back to practice
              </Button>
            }
          >
            <p className="reading">Nothing is due right now. Keep practicing, and missed questions will appear here when it&apos;s time to revisit them.</p>
          </ActionRow>
        ) : (
          <ActionRow
            action={
              <Button render={<Link href={`/courses/${course.slug}/quiz?${quizParams.toString()}`} />} nativeButton={false} size="lg">
                Start review
              </Button>
            }
          >
            <p className="numeral text-5xl">{dueIds.length}</p>
            <p className="reading mt-2">question{dueIds.length === 1 ? "" : "s"} due, picked from ones you&apos;ve missed before.</p>
          </ActionRow>
        )}
      </Section>
    </Page>
  );
}
