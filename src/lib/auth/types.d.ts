import type { DefaultSession } from "next-auth";

// Auth.js's default types don't know about the `id` the jwt/session callbacks
// in config.ts add -- without this, `session.user.id` is a type error even
// though it's present at runtime.
declare module "next-auth" {
  interface Session {
    user: {
      id: string;
    } & DefaultSession["user"];
  }
}

declare module "next-auth/jwt" {
  interface JWT {
    id?: string;
  }
}
