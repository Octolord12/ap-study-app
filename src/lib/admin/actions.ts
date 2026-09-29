"use server";

import { revalidatePath } from "next/cache";
import { getDb } from "@/lib/db";
import { requireAdminUserId } from "@/lib/admin/session";

export async function markQuestionReviewed(questionId: string) {
  await requireAdminUserId();
  await getDb().question.update({ where: { id: questionId }, data: { reviewed: true } });
  revalidatePath("/admin/review");
}

export async function markFrqReviewed(frqPromptId: string) {
  await requireAdminUserId();
  await getDb().fRQPrompt.update({ where: { id: frqPromptId }, data: { reviewed: true } });
  revalidatePath("/admin/review");
}
