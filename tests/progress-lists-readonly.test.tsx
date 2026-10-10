import { render } from "@testing-library/react";
import { describe, expect, it } from "vitest";
import { UnitMasteryList } from "@/components/study/unit-mastery-list";
import { WeakTopicsList } from "@/components/study/weak-topics-list";

const UNITS = [{ id: "u1", slug: "unit-1", name: "Limits and Continuity", total: 30, attempted: 10, correct: 7 }];
const WEAK = [
  { topicId: "t1", topicName: "Related Rates", topicSlug: "related-rates", unitSlug: "unit-4", unitName: "Contextual Applications", courseSlug: "ap-calc", courseName: "AP Calculus AB", attempted: 4, correct: 2, accuracyPercent: 50 },
];

describe("UnitMasteryList", () => {
  it("links each unit to its page by default (the student's own Progress page)", () => {
    const { container } = render(<UnitMasteryList courseSlug="ap-calc" units={UNITS} />);
    expect(container.querySelector("a")?.getAttribute("href")).toBe("/courses/ap-calc/units/unit-1");
  });

  it("with links off (the parent's page) shows the same numbers and no links", () => {
    const withLinks = render(<UnitMasteryList courseSlug="ap-calc" units={UNITS} />);
    const textWith = withLinks.container.textContent;
    withLinks.unmount();
    const { container } = render(<UnitMasteryList courseSlug="ap-calc" units={UNITS} links={false} />);
    expect(container.querySelectorAll("a")).toHaveLength(0);
    expect(container.textContent).toBe(textWith);
    expect(container.textContent).toContain("70%");
  });

  it("does not say 'you' to a parent reading it", () => {
    const { container } = render(<UnitMasteryList courseSlug="ap-calc" units={UNITS} links={false} />);
    expect(container.textContent).not.toMatch(/\byou\b/i);
  });
});

describe("WeakTopicsList", () => {
  it("offers Refresher and Practice links by default", () => {
    const { container } = render(<WeakTopicsList topics={WEAK} withRefresher={new Set(["t1"])} />);
    expect([...container.querySelectorAll("a")].map((a) => a.textContent)).toEqual(["Refresher", "Practice"]);
  });

  it("with links off shows the topic and its score and nothing to click, even for a topic that has a refresher", () => {
    const { container } = render(<WeakTopicsList topics={WEAK} withRefresher={new Set(["t1"])} links={false} />);
    expect(container.querySelectorAll("a")).toHaveLength(0);
    expect(container.textContent).toContain("Related Rates");
    expect(container.textContent).toContain("50%");
  });

  it("speaks to the student on their page and neutrally on a parent's", () => {
    expect(render(<WeakTopicsList topics={[]} />).container.textContent).toMatch(/Once you have answered/);
    const parent = render(<WeakTopicsList topics={[]} links={false} />);
    expect(parent.container.textContent).toMatch(/Once a few questions on a topic have been answered/);
    expect(parent.container.textContent).not.toMatch(/\byou\b/i);
  });
});
