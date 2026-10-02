import Link from "next/link";
import { notFound } from "next/navigation";
import { requireAdminUserId } from "@/lib/admin/session";
import { getUnitUnreviewedContent } from "@/lib/admin/queries";
import { markFrqReviewed, markQuestionReviewed } from "@/lib/admin/actions";
import { ContentRenderer } from "@/components/content-renderer";
import { renderContentToHtml } from "@/lib/content/render";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader } from "@/components/ui/card";
import type { RubricLine } from "@/lib/scoring/grading";
import { DiagramRenderer } from "@/components/diagrams/diagram-renderer";
import type { Diagram } from "@/lib/content/diagram-schema";
import { isPaperLinedCourse } from "@/lib/content/paper-lined";

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
      choices: await Promise.all(
        question.choices.map(async (choice) => ({ ...choice, textHtml: await renderContentToHtml(choice.text) })),
      ),
    })),
  );

  return (
    <div className="mx-auto w-full max-w-3xl px-6 py-10">
      <p className="mb-1 text-sm text-muted-foreground">
        <Link href="/admin/review" className="hover:text-foreground">
          Content review
        </Link>{" "}
        /{" "}
        <Link href={`/admin/review/${course.slug}`} className="hover:text-foreground">
          {course.name}
        </Link>
      </p>
      <h1 className="mb-6 text-2xl font-bold tracking-tight">{unit.name}</h1>

      {unit.questions.length === 0 && unit.frqPrompts.length === 0 ? (
        <p className="text-sm text-muted-foreground">Everything in this unit has been reviewed.</p>
      ) : null}

      {unit.questions.length > 0 ? (
        <>
          <h2 className="mb-3 text-sm font-semibold uppercase tracking-wide text-muted-foreground">
            Questions ({unit.questions.length})
          </h2>
          <div className="mb-8 grid gap-4">
            {questions.map((question) => (
              <Card key={question.id} className={paperLined ? "paper-lined" : undefined}>
                <CardHeader>
                  <p className="text-xs text-muted-foreground">
                    {question.topic.name} · {question.difficulty}
                  </p>
                </CardHeader>
                <CardContent>
                  <ContentRenderer>{question.stem}</ContentRenderer>
                  {question.diagram && <DiagramRenderer diagram={question.diagram as unknown as Diagram} />}
                  <ul className="mt-3 space-y-1">
                    {question.choices.map((choice) => (
                      <li
                        key={choice.id}
                        className={
                          choice.isCorrect
                            ? "rounded border border-primary/40 bg-primary/5 px-2 py-1 text-sm"
                            : "px-2 py-1 text-sm text-muted-foreground"
                        }
                      >
                        <span className="flex items-start gap-1.5">
                          <span className="font-medium">{choice.label}.</span>{" "}
                          <span
                            className="[&_p]:m-0 [&_p]:inline"
                            dangerouslySetInnerHTML={{ __html: choice.textHtml }}
                          />
                        </span>
                      </li>
                    ))}
                  </ul>
                  <div className="mt-3 text-sm text-muted-foreground">
                    <ContentRenderer>{question.explanation}</ContentRenderer>
                  </div>
                  <form action={markQuestionReviewed.bind(null, question.id)} className="mt-4">
                    <Button type="submit" size="sm">
                      Approve
                    </Button>
                  </form>
                </CardContent>
              </Card>
            ))}
          </div>
        </>
      ) : null}

      {unit.frqPrompts.length > 0 ? (
        <>
          <h2 className="mb-3 text-sm font-semibold uppercase tracking-wide text-muted-foreground">
            Free response ({unit.frqPrompts.length})
          </h2>
          <div className="grid gap-4">
            {unit.frqPrompts.map((frq) => {
              const rubric = frq.rubric as unknown as RubricLine[];
              return (
                <Card key={frq.id} className={paperLined ? "paper-lined" : undefined}>
                  <CardHeader>
                    <p className="text-xs text-muted-foreground">
                      {frq.topic.name} · {frq.pointValue} pts
                    </p>
                  </CardHeader>
                  <CardContent>
                    <ContentRenderer>{frq.prompt}</ContentRenderer>
                    {frq.diagram && <DiagramRenderer diagram={frq.diagram as unknown as Diagram} />}
                    <ul className="mt-3 list-inside list-disc space-y-1 text-sm text-muted-foreground">
                      {rubric.map((line) => (
                        <li key={line.id}>
                          ({line.points} pt{line.points === 1 ? "" : "s"}) {line.description}
                        </li>
                      ))}
                    </ul>
                    <div className="mt-3 text-sm text-muted-foreground">
                      <ContentRenderer>{frq.sampleResponse}</ContentRenderer>
                    </div>
                    <form action={markFrqReviewed.bind(null, frq.id)} className="mt-4">
                      <Button type="submit" size="sm">
                        Approve
                      </Button>
                    </form>
                  </CardContent>
                </Card>
              );
            })}
          </div>
        </>
      ) : null}
    </div>
  );
}
