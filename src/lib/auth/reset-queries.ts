import { getDb } from "@/lib/db";
import { hashResetToken, looksLikeResetToken } from "@/lib/auth/reset-token";

// For the reset page: say so up front when a link is already dead, without using it up. Not in
// reset-actions.ts because every export of a "use server" file is callable from the browser.
export async function isResetLinkUsable(token: unknown): Promise<boolean> {
  if (!looksLikeResetToken(token)) return false;
  const row = await getDb().passwordResetToken.findUnique({ where: { tokenHash: hashResetToken(token) }, select: { usedAt: true, expiresAt: true } });
  return Boolean(row && !row.usedAt && row.expiresAt > new Date());
}
