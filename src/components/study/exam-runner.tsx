"use client";

import { useEffect, useRef, useState } from "react";
import { submitExamAttempt } from "@/lib/study/actions";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { Textarea } from "@/components/ui/textarea";

export interface ExamMcqItem {
  id: string;
  stemHtml: string;
  choices: { id: string; label: string; text: string }[];
}

export interface ExamFrqItem {
  id: string;
  promptHtml: string;
  pointValue: number;
}

interface ExamRunnerProps {
  examAttemptId: string;
  courseSlug: string;
  totalDurationMinutes: number;
  mcqItems: ExamMcqItem[];
  frqItems: ExamFrqItem[];
}

function formatTime(totalSeconds: number): string {
  const minutes = Math.floor(totalSeconds / 60);
  const seconds = totalSeconds % 60;
  return `${minutes}:${String(seconds).padStart(2, "0")}`;
}

export function ExamRunner({ examAttemptId, courseSlug, totalDurationMinutes, mcqItems, frqItems }: ExamRunnerProps) {
  const [index, setIndex] = useState(0);
  const [mcqAnswers, setMcqAnswers] = useState<Record<string, string>>({});
  const [frqResponses, setFrqResponses] = useState<Record<string, string>>({});
  const [secondsLeft, setSecondsLeft] = useState(totalDurationMinutes * 60);
  const [submitting, setSubmitting] = useState(false);
  const submittingRef = useRef(false);

  const items = [...mcqItems, ...frqItems];
  const total = items.length;

  async function handleSubmit() {
    if (submittingRef.current) return;
    submittingRef.current = true;
    setSubmitting(true);
    await submitExamAttempt({
      examAttemptId,
      courseSlug,
      mcqAnswers: mcqItems
        .filter((q) => mcqAnswers[q.id])
        .map((q) => ({ questionId: q.id, chosenLabel: mcqAnswers[q.id] })),
      frqResponses: frqItems.map((f) => ({ frqPromptId: f.id, responseText: frqResponses[f.id] ?? "" })),
    });
  }

  useEffect(() => {
    const interval = setInterval(() => {
      setSecondsLeft((s) => {
        if (s <= 1) {
          clearInterval(interval);
          void handleSubmit();
          return 0;
        }
        return s - 1;
      });
    }, 1000);
    return () => clearInterval(interval);
    // eslint-disable-next-line react-hooks/exhaustive-deps -- handleSubmit closes over state that changes every render; only want the interval set up once.
  }, []);

  const lowTime = secondsLeft <= 300; // last 5 minutes

  if (total === 0) {
    return (
      <Card>
        <CardContent className="py-10 text-center text-sm text-muted-foreground">
          No questions available for this exam.
        </CardContent>
      </Card>
    );
  }

  const isFrq = index >= mcqItems.length;
  const mcqItem = !isFrq ? mcqItems[index] : null;
  const frqItem = isFrq ? frqItems[index - mcqItems.length] : null;

  return (
    <div className="space-y-3">
      <div className="flex items-center justify-between text-sm">
        <span className="text-muted-foreground">
          {isFrq ? "FRQ" : "MCQ"} · Question {index + 1} of {total}
        </span>
        <span className={lowTime ? "font-semibold text-destructive" : "text-muted-foreground"}>
          {formatTime(secondsLeft)}
        </span>
      </div>

      <Card>
        <CardContent className="space-y-4 py-6">
          {mcqItem ? (
            <>
              <div
                className="prose prose-neutral dark:prose-invert max-w-none"
                dangerouslySetInnerHTML={{ __html: mcqItem.stemHtml }}
              />
              <div className="space-y-2">
                {mcqItem.choices.map((choice) => (
                  <button
                    key={choice.id}
                    type="button"
                    onClick={() => setMcqAnswers((prev) => ({ ...prev, [mcqItem.id]: choice.label }))}
                    className={[
                      "w-full rounded-lg border px-4 py-2 text-left text-sm transition-colors",
                      mcqAnswers[mcqItem.id] === choice.label ? "border-foreground bg-muted" : "border-border",
                    ].join(" ")}
                  >
                    <span className="font-medium">{choice.label}.</span> {choice.text}
                  </button>
                ))}
              </div>
            </>
          ) : null}

          {frqItem ? (
            <>
              <div
                className="prose prose-neutral dark:prose-invert max-w-none"
                dangerouslySetInnerHTML={{ __html: frqItem.promptHtml }}
              />
              <Textarea
                value={frqResponses[frqItem.id] ?? ""}
                onChange={(e) => setFrqResponses((prev) => ({ ...prev, [frqItem.id]: e.target.value }))}
                placeholder="Write your response..."
                rows={10}
              />
            </>
          ) : null}
        </CardContent>
      </Card>

      <div className="flex items-center justify-between">
        <Button variant="outline" onClick={() => setIndex((i) => Math.max(0, i - 1))} disabled={index === 0}>
          Previous
        </Button>
        <div className="flex gap-2">
          <Button variant="outline" onClick={() => void handleSubmit()} disabled={submitting}>
            Submit exam
          </Button>
          {index < total - 1 ? (
            <Button onClick={() => setIndex((i) => Math.min(total - 1, i + 1))}>Next</Button>
          ) : null}
        </div>
      </div>
    </div>
  );
}
