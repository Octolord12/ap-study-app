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

export async function markRefresherReviewed(topicId: string) {
  await requireAdminUserId();
  await getDb().topic.update({ where: { id: topicId }, data: { refresherReviewed: true } });
  revalidatePath("/admin/review");
}

// "Approve all" approves exactly the items the admin was looking at (the ids the page rendered), not
// "everything unreviewed in the unit" at click time, so a re-seed that lands while the page is open
// can't get content approved that nobody saw. Only rows still in this unit and still unreviewed change.
export async function approveUnitContent(
  unitId: string,
  questionIds: string[],
  frqPromptIds: string[],
  refresherTopicIds: string[] = [],
): Promise<{ approved: number }> {
  await requireAdminUserId();
  const MAX = 500;
  if (questionIds.length > MAX || frqPromptIds.length > MAX || refresherTopicIds.length > MAX) throw new Error("Too many items");

  const db = getDb();
  const [questions, frqs, refreshers] = await Promise.all([
    questionIds.length ? db.question.updateMany({ where: { id: { in: questionIds }, unitId, reviewed: false }, data: { reviewed: true } }) : { count: 0 },
    frqPromptIds.length ? db.fRQPrompt.updateMany({ where: { id: { in: frqPromptIds }, unitId, reviewed: false }, data: { reviewed: true } }) : { count: 0 },
    refresherTopicIds.length
      ? db.topic.updateMany({
          where: { id: { in: refresherTopicIds }, unitId, refresher: { not: null }, refresherReviewed: false },
          data: { refresherReviewed: true },
        })
      : { count: 0 },
  ]);
  revalidatePath("/admin/review");
  return { approved: questions.count + frqs.count + refreshers.count };
}
