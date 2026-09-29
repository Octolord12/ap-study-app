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
export async function renderContentToHtml(markdown: string): Promise<string> {
  const file = await unified()
    .use(remarkParse)
    .use(remarkMath)
    .use(remarkRehype)
    .use(rehypeKatex)
    .use(rehypePrettyCode, { theme: "github-dark" })
    .use(rehypeStringify)
    .process(markdown);

  return String(file);
}
