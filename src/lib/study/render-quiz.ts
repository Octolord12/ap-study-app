import { renderChoiceTextToHtml, renderContentToHtml } from "@/lib/content/render";
import { getQuestionsByIds, getTopicKeysWithRefreshers } from "@/lib/study/queries";
import { topicHref, topicKey } from "@/lib/study/concept-link";
import { displayLabelMap, remapChoiceLetters, shuffleChoices } from "@/lib/study/shuffle-choices";
import type { RenderedQuestion } from "@/components/study/quiz-runner";
import type { Diagram } from "@/lib/content/diagram-schema";

// Shared by every quiz entry point (unit practice, custom quiz, weak-spot
// review, daily challenge). Rendering markdown -> HTML has to happen
// server-side even though the quiz itself is a Client Component: see the
// react-markdown gotcha in CLAUDE.md (async Shiki highlighter can't run
// client-side).
//
// Choices are shuffled here, on every call, so each showing of a question has
// its own order. `label` stays the authored label (what is sent back, stored
// and graded); `displayLabel` is the letter shown. See shuffle-choices.ts.
export async function renderQuizQuestions(questionIds: string[], courseSlug: string): Promise<RenderedQuestion[]> {
  const [questions, topicsWithRefreshers] = await Promise.all([getQuestionsByIds(questionIds), getTopicKeysWithRefreshers(courseSlug)]);

  return Promise.all(
    questions.map(async (q) => {
      // conceptLink is "<course-slug>/<unit-slug>/<topic-slug>" (validated at
      // content-authoring time). It opens the topic's refresher page when one is written, and the unit page
      // filtered to that topic otherwise.
      const [, unitPart, topicPart] = q.conceptLink.split("/");
      const choices = shuffleChoices(q.choices);
      const letters = displayLabelMap(choices);
      const withShownLetters = (text: string) => remapChoiceLetters(text, letters);
      return {
        id: q.id,
        difficulty: q.difficulty,
        stemHtml: await renderContentToHtml(withShownLetters(q.stem), courseSlug),
        explanationHtml: await renderContentToHtml(withShownLetters(q.explanation), courseSlug),
        diagram: (q.diagram as Diagram | null) ?? null,
        conceptHref: topicHref(courseSlug, unitPart, topicPart, topicsWithRefreshers.has(topicKey(unitPart, topicPart))),
        choices: await Promise.all(
          choices.map(async (c) => ({
            id: c.id,
            label: c.label,
            displayLabel: c.displayLabel,
            textHtml: await renderChoiceTextToHtml(withShownLetters(c.text), courseSlug),
            isCorrect: c.isCorrect,
            explanationHtml: await renderContentToHtml(withShownLetters(c.explanation), courseSlug),
          })),
        ),
      };
    }),
  );
}
