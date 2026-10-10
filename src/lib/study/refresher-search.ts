import { getDb } from "@/lib/db";

export const MIN_QUERY_LENGTH = 2;
export const MAX_QUERY_LENGTH = 60;
export const MAX_RESULTS = 30;
const SNIPPET_LENGTH = 170;

// Trimmed, whitespace collapsed; null when it is too short to search for or too long to be a real search (the page says which).
export function normalizeSearchQuery(raw: string | string[] | undefined): string | null {
  if (typeof raw !== "string") return null;
  const q = raw.replace(/\s+/g, " ").trim();
  return q.length >= MIN_QUERY_LENGTH && q.length <= MAX_QUERY_LENGTH ? q : null;
}

// A refresher is markdown with LaTeX. Searching its source would match "frac" or "dfrac" and show a snippet of backslashes, so the search
// and the snippet both work on this readable version: no heading marks, emphasis, `$`, TeX commands or braces.
export function toPlainText(markdown: string): string {
  return markdown
    .replace(/\$\$?/g, " ")
    .replace(/\\[a-zA-Z]+/g, " ")
    .replace(/\\[^a-zA-Z\s]/g, " ")
    .replace(/[{}^_#*>`|]/g, " ")
    .replace(/\s+/g, " ")
    .trim();
}

const contains = (haystack: string, needle: string) => haystack.toLowerCase().includes(needle.toLowerCase());

// About SNIPPET_LENGTH characters around the first match, cut on word boundaries, with an ellipsis where text was left out. When the term is
// only in the topic's name there is nothing to show around it, so the start of the text is used.
export function makeSnippet(plain: string, query: string): string {
  const at = plain.toLowerCase().indexOf(query.toLowerCase());
  if (plain.length <= SNIPPET_LENGTH) return plain;
  if (at < 0) return plain.slice(0, SNIPPET_LENGTH).replace(/\s+\S*$/, "") + "…";
  let start = Math.max(0, at - Math.floor((SNIPPET_LENGTH - query.length) / 2));
  let end = Math.min(plain.length, start + SNIPPET_LENGTH);
  start = Math.max(0, end - SNIPPET_LENGTH);
  if (start > 0) start = plain.indexOf(" ", start) + 1 || start;
  if (end < plain.length) {
    const cut = plain.lastIndexOf(" ", end);
    if (cut > at + query.length) end = cut;
  }
  return `${start > 0 ? "…" : ""}${plain.slice(start, end).trim()}${end < plain.length ? "…" : ""}`;
}

// Cuts text into pieces, marking the ones that are the query (any case), so the page can wrap them in <mark> through React, never as HTML.
export function splitHighlight(text: string, query: string): { text: string; match: boolean }[] {
  const lower = text.toLowerCase();
  const q = query.toLowerCase();
  const parts: { text: string; match: boolean }[] = [];
  let from = 0;
  for (let at = lower.indexOf(q); at !== -1; at = lower.indexOf(q, from)) {
    if (at > from) parts.push({ text: text.slice(from, at), match: false });
    parts.push({ text: text.slice(at, at + q.length), match: true });
    from = at + q.length;
  }
  if (from < text.length) parts.push({ text: text.slice(from), match: false });
  return parts;
}

export interface RefresherCandidate {
  name: string;
  slug: string;
  order: number;
  refresher: string | null;
  unit: { slug: string; name: string; order: number };
}

export interface RefresherHit {
  topicName: string;
  topicSlug: string;
  unitSlug: string;
  unitName: string;
  unitNumber: number;
  inName: boolean;
  snippet: string;
}

// Keeps only topics whose readable text really contains the query, topic-name matches first, then in course order.
export function rankHits(candidates: RefresherCandidate[], query: string): RefresherHit[] {
  const hits: RefresherHit[] = [];
  for (const c of candidates) {
    const plain = toPlainText(c.refresher ?? "");
    const inName = contains(c.name, query);
    if (!inName && !contains(plain, query)) continue;
    hits.push({
      topicName: c.name,
      topicSlug: c.slug,
      unitSlug: c.unit.slug,
      unitName: c.unit.name,
      unitNumber: c.unit.order,
      inName,
      snippet: makeSnippet(plain, query),
    });
  }
  const orderOf = new Map(candidates.map((c, i) => [`${c.unit.slug}/${c.slug}`, [c.unit.order, c.order, i] as const]));
  return hits
    .sort((a, b) => {
      if (a.inName !== b.inName) return a.inName ? -1 : 1;
      const [au, at] = orderOf.get(`${a.unitSlug}/${a.topicSlug}`)!;
      const [bu, bt] = orderOf.get(`${b.unitSlug}/${b.topicSlug}`)!;
      return au - bu || at - bt;
    })
    .slice(0, MAX_RESULTS);
}

// Reads this course's refreshers (at most about 46, roughly 70 KB) and filters in code. A database `contains` on the raw text would be wrong in
// both directions: it matches TeX source, and it misses a phrase that crosses markdown ("the **mean** value"). Never reads other courses' topics.
export async function searchRefreshers(courseSlug: string, query: string): Promise<RefresherHit[]> {
  const candidates = await getDb().topic.findMany({
    where: { unit: { course: { slug: courseSlug } }, refresher: { not: null } },
    select: { name: true, slug: true, order: true, refresher: true, unit: { select: { slug: true, name: true, order: true } } },
  });
  return rankHits(candidates, query);
}
