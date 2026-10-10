import { beforeEach, describe, expect, it, vi } from "vitest";

const mocks = vi.hoisted(() => ({ topics: [] as unknown[], findMany: vi.fn() }));
vi.mock("@/lib/db", () => ({ getDb: () => ({ topic: { findMany: mocks.findMany } }) }));

import {
  MAX_RESULTS,
  makeSnippet,
  normalizeSearchQuery,
  rankHits,
  searchRefreshers,
  splitHighlight,
  toPlainText,
  type RefresherCandidate,
} from "@/lib/study/refresher-search";

const MVT = `### The idea
The **Mean Value Theorem** says that if $f$ is continuous on $[a, b]$ and differentiable on $(a, b)$, some point $c$ has
$$
f'(c) = \\dfrac{f(b) - f(a)}{b - a}.
$$

### Key facts
- It needs both conditions. Without differentiability the guarantee fails.
- Think of the average rate of change matching an instantaneous rate somewhere.`;

const topic = (name: string, slug: string, order: number, refresher: string | null, unit = { slug: "unit-5", name: "Analytical Applications", order: 5 }): RefresherCandidate => ({
  name,
  slug,
  order,
  refresher,
  unit,
});

describe("normalizeSearchQuery", () => {
  it("trims and collapses whitespace", () => {
    expect(normalizeSearchQuery("  mean   value  ")).toBe("mean value");
  });

  it("is null when too short, too long, missing or not a single string", () => {
    expect(normalizeSearchQuery("a")).toBeNull();
    expect(normalizeSearchQuery("   ")).toBeNull();
    expect(normalizeSearchQuery("x".repeat(61))).toBeNull();
    expect(normalizeSearchQuery(undefined)).toBeNull();
    expect(normalizeSearchQuery(["mean", "value"])).toBeNull();
  });

  it("accepts exactly the limits", () => {
    expect(normalizeSearchQuery("ab")).toBe("ab");
    expect(normalizeSearchQuery("x".repeat(60))).toBe("x".repeat(60));
  });
});

