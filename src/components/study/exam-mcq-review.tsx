import Link from "next/link";
import type { RenderedQuestion } from "@/components/study/quiz-runner";
import { DiagramRenderer } from "@/components/diagrams/diagram-renderer";
import { ChoiceList, ChoiceRow } from "@/components/ui/choice";
import { Html } from "@/components/ui/html";
import { Sheet } from "@/components/ui/sheet";

// Static, always-revealed version of the quiz runner's per-question review --
// the exam is already over, so there's no interactivity left, just the
// explanations the student couldn't see mid-exam.
export function ExamMcqReview({
  questions,
  chosenLabelByQuestionId,
  paperLined = false,
}: {
  questions: RenderedQuestion[];
  chosenLabelByQuestionId: Map<string, string>;
  paperLined?: boolean;
}) {
  return (
    <div className="space-y-6">
      {questions.map((question, index) => {
        const chosenLabel = chosenLabelByQuestionId.get(question.id);
        return (
          <Sheet key={question.id} lined={paperLined}>
            <p className="eyebrow">Question {index + 1}</p>
            <Html html={question.stemHtml} className="mt-2" />
            {question.diagram && <DiagramRenderer diagram={question.diagram} />}
            <div className="mt-4">
              <ChoiceList legend={`Question ${index + 1} answer choices`}>
                {question.choices.map((choice) => {
                  const wasChosen = chosenLabel === choice.label;
                  return (
                    <ChoiceRow
                      key={choice.id}
                      label={choice.label}
                      textHtml={choice.textHtml}
                      explanationHtml={choice.explanationHtml}
                      state={choice.isCorrect ? "correct" : wasChosen ? "wrong" : "idle"}
                      verdict={choice.isCorrect ? (wasChosen ? "Correct, your answer" : "Correct answer") : wasChosen ? "Your answer" : undefined}
                    />
                  );
                })}
              </ChoiceList>
            </div>
            {!chosenLabel ? <p className="mt-3 text-sm font-medium">You didn&apos;t answer this one.</p> : null}
            <div className="mt-5 border-t-2 border-current pt-4">
              <p className="eyebrow !text-current">Explanation</p>
              <Html html={question.explanationHtml} size="sm" className="mt-1.5" />
              <Link
                href={question.conceptHref}
                className="mt-3 inline-block text-sm font-semibold underline underline-offset-4 hover:bg-mark hover:text-on-mark hover:no-underline"
              >
                Review this concept
              </Link>
            </div>
          </Sheet>
        );
      })}
    </div>
  );
}
