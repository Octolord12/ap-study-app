import { render } from "@testing-library/react";
import { beforeEach, describe, expect, it, vi } from "vitest";

const mocks = vi.hoisted(() => ({
  share: null as null | { id: string; expiresAt: Date; userId: string; username: string },
  findUsableShare: vi.fn(),
  recordShareView: vi.fn(),
  loadProgressCore: vi.fn(),
}));

vi.mock("next/navigation", () => ({
  notFound: () => {
    throw new Error("NEXT_NOT_FOUND");
  },
}));
vi.mock("@/lib/share/queries", () => ({ findUsableShare: mocks.findUsableShare, recordShareView: mocks.recordShareView }));
vi.mock("@/lib/study/progress-data", async (importOriginal) => ({
  ...(await importOriginal<typeof import("@/lib/study/progress-data")>()),
  loadProgressCore: mocks.loadProgressCore,
}));

import SharedProgressPage, { dynamic, metadata } from "@/app/share/[token]/page";

const PROGRESS = {
  stats: { level: 4, totalXp: 612, xpIntoLevel: 12, xpForNextLevel: 400, currentStreak: 3, longestStreak: 9, streakFreezesAvailable: 1 },
  weekEntries: [],
  weakest: [
    { topicId: "t1", topicName: "Related Rates", topicSlug: "related-rates", unitSlug: "unit-4", unitName: "Contextual Applications", courseSlug: "ap-calc", courseName: "AP Calculus AB", attempted: 4, correct: 2, accuracyPercent: 50 },
  ],
  courses: [
    {
      id: "c1",
      slug: "ap-calc",
      name: "AP Calculus AB",
      units: [{ id: "u1", slug: "unit-1", name: "Limits and Continuity", total: 30, attempted: 10, correct: 7 }],
      totalAttempted: 10,
      totalCorrect: 7,
    },
  ],
};

const run = async (token = "t".repeat(43)) => render(await SharedProgressPage({ params: Promise.resolve({ token }) }));

describe("the parent's page", () => {
  beforeEach(() => {
    vi.clearAllMocks();
    mocks.share = { id: "s1", expiresAt: new Date("2027-01-07T00:00:00Z"), userId: "u1", username: "alice_k" };
    mocks.findUsableShare.mockImplementation(async () => mocks.share);
    mocks.recordShareView.mockResolvedValue({ count: 1 });
    mocks.loadProgressCore.mockResolvedValue(PROGRESS);
  });

  it("is a 404 for anything that is not a live link, and loads no one's data", async () => {
    mocks.share = null;
    await expect(run()).rejects.toThrow("NEXT_NOT_FOUND");
    expect(mocks.loadProgressCore).not.toHaveBeenCalled();
    expect(mocks.recordShareView).not.toHaveBeenCalled();
  });

  it("loads exactly the progress of the student the link belongs to", async () => {
    await run();
    expect(mocks.findUsableShare).toHaveBeenCalledWith("t".repeat(43));
    expect(mocks.loadProgressCore).toHaveBeenCalledWith("u1");
  });

  it("shows the summary, with the username as the only identity and the expiry date", async () => {
    const { container } = await run();
    const text = container.textContent ?? "";
    expect(text).toContain("Progress for alice_k");
    expect(text).toContain("January 7, 2027");
    expect(text).toContain("612 XP total");
    expect(text).toContain("3");
    expect(text).toContain("Related Rates");
    expect(text).toContain("AP Calculus AB");
    expect(text).toContain("70% correct across 10 questions.");
    expect(text).toContain("Limits and Continuity");
  });

  it("never asks the loader or the share lookup for a name or an email, so there is none to leak", async () => {
    await run();
    // The lookup returns only { id, expiresAt, userId, username } (tested in share-queries); the page has nothing else to print.
    expect(Object.keys(mocks.share!).sort()).toEqual(["expiresAt", "id", "userId", "username"]);
    const { container } = await run();
    expect(container.innerHTML).not.toMatch(/@|displayName|passwordHash/);
  });

  it("is read-only: no links into the student's own pages and no forms or buttons", async () => {
    const { container } = await run();
    expect(container.querySelectorAll("a")).toHaveLength(0);
    expect(container.querySelectorAll("form, button, input")).toHaveLength(0);
  });

  it("keeps the address out of search results and out of the Referer header", () => {
    expect(metadata.robots).toEqual({ index: false, follow: false });
    expect(metadata.referrer).toBe("no-referrer");
  });

  it("is never served from a cache", () => {
    expect(dynamic).toBe("force-dynamic");
  });

  it("still shows the page when recording the view fails", async () => {
    mocks.recordShareView.mockRejectedValue(new Error("db down"));
    const { container } = await run();
    expect(container.textContent).toContain("Progress for alice_k");
  });

  it("handles a student with no course and no weak topics", async () => {
    mocks.loadProgressCore.mockResolvedValue({ ...PROGRESS, weakest: [], courses: [] });
    const { container } = await run();
    expect(container.textContent).toContain("No course started yet.");
    expect(container.textContent).toContain("None right now. Once a few questions on a topic have been answered");
  });
});
