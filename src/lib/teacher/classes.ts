import { notFound } from "next/navigation";
import { requireUserId } from "@/lib/auth/session";
import { getDb } from "@/lib/db";
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

// There is no teacher role: anyone who owns a class is a teacher of it. Anyone
// else gets a 404, the same convention as the admin pages. When real student
// data is added to this area, replace this with an explicit role.
export async function requireOwnedClasses(): Promise<{ userId: string; classes: OwnedClass[] }> {
  const userId = await requireUserId();
  const classes = await getOwnedClasses(userId);
  if (classes.length === 0) notFound();
  return { userId, classes };
}
