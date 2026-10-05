"use client";

import { useActionState } from "react";
import { changePasswordAction } from "@/lib/auth/account-actions";
import { PASSWORD_MIN_LENGTH } from "@/lib/auth/password";
import type { PasswordFormState } from "@/lib/auth/schema";
import { Button } from "@/components/ui/button";
import { Field } from "@/components/ui/field";
import { Input } from "@/components/ui/input";

// Passwords are never refilled: after any result the fields come back empty.
export function ChangePasswordForm() {
  const [state, formAction, isPending] = useActionState(changePasswordAction, {} as PasswordFormState);

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
