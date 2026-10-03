"use client";

import { useState } from "react";
import dynamic from "next/dynamic";
import { submitFrqAttempt, updateFrqGrade } from "@/lib/study/actions";
import { Button } from "@/components/ui/button";
import { Textarea } from "@/components/ui/textarea";
import { hasReward, type Reward } from "@/components/gamification/reward-toast";

// framer-motion (RewardToast's only real dependency beyond React) is
// dead weight on every FRQ practice page load until a reward actually
// fires -- deferred here instead of bundled into this much more common
// code path.
const RewardToast = dynamic(
  () => import("@/components/gamification/reward-toast").then((m) => m.RewardToast),
  { ssr: false },
);

export interface RubricLineView {
  id: string;
  points: number;
  description: string;
  descriptionHtml: string;
}

interface FrqSelfGradeProps {
  frqPromptId: string;
  pointValue: number;
  rubric: RubricLineView[];
  sampleResponseHtml: string;
  /** Set when the response was already written elsewhere (the exam flow) -- makes the textarea read-only. */
  existingResponseText?: string;
  /** Set alongside existingResponseText: grades that attempt in place instead of creating a new one. */
  existingAttemptId?: string;
  onGraded?: (result: { pointsAwarded: number; maxPoints: number }) => void;
  /**
   * Wraps this component's own root in the paper-lined card chrome (border,
   * padding, notebook background). Only pass this when the caller ISN'T
   * already nesting this component inside its own paper-lined container
   * (e.g. the exam results page shares one Card with the prompt above it) --
   * two paper-lined boxes nested inside each other makes the ruled lines
   * visibly discontinuous where the inner box's background restarts.
   */
  paperLined?: boolean;
}

export function FrqSelfGrade({
  frqPromptId,
  pointValue,
  rubric,
  sampleResponseHtml,
  existingResponseText,
  existingAttemptId,
  onGraded,
  paperLined = false,
}: FrqSelfGradeProps) {
  const [responseText, setResponseText] = useState(existingResponseText ?? "");
  const [revealed, setRevealed] = useState(false);
  const [checkedLineIds, setCheckedLineIds] = useState<Set<string>>(new Set());
  const [saved, setSaved] = useState<{ pointsAwarded: number; maxPoints: number } | null>(null);
  const [reward, setReward] = useState<Reward | null>(null);
  const readOnlyResponse = existingResponseText !== undefined;

  const pointsSoFar = rubric.filter((line) => checkedLineIds.has(line.id)).reduce((sum, line) => sum + line.points, 0);

  function toggleLine(lineId: string) {
    setCheckedLineIds((prev) => {
      const next = new Set(prev);
      if (next.has(lineId)) next.delete(lineId);
      else next.add(lineId);
      return next;
    });
  }

  async function handleSave() {
    const result = existingAttemptId
      ? await updateFrqGrade({ frqAttemptId: existingAttemptId, checkedLineIds: Array.from(checkedLineIds) })
      : await submitFrqAttempt({ frqPromptId, responseText, checkedLineIds: Array.from(checkedLineIds) });
    setSaved(result);
    onGraded?.(result);

    const nextReward: Reward = {
      xpAwarded: result.xpAwarded,
      leveledUp: result.leveledUp,
      newLevel: result.newLevel,
      newBadges: result.newBadges,
    };
    if (hasReward(nextReward)) setReward(nextReward);
  }

  return (
    <div className={paperLined ? "paper-lined space-y-4 rounded-lg border border-border p-6" : "space-y-4"}>
      {reward ? <RewardToast reward={reward} onDismiss={() => setReward(null)} /> : null}
      {readOnlyResponse ? (
        <div className="rounded-lg border border-border bg-muted p-4 text-sm whitespace-pre-wrap">
          {responseText || <span className="text-muted-foreground">(no response written)</span>}
        </div>
      ) : (
        <Textarea
          value={responseText}
          onChange={(e) => setResponseText(e.target.value)}
          disabled={revealed}
          placeholder="Write your response..."
          rows={8}
        />
      )}

      {!revealed ? (
        <Button onClick={() => setRevealed(true)} disabled={!readOnlyResponse && responseText.trim().length === 0}>
          Reveal rubric &amp; sample response
        </Button>
      ) : (
        <div className="space-y-4">
          <div>
            <p className="mb-2 text-xs font-semibold uppercase tracking-wide text-muted-foreground">
              Rubric ({pointValue} point{pointValue === 1 ? "" : "s"} total) -- check what your response did
            </p>
            <div className="space-y-2">
              {rubric.map((line) => (
                <label key={line.id} className="flex items-start gap-2 text-sm">
                  <input
                    type="checkbox"
                    className="mt-0.5"
                    checked={checkedLineIds.has(line.id)}
                    onChange={() => toggleLine(line.id)}
                    disabled={saved !== null}
                  />
                  <span>
                    <span className="font-medium">({line.points} pt{line.points === 1 ? "" : "s"})</span>{" "}
                    <span className="[&_p]:m-0 [&_p]:inline" dangerouslySetInnerHTML={{ __html: line.descriptionHtml }} />
                  </span>
                </label>
              ))}
            </div>
          </div>

          <div>
            <p className="mb-2 text-xs font-semibold uppercase tracking-wide text-muted-foreground">Sample response</p>
            <div
              className="prose prose-sm prose-neutral dark:prose-invert max-w-none rounded-lg border border-border p-4"
              dangerouslySetInnerHTML={{ __html: sampleResponseHtml }}
            />
          </div>

          <div className="flex items-center gap-3">
            {saved === null ? (
              <Button onClick={handleSave}>Save my grade ({pointsSoFar} pts so far)</Button>
            ) : (
              <p className="text-sm font-medium">
                Saved: {saved.pointsAwarded} / {saved.maxPoints} points
              </p>
            )}
          </div>
        </div>
      )}
    </div>
  );
}
