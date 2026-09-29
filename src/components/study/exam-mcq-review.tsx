import Link from "next/link";
import type { RenderedQuestion } from "@/components/study/quiz-runner";

// Static, always-revealed version of the quiz runner's per-question review --
// the exam is already over, so there's no interactivity left, just the
// explanations the student couldn't see mid-exam.
export function ExamMcqReview({
  questions,
  chosenLabelByQuestionId,
}: {
  questions: RenderedQuestion[];
  chosenLabelByQuestionId: Map<string, string>;
}) {
  return (
    <div className="space-y-4">
      {questions.map((question, index) => {
        const chosenLabel = chosenLabelByQuestionId.get(question.id);
        return (
          <div key={question.id} className="rounded-lg border border-border p-4">
            <p className="mb-2 text-xs text-muted-foreground">Question {index + 1}</p>
            <div
              className="prose prose-sm prose-neutral dark:prose-invert mb-3 max-w-none"
              dangerouslySetInnerHTML={{ __html: question.stemHtml }}
            />
            <div className="space-y-2">
              {question.choices.map((choice) => {
                const wasChosen = chosenLabel === choice.label;
                return (
                  <div
                    key={choice.id}
                    className={[
                      "rounded-lg border px-3 py-2 text-sm",
                      choice.isCorrect ? "border-green-600 bg-green-50 dark:bg-green-950" : "",
                      wasChosen && !choice.isCorrect ? "border-destructive bg-red-50 dark:bg-red-950" : "",
                      !choice.isCorrect && !wasChosen ? "border-border" : "",
                    ].join(" ")}
                  >
                    <span className="font-medium">{choice.label}.</span> {choice.text}
                    {wasChosen ? <span className="ml-2 text-xs text-muted-foreground">(your answer)</span> : null}
                  </div>
                );
              })}
              {!chosenLabel ? <p className="text-xs text-muted-foreground">You didn&apos;t answer this one.</p> : null}
            </div>
            <div
              className="prose prose-sm prose-neutral dark:prose-invert mt-3 max-w-none"
              dangerouslySetInnerHTML={{ __html: question.explanationHtml }}
            />
            <Link href={question.conceptHref} className="mt-1 inline-block text-xs font-medium underline underline-offset-4">
              Review this concept
            </Link>
          </div>
        );
      })}
    </div>
  );
}
