import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { requireUserId } from "@/lib/auth/session";
import { getUnitWithQuestions } from "@/lib/study/queries";
import { renderQuizQuestions } from "@/lib/study/render-quiz";
import { BossBattleRunner } from "@/components/study/boss-battle-runner";
import { Page } from "@/components/ui/page";

export const metadata: Metadata = { title: "Boss battle" };

export default async function BossBattlePage({
  params,
}: {
  params: Promise<{ courseSlug: string; unitSlug: string }>;
}) {
  await requireUserId();
  const { courseSlug, unitSlug } = await params;

  const result = await getUnitWithQuestions(courseSlug, unitSlug);
  if (!result) notFound();
  const { course, unit } = result;
  if (unit.questions.length === 0) notFound();

  const questions = await renderQuizQuestions(
    unit.questions.map((q) => q.id),
    course.slug,
  );

  return (
    <Page>
      <BossBattleRunner
        unitId={unit.id}
        unitName={unit.name}
        courseSlug={course.slug}
        unitSlug={unit.slug}
        questions={questions}
      />
    </Page>
  );
}
