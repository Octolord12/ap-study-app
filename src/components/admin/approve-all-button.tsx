"use client";

import { useState, useTransition } from "react";
import { Button } from "@/components/ui/button";

interface ApproveAllButtonProps {
  count: number;
  action: () => Promise<unknown>;
}

// Two steps on purpose: approving marks content as checked by a person, which the About page then claims.
export function ApproveAllButton({ count, action }: ApproveAllButtonProps) {
  const [confirming, setConfirming] = useState(false);
  const [failed, setFailed] = useState(false);
  const [pending, startTransition] = useTransition();
  // The failure state commits before the transition's pending flag clears; without this the error shows for a moment above a button
  // that still says "Approving…" and is disabled.
  const busy = pending && !failed;

  function approve() {
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
      <Button type="button" variant="outline" onClick={() => setConfirming(true)}>
        Approve all {count} in this unit
      </Button>
    );
  }

  return (
    <div className="space-y-3">
      <p className="reading max-w-[56ch]">
        Mark all {count} item{count === 1 ? "" : "s"} below as checked by a person? The About page counts them as reviewed.
      </p>
      <div className="flex flex-wrap gap-2">
        <Button type="button" onClick={approve} disabled={busy}>
          {busy ? "Approving…" : `Yes, approve all ${count}`}
        </Button>
        <Button type="button" variant="ghost" onClick={() => setConfirming(false)} disabled={busy}>
          Cancel
        </Button>
      </div>
      {failed ? (
        <p role="alert" className="text-sm text-incorrect">
          Could not approve. Nothing was changed; try again.
        </p>
      ) : null}
    </div>
  );
}
