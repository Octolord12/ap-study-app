"use server";

import { revalidatePath } from "next/cache";
import { redirect } from "next/navigation";
import { auth } from "@/lib/auth/config";
import { getDb } from "@/lib/db";
import { computeNextReview } from "@/lib/study/spaced-repetition";
import { pickQuestionIdsForCustomQuiz } from "@/lib/study/queries";
import { estimateApScoreRange } from "@/lib/study/exam-scoring";
import { SelfGradingStrategy, type RubricLine } from "@/lib/scoring/grading";
import { grantXpForActivity } from "@/lib/gamification/activity";
import { xpForCorrectAnswer, xpForFrqPoints } from "@/lib/gamification/xp";
import { checkAndAwardBadges, type BadgeDefinition } from "@/lib/gamification/badges";
import { unitConquerorTitle } from "@/lib/gamification/titles";
import { hasPassedBossBattle, scoreBossBattle } from "@/lib/study/boss-battle-rules";
import { bossBattleSecret, verifyBossBattle } from "@/lib/study/boss-battle-token";
import type { AttemptSource, Difficulty } from "@/generated/prisma/client";
import type { Course as ContentCourse } from "@/lib/content/schema";

function shuffle<T>(items: T[]): T[] {
  return [...items].sort(() => Math.random() - 0.5);
}

async function requireUserId(): Promise<string> {
  const session = await auth();
  if (!session?.user?.id) throw new Error("Not authenticated");
  return session.user.id;
}

export async function enrollInCourse(courseId: string) {
  const userId = await requireUserId();
  await getDb().enrollment.upsert({
    where: { userId_courseId: { userId, courseId } },
    create: { userId, courseId },
    update: {},
  });
  revalidatePath("/dashboard");
}

export async function toggleBookmark(questionId: string): Promise<{ bookmarked: boolean }> {
  const userId = await requireUserId();
  const db = getDb();

  const existing = await db.bookmark.findUnique({ where: { userId_questionId: { userId, questionId } } });
  if (existing) {
    await db.bookmark.delete({ where: { userId_questionId: { userId, questionId } } });
    return { bookmarked: false };
  }

  await db.bookmark.create({ data: { userId, questionId } });
  return { bookmarked: true };
}

interface RecordAttemptInput {
  questionId: string;
  chosenLabel: string;
  timeSpentMs: number;
  source?: AttemptSource;
}

export interface RecordAttemptResult {
  correct: boolean;
  xpAwarded: number;
  leveledUp: boolean;
  newLevel: number;
  currentStreak: number;
  newBadges: BadgeDefinition[];
}

// Correctness is always looked up fresh from the DB here, never taken from the
// client -- the client already knows the answer (it renders the explanation),
// but the persisted attempt log has to be trustworthy regardless of what the
// client claims. XP/streak/badges follow the same rule: computed here, from
// what was just looked up, never from anything the client sent.
export async function recordAttempt(input: RecordAttemptInput): Promise<RecordAttemptResult> {
  const userId = await requireUserId();
  const db = getDb();

  const question = await db.question.findUnique({
    where: { id: input.questionId },
    include: { choices: true },
  });
  if (!question) throw new Error("Question not found");

  const chosenChoice = question.choices.find((c) => c.label === input.chosenLabel);
  const correct = chosenChoice?.isCorrect ?? false;

  await db.questionAttempt.create({
    data: {
      userId,
      questionId: input.questionId,
      chosenLabel: input.chosenLabel,
      correct,
      timeSpentMs: input.timeSpentMs,
      source: input.source ?? "PRACTICE",
    },
  });

  const existingReviewState = await db.spacedRepetitionState.findUnique({
    where: { userId_questionId: { userId, questionId: input.questionId } },
  });
  const nextReview = computeNextReview(
    existingReviewState ?? { easeFactor: 2.5, intervalDays: 1, lapses: 0 },
    correct,
  );
  await db.spacedRepetitionState.upsert({
    where: { userId_questionId: { userId, questionId: input.questionId } },
    create: { userId, questionId: input.questionId, ...nextReview },
    update: nextReview,
  });

  const xpResult = correct
    ? await grantXpForActivity(userId, (streak) => xpForCorrectAnswer(question.difficulty, streak))
    : null;
  const newBadges = await checkAndAwardBadges(userId);

  revalidatePath("/dashboard");
  return {
    correct,
    xpAwarded: xpResult?.xpAwarded ?? 0,
    leveledUp: xpResult?.leveledUp ?? false,
    newLevel: xpResult?.newLevel ?? 0,
    currentStreak: xpResult?.currentStreak ?? 0,
    newBadges,
  };
}

