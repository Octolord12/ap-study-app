import fs from "node:fs";
import { createRequire } from "node:module";
import path from "node:path";
import { describe, expect, it } from "vitest";
import { renderContentToHtml } from "@/lib/content/render";

// The math is drawn by the KaTeX that rehype-katex uses, but the stylesheet and
// fonts come from the KaTeX we import in globals.css. KaTeX renames CSS classes
// between versions, so when the two differed (0.16 drawing, 0.18 styling) every
// symbol built with an overlay (\neq, \ne, \not) lost its positioning and
// showed as "x /= 2". These tests make that impossible to do again unnoticed.

const root = path.resolve(import.meta.dirname, "..");
const requireFrom = (dir: string) => createRequire(path.join(dir, "package.json"));
const katexVersion = (from: NodeJS.Require) => JSON.parse(fs.readFileSync(from.resolve("katex/package.json"), "utf8")).version as string;

describe("KaTeX versions", () => {
  it("the renderer and the stylesheet we import are the same version", () => {
    const stylesheet = katexVersion(requireFrom(root));
    const renderer = katexVersion(createRequire(requireFrom(root).resolve("rehype-katex")));
    const parser = katexVersion(createRequire(requireFrom(root).resolve("micromark-extension-math")));
    expect(renderer).toBe(stylesheet);
    expect(parser).toBe(stylesheet);
  });
});

describe("KaTeX output and stylesheet agree", () => {
  const css = fs.readFileSync(path.join(root, "node_modules/katex/dist/katex.min.css"), "utf8");

  it("styles every child of the overlay wrapper that \\neq, \\ne and \\not produce", async () => {
    const html = await renderContentToHtml("$x \\neq 2$ and $a \\ne b$ and $x \\not= 3$", "ap-calc");
    const host = document.createElement("div");
    host.innerHTML = html;

    const wrappers = host.querySelectorAll(".rlap");
    expect(wrappers.length).toBe(3);
    // The wrapper's direct children are positioned by `.rlap>.<child>` rules, whatever this
    // KaTeX version calls them. Without the rule the slash lands beside the "=" instead of on it.
    const children = new Set<string>();
    for (const wrapper of wrappers) for (const child of wrapper.children) for (const cls of child.classList) children.add(cls);
    children.delete("strut");
    expect(children.size).toBeGreaterThan(0);
    for (const cls of children) expect(css).toContain(`.rlap>.${cls}`);
  }, 30000);

  it("draws the not-equal slash on top of the equals sign, not beside it", async () => {
    const html = await renderContentToHtml("$x \\neq 2$", "ap-calc");
    const child = /<span class="rlap"><span class="strut"[^>]*><\/span><span class="([^"]+)"/.exec(html)?.[1];
    expect(child).toBeDefined();
    expect(css).toMatch(new RegExp(`\\.rlap>\\.${child}\\{[^}]*position:absolute`));
  }, 30000);
});
