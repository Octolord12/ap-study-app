import Link from "next/link";
import type { ExamWeakUnit } from "@/lib/study/exam-breakdown";
import { RuledList } from "@/components/ui/page";

const MAX_QUIZ_QUESTIONS = 20;

// Where the multiple-choice points went, each with a quiz of exactly the questions missed.
export function ExamWeakUnits({ units, courseSlug, backHref }: { units: ExamWeakUnit[]; courseSlug: string; backHref: string }) {
  if (units.length === 0) {
    return <p className="reading max-w-[52ch]">You got every multiple-choice question right.</p>;
  }
  return (
    <RuledList>
      {units.map((u) => {
        const ids = u.missedIds.slice(0, MAX_QUIZ_QUESTIONS);
        const params = new URLSearchParams({ ids: ids.join(","), source: "PRACTICE", back: backHref, backLabel: "Back to results" });
        return (
          <li key={u.unitSlug} className="flex flex-wrap items-center justify-between gap-x-6 gap-y-2 py-4">
            <div className="min-w-0">
              <p className="heading text-lg">{u.unitName}</p>
              <p className="eyebrow mt-1">
                {u.missed} of {u.total} missed or skipped
              </p>
            </div>
            <Link
              href={`/courses/${courseSlug}/quiz?${params.toString()}`}
              className="text-sm font-semibold underline underline-offset-4 hover:bg-mark hover:text-on-mark hover:no-underline"
            >
              Practice the {ids.length} you missed
            </Link>
          </li>
        );
      })}
    </RuledList>
  );
}