const VALID_DIFFICULTIES: Difficulty[] = ["EASY", "MEDIUM", "HARD"];

export async function startCustomQuiz(formData: FormData): Promise<void> {
  await requireUserId();

  const courseId = formData.get("courseId") as string;
  const courseSlug = formData.get("courseSlug") as string;
  const unitIds = formData.getAll("unitId") as string[];
  const difficultyRaw = formData.get("difficulty");
  const difficulty = VALID_DIFFICULTIES.includes(difficultyRaw as Difficulty) ? (difficultyRaw as Difficulty) : undefined;
  const length = Math.max(1, Math.min(50, Number(formData.get("length")) || 10));

  if (unitIds.length === 0) {
    redirect(`/courses/${courseSlug}/practice/custom?error=no-units`);
  }

  const ids = await pickQuestionIdsForCustomQuiz({ courseId, unitIds, difficulty, length });
  if (ids.length === 0) {
    redirect(`/courses/${courseSlug}/practice/custom?error=no-matches`);
  }

  const params = new URLSearchParams({
    ids: ids.join(","),
    source: "QUIZ",
    back: `/courses/${courseSlug}/practice`,
    backLabel: "Back to practice",
  });
  redirect(`/courses/${courseSlug}/quiz?${params.toString()}`);
}

interface FrqGradeResult {
  pointsAwarded: number;
  maxPoints: number;
  xpAwarded: number;
  leveledUp: boolean;
  newLevel: number;
  newBadges: BadgeDefinition[];
}

// A zero-credit response earns no XP/streak/badge credit -- otherwise
// submitting blank responses would be a free way to farm all three.
async function grantFrqXpIfEarned(userId: string, pointsAwarded: number) {
  if (pointsAwarded <= 0) return { xpAwarded: 0, leveledUp: false, newLevel: 0 };
  return grantXpForActivity(userId, (streak) => xpForFrqPoints(pointsAwarded, streak));
}

// Standalone FRQ practice: response and self-grade happen in one sitting, so
// this creates the attempt already graded.
export async function submitFrqAttempt(input: {
  frqPromptId: string;
  responseText: string;
  checkedLineIds: string[];
}): Promise<FrqGradeResult> {
  const userId = await requireUserId();
  const db = getDb();

  const frq = await db.fRQPrompt.findUnique({ where: { id: input.frqPromptId } });
  if (!frq) throw new Error("FRQ not found");

  const rubric = frq.rubric as unknown as RubricLine[];
  const result = await new SelfGradingStrategy().grade(
    { responseText: input.responseText, rubric, maxPoints: frq.pointValue },
    { checkedLineIds: input.checkedLineIds },
  );

  await db.fRQAttempt.create({
    data: {
      userId,
      frqPromptId: input.frqPromptId,
      responseText: input.responseText,
      selfGradedPoints: result.pointsAwarded,
    },
  });

  const xpResult = await grantFrqXpIfEarned(userId, result.pointsAwarded);
  const newBadges = await checkAndAwardBadges(userId);

  revalidatePath("/dashboard");
  return { pointsAwarded: result.pointsAwarded, maxPoints: result.maxPoints, ...xpResult, newBadges };
}

