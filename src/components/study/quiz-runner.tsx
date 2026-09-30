"use client";

import { useState } from "react";
import Link from "next/link";
import dynamic from "next/dynamic";
import { recordAttempt } from "@/lib/study/actions";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { hasReward, type Reward } from "@/components/gamification/reward-toast";

// framer-motion (RewardToast's only real dependency beyond React) is
// dead weight on every quiz page load until a reward actually fires --
// deferred here instead of bundled into this much more common code path.
const RewardToast = dynamic(
  () => import("@/components/gamification/reward-toast").then((m) => m.RewardToast),
  { ssr: false },
);
import type { AttemptSource } from "@/generated/prisma/client";
import { DiagramRenderer } from "@/components/diagrams/diagram-renderer";
import type { Diagram } from "@/lib/content/diagram-schema";

export interface RenderedChoice {
  id: string;
  label: string;
  text: string;
  isCorrect: boolean;
  explanationHtml: string;
}

export interface RenderedQuestion {
  id: string;
  difficulty: "EASY" | "MEDIUM" | "HARD";
  stemHtml: string;
  explanationHtml: string;
  diagram: Diagram | null;
  conceptHref: string;
  choices: RenderedChoice[];
}

export function QuizRunner({
  questions,
  backHref,
  backLabel,
  source = "PRACTICE",
}: {
  questions: RenderedQuestion[];
  backHref: string;
  backLabel: string;
  source?: AttemptSource;
}) {
  const [index, setIndex] = useState(0);
  const [selectedLabel, setSelectedLabel] = useState<string | null>(null);
  const [revealed, setRevealed] = useState(false);
  const [results, setResults] = useState<{ questionId: string; correct: boolean }[]>([]);
  const [startedAt, setStartedAt] = useState(() => Date.now());
  const [reward, setReward] = useState<Reward | null>(null);
  const [rewardKey, setRewardKey] = useState(0);
  // Deliberately not derived from results.length === questions.length: that
  // would go true the instant the last answer is recorded, before the
  // student has seen its reveal/explanation. finished is set explicitly by
  // handleNext, only after they've clicked past the last question.
  const [finished, setFinished] = useState(false);

  if (finished) {
    const correctCount = results.filter((r) => r.correct).length;
    return (
      <>
        {reward ? <RewardToast key={rewardKey} reward={reward} onDismiss={() => setReward(null)} /> : null}
        <Card>
        <CardContent className="space-y-4 py-10 text-center">
          <h2 className="text-xl font-bold">
            {correctCount} / {questions.length} correct
          </h2>
          <Button render={<Link href={backHref} />} nativeButton={false}>
            {backLabel}
          </Button>
        </CardContent>
        </Card>
      </>
    );
  }

  const question = questions[index];
  const isLast = index === questions.length - 1;

  async function handleSubmit() {
    if (!selectedLabel) return;
    const chosen = question.choices.find((c) => c.label === selectedLabel);
    const correct = chosen?.isCorrect ?? false;

    setResults((prev) => [...prev, { questionId: question.id, correct }]);
    setRevealed(true);

    // The reveal above already happened using the (already fetched, trusted)
    // choice data -- this call is purely for the persisted attempt log and
    // whatever XP/streak/badges the server decides it earned, which we await
    // only to show the reward toast, not to gate the reveal.
    const result = await recordAttempt({
      questionId: question.id,
      chosenLabel: selectedLabel,
      timeSpentMs: Date.now() - startedAt,
      source,
    });
    const nextReward: Reward = {
      xpAwarded: result.xpAwarded,
      leveledUp: result.leveledUp,
      newLevel: result.newLevel,
      newBadges: result.newBadges,
    };
    if (hasReward(nextReward)) {
      setReward(nextReward);
      setRewardKey((k) => k + 1);
    }
  }

  function handleNext() {
    if (isLast) {
      setFinished(true);
      return;
    }
    setIndex((i) => i + 1);
    setSelectedLabel(null);
    setRevealed(false);
    setStartedAt(Date.now());
  }

  return (
    <>
      {reward ? <RewardToast key={rewardKey} reward={reward} onDismiss={() => setReward(null)} /> : null}
      <Card>
      <CardContent className="space-y-4 py-6">
        <p className="text-xs text-muted-foreground">
          Question {index + 1} of {questions.length} ·{" "}
          <span className="capitalize">{question.difficulty.toLowerCase()}</span>
        </p>
        <div
          className="prose prose-neutral dark:prose-invert max-w-none"
          dangerouslySetInnerHTML={{ __html: question.stemHtml }}
        />
        {question.diagram && <DiagramRenderer diagram={question.diagram} />}

        <div className="space-y-2">
          {question.choices.map((choice) => {
            const isSelected = selectedLabel === choice.label;
            const correctHighlight = revealed && choice.isCorrect;
            const wrongHighlight = revealed && isSelected && !choice.isCorrect;

            return (
              <button
                key={choice.id}
                type="button"
                disabled={revealed}
                onClick={() => setSelectedLabel(choice.label)}
                className={[
                  "w-full rounded-lg border px-4 py-2 text-left text-sm transition-colors disabled:cursor-default",
                  isSelected && !revealed ? "border-foreground" : "border-border",
                  correctHighlight ? "border-green-600 bg-green-50 dark:bg-green-950" : "",
                  wrongHighlight ? "border-destructive bg-red-50 dark:bg-red-950" : "",
                ].join(" ")}
              >
                <span className="font-medium">{choice.label}.</span> {choice.text}
                {revealed ? (
                  <div
                    className="prose prose-sm prose-neutral dark:prose-invert mt-2 max-w-none"
                    dangerouslySetInnerHTML={{ __html: choice.explanationHtml }}
                  />
                ) : null}
              </button>
            );
          })}
        </div>

        {revealed ? (
          <div className="rounded-lg bg-muted p-4">
            <p className="mb-1 text-xs font-semibold uppercase tracking-wide text-muted-foreground">Explanation</p>
            <div
              className="prose prose-sm prose-neutral dark:prose-invert max-w-none"
              dangerouslySetInnerHTML={{ __html: question.explanationHtml }}
            />
            <Link href={question.conceptHref} className="mt-2 inline-block text-xs font-medium underline underline-offset-4">
              Review this concept
            </Link>
          </div>
        ) : null}

        <div className="flex justify-end">
          {!revealed ? (
            <Button onClick={handleSubmit} disabled={!selectedLabel}>
              Submit
            </Button>
          ) : (
            <Button onClick={handleNext}>{isLast ? "See results" : "Next question"}</Button>
          )}
        </div>
      </CardContent>
      </Card>
    </>
  );
}
