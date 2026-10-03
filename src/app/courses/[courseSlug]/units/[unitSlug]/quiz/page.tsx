import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { requireUserId } from "@/lib/auth/session";
import { renderQuizQuestions } from "@/lib/study/render-quiz";
import { QuizRunner } from "@/components/study/quiz-runner";
import { Page } from "@/components/ui/page";
import { isPaperLinedCourse } from "@/lib/content/paper-lined";

export const metadata: Metadata = { title: "Unit quiz" };

export default async function UnitQuizPage({
  params,
  searchParams,
}: {
  params: Promise<{ courseSlug: string; unitSlug: string }>;
  searchParams: Promise<{ ids?: string }>;
}) {
  await requireUserId();
  const { courseSlug, unitSlug } = await params;
  const { ids } = await searchParams;

  const questionIds = (ids ?? "").split(",").filter(Boolean);
  if (questionIds.length === 0) notFound();

  const rendered = await renderQuizQuestions(questionIds, courseSlug);
  if (rendered.length === 0) notFound();

  return (
    <Page>
      <QuizRunner
        questions={rendered}
        backHref={`/courses/${courseSlug}/units/${unitSlug}`}
        backLabel="Back to unit"
        paperLined={isPaperLinedCourse(courseSlug)}
      />
    </Page>
  );
}