// Exam flow: the response was already written and saved (ungraded) when the
// exam was submitted, since self-grading happens afterward, against the
// rubric the student couldn't see mid-exam. This just (re-)grades it.
export async function updateFrqGrade(input: {
  frqAttemptId: string;
  checkedLineIds: string[];
}): Promise<FrqGradeResult> {
  const userId = await requireUserId();
  const db = getDb();

  const attempt = await db.fRQAttempt.findUnique({
    where: { id: input.frqAttemptId },
    include: { frq: true },
  });
  if (!attempt || attempt.userId !== userId) throw new Error("FRQ attempt not found");

  const rubric = attempt.frq.rubric as unknown as RubricLine[];
  const result = await new SelfGradingStrategy().grade(
    { responseText: attempt.responseText, rubric, maxPoints: attempt.frq.pointValue },
    { checkedLineIds: input.checkedLineIds },
  );

  await db.fRQAttempt.update({
    where: { id: input.frqAttemptId },
    data: { selfGradedPoints: result.pointsAwarded },
  });

  // Only award XP the first time this attempt goes from ungraded to graded --
  // revisiting the results page and re-saving a grade shouldn't re-farm XP.
  const alreadyGraded = attempt.selfGradedPoints > 0;
  const xpResult = alreadyGraded ? { xpAwarded: 0, leveledUp: false, newLevel: 0 } : await grantFrqXpIfEarned(userId, result.pointsAwarded);
  const newBadges = await checkAndAwardBadges(userId);

  revalidatePath("/dashboard");
  return { pointsAwarded: result.pointsAwarded, maxPoints: result.maxPoints, ...xpResult, newBadges };
}

export async function startExam(courseId: string, courseSlug: string): Promise<void> {
  const userId = await requireUserId();
  const db = getDb();

  const course = await db.course.findUnique({ where: { id: courseId } });
  if (!course) throw new Error("Course not found");

  const examFormat = course.examFormat as unknown as ContentCourse["examFormat"];
  const mcqTarget = examFormat.sections.find((s) => s.type === "MCQ")?.questionCount;
  const frqTarget = examFormat.sections.find((s) => s.type === "FRQ")?.questionCount;

  const [availableQuestions, availableFrqs] = await Promise.all([
    db.question.findMany({ where: { courseId }, select: { id: true } }),
    db.fRQPrompt.findMany({ where: { courseId }, select: { id: true } }),
  ]);

  // We rarely have anywhere near the real exam's question count yet (content
  // is seeded incrementally, full banks are Milestone 7) -- use whatever's
  // available rather than failing, and say so on the intro screen.
  const questionIds = shuffle(availableQuestions.map((q) => q.id)).slice(0, mcqTarget ?? availableQuestions.length);
  const frqPromptIds = shuffle(availableFrqs.map((f) => f.id)).slice(0, frqTarget ?? availableFrqs.length);

  const attempt = await db.examAttempt.create({
    data: { userId, courseId, questionIds, frqPromptIds },
  });

  redirect(`/courses/${courseSlug}/exam/${attempt.id}`);
}

interface SubmitExamInput {
  examAttemptId: string;
  courseSlug: string;
  mcqAnswers: { questionId: string; chosenLabel: string }[];
  frqResponses: { frqPromptId: string; responseText: string }[];
}

