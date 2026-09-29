import Link from "next/link";
import { notFound } from "next/navigation";
import { requireUserId } from "@/lib/auth/session";
import { getClassDetail, getClassLeaderboard } from "@/lib/social/queries";
import { leaveClass } from "@/lib/social/actions";
import { LeaderboardTable } from "@/components/social/leaderboard-table";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

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
    <div className="mx-auto w-full max-w-2xl px-6 py-10">
      <p className="mb-1 text-sm text-muted-foreground">
        <Link href="/classes" className="hover:text-foreground">
          Classes
        </Link>
      </p>
      <div className="mb-6 flex items-start justify-between gap-4">
        <div>
          <h1 className="text-2xl font-bold tracking-tight">{classDetail.name}</h1>
          {classDetail.course ? <p className="text-sm text-muted-foreground">{classDetail.course.name}</p> : null}
        </div>
        {myMembership?.role !== "OWNER" ? (
          <form action={leaveClassAction}>
            <Button type="submit" variant="outline" size="sm">
              Leave class
            </Button>
          </form>
        ) : null}
      </div>

      <Card className="mb-8">
        <CardHeader>
          <CardTitle className="text-sm">Invite code</CardTitle>
        </CardHeader>
        <CardContent>
          <p className="font-mono text-2xl tracking-widest">{classDetail.inviteCode}</p>
          <p className="mt-1 text-xs text-muted-foreground">Share this so others can join at /classes</p>
        </CardContent>
      </Card>

      <h2 className="mb-3 text-sm font-semibold uppercase tracking-wide text-muted-foreground">Leaderboard</h2>
      <div className="mb-8">
        <LeaderboardTable entries={leaderboard} currentUserId={userId} period={period} basePath={`/classes/${classId}`} />
      </div>

      <h2 className="mb-3 text-sm font-semibold uppercase tracking-wide text-muted-foreground">
        Members ({classDetail.memberships.length})
      </h2>
      <ul className="divide-y divide-border rounded-lg border border-border">
        {classDetail.memberships.map((m) => (
          <li key={m.userId} className="flex items-center justify-between px-4 py-2 text-sm">
            <span>{m.user.username}</span>
            <span className="text-xs text-muted-foreground">{m.role === "OWNER" ? "Owner" : "Member"}</span>
          </li>
        ))}
      </ul>
    </div>
  );
}
