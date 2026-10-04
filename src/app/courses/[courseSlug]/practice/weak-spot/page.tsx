import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { requireUserId } from "@/lib/auth/session";
import { getDb } from "@/lib/db";
import { getReviewQueueIds } from "@/lib/study/queries";
import { isCramModeOn } from "@/lib/study/cram-mode";
import { CramNotice } from "@/components/study/cram-toggle";
import { Button } from "@/components/ui/button";
import { ActionRow, Breadcrumb, Page, PageHeader, Section } from "@/components/ui/page";

export const metadata: Metadata = { title: "Weak-spot review" };

export default async function WeakSpotReviewPage({ params }: { params: Promise<{ courseSlug: string }> }) {
  const { courseSlug } = await params;
  const userId = await requireUserId();

  const course = await getDb().course.findUnique({ where: { slug: courseSlug } });
  if (!course) notFound();

  const cram = await isCramModeOn(userId);
  const dueIds = await getReviewQueueIds(userId, course.id, cram);

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
              { label: cram ? "Cram" : "Weak spots" },
            ]}
          />
        }
        title={cram ? "Cram review" : "Weak-spot review"}
        description={
          cram
            ? "Your most-missed questions first, then ones you haven't seen. Due dates are ignored."
            : "Questions come back on a schedule, sooner when you miss them, so you see them again as they start to fade."
        }
      />
      {cram ? <CramNotice className="mt-6" /> : null}
      <Section>
        {dueIds.length === 0 ? (
          <ActionRow
            action={
              <Button render={<Link href={`/courses/${course.slug}/practice`} />} nativeButton={false} variant="outline" size="lg">
                Back to practice
              </Button>
            }
          >
            <p className="reading">Nothing is due right now. Keep practicing, and questions will appear here when it&apos;s time to revisit them.</p>
          </ActionRow>
        ) : (
          <ActionRow
            action={
              <Button render={<Link href={`/courses/${course.slug}/quiz?${quizParams.toString()}`} />} nativeButton={false} size="lg">
                {cram ? "Start cram" : "Start review"}
              </Button>
            }
          >
            <p className="numeral text-5xl">{dueIds.length}</p>
            <p className="reading mt-2">
              question{dueIds.length === 1 ? "" : "s"} {cram ? "to cram." : "due for review."}
            </p>
          </ActionRow>
        )}
      </Section>
    </Page>
  );
}
