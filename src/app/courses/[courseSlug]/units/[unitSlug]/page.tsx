import Link from "next/link";
import { notFound } from "next/navigation";
import { requireUserId } from "@/lib/auth/session";
import { getUnitWithQuestions, getUserQuestionState } from "@/lib/study/queries";
import { UnitQuestionBrowser, type QuestionRow } from "@/components/study/unit-question-browser";

export default async function UnitPage({
  params,
  searchParams,
}: {
  params: Promise<{ courseSlug: string; unitSlug: string }>;
  searchParams: Promise<{ topic?: string }>;
}) {
  const { courseSlug, unitSlug } = await params;
  const { topic } = await searchParams;
  const userId = await requireUserId();

  const result = await getUnitWithQuestions(courseSlug, unitSlug);
  if (!result) notFound();
  const { course, unit } = result;

  const { bookmarkedIds, latestCorrectByQuestion } = await getUserQuestionState(
    userId,
    unit.questions.map((q) => q.id),
  );

  const questionRows: QuestionRow[] = unit.questions.map((q) => ({
    id: q.id,
    difficulty: q.difficulty,
    topicSlug: q.topic.slug,
    topicName: q.topic.name,
    bookmarked: bookmarkedIds.has(q.id),
    missed: latestCorrectByQuestion.has(q.id) ? !latestCorrectByQuestion.get(q.id) : undefined,
  }));

  return (
    <div className="mx-auto w-full max-w-3xl px-6 py-10">
      <p className="mb-1 text-sm text-muted-foreground">
        <Link href={`/courses/${course.slug}`} className="hover:text-foreground">
          {course.name}
        </Link>
      </p>
      <h1 className="mb-1 text-2xl font-bold tracking-tight">{unit.name}</h1>
      <p className="mb-6 text-sm text-muted-foreground">
        {unit.weightingMin}–{unit.weightingMax}% of exam
      </p>

      <div className="mb-6 flex flex-wrap gap-2">
        {unit.topics.map((topic) => (
          <span key={topic.id} className="rounded-full border border-border px-3 py-1 text-xs text-muted-foreground">
            {topic.name}
          </span>
        ))}
      </div>

      <h2 className="mb-3 text-sm font-semibold uppercase tracking-wide text-muted-foreground">Questions</h2>
      <UnitQuestionBrowser
        courseSlug={course.slug}
        unitSlug={unit.slug}
        questions={questionRows}
        initialTopicSlug={topic}
      />

      {unit.frqPrompts.length > 0 ? (
        <>
          <h2 className="mt-8 mb-3 text-sm font-semibold uppercase tracking-wide text-muted-foreground">
            Free response
          </h2>
          <ul className="divide-y divide-border rounded-lg border border-border">
            {unit.frqPrompts.map((frq, index) => (
              <li key={frq.id} className="flex items-center justify-between px-4 py-2 text-sm">
                <span>
                  FRQ {index + 1} · {frq.topic.name} · {frq.pointValue} pts
                </span>
                <Link
                  href={`/courses/${course.slug}/units/${unit.slug}/frq/${frq.id}`}
                  className="font-medium underline underline-offset-4"
                >
                  Practice
                </Link>
              </li>
            ))}
          </ul>
        </>
      ) : null}
    </div>
  );
}
