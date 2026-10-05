"use client";

import { useState, useSyncExternalStore } from "react";
import Link from "next/link";
import { PLAN_SECONDS_PER_QUESTION, buildStudyPlan, formatExamDate, toIsoDate } from "@/lib/study/exam-plan";

const noSubscription = () => () => {};
// False on the server and during hydration, true afterwards. "Today" is the student's
// own date, which only the browser knows, so the countdown is worked out there.
const useIsClient = () => useSyncExternalStore(noSubscription, () => true, () => false);

const plural = (n: number, word: string) => `${n} ${word}${n === 1 ? "" : "s"}`;
const oneDecimal = (n: number) => (Math.round(n * 10) / 10).toString();
const LINK = "font-semibold underline underline-offset-4 hover:bg-mark hover:text-on-mark hover:no-underline";

export function ExamCountdown({
  examDateIso,
  total,
  tried,
  newPerDay,
  cramOn,
  changeHref,
}: {
  examDateIso: string;
  total: number;
  tried: number;
  newPerDay: number;
  cramOn: boolean;
  changeHref?: string; // where to change the date, when the form isn't on this page
}) {
  const isClient = useIsClient();
  const [now] = useState(() => new Date());

  const date = <p className="eyebrow">{formatExamDate(examDateIso)}</p>;
  if (!isClient) {
    return (
      <div className="min-h-[7rem]">
        {date}
        <p className="eyebrow mt-3">Working out your plan…</p>
      </div>
    );
  }

  const plan = buildStudyPlan({ examDateIso, todayIso: toIsoDate(now, "local"), totalQuestions: total, triedQuestions: tried, newPerDayLast7: newPerDay });
  const change = changeHref ? (
    <Link href={changeHref} className={LINK}>
      Change the date
    </Link>
  ) : null;

  if (plan.kind === "passed") {
    return (
      <div>
        {date}
        <p className="reading mt-2 max-w-[56ch]">
          That date was {plural(plan.daysAgo, "day")} ago. {changeHref ? <>{change} if you are studying for another sitting.</> : "Set a new one if you are studying for another sitting."}
        </p>
      </div>
    );
  }
  if (plan.kind === "exam-day") {
    return (
      <div>
        {date}
        <p className="numeral mt-2 text-5xl">Today</p>
        <p className="reading mt-2">It is exam day.</p>
      </div>
    );
  }

  return (
    <div>
      {date}
      <div className="mt-2 flex flex-wrap items-baseline gap-x-3">
        <p className="numeral text-5xl">{plan.daysLeft}</p>
        <p className="heading text-xl">{plan.daysLeft === 1 ? "day to go" : "days to go"}</p>
      </div>

      {plan.kind === "covered" ? (
        <p className="reading mt-3 max-w-[56ch]">
          You have tried every question. Weak-spot review and Cram Mode are for firming up the ones you missed.
        </p>
      ) : (
        <div className="mt-3 max-w-[60ch] space-y-3">
          <p className="reading">
            To try every question once before then: <strong>{plural(plan.perDay, "new question")} a day</strong>, about{" "}
            <strong>{plural(plan.minutesPerDay, "minute")}</strong>.
          </p>
          <p className="reading text-[1.0625rem]">
            {plan.pace === "not-started"
              ? `You have not started yet. Begin with ${plural(plan.perDay, "question")} today.`
              : plan.pace === "on-pace"
                ? `On pace: this week you tried ${oneDecimal(plan.pacePerDay)} new questions a day.`
                : `Behind pace: this week you tried ${oneDecimal(plan.pacePerDay)} new questions a day, and ${plan.perDay} a day would finish in time.`}
          </p>
          <p className="text-sm text-muted-foreground">
            Based on the {plan.untried} questions you have not tried yet, at {PLAN_SECONDS_PER_QUESTION} seconds each to answer and read the explanation.
          </p>
          {plan.cramHint && !cramOn ? (
            <p className="text-sm font-medium">
              The last two weeks are what{" "}
              <Link href="/dashboard" className={LINK}>
                Cram Mode
              </Link>{" "}
              is for.
            </p>
          ) : null}
        </div>
      )}
      {change ? <p className="mt-3 text-sm">{change}</p> : null}
    </div>
  );
}
