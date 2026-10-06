import { beforeEach, describe, expect, it, vi } from "vitest";

// approveUnitContent with the database and session faked. What matters: only an admin can run it, and it can
// only ever touch the rows it was handed that still belong to the unit and are still unreviewed.

const mocks = vi.hoisted(() => {
  const state = { userId: "u-admin" as string | null, role: "ADMIN" as string };
  const db = {
    user: { findUnique: vi.fn(async () => ({ role: state.role })) },
    question: { updateMany: vi.fn(async ({ where }: { where: { id: { in: string[] } } }) => ({ count: where.id.in.length })) },
    fRQPrompt: { updateMany: vi.fn(async ({ where }: { where: { id: { in: string[] } } }) => ({ count: where.id.in.length })) },
  };
  const revalidatePath = vi.fn();
  return { state, db, revalidatePath };
});

vi.mock("@/lib/db", () => ({ getDb: () => mocks.db }));
vi.mock("@/lib/auth/config", () => ({ auth: async () => (mocks.state.userId ? { user: { id: mocks.state.userId } } : null) }));
vi.mock("next/cache", () => ({ revalidatePath: mocks.revalidatePath }));
vi.mock("next/navigation", () => ({
  redirect: (to: string) => {
    throw new Error(`redirect:${to}`);
  },
  notFound: () => {
    throw new Error("not-found");
  },
}));

import { approveUnitContent } from "@/lib/admin/actions";

describe("approveUnitContent", () => {
  beforeEach(() => {
    vi.clearAllMocks();
    mocks.state.userId = "u-admin";
    mocks.state.role = "ADMIN";
  });

  it("approves the given questions and prompts of the unit, only those still unreviewed, and reports the total", async () => {
    const result = await approveUnitContent("unit-1", ["q1", "q2", "q3"], ["f1", "f2"]);
    expect(result).toEqual({ approved: 5 });
    expect(mocks.db.question.updateMany).toHaveBeenCalledWith({ where: { id: { in: ["q1", "q2", "q3"] }, unitId: "unit-1", reviewed: false }, data: { reviewed: true } });
    expect(mocks.db.fRQPrompt.updateMany).toHaveBeenCalledWith({ where: { id: { in: ["f1", "f2"] }, unitId: "unit-1", reviewed: false }, data: { reviewed: true } });
    expect(mocks.revalidatePath).toHaveBeenCalledWith("/admin/review");
  });

  it("skips the query for an empty list", async () => {
    await approveUnitContent("unit-1", ["q1"], []);
    expect(mocks.db.fRQPrompt.updateMany).not.toHaveBeenCalled();
  });

  it("refuses a student and changes nothing", async () => {
    mocks.state.role = "STUDENT";
    await expect(approveUnitContent("unit-1", ["q1"], [])).rejects.toThrow("not-found");
    expect(mocks.db.question.updateMany).not.toHaveBeenCalled();
    expect(mocks.db.fRQPrompt.updateMany).not.toHaveBeenCalled();
  });

  it("refuses someone signed out", async () => {
    mocks.state.userId = null;
    await expect(approveUnitContent("unit-1", ["q1"], [])).rejects.toThrow("redirect:/login");
    expect(mocks.db.question.updateMany).not.toHaveBeenCalled();
  });

  it("refuses an absurdly long list", async () => {
    const many = Array.from({ length: 501 }, (_, i) => `q${i}`);
    await expect(approveUnitContent("unit-1", many, [])).rejects.toThrow("Too many items");
    expect(mocks.db.question.updateMany).not.toHaveBeenCalled();
  });
});
