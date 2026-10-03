import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { requireUserId } from "@/lib/auth/session";
import { renderQuizQuestions } from "@/lib/study/render-quiz";
import { QuizRunner } from "@/components/study/quiz-runner";
import { Page } from "@/components/ui/page";
import { isPaperLinedCourse } from "@/lib/content/paper-lined";
import type { AttemptSource } from "@/generated/prisma/client";

export const metadata: Metadata = { title: "Quiz" };

const VALID_SOURCES: AttemptSource[] = ["PRACTICE", "QUIZ", "DAILY", "WEAK_SPOT"];

// Generic quiz entry point for anything that isn't unit-scoped browsing:
// custom quizzes, weak-spot review, and the daily challenge. Unit practice
// has its own route (units/[unitSlug]/quiz) so it can link "back to unit".
export default async function CourseQuizPage({
  params,
  searchParams,
}: {
  params: Promise<{ courseSlug: string }>;
  searchParams: Promise<{ ids?: string; source?: string; back?: string; backLabel?: string }>;
}) {
  await requireUserId();
  const { courseSlug } = await params;
  const { ids, source, back, backLabel } = await searchParams;

  const questionIds = (ids ?? "").split(",").filter(Boolean);
  if (questionIds.length === 0) notFound();

  const rendered = await renderQuizQuestions(questionIds, courseSlug);
  if (rendered.length === 0) notFound();

  const attemptSource = VALID_SOURCES.includes(source as AttemptSource) ? (source as AttemptSource) : "PRACTICE";
  // Only ever used as an href on our own <Link>, never for a server redirect,
  // but still restricted to same-origin relative paths defensively.
  const backHref = back && back.startsWith("/") ? back : `/courses/${courseSlug}`;

  return (
    <Page>
      <QuizRunner
        questions={rendered}
        backHref={backHref}
        backLabel={backLabel || "Back to course"}
        source={attemptSource}
        paperLined={isPaperLinedCourse(courseSlug)}
      />
    </Page>
  );
}
