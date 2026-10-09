import { describe, expect, it } from "vitest";
import { CLASS_NAME_MAX, normalizeClassName } from "@/lib/social/class-name";

describe("normalizeClassName", () => {
  it("trims the name", () => {
    expect(normalizeClassName("  Period 3 AP CSA  ")).toBe("Period 3 AP CSA");
  });

  it("refuses an empty or whitespace-only name, which the browser's 'required' lets through", () => {
    expect(normalizeClassName("")).toBeNull();
    expect(normalizeClassName("   ")).toBeNull();
  });

  it("refuses anything that is not text, such as a missing field or an uploaded file", () => {
    expect(normalizeClassName(null)).toBeNull();
    expect(normalizeClassName(new File(["x"], "x.txt"))).toBeNull();
  });

  it("accepts exactly the longest allowed name and refuses one character more", () => {
    expect(normalizeClassName("a".repeat(CLASS_NAME_MAX))).toBe("a".repeat(CLASS_NAME_MAX));
    expect(normalizeClassName("a".repeat(CLASS_NAME_MAX + 1))).toBeNull();
  });

  it("measures the length after trimming, so padding does not count against the limit", () => {
    expect(normalizeClassName(` ${"a".repeat(CLASS_NAME_MAX)} `)).toBe("a".repeat(CLASS_NAME_MAX));
  });
});
