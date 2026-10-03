import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { requireAdminUserId } from "@/lib/admin/session";
import { getUnitsWithUnreviewedCounts } from "@/lib/admin/queries";
import { Breadcrumb, Page, PageHeader, RuledList, Section } from "@/components/ui/page";
import { cn } from "cn";

export const metadata: Metadata = { title: "Content review" };

export default async function AdminReviewCoursePage({
  params,
}: {
  params: Promise<{ courseSlug: string }>;
}) {
  await requireAdminUserId();
  const { courseSlug } = await params;

  const result = await getUnitsWithUnreviewedCounts(courseSlug);
  if (!result) notFound();
  const { course, units } = result;

  return (
    <Page>
      <PageHeader eyebrow={<Breadcrumb items={[{ label: "Content review", href: "/admin/review" }, { label: course.name }]} />} title={course.name} />
      <Section label="Units">
        <RuledList>
          {units.map((unit) => {
            const pending = unit._count.questions + unit._count.frqPrompts;
            return (
              <li key={unit.id}>
                <Link
                  href={`/admin/review/${course.slug}/${unit.slug}`}
                  className={cn("group flex flex-wrap items-baseline justify-between gap-x-6 gap-y-1 py-4", pending === 0 && "opacity-50")}
                >
                  <span className="heading text-xl underline-offset-4 decoration-2 group-hover:underline">{unit.name}</span>
                  <span className="eyebrow">
                    {pending === 0
                      ? "All reviewed"
                      : `${unit._count.questions} question${unit._count.questions === 1 ? "" : "s"} · ${unit._count.frqPrompts} FRQ${unit._count.frqPrompts === 1 ? "" : "s"} pending`}
                  </span>
                </Link>
              </li>
            );
          })}
        </RuledList>
      </Section>
    </Page>
  );
}
