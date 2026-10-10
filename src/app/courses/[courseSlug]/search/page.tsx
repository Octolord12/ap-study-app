import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { requireUserId } from "@/lib/auth/session";
import { getDb } from "@/lib/db";
import { normalizeSearchQuery, searchRefreshers } from "@/lib/study/refresher-search";
import { RefresherSearchForm } from "@/components/study/refresher-search-form";
import { RefresherSearchResults } from "@/components/study/refresher-search-results";
import { Breadcrumb, Page, PageHeader, Section } from "@/components/ui/page";

export const metadata: Metadata = { title: "Search refreshers" };

export default async function RefresherSearchPage({
  params,
  searchParams,
}: {
  params: Promise<{ courseSlug: string }>;
  searchParams: Promise<{ q?: string | string[] }>;
}) {
  await requireUserId();
  const { courseSlug } = await params;
  const { q: rawQuery } = await searchParams;

  const course = await getDb().course.findUnique({ where: { slug: courseSlug }, select: { slug: true, name: true } });
  if (!course) notFound();

  const query = normalizeSearchQuery(rawQuery);
  const hits = query ? await searchRefreshers(course.slug, query) : null;

  return (
    <Page>
      <PageHeader
        eyebrow={<Breadcrumb items={[{ label: "Courses", href: "/courses" }, { label: course.name, href: `/courses/${course.slug}` }, { label: "Search" }]} />}
        title="Search refreshers"
        description={`Find a topic or a term in ${course.name}.`}
      />
      <Section label="Search">
        <RefresherSearchForm courseSlug={course.slug} query={query ?? undefined} />
      </Section>
      <Section label="Results">
        <RefresherSearchResults courseSlug={course.slug} query={query} hits={hits} />
      </Section>
    </Page>
  );
}
