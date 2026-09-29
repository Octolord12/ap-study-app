import { notFound } from "next/navigation";
import { requireUserId } from "@/lib/auth/session";
import { renderQuizQuestions } from "@/lib/study/render-quiz";
import { QuizRunner } from "@/components/study/quiz-runner";

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
    <div className="mx-auto w-full max-w-2xl px-6 py-10">
      <QuizRunner
        questions={rendered}
        backHref={`/courses/${courseSlug}/units/${unitSlug}`}
        backLabel="Back to unit"
      />
    </div>
  );
}
