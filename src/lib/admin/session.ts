import { notFound } from "next/navigation";
import { requireUserId } from "@/lib/auth/session";
import { getDb } from "@/lib/db";

// Role isn't on the session (see src/lib/auth/config.ts) -- a DB lookup here
// is simpler than threading role through the jwt/session callbacks for a
// single admin-only page.
export async function requireAdminUserId(): Promise<string> {
  const userId = await requireUserId();
  const user = await getDb().user.findUnique({ where: { id: userId }, select: { role: true } });
  if (user?.role !== "ADMIN") notFound();
  return userId;
}
