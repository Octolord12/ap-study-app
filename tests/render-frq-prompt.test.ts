import { describe, expect, it, vi } from "vitest";

const render = vi.hoisted(() => vi.fn<(text: string, courseSlug?: string) => Promise<string>>(async (text) => `<html>${text}</html>`));
vi.mock("@/lib/content/render", () => ({ renderContentToHtml: render }));

import { renderFrqPrompt } from "@/lib/study/render-frq-prompt";

const PROMPT = "Set-up.\n\n**(a)** First.\n\n**(b)** Second.";

describe("renderFrqPrompt", () => {
  it("renders the set-up and the parts separately when there is a figure to put between them", async () => {
    expect(await renderFrqPrompt(PROMPT, "ap-biology", true)).toEqual({
      introHtml: "<html>Set-up.</html>",
      partsHtml: "<html>**(a)** First.\n\n**(b)** Second.</html>",
    });
  });

  it("keeps a prompt without a figure as one block", async () => {
    render.mockClear();
    expect(await renderFrqPrompt(PROMPT, "ap-csa", false)).toEqual({ introHtml: `<html>${PROMPT}</html>`, partsHtml: "" });
    expect(render).toHaveBeenCalledTimes(1);
  });

  it("keeps a prompt with a figure but no lettered parts as one block", async () => {
    const text = "Describe the graph.";
    expect(await renderFrqPrompt(text, "ap-biology", true)).toEqual({ introHtml: `<html>${text}</html>`, partsHtml: "" });
  });

  it("passes the course on to the renderer", async () => {
    render.mockClear();
    await renderFrqPrompt(PROMPT, "ap-calc", true);
    expect(render.mock.calls.map((c) => c[1])).toEqual(["ap-calc", "ap-calc"]);
  });
});
