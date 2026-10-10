import { beforeEach, describe, expect, it, vi } from "vitest";

const mocks = vi.hoisted(() => ({
  userId: "u1" as string | null,
  role: "STUDENT" as string | null, // null = no such user row
  findUnique: vi.fn(),
  classFindMany: vi.fn(),
}));

vi.mock("@/lib/db", () => ({ getDb: () => ({ user: { findUnique: mocks.findUnique }, class: { findMany: mocks.classFindMany } }) }));
vi.mock("@/lib/auth/session", () => ({
  requireUserId: async () => {
    if (!mocks.userId) throw new Error("NEXT_REDIRECT:/login");
    return mocks.userId;
  },
}));
vi.mock("next/navigation", () => ({
  notFound: () => {
    throw new Error("NEXT_NOT_FOUND");
  },
}));

import { requireTeacherClasses } from "@/lib/teacher/classes";
import { isTeacherRole, requireTeacherUserId, userIsTeacher } from "@/lib/teacher/role";

describe("isTeacherRole", () => {
  it("is true for a teacher and for an admin, and for nothing else", () => {
    expect(isTeacherRole("TEACHER")).toBe(true);
    expect(isTeacherRole("ADMIN")).toBe(true);
    expect(isTeacherRole("STUDENT")).toBe(false);
    expect(isTeacherRole("teacher")).toBe(false);
    expect(isTeacherRole("")).toBe(false);
    expect(isTeacherRole(null)).toBe(false);
    expect(isTeacherRole(undefined)).toBe(false);
  });
});

describe("the teacher gate", () => {
  beforeEach(() => {
    vi.clearAllMocks();
    mocks.userId = "u1";
    mocks.role = "STUDENT";
    mocks.findUnique.mockImplementation(async () => (mocks.role === null ? null : { role: mocks.role }));
    mocks.classFindMany.mockImplementation(async () => [{ id: "c1", name: "Period 3", inviteCode: "ABC234", course: null, _count: { memberships: 3 } }]);
  });

  it("lets a teacher in and returns their id", async () => {
    mocks.role = "TEACHER";
    await expect(requireTeacherUserId()).resolves.toBe("u1");
  });

  it("lets an admin in", async () => {
    mocks.role = "ADMIN";
    await expect(requireTeacherUserId()).resolves.toBe("u1");
  });

  it("shows a student a 404, even one who owns a class", async () => {
    mocks.role = "STUDENT";
    await expect(requireTeacherUserId()).rejects.toThrow("NEXT_NOT_FOUND");
    await expect(requireTeacherClasses()).rejects.toThrow("NEXT_NOT_FOUND");
    expect(mocks.classFindMany).not.toHaveBeenCalled(); // never even looks at their classes
  });

  it("shows a 404 when the account no longer exists", async () => {
    mocks.role = null;
    await expect(requireTeacherUserId()).rejects.toThrow("NEXT_NOT_FOUND");
  });

  it("sends a signed-out visitor to sign in (the session check runs first)", async () => {
    mocks.userId = null;
    await expect(requireTeacherUserId()).rejects.toThrow("NEXT_REDIRECT:/login");
    expect(mocks.findUnique).not.toHaveBeenCalled();
  });

  it("reads the role for the signed-in user only", async () => {
    mocks.role = "TEACHER";
    await requireTeacherUserId();
    expect(mocks.findUnique.mock.calls[0][0].where).toEqual({ id: "u1" });
  });

  it("gives a teacher their own classes, and an empty list (not a 404) while they have none", async () => {
    mocks.role = "TEACHER";
    expect((await requireTeacherClasses()).classes.map((c) => c.id)).toEqual(["c1"]);
    expect(mocks.classFindMany.mock.calls[0][0].where).toEqual({ ownerId: "u1" });
    mocks.classFindMany.mockImplementation(async () => []);
    expect((await requireTeacherClasses()).classes).toEqual([]);
  });

  it("userIsTeacher answers yes or no without throwing", async () => {
    mocks.role = "TEACHER";
    expect(await userIsTeacher("u1")).toBe(true);
    mocks.role = "STUDENT";
    expect(await userIsTeacher("u1")).toBe(false);
    mocks.role = null;
    expect(await userIsTeacher("u1")).toBe(false);
  });
});
