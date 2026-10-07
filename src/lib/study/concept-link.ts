// Where "Review this concept" goes. A topic that has a written refresher has its own page; one that
// doesn't (a course whose refreshers aren't written yet) keeps the old behavior of opening the unit's
// question list filtered to that topic. See "Topic refreshers" in CLAUDE.md.
export function topicHref(courseSlug: string, unitSlug: string, topicSlug: string, hasRefresher: boolean): string {
  const unit = `/courses/${courseSlug}/units/${unitSlug}`;
  return hasRefresher ? `${unit}/topics/${topicSlug}` : `${unit}?topic=${topicSlug}`;
}

// A refresher is keyed the way a question's conceptLink and the content files are: "<unit>/<topic>".
export function topicKey(unitSlug: string, topicSlug: string): string {
  return `${unitSlug}/${topicSlug}`;
}
