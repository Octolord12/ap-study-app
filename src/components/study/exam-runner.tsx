"use client";

import { Fragment, useEffect, useRef, useState } from "react";
import { submitExamAttempt } from "@/lib/study/actions";
import { Button } from "@/components/ui/button";
import { Choice, ChoiceList } from "@/components/ui/choice";
import { Html } from "@/components/ui/html";
import { Label } from "@/components/ui/label";
import { Sheet } from "@/components/ui/sheet";
import { Textarea } from "@/components/ui/textarea";
import { cn } from "cn";
import { DiagramRenderer } from "@/components/diagrams/diagram-renderer";
import type { Diagram } from "@/lib/content/diagram-schema";
import { isPaperLinedCourse } from "@/lib/content/paper-lined";
import { frqTitle } from "@/lib/content/exam-format";
import { examDraftKey, parseExamDraft, purgeStaleExamDrafts, serializeExamDraft } from "@/lib/study/exam-draft";

export interface ExamMcqItem {
  id: string;
  stemHtml: string;
  diagram: Diagram | null;
  choices: { id: string; label: string; displayLabel: string; textHtml: string }[];
}

export interface ExamFrqItem {
  id: string;
  type: string; // FRQ, SAQ, DBQ or LEQ
  promptHtml: string;
  diagram: Diagram | null;
  pointValue: number;
}

interface ExamRunnerProps {
  examAttemptId: string;
  courseSlug: string;
  // Computed on the server from ExamAttempt.startedAt, so a reload resumes the real clock.
  initialSecondsLeft: number;
  mcqItems: ExamMcqItem[];
  frqItems: ExamFrqItem[];
}

function formatTime(totalSeconds: number): string {
  const hours = Math.floor(totalSeconds / 3600);
  const minutes = Math.floor((totalSeconds % 3600) / 60);
  const seconds = totalSeconds % 60;
  const ss = String(seconds).padStart(2, "0");
  return hours > 0 ? `${hours}:${String(minutes).padStart(2, "0")}:${ss}` : `${minutes}:${ss}`;
}

// Only whole checkpoints get a message (null everywhere else) -- an
// aria-live region that updated every second would spam screen readers with
// the ticking countdown.
function checkpointAnnouncement(secondsLeft: number): string | null {
  if (secondsLeft <= 0) return "Time is up.";
  if (secondsLeft <= 60 && secondsLeft % 10 === 0) return `${secondsLeft} seconds remaining.`;
  if (secondsLeft > 60 && secondsLeft % 60 === 0) return `${Math.floor(secondsLeft / 60)} minutes remaining.`;
  return null;
}

