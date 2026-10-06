"use server";

import bcrypt from "bcryptjs";
import { auth, signOut } from "@/lib/auth/config";
import { getDb } from "@/lib/db";
import { BCRYPT_ROUNDS } from "@/lib/auth/password";
import { notifyPasswordChanged } from "@/lib/email/notify";
import {
  ChangePasswordSchema,
  DeleteAccountSchema,
  type DeleteAccountFormState,
  type PasswordFormState,
} from "@/lib/auth/schema";

// Both actions act on the signed-in student's own account, taken from the session and
// never from anything the form sends, and both re-ask for the password: a session
// that was left open on a shared computer shouldn't be enough to lock someone out
// of their account or erase it.
async function requireUserId(): Promise<string> {
  const session = await auth();
  if (!session?.user?.id) throw new Error("Not authenticated");
  return session.user.id;
}

export async function changePasswordAction(_prev: PasswordFormState, formData: FormData): Promise<PasswordFormState> {
  const userId = await requireUserId();

  const parsed = ChangePasswordSchema.safeParse({
    currentPassword: formData.get("currentPassword"),
    newPassword: formData.get("newPassword"),
    confirmPassword: formData.get("confirmPassword"),
  });
  if (!parsed.success) return { error: parsed.error.issues[0]?.message ?? "Invalid input." };

  const db = getDb();
  const user = await db.user.findUnique({ where: { id: userId }, select: { email: true, passwordHash: true } });
  if (!user?.passwordHash) return { error: "This account doesn't use a password." };
  if (!(await bcrypt.compare(parsed.data.currentPassword, user.passwordHash))) return { error: "That isn't your current password." };

  await db.user.update({ where: { id: userId }, data: { passwordHash: await bcrypt.hash(parsed.data.newPassword, BCRYPT_ROUNDS) } });

  // Every sign-in token issued before this moment is now void (credentials-stamp.ts),
  // this device's included. This device is signed in again by the form, from the browser,
  // through Auth.js's own login endpoint, and not here: setting a cookie in a Server Action
  // makes Next re-render the page in the same request from the *old* cookie header, which
  // bounced the student to /login and lost this confirmation.
  notifyPasswordChanged(user.email);
  return { message: "Password changed.", signInAs: user.email };
}

export async function deleteAccountAction(_prev: DeleteAccountFormState, formData: FormData): Promise<DeleteAccountFormState> {
  const userId = await requireUserId();

  const parsed = DeleteAccountSchema.safeParse({ password: formData.get("password"), understand: formData.get("understand") });
  if (!parsed.success) return { error: parsed.error.issues[0]?.message ?? "Invalid input." };

  const db = getDb();
  const user = await db.user.findUnique({ where: { id: userId }, select: { email: true, passwordHash: true } });
  if (!user?.passwordHash) return { error: "This account doesn't use a password." };
  if (!(await bcrypt.compare(parsed.data.password, user.passwordHash))) return { error: "That isn't your password." };

  // Deleting the user removes everything tied to it (answers, progress, free-response
  // work, friends, memberships, and any class they own) through the schema's cascades.
  // The waitlist isn't tied to a user, so a signup under the same email goes with it.
  await db.$transaction([db.waitlistSignup.deleteMany({ where: { email: user.email.toLowerCase() } }), db.user.delete({ where: { id: userId } })]);

  // Throws the redirect; nothing after it runs.
  await signOut({ redirectTo: "/account-deleted" });
  return {};
}
