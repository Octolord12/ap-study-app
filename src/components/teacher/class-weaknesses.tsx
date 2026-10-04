import type { ClassWeakness } from "@/lib/teacher/types";
import { RuledList } from "@/components/ui/page";

// Takes its rows as a prop so the aggregation can be added later without
// touching this component. Until then the caller passes none and this shows
// its empty state: no invented numbers.
export function ClassWeaknesses({ items }: { items: ClassWeakness[] }) {
  if (items.length === 0) {
    return (
      <div className="max-w-[60ch]">
        <p className="reading">
          Not built yet. This panel will list the units your class misses most, with how many students are below proficient in each.
        </p>
        <div aria-hidden className="mt-4 grid grid-cols-[minmax(0,1fr)_5.5rem_10rem] gap-x-4 border-y border-dashed border-border py-2">
          <span className="eyebrow">Unit</span>
          <span className="eyebrow text-right">Accuracy</span>
          <span className="eyebrow text-right">Below proficient</span>
        </div>
        <p className="eyebrow mt-3">No data yet</p>
      </div>
    );
  }

  return (
    <RuledList>
      {items.map((w) => (
        <li key={w.unitId} className="grid grid-cols-[minmax(0,1fr)_5.5rem_10rem] items-baseline gap-x-4 py-3">
          <span className="text-sm font-medium">{w.unitName}</span>
          <span className="numeral text-right text-lg">{w.classAccuracyPercent}%</span>
          <span className="eyebrow text-right">
            {w.studentsBelowProficient} of {w.studentsTried}
          </span>
        </li>
      ))}
    </RuledList>
  );
}
