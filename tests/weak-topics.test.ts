import { describe, expect, it } from "vitest";
import { weakTopics, type TopicAttempt } from "@/lib/study/weak-topics";

let n = 0;
function a(topic: string, correct: boolean, over: Partial<TopicAttempt> = {}): TopicAttempt {
  n++;
  return {
    questionId: `q${n}`,
    topicId: topic,
    topicName: `Topic ${topic}`,
    topicSlug: `topic-${topic}`,
    unitSlug: "unit-1",
    unitName: "Unit 1",
    courseSlug: "ap-calc",
    courseName: "AP Calculus AB",
    correct,
    createdAt: new Date(2026, 0, 1, 0, n),
    ...over,
  };
}
const many = (topic: string, right: number, wrong: number) => [...Array.from({ length: right }, () => a(topic, true)), ...Array.from({ length: wrong }, () => a(topic, false))];

describe("weakTopics", () => {
  it("ranks the lowest-accuracy topics first", () => {
    const result = weakTopics([...many("A", 1, 3), ...many("B", 2, 2), ...many("C", 0, 3)]);
    expect(result.map((t) => t.topicId)).toEqual(["C", "A", "B"]);
    expect(result[0]).toMatchObject({ attempted: 3, correct: 0, accuracyPercent: 0 });
  });

  it("leaves out topics with too few questions tried to mean anything", () => {
    expect(weakTopics(many("A", 0, 2))).toEqual([]);
    expect(weakTopics(many("A", 0, 2), { minQuestions: 2 })).toHaveLength(1);
  });

  it("leaves out topics the student is proficient at", () => {
    expect(weakTopics(many("A", 4, 1))).toEqual([]); // 80%
    expect(weakTopics(many("A", 3, 2))).toHaveLength(1); // 60%
  });

  it("judges each question by its latest attempt only", () => {
    const first = a("A", false, { questionId: "same", createdAt: new Date(2026, 0, 1) });
    const second = a("A", true, { questionId: "same", createdAt: new Date(2026, 0, 2) });
    const result = weakTopics([first, second, ...many("A", 0, 2)]);
    expect(result[0]).toMatchObject({ attempted: 3, correct: 1 });
  });

  it("caps the list", () => {
    const all = ["A", "B", "C", "D", "E"].flatMap((t) => many(t, 0, 3));
    expect(weakTopics(all)).toHaveLength(3);
    expect(weakTopics(all, { limit: 5 })).toHaveLength(5);
  });

  it("is empty with no attempts", () => {
    expect(weakTopics([])).toEqual([]);
  });
});
