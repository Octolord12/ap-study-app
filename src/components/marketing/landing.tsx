import Link from "next/link";
import { getDb } from "@/lib/db";
import { listCourses } from "@/lib/study/queries";
import { countWord } from "@/lib/count-word";
import { describeExamFormat, formatDuration } from "@/lib/content/exam-format";
import { renderSamples } from "@/lib/marketing/render-samples";
import { TESTIMONIALS } from "@/lib/marketing/testimonials";
import { ComingSoon } from "@/components/marketing/coming-soon";
import { SampleQuestion } from "@/components/marketing/sample-question";
import { Testimonials } from "@/components/marketing/testimonials";
import { Button } from "@/components/ui/button";
import { CourseTab } from "@/components/ui/course-tab";
import { Page, RuledList, Section } from "@/components/ui/page";

const HOW_IT_WORKS = [
  "Answer a question, then read why each choice is right or wrong, not only the one you picked.",
  "Questions come back on a schedule, sooner when you miss them, so the app picks your weak spots for you.",
  "Work from a daily set of five, a timed full-length exam with an estimated score range, or a boss battle at the end of each unit.",
  "Free-response prompts come with a rubric and a sample answer. You grade your own work against them.",
  "A correct answer earns 10 to 25 XP by difficulty, plus up to 10 for your streak. Friends and classes get leaderboards, and you can opt out of them.",
];

// Everything on this page that states a number reads it from the database, so
// the copy can't drift from the question bank.
export async function Landing() {
  const db = getDb();
  const [courses, mcqCounts, frqCounts, unitCounts] = await Promise.all([
    listCourses(),
    db.question.groupBy({ by: ["courseId"], _count: { _all: true } }),
    db.fRQPrompt.groupBy({ by: ["courseId"], _count: { _all: true } }),
    db.unit.groupBy({ by: ["courseId"], _count: { _all: true } }),
  ]);
  const countFor = (rows: { courseId: string; _count: { _all: number } }[], courseId: string) =>
    rows.find((r) => r.courseId === courseId)?._count._all ?? 0;
  const totalMcq = mcqCounts.reduce((sum, r) => sum + r._count._all, 0);
  const totalFrq = frqCounts.reduce((sum, r) => sum + r._count._all, 0);

  const samples = await renderSamples();

  return (
    <Page className="md:pt-14">
      <div className="grid grid-cols-[minmax(0,1fr)] items-start gap-10 lg:grid-cols-[minmax(0,5fr)_minmax(0,7fr)] lg:gap-14">
        <div>
          <h1 className="display text-[clamp(2.5rem,5.6vw,4.25rem)]">
            Practice for AP exams. Every incorrect answer analyzed.
          </h1>
          <p className="reading mt-6 max-w-[40ch] text-lg">
            {totalMcq.toLocaleString("en-US")} multiple-choice questions and {totalFrq} free-response prompts across {countWord(courses.length)} exams. Each
            answer choice comes with the reason it is right or wrong, so a miss teaches you something. Pick a tab and try one.
          </p>
          <div className="mt-8 flex flex-wrap items-center gap-x-6 gap-y-3">
            <Button render={<Link href="/signup" />} nativeButton={false} size="lg">
              Create an account
            </Button>
            <Link href="/login" className="text-sm font-bold underline underline-offset-4 hover:bg-mark hover:text-on-mark hover:no-underline">
              I already have one
            </Link>
          </div>
        </div>
        <SampleQuestion samples={samples} />
      </div>

      <div className="mt-16 border-t-[1.5px] border-foreground md:mt-24 [&>section:first-child]:border-t-0">
        <Section label="The exams" note="Section counts and timing as of 2026-27.">
          <RuledList>
            {courses.map((course) => {
              const format = course.examFormat as unknown as Parameters<typeof describeExamFormat>[0];
              return (
                <li key={course.id} className="grid gap-x-8 gap-y-1 py-5 md:grid-cols-[minmax(0,1.1fr)_minmax(0,1fr)]">
                  <h3 className="heading flex items-start gap-3 text-2xl">
                    <CourseTab slug={course.slug} name={course.name} className="mt-1 shrink-0 text-[0.8125rem]" />
                    <span>{course.name}</span>
                  </h3>
                  <div className="text-sm leading-relaxed text-muted-foreground">
                    <p>
                      {describeExamFormat(format)}. {formatDuration(format.totalDurationMinutes)}.
                    </p>
                    <p>
                      {countFor(unitCounts, course.id)} units, {countFor(mcqCounts, course.id)} questions,{" "}
                      {countFor(frqCounts, course.id)} free-response prompts
                    </p>
                  </div>
                </li>
              );
            })}
          </RuledList>
        </Section>

        <Section label="How it works">
          <ul className="grid max-w-[64ch] gap-3.5">
            {HOW_IT_WORKS.map((line) => (
              <li key={line} className="reading relative pl-6 text-[1.0625rem]">
                <span aria-hidden className="absolute top-[0.6em] left-0 size-2.5 rounded-full border-[1.5px] border-foreground" />
                {line}
              </li>
            ))}
          </ul>
        </Section>

        <Testimonials items={TESTIMONIALS} />

        <ComingSoon />
      </div>
    </Page>
  );
}
