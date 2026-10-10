"use client";

import { useState, useTransition, type ReactNode } from "react";
import { Button } from "@/components/ui/button";

interface TwoStepButtonProps {
  label: string;
  question: ReactNode;
  action: () => Promise<unknown>;
  // The wording defaults to a removal's; a different action passes its own.
  trigger?: string;
  confirm?: string;
  working?: string;
  failure?: string;
  // A second, different way to confirm (e.g. "Remove and block"), shown beside the first.
  alternate?: { confirm: string; working: string; action: () => Promise<unknown> };
}

// Two steps on purpose: what this does can't be undone by the person who clicks it, so the first click only asks.
export function TwoStepButton({
  label,
  question,
  action,
  trigger = "Remove",
  confirm = "Yes, remove",
  working = "Removing…",
  failure = "Could not remove. Nothing was changed; try again.",
  alternate,
}: TwoStepButtonProps) {
  const [confirming, setConfirming] = useState(false);
  const [failed, setFailed] = useState(false);
  const [running, setRunning] = useState<"primary" | "alternate">("primary");
  const [pending, startTransition] = useTransition();
  // The failure state commits before the transition's pending flag clears; without this the error shows for a moment above a button
  // that still shows the working label and is disabled.
  const busy = pending && !failed;

  function run(which: "primary" | "alternate") {
    setFailed(false);
    setRunning(which);
    startTransition(async () => {
      try {
        await (which === "alternate" && alternate ? alternate.action : action)();
        setConfirming(false);
      } catch {
        setFailed(true);
      }
    });
  }

  if (!confirming) {
    return (
      <Button type="button" size="sm" variant="outline" onClick={() => setConfirming(true)} aria-label={label}>
        {trigger}
      </Button>
    );
  }

  return (
    <div className="space-y-2">
      <p className="max-w-[40ch] text-sm">{question}</p>
      <div className="flex flex-wrap gap-2">
        <Button type="button" size="sm" onClick={() => run("primary")} disabled={busy}>
          {busy && running === "primary" ? working : confirm}
        </Button>
        {alternate ? (
          <Button type="button" size="sm" onClick={() => run("alternate")} disabled={busy}>
            {busy && running === "alternate" ? alternate.working : alternate.confirm}
          </Button>
        ) : null}
        <Button type="button" size="sm" variant="ghost" onClick={() => setConfirming(false)} disabled={busy}>
          Keep
        </Button>
      </div>
      {failed ? (
        <p role="alert" className="text-sm text-incorrect">
          {failure}
        </p>
      ) : null}
    </div>
  );
}
