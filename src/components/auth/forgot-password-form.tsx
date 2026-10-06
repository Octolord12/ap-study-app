"use client";

import { useActionState } from "react";
import Link from "next/link";
import { requestPasswordResetAction } from "@/lib/auth/reset-actions";
import { RESET_TOKEN_MINUTES } from "@/lib/auth/reset-constants";
import type { ForgotPasswordFormState } from "@/lib/auth/schema";
import { Button } from "@/components/ui/button";
import { Field } from "@/components/ui/field";
import { Input } from "@/components/ui/input";

const linkClass = "text-sm font-semibold underline underline-offset-4 hover:bg-mark hover:text-on-mark hover:no-underline";

export function ForgotPasswordForm() {
  const [{ error, sent, values }, formAction, isPending] = useActionState(requestPasswordResetAction, {} as ForgotPasswordFormState);

  // The same words for every address, so the page never says whether an account exists.
  if (sent) {
    return (
      <div className="max-w-md space-y-4" role="status">
        <p className="reading text-lg">If {values?.email ? <strong>{values.email}</strong> : "that email"} has an account, we have sent a link to choose a new password.</p>
        <p className="reading">
          It works once and expires in {RESET_TOKEN_MINUTES} minutes. If nothing arrives in a few minutes, check your spam folder.
        </p>
        <Link href="/login" className={linkClass}>
          Back to log in
        </Link>
      </div>
    );
  }

  return (
    <form action={formAction} className="max-w-sm space-y-5">
      <Field id="email" label="Email" hint="The email you signed up with.">
        <Input key={values?.email ?? ""} id="email" name="email" type="email" required autoComplete="email" defaultValue={values?.email} />
      </Field>
      {error ? (
        <p role="alert" className="text-sm font-medium text-incorrect">
          {error}
        </p>
      ) : null}
      <div className="flex flex-wrap items-center gap-x-6 gap-y-3 pt-1">
        <Button type="submit" size="lg" disabled={isPending}>
          {isPending ? "Sending…" : "Send reset link"}
        </Button>
        <Link href="/login" className={linkClass}>
          Back to log in
        </Link>
      </div>
    </form>
  );
}