export function ExamRunner({ examAttemptId, courseSlug, initialSecondsLeft, mcqItems, frqItems }: ExamRunnerProps) {
  const [index, setIndex] = useState(0);
  const [mcqAnswers, setMcqAnswers] = useState<Record<string, string>>({});
  const [frqResponses, setFrqResponses] = useState<Record<string, string>>({});
  const [secondsLeft, setSecondsLeft] = useState(initialSecondsLeft);
  // Fixed once, so the countdown is wall-clock time rather than "number of ticks": a
  // throttled background tab or a long main-thread pause can't make it drift.
  const [deadlineMs] = useState(() => Date.now() + initialSecondsLeft * 1000);
  const [restored, setRestored] = useState(false);
  const [resumed, setResumed] = useState(false);
  const [submitting, setSubmitting] = useState(false);
  const submittingRef = useRef(false);
  const [timeAnnouncement, setTimeAnnouncement] = useState("");
  const [confirming, setConfirming] = useState(false);

  const items = [...mcqItems, ...frqItems];
  const total = items.length;
  const paperLined = isPaperLinedCourse(courseSlug);

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

  // The interval is created once, but must submit the answers as they are when time
  // runs out, not as they were at mount (it used to submit an empty exam). Hence a
  // ref to the latest handleSubmit, refreshed after every render.
  const submitRef = useRef(handleSubmit);
  useEffect(() => {
    submitRef.current = handleSubmit;
  });

  useEffect(() => {
    const interval = setInterval(() => {
      const left = Math.max(0, Math.ceil((deadlineMs - Date.now()) / 1000));
      setSecondsLeft(left);
      if (left <= 0) {
        clearInterval(interval);
        void submitRef.current();
      }
    }, 1000);
    return () => clearInterval(interval);
  }, [deadlineMs]);

  // Answers come back from this device's storage after a reload. It can only be read
  // after mount (the server render has no storage), so it is an effect, not an initialiser.
  useEffect(() => {
    try {
      purgeStaleExamDrafts(localStorage, Date.now());
      const draft = parseExamDraft(localStorage.getItem(examDraftKey(examAttemptId)), Date.now(), {
        mcqIds: mcqItems.map((q) => q.id),
        frqIds: frqItems.map((f) => f.id),
        total: mcqItems.length + frqItems.length,
      });
      if (draft) {
        // eslint-disable-next-line react-hooks/set-state-in-effect -- one-time restore from localStorage on mount
        setMcqAnswers(draft.mcq);
        setFrqResponses(draft.frq);
        setIndex(draft.index);
        setResumed(Object.keys(draft.mcq).length + Object.keys(draft.frq).length > 0);
      }
    } catch {
      // Storage can be blocked (private mode); the exam still works, it just can't resume.
    }
    setRestored(true);
    // eslint-disable-next-line react-hooks/exhaustive-deps -- restore once per attempt; the items are fixed for it.
  }, [examAttemptId]);

  // Not before the restore above: saving the empty initial state would overwrite the draft.
  useEffect(() => {
    if (!restored) return;
    try {
      localStorage.setItem(examDraftKey(examAttemptId), serializeExamDraft({ mcq: mcqAnswers, frq: frqResponses, index }, Date.now()));
    } catch {
      // Out of space or blocked: nothing to do, the exam carries on.
    }
  }, [restored, examAttemptId, mcqAnswers, frqResponses, index]);

  const lowTime = secondsLeft <= 300; // last 5 minutes

  // Render-phase state adjustment (React-sanctioned, not an effect): only
  // updates when secondsLeft actually hits a checkpoint, so it doesn't
  // cascade every second.
  const checkpoint = checkpointAnnouncement(secondsLeft);
  if (checkpoint !== null && checkpoint !== timeAnnouncement) {
    setTimeAnnouncement(checkpoint);
  }

  if (total === 0) {
    return <p className="reading border-t-2 border-foreground pt-6 text-lg">No questions are available for this exam.</p>;
  }

  const isFrq = index >= mcqItems.length;
  const mcqItem = !isFrq ? mcqItems[index] : null;
  const frqItem = isFrq ? frqItems[index - mcqItems.length] : null;

  const isAnswered = (i: number) =>
    i < mcqItems.length ? Boolean(mcqAnswers[mcqItems[i].id]) : (frqResponses[frqItems[i - mcqItems.length].id] ?? "").trim().length > 0;
  const unanswered = items.filter((_, i) => !isAnswered(i)).length;
  // "Short answer 2 of 3" when the exam has several prompts of the kind, just the kind when it has one.
  const sameKind = frqItem ? frqItems.filter((f) => f.type === frqItem.type) : [];
  const sectionLabel = frqItem
    ? sameKind.length > 1
      ? `${frqTitle(frqItem.type)} ${sameKind.indexOf(frqItem) + 1} of ${sameKind.length}`
      : frqTitle(frqItem.type)
    : "Multiple choice";

  const grid = (
    <div className="flex flex-wrap gap-1" role="group" aria-label="Jump to a question">
      {items.map((item, i) => (
        <Fragment key={item.id}>
          {i === mcqItems.length && mcqItems.length > 0 ? <span aria-hidden className="h-0 basis-full" /> : null}
        <button
          type="button"
          onClick={() => setIndex(i)}
          aria-label={`Question ${i + 1}${i >= mcqItems.length ? ` (${frqTitle(frqItems[i - mcqItems.length].type).toLowerCase()})` : ""}, ${isAnswered(i) ? "answered" : "not answered"}`}
          aria-current={i === index ? "step" : undefined}
          className={cn(
            "grid size-9 place-items-center border-[1.5px] border-foreground text-xs font-semibold tabular-nums hover:bg-mark hover:text-on-mark",
            isAnswered(i) && "bg-foreground text-background",
            i === index && "bg-mark text-on-mark outline-2 outline-offset-1 outline-foreground",
            i === mcqItems.length && mcqItems.length > 0 && "mt-1"
          )}
        >
          {i + 1}
        </button>
        </Fragment>
      ))}
    </div>
  );

  const timer = (
    <p className={cn("numeral text-4xl", lowTime && "text-incorrect")}>{formatTime(secondsLeft)}</p>
  );

  return (
    <div className="grid gap-x-10 gap-y-4 md:grid-cols-[10.5rem_minmax(0,1fr)]">
      <span role="status" aria-live="polite" className="sr-only">
        {timeAnnouncement}
      </span>

      {resumed ? (
        <p role="note" className="border-2 border-foreground p-3 text-sm font-medium md:col-span-2">
          Welcome back. Your answers were kept on this device and the clock kept running. The choices may be in a different
          order.
        </p>
      ) : null}

      {/* Phones: a thin sticky strip, so the clock is always in view. */}
      <div className="sticky top-0 z-30 -mx-4 flex items-baseline justify-between border-b border-border bg-background px-4 py-2 md:hidden">
        <span className="eyebrow !text-foreground">
          {sectionLabel} · {index + 1} of {total}
        </span>
        <span className={cn("numeral text-xl", lowTime && "text-incorrect")}>{formatTime(secondsLeft)}</span>
      </div>

      {/* Desktop: the margin column is the answer sheet's header. */}
      <div className="hidden space-y-4 md:sticky md:top-4 md:block md:self-start">
        <div>
          {timer}
          <p className="eyebrow mt-1">{lowTime ? "Under 5 minutes" : "Time left"}</p>
        </div>
        <p className="eyebrow !text-foreground">
          {sectionLabel}
          <br />
          Question {index + 1} of {total}
        </p>
        {grid}
      </div>

      <div className="min-w-0 space-y-4">
        <details className="md:hidden">
          <summary className="cursor-pointer text-sm font-semibold underline-offset-4 hover:underline">
            Jump to a question ({unanswered} unanswered)
          </summary>
          <div className="mt-3">{grid}</div>
        </details>

        <Sheet lined={paperLined}>
          {mcqItem ? (
            <>
              <Html html={mcqItem.stemHtml} className="text-[1.1875rem]" />
              {mcqItem.diagram && <DiagramRenderer diagram={mcqItem.diagram} />}
              <div className="mt-5">
                <ChoiceList legend="Answer choices">
                  {mcqItem.choices.map((choice) => (
                    <Choice
                      key={choice.id}
                      name={`exam-question-${mcqItem.id}`}
                      label={choice.label}
                      displayLabel={choice.displayLabel}
                      textHtml={choice.textHtml}
                      checked={mcqAnswers[mcqItem.id] === choice.label}
                      revealed={false}
                      onSelect={() => setMcqAnswers((prev) => ({ ...prev, [mcqItem.id]: choice.label }))}
                    />
                  ))}
                </ChoiceList>
              </div>
            </>
          ) : null}

          {frqItem ? (
            <>
              <p className="eyebrow mb-2">
                {frqItem.pointValue} point{frqItem.pointValue === 1 ? "" : "s"}
              </p>
              <Html html={frqItem.promptHtml} />
              {frqItem.diagram && <DiagramRenderer diagram={frqItem.diagram} />}
              <div className="mt-5 space-y-1.5">
                <Label htmlFor={`frq-${frqItem.id}`}>Your response</Label>
                <Textarea
                  id={`frq-${frqItem.id}`}
                  value={frqResponses[frqItem.id] ?? ""}
                  onChange={(e) => setFrqResponses((prev) => ({ ...prev, [frqItem.id]: e.target.value }))}
                  placeholder="Write your response here."
                  rows={10}
                />
              </div>
            </>
          ) : null}
        </Sheet>

        <div className="flex flex-wrap items-center justify-between gap-3">
          <Button variant="outline" size="lg" onClick={() => setIndex((i) => Math.max(0, i - 1))} disabled={index === 0}>
            Previous
          </Button>
          {index < total - 1 ? (
            <Button size="lg" onClick={() => setIndex((i) => Math.min(total - 1, i + 1))}>
              Next
            </Button>
          ) : null}
        </div>

        <div className="border-t-2 border-foreground pt-4">
          {confirming ? (
            <div role="alertdialog" aria-label="Confirm submit" className="space-y-3">
              <p className="text-sm font-medium">
                Submit the exam now?{" "}
                {unanswered > 0 ? `${unanswered} of ${total} questions are unanswered.` : "Every question has an answer."}
              </p>
              <div className="flex flex-wrap gap-3">
                <Button size="lg" onClick={() => void handleSubmit()} disabled={submitting}>
                  {submitting ? "Submitting…" : "Yes, submit"}
                </Button>
                <Button size="lg" variant="outline" onClick={() => setConfirming(false)} disabled={submitting}>
                  Keep working
                </Button>
              </div>
            </div>
          ) : (
            <Button variant="outline" onClick={() => setConfirming(true)} disabled={submitting}>
              Submit exam
            </Button>
          )}
        </div>
      </div>
    </div>
  );
}
