"use client";

import { useActionState } from "react";
import Link from "next/link";
import { signUpAction } from "@/lib/auth/actions";
import type { SignUpFormState } from "@/lib/auth/schema";
import { Button } from "@/components/ui/button";
import { Field } from "@/components/ui/field";
import { Input } from "@/components/ui/input";
import { MINIMUM_AGE } from "@/lib/age";

export function SignupForm() {
  // `values` refills the fields after a rejected submit: React empties an
  // uncontrolled form when its action finishes, and resets to these defaults.
  // Each field's key is its refilled value: Base UI warns if the default of a
  // mounted input changes, so a new value mounts a fresh input instead.
  const [{ error, values }, formAction, isPending] = useActionState(signUpAction, {} as SignUpFormState);

  return (
    <form action={formAction} className="max-w-sm space-y-5">
      <Field id="displayName" label="Your name">
        <Input key={values?.displayName ?? ""} id="displayName" name="displayName" required autoComplete="name" defaultValue={values?.displayName} />
      </Field>
      <Field id="username" label="Username" hint="3 to 24 letters, numbers or underscores. Friends and leaderboards show this, never your name.">
        <Input key={values?.username ?? ""} id="username" name="username" required autoComplete="username" minLength={3} maxLength={24} pattern="[a-zA-Z0-9_]+" defaultValue={values?.username} />
      </Field>
      <Field id="email" label="Email">
        <Input key={values?.email ?? ""} id="email" name="email" type="email" required autoComplete="email" defaultValue={values?.email} />
      </Field>
      <Field id="password" label="Password" hint="At least 8 characters.">
        <Input id="password" name="password" type="password" required autoComplete="new-password" minLength={8} />
      </Field>
      <label className="flex items-center gap-3 text-sm font-medium">
        <input type="checkbox" className="check" name="ageConfirmed" value="yes" required defaultChecked={values?.ageConfirmed} />
        <span>I am {MINIMUM_AGE} or older.</span>
      </label>
      {error ? (
        <p role="alert" className="text-sm font-medium text-incorrect">
          {error}
        </p>
      ) : null}
      <div className="flex flex-wrap items-center gap-x-6 gap-y-3 pt-1">
        <Button type="submit" size="lg" disabled={isPending}>
          {isPending ? "Creating account…" : "Create account"}
        </Button>
        <Link href="/login" className="text-sm font-semibold underline underline-offset-4 hover:bg-mark hover:text-on-mark hover:no-underline">
          I already have an account
        </Link>
      </div>
    </form>
  );
}
