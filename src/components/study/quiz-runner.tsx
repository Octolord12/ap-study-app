"use client";

import { useState } from "react";
import Link from "next/link";
import dynamic from "next/dynamic";
import { recordAttempt } from "@/lib/study/actions";
import { Button } from "@/components/ui/button";
import { Choice, ChoiceList } from "@/components/ui/choice";
import { Html } from "@/components/ui/html";
import { Sheet } from "@/components/ui/sheet";
import { hasReward, type Reward } from "@/components/gamification/reward-toast";
import { QuizProgress } from "@/components/study/quiz-progress";

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
  textHtml: string;
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
  paperLined = false,
}: {
  questions: RenderedQuestion[];
  backHref: string;
  backLabel: string;
  source?: AttemptSource;
  paperLined?: boolean;
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
        <div className="border-t-2 border-foreground pt-6">
          <p className="eyebrow">Finished</p>
          <p className="numeral mt-2 text-[clamp(4rem,14vw,8rem)]">
            {correctCount} / {questions.length}
          </p>
          <p className="reading mt-2 text-lg">correct</p>
          <Button render={<Link href={backHref} />} nativeButton={false} size="lg" className="mt-8">
            {backLabel}
          </Button>
        </div>
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
      <div className="grid gap-x-10 gap-y-3 md:grid-cols-[10.5rem_minmax(0,1fr)]">
        <div className="space-y-3 md:pt-1">
          <p className="eyebrow !text-foreground">
            Question {index + 1} of {questions.length}
          </p>
          <p className="eyebrow">{question.difficulty.toLowerCase()}</p>
          <QuizProgress total={questions.length} current={index} className="hidden md:flex" />
          <Link href={backHref} className="eyebrow hidden underline underline-offset-4 hover:bg-mark hover:text-on-mark hover:no-underline md:inline-block">
            Leave quiz
          </Link>
        </div>

        <Sheet lined={paperLined} className="min-w-0">
          <Html html={question.stemHtml} className="text-[1.1875rem]" />
          {question.diagram && <DiagramRenderer diagram={question.diagram} />}

          <div className="mt-5">
            <ChoiceList legend="Answer choices">
              {question.choices.map((choice) => (
                <Choice
                  key={choice.id}
                  name={`question-${question.id}`}
                  label={choice.label}
                  textHtml={choice.textHtml}
                  explanationHtml={choice.explanationHtml}
                  checked={selectedLabel === choice.label}
                  disabled={revealed}
                  revealed={revealed}
                  state={revealed ? (choice.isCorrect ? "correct" : selectedLabel === choice.label ? "wrong" : "idle") : "idle"}
                  onSelect={() => setSelectedLabel(choice.label)}
                />
              ))}
            </ChoiceList>
          </div>

          {revealed ? (
            <div className="mt-6 border-t-2 border-current pt-4">
              <p className="eyebrow !text-current">Explanation</p>
              <Html html={question.explanationHtml} size="sm" className="mt-1.5" />
              <Link
                href={question.conceptHref}
                className="mt-3 inline-block text-sm font-semibold underline underline-offset-4 hover:bg-mark hover:text-on-mark hover:no-underline"
              >
                Review this concept
              </Link>
            </div>
          ) : null}

          <div className="mt-6 flex justify-end">
            {!revealed ? (
              <Button onClick={handleSubmit} disabled={!selectedLabel} size="lg">
                Submit
              </Button>
            ) : (
              <Button onClick={handleNext} size="lg">
                {isLast ? "See results" : "Next question"}
              </Button>
            )}
          </div>
        </Sheet>
      </div>
    </>
  );
}
