// Each course has one color, the divider tab of the binder. The color itself lives in globals.css
// (`[data-c="<key>"] { --c: ... }`); this file maps a course slug to its key and its short tab label.
// A slug that is not listed (a course added later) gets no key and so the default color.

interface Accent {
  key: string;
  tab: string;
}

const ACCENTS: Readonly<Record<string, Accent>> = {
  "ap-csa": { key: "csa", tab: "CSA" },
  "ap-world": { key: "world", tab: "World" },
  "ap-us-history": { key: "ush", tab: "U.S." },
  "ap-calc": { key: "ab", tab: "Calc AB" },
  "ap-calc-bc": { key: "bc", tab: "Calc BC" },
  "ap-physics-1": { key: "phys", tab: "Phys 1" },
  "ap-biology": { key: "bio", tab: "Bio" },
  "ap-statistics": { key: "stats", tab: "Stats" },
};

export const COURSE_ACCENT_KEYS: readonly string[] = Object.values(ACCENTS).map((a) => a.key);

export function courseAccent(courseSlug: string): string | undefined {
  return ACCENTS[courseSlug]?.key;
}

export function courseTabLabel(courseSlug: string, fallback: string): string {
  return ACCENTS[courseSlug]?.tab ?? fallback;
}
