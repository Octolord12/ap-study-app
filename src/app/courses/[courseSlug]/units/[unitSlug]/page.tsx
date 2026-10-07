import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { requireUserId } from "@/lib/auth/session";
import { getDb } from "@/lib/db";
import { getUnitWithQuestions, getUserQuestionState } from "@/lib/study/queries";
import { UnitQuestionBrowser, type QuestionRow } from "@/components/study/unit-question-browser";
import { Button } from "@/components/ui/button";
import { BadgeStamp } from "@/components/ui/stamp";
import { Breadcrumb, Page, PageHeader, RuledList, Section } from "@/components/ui/page";
import { topicHref } from "@/lib/study/concept-link";
import { cn } from "cn";

export async function generateMetadata({
  params,
}: {
  params: Promise<{ courseSlug: string; unitSlug: string }>;
}): Promise<Metadata> {
  const { courseSlug, unitSlug } = await params;
  const unit = await getDb().unit.findFirst({
    where: { slug: unitSlug, course: { slug: courseSlug } },
    select: { name: true },
  });
  return { title: unit?.name ?? "Unit" };
}

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

  const [{ bookmarkedIds, latestCorrectByQuestion }, bossBattle] = await Promise.all([
    getUserQuestionState(
      userId,
      unit.questions.map((q) => q.id),
    ),
    getDb().bossBattleAttempt.findUnique({ where: { userId_unitId: { userId, unitId: unit.id } } }),
  ]);

  const questionRows: QuestionRow[] = unit.questions.map((q) => ({
    id: q.id,
    difficulty: q.difficulty,
    topicSlug: q.topic.slug,
    topicName: q.topic.name,
    bookmarked: bookmarkedIds.has(q.id),
    missed: latestCorrectByQuestion.has(q.id) ? !latestCorrectByQuestion.get(q.id) : undefined,
  }));

  const unitHref = `/courses/${course.slug}/units/${unit.slug}`;

  return (
    <Page>
      <PageHeader
        eyebrow={
          <Breadcrumb
            items={[
              { label: course.name, href: `/courses/${course.slug}` },
              { label: `Unit ${unit.order}` },
            ]}
          />
        }
        title={unit.name}
        description={`${unit.weightingMin}–${unit.weightingMax}% of the exam. ${unit.topics.length} topics, ${unit.questions.length} questions${unit.frqPrompts.length > 0 ? `, ${unit.frqPrompts.length} free-response prompts` : ""}.`}
      />

      <Section label="Topics" note="Pick one to filter the questions below.">
        <ul className="flex flex-wrap gap-x-1 gap-y-1">
          {[{ id: "all", slug: undefined, name: "All topics" }, ...unit.topics.map((t) => ({ id: t.id, slug: t.slug, name: t.name }))].map((t) => {
            const active = (topic ?? undefined) === t.slug;
            return (
              <li key={t.id}>
                <Link
                  href={t.slug ? `${unitHref}?topic=${t.slug}` : unitHref}
                  aria-current={active ? "true" : undefined}
                  className={cn(
                    "inline-block px-2 py-1.5 text-sm font-medium underline-offset-4",
                    active ? "bg-mark text-on-mark" : "hover:underline"
                  )}
                >
                  {t.name}
                </Link>
              </li>
            );
          })}
        </ul>
      </Section>

      {unit.topics.some((t) => t.refresher) ? (
        <Section label="Refreshers" note="A short read on each topic, for when something isn't clicking.">
          <RuledList>
            {unit.topics
              .filter((t) => t.refresher)
              .map((t) => (
                <li key={t.id} className="flex flex-wrap items-center justify-between gap-x-6 gap-y-2 py-3 text-sm">
                  <span>{t.name}</span>
                  <Link
                    href={topicHref(course.slug, unit.slug, t.slug, true)}
                    className="font-semibold underline underline-offset-4 hover:bg-mark hover:text-on-mark hover:no-underline"
                  >
                    Read
                  </Link>
                </li>
              ))}
          </RuledList>
        </Section>
      ) : null}

      {unit.questions.length > 0 ? (
        <Section label="Boss battle" note="Answer 70% correctly to conquer the unit.">
          <div className="flex flex-wrap items-center justify-between gap-x-6 gap-y-4">
            <div className="flex items-center gap-4">
              {bossBattle?.passed ? <BadgeStamp slug="boss_slayer" className="size-14" /> : null}
              <div>
                <p className="heading text-xl">{bossBattle?.passed ? "Unit conquered" : "Unit boss battle"}</p>
                <p className="mt-0.5 text-sm text-muted-foreground">
                  {bossBattle?.passed
                    ? `Defeated in ${bossBattle.attemptsCount} attempt${bossBattle.attemptsCount === 1 ? "" : "s"}`
                    : "Every question in the unit, with a health bar that drains as you get them right."}
                </p>
              </div>
            </div>
            <Button render={<Link href={`${unitHref}/boss`} />} nativeButton={false} variant={bossBattle?.passed ? "outline" : "default"}>
              {bossBattle?.passed ? "Battle again" : "Fight"}
            </Button>
          </div>
        </Section>
      ) : null}

      <Section label="Questions">
        <UnitQuestionBrowser
          key={topic ?? "all"}
          courseSlug={course.slug}
          unitSlug={unit.slug}
          questions={questionRows}
          initialTopicSlug={topic}
        />
      </Section>

      {unit.frqPrompts.length > 0 ? (
        <Section label="Free response" note="Write your answer, then grade it against the rubric.">
          <RuledList>
            {unit.frqPrompts.map((frq, index) => (
              <li key={frq.id} className="flex flex-wrap items-center justify-between gap-x-6 gap-y-2 py-3 text-sm">
                <span className="flex min-w-0 flex-wrap items-baseline gap-x-3">
                  <span className="eyebrow !text-foreground">FRQ {index + 1}</span>
                  <span>{frq.topic.name}</span>
                  <span className="eyebrow">{frq.pointValue} pts</span>
                </span>
                <Button render={<Link href={`${unitHref}/frq/${frq.id}`} />} nativeButton={false} variant="outline" size="sm">
                  Practice
                </Button>
              </li>
            ))}
          </RuledList>
        </Section>
      ) : null}
    </Page>
  );
}
