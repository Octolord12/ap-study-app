import Link from "next/link";
import { notFound } from "next/navigation";
import { requireAdminUserId } from "@/lib/admin/session";
import { getUnitsWithUnreviewedCounts } from "@/lib/admin/queries";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

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
    <div className="mx-auto w-full max-w-3xl px-6 py-10">
      <p className="mb-1 text-sm text-muted-foreground">
        <Link href="/admin/review" className="hover:text-foreground">
          Content review
        </Link>
      </p>
      <h1 className="mb-6 text-2xl font-bold tracking-tight">{course.name}</h1>
      <div className="grid gap-3">
        {units.map((unit) => {
          const pending = unit._count.questions + unit._count.frqPrompts;
          return (
            <Link key={unit.id} href={`/admin/review/${course.slug}/${unit.slug}`}>
              <Card className={pending === 0 ? "opacity-50 transition-colors hover:border-foreground/30" : "transition-colors hover:border-foreground/30"}>
                <CardHeader>
                  <CardTitle className="text-base">{unit.name}</CardTitle>
                </CardHeader>
                <CardContent>
                  <p className="text-sm text-muted-foreground">
                    {pending === 0
                      ? "All reviewed"
                      : `${unit._count.questions} question${unit._count.questions === 1 ? "" : "s"} · ${unit._count.frqPrompts} FRQ${unit._count.frqPrompts === 1 ? "" : "s"} pending`}
                  </p>
                </CardContent>
              </Card>
            </Link>
          );
        })}
      </div>
    </div>
  );
}
