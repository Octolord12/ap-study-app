import type { Metadata } from "next";
import { notFound, redirect } from "next/navigation";
import { requireUserId } from "@/lib/auth/session";
import { getDb } from "@/lib/db";
import { renderChoiceTextToHtml, renderContentToHtml } from "@/lib/content/render";
import { displayLabelMap, remapChoiceLetters, shuffleChoices } from "@/lib/study/shuffle-choices";
import { examSecondsLeft } from "@/lib/study/exam-clock";
import { ExamRunner, type ExamFrqItem, type ExamMcqItem } from "@/components/study/exam-runner";
import type { Course as ContentCourse } from "@/lib/content/schema";
import type { Diagram } from "@/lib/content/diagram-schema";
import { Page } from "@/components/ui/page";

export const metadata: Metadata = { title: "Exam in progress" };

export default async function ExamRunnerPage({
  params,
}: {
  params: Promise<{ courseSlug: string; examAttemptId: string }>;
}) {
  const userId = await requireUserId();
  const { courseSlug, examAttemptId } = await params;
  const db = getDb();

  const attempt = await db.examAttempt.findUnique({ where: { id: examAttemptId } });
  if (!attempt || attempt.userId !== userId) notFound();
  if (attempt.completedAt) redirect(`/courses/${courseSlug}/exam/${attempt.id}/results`);

  const course = await db.course.findUnique({ where: { slug: courseSlug } });
  if (!course) notFound();
  const examFormat = course.examFormat as unknown as ContentCourse["examFormat"];

  const questionIds = attempt.questionIds as string[];
  const frqPromptIds = attempt.frqPromptIds as string[];

  const [questions, frqs] = await Promise.all([
    db.question.findMany({ where: { id: { in: questionIds } }, include: { choices: { orderBy: { label: "asc" } } } }),
    db.fRQPrompt.findMany({ where: { id: { in: frqPromptIds } } }),
  ]);
  const questionById = new Map(questions.map((q) => [q.id, q]));
  const frqById = new Map(frqs.map((f) => [f.id, f]));

  const mcqItems: ExamMcqItem[] = await Promise.all(
    questionIds
      .map((id) => questionById.get(id))
      .filter((q): q is NonNullable<typeof q> => q !== undefined)
      .map(async (q) => {
        // The exam's questions are fixed at start, but their choices are
        // shuffled each time the page is shown, like everywhere else.
        const choices = shuffleChoices(q.choices);
        const letters = displayLabelMap(choices);
        return {
          id: q.id,
          stemHtml: await renderContentToHtml(remapChoiceLetters(q.stem, letters), courseSlug),
          diagram: (q.diagram as Diagram | null) ?? null,
          choices: await Promise.all(
            choices.map(async (c) => ({
              id: c.id,
              label: c.label,
              displayLabel: c.displayLabel,
              textHtml: await renderChoiceTextToHtml(remapChoiceLetters(c.text, letters), courseSlug),
            })),
          ),
        };
      }),
  );

  const frqItems: ExamFrqItem[] = await Promise.all(
    frqPromptIds
      .map((id) => frqById.get(id))
      .filter((f): f is NonNullable<typeof f> => f !== undefined)
      .map(async (f) => ({
        id: f.id,
        type: f.type,
        promptHtml: await renderContentToHtml(f.prompt, courseSlug),
        diagram: (f.diagram as Diagram | null) ?? null,
        pointValue: f.pointValue,
      })),
  );

  return (
    <Page>
      <ExamRunner
        examAttemptId={attempt.id}
        courseSlug={courseSlug}
        initialSecondsLeft={examSecondsLeft(attempt.startedAt, examFormat.totalDurationMinutes)}
        mcqItems={mcqItems}
        frqItems={frqItems}
      />
    </Page>
  );
}
