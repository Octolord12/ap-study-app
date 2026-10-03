"use server";

import bcrypt from "bcryptjs";
import { AuthError } from "next-auth";
import { getDb } from "@/lib/db";
import { signIn, signOut } from "@/lib/auth/config";
import { LoginSchema, SignUpSchema } from "@/lib/auth/schema";

const BCRYPT_ROUNDS = 12;

export async function signUpAction(_prevState: string | undefined, formData: FormData): Promise<string | undefined> {
  const parsed = SignUpSchema.safeParse({
    displayName: formData.get("displayName"),
    username: formData.get("username"),
    email: formData.get("email"),
    password: formData.get("password"),
  });

  if (!parsed.success) {
    return parsed.error.issues[0]?.message ?? "Invalid input.";
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
    return existing.email === email ? "That email is already registered." : "That username is taken.";
  }

  const passwordHash = await bcrypt.hash(password, BCRYPT_ROUNDS);
  await db.user.create({
    data: { displayName, username, email, passwordHash },
  });

  // Signing in after create throws a Next.js redirect internally -- let it propagate.
  await signIn("credentials", { email, password, redirectTo: "/courses" });
}

export async function loginAction(_prevState: string | undefined, formData: FormData): Promise<string | undefined> {
  const parsed = LoginSchema.safeParse({
    email: formData.get("email"),
    password: formData.get("password"),
  });

  if (!parsed.success) {
    return parsed.error.issues[0]?.message ?? "Invalid input.";
  }

  try {
    await signIn("credentials", { ...parsed.data, redirectTo: "/" });
  } catch (error) {
    // AuthError covers bad credentials; anything else (including the redirect
    // Next.js throws on success) must propagate, not be swallowed here.
    if (error instanceof AuthError) {
      return "Incorrect email or password.";
    }
    throw error;
  }
}

export async function logoutAction() {
  await signOut({ redirectTo: "/" });
}
