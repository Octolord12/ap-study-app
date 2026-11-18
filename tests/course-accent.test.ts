import { readdirSync, readFileSync } from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";
import { COURSE_ACCENT_KEYS, courseAccent, courseTabLabel } from "@/lib/content/course-accent";

const root = path.resolve(import.meta.dirname, "..");
const css = readFileSync(path.join(root, "src/app/globals.css"), "utf8");
const courseSlugs = readdirSync(path.join(root, "content"), { withFileTypes: true })
  .filter((entry) => entry.isDirectory())
  .map((entry) => entry.name);

describe("course accent colors", () => {
  it("gives every course in /content its own key", () => {
    const keys = courseSlugs.map((slug) => courseAccent(slug));
    expect(keys.every(Boolean), `no accent for: ${courseSlugs.filter((s) => !courseAccent(s)).join(", ")}`).toBe(true);
    expect(new Set(keys).size).toBe(courseSlugs.length);
  });

  it("has a color rule in globals.css for every key, so a course never silently falls back to the default", () => {
    for (const key of COURSE_ACCENT_KEYS) {
      expect(css, key).toMatch(new RegExp(`\\[data-c="${key}"\\]\\s*\\{\\s*--c:\\s*#[0-9a-f]{6};`));
    }
  });

  it("re-declares --mark on every [data-c] element (var() is resolved where it is declared)", () => {
    expect(css).toMatch(/:root,\s*\[data-c\]\s*\{[^}]*--mark:\s*var\(--c\)/);
  });

  it("keeps the colors in step with the ink the tabs carry (every pair is at least 6:1)", () => {
    const luminance = (hex: string) => {
      const [r, g, b] = [1, 3, 5].map((i) => parseInt(hex.slice(i, i + 2), 16) / 255).map((c) => (c <= 0.03928 ? c / 12.92 : ((c + 0.055) / 1.055) ** 2.4));
      return 0.2126 * r + 0.7152 * g + 0.0722 * b;
    };
    const ink = css.match(/--on-mark:\s*(#[0-9a-f]{6})/)![1];
    for (const key of COURSE_ACCENT_KEYS) {
      const color = css.match(new RegExp(`\\[data-c="${key}"\\]\\s*\\{\\s*--c:\\s*(#[0-9a-f]{6})`))![1];
      const [hi, lo] = [luminance(color), luminance(ink)].sort((a, b) => b - a);
      expect((hi + 0.05) / (lo + 0.05), `${key} ${color} on ${ink}`).toBeGreaterThanOrEqual(6);
    }
  });

  it("falls back for a course it does not know", () => {
    expect(courseAccent("ap-something-new")).toBeUndefined();
    expect(courseTabLabel("ap-something-new", "AP Something New")).toBe("AP Something New");
    expect(courseTabLabel("ap-calc-bc", "AP Calculus BC")).toBe("Calc BC");
  });
});
