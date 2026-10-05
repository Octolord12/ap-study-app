import { describe, expect, it } from "vitest";
import { isPasswordTooLong } from "@/lib/auth/password";
import { ChangePasswordSchema, DeleteAccountSchema, SignUpSchema } from "@/lib/auth/schema";

const change = (over: Record<string, unknown> = {}) =>
  ChangePasswordSchema.safeParse({ currentPassword: "old-password", newPassword: "new-password-1", confirmPassword: "new-password-1", ...over });
const message = (r: ReturnType<typeof change>) => (r.success ? null : r.error.issues[0]?.message);

describe("ChangePasswordSchema", () => {
  it("accepts a valid change", () => {
    expect(change().success).toBe(true);
  });

  it("needs the current password", () => {
    expect(message(change({ currentPassword: "" }))).toBe("Enter your current password");
  });

  it("holds the new password to the same rules as signup", () => {
    expect(message(change({ newPassword: "short", confirmPassword: "short" }))).toBe("At least 8 characters");
  });

  it("makes sure the two new passwords match", () => {
    expect(message(change({ confirmPassword: "something-else" }))).toBe("The new passwords don't match.");
  });

  it("refuses a 'new' password that is the same as the current one", () => {
    expect(message(change({ currentPassword: "same-password", newPassword: "same-password", confirmPassword: "same-password" }))).toBe(
      "The new password is the same as the current one.",
    );
  });
});

describe("password length limit (bcrypt reads 72 bytes)", () => {
  it("counts bytes, not characters", () => {
    expect(isPasswordTooLong("a".repeat(72))).toBe(false);
    expect(isPasswordTooLong("a".repeat(73))).toBe(true);
    expect(isPasswordTooLong("é".repeat(36))).toBe(false); // 72 bytes
    expect(isPasswordTooLong("é".repeat(37))).toBe(true); // 74 bytes, only 37 characters
    expect(isPasswordTooLong("😀".repeat(19))).toBe(true); // 76 bytes
  });

  it("is enforced when signing up and when changing a password", () => {
    const long = "é".repeat(37);
    expect(SignUpSchema.safeParse({ displayName: "A", username: "abc", email: "a@example.com", password: long, ageConfirmed: "yes" }).success).toBe(false);
    expect(message(change({ newPassword: long, confirmPassword: long }))).toBe("That password is too long. Use a shorter one.");
  });
});

describe("DeleteAccountSchema", () => {
  it("needs the password and the confirmation", () => {
    expect(DeleteAccountSchema.safeParse({ password: "pw", understand: "yes" }).success).toBe(true);
    expect(DeleteAccountSchema.safeParse({ password: "", understand: "yes" }).success).toBe(false);
    for (const understand of [undefined, null, "", "no", "on", "true"]) {
      const r = DeleteAccountSchema.safeParse({ password: "pw", understand });
      expect(r.success).toBe(false);
      if (!r.success) expect(r.error.issues[0]?.message).toBe("Tick the box to confirm you want to delete your account.");
    }
  });
});
