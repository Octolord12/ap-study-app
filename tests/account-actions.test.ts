import { beforeEach, describe, expect, it, vi } from "vitest";

const mocks = vi.hoisted(() => ({
  userId: "user-1" as string | null,
  row: { email: "Sam@Example.com", passwordHash: "hashed:current-password" } as { email: string; passwordHash: string | null } | null,
  db: {
    user: { findUnique: vi.fn(), update: vi.fn(), delete: vi.fn() },
    waitlistSignup: { deleteMany: vi.fn() },
    $transaction: vi.fn(),
  },
  signOut: vi.fn(),
}));

mocks.db.user.findUnique.mockImplementation(async () => mocks.row);
mocks.db.user.update.mockImplementation(async () => ({}));
mocks.db.user.delete.mockImplementation(async () => ({}));
mocks.db.waitlistSignup.deleteMany.mockImplementation(async () => ({ count: 1 }));
mocks.db.$transaction.mockImplementation(async (ops: Promise<unknown>[]) => Promise.all(ops));
mocks.signOut.mockImplementation(async () => {
  throw new Error("NEXT_REDIRECT");
});

vi.mock("@/lib/db", () => ({ getDb: () => mocks.db }));
vi.mock("@/lib/auth/config", () => ({ auth: async () => (mocks.userId ? { user: { id: mocks.userId } } : null), signOut: mocks.signOut }));
vi.mock("bcryptjs", () => ({
  default: {
    compare: vi.fn(async (pw: string, hash: string) => hash === `hashed:${pw}`),
    hash: vi.fn(async (pw: string) => `hashed:${pw}`),
  },
}));

import { changePasswordAction, deleteAccountAction } from "@/lib/auth/account-actions";

const form = (fields: Record<string, string>) => {
  const data = new FormData();
  for (const [k, v] of Object.entries(fields)) data.set(k, v);
  return data;
};
const change = (over: Record<string, string> = {}) =>
  form({ currentPassword: "current-password", newPassword: "brand-new-pass", confirmPassword: "brand-new-pass", ...over });

beforeEach(() => {
  vi.clearAllMocks();
  mocks.userId = "user-1";
  mocks.row = { email: "Sam@Example.com", passwordHash: "hashed:current-password" };
});

describe("changePasswordAction", () => {
  it("stores the new password, hashed, on the signed-in student's own account only", async () => {
    expect(await changePasswordAction({}, change())).toEqual({ message: "Password changed." });
    expect(mocks.db.user.update).toHaveBeenCalledWith({ where: { id: "user-1" }, data: { passwordHash: "hashed:brand-new-pass" } });
  });

  it("refuses a wrong current password and changes nothing", async () => {
    expect(await changePasswordAction({}, change({ currentPassword: "not-it" }))).toEqual({ error: "That isn't your current password." });
    expect(mocks.db.user.update).not.toHaveBeenCalled();
  });

  it("refuses bad input before it even looks the account up", async () => {
    const badInputs: Record<string, string>[] = [
      { confirmPassword: "different" },
      { newPassword: "short", confirmPassword: "short" },
      { newPassword: "current-password", confirmPassword: "current-password" },
    ];
    for (const bad of badInputs) {
      const result = await changePasswordAction({}, change(bad));
      expect(result.error).toBeDefined();
    }
    expect(mocks.db.user.findUnique).not.toHaveBeenCalled();
    expect(mocks.db.user.update).not.toHaveBeenCalled();
  });

  it("ignores a user id smuggled into the form", async () => {
    await changePasswordAction({}, change({ userId: "someone-else", id: "someone-else" }));
    expect(mocks.db.user.update.mock.calls[0][0].where).toEqual({ id: "user-1" });
  });

  it("says so for an account that has no password", async () => {
    mocks.row = { email: "a@b.c", passwordHash: null };
    expect(await changePasswordAction({}, change())).toEqual({ error: "This account doesn't use a password." });
    expect(mocks.db.user.update).not.toHaveBeenCalled();
  });

  it("never sends any password back to the browser", async () => {
    for (const fields of [change(), change({ currentPassword: "wrong" }), change({ confirmPassword: "nope" })]) {
      const json = JSON.stringify(await changePasswordAction({}, fields));
      for (const secret of ["current-password", "brand-new-pass", "hashed:", "wrong", "nope"]) expect(json).not.toContain(secret);
    }
  });

  it("requires a signed-in student", async () => {
    mocks.userId = null;
    await expect(changePasswordAction({}, change())).rejects.toThrow("Not authenticated");
    expect(mocks.db.user.update).not.toHaveBeenCalled();
  });
});

describe("deleteAccountAction", () => {
  const del = (over: Record<string, string> = {}) => form({ password: "current-password", understand: "yes", ...over });

  it("deletes the signed-in student's account and their waitlist signup, then signs them out", async () => {
    await expect(deleteAccountAction({}, del())).rejects.toThrow("NEXT_REDIRECT");
    expect(mocks.db.$transaction).toHaveBeenCalledTimes(1);
    expect(mocks.db.user.delete).toHaveBeenCalledWith({ where: { id: "user-1" } });
    // The waitlist stores emails lowercased, whatever case the account used.
    expect(mocks.db.waitlistSignup.deleteMany).toHaveBeenCalledWith({ where: { email: "sam@example.com" } });
    expect(mocks.signOut).toHaveBeenCalledWith({ redirectTo: "/account-deleted" });
  });

  it("refuses a wrong password and deletes nothing", async () => {
    expect(await deleteAccountAction({}, del({ password: "not-it" }))).toEqual({ error: "That isn't your password." });
    expect(mocks.db.$transaction).not.toHaveBeenCalled();
    expect(mocks.db.user.delete).not.toHaveBeenCalled();
    expect(mocks.signOut).not.toHaveBeenCalled();
  });

  it("refuses without the confirmation tick, however the field is faked", async () => {
    for (const understand of ["", "no", "on", "true"]) {
      const result = await deleteAccountAction({}, del({ understand }));
      expect(result.error).toBe("Tick the box to confirm you want to delete your account.");
    }
    expect(await deleteAccountAction({}, form({ password: "current-password" }))).toHaveProperty("error");
    expect(mocks.db.user.delete).not.toHaveBeenCalled();
  });

  it("ignores a user id smuggled into the form: only the session's account can be deleted", async () => {
    await expect(deleteAccountAction({}, del({ userId: "someone-else" }))).rejects.toThrow();
    expect(mocks.db.user.delete).toHaveBeenCalledWith({ where: { id: "user-1" } });
    expect(mocks.db.user.delete).not.toHaveBeenCalledWith({ where: { id: "someone-else" } });
  });

  it("says so for an account that has no password, and deletes nothing", async () => {
    mocks.row = { email: "a@b.c", passwordHash: null };
    expect(await deleteAccountAction({}, del())).toEqual({ error: "This account doesn't use a password." });
    expect(mocks.db.user.delete).not.toHaveBeenCalled();
  });

  it("requires a signed-in student", async () => {
    mocks.userId = null;
    await expect(deleteAccountAction({}, del())).rejects.toThrow("Not authenticated");
    expect(mocks.db.user.delete).not.toHaveBeenCalled();
  });
});
