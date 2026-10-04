import Link from "next/link";
import type { OwnedClass } from "@/lib/teacher/types";
import { RuledList } from "@/components/ui/page";

export function ClassPicker({ classes, selectedId }: { classes: OwnedClass[]; selectedId: string }) {
  return (
    <RuledList className="max-w-xl">
      {classes.map((c) => {
        const selected = c.id === selectedId;
        return (
          <li key={c.id}>
            <Link
              href={`/teacher?class=${c.id}`}
              aria-current={selected ? "true" : undefined}
              className={`flex items-baseline justify-between gap-4 py-3 ${selected ? "bg-mark px-2 text-on-mark" : "px-2 hover:bg-muted"}`}
            >
              <span className="heading text-lg">{c.name}</span>
              <span className="eyebrow !text-current">
                {c.memberCount} member{c.memberCount === 1 ? "" : "s"}
              </span>
            </Link>
          </li>
        );
      })}
    </RuledList>
  );
}