export async function submitExamAttempt(input: SubmitExamInput): Promise<void> {
  const userId = await requireUserId();
  const db = getDb();

  const attempt = await db.examAttempt.findUnique({ where: { id: input.examAttemptId } });
  if (!attempt || attempt.userId !== userId) throw new Error("Exam attempt not found");

  if (!attempt.completedAt) {
    let mcqCorrect = 0;
    for (const answer of input.mcqAnswers) {
      const question = await db.question.findUnique({
        where: { id: answer.questionId },
        include: { choices: true },
      });
      if (!question) continue;

      const chosen = question.choices.find((c) => c.label === answer.chosenLabel);
      const correct = chosen?.isCorrect ?? false;
      if (correct) mcqCorrect++;

      await db.questionAttempt.create({
        data: {
          userId,
          questionId: answer.questionId,
          chosenLabel: answer.chosenLabel,
          correct,
          timeSpentMs: 0,
          source: "EXAM",
        },
      });

      if (correct) {
        await grantXpForActivity(userId, (streak) => xpForCorrectAnswer(question.difficulty, streak));
      }
    }

    // FRQs are graded afterward on the results page (self-grading needs the
    // rubric, which the student can't see mid-exam) -- 0 here just means
    // "not graded yet," not an actual score.
    for (const response of input.frqResponses) {
      await db.fRQAttempt.create({
        data: {
          userId,
          frqPromptId: response.frqPromptId,
          responseText: response.responseText,
          selfGradedPoints: 0,
        },
      });
    }

    const mcqTotal = (attempt.questionIds as string[]).length;
    const mcqAccuracy = mcqTotal > 0 ? mcqCorrect / mcqTotal : 0;

    await db.examAttempt.update({
      where: { id: attempt.id },
      data: {
        completedAt: new Date(),
        sectionScores: { mcqCorrect, mcqTotal },
        estimatedScore: estimateApScoreRange(mcqAccuracy),
      },
    });

    await checkAndAwardBadges(userId); // covers "exam_finisher"; picked up next time the header/dashboard renders
  }

  revalidatePath("/dashboard");
  redirect(`/courses/${input.courseSlug}/exam/${attempt.id}/results`);
}

export type SubmitBossBattleResult =
  | {
      status: "ok";
      passed: boolean;
      correctCount: number;
      total: number;
      newBadges: BadgeDefinition[];
      // Set only the first time this unit is conquered, not on a rematch.
      newTitle: { title: string; unitNumber: number } | null;
    }
  | { status: "expired" | "invalid" };

// The per-question answers were already graded on the server by recordAttempt
// as the student went (same XP/spaced-repetition path as any other quiz). This
// records the unit-level result once the battle's over, and the result is
// *counted here from those stored attempts*, never taken from the browser: the
// token (signed when the boss page loaded) fixes whose battle it is and when it
// started, and only answers given since then count. A battle that wasn't played
// scores 0, whatever the client claims.
export async function submitBossBattle(input: { battleToken: string }): Promise<SubmitBossBattleResult> {
  const userId = await requireUserId();
  const db = getDb();

  const check = verifyBossBattle(input.battleToken, bossBattleSecret());
  if (!check.ok) return { status: check.reason };
  const { unitId, startedAtMs } = check.start;
  if (check.start.userId !== userId) return { status: "invalid" };

  const questions = await db.question.findMany({ where: { unitId }, select: { id: true } });
  const questionIds = questions.map((q) => q.id);
  const attempts = await db.questionAttempt.findMany({
    where: { userId, questionId: { in: questionIds }, createdAt: { gte: new Date(startedAtMs) } },
    select: { questionId: true, correct: true, createdAt: true },
  });

  const total = questionIds.length;
  const correctCount = scoreBossBattle(questionIds, attempts, startedAtMs);
  const passed = hasPassedBossBattle(correctCount, total);

  const existing = await db.bossBattleAttempt.findUnique({
    where: { userId_unitId: { userId, unitId } },
  });

  await db.bossBattleAttempt.upsert({
    where: { userId_unitId: { userId, unitId } },
    create: { userId, unitId, passed, attemptsCount: 1, bestScore: correctCount },
    update: {
      passed: passed || (existing?.passed ?? false), // once conquered, stays conquered
      attemptsCount: (existing?.attemptsCount ?? 0) + 1,
      bestScore: Math.max(existing?.bestScore ?? 0, correctCount),
    },
  });

  const newBadges = passed ? await checkAndAwardBadges(userId) : [];

  let newTitle: { title: string; unitNumber: number } | null = null;
  if (passed && !existing?.passed) {
    const unit = await db.unit.findUnique({ where: { id: unitId }, select: { order: true } });
    if (unit) newTitle = { title: unitConquerorTitle(unit.order), unitNumber: unit.order };
  }

  revalidatePath("/dashboard");
  return { status: "ok", passed, correctCount, total, newBadges, newTitle };
}
