"use client";

import { useMemo, useState, useTransition } from "react";
import Link from "next/link";
import { toggleBookmark } from "@/lib/study/actions";
import { Button } from "@/components/ui/button";

export interface QuestionRow {
  id: string;
  difficulty: "EASY" | "MEDIUM" | "HARD";
  topicSlug: string;
  topicName: string;
  bookmarked: boolean;
  missed: boolean | undefined; // undefined = never attempted
}

export function UnitQuestionBrowser({
  courseSlug,
  unitSlug,
  questions,
  initialTopicSlug,
}: {
  courseSlug: string;
  unitSlug: string;
  questions: QuestionRow[];
  initialTopicSlug?: string;
}) {
  const [topicFilter, setTopicFilter] = useState(initialTopicSlug ?? "all");
  const [difficultyFilter, setDifficultyFilter] = useState("all");
  const [bookmarkedOnly, setBookmarkedOnly] = useState(false);
  const [missedOnly, setMissedOnly] = useState(false);
  const [bookmarks, setBookmarks] = useState(() => new Set(questions.filter((q) => q.bookmarked).map((q) => q.id)));
  const [, startTransition] = useTransition();

  const topics = useMemo(() => {
    const seen = new Map<string, string>();
    for (const q of questions) seen.set(q.topicSlug, q.topicName);
    return Array.from(seen.entries());
  }, [questions]);

  const filtered = questions.filter((q) => {
    if (topicFilter !== "all" && q.topicSlug !== topicFilter) return false;
    if (difficultyFilter !== "all" && q.difficulty !== difficultyFilter) return false;
    if (bookmarkedOnly && !bookmarks.has(q.id)) return false;
    if (missedOnly && q.missed !== true) return false;
    return true;
  });

  function handleToggleBookmark(questionId: string) {
    setBookmarks((prev) => {
      const next = new Set(prev);
      if (next.has(questionId)) next.delete(questionId);
      else next.add(questionId);
      return next;
    });
    startTransition(async () => {
      await toggleBookmark(questionId);
    });
  }

  const selectClass = "rounded-md border border-input bg-background px-2 py-1 text-sm";
  const quizHref = `/courses/${courseSlug}/units/${unitSlug}/quiz?ids=${filtered.map((q) => q.id).join(",")}`;

  return (
    <div>
      <div className="mb-4 flex flex-wrap items-center gap-3">
        <select
          value={topicFilter}
          onChange={(e) => setTopicFilter(e.target.value)}
          className={selectClass}
          aria-label="Filter by topic"
        >
          <option value="all">All topics</option>
          {topics.map(([slug, name]) => (
            <option key={slug} value={slug}>
              {name}
            </option>
          ))}
        </select>
        <select
          value={difficultyFilter}
          onChange={(e) => setDifficultyFilter(e.target.value)}
          className={selectClass}
          aria-label="Filter by difficulty"
        >
          <option value="all">All difficulties</option>
          <option value="EASY">Easy</option>
          <option value="MEDIUM">Medium</option>
          <option value="HARD">Hard</option>
        </select>
        <label className="flex items-center gap-1.5 text-sm">
          <input type="checkbox" checked={bookmarkedOnly} onChange={(e) => setBookmarkedOnly(e.target.checked)} />
          Bookmarked
        </label>
        <label className="flex items-center gap-1.5 text-sm">
          <input type="checkbox" checked={missedOnly} onChange={(e) => setMissedOnly(e.target.checked)} />
          Missed
        </label>
      </div>

      <ul className="mb-4 divide-y divide-border rounded-lg border border-border">
        {filtered.map((q, index) => (
          <li key={q.id} className="flex items-center justify-between px-4 py-2 text-sm">
            <span>
              Q{index + 1} · {q.topicName} · <span className="capitalize">{q.difficulty.toLowerCase()}</span>
              {q.missed === true ? <span className="ml-2 text-destructive">missed last time</span> : null}
            </span>
            <button
              type="button"
              onClick={() => handleToggleBookmark(q.id)}
              className="text-muted-foreground hover:text-foreground"
              aria-label={bookmarks.has(q.id) ? "Remove bookmark" : "Add bookmark"}
            >
              {bookmarks.has(q.id) ? "★" : "☆"}
            </button>
          </li>
        ))}
        {filtered.length === 0 ? (
          <li className="px-4 py-6 text-center text-sm text-muted-foreground">No questions match these filters.</li>
        ) : null}
      </ul>

      {filtered.length > 0 ? (
        <Button render={<Link href={quizHref} />} nativeButton={false}>
          Practice {filtered.length} question{filtered.length === 1 ? "" : "s"}
        </Button>
      ) : null}
    </div>
  );
}
