import { beforeEach, describe, expect, it, vi } from "vitest";

const mocks = vi.hoisted(() => ({
  done: false,
  ids: ["q1", "q2", "q3", "q4", "q5"] as string[],
  redirect: vi.fn((url: string) => {
    throw new Error(`NEXT_REDIRECT:${url}`);
  }),
  db: { course: { findUnique: vi.fn(async () => ({ id: "c1", slug: "ap-calc", name: "AP Calculus AB" })) }, questionAttempt: { findMany: vi.fn(async () => []) } },
}));

vi.mock("next/navigation", () => ({ redirect: mocks.redirect, notFound: () => { throw new Error("NEXT_NOT_FOUND"); } }));
vi.mock("@/lib/auth/session", () => ({ requireUserId: async () => "user-1" }));
vi.mock("@/lib/db", () => ({ getDb: () => mocks.db }));
vi.mock("@/lib/study/queries", () => ({
  hasCompletedDailyChallengeToday: async () => mocks.done,
  pickDailyChallengeQuestionIds: async () => mocks.ids,
}));

import DailyChallengePage from "@/app/courses/[courseSlug]/daily/page";

const run = () => DailyChallengePage({ params: Promise.resolve({ courseSlug: "ap-calc" }) });

describe("daily challenge page", () => {
  beforeEach(() => {
    mocks.done = false;
    mocks.ids = ["q1", "q2", "q3", "q4", "q5"];
    mocks.redirect.mockClear();
  });

  it("goes straight into today's questions instead of showing a page that asks for another click", async () => {
    await expect(run()).rejects.toThrow(/NEXT_REDIRECT/);
    const url = mocks.redirect.mock.calls[0][0] as string;
    expect(url.startsWith("/courses/ap-calc/quiz?")).toBe(true);
    const params = new URLSearchParams(url.split("?")[1]);
    expect(params.get("ids")).toBe("q1,q2,q3,q4,q5");
    expect(params.get("source")).toBe("DAILY");
    expect(params.get("back")).toBe("/courses/ap-calc/practice");
  });

  it("still shows today's result, not a redirect, once the set is done", async () => {
    mocks.done = true;
    const page = await run();
    expect(mocks.redirect).not.toHaveBeenCalled();
    expect(page).toBeTruthy();
  });

  it("says so, rather than redirecting, when the course has no questions", async () => {
    mocks.ids = [];
    const page = await run();
    expect(mocks.redirect).not.toHaveBeenCalled();
    expect(page).toBeTruthy();
  });
});
