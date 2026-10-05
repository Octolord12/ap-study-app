import { z } from "zod";
import { MINIMUM_AGE } from "@/lib/age";

// Usernames double as public leaderboard identity (Milestone 6), so they're
// restricted to characters that are safe to display and URL-embed.
export const SignUpSchema = z.object({
  displayName: z.string().trim().min(1, "Enter a name").max(60),
  username: z
    .string()
    .trim()
    .min(3, "At least 3 characters")
    .max(24)
    .regex(/^[a-zA-Z0-9_]+$/, "Letters, numbers, and underscores only"),
  email: z.email("Enter a valid email"),
  password: z.string().min(8, "At least 8 characters"),
  // The checkbox's value. Checked on the server so omitting the field from a
  // hand-made request doesn't skip it.
  ageConfirmed: z.literal("yes", `You must be ${MINIMUM_AGE} or older to create an account.`),
});

export const LoginSchema = z.object({
  email: z.email("Enter a valid email"),
  password: z.string().min(1, "Enter your password"),
});

export type SignUpInput = z.infer<typeof SignUpSchema>;
export type LoginInput = z.infer<typeof LoginSchema>;
