import { getDb } from "@/lib/db";
import { computeLevel, type LevelProgress } from "@/lib/gamification/level";
import { BADGE_DEFINITIONS, type BadgeDefinition } from "@/lib/gamification/badges";
import { displayStreak, wasActiveToday } from "@/lib/gamification/streak";
import { sortUnitTitles, unitConquerorTitle, type UnitTitle } from "@/lib/gamification/titles";

export interface UserGamificationStats extends LevelProgress {
  totalXp: number;
  currentStreak: number;
  longestStreak: number;
  streakFreezesAvailable: number;
  studiedToday: boolean;
}

export async function getUserGamificationStats(userId: string): Promise<UserGamificationStats> {
  const db = getDb();

  const [user, xpResult] = await Promise.all([
    db.user.findUnique({
      where: { id: userId },
      select: { currentStreak: true, longestStreak: true, streakFreezesAvailable: true, lastActiveDate: true },
    }),
    db.xPEvent.aggregate({ where: { userId }, _sum: { amount: true } }),
  ]);

  const totalXp = xpResult._sum.amount ?? 0;
  const now = new Date();

  return {
    totalXp,
    ...computeLevel(totalXp),
    // Live value, not the stored one -- see displayStreak.
    currentStreak: user ? displayStreak(user, now) : 0,
    longestStreak: user?.longestStreak ?? 0,
    streakFreezesAvailable: user?.streakFreezesAvailable ?? 0,
    studiedToday: wasActiveToday(user?.lastActiveDate ?? null, now),
  };
}

export interface BadgeStatus extends BadgeDefinition {
  earned: boolean;
  earnedAt: Date | null;
}

// Every defined badge, earned or not -- the dashboard shows locked ones
// grayed out as a motivator, not just the ones already won.
export async function getAllBadgeStatuses(userId: string): Promise<BadgeStatus[]> {
  const earned = await getDb().userBadge.findMany({
    where: { userId },
    include: { badge: true },
  });
  const earnedBySlug = new Map(earned.map((e) => [e.badge.slug, e.earnedAt]));

  return BADGE_DEFINITIONS.map((def) => ({
    ...def,
    earned: earnedBySlug.has(def.slug),
    earnedAt: earnedBySlug.get(def.slug) ?? null,
  }));
}

export async function getUserUnitTitles(userId: string): Promise<UnitTitle[]> {
  const conquered = await getDb().bossBattleAttempt.findMany({
    where: { userId, passed: true },
    select: { unit: { select: { id: true, slug: true, name: true, order: true, course: { select: { slug: true, name: true } } } } },
  });

  return sortUnitTitles(
    conquered.map(({ unit }) => ({
      unitId: unit.id,
      unitSlug: unit.slug,
      unitName: unit.name,
      unitNumber: unit.order,
      courseSlug: unit.course.slug,
      courseName: unit.course.name,
      title: unitConquerorTitle(unit.order),
    })),
  );
}
