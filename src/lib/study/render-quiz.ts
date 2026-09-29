import { renderContentToHtml } from "@/lib/content/render";
import { getQuestionsByIds } from "@/lib/study/queries";
import type { RenderedQuestion } from "@/components/study/quiz-runner";

// Shared by every quiz entry point (unit practice, custom quiz, weak-spot
// review, daily challenge). Rendering markdown -> HTML has to happen
// server-side even though the quiz itself is a Client Component: see the
// ContentRenderer gotcha in CLAUDE.md (async Shiki highlighter can't run
// client-side).
export async function renderQuizQuestions(questionIds: string[], courseSlug: string): Promise<RenderedQuestion[]> {
  const questions = await getQuestionsByIds(questionIds);

  return Promise.all(
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
}
