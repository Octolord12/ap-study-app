"use server";

import bcrypt from "bcryptjs";
import { AuthError } from "next-auth";
import { getDb } from "@/lib/db";
import { signIn, signOut } from "@/lib/auth/config";
import { BCRYPT_ROUNDS } from "@/lib/auth/password";
import { LoginSchema, SignUpSchema, type LoginFormState, type SignUpFormState } from "@/lib/auth/schema";

// What the person typed, echoed back so the form can refill itself (capped, since
// it is the request's own input).
function typed(formData: FormData, key: string): string {
  const value = formData.get(key);
  return typeof value === "string" ? value.slice(0, 254) : "";
}

export async function signUpAction(_prevState: SignUpFormState, formData: FormData): Promise<SignUpFormState> {
  const values = {
    displayName: typed(formData, "displayName"),
    username: typed(formData, "username"),
    email: typed(formData, "email"),
    ageConfirmed: formData.get("ageConfirmed") === "yes",
  };
  const parsed = SignUpSchema.safeParse({
    displayName: formData.get("displayName"),
    username: formData.get("username"),
    email: formData.get("email"),
    password: formData.get("password"),
    ageConfirmed: formData.get("ageConfirmed"),
  });

  if (!parsed.success) {
    return { error: parsed.error.issues[0]?.message ?? "Invalid input.", values };
  }

  const { displayName, username, email, password } = parsed.data;
  const db = getDb();

  // Username uniqueness is checked case-insensitively so two accounts can't
  // register case-variant usernames (e.g. "JohnDoe" and "johndoe") -- that
  // would make the friend-search lookup in social/actions.ts, which is
  // deliberately case-insensitive, ambiguous.
  const existing = await db.user.findFirst({
    where: { OR: [{ email }, { username: { equals: username, mode: "insensitive" } }] },
    select: { email: true, username: true },
  });
  if (existing) {
    return { error: existing.email === email ? "That email is already registered." : "That username is taken.", values };
  }

  const passwordHash = await bcrypt.hash(password, BCRYPT_ROUNDS);
  await db.user.create({
    data: { displayName, username, email, passwordHash },
  });

  // Signing in after create throws a Next.js redirect internally -- let it propagate.
  await signIn("credentials", { email, password, redirectTo: "/courses" });
  return {};
}

export async function loginAction(_prevState: LoginFormState, formData: FormData): Promise<LoginFormState> {
  const values = { email: typed(formData, "email") };
  const parsed = LoginSchema.safeParse({
    email: formData.get("email"),
    password: formData.get("password"),
  });

  if (!parsed.success) {
    return { error: parsed.error.issues[0]?.message ?? "Invalid input.", values };
  }

  try {
    await signIn("credentials", { ...parsed.data, redirectTo: "/" });
  } catch (error) {
    // AuthError covers bad credentials; anything else (including the redirect
    // Next.js throws on success) must propagate, not be swallowed here.
    if (error instanceof AuthError) {
      return { error: "Incorrect email or password.", values };
    }
    throw error;
  }
  return {};
}

export async function logoutAction() {
  await signOut({ redirectTo: "/" });
}
