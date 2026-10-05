import { describe, expect, it } from "vitest";
import { EXAM_DRAFT_MAX_AGE_MS, examDraftKey, parseExamDraft, purgeStaleExamDrafts, serializeExamDraft } from "@/lib/study/exam-draft";

const NOW = Date.UTC(2026, 9, 5, 12, 0, 0);
const exam = { mcqIds: ["q1", "q2", "q3"], frqIds: ["f1"], total: 4 };

describe("exam draft", () => {
  it("round-trips answers and the current question", () => {
    const raw = serializeExamDraft({ mcq: { q1: "B", q3: "D" }, frq: { f1: "my answer" }, index: 2 }, NOW);
    expect(parseExamDraft(raw, NOW + 1000, exam)).toEqual({ mcq: { q1: "B", q3: "D" }, frq: { f1: "my answer" }, index: 2 });
  });

  it("is keyed by the exam attempt, so two exams never mix", () => {
    expect(examDraftKey("a")).not.toBe(examDraftKey("b"));
  });

  it("returns nothing for a missing, broken or foreign value", () => {
    for (const raw of [null, "", "not json", "null", "42", '"text"', "[]"]) {
      expect(parseExamDraft(raw, NOW, exam)).toBeNull();
    }
  });

  it("expires after a day", () => {
    const raw = serializeExamDraft({ mcq: { q1: "A" }, frq: {}, index: 0 }, NOW);
    expect(parseExamDraft(raw, NOW + EXAM_DRAFT_MAX_AGE_MS, exam)).not.toBeNull();
    expect(parseExamDraft(raw, NOW + EXAM_DRAFT_MAX_AGE_MS + 1, exam)).toBeNull();
  });

  it("keeps only answers to questions that are in this exam, with sane values", () => {
    const raw = JSON.stringify({
      savedAtMs: NOW,
      index: 0,
      mcq: { q1: "A", q2: "Z", q3: 7, stranger: "B", __proto__: "x" },
      frq: { f1: "ok", other: "not in this exam" },
    });
    expect(parseExamDraft(raw, NOW, exam)).toEqual({ mcq: { q1: "A" }, frq: { f1: "ok" }, index: 0 });
  });

  it("clamps a wild question index into range", () => {
    for (const [index, expected] of [[99, 3], [-5, 0], [1.5, 0], ["2", 0], [null, 0]] as const) {
      const raw = JSON.stringify({ savedAtMs: NOW, index, mcq: {}, frq: {} });
      expect(parseExamDraft(raw, NOW, exam)?.index).toBe(expected);
    }
  });

  it("refuses an absurdly long free-response answer", () => {
    const raw = JSON.stringify({ savedAtMs: NOW, index: 0, mcq: {}, frq: { f1: "x".repeat(100_001) } });
    expect(parseExamDraft(raw, NOW, exam)?.frq).toEqual({});
  });
});

describe("purgeStaleExamDrafts", () => {
  function fakeStorage(entries: Record<string, string>) {
    const data = new Map(Object.entries(entries));
    return {
      get length() { return data.size; },
      key: (i: number) => [...data.keys()][i] ?? null,
      getItem: (k: string) => data.get(k) ?? null,
      removeItem: (k: string) => void data.delete(k),
      keys: () => [...data.keys()],
    };
  }

  it("removes expired and unreadable drafts, and nothing else", () => {
    const fresh = serializeExamDraft({ mcq: {}, frq: {}, index: 0 }, NOW - 1000);
    const old = serializeExamDraft({ mcq: {}, frq: { f1: "someone's essay" }, index: 0 }, NOW - EXAM_DRAFT_MAX_AGE_MS - 1);
    const storage = fakeStorage({
      [examDraftKey("fresh")]: fresh,
      [examDraftKey("old")]: old,
      [examDraftKey("garbage")]: "not json",
      "ap-study-app:sound-muted": "true",
      "unrelated-key": "keep me",
    });
    expect(purgeStaleExamDrafts(storage, NOW)).toBe(2);
    expect(storage.keys().sort()).toEqual([examDraftKey("fresh"), "ap-study-app:sound-muted", "unrelated-key"].sort());
  });

  it("does nothing when there are no drafts", () => {
    expect(purgeStaleExamDrafts(fakeStorage({ other: "x" }), NOW)).toBe(0);
  });
});
