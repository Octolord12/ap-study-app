import { cache } from "react";
import { unified } from "unified";
import remarkParse from "remark-parse";
import remarkMath from "remark-math";
import remarkRehype from "remark-rehype";
import rehypeKatex from "rehype-katex";
import rehypePrettyCode from "rehype-pretty-code";
import rehypeStringify from "rehype-stringify";
import { isMathCourse } from "@/lib/content/math-courses";
import { normalizePlainMath } from "@/lib/content/plain-math";

// Shared by every Server Component that renders markdown, and anywhere that needs to
// pre-render markdown to HTML before handing it to a Client Component (e.g.
// the quiz runner, which needs client-side interactivity but can't run this
// pipeline itself -- see the react-markdown gotcha in CLAUDE.md).
//
// Wrapped in React's cache() for per-request memoization: render-quiz.ts
// calls this once per stem, explanation, and choice explanation, per
// question, every request, and the same markdown always produces the same
// HTML, so re-running the full Shiki/KaTeX pipeline on a cache hit is pure
// waste. This only dedupes *within* a single request/render pass, not across
// requests -- cross-request caching (e.g. unstable_cache) would need
// invalidation handling on content re-seed, not worth the complexity here.
//
// courseSlug is optional only so callers without a course (none today) still
// work; pass it whenever known -- it decides how much plain-text math gets
// typeset (see plain-math.ts).
export const renderContentToHtml = cache(async (markdown: string, courseSlug?: string): Promise<string> => {
  const normalized = normalizePlainMath(markdown, { mathCourse: courseSlug ? isMathCourse(courseSlug) : false });
  const file = await unified()
    .use(remarkParse)
    .use(remarkMath)
    .use(remarkRehype)
    .use(rehypeKatex)
    .use(rehypePrettyCode, { theme: "github-dark" })
    .use(rehypeStringify)
    .process(normalized);

  return String(file);
});

// Answer choices are authored as single lines, but program-output choices
// (AP CSA) write multi-line output with a literal backslash-n ("A\nB").
// Show those as the separate lines a student would actually see printed.
export const renderChoiceTextToHtml = cache(async (text: string, courseSlug?: string): Promise<string> =>
  renderContentToHtml(text.replace(/\\n/g, "  \n"), courseSlug),
);
