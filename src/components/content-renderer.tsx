import { renderContentToHtml } from "@/lib/content/render";

// Renders question stems, explanations, and FRQ prompts: markdown text that can
// contain inline/block LaTeX ($...$, $$...$$) and fenced code blocks.
//
// Server Component only -- rehype-pretty-code loads a Shiki highlighter
// asynchronously, which is incompatible with react-markdown's synchronous
// rendering (crashes Next's static prerender). See renderContentToHtml for
// the pipeline itself, and use that directly when you need the HTML in a
// Client Component instead (it can't run this pipeline client-side).
//
// The HTML is only ever built from our own authored content (never end-user
// input), so dangerouslySetInnerHTML here doesn't open an XSS hole.
export async function ContentRenderer({ children }: { children: string }) {
  const html = await renderContentToHtml(children);

  return <div className="prose prose-neutral dark:prose-invert max-w-none" dangerouslySetInnerHTML={{ __html: html }} />;
}
