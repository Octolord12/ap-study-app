import type { FRQ, Question } from "./schema";

// `npm run content:seed` used to write `reviewed: false` over every row, which would silently throw away
// every approval made in /admin/review. These decide what a re-seed does instead: an approved item stays
// approved while its content is byte-for-byte what the person approved, and goes back to unreviewed the
// moment the seed would change it.

export interface StoredQuestion {
  difficulty: string;
  stem: string;
  explanation: string;
  conceptLink: string;
  diagram: unknown;
  reviewed: boolean;
  choices: { label: string; text: string; isCorrect: boolean; explanation: string }[];
}

export interface StoredFrq {
  type: string;
  prompt: string;
  pointValue: number;
  rubric: unknown;
  sampleResponse: string;
  diagram: unknown;
  reviewed: boolean;
}

// Postgres jsonb does not keep key order, so JSON read back can differ from the file only in order.
function canonical(value: unknown): string {
  if (value === undefined || value === null) return "null";
  if (Array.isArray(value)) return `[${value.map(canonical).join(",")}]`;
  if (typeof value === "object") {
    const entries = Object.entries(value as Record<string, unknown>)
      .filter(([, v]) => v !== undefined)
      .sort(([a], [b]) => (a < b ? -1 : a > b ? 1 : 0));
    return `{${entries.map(([k, v]) => `${JSON.stringify(k)}:${canonical(v)}`).join(",")}}`;
  }
  return JSON.stringify(value);
}

export function questionContentChanged(stored: StoredQuestion, incoming: Question): boolean {
  const byLabel = <T extends { label: string }>(items: T[]) => [...items].sort((a, b) => (a.label < b.label ? -1 : 1));
  const choices = (items: Question["choices"] | StoredQuestion["choices"]) =>
    byLabel([...items]).map((c) => ({ label: c.label, text: c.text, isCorrect: c.isCorrect, explanation: c.explanation }));
  return (
    stored.difficulty.toUpperCase() !== incoming.difficulty.toUpperCase() ||
    stored.stem !== incoming.stem ||
    stored.explanation !== incoming.explanation ||
    stored.conceptLink !== incoming.conceptLink ||
    canonical(stored.diagram) !== canonical(incoming.diagram) ||
    canonical(choices(stored.choices)) !== canonical(choices(incoming.choices))
  );
}

export function frqContentChanged(stored: StoredFrq, incoming: FRQ): boolean {
  return (
    stored.type !== (incoming.type ?? "FRQ") ||
    stored.prompt !== incoming.prompt ||
    stored.pointValue !== incoming.pointValue ||
    stored.sampleResponse !== incoming.sampleResponse ||
    canonical(stored.rubric) !== canonical(incoming.rubric) ||
    canonical(stored.diagram) !== canonical(incoming.diagram)
  );
}

// `stored` is null for an item the database has not seen. A file that says `reviewed: true` always wins.
export function nextReviewedFlag(stored: { reviewed: boolean } | null, changed: boolean, fileFlag: boolean): boolean {
  if (fileFlag) return true;
  if (!stored) return false;
  return stored.reviewed && !changed;
}

// A topic's refresher follows the same rule as a question: an approval stays while the stored text is
// exactly what the file says now, and resets the moment the seed would change it. `incoming` is null
// when the file has no refresher for the topic, which clears a stored one (the files are the source).
export interface StoredRefresher {
  refresher: string | null;
  refresherReviewed: boolean;
}

export function nextRefresherState(
  stored: StoredRefresher | null,
  incoming: { body: string; reviewed: boolean } | null,
): StoredRefresher {
  if (!incoming) return { refresher: null, refresherReviewed: false };
  const changed = !stored || stored.refresher !== incoming.body;
  return {
    refresher: incoming.body,
    refresherReviewed: nextReviewedFlag(stored ? { reviewed: stored.refresherReviewed } : null, changed, incoming.reviewed),
  };
}
