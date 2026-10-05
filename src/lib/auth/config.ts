import { cache } from "react";
import NextAuth from "next-auth";
import Credentials from "next-auth/providers/credentials";
import { PrismaAdapter } from "@auth/prisma-adapter";
import bcrypt from "bcryptjs";
import { getDb } from "@/lib/db";
import { credentialsStamp, judgeStamp, type StampVerdict } from "@/lib/auth/credentials-stamp";

// Keyed by the token's own stamp as well as the user: a password change inside one
// request (the change-password action signs the student back in) must not be answered
// from a result computed before it.
const checkStamp = cache(async (userId: string, tokenStamp: string): Promise<StampVerdict> => {
  const user = await getDb().user.findUnique({ where: { id: userId }, select: { passwordHash: true } });
  return judgeStamp(tokenStamp || undefined, user ? credentialsStamp(user.passwordHash) : null);
});

// Full login/signup pages are built in Milestone 3. This wires the provider
// so the rest of the stack (Prisma adapter, session shape) is proven out now.
export const { handlers, auth, signIn, signOut } = NextAuth({
  trustHost: true,
  adapter: PrismaAdapter(getDb()),
  // Credentials logins can't be persisted as adapter sessions, so this
  // provider requires JWT session storage (cookie-based, not a DB row).
  session: { strategy: "jwt" },
  providers: [
    Credentials({
      credentials: {
        email: { label: "Email", type: "email" },
        password: { label: "Password", type: "password" },
      },
      authorize: async (credentials) => {
        const email = credentials?.email as string | undefined;
        const password = credentials?.password as string | undefined;
        if (!email || !password) return null;

        const user = await getDb().user.findUnique({ where: { email } });
        if (!user?.passwordHash) return null;

        const passwordMatches = await bcrypt.compare(password, user.passwordHash);
        if (!passwordMatches) return null;

        return { id: user.id, email: user.email, name: user.displayName, stamp: credentialsStamp(user.passwordHash) };
      },
    }),
  ],
  pages: {
    signIn: "/login",
  },
  callbacks: {
    // Auth.js's default JWT session does NOT include the user id -- session.user
    // only gets name/email/image unless these two callbacks propagate it
    // token -> session. Every requireUserId() call and Server Action depends
    // on session.user.id existing, so this isn't optional.
    //
    // It also decides whether a token is still good (returning null signs it out and
    // clears its cookie): a token is only honoured while the account exists and its
    // password hasn't changed since the token was issued, so changing a password, or
    // deleting the account, signs out every other device. Deliberately ignores
    // `trigger: "update"`: a client can post that to /api/auth/session itself, so
    // letting it refresh the stamp would let a stale token revive itself.
    async jwt({ token, user }) {
      if (user) {
        token.id = user.id;
        token.stamp = user.stamp;
        return token;
      }
      if (!token.id) return token;
      try {
        const verdict = await checkStamp(token.id as string, (token.stamp as string | undefined) ?? "");
        if (!verdict.ok) return null;
        token.stamp = verdict.stamp;
      } catch (error) {
        // A database blip shouldn't sign everyone out; the pages that need it will fail
        // on their own. Log the kind of error only.
        console.error("session check failed", error instanceof Error ? error.name : "unknown");
      }
      return token;
    },
    session({ session, token }) {
      if (session.user) session.user.id = token.id as string;
      return session;
    },
  },
});
