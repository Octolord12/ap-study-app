// An in-progress exam's answers, kept on the student's own device so a reload
// (or a dropped connection) doesn't wipe them. Not sent anywhere: the server
// only learns the answers when the exam is submitted.
//
// Answers are stored by the choice's authored label, which doesn't change when
// the choices are reshuffled on reload, so the right bubble is filled again.

export interface ExamDraft {
  mcq: Record<string, string>;
  frq: Record<string, string>;
  index: number;
}

export const EXAM_DRAFT_MAX_AGE_MS = 24 * 60 * 60 * 1000;
const MAX_RESPONSE_CHARS = 100_000;

export const examDraftKey = (examAttemptId: string) => `ap-study-app:exam-draft:${examAttemptId}`;

export function serializeExamDraft(draft: ExamDraft, nowMs: number): string {
  return JSON.stringify({ ...draft, savedAtMs: nowMs });
}

// Reads a draft back defensively: it comes from storage anything could have
// touched, so only answers to questions that are really in this exam survive.
export function parseExamDraft(
  raw: string | null,
  nowMs: number,
  exam: { mcqIds: string[]; frqIds: string[]; total: number },
): ExamDraft | null {
  if (!raw) return null;
  let data: unknown;
  try {
    data = JSON.parse(raw);
  } catch {
    return null;
  }
  if (typeof data !== "object" || data === null) return null;
  const d = data as { mcq?: unknown; frq?: unknown; index?: unknown; savedAtMs?: unknown };
  if (typeof d.savedAtMs !== "number" || nowMs - d.savedAtMs > EXAM_DRAFT_MAX_AGE_MS) return null;

  const pick = (source: unknown, ids: string[], valid: (value: string) => boolean) => {
    const out: Record<string, string> = {};
    if (typeof source !== "object" || source === null) return out;
    for (const id of ids) {
      const value = (source as Record<string, unknown>)[id];
      if (typeof value === "string" && valid(value)) out[id] = value;
    }
    return out;
  };

  const index = typeof d.index === "number" && Number.isInteger(d.index) ? Math.min(Math.max(d.index, 0), Math.max(exam.total - 1, 0)) : 0;
  return {
    mcq: pick(d.mcq, exam.mcqIds, (v) => /^[A-E]$/.test(v)),
    frq: pick(d.frq, exam.frqIds, (v) => v.length <= MAX_RESPONSE_CHARS),
    index,
  };
}

const DRAFT_KEY_PREFIX = "ap-study-app:exam-draft:";

// Drafts for exams that were never submitted would otherwise sit in the browser
// for good, free-response text included. Anything older than a day is already
// ignored when read; this removes it. `storage` is the browser's localStorage.
export function purgeStaleExamDrafts(storage: Pick<Storage, "length" | "key" | "getItem" | "removeItem">, nowMs: number): number {
  const stale: string[] = [];
  for (let i = 0; i < storage.length; i++) {
    const key = storage.key(i);
    if (!key || !key.startsWith(DRAFT_KEY_PREFIX)) continue;
    let savedAtMs: unknown;
    try {
      savedAtMs = JSON.parse(storage.getItem(key) ?? "null")?.savedAtMs;
    } catch {
      savedAtMs = undefined;
    }
    if (typeof savedAtMs !== "number" || nowMs - savedAtMs > EXAM_DRAFT_MAX_AGE_MS) stale.push(key);
  }
  for (const key of stale) storage.removeItem(key);
  return stale.length;
}
