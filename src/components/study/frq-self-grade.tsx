"use client";

import { useState } from "react";
import dynamic from "next/dynamic";
import { submitFrqAttempt, updateFrqGrade } from "@/lib/study/actions";
import { Button } from "@/components/ui/button";
import { Html } from "@/components/ui/html";
import { Label } from "@/components/ui/label";
import { Sheet } from "@/components/ui/sheet";
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

  const content = (
    <div className="space-y-6">
      {reward ? <RewardToast reward={reward} onDismiss={() => setReward(null)} /> : null}
      {readOnlyResponse ? (
        <div>
          <p className="eyebrow !text-current">Your response</p>
          <div className="mt-2 border border-current/30 bg-muted/50 p-4 text-sm leading-relaxed whitespace-pre-wrap text-foreground">
            {responseText || <span className="text-muted-foreground">(no response written)</span>}
          </div>
        </div>
      ) : (
        <div className="space-y-1.5">
          <Label htmlFor={`frq-response-${frqPromptId}`}>Your response</Label>
          <Textarea
            id={`frq-response-${frqPromptId}`}
            value={responseText}
            onChange={(e) => setResponseText(e.target.value)}
            disabled={revealed}
            placeholder="Write your response here."
            rows={8}
          />
        </div>
      )}

      {!revealed ? (
        <Button size="lg" onClick={() => setRevealed(true)} disabled={!readOnlyResponse && responseText.trim().length === 0}>
          Reveal rubric and sample response
        </Button>
      ) : (
        <div className="space-y-6">
          <div>
            <p className="eyebrow !text-current">
              Rubric · {pointValue} point{pointValue === 1 ? "" : "s"} total
            </p>
            <p className="mt-1 text-sm">Check each line your response earned.</p>
            <ul className="mt-3 border-b border-current/25 [&>li]:border-t [&>li]:border-current/25">
              {rubric.map((line) => (
                <li key={line.id}>
                  <label className="flex cursor-pointer items-start gap-3 py-3 text-sm">
                    <input
                      type="checkbox"
                      className="check mt-0.5"
                      checked={checkedLineIds.has(line.id)}
                      onChange={() => toggleLine(line.id)}
                      disabled={saved !== null}
                    />
                    <span className="min-w-0">
                      <span className="font-semibold tabular-nums">
                        {line.points} pt{line.points === 1 ? "" : "s"}
                      </span>{" "}
                      <Html html={line.descriptionHtml} inline size="sm" className="inline" />
                    </span>
                  </label>
                </li>
              ))}
            </ul>
          </div>

          <div className="border-t-2 border-current pt-4">
            <p className="eyebrow !text-current">Sample response</p>
            <Html html={sampleResponseHtml} size="sm" className="mt-2" />
          </div>

          <div className="flex flex-wrap items-center gap-4">
            {saved === null ? (
              <Button size="lg" onClick={handleSave}>
                Save my grade ({pointsSoFar} {pointsSoFar === 1 ? "pt" : "pts"} so far)
              </Button>
            ) : (
              <p className="flex items-baseline gap-3">
                <span className="numeral text-4xl">
                  {saved.pointsAwarded} / {saved.maxPoints}
                </span>
                <span className="text-sm font-semibold">points saved</span>
              </p>
            )}
          </div>
        </div>
      )}
    </div>
  );

  return paperLined ? <Sheet lined>{content}</Sheet> : content;
}
