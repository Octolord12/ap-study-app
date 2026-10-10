import Link from "next/link";
import { MAX_QUERY_LENGTH, MAX_RESULTS, MIN_QUERY_LENGTH, splitHighlight, type RefresherHit } from "@/lib/study/refresher-search";
import { RuledList } from "@/components/ui/page";

// The matched words are wrapped in <mark> by React from pieces of plain text, never as HTML, so nothing in a refresher can inject markup.
function Highlighted({ text, query }: { text: string; query: string }) {
  return (
    <>
      {splitHighlight(text, query).map((part, i) =>
        part.match ? (
          <mark key={i} className="bg-mark text-on-mark">
            {part.text}
          </mark>
        ) : (
          <span key={i}>{part.text}</span>
        ),
      )}
    </>
  );
}

export function RefresherSearchResults({ courseSlug, query, hits }: { courseSlug: string; query: string | null; hits: RefresherHit[] | null }) {
  if (query === null || hits === null) {
    return (
      <p className="reading max-w-[52ch]">
        Type {MIN_QUERY_LENGTH} to {MAX_QUERY_LENGTH} characters: a topic name, or a word you remember from the notes.
      </p>
    );
  }
  if (hits.length === 0) {
    return (
      <p className="reading max-w-[52ch]">
        No refresher mentions &ldquo;{query}&rdquo;. Try a shorter word, or the name of the topic.
      </p>
    );
  }
  return (
    <div className="space-y-3">
      <p className="eyebrow" role="status">
        {hits.length === MAX_RESULTS ? `First ${MAX_RESULTS} topics` : `${hits.length} topic${hits.length === 1 ? "" : "s"}`}
      </p>
      <RuledList>
        {hits.map((hit) => (
          <li key={`${hit.unitSlug}/${hit.topicSlug}`}>
            <Link href={`/courses/${courseSlug}/units/${hit.unitSlug}/topics/${hit.topicSlug}`} className="group block space-y-1.5 py-4">
              <p className="eyebrow">
                Unit {hit.unitNumber} · {hit.unitName}
              </p>
              <h3 className="heading text-xl underline-offset-4 decoration-2 group-hover:underline">
                <Highlighted text={hit.topicName} query={query} />
              </h3>
              <p className="reading-sm max-w-[68ch] text-muted-foreground">
                <Highlighted text={hit.snippet} query={query} />
              </p>
            </Link>
          </li>
        ))}
      </RuledList>
    </div>
  );
}
