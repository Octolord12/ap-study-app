"use client";

import { useState } from "react";
import Link from "next/link";
import { motion, useReducedMotion } from "framer-motion";
import { recordAttempt, submitBossBattle } from "@/lib/study/actions";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { RewardToast, hasReward, type Reward } from "@/components/gamification/reward-toast";
import { playBossDefeatedSound, playBossHitSound } from "@/lib/gamification/sound";
import type { RenderedQuestion } from "@/components/study/quiz-runner";
import { DiagramRenderer } from "@/components/diagrams/diagram-renderer";
import { isPaperLinedCourse } from "@/lib/content/paper-lined";

const PASS_THRESHOLD = 0.7;

export function BossBattleRunner({
  unitId,
  unitName,
  courseSlug,
  unitSlug,
  questions,
}: {
  unitId: string;
  unitName: string;
  courseSlug: string;
  unitSlug: string;
  questions: RenderedQuestion[];
}) {
  const shouldReduceMotion = useReducedMotion();
  const [index, setIndex] = useState(0);
  const [selectedLabel, setSelectedLabel] = useState<string | null>(null);
  const [revealed, setRevealed] = useState(false);
  const [correctCount, setCorrectCount] = useState(0);
  const [startedAt, setStartedAt] = useState(() => Date.now());
  const [reward, setReward] = useState<Reward | null>(null);
  const [rewardKey, setRewardKey] = useState(0);
  const [battleResult, setBattleResult] = useState<{ passed: boolean } | null>(null);
  const [submitting, setSubmitting] = useState(false);

  const total = questions.length;
  const healthPct = Math.max(0, 100 - Math.round((correctCount / total) * 100));
  const question = questions[index];
  const paperLined = isPaperLinedCourse(courseSlug);
  const isLast = index === total - 1;

  async function handleAttack() {
    if (!selectedLabel) return;
    const chosen = question.choices.find((c) => c.label === selectedLabel);
    const correct = chosen?.isCorrect ?? false;

    setRevealed(true);
    if (correct) {
      setCorrectCount((c) => c + 1);
      playBossHitSound();
    }

    const result = await recordAttempt({
      questionId: question.id,
      chosenLabel: selectedLabel,
      timeSpentMs: Date.now() - startedAt,
      source: "QUIZ",
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

  async function handleNext() {
    if (!isLast) {
      setIndex((i) => i + 1);
      setSelectedLabel(null);
      setRevealed(false);
      setStartedAt(Date.now());
      return;
    }

    setSubmitting(true);
    const result = await submitBossBattle({ unitId, correctCount, total });
    setBattleResult({ passed: result.passed });
    if (result.passed) playBossDefeatedSound();
    if (result.newBadges.length > 0) {
      setReward({ xpAwarded: 0, leveledUp: false, newLevel: 0, newBadges: result.newBadges });
      setRewardKey((k) => k + 1);
    }
    setSubmitting(false);
  }

  if (battleResult) {
    return (
      <Card>
        <CardContent className="space-y-4 py-10 text-center">
          <div className="text-4xl">{battleResult.passed ? "🏆" : "💀"}</div>
          <h2 className="text-xl font-bold">
            {battleResult.passed ? `${unitName} Boss defeated!` : "The boss survives... this time"}
          </h2>
          <p className="text-sm text-muted-foreground">
            {correctCount} / {total} correct
            {!battleResult.passed ? ` -- need ${Math.ceil(total * PASS_THRESHOLD)} to win` : ""}
          </p>
          <div className="flex justify-center gap-2">
            {!battleResult.passed ? (
              <Button render={<Link href={`/courses/${courseSlug}/units/${unitSlug}/boss`} />} nativeButton={false}>
                Try again
              </Button>
            ) : null}
            <Button
              render={<Link href={`/courses/${courseSlug}/units/${unitSlug}`} />}
              nativeButton={false}
              variant="outline"
            >
              Back to unit
            </Button>
          </div>
        </CardContent>
      </Card>
    );
  }

  return (
    <div className="space-y-4">
      {reward ? <RewardToast key={rewardKey} reward={reward} onDismiss={() => setReward(null)} /> : null}

      <div>
        <div className="mb-1 flex items-center justify-between text-sm">
          <span className="font-semibold">{unitName} Boss</span>
          <span className="text-muted-foreground">{healthPct}% HP</span>
        </div>
        <div className="h-4 overflow-hidden rounded-full bg-muted">
          <motion.div
            className="h-full bg-destructive"
            initial={false}
            animate={{ width: `${healthPct}%` }}
            transition={shouldReduceMotion ? { duration: 0 } : { type: "spring", stiffness: 120, damping: 20 }}
          />
        </div>
      </div>

      <Card className={paperLined ? "paper-lined" : undefined}>
        <CardContent className="space-y-4 py-6">
          <p className="text-xs text-muted-foreground">
            Question {index + 1} of {total}
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
                  <span className="flex items-start gap-1.5">
                    <span className="font-medium">{choice.label}.</span>{" "}
                    <span
                      className="[&_p]:m-0 [&_p]:inline"
                      dangerouslySetInnerHTML={{ __html: choice.textHtml }}
                    />
                  </span>
                </button>
              );
            })}
          </div>

          <div className="flex justify-end">
            {!revealed ? (
              <Button onClick={handleAttack} disabled={!selectedLabel}>
                Attack!
              </Button>
            ) : (
              <Button onClick={handleNext} disabled={submitting}>
                {isLast ? "Finish battle" : "Next question"}
              </Button>
            )}
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
