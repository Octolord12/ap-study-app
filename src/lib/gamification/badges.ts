import { getDb } from "@/lib/db";
import { computeUnitMastery } from "@/lib/study/mastery";
import type { PrismaClient } from "@/generated/prisma/client";

export interface BadgeDefinition {
  slug: string;
  name: string;
  description: string;
  icon: string;
}

export const BADGE_DEFINITIONS: BadgeDefinition[] = [
  { slug: "first_quiz", name: "First Steps", description: "Answer your first question", icon: "🎯" },
  { slug: "streak_7", name: "On Fire", description: "Reach a 7-day streak", icon: "🔥" },
  { slug: "unit_mastery", name: "Unit Master", description: "Get every attempted question in a unit correct", icon: "🏅" },
  { slug: "perfect_ten", name: "Perfect Ten", description: "Answer 10 questions correctly in a row", icon: "⭐" },
  { slug: "exam_finisher", name: "Exam Ready", description: "Complete a full exam simulation", icon: "📝" },
  { slug: "boss_slayer", name: "Boss Slayer", description: "Defeat a unit boss battle", icon: "⚔️" },
];

export async function ensureBadgesSeeded(): Promise<void> {
  const db = getDb();
  for (const badge of BADGE_DEFINITIONS) {
    await db.badge.upsert({
      where: { slug: badge.slug },
      create: badge,
      update: { name: badge.name, description: badge.description, icon: badge.icon },
    });
  }
}

async function meetsCriteria(db: PrismaClient, userId: string, slug: string): Promise<boolean> {
  switch (slug) {
    case "first_quiz": {
      const count = await db.questionAttempt.count({ where: { userId } });
      return count >= 1;
    }
    case "streak_7": {
      const user = await db.user.findUnique({ where: { id: userId }, select: { currentStreak: true } });
      return (user?.currentStreak ?? 0) >= 7;
    }
    case "perfect_ten": {
      const recent = await db.questionAttempt.findMany({
        where: { userId },
        orderBy: { createdAt: "desc" },
        take: 10,
        select: { correct: true },
      });
      return recent.length === 10 && recent.every((a) => a.correct);
    }
    case "exam_finisher": {
      const count = await db.examAttempt.count({ where: { userId, completedAt: { not: null } } });
      return count >= 1;
    }
    case "boss_slayer": {
      const count = await db.bossBattleAttempt.count({ where: { userId, passed: true } });
      return count >= 1;
    }
    case "unit_mastery":
      return hasAnyMasteredUnit(db, userId);
    default:
      return false;
  }
}

async function hasAnyMasteredUnit(db: PrismaClient, userId: string): Promise<boolean> {
  const attempts = await db.questionAttempt.findMany({
    where: { userId },
    select: { questionId: true, correct: true, createdAt: true, question: { select: { unitId: true } } },
  });
  const mastery = computeUnitMastery(
    attempts.map((a) => ({
      questionId: a.questionId,
      unitId: a.question.unitId,
      correct: a.correct,
      createdAt: a.createdAt,
    })),
  );

  const units = await db.unit.findMany({ select: { id: true, _count: { select: { questions: true } } } });
  const totalByUnit = new Map(units.map((u) => [u.id, u._count.questions]));

  return mastery.some((m) => {
    const total = totalByUnit.get(m.unitId) ?? 0;
    return total > 0 && m.questionsAttempted >= total && m.questionsCorrect === m.questionsAttempted;
  });
}

// Checks every not-yet-earned badge's criteria for this user and awards any
// newly met ones. Small, indexed queries -- cheap enough to call after every
// scoring action rather than needing a more elaborate event-driven system.
export async function checkAndAwardBadges(userId: string): Promise<BadgeDefinition[]> {
  const db = getDb();

  const alreadyEarned = await db.userBadge.findMany({
    where: { userId },
    select: { badge: { select: { slug: true } } },
  });
  const earnedSlugs = new Set(alreadyEarned.map((u) => u.badge.slug));
  const toCheck = BADGE_DEFINITIONS.filter((b) => !earnedSlugs.has(b.slug));
  if (toCheck.length === 0) return [];

  const newlyEarnedSlugs: string[] = [];
  for (const badge of toCheck) {
    if (await meetsCriteria(db, userId, badge.slug)) newlyEarnedSlugs.push(badge.slug);
  }
  if (newlyEarnedSlugs.length === 0) return [];

  await ensureBadgesSeeded();
  const badgeRows = await db.badge.findMany({ where: { slug: { in: newlyEarnedSlugs } } });
  await db.userBadge.createMany({
    data: badgeRows.map((b) => ({ userId, badgeId: b.id })),
    skipDuplicates: true,
  });

  return BADGE_DEFINITIONS.filter((b) => newlyEarnedSlugs.includes(b.slug));
}
