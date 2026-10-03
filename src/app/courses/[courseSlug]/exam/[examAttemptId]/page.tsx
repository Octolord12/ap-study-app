import { notFound, redirect } from "next/navigation";
import { requireUserId } from "@/lib/auth/session";
import { getDb } from "@/lib/db";
import { renderChoiceTextToHtml, renderContentToHtml } from "@/lib/content/render";
import { ExamRunner, type ExamFrqItem, type ExamMcqItem } from "@/components/study/exam-runner";
import type { Course as ContentCourse } from "@/lib/content/schema";
import type { Diagram } from "@/lib/content/diagram-schema";

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
      .map(async (q) => ({
        id: q.id,
        stemHtml: await renderContentToHtml(q.stem, courseSlug),
        diagram: (q.diagram as Diagram | null) ?? null,
        choices: await Promise.all(
          q.choices.map(async (c) => ({
            id: c.id,
            label: c.label,
            textHtml: await renderChoiceTextToHtml(c.text, courseSlug),
          })),
        ),
      })),
  );

  const frqItems: ExamFrqItem[] = await Promise.all(
    frqPromptIds
      .map((id) => frqById.get(id))
      .filter((f): f is NonNullable<typeof f> => f !== undefined)
      .map(async (f) => ({
        id: f.id,
        promptHtml: await renderContentToHtml(f.prompt, courseSlug),
        diagram: (f.diagram as Diagram | null) ?? null,
        pointValue: f.pointValue,
      })),
  );

  return (
    <div className="mx-auto w-full max-w-2xl px-6 py-10">
      <ExamRunner
        examAttemptId={attempt.id}
        courseSlug={courseSlug}
        totalDurationMinutes={examFormat.totalDurationMinutes}
        mcqItems={mcqItems}
        frqItems={frqItems}
      />
    </div>
  );
}
