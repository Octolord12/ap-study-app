import { beforeEach, describe, expect, it, vi } from "vitest";

const question = {
  id: "q-1",
  difficulty: "EASY" as const,
  stem: "Which is fastest?",
  explanation: "B wins.",
  diagram: null,
  conceptLink: "ap-x/unit-1/topic-1",
  choices: [
    { id: "c-a", label: "A", text: "slow", isCorrect: true, explanation: "Correct. This beats option B." },
    { id: "c-b", label: "B", text: "slower", isCorrect: false, explanation: "Not as good as option A." },
    { id: "c-c", label: "C", text: "slowest", isCorrect: false, explanation: "no" },
    { id: "c-d", label: "D", text: "stopped", isCorrect: false, explanation: "no" },
  ],
};

vi.mock("@/lib/study/queries", () => ({ getQuestionsByIds: vi.fn(async () => [question]) }));
vi.mock("@/lib/content/render", () => ({
  renderContentToHtml: async (text: string) => text,
  renderChoiceTextToHtml: async (text: string) => text,
}));

import { renderQuizQuestions } from "@/lib/study/render-quiz";

describe("renderQuizQuestions shuffles choices every time", () => {
  beforeEach(() => vi.clearAllMocks());

  it("keeps each choice's authored label, correctness and text together", async () => {
    const [rendered] = await renderQuizQuestions(["q-1"], "ap-x");
    for (const c of rendered.choices) {
      const authored = question.choices.find((q) => q.label === c.label)!;
      expect(c.id).toBe(authored.id);
      expect(c.isCorrect).toBe(authored.isCorrect);
      expect(c.textHtml).toBe(authored.text);
    }
    expect(rendered.choices.map((c) => c.displayLabel)).toEqual(["A", "B", "C", "D"]);
  });

  it("puts the correct answer in every slot across repeated showings (never fixed at A)", async () => {
    const seen = new Set<string>();
    for (let i = 0; i < 200; i++) {
      const [rendered] = await renderQuizQuestions(["q-1"], "ap-x");
      seen.add(rendered.choices.find((c) => c.isCorrect)!.displayLabel);
    }
    expect([...seen].sort()).toEqual(["A", "B", "C", "D"]);
  });

  it("rewrites 'option X' in explanations to the letters on screen", async () => {
    for (let i = 0; i < 20; i++) {
      const [rendered] = await renderQuizQuestions(["q-1"], "ap-x");
      const shown = Object.fromEntries(rendered.choices.map((c) => [c.label, c.displayLabel]));
      const a = rendered.choices.find((c) => c.label === "A")!;
      const b = rendered.choices.find((c) => c.label === "B")!;
      expect(a.explanationHtml).toBe(`Correct. This beats option ${shown.B}.`);
      expect(b.explanationHtml).toBe(`Not as good as option ${shown.A}.`);
    }
  });
});
