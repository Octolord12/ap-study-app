"use client";

import { useState, useSyncExternalStore } from "react";
import { summarizeWeek, type ActivityEntry } from "@/lib/study/week-activity";
import { cn } from "cn";

const noSubscription = () => () => {};
// False on the server and during hydration, true afterwards: the week is bucketed in
// the browser's own timezone, which the server can't know, so it is drawn only there.
const useIsClient = () => useSyncExternalStore(noSubscription, () => true, () => false);

function Stat({ value, unit, label }: { value: string; unit?: string; label: string }) {
  return (
    <div>
      <p className="numeral text-4xl">
        {value}
        {unit ? <span className="ml-1 text-base font-semibold text-muted-foreground">{unit}</span> : null}
      </p>
      <p className="eyebrow mt-1">{label}</p>
    </div>
  );
}

// `forParent` only changes the wording of the empty state, which speaks to the student on their own page.
export function WeekActivity({ entries, forParent = false }: { entries: ActivityEntry[]; forParent?: boolean }) {
  const isClient = useIsClient();
  const [now] = useState(() => Date.now());

  if (!isClient) {
    return <p className="eyebrow min-h-[13rem]">Loading the week…</p>;
  }

  const week = summarizeWeek(entries, now);
  const peak = Math.max(1, ...week.days.map((d) => d.questions));

  return (
    <div>
      <dl className="grid grid-cols-2 gap-x-8 gap-y-6 sm:grid-cols-4">
        <Stat value={String(week.daysStudied)} unit="of 7" label="Days studied" />
        <Stat value={String(week.questions)} label="Questions answered" />
        <Stat value={week.accuracyPercent === null ? "–" : `${week.accuracyPercent}%`} label="Correct" />
        <Stat value={String(week.minutes)} unit="min" label="Time answering" />
      </dl>

      <ol aria-label="Questions answered each day, oldest first" className="mt-8 grid max-w-xl grid-cols-7 gap-2">
        {week.days.map((day, i) => (
          <li key={i} aria-label={`${day.label}${day.isToday ? " (today)" : ""}: ${day.questions} question${day.questions === 1 ? "" : "s"}`} className="flex flex-col items-center gap-1.5">
            <span aria-hidden className="numeral text-sm">
              {day.questions || ""}
            </span>
            <span aria-hidden className="flex h-24 w-full items-end bg-border">
              <i
                className={cn("block w-full", day.isToday ? "bg-mark border-b-2 border-foreground" : "bg-foreground")}
                style={{ height: day.questions > 0 ? `${Math.max(6, Math.round((day.questions / peak) * 100))}%` : day.active ? "3px" : "0" }}
              />
            </span>
            <span aria-hidden className={cn("eyebrow", day.isToday && "!text-foreground font-semibold")}>
              {day.label}
            </span>
          </li>
        ))}
      </ol>

      <p className="mt-5 max-w-[60ch] text-sm text-muted-foreground">
        {week.daysStudied === 0
          ? forParent
            ? "Nothing in the last 7 days."
            : "Nothing in the last 7 days yet. Answer a question and today's bar appears."
          : "Time counts the seconds spent choosing answers and the length of timed exams. Reading explanations isn't counted, so the real time is a bit more. A small mark with no number is a day with free-response work only."}
      </p>
    </div>
  );
}
