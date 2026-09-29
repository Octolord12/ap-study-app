import { getDb } from "@/lib/db";
import { rankLeaderboard, type LeaderboardEntry } from "@/lib/social/leaderboard";

const WEEK_MS = 7 * 24 * 60 * 60 * 1000;

// "Weekly" is a rolling 7-day window ending now, not a calendar week -- avoids
// timezone/week-start ambiguity for a one-family app at this scale.
async function computeLeaderboard(userIds: string[], period: "week" | "all"): Promise<LeaderboardEntry[]> {
  if (userIds.length === 0) return [];
  const db = getDb();
  const since = period === "week" ? new Date(Date.now() - WEEK_MS) : undefined;

  const [users, xpSums] = await Promise.all([
    db.user.findMany({
      where: { id: { in: userIds } },
      select: { id: true, username: true, leaderboardOptOut: true },
    }),
    db.xPEvent.groupBy({
      by: ["userId"],
      where: { userId: { in: userIds }, ...(since ? { createdAt: { gte: since } } : {}) },
      _sum: { amount: true },
    }),
  ]);

  const xpByUser = new Map(xpSums.map((x) => [x.userId, x._sum.amount ?? 0]));

  return rankLeaderboard(
    users.map((u) => ({
      userId: u.id,
      username: u.username,
      totalXp: xpByUser.get(u.id) ?? 0,
      optedOut: u.leaderboardOptOut,
    })),
  );
}

export async function getFriendUserIds(userId: string): Promise<string[]> {
  const friendships = await getDb().friendship.findMany({
    where: { status: "ACCEPTED", OR: [{ requesterId: userId }, { addresseeId: userId }] },
  });
  return friendships.map((f) => (f.requesterId === userId ? f.addresseeId : f.requesterId));
}

export async function getFriendsLeaderboard(userId: string, period: "week" | "all"): Promise<LeaderboardEntry[]> {
  const friendIds = await getFriendUserIds(userId);
  return computeLeaderboard([userId, ...friendIds], period);
}

export async function getClassLeaderboard(classId: string, period: "week" | "all"): Promise<LeaderboardEntry[]> {
  const memberships = await getDb().classMembership.findMany({ where: { classId }, select: { userId: true } });
  return computeLeaderboard(
    memberships.map((m) => m.userId),
    period,
  );
}

export async function getPendingFriendRequests(userId: string) {
  const db = getDb();
  const [incoming, outgoing] = await Promise.all([
    db.friendship.findMany({
      where: { addresseeId: userId, status: "PENDING" },
      include: { requester: { select: { id: true, username: true, displayName: true } } },
    }),
    db.friendship.findMany({
      where: { requesterId: userId, status: "PENDING" },
      include: { addressee: { select: { id: true, username: true, displayName: true } } },
    }),
  ]);
  return { incoming, outgoing };
}

export async function getFriendsList(userId: string) {
  const db = getDb();
  const friendships = await db.friendship.findMany({
    where: { status: "ACCEPTED", OR: [{ requesterId: userId }, { addresseeId: userId }] },
    include: {
      requester: { select: { id: true, username: true, displayName: true } },
      addressee: { select: { id: true, username: true, displayName: true } },
    },
  });
  return friendships.map((f) => (f.requesterId === userId ? f.addressee : f.requester));
}

export async function getMyClasses(userId: string) {
  const memberships = await getDb().classMembership.findMany({
    where: { userId },
    include: { class: { include: { course: true, _count: { select: { memberships: true } } } } },
  });
  return memberships.map((m) => ({ ...m.class, myRole: m.role }));
}

export async function getClassDetail(classId: string) {
  return getDb().class.findUnique({
    where: { id: classId },
    include: {
      course: true,
      memberships: {
        include: { user: { select: { id: true, username: true, displayName: true } } },
        orderBy: { joinedAt: "asc" },
      },
    },
  });
}
