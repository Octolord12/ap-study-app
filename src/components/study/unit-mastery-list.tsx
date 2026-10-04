import Link from "next/link";
import { rateUnitMastery, type MasteryLevel } from "@/lib/study/mastery";
import { MasteryBar } from "@/components/ui/meter";
import { RuledList } from "@/components/ui/page";

export interface UnitMasteryRow {
  id: string;
  slug: string;
  name: string;
  total: number;
  attempted: number;
  correct: number;
}

const LEVEL_LABEL: Record<MasteryLevel, string> = {
  "not-started": "Not started",
  building: "Building",
  proficient: "Proficient",
};

// One row per unit: the bar, the score on what has been tried, and a word for
// where that puts the student. The word is text, not just a color.
export function UnitMasteryList({ courseSlug, units }: { courseSlug: string; units: UnitMasteryRow[] }) {
  return (
    <RuledList>
      {units.map((unit) => {
        const rating = rateUnitMastery(unit);
        const barLabel =
          unit.attempted === 0
            ? `${unit.name}: not started, ${unit.total} questions`
            : `${unit.name}: ${unit.correct} of ${unit.total} questions answered correctly, ${unit.attempted} tried`;

        return (
          <li key={unit.id}>
            <Link
              href={`/courses/${courseSlug}/units/${unit.slug}`}
              className="group grid gap-x-6 gap-y-2.5 py-4 sm:grid-cols-[minmax(0,1fr)_minmax(7rem,13rem)_8.5rem] sm:items-center"
            >
              <div className="min-w-0">
                <span className="text-sm font-medium decoration-2 underline-offset-4 group-hover:underline">{unit.name}</span>
                <p className="eyebrow mt-1">
                  {unit.attempted === 0 ? `${unit.total} questions` : `${unit.attempted} of ${unit.total} tried · ${unit.correct} correct`}
                </p>
              </div>
              <MasteryBar correctPercent={rating.correctPercent} coveragePercent={rating.coveragePercent} label={barLabel} />
              <p className="flex items-baseline gap-2 sm:justify-end">
                {rating.accuracyPercent !== null ? (
                  <span className="numeral text-xl">
                    {rating.accuracyPercent}%<span className="sr-only"> of the questions you tried were correct</span>
                  </span>
                ) : null}
                <span className={rating.level === "proficient" ? "eyebrow !text-correct font-semibold" : "eyebrow"}>{LEVEL_LABEL[rating.level]}</span>
              </p>
            </Link>
          </li>
        );
      })}
    </RuledList>
  );
}
