import { describe, expect, it } from "vitest";
import { hashResetToken, looksLikeResetToken, newResetToken } from "@/lib/auth/reset-token";
import { RESET_TOKEN_MINUTES } from "@/lib/auth/reset-constants";

describe("newResetToken", () => {
  it("makes a 43-character url-safe code, and stores only its SHA-256", () => {
    const { token, tokenHash } = newResetToken();
    expect(token).toMatch(/^[A-Za-z0-9_-]{43}$/);
    expect(tokenHash).toMatch(/^[0-9a-f]{64}$/);
    expect(tokenHash).not.toContain(token);
    expect(hashResetToken(token)).toBe(tokenHash);
  });

  it("expires after the stated number of minutes", () => {
    const now = new Date("2026-10-05T12:00:00Z");
    expect(newResetToken(now).expiresAt.toISOString()).toBe(new Date(now.getTime() + RESET_TOKEN_MINUTES * 60_000).toISOString());
  });

  it("never repeats", () => {
    const seen = new Set(Array.from({ length: 500 }, () => newResetToken().token));
    expect(seen.size).toBe(500);
  });

  it("is deterministic only through the injected randomness (the real source is crypto-random)", () => {
    const fixed = (n: number) => Buffer.alloc(n, 7);
    expect(newResetToken(new Date(), fixed).token).toBe(newResetToken(new Date(), fixed).token);
  });
});

describe("looksLikeResetToken", () => {
  it("accepts a real code and rejects anything else", () => {
    expect(looksLikeResetToken(newResetToken().token)).toBe(true);
    for (const bad of ["", "abc", "a".repeat(42), "a".repeat(44), "a".repeat(42) + "!", "a".repeat(42) + " ", undefined, null, 12, ["x"]]) {
      expect(looksLikeResetToken(bad)).toBe(false);
    }
  });
});
