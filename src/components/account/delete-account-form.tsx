"use client";

import { useActionState } from "react";
import { deleteAccountAction } from "@/lib/auth/account-actions";
import type { DeleteAccountFormState } from "@/lib/auth/schema";
import { Button } from "@/components/ui/button";
import { Field } from "@/components/ui/field";
import { Input } from "@/components/ui/input";

export interface OwnedClass {
  id: string;
  name: string;
  otherMembers: number;
}

export function DeleteAccountForm({ ownedClasses }: { ownedClasses: OwnedClass[] }) {
  const [state, formAction, isPending] = useActionState(deleteAccountAction, {} as DeleteAccountFormState);
  const one = ownedClasses.length === 1;
  const others = ownedClasses.reduce((n, c) => n + c.otherMembers, 0);
  const them = one ? "it" : "them";
  const classWarning =
    `You own ${one ? "a class" : `${ownedClasses.length} classes`} (${ownedClasses.map((c) => c.name).join(", ")}). Classes can't be handed over, so deleting your account deletes ${them}` +
    (others > 0 ? ` for everyone in ${them}: ${others} other ${others === 1 ? "student" : "students"}.` : `, though nobody else is in ${them}.`);

  return (
    <form action={formAction} className="max-w-md space-y-5">
      <div className="reading space-y-2 text-[1.0625rem]">
        <p>Deleting your account removes:</p>
        <ul className="list-disc space-y-1 pl-6">
          <li>your account, name, username and email</li>
          <li>your answers, XP, streak, badges and titles, exams and free-response work</li>
          <li>your friends, and your place in any class you joined</li>
          <li>your waitlist signup, if you used the same email</li>
        </ul>
        <p className="font-semibold">This can&apos;t be undone.</p>
      </div>

      {ownedClasses.length > 0 ? (
        <div role="note" className="border-2 border-foreground p-3 text-sm font-medium">
          {classWarning}
        </div>
      ) : null}

      <Field id="deletePassword" label="Your password" hint="To be sure it is you.">
        <Input id="deletePassword" name="password" type="password" required autoComplete="current-password" />
      </Field>
      <label className="flex items-start gap-3 text-sm font-medium">
        <input type="checkbox" className="check mt-0.5" name="understand" value="yes" required />
        <span>I understand my account and its data will be deleted for good.</span>
      </label>
      {state.error ? (
        <p role="alert" className="text-sm font-medium text-incorrect">
          {state.error}
        </p>
      ) : null}
      <Button type="submit" variant="destructive" size="lg" disabled={isPending}>
        {isPending ? "Deleting…" : "Delete my account"}
      </Button>
    </form>
  );
}
