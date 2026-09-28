import { unified } from "unified";
import remarkParse from "remark-parse";
import remarkMath from "remark-math";
import remarkRehype from "remark-rehype";
import rehypeKatex from "rehype-katex";
import rehypePrettyCode from "rehype-pretty-code";
import rehypeStringify from "rehype-stringify";

// Renders question stems, explanations, and FRQ prompts: markdown text that can
// contain inline/block LaTeX ($...$, $$...$$) and fenced code blocks. This is
// the one place both are wired together, so content authors just write markdown.
//
// This runs the unified pipeline directly (not react-markdown's built-in one):
// rehype-pretty-code loads a Shiki highlighter asynchronously on first use, and
// react-markdown renders synchronously, which crashes Next's static prerender
// with "runSync finished async". Doing it ourselves lets this stay an async
// Server Component. The HTML is only ever built from our own authored content
// (never end-user input), so dangerouslySetInnerHTML here doesn't open an XSS hole.
export async function ContentRenderer({ children }: { children: string }) {
  const file = await unified()
    .use(remarkParse)
    .use(remarkMath)
    .use(remarkRehype)
    .use(rehypeKatex)
    .use(rehypePrettyCode, { theme: "github-dark" })
    .use(rehypeStringify)
    .process(children);

  return (
    <div
      className="prose prose-neutral dark:prose-invert max-w-none"
      dangerouslySetInnerHTML={{ __html: String(file) }}
    />
  );
}
