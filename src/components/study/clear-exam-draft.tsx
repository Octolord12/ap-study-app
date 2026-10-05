"use client";

import { useEffect } from "react";
import { examDraftKey } from "@/lib/study/exam-draft";

// The exam is over, so its saved answers (including free-response text) shouldn't
// linger in the browser. Rendered by the results page.
export function ClearExamDraft({ examAttemptId }: { examAttemptId: string }) {
  useEffect(() => {
    try {
      localStorage.removeItem(examDraftKey(examAttemptId));
    } catch {
      // Storage unavailable: nothing was saved there.
    }
  }, [examAttemptId]);
  return null;
}
