import { getDb } from "@/lib/db";
import { topicKey } from "@/lib/study/concept-link";
import { rankCramQuestions, type CramCandidate } from "@/lib/study/cram";
import { shuffled } from "@/lib/study/exam-selection";

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

// For the custom-quiz form: units with how many questions each has, so the
// student can see what a difficulty/unit combination will actually give them.
export function getCourseUnitsWithQuestionCounts(courseSlug: string) {
  return getDb().course.findUnique({
    where: { slug: courseSlug },
    include: {
      units: {
        orderBy: { order: "asc" },
        include: { _count: { select: { questions: true } } },
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
      frqPrompts: {
        orderBy: { createdAt: "asc" },
        include: { topic: true },
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

interface CustomQuizFilter {
  courseId: string;
  unitIds: string[];
  difficulty?: "EASY" | "MEDIUM" | "HARD";
  length: number;
}

// Picks a random subset matching the filter, uniformly: every matching question is equally likely.
// (`sort(() => Math.random() - 0.5)` looks the same but is not uniform: at 360 questions and a 20-question
// quiz it picked the first ones about 1.75x as often as it should and the last ones about 0.56x.)
export async function pickQuestionIdsForCustomQuiz(filter: CustomQuizFilter): Promise<string[]> {
  const matches = await getDb().question.findMany({
    where: {
      courseId: filter.courseId,
      unitId: { in: filter.unitIds },
      ...(filter.difficulty ? { difficulty: filter.difficulty } : {}),
    },
    select: { id: true },
  });

  return shuffled(matches)
    .slice(0, filter.length)
    .map((q) => q.id);
}

// Questions the student has previously gotten wrong (or hasn't reinforced
// enough) whose spaced-repetition due date has arrived.
export async function getDueWeakSpotQuestionIds(userId: string, courseId: string, limit = 20): Promise<string[]> {
  const dueStates = await getDb().spacedRepetitionState.findMany({
    where: {
      userId,
      dueAt: { lte: new Date() },
      question: { courseId },
    },
    orderBy: { dueAt: "asc" },
    take: limit,
    select: { questionId: true },
  });
  return dueStates.map((s) => s.questionId);
}

// Cram mode's version of the review queue: the student's most-missed questions
// and the ones they have never seen, whatever their spaced-repetition due
// dates say. Scoped to one course, like every other practice flow.
export async function getCramQuestionIds(userId: string, courseId: string): Promise<string[]> {
  const db = getDb();
  const [questions, attemptCounts] = await Promise.all([
    db.question.findMany({ where: { courseId }, select: { id: true } }),
    db.questionAttempt.groupBy({
      by: ["questionId", "correct"],
      where: { userId, question: { courseId } },
      _count: { _all: true },
    }),
  ]);

  const byId = new Map<string, CramCandidate>(questions.map((q) => [q.id, { id: q.id, attempts: 0, misses: 0 }]));
  for (const row of attemptCounts) {
    const candidate = byId.get(row.questionId);
    if (!candidate) continue;
    candidate.attempts += row._count._all;
    if (!row.correct) candidate.misses += row._count._all;
  }
  return rankCramQuestions([...byId.values()]);
}

// The one place that decides what "review" means, so the practice hub, the
// weak-spot page and the Today screen can't disagree about it.
export function getReviewQueueIds(userId: string, courseId: string, cram: boolean): Promise<string[]> {
  return cram ? getCramQuestionIds(userId, courseId) : getDueWeakSpotQuestionIds(userId, courseId);
}

const DAILY_CHALLENGE_SIZE = 5;

export async function hasCompletedDailyChallengeToday(userId: string, courseId: string): Promise<boolean> {
  const startOfToday = new Date();
  startOfToday.setHours(0, 0, 0, 0);

  const count = await getDb().questionAttempt.count({
    where: {
      userId,
      source: "DAILY",
      createdAt: { gte: startOfToday },
      question: { courseId },
    },
  });
  return count > 0;
}

// Prioritizes weak-spot questions (already due for review) to fill the daily
// set; tops up with a random sample of the rest if there aren't enough.
export async function pickDailyChallengeQuestionIds(userId: string, courseId: string): Promise<string[]> {
  const dueIds = await getDueWeakSpotQuestionIds(userId, courseId, DAILY_CHALLENGE_SIZE);
  if (dueIds.length >= DAILY_CHALLENGE_SIZE) return dueIds.slice(0, DAILY_CHALLENGE_SIZE);

  const remaining = DAILY_CHALLENGE_SIZE - dueIds.length;
  const fillerCandidates = await getDb().question.findMany({
    where: { courseId, id: { notIn: dueIds } },
    select: { id: true },
  });
  const filler = shuffled(fillerCandidates).slice(0, remaining);

  return [...dueIds, ...filler.map((q) => q.id)];
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

// "<unit>/<topic>" for every topic of the course that has a written refresher. One small query, used to
// decide where each "Review this concept" link goes (see concept-link.ts).
export async function getTopicKeysWithRefreshers(courseSlug: string): Promise<Set<string>> {
  const topics = await getDb().topic.findMany({
    where: { refresher: { not: null }, unit: { course: { slug: courseSlug } } },
    select: { slug: true, unit: { select: { slug: true } } },
  });
  return new Set(topics.map((t) => topicKey(t.unit.slug, t.slug)));
}

// A topic with its unit, course, its unit's other topics (for previous/next) and its questions.
export async function getTopicWithQuestions(courseSlug: string, unitSlug: string, topicSlug: string) {
  const db = getDb();
  const course = await db.course.findUnique({ where: { slug: courseSlug } });
  if (!course) return null;

  const unit = await db.unit.findUnique({
    where: { courseId_slug: { courseId: course.id, slug: unitSlug } },
    include: { topics: { orderBy: { order: "asc" }, select: { id: true, slug: true, name: true, order: true, refresher: true } } },
  });
  if (!unit) return null;

  const topic = await db.topic.findUnique({
    where: { unitId_slug: { unitId: unit.id, slug: topicSlug } },
    include: { questions: { select: { id: true } } },
  });
  if (!topic) return null;

  return { course, unit, topic };
}
