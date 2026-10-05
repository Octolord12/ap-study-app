"use client";

import { useActionState } from "react";
import { setExamDate } from "@/lib/study/exam-date-actions";
import type { ExamDateState } from "@/lib/study/exam-plan";
import { Button } from "@/components/ui/button";
import { Field } from "@/components/ui/field";
import { Input } from "@/components/ui/input";

export function ExamDateForm({ courseId, currentIso }: { courseId: string; currentIso: string | null }) {
  const [state, formAction, isPending] = useActionState(setExamDate.bind(null, courseId), {} as ExamDateState);

  return (
    <div className="space-y-3">
      <form action={formAction} className="flex flex-wrap items-end gap-3">
        <Field id={`exam-date-${courseId}`} label="Exam date" hint="Your school or the College Board's AP schedule has it." error={state.error}>
          {/* Keyed by the saved date: a changed default on a mounted Base UI input logs a warning. */}
          <Input key={currentIso ?? "none"} id={`exam-date-${courseId}`} name="examDate" type="date" required defaultValue={currentIso ?? ""} className="w-auto" />
        </Field>
        <Button type="submit" size="lg" disabled={isPending}>
          {isPending ? "Saving…" : currentIso ? "Change date" : "Save date"}
        </Button>
      </form>
      {currentIso ? (
        <form action={formAction}>
          <input type="hidden" name="intent" value="clear" />
          <Button type="submit" variant="outline" size="sm" disabled={isPending}>
            Remove date
          </Button>
        </form>
      ) : null}
      {state.message ? (
        <p role="status" className="text-sm font-medium">
          {state.message}
        </p>
      ) : null}
    </div>
  );
}
