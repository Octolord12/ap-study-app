import { notFound } from "next/navigation";
import { requireUserId } from "@/lib/auth/session";
import { getQuestionsByIds } from "@/lib/study/queries";
import { renderContentToHtml } from "@/lib/content/render";
import { QuizRunner, type RenderedQuestion } from "@/components/study/quiz-runner";

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

  const questions = await getQuestionsByIds(questionIds);
  if (questions.length === 0) notFound();

  // Rendering markdown -> HTML has to happen here (a Server Component): the
  // quiz itself needs client-side interactivity, but rehype-pretty-code's
  // async Shiki highlighter can't run in a Client Component. See the
  // ContentRenderer gotcha in CLAUDE.md.
  const rendered: RenderedQuestion[] = await Promise.all(
    questions.map(async (q) => {
      // conceptLink is "<course-slug>/<unit-slug>/<topic-slug>" (validated at
      // content-authoring time); there's no dedicated topic page, so this
      // points back to the unit page pre-filtered to that topic.
      const [, unitPart, topicPart] = q.conceptLink.split("/");
      return {
        id: q.id,
        difficulty: q.difficulty,
        stemHtml: await renderContentToHtml(q.stem),
        explanationHtml: await renderContentToHtml(q.explanation),
        conceptHref: `/courses/${courseSlug}/units/${unitPart}?topic=${topicPart}`,
        choices: await Promise.all(
          q.choices.map(async (c) => ({
            id: c.id,
            label: c.label,
            text: c.text,
            isCorrect: c.isCorrect,
            explanationHtml: await renderContentToHtml(c.explanation),
          })),
        ),
      };
    }),
  );

  return (
    <div className="mx-auto w-full max-w-2xl px-6 py-10">
      <QuizRunner courseSlug={courseSlug} unitSlug={unitSlug} questions={rendered} />
    </div>
  );
}
