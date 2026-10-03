import type { Metadata } from "next";
import Link from "next/link";
import { requireAdminUserId } from "@/lib/admin/session";
import { listCoursesWithUnreviewedCounts } from "@/lib/admin/queries";
import { Page, PageHeader, RuledList, Section } from "@/components/ui/page";

export const metadata: Metadata = { title: "Content review" };

export default async function AdminReviewIndexPage() {
  await requireAdminUserId();
  const courses = await listCoursesWithUnreviewedCounts();

  return (
    <Page>
      <PageHeader
        eyebrow="Admin"
        title="Content review"
        description="Spot-check generated content before it reaches students. Everything listed is still marked reviewed: false."
      />
      <Section label="Courses">
        <RuledList>
          {courses.map(({ course, questionCount, frqCount }) => (
            <li key={course.id}>
              <Link href={`/admin/review/${course.slug}`} className="group flex flex-wrap items-baseline justify-between gap-x-6 gap-y-1 py-4">
                <span className="heading text-xl underline-offset-4 decoration-2 group-hover:underline">{course.name}</span>
                <span className="eyebrow">
                  {questionCount} question{questionCount === 1 ? "" : "s"} · {frqCount} FRQ{frqCount === 1 ? "" : "s"} pending
                </span>
              </Link>
            </li>
          ))}
        </RuledList>
      </Section>
    </Page>
  );
}
