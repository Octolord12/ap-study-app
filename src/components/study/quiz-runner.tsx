"use client";

import { useState } from "react";
import Link from "next/link";
import { recordAttempt } from "@/lib/study/actions";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import type { AttemptSource } from "@/generated/prisma/client";

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

  const done = results.length === questions.length;

  if (done) {
    const correctCount = results.filter((r) => r.correct).length;
    return (
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
    );
  }

  const question = questions[index];
  const isLast = index === questions.length - 1;

  function handleSubmit() {
    if (!selectedLabel) return;
    const chosen = question.choices.find((c) => c.label === selectedLabel);
    const correct = chosen?.isCorrect ?? false;

    setResults((prev) => [...prev, { questionId: question.id, correct }]);
    setRevealed(true);

    // Fire-and-forget: the UI already reflects correctness from the (already
    // fetched, trusted) choice data. The persisted attempt log is what needs
    // the server's own lookup -- see recordAttempt.
    void recordAttempt({
      questionId: question.id,
      chosenLabel: selectedLabel,
      timeSpentMs: Date.now() - startedAt,
      source,
    });
  }

  function handleNext() {
    setIndex((i) => i + 1);
    setSelectedLabel(null);
    setRevealed(false);
    setStartedAt(Date.now());
  }

  return (
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
  );
}
