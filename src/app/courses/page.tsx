import type { Metadata } from "next";
import { requireUserId } from "@/lib/auth/session";
import { getDb } from "@/lib/db";
import { listCourses } from "@/lib/study/queries";
import { countWord } from "@/lib/count-word";
import { CourseRow } from "@/components/study/course-row";
import { Page, PageHeader, RuledList, Section } from "@/components/ui/page";

export const metadata: Metadata = { title: "Courses" };

export default async function CoursesPage() {
  const userId = await requireUserId();

  const [courses, enrollments] = await Promise.all([
    listCourses(),
    getDb().enrollment.findMany({ where: { userId }, select: { courseId: true } }),
  ]);
  const enrolledIds = new Set(enrollments.map((e) => e.courseId));
  const mine = courses.filter((c) => enrolledIds.has(c.id));
  const others = courses.filter((c) => !enrolledIds.has(c.id));

  const rows = (list: typeof courses) => (
    <RuledList>
      {list.map((course) => (
        <CourseRow
          key={course.id}
          slug={course.slug}
          name={course.name}
          description={course.description}
          examFormat={course.examFormat}
          enrolled={enrolledIds.has(course.id)}
        />
      ))}
    </RuledList>
  );

  return (
    <Page>
      <PageHeader eyebrow="Courses" title={`${countWord(courses.length, true)} exams. Pick one.`} description="Open a course to see its units, then practice by unit, by weak spot, or under exam conditions." />
      {mine.length > 0 ? <Section label="Your courses">{rows(mine)}</Section> : null}
      {others.length > 0 ? <Section label={mine.length > 0 ? "More courses" : "All courses"}>{rows(others)}</Section> : null}
    </Page>
  );
}
