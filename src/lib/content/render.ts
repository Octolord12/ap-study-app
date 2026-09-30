import { cache } from "react";
import { unified } from "unified";
import remarkParse from "remark-parse";
import remarkMath from "remark-math";
import remarkRehype from "remark-rehype";
import rehypeKatex from "rehype-katex";
import rehypePrettyCode from "rehype-pretty-code";
import rehypeStringify from "rehype-stringify";

// Shared by ContentRenderer (Server Components) and anywhere that needs to
// pre-render markdown to HTML before handing it to a Client Component (e.g.
// the quiz runner, which needs client-side interactivity but can't run this
// pipeline itself -- see the ContentRenderer gotcha in CLAUDE.md).
//
// Wrapped in React's cache() for per-request memoization: render-quiz.ts
// calls this once per stem, explanation, and choice explanation, per
// question, every request, and the same markdown always produces the same
// HTML, so re-running the full Shiki/KaTeX pipeline on a cache hit is pure
// waste. This only dedupes *within* a single request/render pass, not across
// requests -- cross-request caching (e.g. unstable_cache) would need
// invalidation handling on content re-seed, not worth the complexity here.
export const renderContentToHtml = cache(async (markdown: string): Promise<string> => {
  const file = await unified()
    .use(remarkParse)
    .use(remarkMath)
    .use(remarkRehype)
    .use(rehypeKatex)
    .use(rehypePrettyCode, { theme: "github-dark" })
    .use(rehypeStringify)
    .process(markdown);

  return String(file);
});
