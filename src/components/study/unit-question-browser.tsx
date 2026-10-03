"use client";

import { useMemo, useState, useTransition } from "react";
import Link from "next/link";
import { Bookmark } from "lucide-react";
import { toggleBookmark } from "@/lib/study/actions";
import { Button } from "@/components/ui/button";
import { Select } from "@/components/ui/select";
import { cn } from "cn";

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

  const quizHref = `/courses/${courseSlug}/units/${unitSlug}/quiz?ids=${filtered.map((q) => q.id).join(",")}`;

  return (
    <div>
      <div className="mb-5 flex flex-wrap items-center gap-x-5 gap-y-3">
        <Select
          value={topicFilter}
          onChange={(e) => setTopicFilter(e.target.value)}
          aria-label="Filter by topic"
          className="sm:w-auto sm:min-w-52"
        >
          <option value="all">All topics</option>
          {topics.map(([slug, name]) => (
            <option key={slug} value={slug}>
              {name}
            </option>
          ))}
        </Select>
        <Select
          value={difficultyFilter}
          onChange={(e) => setDifficultyFilter(e.target.value)}
          aria-label="Filter by difficulty"
          className="sm:w-auto"
        >
          <option value="all">All difficulties</option>
          <option value="EASY">Easy</option>
          <option value="MEDIUM">Medium</option>
          <option value="HARD">Hard</option>
        </Select>
        <label className="flex items-center gap-2 text-sm font-medium">
          <input type="checkbox" className="check" checked={bookmarkedOnly} onChange={(e) => setBookmarkedOnly(e.target.checked)} />
          Bookmarked
        </label>
        <label className="flex items-center gap-2 text-sm font-medium">
          <input type="checkbox" className="check" checked={missedOnly} onChange={(e) => setMissedOnly(e.target.checked)} />
          Missed
        </label>
      </div>

      <ul className="mb-6 border-b border-border [&>li]:border-t [&>li]:border-border">
        {filtered.map((q, index) => (
          <li key={q.id} className="flex items-center justify-between gap-3 py-1.5 text-sm">
            <span className="flex min-w-0 flex-wrap items-baseline gap-x-3">
              <span className="eyebrow w-9 shrink-0 !text-foreground">Q{index + 1}</span>
              <span className="min-w-0">{q.topicName}</span>
              <span className="eyebrow">{q.difficulty.toLowerCase()}</span>
              {q.missed === true ? <span className="eyebrow !text-incorrect">missed last time</span> : null}
            </span>
            <button
              type="button"
              onClick={() => handleToggleBookmark(q.id)}
              aria-pressed={bookmarks.has(q.id)}
              aria-label={bookmarks.has(q.id) ? "Remove bookmark" : "Add bookmark"}
              className={cn("grid size-11 shrink-0 place-items-center hover:bg-mark hover:text-on-mark", bookmarks.has(q.id) && "text-foreground")}
            >
              <Bookmark className="size-5" fill={bookmarks.has(q.id) ? "currentColor" : "none"} strokeWidth={1.75} aria-hidden />
            </button>
          </li>
        ))}
        {filtered.length === 0 ? <li className="py-6 text-sm text-muted-foreground">No questions match these filters.</li> : null}
      </ul>

      {filtered.length > 0 ? (
        <Button render={<Link href={quizHref} />} nativeButton={false} size="lg">
          Practice {filtered.length} question{filtered.length === 1 ? "" : "s"}
        </Button>
      ) : null}
    </div>
  );
}
