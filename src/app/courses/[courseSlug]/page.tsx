import Link from "next/link";
import { notFound } from "next/navigation";
import { requireUserId } from "@/lib/auth/session";
import { getDb } from "@/lib/db";
import { getCourseTree } from "@/lib/study/queries";
import { enrollInCourse } from "@/lib/study/actions";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

export default async function CoursePage({ params }: { params: Promise<{ courseSlug: string }> }) {
  const { courseSlug } = await params;
  const userId = await requireUserId();

  const course = await getCourseTree(courseSlug);
  if (!course) notFound();

  const enrollment = await getDb().enrollment.findUnique({
    where: { userId_courseId: { userId, courseId: course.id } },
  });

  const enrollAction = enrollInCourse.bind(null, course.id);

  return (
    <div className="mx-auto w-full max-w-3xl px-6 py-10">
      <div className="mb-6 flex items-start justify-between gap-4">
        <div>
          <h1 className="text-2xl font-bold tracking-tight">{course.name}</h1>
          <p className="mt-1 text-sm text-muted-foreground">{course.description}</p>
        </div>
        <div className="flex shrink-0 gap-2">
          {enrollment ? (
            <Button render={<Link href={`/courses/${course.slug}/practice`} />} nativeButton={false} variant="outline">
              Practice
            </Button>
          ) : (
            <form action={enrollAction}>
              <Button type="submit">Start studying</Button>
            </form>
          )}
        </div>
      </div>

      <h2 className="mb-3 text-sm font-semibold uppercase tracking-wide text-muted-foreground">Units</h2>
      <div className="space-y-3">
        {course.units.map((unit) => (
          <Link key={unit.id} href={`/courses/${course.slug}/units/${unit.slug}`}>
            <Card className="transition-colors hover:border-foreground/30">
              <CardHeader>
                <CardTitle className="text-base">{unit.name}</CardTitle>
              </CardHeader>
              <CardContent>
                <p className="text-xs text-muted-foreground">
                  {unit.weightingMin}–{unit.weightingMax}% of exam · {unit.topics.length} topics
                </p>
              </CardContent>
            </Card>
          </Link>
        ))}
      </div>
    </div>
  );
}
