import type { Metadata } from "next";
import Link from "next/link";
import { notFound, redirect } from "next/navigation";
import { requireUserId } from "@/lib/auth/session";
import { getDb } from "@/lib/db";
import { getTopicWithQuestions, getUserQuestionState } from "@/lib/study/queries";
import { topicHref, topicKey } from "@/lib/study/concept-link";
import { shuffled } from "@/lib/study/exam-selection";
import { renderContentToHtml } from "@/lib/content/render";
import { ReportProblem } from "@/components/study/report-problem";
import { Html } from "@/components/ui/html";
import { Button } from "@/components/ui/button";
import { Breadcrumb, Page, PageHeader, Section } from "@/components/ui/page";

// How many of the topic's questions the "Practice this topic" quiz asks.
const PRACTICE_SIZE = 10;

export async function generateMetadata({
  params,
}: {
  params: Promise<{ courseSlug: string; unitSlug: string; topicSlug: string }>;
}): Promise<Metadata> {
  const { courseSlug, unitSlug, topicSlug } = await params;
  const topic = await getDb().topic.findFirst({
    where: { slug: topicSlug, unit: { slug: unitSlug, course: { slug: courseSlug } } },
    select: { name: true },
  });
  return { title: topic ? `${topic.name}: refresher` : "Refresher" };
}

export default async function TopicRefresherPage({ params }: { params: Promise<{ courseSlug: string; unitSlug: string; topicSlug: string }> }) {
  const { courseSlug, unitSlug, topicSlug } = await params;
  const userId = await requireUserId();

  const result = await getTopicWithQuestions(courseSlug, unitSlug, topicSlug);
  if (!result) notFound();
  const { course, unit, topic } = result;

  // A topic whose refresher isn't written yet has nothing to show here; the unit page's topic filter
  // is what "Review this concept" meant before refreshers existed.
  if (!topic.refresher) redirect(topicHref(course.slug, unit.slug, topic.slug, false));

  const unitHref = `/courses/${course.slug}/units/${unit.slug}`;
  const here = topicHref(course.slug, unit.slug, topic.slug, true);

  const questionIds = topic.questions.map((q) => q.id);
  const [html, { latestCorrectByQuestion }] = await Promise.all([
    renderContentToHtml(topic.refresher, course.slug),
    getUserQuestionState(userId, questionIds),
  ]);

  const tried = questionIds.filter((id) => latestCorrectByQuestion.has(id)).length;
  const correct = questionIds.filter((id) => latestCorrectByQuestion.get(id) === true).length;

  const practiceIds = shuffled(questionIds).slice(0, PRACTICE_SIZE);
  const practiceHref =
    `/courses/${course.slug}/quiz?ids=${practiceIds.join(",")}&source=QUIZ` +
    `&back=${encodeURIComponent(here)}&backLabel=${encodeURIComponent("Back to the refresher")}`;

  const index = unit.topics.findIndex((t) => t.id === topic.id);
  const neighbour = (t: (typeof unit.topics)[number] | undefined) =>
    t ? { name: t.name, href: topicHref(course.slug, unit.slug, t.slug, Boolean(t.refresher)) } : null;
  const previous = neighbour(unit.topics[index - 1]);
  const next = neighbour(unit.topics[index + 1]);

  return (
    <Page>
      <PageHeader
        eyebrow={
          <Breadcrumb
            items={[
              { label: course.name, href: `/courses/${course.slug}` },
              { label: `Unit ${unit.order}`, href: unitHref },
              { label: topic.name },
            ]}
          />
        }
        title={topic.name}
        description={`A short refresher. ${unit.name}.`}
        actions={
          questionIds.length > 0 ? (
            <Button render={<Link href={practiceHref} />} nativeButton={false}>
              Practice this topic
            </Button>
          ) : null
        }
      />

      <Section label="Refresher">
        <Html html={html} className="max-w-[64ch]" />
        {!topic.refresherReviewed ? (
          <p className="mt-6 max-w-[64ch] text-sm text-muted-foreground">
            This refresher was written with AI help and has not been checked by a person yet, so it may contain mistakes.
          </p>
        ) : null}
        <p className="mt-4">
          <ReportProblem id={`${course.slug}/${topicKey(unit.slug, topic.slug)}`} kind="refresher" />
        </p>
      </Section>

      {questionIds.length > 0 ? (
        <Section label="Your practice" note="From your latest answer to each question in this topic.">
          <p className="reading">
            {tried === 0
              ? `${questionIds.length} questions in this topic, none tried yet.`
              : `${tried} of ${questionIds.length} questions tried, ${correct} answered correctly the last time.`}
          </p>
          <p className="mt-3">
            <Link href={`${unitHref}?topic=${topic.slug}`} className="text-sm font-semibold underline underline-offset-4 hover:bg-mark hover:text-on-mark hover:no-underline">
              See all the questions in this topic
            </Link>
          </p>
        </Section>
      ) : null}

      {previous || next ? (
        <nav aria-label="Other topics in this unit" className="mt-10 flex flex-wrap justify-between gap-x-6 gap-y-3 border-t border-border pt-6 text-sm">
          {previous ? (
            <Link href={previous.href} className="underline-offset-4 hover:bg-mark hover:text-on-mark hover:no-underline">
              <span className="eyebrow block">Previous topic</span>
              <span className="font-semibold">{previous.name}</span>
            </Link>
          ) : (
            <span />
          )}
          {next ? (
            <Link href={next.href} className="text-right underline-offset-4 hover:bg-mark hover:text-on-mark hover:no-underline">
              <span className="eyebrow block">Next topic</span>
              <span className="font-semibold">{next.name}</span>
            </Link>
          ) : null}
        </nav>
      ) : null}
    </Page>
  );
}
