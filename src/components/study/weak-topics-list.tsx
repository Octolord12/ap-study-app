import Link from "next/link";
import type { WeakTopic } from "@/lib/study/weak-topics";
import { RuledList } from "@/components/ui/page";
import { topicHref } from "@/lib/study/concept-link";

const LINK = "text-sm font-semibold underline underline-offset-4 hover:bg-mark hover:text-on-mark hover:no-underline";

export function WeakTopicsList({ topics, withRefresher = new Set() }: { topics: WeakTopic[]; withRefresher?: ReadonlySet<string> }) {
  if (topics.length === 0) {
    return (
      <p className="reading max-w-[52ch]">
        None right now. Once you have answered a few questions on a topic, the ones you find hardest are listed here.
      </p>
    );
  }
  return (
    <RuledList>
      {topics.map((t) => (
        <li key={t.topicId} className="flex flex-wrap items-center justify-between gap-x-6 gap-y-2 py-4">
          <div className="min-w-0">
            <p className="heading text-lg">{t.topicName}</p>
            <p className="eyebrow mt-1">
              {t.unitName} · {t.courseName}
            </p>
          </div>
          <div className="flex items-center gap-x-5">
            <p className="text-sm">
              <span className="numeral text-xl">{t.accuracyPercent}%</span> <span className="eyebrow">{t.correct} of {t.attempted} right</span>
            </p>
            {withRefresher.has(t.topicId) ? (
              <Link href={topicHref(t.courseSlug, t.unitSlug, t.topicSlug, true)} className={LINK}>
                Refresher
              </Link>
            ) : null}
            <Link href={`/courses/${t.courseSlug}/units/${t.unitSlug}?topic=${t.topicSlug}`} className={LINK}>
              Practice
            </Link>
          </div>
        </li>
      ))}
    </RuledList>
  );
}
