"use server";

import { revalidatePath } from "next/cache";
import { auth } from "@/lib/auth/config";
import { getDb } from "@/lib/db";
import { toIsoDate, validateExamDate, type ExamDateState } from "@/lib/study/exam-plan";

// Sets, changes or clears the signed-in student's exam date for one course. Only
// their own enrollment can be touched: the where clause is keyed on the session's
// user, never on anything the form sends.
export async function setExamDate(courseId: string, _prev: ExamDateState, formData: FormData): Promise<ExamDateState> {
  const session = await auth();
  if (!session?.user?.id) throw new Error("Not authenticated");

  const clearing = formData.get("intent") === "clear";
  let examDate: Date | null = null;
  if (!clearing) {
    const check = validateExamDate(formData.get("examDate"), toIsoDate(new Date(), "utc"));
    if (!check.ok) return { error: check.error };
    examDate = new Date(`${check.iso}T00:00:00.000Z`);
  }

  const updated = await getDb().enrollment.updateMany({ where: { userId: session.user.id, courseId }, data: { examDate } });
  if (updated.count === 0) return { error: "Start studying this course first." };

  // Today, the course page and the plan all read this.
  revalidatePath("/", "layout");
  return { message: clearing ? "Date removed." : "Saved." };
}
