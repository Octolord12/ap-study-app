import { getDb } from "@/lib/db";

export function listCourses() {
  return getDb().course.findMany({ orderBy: { name: "asc" } });
}

export function getCourseTree(courseSlug: string) {
  return getDb().course.findUnique({
    where: { slug: courseSlug },
    include: {
      units: {
        orderBy: { order: "asc" },
        include: { topics: { orderBy: { order: "asc" } } },
      },
    },
  });
}

export async function getUnitWithQuestions(courseSlug: string, unitSlug: string) {
  const db = getDb();
  const course = await db.course.findUnique({ where: { slug: courseSlug } });
  if (!course) return null;

  const unit = await db.unit.findUnique({
    where: { courseId_slug: { courseId: course.id, slug: unitSlug } },
    include: {
      topics: { orderBy: { order: "asc" } },
      questions: {
        orderBy: { createdAt: "asc" },
        include: { choices: { orderBy: { label: "asc" } }, topic: true },
      },
    },
  });
  if (!unit) return null;

  return { course, unit };
}

// Reorders results to match questionIds -- Prisma's `id: { in: [...] }` doesn't
// guarantee result order, but the quiz should follow the order the student saw
// in the (possibly filtered) unit question list.
export async function getQuestionsByIds(questionIds: string[]) {
  const questions = await getDb().question.findMany({
    where: { id: { in: questionIds } },
    include: { choices: { orderBy: { label: "asc" } } },
  });

  const byId = new Map(questions.map((q) => [q.id, q]));
  return questionIds.map((id) => byId.get(id)).filter((q): q is NonNullable<typeof q> => q !== undefined);
}

// "Missed" is derived from each question's most recent attempt, not just "ever
// missed" -- a question the student now answers correctly shouldn't stay flagged.
export async function getUserQuestionState(userId: string, questionIds: string[]) {
  const db = getDb();

  const [bookmarks, attempts] = await Promise.all([
    db.bookmark.findMany({ where: { userId, questionId: { in: questionIds } } }),
    db.questionAttempt.findMany({
      where: { userId, questionId: { in: questionIds } },
      orderBy: { createdAt: "desc" },
      select: { questionId: true, correct: true },
    }),
  ]);

  const bookmarkedIds = new Set(bookmarks.map((b) => b.questionId));

  const latestCorrectByQuestion = new Map<string, boolean>();
  for (const attempt of attempts) {
    if (!latestCorrectByQuestion.has(attempt.questionId)) {
      latestCorrectByQuestion.set(attempt.questionId, attempt.correct);
    }
  }

  return { bookmarkedIds, latestCorrectByQuestion };
}