describe("toPlainText", () => {
  it("drops headings, emphasis, math delimiters, TeX commands and braces, leaving the words", () => {
    const plain = toPlainText(MVT);
    expect(plain).toContain("The Mean Value Theorem says that if f is continuous on [a, b]");
    expect(plain).not.toMatch(/[#*$\\{}]/);
    expect(plain).not.toContain("dfrac");
  });

  it("collapses whitespace and line breaks", () => {
    expect(toPlainText("a\n\n   b\n- c")).toBe("a b - c");
  });
});

describe("makeSnippet", () => {
  const long = `${"alpha ".repeat(60)}the Mean Value Theorem appears here ${"omega ".repeat(60)}`.trim();

  it("returns short text whole", () => {
    expect(makeSnippet("a short note", "note")).toBe("a short note");
  });

  it("centers on the first match, with ellipses on both cut sides, and keeps the match", () => {
    const snippet = makeSnippet(long, "mean value");
    expect(snippet.startsWith("…")).toBe(true);
    expect(snippet.endsWith("…")).toBe(true);
    expect(snippet.toLowerCase()).toContain("mean value theorem");
    expect(snippet.length).toBeLessThanOrEqual(190);
  });

  it("starts at the beginning, with no leading ellipsis, when the match is near it", () => {
    const text = `Mean value first. ${"filler ".repeat(60)}`.trim();
    const snippet = makeSnippet(text, "mean value");
    expect(snippet.startsWith("Mean value")).toBe(true);
    expect(snippet.endsWith("…")).toBe(true);
  });

  it("falls back to the start of the text when the term is only in the topic's name", () => {
    const text = "Opening sentence. ".repeat(30).trim();
    const snippet = makeSnippet(text, "absent");
    expect(snippet.startsWith("Opening sentence.")).toBe(true);
    expect(snippet.endsWith("…")).toBe(true);
  });
});

describe("splitHighlight", () => {
  it("marks every match, in any case, and keeps the original capitalization", () => {
    expect(splitHighlight("The Mean value and mean VALUE", "mean value")).toEqual([
      { text: "The ", match: false },
      { text: "Mean value", match: true },
      { text: " and ", match: false },
      { text: "mean VALUE", match: true },
    ]);
  });

  it("gives one unmarked piece when nothing matches, and nothing for empty text", () => {
    expect(splitHighlight("no hit here", "xyz")).toEqual([{ text: "no hit here", match: false }]);
    expect(splitHighlight("", "xyz")).toEqual([]);
  });

  it("treats the query as plain text, not a pattern", () => {
    expect(splitHighlight("cost is (a+b)* here", "(a+b)*")).toEqual([
      { text: "cost is ", match: false },
      { text: "(a+b)*", match: true },
      { text: " here", match: false },
    ]);
  });
});

describe("rankHits", () => {
  const candidates = [
    topic("Connecting f, f', and f''", "connecting", 1, "Use the sign of the derivative. The mean value idea is not needed here."),
    topic("Mean Value Theorem", "mvt", 2, MVT),
    topic("Optimization", "opt", 3, "Set the derivative to zero. Nothing about averages."),
    topic("Related Rates", "rr", 1, "Differentiate with respect to time. Mean value shows up once.", { slug: "unit-4", name: "Contextual Applications", order: 4 }),
  ];

  it("keeps only topics whose readable text or name contains the query, in any case", () => {
    expect(rankHits(candidates, "MEAN VALUE").map((h) => h.topicSlug)).toEqual(["mvt", "rr", "connecting"]);
  });

  it("puts topic-name matches first, then follows course order (unit, then topic)", () => {
    const hits = rankHits(candidates, "mean value");
    expect(hits[0].topicSlug).toBe("mvt");
    expect(hits[0].inName).toBe(true);
    expect(hits.slice(1).map((h) => h.topicSlug)).toEqual(["rr", "connecting"]); // unit 4 before unit 5
  });

  it("does not match TeX source: searching 'dfrac' finds nothing although it is in the raw text", () => {
    expect(MVT).toContain("dfrac");
    expect(rankHits(candidates, "dfrac")).toEqual([]);
  });

  it("matches a phrase that crosses emphasis marks in the raw text", () => {
    const hits = rankHits([topic("Limits", "lim", 1, "Use the **mean** value of the two sides.")], "the mean value");
    expect(hits.map((h) => h.topicSlug)).toEqual(["lim"]);
  });

  it("returns a snippet around the match, never raw TeX", () => {
    const [hit] = rankHits(candidates, "differentiability");
    expect(hit.topicSlug).toBe("mvt");
    expect(hit.snippet.toLowerCase()).toContain("differentiability");
    expect(hit.snippet).not.toMatch(/[\\$]/);
  });

  it("handles a topic with no refresher", () => {
    expect(rankHits([topic("Empty", "e", 1, null)], "empty").map((h) => h.topicSlug)).toEqual(["e"]);
    expect(rankHits([topic("Empty", "e", 1, null)], "zzz")).toEqual([]);
  });

  it("returns at most MAX_RESULTS", () => {
    const many = Array.from({ length: MAX_RESULTS + 15 }, (_, i) => topic(`Topic ${i}`, `t${i}`, i, "the common word"));
    expect(rankHits(many, "common")).toHaveLength(MAX_RESULTS);
  });
});

describe("searchRefreshers", () => {
  beforeEach(() => {
    vi.clearAllMocks();
    mocks.findMany.mockImplementation(async () => [topic("Mean Value Theorem", "mvt", 2, MVT)]);
  });

  it("asks only for this course's topics that have a refresher", async () => {
    await searchRefreshers("ap-calc", "mean value");
    expect(mocks.findMany.mock.calls[0][0].where).toEqual({ unit: { course: { slug: "ap-calc" } }, refresher: { not: null } });
  });

  it("returns the ranked hits", async () => {
    expect((await searchRefreshers("ap-calc", "theorem")).map((h) => h.topicSlug)).toEqual(["mvt"]);
  });

  it("does not hand the query to the database, so it cannot act as a pattern or an injection", async () => {
    await searchRefreshers("ap-calc", "100%_' OR 1=1 --");
    expect(JSON.stringify(mocks.findMany.mock.calls[0][0])).not.toContain("OR 1=1");
  });
});
