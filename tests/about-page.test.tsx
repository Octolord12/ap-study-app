import { render, screen } from "@testing-library/react";
import { beforeEach, describe, expect, it, vi } from "vitest";

const mocks = vi.hoisted(() => ({
  counts: { questions: 1050, reviewedQuestions: 0, prompts: 105, reviewedPrompts: 0, refreshers: 0, reviewedRefreshers: 0 },
  db: {
    question: { count: vi.fn() },
    fRQPrompt: { count: vi.fn() },
    topic: { count: vi.fn() },
  },
}));

mocks.db.question.count.mockImplementation(async (args?: { where?: { reviewed?: boolean } }) => (args?.where?.reviewed ? mocks.counts.reviewedQuestions : mocks.counts.questions));
mocks.db.fRQPrompt.count.mockImplementation(async (args?: { where?: { reviewed?: boolean } }) => (args?.where?.reviewed ? mocks.counts.reviewedPrompts : mocks.counts.prompts));

mocks.db.topic.count.mockImplementation(async (args?: { where?: { refresherReviewed?: boolean } }) => (args?.where?.refresherReviewed ? mocks.counts.reviewedRefreshers : mocks.counts.refreshers));

vi.mock("@/lib/db", () => ({ getDb: () => mocks.db }));
vi.mock("@/lib/study/queries", () => ({
  listCourses: async () => [{ name: "AP Calculus AB" }, { name: "AP Physics 1" }, { name: "AP World History: Modern" }],
}));

import AboutPage from "@/app/about/page";
import { SOCIAL_SAFETY_NOTE } from "@/lib/social/copy";

async function renderPage() {
  return render(await AboutPage());
}

describe("About and FAQ", () => {
  beforeEach(() => {
    mocks.counts = { questions: 1050, reviewedQuestions: 0, prompts: 105, reviewedPrompts: 0, refreshers: 0, reviewedRefreshers: 0 };
  });

  it("names the courses from the database, and says it was built by one person, with no name", async () => {
    const { container } = await renderPage();
    expect(container.textContent).toContain("AP Calculus AB, AP Physics 1 and AP World History: Modern");
    expect(screen.getByText("Built by one person for students preparing for AP exams.")).toBeInTheDocument();
  });

  it("says plainly that nothing has been checked by a teacher yet, when that is true", async () => {
    const { container } = await renderPage();
    expect(container.textContent).toMatch(/None of them has been checked by a teacher yet/);
    expect(container.textContent).toMatch(/written with the help of AI/);
  });

  it("states the real review count once some content has been approved", async () => {
    mocks.counts = { questions: 1050, reviewedQuestions: 200, prompts: 105, reviewedPrompts: 5, refreshers: 0, reviewedRefreshers: 0 };
    const { container } = await renderPage();
    expect(container.textContent).toContain("205 of 1,155 have been checked by a person");
    expect(container.textContent).not.toMatch(/None of them/);
  });

  it("counts the topic refreshers with the questions, because they are written the same way", async () => {
    mocks.counts = { questions: 1050, reviewedQuestions: 200, prompts: 105, reviewedPrompts: 5, refreshers: 35, reviewedRefreshers: 10 };
    const { container } = await renderPage();
    expect(container.textContent).toContain("215 of 1,190 have been checked by a person");
    expect(container.textContent).toMatch(/topic refreshers were written with the help of AI/);
  });

  it("does not mention price, because the owner chose not to say yet", async () => {
    const { container } = await renderPage();
    expect(container.textContent).not.toMatch(/\b(price|pricing|cost|costs|subscription|paid|charge|charging|free of charge)\b/i);
  });

  it("repeats the safety facts from the single sources of truth", async () => {
    const { container } = await renderPage();
    expect(container.textContent).toContain("13 or older");
    expect(container.textContent).toContain(SOCIAL_SAFETY_NOTE);
  });

  it("links to privacy, and to a mail link that doesn't print the address", async () => {
    const { container } = await renderPage();
    expect(screen.getByRole("link", { name: "Privacy page" })).toHaveAttribute("href", "/privacy");
    expect(screen.getByRole("link", { name: "send a suggestion" }).getAttribute("href")).toMatch(/^mailto:/);
    expect(container.textContent).not.toMatch(/@|gmail/i);
  });
});
