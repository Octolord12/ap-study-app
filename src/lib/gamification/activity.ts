import { getDb } from "@/lib/db";
import { computeLevel } from "@/lib/gamification/level";
import { updateStreakOnActivity } from "@/lib/gamification/streak";
import type { PrismaClient } from "@/generated/prisma/client";

export interface CorrectAnswerResult {
  xpAwarded: number;
  leveledUp: boolean;
  newLevel: number;
  currentStreak: number;
  freezeUsed: boolean;
}

function startOfDay(date: Date): Date {
  const d = new Date(date);
  d.setHours(0, 0, 0, 0);
  return d;
}

async function getTotalXp(db: PrismaClient, userId: string): Promise<number> {
  const result = await db.xPEvent.aggregate({ where: { userId }, _sum: { amount: true } });
  return result._sum.amount ?? 0;
}

// Called once per scoring event worth XP (a correct MCQ, or an FRQ that
// earned at least one rubric point) -- badge checking is a separate,
// always-run step (see checkAndAwardBadges) since some badges (e.g.
// "answered your first question") shouldn't require being right.
//
// xpFormula is a callback rather than a plain number because the streak
// bonus depends on the CURRENT streak, which this function only knows after
// it updates it -- MCQ and FRQ scoring use different base-XP formulas (see
// xpForCorrectAnswer / xpForFrqPoints in ./xp.ts) but share this bookkeeping.
export async function grantXpForActivity(userId: string, xpFormula: (currentStreak: number) => number): Promise<CorrectAnswerResult> {
  const db = getDb();
  const now = new Date();

  const user = await db.user.findUniqueOrThrow({
    where: { id: userId },
    select: { currentStreak: true, longestStreak: true, lastActiveDate: true, streakFreezesAvailable: true },
  });

  const alreadyActiveToday = user.lastActiveDate
    ? startOfDay(user.lastActiveDate).getTime() === startOfDay(now).getTime()
    : false;

  let currentStreak = user.currentStreak;
  let freezeUsed = false;

  if (!alreadyActiveToday) {
    const streakUpdate = updateStreakOnActivity(user, now);
    currentStreak = streakUpdate.currentStreak;
    freezeUsed = streakUpdate.freezeUsed;
    await db.user.update({
      where: { id: userId },
      data: {
        currentStreak: streakUpdate.currentStreak,
        longestStreak: streakUpdate.longestStreak,
        lastActiveDate: streakUpdate.lastActiveDate,
        streakFreezesAvailable: streakUpdate.streakFreezesAvailable,
      },
    });
  }

  const totalXpBefore = await getTotalXp(db, userId);
  const levelBefore = computeLevel(totalXpBefore).level;

  const xpAwarded = xpFormula(currentStreak);
  await db.xPEvent.create({ data: { userId, amount: xpAwarded, reason: "question_correct" } });

  const levelAfter = computeLevel(totalXpBefore + xpAwarded).level;

  return {
    xpAwarded,
    leveledUp: levelAfter > levelBefore,
    newLevel: levelAfter,
    currentStreak,
    freezeUsed,
  };
}
