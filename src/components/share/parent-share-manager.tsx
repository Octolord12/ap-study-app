"use client";

import { useState, useTransition } from "react";
import { Button } from "@/components/ui/button";

export interface ParentShareStatus {
  created: string;
  expires: string;
  lastViewed: string | null;
}

interface ParentShareManagerProps {
  active: ParentShareStatus | null;
  days: number;
  createAction: () => Promise<{ url: string }>;
  revokeAction: () => Promise<void>;
}

// The student's side of the parent link. The full link is shown once, right after it is made, because only its hash is stored afterwards.
export function ParentShareManager({ active, days, createAction, revokeAction }: ParentShareManagerProps) {
  const [url, setUrl] = useState<string | null>(null);
  const [copied, setCopied] = useState(false);
  const [failed, setFailed] = useState<"create" | "revoke" | null>(null);
  const [pending, startTransition] = useTransition();
  // The failure commits before the transition's pending flag clears; without this the error shows above a button that still says "Working…".
  const busy = pending && failed === null;

  function create() {
    setFailed(null);
    setCopied(false);
    startTransition(async () => {
      try {
        setUrl((await createAction()).url);
      } catch {
        setFailed("create");
      }
    });
  }

  function turnOff() {
    setFailed(null);
    startTransition(async () => {
      try {
        await revokeAction();
        setUrl(null);
      } catch {
        setFailed("revoke");
      }
    });
  }

  async function copy() {
    if (!url) return;
    try {
      await navigator.clipboard.writeText(url);
      setCopied(true);
    } catch {
      setCopied(false); // the link is also in the box, selectable by hand
    }
  }

  return (
    <div className="max-w-xl space-y-5">
      <p className="reading text-[1.0625rem]">
        Make a link that shows a parent a summary of your progress: your level and streak, the last 7 days, your weakest topics, and how you are doing in each unit.
        It shows your username, not your name or email, and none of your answers, friends or classes. It works for {days} days, or until you turn it off.
        Anyone who has the link can open it, so send it only to someone you trust.
      </p>

      {url ? (
        <div className="space-y-2" role="group" aria-label="Your new link">
          <label htmlFor="parent-link" className="eyebrow block">
            Your link (shown only now)
          </label>
          <div className="flex flex-wrap gap-2">
            <input id="parent-link" readOnly value={url} onFocus={(e) => e.currentTarget.select()} className="min-w-0 flex-1 border border-border bg-card px-3 py-2 font-mono text-sm" />
            <Button type="button" variant="outline" onClick={copy}>
              {copied ? "Copied" : "Copy"}
            </Button>
          </div>
          <p className="text-sm text-muted-foreground">Copy it now. If you lose it, make a new one; the old one then stops working.</p>
        </div>
      ) : null}

      {active ? (
        <p className="text-sm" role="status">
          A link is on. Made {active.created}, works until {active.expires}. {active.lastViewed ? `Last opened ${active.lastViewed}.` : "Not opened yet."}
        </p>
      ) : (
        <p className="text-sm text-muted-foreground" role="status">
          No link is on.
        </p>
      )}

      <div className="flex flex-wrap gap-2">
        <Button type="button" onClick={create} disabled={busy}>
          {busy ? "Working…" : active ? "Make a new link" : "Make a link"}
        </Button>
        {active ? (
          <Button type="button" variant="outline" onClick={turnOff} disabled={busy}>
            Turn off
          </Button>
        ) : null}
      </div>
      {active ? <p className="text-sm text-muted-foreground">Making a new link turns the old one off.</p> : null}

      {failed ? (
        <p role="alert" className="text-sm font-medium text-incorrect">
          {failed === "create" ? "Could not make a link. Nothing was changed; try again." : "Could not turn the link off. Try again."}
        </p>
      ) : null}
    </div>
  );
}
