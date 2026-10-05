import { PROFICIENT_MIN_ACCURACY } from "@/lib/study/mastery";

export interface TopicAttempt {
  questionId: string;
  topicId: string;
  topicName: string;
  topicSlug: string;
  unitSlug: string;
  unitName: string;
  courseSlug: string;
  courseName: string;
  correct: boolean;
  createdAt: Date;
}

export interface WeakTopic {
  topicId: string;
  topicName: string;
  topicSlug: string;
  unitSlug: string;
  unitName: string;
  courseSlug: string;
  courseName: string;
  attempted: number;
  correct: number;
  accuracyPercent: number;
}

// The topics the student is currently weakest at: judged on each question's latest
// attempt (a miss they have since got right doesn't count against them, same as unit
// mastery), only topics with enough questions tried to mean something, and only those
// below the proficiency line.
export function weakTopics(attempts: TopicAttempt[], { minQuestions = 3, limit = 3 }: { minQuestions?: number; limit?: number } = {}): WeakTopic[] {
  const latest = new Map<string, TopicAttempt>();
  for (const a of attempts) {
    const seen = latest.get(a.questionId);
    if (!seen || a.createdAt > seen.createdAt) latest.set(a.questionId, a);
  }

  const byTopic = new Map<string, WeakTopic>();
  for (const a of latest.values()) {
    const t = byTopic.get(a.topicId) ?? {
      topicId: a.topicId,
      topicName: a.topicName,
      topicSlug: a.topicSlug,
      unitSlug: a.unitSlug,
      unitName: a.unitName,
      courseSlug: a.courseSlug,
      courseName: a.courseName,
      attempted: 0,
      correct: 0,
      accuracyPercent: 0,
    };
    t.attempted++;
    if (a.correct) t.correct++;
    byTopic.set(a.topicId, t);
  }

  return [...byTopic.values()]
    .map((t) => ({ ...t, accuracyPercent: Math.round((t.correct / t.attempted) * 100) }))
    .filter((t) => t.attempted >= minQuestions && t.accuracyPercent < PROFICIENT_MIN_ACCURACY)
    .sort((a, b) => a.accuracyPercent - b.accuracyPercent || b.attempted - a.attempted || a.topicName.localeCompare(b.topicName))
    .slice(0, limit);
}
