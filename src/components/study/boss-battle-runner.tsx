"use client";

import { useState } from "react";
import Link from "next/link";
import { motion, useReducedMotion } from "framer-motion";
import { recordAttempt, submitBossBattle } from "@/lib/study/actions";
import { Button } from "@/components/ui/button";
import { Choice, ChoiceList } from "@/components/ui/choice";
import { Html } from "@/components/ui/html";
import { Sheet } from "@/components/ui/sheet";
import { BadgeStamp } from "@/components/ui/stamp";
import { QuizProgress } from "@/components/study/quiz-progress";
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
      <div className="border-t-2 border-foreground pt-6">
        <p className="eyebrow">{unitName}</p>
        <div className="mt-3 flex items-center gap-5">
          {battleResult.passed ? <BadgeStamp slug="boss_slayer" className="size-20 shrink-0" /> : null}
          <h2 className="display text-[clamp(2.5rem,8vw,4.5rem)]">
            {battleResult.passed ? "Boss defeated." : "The boss survives. This time."}
          </h2>
        </div>
        <p className="numeral mt-6 text-5xl">
          {correctCount} / {total}
        </p>
        <p className="reading mt-1 text-lg">
          correct{!battleResult.passed ? `. You need ${Math.ceil(total * PASS_THRESHOLD)} to win.` : "."}
        </p>
        <div className="mt-8 flex flex-wrap gap-3">
          {!battleResult.passed ? (
            <Button render={<Link href={`/courses/${courseSlug}/units/${unitSlug}/boss`} />} nativeButton={false} size="lg">
              Try again
            </Button>
          ) : null}
          <Button
            render={<Link href={`/courses/${courseSlug}/units/${unitSlug}`} />}
            nativeButton={false}
            variant={battleResult.passed ? "default" : "outline"}
            size="lg"
          >
            Back to unit
          </Button>
        </div>
      </div>
    );
  }

  return (
    <div className="grid gap-x-10 gap-y-3 md:grid-cols-[10.5rem_minmax(0,1fr)]">
      {reward ? <RewardToast key={rewardKey} reward={reward} onDismiss={() => setReward(null)} /> : null}

      <div className="space-y-3 md:pt-1">
        <p className="eyebrow !text-foreground">
          Question {index + 1} of {total}
        </p>
        <QuizProgress total={total} current={index} className="hidden md:flex" />
        <Link
          href={`/courses/${courseSlug}/units/${unitSlug}`}
          className="eyebrow hidden underline underline-offset-4 hover:bg-mark hover:text-on-mark hover:no-underline md:inline-block"
        >
          Leave battle
        </Link>
      </div>

      <div className="min-w-0 space-y-4">
        <div>
          <div className="mb-1.5 flex items-baseline justify-between gap-4">
            <p className="heading text-lg">{unitName} boss</p>
            <p className="eyebrow !text-foreground tabular-nums">{healthPct}% HP</p>
          </div>
          <div
            role="progressbar"
            aria-label="Boss health"
            aria-valuemin={0}
            aria-valuemax={100}
            aria-valuenow={healthPct}
            className="h-4 overflow-hidden border-2 border-foreground bg-card"
          >
            <motion.div
              className="h-full bg-incorrect"
              initial={false}
              animate={{ width: `${healthPct}%` }}
              transition={shouldReduceMotion ? { duration: 0 } : { type: "spring", stiffness: 120, damping: 20 }}
            />
          </div>
        </div>

        <Sheet lined={paperLined}>
          <Html html={question.stemHtml} className="text-[1.1875rem]" />
          {question.diagram && <DiagramRenderer diagram={question.diagram} />}

          <div className="mt-5">
            <ChoiceList legend="Answer choices">
              {question.choices.map((choice) => (
                <Choice
                  key={choice.id}
                  name={`boss-question-${question.id}`}
                  label={choice.label}
                  textHtml={choice.textHtml}
                  checked={selectedLabel === choice.label}
                  disabled={revealed}
                  revealed={revealed}
                  state={revealed ? (choice.isCorrect ? "correct" : selectedLabel === choice.label ? "wrong" : "idle") : "idle"}
                  onSelect={() => setSelectedLabel(choice.label)}
                />
              ))}
            </ChoiceList>
          </div>

          <div className="mt-6 flex justify-end">
            {!revealed ? (
              <Button onClick={handleAttack} disabled={!selectedLabel} size="lg">
                Attack
              </Button>
            ) : (
              <Button onClick={handleNext} disabled={submitting} size="lg">
                {isLast ? "Finish battle" : "Next question"}
              </Button>
            )}
          </div>
        </Sheet>
      </div>
    </div>
  );
}
