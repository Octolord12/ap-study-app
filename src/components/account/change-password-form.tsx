"use client";

import { useActionState } from "react";
import { signIn } from "next-auth/react";
import { changePasswordAction } from "@/lib/auth/account-actions";
import { PASSWORD_MIN_LENGTH } from "@/lib/auth/password";
import type { PasswordFormState } from "@/lib/auth/schema";
import { Button } from "@/components/ui/button";
import { Field } from "@/components/ui/field";
import { Input } from "@/components/ui/input";

// Changing the password voids every sign-in issued before it, on every device, this one
// included. So once the server has changed it, this device signs itself in again with the
// new password (the form still has it) and every other device stays signed out.
async function changePasswordAndStaySignedIn(previous: PasswordFormState, formData: FormData): Promise<PasswordFormState> {
  const result = await changePasswordAction(previous, formData);
  if (!result.signInAs) return result;

  try {
    const again = await signIn("credentials", {
      email: result.signInAs,
      password: String(formData.get("newPassword") ?? ""),
      redirect: false,
    });
    if (again?.error) throw new Error(again.error);
  } catch {
    return { message: "Password changed. Sign in again with the new one." };
  }
  return { message: "Password changed. Any other device you were signed in on has been signed out." };
}

// Passwords are never refilled: after any result the fields come back empty.
export function ChangePasswordForm() {
  const [state, formAction, isPending] = useActionState(changePasswordAndStaySignedIn, {} as PasswordFormState);

  return (
    <form action={formAction} className="max-w-sm space-y-5">
      <Field id="currentPassword" label="Current password">
        <Input id="currentPassword" name="currentPassword" type="password" required autoComplete="current-password" />
      </Field>
      <Field id="newPassword" label="New password" hint={`At least ${PASSWORD_MIN_LENGTH} characters.`}>
        <Input id="newPassword" name="newPassword" type="password" required autoComplete="new-password" minLength={PASSWORD_MIN_LENGTH} />
      </Field>
      <Field id="confirmPassword" label="New password again">
        <Input id="confirmPassword" name="confirmPassword" type="password" required autoComplete="new-password" />
      </Field>
      {state.error ? (
        <p role="alert" className="text-sm font-medium text-incorrect">
          {state.error}
        </p>
      ) : null}
      {state.message ? (
        <p role="status" className="text-sm font-medium">
          {state.message}
        </p>
      ) : null}
      <Button type="submit" size="lg" disabled={isPending}>
        {isPending ? "Changing…" : "Change password"}
      </Button>
    </form>
  );
}
