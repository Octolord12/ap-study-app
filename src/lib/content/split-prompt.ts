export interface SplitPrompt {
  intro: string;
  parts: string;
}

// A free-response prompt is written as a set-up paragraph or two followed by the lettered parts, "**(a)** ...".
// A figure belongs between the two: the real exam shows the stimulus before the questions that refer to it.
const FIRST_PART = /\r?\n\r?\n(?=(?:\*\*\(a\)\*\*|\(a\))[ \t])/;

function isBalanced(markdown: string): boolean {
  const fences = markdown.split("\n").filter((line) => line.trimStart().startsWith("```")).length;
  const unescaped = markdown.replace(/\\\$/g, "");
  const display = unescaped.split("$$").length - 1;
  const inline = unescaped.replace(/\$\$/g, "").split("$").length - 1;
  return fences % 2 === 0 && display % 2 === 0 && inline % 2 === 0;
}

// Null when there is nothing to split: no lettered part, no set-up text before it, or a start that
// would cut through a code fence or a formula.
export function splitPromptAtParts(markdown: string): SplitPrompt | null {
  const match = FIRST_PART.exec(markdown);
  if (!match) return null;
  const intro = markdown.slice(0, match.index).trim();
  const parts = markdown.slice(match.index).trim();
  if (intro === "" || parts === "" || !isBalanced(intro)) return null;
  return { intro, parts };
}
