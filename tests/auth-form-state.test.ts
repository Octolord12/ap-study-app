import { beforeEach, describe, expect, it, vi } from "vitest";

const mocks = vi.hoisted(() => ({
  db: { user: { findFirst: vi.fn(async () => null as null | { email: string; username: string }), create: vi.fn(async () => ({})) } },
  signIn: vi.fn(async () => undefined as unknown),
}));

vi.mock("@/lib/db", () => ({ getDb: () => mocks.db }));
vi.mock("@/lib/auth/config", () => ({ signIn: mocks.signIn, signOut: vi.fn() }));
vi.mock("next-auth", () => ({ AuthError: class AuthError extends Error {} }));
vi.mock("bcryptjs", () => ({ default: { hash: vi.fn(async () => "hashed") } }));

import { AuthError } from "next-auth";
import { loginAction, signUpAction } from "@/lib/auth/actions";

const PASSWORD = "correct-horse-battery-staple";

function form(fields: Record<string, string>) {
  const data = new FormData();
  for (const [k, v] of Object.entries(fields)) data.set(k, v);
  return data;
}

describe("signUpAction gives the form back what was typed", () => {
  beforeEach(() => {
    vi.clearAllMocks();
    mocks.db.user.findFirst.mockResolvedValue(null);
  });

  const typed = { displayName: "Sam Student", username: "sam_s", email: "sam@example.com", password: PASSWORD };

  it("after a validation error (here: age box unchecked)", async () => {
    const result = await signUpAction({}, form(typed));
    expect(result.error).toBe("You must be 13 or older to create an account.");
    expect(result.values).toEqual({ displayName: "Sam Student", username: "sam_s", email: "sam@example.com", ageConfirmed: false });
  });

  it("remembers that the age box was checked", async () => {
    const result = await signUpAction({}, form({ ...typed, username: "x", ageConfirmed: "yes" }));
    expect(result.error).toBeDefined();
    expect(result.values?.ageConfirmed).toBe(true);
  });

  it("after a duplicate-account error", async () => {
    mocks.db.user.findFirst.mockResolvedValue({ email: "other@example.com", username: "sam_s" });
    const result = await signUpAction({}, form({ ...typed, ageConfirmed: "yes" }));
    expect(result.error).toBe("That username is taken.");
    expect(result.values).toMatchObject({ username: "sam_s", email: "sam@example.com", displayName: "Sam Student", ageConfirmed: true });
    expect(mocks.db.user.create).not.toHaveBeenCalled();
  });

  it("never sends the password back", async () => {
    mocks.db.user.findFirst.mockResolvedValue({ email: "sam@example.com", username: "other" });
    for (const fields of [typed, { ...typed, ageConfirmed: "yes" }]) {
      const result = await signUpAction({}, form(fields));
      expect(JSON.stringify(result)).not.toContain(PASSWORD);
      expect(Object.keys(result.values ?? {})).not.toContain("password");
    }
  });

  it("caps what it echoes, and ignores non-text fields", async () => {
    const data = form({ ...typed, displayName: "x".repeat(5000) });
    data.set("username", new File(["x"], "x.txt"));
    const result = await signUpAction({}, data);
    expect(result.values?.displayName).toHaveLength(254);
    expect(result.values?.username).toBe("");
  });
});

describe("loginAction gives the form back the email", () => {
  beforeEach(() => vi.clearAllMocks());

  it("after a validation error", async () => {
    const result = await loginAction({}, form({ email: "sam@example.com", password: "" }));
    expect(result.error).toBeDefined();
    expect(result.values).toEqual({ email: "sam@example.com" });
  });

  it("after wrong credentials, and never the password", async () => {
    mocks.signIn.mockRejectedValue(new AuthError());
    const result = await loginAction({}, form({ email: "sam@example.com", password: PASSWORD }));
    expect(result.error).toBe("Incorrect email or password.");
    expect(result.values).toEqual({ email: "sam@example.com" });
    expect(JSON.stringify(result)).not.toContain(PASSWORD);
  });

  it("still lets the success redirect (any other error) through instead of swallowing it", async () => {
    const redirect = new Error("NEXT_REDIRECT");
    mocks.signIn.mockRejectedValue(redirect);
    await expect(loginAction({}, form({ email: "sam@example.com", password: PASSWORD }))).rejects.toBe(redirect);
  });
});
