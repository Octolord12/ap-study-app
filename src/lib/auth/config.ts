import NextAuth from "next-auth";
import Credentials from "next-auth/providers/credentials";
import { PrismaAdapter } from "@auth/prisma-adapter";
import bcrypt from "bcryptjs";
import { getDb } from "@/lib/db";

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

        return { id: user.id, email: user.email, name: user.displayName };
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
    jwt({ token, user }) {
      if (user) token.id = user.id;
      return token;
    },
    session({ session, token }) {
      if (session.user) session.user.id = token.id as string;
      return session;
    },
  },
});
