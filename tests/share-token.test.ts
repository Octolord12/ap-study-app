import { describe, expect, it } from "vitest";
import { PARENT_LINK_DAYS } from "@/lib/share/constants";
import { hashShareToken, isShareUsable, looksLikeShareToken, newShareToken } from "@/lib/share/token";
import { hashResetToken } from "@/lib/auth/reset-token";

const DAY = 24 * 60 * 60 * 1000;

describe("newShareToken", () => {
  it("makes a 32-byte secret as 43 URL-safe characters, and returns its hash, not the secret, for storage", () => {
    const { token, tokenHash } = newShareToken();
    expect(token).toMatch(/^[A-Za-z0-9_-]{43}$/);
    expect(tokenHash).toMatch(/^[0-9a-f]{64}$/);
    expect(tokenHash).not.toContain(token);
    expect(tokenHash).toBe(hashShareToken(token));
  });

  it("is different every time", () => {
    expect(new Set(Array.from({ length: 50 }, () => newShareToken().token)).size).toBe(50);
  });

  it("expires PARENT_LINK_DAYS from now", () => {
    const now = new Date("2026-10-09T12:00:00Z");
    expect(newShareToken(now).expiresAt.getTime() - now.getTime()).toBe(PARENT_LINK_DAYS * DAY);
    expect(PARENT_LINK_DAYS).toBe(90);
  });

  it("takes its randomness from the secure source it is given (32 bytes)", () => {
    let asked = 0;
    const { token } = newShareToken(new Date(), (n) => {
      asked = n;
      return Buffer.alloc(n, 7);
    });
    expect(asked).toBe(32);
    expect(Buffer.from(token, "base64url")).toEqual(Buffer.alloc(32, 7));
  });
});

describe("hashShareToken", () => {
  it("is stable, and never equals the password-reset hash of the same text", () => {
    const t = "a".repeat(43);
    expect(hashShareToken(t)).toBe(hashShareToken(t));
    expect(hashShareToken(t)).not.toBe(hashResetToken(t));
  });
});

describe("looksLikeShareToken", () => {
  it("accepts only the exact shape, so junk in the URL never reaches the database", () => {
    expect(looksLikeShareToken(newShareToken().token)).toBe(true);
    for (const bad of ["", "short", "a".repeat(42), "a".repeat(44), `${"a".repeat(42)}!`, `${"a".repeat(42)} `, "../../etc/passwd", null, undefined, 42, ["x"]]) {
      expect(looksLikeShareToken(bad), String(bad)).toBe(false);
    }
  });
});

describe("isShareUsable", () => {
  const now = new Date("2026-10-09T12:00:00Z");
  it("is usable only while not revoked and not expired", () => {
    expect(isShareUsable({ revokedAt: null, expiresAt: new Date(now.getTime() + 1) }, now)).toBe(true);
    expect(isShareUsable({ revokedAt: null, expiresAt: now }, now)).toBe(false); // expires at that instant
    expect(isShareUsable({ revokedAt: null, expiresAt: new Date(now.getTime() - 1) }, now)).toBe(false);
    expect(isShareUsable({ revokedAt: new Date(now.getTime() - 1000), expiresAt: new Date(now.getTime() + DAY) }, now)).toBe(false);
  });
});
