import { beforeEach, describe, expect, it, vi } from "vitest";

const mocks = vi.hoisted(() => ({
  db: {
    user: { findFirst: vi.fn(async () => null), create: vi.fn(async () => ({})) },
  },
  signIn: vi.fn(async () => undefined),
}));

vi.mock("@/lib/db", () => ({ getDb: () => mocks.db }));
vi.mock("@/lib/auth/config", () => ({ signIn: mocks.signIn, signOut: vi.fn() }));
vi.mock("next-auth", () => ({ AuthError: class AuthError extends Error {} }));
vi.mock("bcryptjs", () => ({ default: { hash: vi.fn(async () => "hashed") } }));

import { MINIMUM_AGE } from "@/lib/age";
import { signUpAction } from "@/lib/auth/actions";
import { SignUpSchema } from "@/lib/auth/schema";

const valid = { displayName: "Test Student", username: "test_student", email: "test@example.com", password: "long-enough-pw" };

function form(fields: Record<string, string | undefined>) {
  const data = new FormData();
  for (const [key, value] of Object.entries(fields)) if (value !== undefined) data.set(key, value);
  return data;
}

describe("minimum age", () => {
  it("is 13", () => {
    expect(MINIMUM_AGE).toBe(13);
  });
});

describe("SignUpSchema age confirmation", () => {
  it("accepts a signup that confirms the age", () => {
    expect(SignUpSchema.safeParse({ ...valid, ageConfirmed: "yes" }).success).toBe(true);
  });

  it("rejects a missing, empty or other value, with a message that names the age", () => {
    for (const ageConfirmed of [undefined, null, "", "no", "on", "true"]) {
      const result = SignUpSchema.safeParse({ ...valid, ageConfirmed });
      expect(result.success).toBe(false);
      if (!result.success) expect(result.error.issues[0]?.message).toBe("You must be 13 or older to create an account.");
    }
  });
});

describe("signUpAction", () => {
  beforeEach(() => vi.clearAllMocks());

  it("creates no account, and signs nobody in, when the age box is not checked", async () => {
    const result = await signUpAction(undefined, form({ ...valid }));
    expect(result).toBe("You must be 13 or older to create an account.");
    expect(mocks.db.user.create).not.toHaveBeenCalled();
    expect(mocks.signIn).not.toHaveBeenCalled();
  });

  it("is not fooled by a different value for the field", async () => {
    await signUpAction(undefined, form({ ...valid, ageConfirmed: "off" }));
    expect(mocks.db.user.create).not.toHaveBeenCalled();
  });

  it("creates the account when the age is confirmed", async () => {
    await signUpAction(undefined, form({ ...valid, ageConfirmed: "yes" }));
    expect(mocks.db.user.create).toHaveBeenCalledTimes(1);
    expect(mocks.db.user.create).toHaveBeenCalledWith({
      data: expect.objectContaining({ email: "test@example.com", username: "test_student" }),
    });
    expect(mocks.signIn).toHaveBeenCalledTimes(1);
  });

  it("does not store the age confirmation on the user", async () => {
    await signUpAction(undefined, form({ ...valid, ageConfirmed: "yes" }));
    const data = (mocks.db.user.create.mock.calls[0] as unknown as [{ data: Record<string, unknown> }])[0].data;
    expect(Object.keys(data)).not.toContain("ageConfirmed");
  });
});
