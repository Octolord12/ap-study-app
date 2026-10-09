import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { requireUserId } from "@/lib/auth/session";
import { getClassDetail, getClassLeaderboard } from "@/lib/social/queries";
import { leaveClass, regenerateInviteCode, removeClassMember, renameClass } from "@/lib/social/actions";
import { CLASS_NAME_MAX } from "@/lib/social/class-name";
import { RegenerateInviteCodeButton } from "@/components/social/regenerate-invite-code-button";
import { RemoveClassMemberButton } from "@/components/social/remove-class-member-button";
import { Ledger } from "@/components/ui/ledger";
import { Button } from "@/components/ui/button";
import { Field } from "@/components/ui/field";
import { Input } from "@/components/ui/input";
import { Breadcrumb, Page, PageHeader, RuledList, Section } from "@/components/ui/page";

export const metadata: Metadata = { title: "Class" };

export default async function ClassDetailPage({
  params,
  searchParams,
}: {
  params: Promise<{ classId: string }>;
  searchParams: Promise<{ period?: string; error?: string }>;
}) {
  const userId = await requireUserId();
  const { classId } = await params;
  const { period: periodParam, error } = await searchParams;
  const period = periodParam === "all" ? "all" : "week";

  const classDetail = await getClassDetail(classId);
  if (!classDetail) notFound();

  const isMember = classDetail.memberships.some((m) => m.userId === userId);
  if (!isMember) notFound();

  const myMembership = classDetail.memberships.find((m) => m.userId === userId);
  const leaderboard = await getClassLeaderboard(classId, period);
  const leaveClassAction = leaveClass.bind(null, classId);
  const isOwner = myMembership?.role === "OWNER";
  const renameClassAction = renameClass.bind(null, classId);
  const regenerateInviteCodeAction = regenerateInviteCode.bind(null, classId);

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
        {isOwner ? (
          <div className="mt-4">
            <RegenerateInviteCodeButton action={regenerateInviteCodeAction} />
          </div>
        ) : null}
      </Section>

      <Section label="Leaderboard">
        <Ledger entries={leaderboard} currentUserId={userId} period={period} basePath={`/classes/${classId}`} />
      </Section>

      <Section label={`Members (${classDetail.memberships.length})`}>
        <RuledList>
          {classDetail.memberships.map((m) => (
            <li key={m.userId} className="flex flex-wrap items-center justify-between gap-3 py-3">
              <span className="font-mono text-sm">{m.user.username}</span>
              <div className="flex items-center gap-3">
                <span className="eyebrow">{m.role === "OWNER" ? "Owner" : "Member"}</span>
                {isOwner && m.role === "MEMBER" ? (
                  <RemoveClassMemberButton username={m.user.username} action={removeClassMember.bind(null, classId, m.userId)} />
                ) : null}
              </div>
            </li>
          ))}
        </RuledList>
      </Section>

      {isOwner ? (
        <Section label="Rename" note="Everyone in the class sees the new name.">
          <form action={renameClassAction} className="flex max-w-md flex-wrap items-end gap-3">
            <Field id="name" label="Class name" className="min-w-48 flex-1">
              <Input id="name" name="name" key={classDetail.name} defaultValue={classDetail.name} required maxLength={CLASS_NAME_MAX} autoComplete="off" />
            </Field>
            <Button type="submit" size="lg">
              Save name
            </Button>
          </form>
          {error === "name" ? (
            <p role="alert" className="mt-3 text-sm font-medium text-incorrect">
              Enter a name of 1 to {CLASS_NAME_MAX} characters.
            </p>
          ) : null}
        </Section>
      ) : null}
    </Page>
  );
}
