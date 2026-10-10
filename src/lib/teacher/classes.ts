import { getDb } from "@/lib/db";
import { requireTeacherUserId } from "@/lib/teacher/role";
import type { OwnedClass } from "@/lib/teacher/types";

export async function getOwnedClasses(userId: string): Promise<OwnedClass[]> {
  const classes = await getDb().class.findMany({
    where: { ownerId: userId },
    orderBy: { name: "asc" },
    select: { id: true, name: true, inviteCode: true, course: { select: { name: true } }, _count: { select: { memberships: true } } },
  });
  return classes.map((c) => ({
    id: c.id,
    name: c.name,
    inviteCode: c.inviteCode,
    courseName: c.course?.name ?? null,
    memberCount: c._count.memberships,
  }));
}

// The teacher area is for teachers (see role.ts). A teacher with no class yet gets an empty list and the page says how to start one; anyone
// who is not a teacher gets a 404.
export async function requireTeacherClasses(): Promise<{ userId: string; classes: OwnedClass[] }> {
  const userId = await requireTeacherUserId();
  return { userId, classes: await getOwnedClasses(userId) };
}
