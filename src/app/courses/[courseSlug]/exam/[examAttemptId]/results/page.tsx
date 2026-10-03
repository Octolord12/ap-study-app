import type { Metadata } from "next";
import { notFound, redirect } from "next/navigation";
import { requireUserId } from "@/lib/auth/session";
import { getDb } from "@/lib/db";
import { renderContentToHtml } from "@/lib/content/render";
import { renderQuizQuestions } from "@/lib/study/render-quiz";
import { ExamMcqReview } from "@/components/study/exam-mcq-review";
import { FrqSelfGrade } from "@/components/study/frq-self-grade";
import { renderRubric } from "@/lib/study/render-rubric";
import { DiagramRenderer } from "@/components/diagrams/diagram-renderer";
import { Html } from "@/components/ui/html";
import { Breadcrumb, Page, PageHeader, Section } from "@/components/ui/page";
import { Sheet } from "@/components/ui/sheet";
import type { Diagram } from "@/lib/content/diagram-schema";
import { isPaperLinedCourse } from "@/lib/content/paper-lined";

export const metadata: Metadata = { title: "Exam results" };

export default async function ExamResultsPage({
  params,
}: {
  params: Promise<{ courseSlug: string; examAttemptId: string }>;
}) {
  const userId = await requireUserId();
  const { courseSlug, examAttemptId } = await params;
  const db = getDb();
  const paperLined = isPaperLinedCourse(courseSlug);

  const attempt = await db.examAttempt.findUnique({ where: { id: examAttemptId } });
  if (!attempt || attempt.userId !== userId) notFound();
  if (!attempt.completedAt) redirect(`/courses/${courseSlug}/exam/${attempt.id}`);

  const questionIds = attempt.questionIds as string[];
  const frqPromptIds = attempt.frqPromptIds as string[];
  const sectionScores = attempt.sectionScores as unknown as { mcqCorrect: number; mcqTotal: number };

  const [renderedQuestions, chosenAttempts, frqPrompts, existingFrqAttempts, course] = await Promise.all([
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
    db.course.findUnique({ where: { slug: courseSlug }, select: { name: true } }),
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
      promptHtml: await renderContentToHtml(frq.prompt, courseSlug),
      sampleResponseHtml: await renderContentToHtml(frq.sampleResponse, courseSlug),
      diagram: (frq.diagram as Diagram | null) ?? null,
      rubric: await renderRubric(frq.rubric, courseSlug),
      existingAttempt: frqAttemptByPromptId.get(frq.id),
    })),
  );

  return (
    <Page>
      <PageHeader
        eyebrow={
          <Breadcrumb
            items={[
              { label: course?.name ?? "Course", href: `/courses/${courseSlug}` },
              { label: "Exam results" },
            ]}
          />
        }
        title="Exam results"
      />

      <Section label="Score">
        <div className="flex flex-wrap items-end gap-x-14 gap-y-6">
          <div>
            <p className="numeral text-6xl">
              {sectionScores.mcqCorrect} / {sectionScores.mcqTotal}
            </p>
            <p className="eyebrow mt-2">Multiple choice correct</p>
          </div>
          <div>
            <p className="numeral text-6xl">{attempt.estimatedScore}</p>
            <p className="eyebrow mt-2">Estimated AP score</p>
          </div>
        </div>
        <p className="mt-5 max-w-[52ch] text-sm text-muted-foreground">
          The estimate comes from multiple-choice accuracy only, so treat it as a rough guide and not a prediction.
        </p>
      </Section>

      {frqSections.length > 0 ? (
        <Section label="Free response" note="Grade your own responses against each rubric.">
          <div className="space-y-6">
            {frqSections.map(({ frq, promptHtml, sampleResponseHtml, diagram, rubric, existingAttempt }) => (
              <Sheet key={frq.id} lined={paperLined}>
                <div className="space-y-6">
                  <div>
                    <p className="eyebrow mb-2">
                      {frq.pointValue} point{frq.pointValue === 1 ? "" : "s"}
                    </p>
                    <Html html={promptHtml} />
                    {diagram && <DiagramRenderer diagram={diagram} />}
                  </div>
                  <FrqSelfGrade
                    frqPromptId={frq.id}
                    pointValue={frq.pointValue}
                    rubric={rubric}
                    sampleResponseHtml={sampleResponseHtml}
                    existingResponseText={existingAttempt?.responseText ?? ""}
                    existingAttemptId={existingAttempt?.id}
                  />
                </div>
              </Sheet>
            ))}
          </div>
        </Section>
      ) : null}

      <Section label="Multiple choice review" note="Every answer choice, with the reason.">
        <ExamMcqReview
          questions={renderedQuestions}
          chosenLabelByQuestionId={chosenLabelByQuestionId}
          paperLined={paperLined}
        />
      </Section>
    </Page>
  );
}
