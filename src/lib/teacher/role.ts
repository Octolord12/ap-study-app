import { notFound } from "next/navigation";
import { requireUserId } from "@/lib/auth/session";
import { getDb } from "@/lib/db";

// Who may use the teacher tools: a TEACHER (granted by an admin in /admin/teachers) or an ADMIN. Owning a class is not enough on its own:
// classes are open to every student, so before this role existed "owns a class" was the only line between a student and the teacher area.
export function isTeacherRole(role: string | null | undefined): boolean {
  return role === "TEACHER" || role === "ADMIN";
}

// Role isn't on the session (see src/lib/auth/config.ts), so it is read from the database, the same way requireAdminUserId does. Anyone who is
// not a teacher gets a 404, the convention the admin pages use.
export async function requireTeacherUserId(): Promise<string> {
  const userId = await requireUserId();
  const user = await getDb().user.findUnique({ where: { id: userId }, select: { role: true } });
  if (!isTeacherRole(user?.role)) notFound();
  return userId;
}

export async function userIsTeacher(userId: string): Promise<boolean> {
  const user = await getDb().user.findUnique({ where: { id: userId }, select: { role: true } });
  return isTeacherRole(user?.role);
}
