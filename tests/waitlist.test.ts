import { describe, expect, it } from "vitest";
import { WaitlistSchema } from "@/lib/marketing/waitlist";

describe("WaitlistSchema", () => {
  it("trims and lowercases so case variants are one signup", () => {
    const parsed = WaitlistSchema.parse({ email: "  Student@Example.COM " });
    expect(parsed.email).toBe("student@example.com");
  });

  it("rejects things that are not email addresses", () => {
    for (const bad of ["", "   ", "not-an-email", "a@b", "two@@example.com"]) {
      expect(WaitlistSchema.safeParse({ email: bad }).success).toBe(false);
    }
  });

  it("rejects a missing field", () => {
    expect(WaitlistSchema.safeParse({ email: null }).success).toBe(false);
  });

  it("rejects addresses longer than 254 characters", () => {
    const long = `${"a".repeat(250)}@example.com`;
    const result = WaitlistSchema.safeParse({ email: long });
    expect(result.success).toBe(false);
    if (!result.success) expect(result.error.issues[0]?.message).toBe("That email address is too long.");
  });
});
