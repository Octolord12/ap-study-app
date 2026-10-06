"use client";

import { useActionState } from "react";
import Link from "next/link";
import { resetPasswordAction } from "@/lib/auth/reset-actions";
import { PASSWORD_MIN_LENGTH } from "@/lib/auth/password";
import type { ResetPasswordFormState } from "@/lib/auth/schema";
import { Button } from "@/components/ui/button";
import { Field } from "@/components/ui/field";
import { Input } from "@/components/ui/input";

const linkClass = "text-sm font-semibold underline underline-offset-4 hover:bg-mark hover:text-on-mark hover:no-underline";

// Passwords are never refilled: after any result the fields come back empty.
export function ResetPasswordForm({ token }: { token: string }) {
  const [state, formAction, isPending] = useActionState(resetPasswordAction, {} as ResetPasswordFormState);

  if (state.done) {
    return (
      <div className="max-w-md space-y-4" role="status">
        <p className="reading text-lg">Your password is changed. Any device that was signed in has been signed out.</p>
        <Link
          href="/login"
          className="inline-flex h-12 items-center justify-center rounded-sm border border-foreground bg-foreground px-5 text-[0.9375rem] font-semibold text-background transition-colors hover:bg-mark hover:text-on-mark"
        >
          Log in
        </Link>
      </div>
    );
  }

  return (
    <form action={formAction} className="max-w-sm space-y-5">
      <input type="hidden" name="token" value={token} />
      <Field id="newPassword" label="New password" hint={`At least ${PASSWORD_MIN_LENGTH} characters.`}>
        <Input id="newPassword" name="newPassword" type="password" required autoComplete="new-password" minLength={PASSWORD_MIN_LENGTH} />
      </Field>
      <Field id="confirmPassword" label="New password again">
        <Input id="confirmPassword" name="confirmPassword" type="password" required autoComplete="new-password" />
      </Field>
      {state.error ? (
        <div role="alert" className="space-y-2">
          <p className="text-sm font-medium text-incorrect">{state.error}</p>
          <Link href="/forgot-password" className={linkClass}>
            Ask for a new link
          </Link>
        </div>
      ) : null}
      <div className="pt-1">
        <Button type="submit" size="lg" disabled={isPending}>
          {isPending ? "Saving…" : "Change password"}
        </Button>
      </div>
    </form>
  );
}
