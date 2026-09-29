import { notFound, redirect } from "next/navigation";
import { requireUserId } from "@/lib/auth/session";
import { getDb } from "@/lib/db";
import { renderContentToHtml } from "@/lib/content/render";
import { renderQuizQuestions } from "@/lib/study/render-quiz";
import { ExamMcqReview } from "@/components/study/exam-mcq-review";
import { FrqSelfGrade, type RubricLineView } from "@/components/study/frq-self-grade";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { DiagramRenderer } from "@/components/diagrams/diagram-renderer";
import type { Diagram } from "@/lib/content/diagram-schema";

export default async function ExamResultsPage({
  params,
}: {
  params: Promise<{ courseSlug: string; examAttemptId: string }>;
}) {
  const userId = await requireUserId();
  const { courseSlug, examAttemptId } = await params;
  const db = getDb();

  const attempt = await db.examAttempt.findUnique({ where: { id: examAttemptId } });
  if (!attempt || attempt.userId !== userId) notFound();
  if (!attempt.completedAt) redirect(`/courses/${courseSlug}/exam/${attempt.id}`);

  const questionIds = attempt.questionIds as string[];
  const frqPromptIds = attempt.frqPromptIds as string[];
  const sectionScores = attempt.sectionScores as unknown as { mcqCorrect: number; mcqTotal: number };

  const [renderedQuestions, chosenAttempts, frqPrompts, existingFrqAttempts] = await Promise.all([
    renderQuizQuestions(questionIds, courseSlug),
    db.questionAttempt.findMany({
      where: { userId, questionId: { in: questionIds }, source: "EXAM" },
      orderBy: { createdAt: "desc" },
      select: { questionId: true, chosenLabel: true },
    }),
    db.fRQPrompt.findMany({ where: { id: { in: frqPromptIds } } }),
    db.fRQAttempt.findMany({
      where: { userId, frqPromptId: { in: frqPromptIds } },
      orderBy: { createdAt: "desc" },
    }),
  ]);

  // Latest EXAM-sourced attempt per question, within this exam's window --
  // an approximation (QuestionAttempt isn't linked to a specific ExamAttempt),
  // fine as long as a student isn't mid-way through two attempts on the same
  // course's exam at once.
  const chosenLabelByQuestionId = new Map<string, string>();
  for (const a of chosenAttempts) {
    if (!chosenLabelByQuestionId.has(a.questionId)) chosenLabelByQuestionId.set(a.questionId, a.chosenLabel);
  }
  const frqAttemptByPromptId = new Map<string, (typeof existingFrqAttempts)[number]>();
  for (const a of existingFrqAttempts) {
    if (!frqAttemptByPromptId.has(a.frqPromptId)) frqAttemptByPromptId.set(a.frqPromptId, a);
  }

  const frqSections = await Promise.all(
    frqPrompts.map(async (frq) => ({
      frq,
      promptHtml: await renderContentToHtml(frq.prompt),
      sampleResponseHtml: await renderContentToHtml(frq.sampleResponse),
      diagram: (frq.diagram as Diagram | null) ?? null,
      rubric: frq.rubric as unknown as RubricLineView[],
      existingAttempt: frqAttemptByPromptId.get(frq.id),
    })),
  );

  return (
    <div className="mx-auto w-full max-w-2xl px-6 py-10 space-y-8">
      <Card>
        <CardHeader>
          <CardTitle>Exam results</CardTitle>
        </CardHeader>
        <CardContent className="space-y-2">
          <p className="text-sm">
            MCQ: {sectionScores.mcqCorrect} / {sectionScores.mcqTotal} correct
          </p>
          <p className="text-sm">
            Estimated AP score: <span className="font-semibold">{attempt.estimatedScore}</span>{" "}
            <span className="text-xs text-muted-foreground">
              (a rough estimate from MCQ accuracy only -- not a real prediction)
            </span>
          </p>
        </CardContent>
      </Card>

      {frqSections.length > 0 ? (
        <div>
          <h2 className="mb-3 text-sm font-semibold uppercase tracking-wide text-muted-foreground">
            Free response -- grade your own responses
          </h2>
          <div className="space-y-6">
            {frqSections.map(({ frq, promptHtml, sampleResponseHtml, diagram, rubric, existingAttempt }) => (
              <Card key={frq.id}>
                <CardContent className="space-y-4 py-6">
                  <div
                    className="prose prose-sm prose-neutral dark:prose-invert max-w-none"
                    dangerouslySetInnerHTML={{ __html: promptHtml }}
                  />
                  {diagram && <DiagramRenderer diagram={diagram} />}
                  <FrqSelfGrade
                    frqPromptId={frq.id}
                    pointValue={frq.pointValue}
                    rubric={rubric}
                    sampleResponseHtml={sampleResponseHtml}
                    existingResponseText={existingAttempt?.responseText ?? ""}
                    existingAttemptId={existingAttempt?.id}
                  />
                </CardContent>
              </Card>
            ))}
          </div>
        </div>
      ) : null}

      <div>
        <h2 className="mb-3 text-sm font-semibold uppercase tracking-wide text-muted-foreground">
          Multiple choice review
        </h2>
        <ExamMcqReview questions={renderedQuestions} chosenLabelByQuestionId={chosenLabelByQuestionId} />
      </div>
    </div>
  );
}
