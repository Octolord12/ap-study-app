import { notFound } from "next/navigation";
import { requireUserId } from "@/lib/auth/session";
import { getDb } from "@/lib/db";
import { startExam } from "@/lib/study/actions";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import type { Course as ContentCourse } from "@/lib/content/schema";

export default async function ExamIntroPage({ params }: { params: Promise<{ courseSlug: string }> }) {
  await requireUserId();
  const { courseSlug } = await params;

  const course = await getDb().course.findUnique({ where: { slug: courseSlug } });
  if (!course) notFound();

  const examFormat = course.examFormat as unknown as ContentCourse["examFormat"];
  const mcqSection = examFormat.sections.find((s) => s.type === "MCQ");
  const frqSection = examFormat.sections.find((s) => s.type === "FRQ");

  const [availableQuestions, availableFrqs] = await Promise.all([
    getDb().question.count({ where: { courseId: course.id } }),
    getDb().fRQPrompt.count({ where: { courseId: course.id } }),
  ]);

  const startExamAction = startExam.bind(null, course.id, course.slug);

  return (
    <div className="mx-auto w-full max-w-2xl px-6 py-10">
      <Card>
        <CardHeader>
          <CardTitle>Exam simulation</CardTitle>
        </CardHeader>
        <CardContent className="space-y-4">
          <p className="text-sm text-muted-foreground">
            The real {course.name} exam is {mcqSection?.questionCount ?? "?"} MCQ +{" "}
            {frqSection?.questionCount ?? "?"} FRQ in {examFormat.totalDurationMinutes} minutes, with no explanations
            until you&apos;re done.
          </p>
          {(availableQuestions < (mcqSection?.questionCount ?? 0) ||
            availableFrqs < (frqSection?.questionCount ?? 0)) && (
            <p className="rounded-lg bg-muted p-3 text-sm text-muted-foreground">
              This course&apos;s question bank is still small ({availableQuestions} MCQ, {availableFrqs} FRQ
              available) -- today&apos;s simulation will use everything available rather than the full count. More
              content lands in a later milestone.
            </p>
          )}
          <form action={startExamAction}>
            <Button type="submit" className="w-full">
              Start exam
            </Button>
          </form>
        </CardContent>
      </Card>
    </div>
  );
}
