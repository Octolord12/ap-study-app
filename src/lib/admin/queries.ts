import { getDb } from "@/lib/db";

// A topic's refresher is waiting for review when one is written and not yet approved.
const REFRESHER_PENDING = { refresher: { not: null }, refresherReviewed: false } as const;

export async function listCoursesWithUnreviewedCounts() {
  const courses = await getDb().course.findMany({ orderBy: { name: "asc" } });
  return Promise.all(
    courses.map(async (course) => {
      const [questionCount, frqCount, refresherCount] = await Promise.all([
        getDb().question.count({ where: { reviewed: false, unit: { courseId: course.id } } }),
        getDb().fRQPrompt.count({ where: { reviewed: false, unit: { courseId: course.id } } }),
        getDb().topic.count({ where: { ...REFRESHER_PENDING, unit: { courseId: course.id } } }),
      ]);
      return { course, questionCount, frqCount, refresherCount };
    }),
  );
}

export async function getUnitsWithUnreviewedCounts(courseSlug: string) {
  const course = await getDb().course.findUnique({ where: { slug: courseSlug } });
  if (!course) return null;

  const units = await getDb().unit.findMany({
    where: { courseId: course.id },
    orderBy: { order: "asc" },
    include: {
      _count: {
        select: {
          questions: { where: { reviewed: false } },
          frqPrompts: { where: { reviewed: false } },
          topics: { where: REFRESHER_PENDING },
        },
      },
    },
  });
  return { course, units };
}

export async function getUnitUnreviewedContent(courseSlug: string, unitSlug: string) {
  const course = await getDb().course.findUnique({ where: { slug: courseSlug } });
  if (!course) return null;

  const unit = await getDb().unit.findUnique({
    where: { courseId_slug: { courseId: course.id, slug: unitSlug } },
    include: {
      questions: {
        where: { reviewed: false },
        orderBy: { createdAt: "asc" },
        include: { choices: { orderBy: { label: "asc" } }, topic: true },
      },
      frqPrompts: {
        where: { reviewed: false },
        orderBy: { createdAt: "asc" },
        include: { topic: true },
      },
      topics: { where: REFRESHER_PENDING, orderBy: { order: "asc" } },
    },
  });
  if (!unit) return null;

  return { course, unit };
}
