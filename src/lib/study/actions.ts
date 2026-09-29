"use server";

import { revalidatePath } from "next/cache";
import { auth } from "@/lib/auth/config";
import { getDb } from "@/lib/db";
import type { AttemptSource } from "@/generated/prisma/client";

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

// Correctness is always looked up fresh from the DB here, never taken from the
// client -- the client already knows the answer (it renders the explanation),
// but the persisted attempt log has to be trustworthy regardless of what the
// client claims.
export async function recordAttempt(input: RecordAttemptInput): Promise<{ correct: boolean }> {
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

  revalidatePath("/dashboard");
  return { correct };
}
