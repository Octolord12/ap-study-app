import { readdirSync, readFileSync, existsSync } from "node:fs";
import { join } from "node:path";
import { describe, expect, it } from "vitest";
import { splitPromptAtParts } from "@/lib/content/split-prompt";

describe("splitPromptAtParts", () => {
  it("splits the set-up from the first lettered part", () => {
    expect(splitPromptAtParts("Set-up one.\n\nSet-up two.\n\n**(a)** First.\n\n**(b)** Second.")).toEqual({
      intro: "Set-up one.\n\nSet-up two.",
      parts: "**(a)** First.\n\n**(b)** Second.",
    });
  });

  it("recognizes the bold capital A. that AP Statistics prompts use", () => {
    expect(splitPromptAtParts("Set-up.\n\nUse the given information to respond to parts A and B.\n\n**A.** First.\n\n**B.** Second.")).toEqual({
      intro: "Set-up.\n\nUse the given information to respond to parts A and B.",
      parts: "**A.** First.\n\n**B.** Second.",
    });
  });

  it("does not take a paragraph that merely starts with a capital A. for the first part", () => {
    expect(splitPromptAtParts("Set-up.\n\nA. Smith studied this.\n\nMore text.")).toBeNull();
  });

  it("also recognizes an unbolded (a)", () => {
    expect(splitPromptAtParts("Set-up.\n\n(a) First.\n\n(b) Second.")).toEqual({ intro: "Set-up.", parts: "(a) First.\n\n(b) Second." });
  });

  it("splits at the first (a), not a later one", () => {
    const split = splitPromptAtParts("Set-up.\n\n**(a)** First.\n\nMore text.\n\n**(a)** Again.");
    expect(split?.intro).toBe("Set-up.");
    expect(split?.parts.startsWith("**(a)** First.")).toBe(true);
  });

  it("does nothing when there is no lettered part", () => {
    expect(splitPromptAtParts("Write an essay.\n\nUse the documents.")).toBeNull();
  });

  it("does nothing when the prompt starts with its first part (no set-up to put a figure after)", () => {
    expect(splitPromptAtParts("**(a)** First.\n\n**(b)** Second.")).toBeNull();
  });

  it("does nothing when only blank lines come before the first part", () => {
    expect(splitPromptAtParts("\n\n**(a)** First.\n\n**(b)** Second.")).toBeNull();
  });

  it("only splits at the start of a paragraph, not at a mention of part (a)", () => {
    expect(splitPromptAtParts("In part (a) you will see the graph.\n\nThen you answer.")).toBeNull();
    expect(splitPromptAtParts("Set-up.\n\nUse your answer to **(a)** later.")).toBeNull();
  });

  it("will not cut through a code block or a formula", () => {
    expect(splitPromptAtParts("Set-up.\n\n```java\nint x;\n\n(a) not a part\n```\n\n**(a)** Real.")).toBeNull();
    expect(splitPromptAtParts("Let $$\nx\n\n(a) y\n$$ be given.\n\n**(a)** Real.")).toBeNull();
  });

  it("will not cut through an inline formula", () => {
    expect(splitPromptAtParts("Let $x\n\n(a) y$ be given.\n\n**(a)** Real.")).toBeNull();
  });

  it("is not fooled by an escaped dollar sign", () => {
    expect(splitPromptAtParts("It costs \\$5.\n\n**(a)** Why?")?.intro).toBe("It costs \\$5.");
  });

  it("gives pieces that put back together as the same text", () => {
    const text = "Set-up.\n\n**(a)** First.\n\n**(b)** Second.";
    const split = splitPromptAtParts(text)!;
    expect(`${split.intro}\n\n${split.parts}`).toBe(text);
  });
});

describe("every shipped free-response prompt that has a figure can be placed", () => {
  const root = join(process.cwd(), "content");
  const withFigure: { id: string; prompt: string }[] = [];
  for (const course of readdirSync(root)) {
    const dir = join(root, course, "frqs");
    if (!existsSync(dir)) continue;
    for (const file of readdirSync(dir).filter((f) => f.endsWith(".json"))) {
      for (const p of JSON.parse(readFileSync(join(dir, file), "utf8")) as { id: string; prompt: string; diagram?: unknown }[]) {
        if (p.diagram) withFigure.push({ id: p.id, prompt: p.prompt });
      }
    }
  }

  it("has some to check", () => {
    expect(withFigure.length).toBeGreaterThan(30);
  });

  it("each splits into set-up text and lettered parts, so its figure lands between them", () => {
    const unplaced = withFigure.filter((p) => splitPromptAtParts(p.prompt) === null).map((p) => p.id);
    expect(unplaced).toEqual([]);
  });
});
