"use client";

import { useState, useTransition, type ReactNode } from "react";
import { Button } from "@/components/ui/button";

interface ConfirmRemoveButtonProps {
  label: string;
  question: ReactNode;
  action: () => Promise<unknown>;
}

// Two steps on purpose: whoever removes someone can't undo it themselves, so the first click only asks.
export function ConfirmRemoveButton({ label, question, action }: ConfirmRemoveButtonProps) {
  const [confirming, setConfirming] = useState(false);
  const [failed, setFailed] = useState(false);
  const [pending, startTransition] = useTransition();

  function remove() {
    setFailed(false);
    startTransition(async () => {
      try {
        await action();
        setConfirming(false);
      } catch {
        setFailed(true);
      }
    });
  }

  if (!confirming) {
    return (
      <Button type="button" size="sm" variant="outline" onClick={() => setConfirming(true)} aria-label={label}>
        Remove
      </Button>
    );
  }

  return (
    <div className="space-y-2">
      <p className="max-w-[40ch] text-sm">{question}</p>
      <div className="flex flex-wrap gap-2">
        <Button type="button" size="sm" onClick={remove} disabled={pending}>
          {pending ? "Removing…" : "Yes, remove"}
        </Button>
        <Button type="button" size="sm" variant="ghost" onClick={() => setConfirming(false)} disabled={pending}>
          Keep
        </Button>
      </div>
      {failed ? (
        <p role="alert" className="text-sm text-incorrect">
          Could not remove. Nothing was changed; try again.
        </p>
      ) : null}
    </div>
  );
}
