import { beforeEach, describe, expect, it, vi } from "vitest";

const mocks = vi.hoisted(() => ({
  userId: "user-1" as string | null,
  updated: 1,
  db: { enrollment: { updateMany: vi.fn() } },
  revalidatePath: vi.fn(),
}));
mocks.db.enrollment.updateMany.mockImplementation(async () => ({ count: mocks.updated }));

vi.mock("@/lib/db", () => ({ getDb: () => mocks.db }));
vi.mock("@/lib/auth/config", () => ({ auth: async () => (mocks.userId ? { user: { id: mocks.userId } } : null) }));
vi.mock("next/cache", () => ({ revalidatePath: mocks.revalidatePath }));

import { setExamDate } from "@/lib/study/exam-date-actions";

const form = (fields: Record<string, string>) => {
  const data = new FormData();
  for (const [k, v] of Object.entries(fields)) data.set(k, v);
  return data;
};
const future = (days: number) => new Date(Date.now() + days * 86_400_000).toISOString().slice(0, 10);

describe("setExamDate", () => {
  beforeEach(() => {
    vi.clearAllMocks();
    mocks.userId = "user-1";
    mocks.updated = 1;
  });

  it("saves a future date as a calendar date, for the signed-in student's own enrollment only", async () => {
    const day = future(90);
    const result = await setExamDate("course-1", {}, form({ examDate: day }));
    expect(result).toEqual({ message: "Saved." });
    expect(mocks.db.enrollment.updateMany).toHaveBeenCalledWith({
      where: { userId: "user-1", courseId: "course-1" },
      data: { examDate: new Date(`${day}T00:00:00.000Z`) },
    });
    expect(mocks.revalidatePath).toHaveBeenCalled();
  });

  it("ignores a user id smuggled into the form: the session decides whose enrollment changes", async () => {
    await setExamDate("course-1", {}, form({ examDate: future(30), userId: "someone-else", courseId: "other-course" }));
    expect(mocks.db.enrollment.updateMany.mock.calls[0][0].where).toEqual({ userId: "user-1", courseId: "course-1" });
  });

  it("clears the date", async () => {
    const result = await setExamDate("course-1", {}, form({ intent: "clear" }));
    expect(result).toEqual({ message: "Date removed." });
    expect(mocks.db.enrollment.updateMany).toHaveBeenCalledWith({ where: { userId: "user-1", courseId: "course-1" }, data: { examDate: null } });
  });

  it("refuses bad input without touching the database", async () => {
    for (const [value, error] of [
      ["", "Pick a date."],
      ["2027-02-30", "That isn't a real date."],
      ["not a date", "That isn't a real date."],
      [future(-30), "That date has already passed."],
      [future(2000), "Pick a date within the next two years."],
    ] as const) {
      expect(await setExamDate("course-1", {}, form({ examDate: value }))).toEqual({ error });
    }
    expect(mocks.db.enrollment.updateMany).not.toHaveBeenCalled();
  });

  it("says to start the course first when the student isn't enrolled, and doesn't pretend it saved", async () => {
    mocks.updated = 0;
    const result = await setExamDate("course-1", {}, form({ examDate: future(30) }));
    expect(result).toEqual({ error: "Start studying this course first." });
    expect(mocks.revalidatePath).not.toHaveBeenCalled();
  });

  it("requires a signed-in student", async () => {
    mocks.userId = null;
    await expect(setExamDate("course-1", {}, form({ examDate: future(30) }))).rejects.toThrow("Not authenticated");
    expect(mocks.db.enrollment.updateMany).not.toHaveBeenCalled();
  });
});
