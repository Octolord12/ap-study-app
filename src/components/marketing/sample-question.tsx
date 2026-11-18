"use client";

import { useState } from "react";
import Link from "next/link";
import { cn } from "cn";
import type { RenderedSample } from "@/lib/marketing/render-samples";
import { Button } from "@/components/ui/button";
import { Choice, ChoiceList } from "@/components/ui/choice";
import { Html } from "@/components/ui/html";
import { Sheet } from "@/components/ui/sheet";

// The landing page's working demo: a binder with one divider tab per course, and a real question behind each.
// Local state only: nothing is recorded, and the copy says so.
export function SampleQuestion({ samples }: { samples: RenderedSample[] }) {
  const [index, setIndex] = useState(0);
  const [selected, setSelected] = useState<string | null>(null);
  const [revealed, setRevealed] = useState(false);
  const sample = samples[index];
  const picked = sample.choices.find((c) => c.label === selected);
  const next = (index + 1) % samples.length;

  function show(i: number) {
    setIndex(i);
    setSelected(null);
    setRevealed(false);
  }

  function onTabKey(event: React.KeyboardEvent<HTMLButtonElement>, i: number) {
    const step = event.key === "ArrowRight" ? 1 : event.key === "ArrowLeft" ? -1 : 0;
    if (!step) return;
    event.preventDefault();
    const to = (i + step + samples.length) % samples.length;
    show(to);
    document.getElementById(`sample-tab-${to}`)?.focus();
  }

  return (
    <div data-c={sample.accent} className="min-w-0">
      <div
        role="tablist"
        aria-label="Courses"
        className="flex items-end gap-1 overflow-x-auto pt-1.5 pr-2.5 pl-9 [scrollbar-width:none] sm:pl-11 [&::-webkit-scrollbar]:hidden"
      >
        {samples.map((s, i) => {
          const on = i === index;
          return (
            <button
              key={s.courseSlug}
              id={`sample-tab-${i}`}
              type="button"
              role="tab"
              data-c={s.accent}
              aria-selected={on}
              aria-controls="sample-panel"
              aria-label={s.course}
              tabIndex={on ? 0 : -1}
              onClick={() => show(i)}
              onKeyDown={(e) => onTabKey(e, i)}
              className={cn(
                "tab-chip shrink-0 cursor-pointer border-b-0 px-3.5 text-sm font-bold transition-[padding,min-height] duration-150 outline-offset-[-4px] hover:pt-3.5",
                on ? "min-h-12 pt-4 pb-2.5" : "min-h-9 pt-2.5 pb-2",
              )}
            >
              {s.tab}
            </button>
          );
        })}
      </div>

      <Sheet binder band stack={2} className="mr-2.5 mb-2.5 rounded-tl-none" bodyClassName="sm:p-7 sm:pl-14">
        <div id="sample-panel" role="tabpanel" aria-labelledby={`sample-tab-${index}`} key={sample.courseSlug} className="animate-in fade-in slide-in-from-bottom-1 duration-200">
          <div className="flex flex-wrap items-center gap-x-3 gap-y-2">
            <span className="plate">{sample.course}</span>
            <span className="eyebrow">{sample.unit}</span>
          </div>
          <Html html={sample.stemHtml} className="mt-4 text-[1.1875rem]" />

          <div className="mt-5">
            <ChoiceList legend="Answer choices">
              {sample.choices.map((c) => (
                <Choice
                  key={c.label}
                  name="sample-question"
                  label={c.label}
                  displayLabel={c.displayLabel}
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
            <div className="mt-5 border-t border-border pt-4">
              <p className="heading text-lg">{picked?.isCorrect ? "Correct." : "Not quite."}</p>
              <Html html={sample.explanationHtml} size="sm" className="mt-1" />
              <p className="mt-3 text-sm">
                This one isn&apos;t saved.{" "}
                <Link href="/signup" className="font-bold underline underline-offset-4 hover:bg-mark hover:text-on-mark hover:no-underline">
                  Create an account
                </Link>{" "}
                to keep your score, XP and streak.
              </p>
            </div>
          ) : null}

          <div className="mt-5 flex flex-wrap items-center gap-3">
            {revealed ? (
              <>
                <Button onClick={() => show(next)}>Try {samples[next].tab}</Button>
                <Button
                  onClick={() => {
                    setSelected(null);
                    setRevealed(false);
                  }}
                  variant="outline"
                >
                  Try again
                </Button>
              </>
            ) : (
              <Button onClick={() => setRevealed(true)} disabled={!selected}>
                Check answer
              </Button>
            )}
            <p aria-live="polite" className="text-sm font-medium text-muted-foreground">
              {revealed ? "" : selected ? `Answer ${picked?.displayLabel ?? selected} selected.` : "Pick one answer."}
            </p>
          </div>
        </div>
      </Sheet>
    </div>
  );
}
