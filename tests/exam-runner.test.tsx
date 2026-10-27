import { StrictMode } from "react";
import { act, fireEvent, render, screen } from "@testing-library/react";
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";

const submit = vi.hoisted(() => vi.fn(async () => undefined));
vi.mock("@/lib/study/actions", () => ({ submitExamAttempt: submit }));

import { ClearExamDraft } from "@/components/study/clear-exam-draft";
import { ExamRunner, type ExamFrqItem, type ExamMcqItem } from "@/components/study/exam-runner";
import { examDraftKey, serializeExamDraft } from "@/lib/study/exam-draft";

const choices = (id: string): ExamMcqItem["choices"] =>
  ["A", "B", "C", "D"].map((label, i) => ({ id: `${id}-${label}`, label, displayLabel: ["A", "B", "C", "D"][(i + 1) % 4], textHtml: `<p>${id} option ${label}</p>` }));

const mcqItems: ExamMcqItem[] = [
  { id: "q1", stemHtml: "<p>First question</p>", diagram: null, choices: choices("q1") },
  { id: "q2", stemHtml: "<p>Second question</p>", diagram: null, choices: choices("q2") },
];
const frqItems: ExamFrqItem[] = [{ id: "f1", type: "FRQ", prompt: { introHtml: "<p>Explain it</p>", partsHtml: "" }, diagram: null, pointValue: 4 }];
const KEY = examDraftKey("exam-1");

function renderRunner(initialSecondsLeft: number) {
  return render(<ExamRunner examAttemptId="exam-1" courseSlug="ap-calc" initialSecondsLeft={initialSecondsLeft} mcqItems={mcqItems} frqItems={frqItems} />);
}
const radio = (container: HTMLElement, label: string) => container.querySelector(`input[type=radio][value="${label}"]`) as HTMLInputElement;

describe("ExamRunner clock", () => {
  beforeEach(() => {
    localStorage.clear();
    submit.mockClear();
  });
  afterEach(() => vi.useRealTimers());

  it("starts from the time left on the server, not from the full duration", () => {
    renderRunner(3 * 3600 + 9 * 60 + 43); // reloaded 17 seconds into a 3:10 exam
    expect(screen.getAllByText("3:09:43").length).toBeGreaterThan(0);
    expect(screen.queryByText("3:10:00")).not.toBeInTheDocument();
  });

  it("counts down by real time", () => {
    vi.useFakeTimers();
    renderRunner(100);
    act(() => void vi.advanceTimersByTime(30_000));
    expect(screen.getAllByText("1:10").length).toBeGreaterThan(0);
  });

  it("submits the answers the student gave, not an empty exam, when time runs out", () => {
    vi.useFakeTimers();
    const { container } = renderRunner(5);
    fireEvent.click(radio(container, "B")); // question 1
    fireEvent.click(screen.getAllByRole("button", { name: /^Question 3/ })[0]); // jump to the free response
    fireEvent.change(screen.getByLabelText("Your response"), { target: { value: "because the limit exists" } });

    act(() => void vi.advanceTimersByTime(5_000));

    expect(submit).toHaveBeenCalledTimes(1);
    expect(submit).toHaveBeenCalledWith({
      examAttemptId: "exam-1",
      courseSlug: "ap-calc",
      mcqAnswers: [{ questionId: "q1", chosenLabel: "B" }],
      frqResponses: [{ frqPromptId: "f1", responseText: "because the limit exists" }],
    });
  });

  it("submits only once however long the clock stays at zero", () => {
    vi.useFakeTimers();
    renderRunner(2);
    act(() => void vi.advanceTimersByTime(20_000));
    expect(submit).toHaveBeenCalledTimes(1);
  });

  it("an attempt whose time ran out while the student was away submits what was saved", () => {
    vi.useFakeTimers();
    localStorage.setItem(KEY, serializeExamDraft({ mcq: { q2: "D" }, frq: { f1: "saved text" }, index: 1 }, Date.now()));
    renderRunner(0);
    act(() => void vi.advanceTimersByTime(1_000));
    expect(submit).toHaveBeenCalledWith(
      expect.objectContaining({ mcqAnswers: [{ questionId: "q2", chosenLabel: "D" }], frqResponses: [{ frqPromptId: "f1", responseText: "saved text" }] }),
    );
  });
});

