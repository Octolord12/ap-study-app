import { describe, expect, it } from "vitest";
import { credentialsStamp, judgeStamp } from "@/lib/auth/credentials-stamp";

describe("credentialsStamp", () => {
  it("is stable for one hash and different for another", () => {
    const a = "$2b$12$aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa";
    const b = "$2b$12$bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb";
    expect(credentialsStamp(a)).toBe(credentialsStamp(a));
    expect(credentialsStamp(a)).not.toBe(credentialsStamp(b));
  });

  it("doesn't contain the hash it was made from", () => {
    const hash = "$2b$12$cccccccccccccccccccccccccccccccccccccccccccccccccccc";
    expect(hash).not.toContain(credentialsStamp(hash));
    expect(credentialsStamp(hash)).toMatch(/^[0-9a-f]{24}$/);
  });

  it("has a value for an account with no password", () => {
    expect(credentialsStamp(null)).toMatch(/^[0-9a-f]{24}$/);
  });
});

describe("judgeStamp", () => {
  it("accepts a token whose stamp is still current", () => {
    expect(judgeStamp("abc", "abc")).toEqual({ ok: true, stamp: "abc" });
  });

  it("rejects a token issued before the password changed", () => {
    expect(judgeStamp("old", "new")).toEqual({ ok: false });
  });

  it("rejects a token for an account that no longer exists", () => {
    expect(judgeStamp("abc", null)).toEqual({ ok: false });
    expect(judgeStamp(undefined, null)).toEqual({ ok: false });
  });

  it("adopts the current stamp for a token issued before stamps existed", () => {
    expect(judgeStamp(undefined, "now")).toEqual({ ok: true, stamp: "now" });
    expect(judgeStamp("", "now")).toEqual({ ok: true, stamp: "now" });
  });
});
