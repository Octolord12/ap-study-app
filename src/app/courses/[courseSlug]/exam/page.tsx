import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { requireUserId } from "@/lib/auth/session";
import { getDb } from "@/lib/db";
import { startExam } from "@/lib/study/actions";
import { formatDuration, SECTION_NAMES } from "@/lib/content/exam-format";
import { Button } from "@/components/ui/button";
import { Breadcrumb, Page, PageHeader, RuledList, Section } from "@/components/ui/page";
import type { Course as ContentCourse } from "@/lib/content/schema";

export const metadata: Metadata = { title: "Exam simulation" };

export default async function ExamIntroPage({ params }: { params: Promise<{ courseSlug: string }> }) {
  await requireUserId();
  const { courseSlug } = await params;

  const course = await getDb().course.findUnique({ where: { slug: courseSlug } });
  if (!course) notFound();

  const examFormat = course.examFormat as unknown as ContentCourse["examFormat"];
  const mcqSection = examFormat.sections.find((s) => s.type === "MCQ");

  const [availableQuestions, frqSupply] = await Promise.all([
    getDb().question.count({ where: { courseId: course.id } }),
    getDb().fRQPrompt.groupBy({ by: ["type"], where: { courseId: course.id }, _count: { _all: true } }),
  ]);
  const availableFrqs = frqSupply.reduce((sum, row) => sum + row._count._all, 0);
  const frqShort = examFormat.sections.some(
    (s) => s.type !== "MCQ" && (frqSupply.find((row) => row.type === s.type)?._count._all ?? 0) < s.questionCount,
  );
  const short = availableQuestions < (mcqSection?.questionCount ?? 0) || frqShort;

  const startExamAction = startExam.bind(null, course.id, course.slug);

  return (
    <Page>
      <PageHeader
        eyebrow={
          <Breadcrumb
            items={[
              { label: course.name, href: `/courses/${course.slug}` },
              { label: "Practice", href: `/courses/${course.slug}/practice` },
              { label: "Exam" },
            ]}
          />
        }
        title="Exam simulation"
        description={`The real ${course.name} exam runs ${formatDuration(examFormat.totalDurationMinutes)}. This one is timed the same way and shows no explanations until you submit.`}
      />

      <Section label="Sections">
        <RuledList>
          {examFormat.sections.map((section) => (
            <li key={section.type} className="grid gap-x-6 gap-y-1 py-4 sm:grid-cols-[minmax(0,1fr)_auto]">
              <p className="heading text-xl capitalize">{SECTION_NAMES[section.type] ?? section.type}</p>
              <p className="eyebrow sm:text-right">
                {section.questionCount} question{section.questionCount === 1 ? "" : "s"} ·{" "}
                {formatDuration(section.durationMinutes)} · {Math.round(section.scoreWeight * 100)}% of score
              </p>
            </li>
          ))}
        </RuledList>
        {short ? (
          <p className="reading mt-5 max-w-[56ch]">
            This course has {availableQuestions} multiple-choice questions and {availableFrqs} free-response prompts
            available, fewer than the real exam, so the simulation uses all of them.
          </p>
        ) : null}
      </Section>

      <Section label="Start">
        <form action={startExamAction}>
          <Button type="submit" size="lg">
            Start exam
          </Button>
        </form>
        <p className="mt-3 max-w-[52ch] text-sm text-muted-foreground">
          You get an estimated AP score range at the end. It comes from multiple-choice accuracy only, so treat it as a
          rough guide.
        </p>
      </Section>
    </Page>
  );
}
