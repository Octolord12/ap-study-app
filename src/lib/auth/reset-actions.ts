"use server";

import bcrypt from "bcryptjs";
import { getDb } from "@/lib/db";
import { afterResponse } from "@/lib/after-response";
import { BCRYPT_ROUNDS } from "@/lib/auth/password";
import { MAX_RESET_REQUESTS_PER_HOUR, RESET_LINK_INVALID } from "@/lib/auth/reset-constants";
import { hashResetToken, looksLikeResetToken, newResetToken } from "@/lib/auth/reset-token";
import {
  ForgotPasswordSchema,
  ResetPasswordSchema,
  type ForgotPasswordFormState,
  type ResetPasswordFormState,
} from "@/lib/auth/schema";
import { isPasswordResetAvailable, siteUrl } from "@/lib/email/config";
import { notifyPasswordChanged } from "@/lib/email/notify";
import { sendEmail } from "@/lib/email/send";
import { passwordResetEmail } from "@/lib/email/templates";

const HOUR_MS = 60 * 60_000;
const DAY_MS = 24 * HOUR_MS;

// The answer is the same for every address, and everything that depends on whether the address has an
// account (the lookup, the throttle, the new token, the email) happens after the response is sent, so
// neither the words nor the timing say whether someone is registered.
export async function requestPasswordResetAction(_prev: ForgotPasswordFormState, formData: FormData): Promise<ForgotPasswordFormState> {
  if (!isPasswordResetAvailable()) return { error: "Password reset isn't available yet." };

  const raw = formData.get("email");
  const values = { email: typeof raw === "string" ? raw.slice(0, 254) : "" };
  const parsed = ForgotPasswordSchema.safeParse({ email: raw });
  if (!parsed.success) return { error: parsed.error.issues[0]?.message ?? "Enter a valid email", values };

  const email = parsed.data.email;
  afterResponse(async () => {
    const db = getDb();
    const user = await db.user.findFirst({ where: { email: { equals: email, mode: "insensitive" } }, select: { id: true, email: true, passwordHash: true } });
    if (!user?.passwordHash) return;

    const now = new Date();
    const recent = await db.passwordResetToken.count({ where: { userId: user.id, createdAt: { gt: new Date(now.getTime() - HOUR_MS) } } });
    if (recent >= MAX_RESET_REQUESTS_PER_HOUR) return;

    // The unique (userId, minuteSlot) index is what makes "one a minute" hold when requests arrive at the
    // same moment: of several, one insert wins and the rest hit the constraint and are dropped quietly.
    const { token, tokenHash, expiresAt } = newResetToken(now);
    try {
      await db.passwordResetToken.create({ data: { userId: user.id, tokenHash, expiresAt, minuteSlot: Math.floor(now.getTime() / 60_000) } });
    } catch (error) {
      if ((error as { code?: string }).code === "P2002") return;
      throw error;
    }
    // Only now, with the new link safely stored, is the older one retired; old rows are tidied here
    // rather than by a scheduled job.
    await db.passwordResetToken.updateMany({ where: { userId: user.id, usedAt: null, tokenHash: { not: tokenHash } }, data: { usedAt: now } });
    await db.passwordResetToken.deleteMany({ where: { createdAt: { lt: new Date(now.getTime() - DAY_MS) } } });

    await sendEmail(passwordResetEmail(user.email, `${siteUrl()}/reset-password?token=${token}`));
  });

  return { sent: true, values };
}

export async function resetPasswordAction(_prev: ResetPasswordFormState, formData: FormData): Promise<ResetPasswordFormState> {
  const token = formData.get("token");
  if (!looksLikeResetToken(token)) return { error: RESET_LINK_INVALID };

  const parsed = ResetPasswordSchema.safeParse({ token, newPassword: formData.get("newPassword"), confirmPassword: formData.get("confirmPassword") });
  if (!parsed.success) return { error: parsed.error.issues[0]?.message ?? "Invalid input." };

  const db = getDb();
  const now = new Date();
  const row = await db.passwordResetToken.findUnique({ where: { tokenHash: hashResetToken(token) }, select: { id: true, userId: true } });
  if (!row) return { error: RESET_LINK_INVALID };

  // Claiming the token is one atomic write that only succeeds for an unused, unexpired row, so two
  // requests with the same link can't both get through.
  const claimed = await db.passwordResetToken.updateMany({ where: { id: row.id, usedAt: null, expiresAt: { gt: now } }, data: { usedAt: now } });
  if (claimed.count !== 1) return { error: RESET_LINK_INVALID };

  const passwordHash = await bcrypt.hash(parsed.data.newPassword, BCRYPT_ROUNDS);
  const user = await db.user.update({ where: { id: row.userId }, data: { passwordHash }, select: { email: true } });
  // Any other unused link for this account dies with the old password. Every sign-in token issued
  // before now is void as well (credentials-stamp.ts), so a thief's session doesn't survive a reset.
  await db.passwordResetToken.updateMany({ where: { userId: row.userId, usedAt: null }, data: { usedAt: now } });

  notifyPasswordChanged(user.email);
  return { done: true };
}
