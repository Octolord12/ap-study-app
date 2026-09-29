import Link from "next/link";
import { requireAdminUserId } from "@/lib/admin/session";
import { listCoursesWithUnreviewedCounts } from "@/lib/admin/queries";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

export default async function AdminReviewIndexPage() {
  await requireAdminUserId();
  const courses = await listCoursesWithUnreviewedCounts();

  return (
    <div className="mx-auto w-full max-w-3xl px-6 py-10">
      <h1 className="mb-1 text-2xl font-bold tracking-tight">Content review</h1>
      <p className="mb-6 text-sm text-muted-foreground">
        Spot-check generated content before it reaches students. Everything below has{" "}
        <code className="rounded bg-muted px-1 py-0.5 text-xs">reviewed: false</code>.
      </p>
      <div className="grid gap-4 sm:grid-cols-2">
        {courses.map(({ course, questionCount, frqCount }) => (
          <Link key={course.id} href={`/admin/review/${course.slug}`}>
            <Card className="h-full transition-colors hover:border-foreground/30">
              <CardHeader>
                <CardTitle>{course.name}</CardTitle>
              </CardHeader>
              <CardContent>
                <p className="text-sm text-muted-foreground">
                  {questionCount} question{questionCount === 1 ? "" : "s"} · {frqCount} FRQ{frqCount === 1 ? "" : "s"}{" "}
                  pending
                </p>
              </CardContent>
            </Card>
          </Link>
        ))}
      </div>
    </div>
  );
}
