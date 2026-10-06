import { z } from "zod";
import { MINIMUM_AGE } from "@/lib/age";
import { PASSWORD_MIN_LENGTH, isPasswordTooLong } from "@/lib/auth/password";

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
  password: z
    .string()
    .min(PASSWORD_MIN_LENGTH, `At least ${PASSWORD_MIN_LENGTH} characters`)
    .refine((p) => !isPasswordTooLong(p), "That password is too long. Use a shorter one."),
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

// What the auth actions hand back to their forms. After a rejected submission the
// form needs the values again: React empties an uncontrolled <form action>
// once its action finishes, so without them everything typed would vanish. The
// password is deliberately never part of this.
export interface SignUpFormState {
  error?: string;
  values?: { displayName: string; username: string; email: string; ageConfirmed: boolean };
}

export interface LoginFormState {
  error?: string;
  values?: { email: string };
}

export const ChangePasswordSchema = z
  .object({
    currentPassword: z.string().min(1, "Enter your current password"),
    newPassword: z
      .string()
      .min(PASSWORD_MIN_LENGTH, `At least ${PASSWORD_MIN_LENGTH} characters`)
      .refine((p) => !isPasswordTooLong(p), "That password is too long. Use a shorter one."),
    confirmPassword: z.string(),
  })
  .refine((d) => d.newPassword === d.confirmPassword, { path: ["confirmPassword"], message: "The new passwords don't match." })
  .refine((d) => d.newPassword !== d.currentPassword, { path: ["newPassword"], message: "The new password is the same as the current one." });

export const DeleteAccountSchema = z.object({
  password: z.string().min(1, "Enter your password"),
  understand: z.literal("yes", "Tick the box to confirm you want to delete your account."),
});

// What the Settings forms get back. Neither ever contains a password.
export interface PasswordFormState {
  error?: string;
  message?: string;
  // Set on success: the email to sign this device back in with (the form already holds
  // the new password). See ChangePasswordForm.
  signInAs?: string;
}

export interface DeleteAccountFormState {
  error?: string;
}

export const ForgotPasswordSchema = z.object({ email: z.email("Enter a valid email") });

export const ResetPasswordSchema = z
  .object({
    token: z.string(),
    newPassword: z
      .string()
      .min(PASSWORD_MIN_LENGTH, `At least ${PASSWORD_MIN_LENGTH} characters`)
      .refine((p) => !isPasswordTooLong(p), "That password is too long. Use a shorter one."),
    confirmPassword: z.string(),
  })
  .refine((d) => d.newPassword === d.confirmPassword, { path: ["confirmPassword"], message: "The new passwords don't match." });

export interface ForgotPasswordFormState {
  error?: string;
  // The same answer whether or not the address has an account.
  sent?: boolean;
  values?: { email: string };
}

export interface ResetPasswordFormState {
  error?: string;
  done?: boolean;
}
