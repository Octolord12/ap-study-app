import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { requireAdminUserId } from "@/lib/admin/session";
import { getUnitUnreviewedContent } from "@/lib/admin/queries";
import { approveUnitContent, markFrqReviewed, markQuestionReviewed, markRefresherReviewed } from "@/lib/admin/actions";
import { ApproveAllButton } from "@/components/admin/approve-all-button";
import { renderChoiceTextToHtml, renderContentToHtml } from "@/lib/content/render";
import { Button } from "@/components/ui/button";
import { ChoiceList, ChoiceRow } from "@/components/ui/choice";
import { Html } from "@/components/ui/html";
import { Breadcrumb, Page, PageHeader, Section } from "@/components/ui/page";
import { Sheet } from "@/components/ui/sheet";
import { renderRubric } from "@/lib/study/render-rubric";
import { DiagramRenderer } from "@/components/diagrams/diagram-renderer";
import type { Diagram } from "@/lib/content/diagram-schema";
import { isPaperLinedCourse } from "@/lib/content/paper-lined";

export const metadata: Metadata = { title: "Content review" };

export default async function AdminReviewUnitPage({
  params,
}: {
  params: Promise<{ courseSlug: string; unitSlug: string }>;
}) {
  await requireAdminUserId();
  const { courseSlug, unitSlug } = await params;

  const result = await getUnitUnreviewedContent(courseSlug, unitSlug);
  if (!result) notFound();
  const { course, unit } = result;
  const paperLined = isPaperLinedCourse(courseSlug);
  const questions = await Promise.all(
    unit.questions.map(async (question) => ({
      ...question,
      stemHtml: await renderContentToHtml(question.stem, courseSlug),
      explanationHtml: await renderContentToHtml(question.explanation, courseSlug),
      choices: await Promise.all(
        question.choices.map(async (choice) => ({ ...choice, textHtml: await renderChoiceTextToHtml(choice.text, courseSlug) })),
      ),
    })),
  );
  const frqPrompts = await Promise.all(
    unit.frqPrompts.map(async (frq) => ({
      ...frq,
      promptHtml: await renderContentToHtml(frq.prompt, courseSlug),
      sampleResponseHtml: await renderContentToHtml(frq.sampleResponse, courseSlug),
      rubricLines: await renderRubric(frq.rubric, courseSlug),
    })),
  );

  const refreshers = await Promise.all(
    unit.topics.map(async (topic) => ({ ...topic, refresherHtml: await renderContentToHtml(topic.refresher ?? "", courseSlug) })),
  );

  const pendingCount = unit.questions.length + unit.frqPrompts.length + unit.topics.length;
  const approveAll =
    pendingCount > 0 ? (
      <ApproveAllButton
        count={pendingCount}
        action={approveUnitContent.bind(
          null,
          unit.id,
          unit.questions.map((q) => q.id),
          unit.frqPrompts.map((f) => f.id),
          unit.topics.map((t) => t.id),
        )}
      />
    ) : null;

  return (
    <Page>
      <PageHeader
        eyebrow={
          <Breadcrumb
            items={[
              { label: "Content review", href: "/admin/review" },
              { label: course.name, href: `/admin/review/${course.slug}` },
            ]}
          />
        }
        title={unit.name}
        description={pendingCount === 0 ? "Everything in this unit has been reviewed." : undefined}
      />

      {approveAll ? (
        <Section label="Whole unit" note="Or read each item below and approve it one at a time.">
          {approveAll}
        </Section>
      ) : null}

      {refreshers.length > 0 ? (
        <Section label={`Refreshers (${refreshers.length})`} note="Check the facts and the examples, not just the wording.">
          <div className="space-y-8">
            {refreshers.map((topic) => (
              <Sheet key={topic.id} lined={paperLined}>
                <p className="eyebrow">Refresher · {topic.name}</p>
                <Html html={topic.refresherHtml} className="mt-2" />
                <form action={markRefresherReviewed.bind(null, topic.id)} className="mt-5">
                  <Button type="submit">Approve</Button>
                </form>
              </Sheet>
            ))}
          </div>
        </Section>
      ) : null}

      {unit.questions.length > 0 ? (
        <Section label={`Questions (${unit.questions.length})`}>
          <div className="space-y-8">
            {questions.map((question) => (
              <Sheet key={question.id} lined={paperLined}>
                <p className="eyebrow">
                  {question.topic.name} · {question.difficulty.toLowerCase()}
                </p>
                <Html html={question.stemHtml} className="mt-2" />
                {question.diagram && <DiagramRenderer diagram={question.diagram as unknown as Diagram} />}
                <div className="mt-4">
                  <ChoiceList legend="Answer choices">
                    {question.choices.map((choice) => (
                      <ChoiceRow
                        key={choice.id}
                        label={choice.label}
                        textHtml={choice.textHtml}
                        state={choice.isCorrect ? "correct" : "idle"}
                        verdict={choice.isCorrect ? "Correct" : undefined}
                      />
                    ))}
                  </ChoiceList>
                </div>
                <div className="mt-5 border-t-2 border-current pt-4">
                  <p className="eyebrow !text-current">Explanation</p>
                  <Html html={question.explanationHtml} size="sm" className="mt-1.5" />
                </div>
                <form action={markQuestionReviewed.bind(null, question.id)} className="mt-5">
                  <Button type="submit">Approve</Button>
                </form>
              </Sheet>
            ))}
          </div>
        </Section>
      ) : null}

      {unit.frqPrompts.length > 0 ? (
        <Section label={`Free response (${unit.frqPrompts.length})`}>
          <div className="space-y-8">
            {frqPrompts.map((frq) => (
              <Sheet key={frq.id} lined={paperLined}>
                <p className="eyebrow">
                  {frq.topic.name} · {frq.pointValue} pts
                </p>
                <Html html={frq.promptHtml} className="mt-2" />
                {frq.diagram && <DiagramRenderer diagram={frq.diagram as unknown as Diagram} />}
                <div className="mt-5 border-t-2 border-current pt-4">
                  <p className="eyebrow !text-current">Rubric</p>
                  <ul className="mt-2 space-y-2 text-sm">
                    {frq.rubricLines.map((line) => (
                      <li key={line.id}>
                        <span className="font-semibold tabular-nums">
                          {line.points} pt{line.points === 1 ? "" : "s"}
                        </span>{" "}
                        <Html html={line.descriptionHtml} inline size="sm" className="inline" />
                      </li>
                    ))}
                  </ul>
                </div>
                <div className="mt-5 border-t-2 border-current pt-4">
                  <p className="eyebrow !text-current">Sample response</p>
                  <Html html={frq.sampleResponseHtml} size="sm" className="mt-1.5" />
                </div>
                <form action={markFrqReviewed.bind(null, frq.id)} className="mt-5">
                  <Button type="submit">Approve</Button>
                </form>
              </Sheet>
            ))}
          </div>
        </Section>
      ) : null}

      {approveAll ? <Section label="Whole unit">{approveAll}</Section> : null}
    </Page>
  );
}