describe("ExamRunner keeps answers across a reload", () => {
  beforeEach(() => {
    localStorage.clear();
    submit.mockClear();
  });

  it("saves answers on this device as they are given", () => {
    const { container } = renderRunner(3600);
    fireEvent.click(radio(container, "C"));
    const saved = JSON.parse(localStorage.getItem(KEY)!);
    expect(saved.mcq).toEqual({ q1: "C" });
    expect(saved.index).toBe(0);
  });

  it("does not wipe a saved draft by saving the empty state before restoring it", () => {
    localStorage.setItem(KEY, serializeExamDraft({ mcq: { q1: "A", q2: "B" }, frq: {}, index: 1 }, Date.now()));
    renderRunner(3600);
    expect(JSON.parse(localStorage.getItem(KEY)!).mcq).toEqual({ q1: "A", q2: "B" });
  });

  it("restores the answers, the question you were on, and says so", () => {
    localStorage.setItem(KEY, serializeExamDraft({ mcq: { q1: "A", q2: "C" }, frq: { f1: "half-written answer" }, index: 1 }, Date.now()));
    const { container } = renderRunner(3600);

    expect(screen.getByRole("note")).toHaveTextContent(/Welcome back/);
    // Back on question 2, with the bubble filled in even though the choices are reshuffled on reload.
    expect(screen.getAllByText(/Question 2 of 3/).length).toBeGreaterThan(0);
    expect(radio(container, "C").checked).toBe(true);
    expect(radio(container, "A").checked).toBe(false);

    fireEvent.click(screen.getAllByRole("button", { name: /^Question 3/ })[0]);
    expect((screen.getByLabelText("Your response") as HTMLTextAreaElement).value).toBe("half-written answer");
  });

  it("still restores under StrictMode, which runs effects twice (as Next does in development)", () => {
    localStorage.setItem(KEY, serializeExamDraft({ mcq: { q1: "D" }, frq: {}, index: 0 }, Date.now()));
    const { container } = render(
      <StrictMode>
        <ExamRunner examAttemptId="exam-1" courseSlug="ap-calc" initialSecondsLeft={3600} mcqItems={mcqItems} frqItems={frqItems} />
      </StrictMode>,
    );
    expect(radio(container, "D").checked).toBe(true);
    expect(JSON.parse(localStorage.getItem(KEY)!).mcq).toEqual({ q1: "D" });
  });

  it("starts clean, with no welcome-back note, when there is nothing saved", () => {
    renderRunner(3600);
    expect(screen.queryByRole("note")).not.toBeInTheDocument();
  });

  it("ignores a draft saved for different questions", () => {
    localStorage.setItem(KEY, serializeExamDraft({ mcq: { "other-question": "A" }, frq: {}, index: 0 }, Date.now()));
    renderRunner(3600);
    expect(screen.queryByRole("note")).not.toBeInTheDocument();
  });

  it("the results page clears the saved answers", () => {
    localStorage.setItem(KEY, "something");
    render(<ClearExamDraft examAttemptId="exam-1" />);
    expect(localStorage.getItem(KEY)).toBeNull();
  });
});

describe("a free-response figure sits between the set-up and the lettered parts", () => {
  const withFigure: ExamFrqItem[] = [
    {
      id: "f2",
      type: "RESULTS",
      prompt: { introHtml: "<p>Set-up text</p>", partsHtml: "<p>(a) Describe the trend.</p>" },
      diagram: { type: "data-table", caption: "Results table", columns: ["Trial", "Rate"], rows: [["1", 2]], rowHeaders: false },
      pointValue: 9,
    },
  ];

  it("shows the table after the set-up text and before part (a)", () => {
    render(<ExamRunner examAttemptId="exam-3" courseSlug="ap-biology" initialSecondsLeft={3600} mcqItems={mcqItems} frqItems={withFigure} />);
    fireEvent.click(screen.getAllByRole("button", { name: /^Question 3/ })[0]);
    const setUp = screen.getByText("Set-up text");
    const table = screen.getByRole("table");
    const partA = screen.getByText("(a) Describe the trend.");
    expect(setUp.compareDocumentPosition(table) & Node.DOCUMENT_POSITION_FOLLOWING).toBeTruthy();
    expect(table.compareDocumentPosition(partA) & Node.DOCUMENT_POSITION_FOLLOWING).toBeTruthy();
  });
});

describe("labels for several kinds of free response", () => {
  const worldFrqs: ExamFrqItem[] = [
    { id: "s1", type: "SAQ", prompt: { introHtml: "<p>SAQ one</p>", partsHtml: "" }, diagram: null, pointValue: 3 },
    { id: "s2", type: "SAQ", prompt: { introHtml: "<p>SAQ two</p>", partsHtml: "" }, diagram: null, pointValue: 3 },
    { id: "d1", type: "DBQ", prompt: { introHtml: "<p>The DBQ</p>", partsHtml: "" }, diagram: null, pointValue: 7 },
    { id: "l1", type: "LEQ", prompt: { introHtml: "<p>The LEQ</p>", partsHtml: "" }, diagram: null, pointValue: 6 },
  ];

  it("names each prompt's kind, numbering only kinds that have several", () => {
    render(<ExamRunner examAttemptId="exam-2" courseSlug="ap-world" initialSecondsLeft={3600} mcqItems={mcqItems} frqItems={worldFrqs} />);
    const label = (name: RegExp) => fireEvent.click(screen.getAllByRole("button", { name })[0]);
    expect(screen.getAllByText(/Multiple choice/).length).toBeGreaterThan(0);

    label(/^Question 3 \(short answer\)/);
    expect(screen.getAllByText(/Short answer 1 of 2/).length).toBeGreaterThan(0);
    label(/^Question 4 \(short answer\)/);
    expect(screen.getAllByText(/Short answer 2 of 2/).length).toBeGreaterThan(0);
    label(/^Question 5 \(document-based question\)/);
    expect(screen.getAllByText(/Document-based question/).length).toBeGreaterThan(0);
    label(/^Question 6 \(long essay\)/);
    expect(screen.getAllByText(/Long essay/).length).toBeGreaterThan(0);
    expect(screen.queryByText(/Free response/)).toBeNull();
  });
});
