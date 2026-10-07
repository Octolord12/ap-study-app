import { render, screen, within } from "@testing-library/react";
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import { ExamWeakUnits } from "@/components/study/exam-weak-units";
import { WeakTopicsList } from "@/components/study/weak-topics-list";
import { WeekActivity } from "@/components/study/week-activity";
import type { ActivityEntry } from "@/lib/study/week-activity";

describe("WeekActivity", () => {
  const NOW = new Date(2026, 9, 5, 15, 0, 0).getTime(); // a Monday afternoon, local time
  const HOUR = 3_600_000;

  beforeEach(() => {
    vi.useFakeTimers();
    vi.setSystemTime(NOW);
  });
  afterEach(() => vi.useRealTimers());

  it("shows the week's numbers and one labelled bar per day", () => {
    const entries: ActivityEntry[] = [
      { at: NOW - HOUR, kind: "question", correct: true, ms: 60_000 },
      { at: NOW - 2 * HOUR, kind: "question", correct: false, ms: 60_000 },
      { at: NOW - 30 * HOUR, kind: "question", correct: true, ms: 60_000 },
    ];
    render(<WeekActivity entries={entries} />);

    expect(screen.getByText("Days studied")).toBeInTheDocument();
    expect(screen.getByText("67%")).toBeInTheDocument(); // 2 of 3 correct
    const bars = within(screen.getByRole("list", { name: /Questions answered each day/ })).getAllByRole("listitem");
    expect(bars).toHaveLength(7);
    expect(bars[6]).toHaveAccessibleName("Mon (today): 2 questions");
    expect(bars[5]).toHaveAccessibleName("Sun: 1 question");
    expect(bars[0]).toHaveAccessibleName(/: 0 questions$/);
  });

  it("says so when nothing happened this week", () => {
    render(<WeekActivity entries={[]} />);
    expect(screen.getByText(/Nothing in the last 7 days yet/)).toBeInTheDocument();
    expect(screen.getByText("–")).toBeInTheDocument();
  });

  it("is honest about what the time measures", () => {
    render(<WeekActivity entries={[{ at: NOW - HOUR, kind: "question", correct: true, ms: 1000 }]} />);
    expect(screen.getByText(/Reading explanations isn't counted/)).toBeInTheDocument();
  });
});

describe("WeakTopicsList", () => {
  it("lists each topic with its score and a link that practices exactly that topic", () => {
    render(
      <WeakTopicsList
        topics={[
          { topicId: "t1", topicName: "The Chain Rule", topicSlug: "chain-rule", unitSlug: "unit-3", unitName: "Composite Functions", courseSlug: "ap-calc", courseName: "AP Calculus AB", attempted: 5, correct: 2, accuracyPercent: 40 },
        ]}
      />,
    );
    expect(screen.getByText("The Chain Rule")).toBeInTheDocument();
    expect(screen.getByText("40%")).toBeInTheDocument();
    expect(screen.getByText("2 of 5 right")).toBeInTheDocument();
    expect(screen.getByRole("link", { name: "Practice" })).toHaveAttribute("href", "/courses/ap-calc/units/unit-3?topic=chain-rule");
  });

  it("offers the refresher first when the topic has one, and still the practice link", () => {
    render(
      <WeakTopicsList
        withRefresher={new Set(["t1"])}
        topics={[
          { topicId: "t1", topicName: "The Chain Rule", topicSlug: "chain-rule", unitSlug: "unit-3", unitName: "Composite Functions", courseSlug: "ap-calc", courseName: "AP Calculus AB", attempted: 5, correct: 2, accuracyPercent: 40 },
          { topicId: "t2", topicName: "Implicit Differentiation", topicSlug: "implicit", unitSlug: "unit-3", unitName: "Composite Functions", courseSlug: "ap-calc", courseName: "AP Calculus AB", attempted: 4, correct: 1, accuracyPercent: 25 },
        ]}
      />,
    );
    const refreshers = screen.getAllByRole("link", { name: "Refresher" });
    expect(refreshers).toHaveLength(1);
    expect(refreshers[0]).toHaveAttribute("href", "/courses/ap-calc/units/unit-3/topics/chain-rule");
    expect(screen.getAllByRole("link", { name: "Practice" })).toHaveLength(2);
  });

  it("explains the empty state instead of showing a blank", () => {
    render(<WeakTopicsList topics={[]} />);
    expect(screen.getByText(/None right now/)).toBeInTheDocument();
  });
});

describe("ExamWeakUnits", () => {
  const unit = { unitSlug: "unit-5", unitName: "Analytical Applications", unitOrder: 5, total: 6, missed: 4, missedIds: ["a", "b", "c", "d"] };

  it("links each unit to a quiz of exactly the questions missed, and back to the results", () => {
    render(<ExamWeakUnits units={[unit]} courseSlug="ap-calc" backHref="/courses/ap-calc/exam/e1/results" />);
    expect(screen.getByText("4 of 6 missed or skipped")).toBeInTheDocument();
    const link = screen.getByRole("link", { name: "Practice the 4 you missed" });
    const url = new URL(link.getAttribute("href")!, "http://x");
    expect(url.pathname).toBe("/courses/ap-calc/quiz");
    expect(url.searchParams.get("ids")).toBe("a,b,c,d");
    expect(url.searchParams.get("source")).toBe("PRACTICE");
    expect(url.searchParams.get("back")).toBe("/courses/ap-calc/exam/e1/results");
  });

  it("caps a practice quiz at 20 questions", () => {
    const ids = Array.from({ length: 30 }, (_, i) => `q${i}`);
    render(<ExamWeakUnits units={[{ ...unit, total: 30, missed: 30, missedIds: ids }]} courseSlug="ap-calc" backHref="/r" />);
    const link = screen.getByRole("link", { name: "Practice the 20 you missed" });
    expect(new URL(link.getAttribute("href")!, "http://x").searchParams.get("ids")!.split(",")).toHaveLength(20);
  });

  it("says so when nothing was missed", () => {
    render(<ExamWeakUnits units={[]} courseSlug="ap-calc" backHref="/r" />);
    expect(screen.getByText("You got every multiple-choice question right.")).toBeInTheDocument();
  });
});
