"use client";

import { useActionState } from "react";
import Link from "next/link";
import { loginAction } from "@/lib/auth/actions";
import type { LoginFormState } from "@/lib/auth/schema";
import { Button } from "@/components/ui/button";
import { Field } from "@/components/ui/field";
import { Input } from "@/components/ui/input";

export function LoginForm() {
  // `values` refills the email after a failed login: React empties an
  // uncontrolled form when its action finishes. The password is never sent back.
  // The field's key is its refilled value: Base UI warns if the default of a
  // mounted input changes, so a new value mounts a fresh input instead.
  const [{ error, values }, formAction, isPending] = useActionState(loginAction, {} as LoginFormState);

  return (
    <form action={formAction} className="max-w-sm space-y-5">
      <Field id="email" label="Email">
        <Input key={values?.email ?? ""} id="email" name="email" type="email" required autoComplete="email" defaultValue={values?.email} />
      </Field>
      <Field id="password" label="Password">
        <Input id="password" name="password" type="password" required autoComplete="current-password" />
      </Field>
      {error ? (
        <p role="alert" className="text-sm font-medium text-incorrect">
          {error}
        </p>
      ) : null}
      <div className="flex flex-wrap items-center gap-x-6 gap-y-3 pt-1">
        <Button type="submit" size="lg" disabled={isPending}>
          {isPending ? "Logging in…" : "Log in"}
        </Button>
        <Link href="/signup" className="text-sm font-semibold underline underline-offset-4 hover:bg-mark hover:text-on-mark hover:no-underline">
          Create an account
        </Link>
      </div>
    </form>
  );
}
