import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { requireUserId } from "@/lib/auth/session";
import { getClassDetail, getClassLeaderboard } from "@/lib/social/queries";
import { leaveClass } from "@/lib/social/actions";
import { Ledger } from "@/components/ui/ledger";
import { Button } from "@/components/ui/button";
import { Breadcrumb, Page, PageHeader, RuledList, Section } from "@/components/ui/page";

export const metadata: Metadata = { title: "Class" };

export default async function ClassDetailPage({
  params,
  searchParams,
}: {
  params: Promise<{ classId: string }>;
  searchParams: Promise<{ period?: string }>;
}) {
  const userId = await requireUserId();
  const { classId } = await params;
  const { period: periodParam } = await searchParams;
  const period = periodParam === "all" ? "all" : "week";

  const classDetail = await getClassDetail(classId);
  if (!classDetail) notFound();

  const isMember = classDetail.memberships.some((m) => m.userId === userId);
  if (!isMember) notFound();

  const myMembership = classDetail.memberships.find((m) => m.userId === userId);
  const leaderboard = await getClassLeaderboard(classId, period);
  const leaveClassAction = leaveClass.bind(null, classId);

  return (
    <Page>
      <PageHeader
        eyebrow={<Breadcrumb items={[{ label: "Classes", href: "/classes" }, { label: "Class" }]} />}
        title={classDetail.name}
        description={classDetail.course?.name}
        actions={
          myMembership?.role !== "OWNER" ? (
            <form action={leaveClassAction}>
              <Button type="submit" variant="outline">
                Leave class
              </Button>
            </form>
          ) : (
            <Button render={<Link href={`/teacher?class=${classId}`} />} nativeButton={false} variant="outline">
              Teacher view
            </Button>
          )
        }
      />

      <Section label="Invite code" note="Share it so others can join from the Classes page.">
        <p className="font-mono text-4xl tracking-[0.25em]">{classDetail.inviteCode}</p>
      </Section>

      <Section label="Leaderboard">
        <Ledger entries={leaderboard} currentUserId={userId} period={period} basePath={`/classes/${classId}`} />
      </Section>

      <Section label={`Members (${classDetail.memberships.length})`}>
        <RuledList>
          {classDetail.memberships.map((m) => (
            <li key={m.userId} className="flex items-baseline justify-between gap-3 py-3">
              <span className="font-mono text-sm">{m.user.username}</span>
              <span className="eyebrow">{m.role === "OWNER" ? "Owner" : "Member"}</span>
            </li>
          ))}
        </RuledList>
      </Section>
    </Page>
  );
}
