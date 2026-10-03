"use client";

import { useState } from "react";
import Link from "next/link";
import { Button } from "@/components/ui/button";
import { Choice, ChoiceList } from "@/components/ui/choice";
import { Html } from "@/components/ui/html";
import { Sheet } from "@/components/ui/sheet";

export interface SampleChoiceView {
  label: string;
  textHtml: string;
  explanationHtml: string;
  isCorrect: boolean;
}

// The landing page's working demo of a question sheet. Local state only:
// nothing is recorded, and the copy says so.
export function SampleQuestion({
  meta,
  stemHtml,
  choices,
  explanationHtml,
}: {
  meta: string;
  stemHtml: string;
  choices: SampleChoiceView[];
  explanationHtml: string;
}) {
  const [selected, setSelected] = useState<string | null>(null);
  const [revealed, setRevealed] = useState(false);
  const picked = choices.find((c) => c.label === selected);

  function reset() {
    setSelected(null);
    setRevealed(false);
  }

  return (
    <Sheet lined>
      <p className="eyebrow">{meta}</p>
      <Html html={stemHtml} className="mt-3 text-[1.1875rem]" />

      <div className="mt-4">
        <ChoiceList legend="Answer choices">
          {choices.map((c) => (
            <Choice
              key={c.label}
              name="sample-question"
              label={c.label}
              textHtml={c.textHtml}
              explanationHtml={c.explanationHtml}
              checked={selected === c.label}
              disabled={revealed}
              revealed={revealed}
              state={revealed ? (c.isCorrect ? "correct" : selected === c.label ? "wrong" : "idle") : "idle"}
              onSelect={() => setSelected(c.label)}
            />
          ))}
        </ChoiceList>
      </div>

      {revealed ? (
        <div className="mt-5 bg-muted/60 p-4">
          <p className="eyebrow">Explanation</p>
          <Html html={explanationHtml} size="sm" className="mt-1" />
          <p className="mt-3 text-sm">
            This one isn&apos;t saved.{" "}
            <Link href="/signup" className="font-semibold underline underline-offset-4 hover:bg-mark hover:text-on-mark hover:no-underline">
              Create an account
            </Link>{" "}
            to keep your score, XP and streak.
          </p>
        </div>
      ) : null}

      <div className="mt-5 flex flex-wrap items-center justify-between gap-3">
        <p aria-live="polite" className="text-sm font-medium">
          {revealed ? (picked?.isCorrect ? "Correct." : "Not quite. Read why each choice is right or wrong.") : selected ? `Answer ${selected} selected.` : "Pick one answer."}
        </p>
        {revealed ? (
          <Button onClick={reset} variant="outline">
            Try again
          </Button>
        ) : (
          <Button onClick={() => setRevealed(true)} disabled={!selected}>
            Submit
          </Button>
        )}
      </div>
    </Sheet>
  );
}
