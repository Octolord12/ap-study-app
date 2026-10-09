import { describe, expect, it, vi } from "vitest";
import { generateInviteCode, normalizeInviteCode } from "@/lib/social/invite-code";

describe("generateInviteCode", () => {
  it("generates a 6-character code", () => {
    expect(generateInviteCode()).toHaveLength(6);
  });

  it("never includes visually ambiguous characters", () => {
    for (let i = 0; i < 50; i++) {
      expect(generateInviteCode()).not.toMatch(/[01OIL]/);
    }
  });

  it("is uppercase", () => {
    const code = generateInviteCode();
    expect(code).toBe(code.toUpperCase());
  });

  it("does not use Math.random: a code lets someone into a class, and Math.random's output can be predicted from earlier output", () => {
    const spy = vi.spyOn(Math, "random");
    try {
      for (let i = 0; i < 200; i++) generateInviteCode();
      expect(spy).not.toHaveBeenCalled();
    } finally {
      spy.mockRestore();
    }
  });

  it("uses every character of the alphabet about equally often, and nothing else", () => {
    const ALPHABET = "ABCDEFGHJKMNPQRSTUVWXYZ23456789";
    const counts = new Map<string, number>();
    const CODES = 60_000;
    for (let i = 0; i < CODES; i++) for (const ch of generateInviteCode()) counts.set(ch, (counts.get(ch) ?? 0) + 1);
    expect([...counts.keys()].sort().join("")).toBe([...ALPHABET].sort().join(""));
    // About 11,600 each with a standard deviation of about 106 (0.9%), so 5% is 5.5 sigma: it will not fail by chance, but it does catch
    // `randomInt(256) % 31`, which favors the first 8 characters by 9%.
    const expected = (CODES * 6) / ALPHABET.length;
    for (const [ch, n] of counts) expect(Math.abs(n - expected) / expected, ch).toBeLessThan(0.05);
  });

  it("gives different codes on repeated calls", () => {
    expect(new Set(Array.from({ length: 200 }, () => generateInviteCode())).size).toBeGreaterThan(195);
  });
});

describe("normalizeInviteCode", () => {
  it("trims whitespace and uppercases", () => {
    expect(normalizeInviteCode("  ab12cd  ")).toBe("AB12CD");
  });
});
