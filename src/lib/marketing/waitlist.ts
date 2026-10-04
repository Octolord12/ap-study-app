import { z } from "zod";

// Trimmed and lowercased before the format check, so the unique index on
// WaitlistSignup.email treats "A@x.com " and "a@x.com" as one signup.
export const WaitlistSchema = z.object({
  email: z
    .string()
    .trim()
    .toLowerCase()
    .max(254, "That email address is too long.")
    .pipe(z.email("Enter a valid email address.")),
});

export type WaitlistState = { status: "idle" } | { status: "done" } | { status: "error"; message: string };

export const WAITLIST_IDLE: WaitlistState = { status: "idle" };
