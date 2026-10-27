import { renderContentToHtml } from "@/lib/content/render";
import { splitPromptAtParts } from "@/lib/content/split-prompt";

// `partsHtml` is empty unless the prompt has a figure to put between the two halves.
export interface RenderedFrqPrompt {
  introHtml: string;
  partsHtml: string;
}

// Rendered on the server for the same reason as renderRubric. Only a prompt with a figure is split: without
// one there is nothing to place, and the prompt stays one block.
export async function renderFrqPrompt(prompt: string, courseSlug: string, hasDiagram: boolean): Promise<RenderedFrqPrompt> {
  const split = hasDiagram ? splitPromptAtParts(prompt) : null;
  if (!split) return { introHtml: await renderContentToHtml(prompt, courseSlug), partsHtml: "" };
  const [introHtml, partsHtml] = await Promise.all([
    renderContentToHtml(split.intro, courseSlug),
    renderContentToHtml(split.parts, courseSlug),
  ]);
  return { introHtml, partsHtml };
}
