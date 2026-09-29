import Link from "next/link";
import { requireUserId } from "@/lib/auth/session";
import { getDb } from "@/lib/db";
import { listCourses } from "@/lib/study/queries";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

export default async function CoursesPage() {
  const userId = await requireUserId();

  const [courses, enrollments] = await Promise.all([
    listCourses(),
    getDb().enrollment.findMany({ where: { userId }, select: { courseId: true } }),
  ]);
  const enrolledCourseIds = new Set(enrollments.map((e) => e.courseId));

  return (
    <div className="mx-auto w-full max-w-3xl px-6 py-10">
      <h1 className="mb-6 text-2xl font-bold tracking-tight">Courses</h1>
      <div className="grid gap-4 sm:grid-cols-2">
        {courses.map((course) => (
          <Link key={course.id} href={`/courses/${course.slug}`}>
            <Card className="h-full transition-colors hover:border-foreground/30">
              <CardHeader>
                <CardTitle>{course.name}</CardTitle>
              </CardHeader>
              <CardContent>
                <p className="text-sm text-muted-foreground">{course.description}</p>
                {enrolledCourseIds.has(course.id) ? (
                  <p className="mt-3 text-xs font-medium text-primary">Enrolled</p>
                ) : null}
              </CardContent>
            </Card>
          </Link>
        ))}
      </div>
    </div>
  );
}
