"use client";

import { useState, useTransition } from "react";
import { Button } from "@/components/ui/button";

interface RemoveFriendButtonProps {
  username: string;
  action: () => Promise<unknown>;
}

// Two steps on purpose: the person who removes a friend can't undo it themselves, they would have to send a new request and be accepted again.
export function RemoveFriendButton({ username, action }: RemoveFriendButtonProps) {
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
      <Button type="button" size="sm" variant="outline" onClick={() => setConfirming(true)} aria-label={`Remove ${username} from your friends`}>
        Remove
      </Button>
    );
  }

  return (
    <div className="space-y-2">
      <p className="max-w-[40ch] text-sm">
        Remove <span className="font-mono">{username}</span> from your friends? To add them again you would send a new request.
      </p>
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
