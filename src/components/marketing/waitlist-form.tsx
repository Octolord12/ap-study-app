"use client";

import { useActionState } from "react";
import { joinWaitlist } from "@/lib/marketing/actions";
import { WAITLIST_IDLE } from "@/lib/marketing/waitlist";
import { Button } from "@/components/ui/button";
import { Field } from "@/components/ui/field";
import { Input } from "@/components/ui/input";
import { MINIMUM_AGE } from "@/lib/age";

export function WaitlistForm() {
  const [state, formAction, isPending] = useActionState(joinWaitlist, WAITLIST_IDLE);

  if (state.status === "done") {
    return (
      <p role="status" className="reading max-w-[52ch]">
        <span className="hl font-semibold">You&apos;re on the list.</span> We&apos;ll email you once, when a new subject is ready.
      </p>
    );
  }

  return (
    <form action={formAction} className="max-w-md space-y-3">
      <div className="flex flex-wrap items-end gap-3">
        <Field
          id="waitlist-email"
          label="Email"
          hint={`One email when a new subject launches. Nothing else. You must be ${MINIMUM_AGE} or older.`}
          error={state.status === "error" ? state.message : undefined}
          className="min-w-56 flex-1"
        >
          <Input id="waitlist-email" name="email" type="email" required autoComplete="email" maxLength={254} />
        </Field>
        <Button type="submit" size="lg" disabled={isPending}>
          {isPending ? "Joining…" : "Join the list"}
        </Button>
      </div>
      <div aria-hidden className="absolute -left-[9999px] h-0 w-0 overflow-hidden">
        <label>
          Leave this empty
          <input type="text" name="website" tabIndex={-1} autoComplete="off" />
        </label>
      </div>
    </form>
  );
}
