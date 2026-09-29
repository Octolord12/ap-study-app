import { describe, expect, it } from "vitest";
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
});

describe("normalizeInviteCode", () => {
  it("trims whitespace and uppercases", () => {
    expect(normalizeInviteCode("  ab12cd  ")).toBe("AB12CD");
  });
});
