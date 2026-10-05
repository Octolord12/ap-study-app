import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { requireUserId } from "@/lib/auth/session";
import { getDb } from "@/lib/db";
import { getCourseTree } from "@/lib/study/queries";
import { enrollInCourse } from "@/lib/study/actions";
import { computeUnitMastery } from "@/lib/study/mastery";
import { getCourseCoverage } from "@/lib/study/coverage";
import { isCramModeOn } from "@/lib/study/cram-mode";
import { toIsoDate } from "@/lib/study/exam-plan";
import { ExamCountdown } from "@/components/study/exam-countdown";
import { ExamDateForm } from "@/components/study/exam-date-form";
import { describeExamFormat, formatDuration } from "@/lib/content/exam-format";
import { Button } from "@/components/ui/button";
import { Bubbles, WeightBar } from "@/components/ui/meter";
import { Breadcrumb, Page, PageHeader, RuledList, Section } from "@/components/ui/page";

export async function generateMetadata({ params }: { params: Promise<{ courseSlug: string }> }): Promise<Metadata> {
  const { courseSlug } = await params;
  const course = await getDb().course.findUnique({ where: { slug: courseSlug }, select: { name: true } });
  return { title: course?.name ?? "Course" };
}

export default async function CoursePage({ params }: { params: Promise<{ courseSlug: string }> }) {
  const { courseSlug } = await params;
  const userId = await requireUserId();

  const course = await getCourseTree(courseSlug);
  if (!course) notFound();

  const [enrollment, attempts] = await Promise.all([
    getDb().enrollment.findUnique({ where: { userId_courseId: { userId, courseId: course.id } } }),
    getDb().questionAttempt.findMany({
      where: { userId, question: { courseId: course.id } },
      select: { questionId: true, correct: true, createdAt: true, question: { select: { unitId: true } } },
    }),
  ]);
  const [coverage, cramOn] = enrollment ? await Promise.all([getCourseCoverage(userId, course.id), isCramModeOn(userId)]) : [null, false];
  const examDateIso = enrollment?.examDate ? toIsoDate(enrollment.examDate, "utc") : null;
  const masteryByUnitId = new Map(
    computeUnitMastery(
      attempts.map((a) => ({ questionId: a.questionId, unitId: a.question.unitId, correct: a.correct, createdAt: a.createdAt })),
    ).map((m) => [m.unitId, m]),
  );

  const format = course.examFormat as unknown as Parameters<typeof describeExamFormat>[0];
  const enrollAction = enrollInCourse.bind(null, course.id);

  return (
    <Page>
      <PageHeader
        eyebrow={<Breadcrumb items={[{ label: "Courses", href: "/courses" }, { label: course.name }]} />}
        title={course.name}
        description={course.description}
        actions={
          enrollment ? (
            <Button render={<Link href={`/courses/${course.slug}/practice`} />} nativeButton={false} size="lg">
              Practice
            </Button>
          ) : (
            <form action={enrollAction}>
              <Button type="submit" size="lg">
                Start studying
              </Button>
            </form>
          )
        }
      />

      {enrollment && coverage ? (
        <Section label="Exam date" note="Set it and the app paces you.">
          <div id="exam-date" className="grid gap-x-12 gap-y-8 lg:grid-cols-[minmax(0,1fr)_minmax(0,1.1fr)]">
            <ExamDateForm courseId={course.id} currentIso={examDateIso} />
            {examDateIso ? (
              <ExamCountdown examDateIso={examDateIso} total={coverage.total} tried={coverage.tried} newPerDay={coverage.newPerDayLast7} cramOn={cramOn} />
            ) : (
              <p className="reading max-w-[48ch]">
                With a date, this page and Today show the days left, how many new questions a day it takes to try them all, and whether you are on pace.
              </p>
            )}
          </div>
        </Section>
      ) : null}

      <Section label="Units" note="Weight is the share of the exam each unit makes up.">
        <RuledList>
          {course.units.map((unit, index) => {
            const m = masteryByUnitId.get(unit.id);
            const attempted = m?.questionsAttempted ?? 0;
            const percent = m && attempted > 0 ? Math.round((m.questionsCorrect / attempted) * 100) : null;
            return (
              <li key={unit.id}>
                <Link
                  href={`/courses/${course.slug}/units/${unit.slug}`}
                  className="group grid gap-x-6 gap-y-3 py-5 sm:grid-cols-[3rem_minmax(0,1fr)_auto]"
                >
                  <span className="numeral hidden text-3xl text-muted-foreground sm:block">{String(index + 1).padStart(2, "0")}</span>
                  <div className="min-w-0">
                    <p className="eyebrow sm:hidden">Unit {String(index + 1).padStart(2, "0")}</p>
                    <h3 className="heading text-xl underline-offset-4 decoration-2 group-hover:underline">{unit.name}</h3>
                    <p className="mt-1.5 text-sm text-muted-foreground">
                      {unit.weightingMin}–{unit.weightingMax}% of exam · {unit.topics.length} topics
                    </p>
                    <WeightBar
                      min={unit.weightingMin}
                      max={unit.weightingMax}
                      label={`${unit.weightingMin} to ${unit.weightingMax} percent of the exam`}
                      className="mt-2"
                    />
                  </div>
                  <div className="flex items-center gap-3 sm:flex-col sm:items-end sm:gap-1.5">
                    <Bubbles percent={percent} />
                    <span className="eyebrow">{percent === null ? "Not started" : `${percent}% of ${attempted}`}</span>
                  </div>
                </Link>
              </li>
            );
          })}
        </RuledList>
      </Section>

      <Section label="The exam" note="Format as of 2026-27.">
        <p className="reading max-w-[56ch]">
          {describeExamFormat(format)}, in {formatDuration(format.totalDurationMinutes)}.
        </p>
        {enrollment ? (
          <Button render={<Link href={`/courses/${course.slug}/exam`} />} nativeButton={false} variant="outline" className="mt-4">
            Take a practice exam
          </Button>
        ) : null}
      </Section>
    </Page>
  );
}
