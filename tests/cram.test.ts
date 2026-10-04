import { describe, expect, it } from "vitest";
import { CRAM_SIZE, rankCramQuestions, type CramCandidate } from "@/lib/study/cram";

// A random() just under 1 makes every Fisher-Yates swap an element with itself, so input order is kept.
const noShuffle = () => 0.999;

function q(id: string, attempts: number, misses: number): CramCandidate {
  return { id, attempts, misses };
}

describe("rankCramQuestions", () => {
  it("puts the most-missed questions first", () => {
    const ids = rankCramQuestions([q("a", 3, 1), q("b", 5, 4), q("c", 4, 2)], 10, noShuffle);
    expect(ids).toEqual(["b", "c", "a"]);
  });

  it("breaks a tie on miss count by the worse miss rate", () => {
    const ids = rankCramQuestions([q("often", 10, 2), q("rarely-seen", 2, 2)], 10, noShuffle);
    expect(ids).toEqual(["rarely-seen", "often"]);
  });

  it("puts unseen questions after missed ones and before answered-correctly ones", () => {
    const ids = rankCramQuestions([q("clean", 4, 0), q("new", 0, 0), q("missed", 2, 1)], 10, noShuffle);
    expect(ids).toEqual(["missed", "new", "clean"]);
  });

  it("ignores spaced-repetition due dates: it only looks at attempts and misses", () => {
    // Nothing about due dates is in the input, so a question that is not due
    // yet (answered and missed yesterday) is still first.
    expect(rankCramQuestions([q("missed-yesterday", 1, 1), q("new", 0, 0)], 10, noShuffle)[0]).toBe("missed-yesterday");
  });

  it("returns at most `limit` ids and defaults to CRAM_SIZE", () => {
    const many = Array.from({ length: 50 }, (_, i) => q(`q${i}`, 0, 0));
    expect(rankCramQuestions(many)).toHaveLength(CRAM_SIZE);
    expect(rankCramQuestions(many, 5)).toHaveLength(5);
  });

  it("returns an empty list when the course has no questions", () => {
    expect(rankCramQuestions([])).toEqual([]);
  });

  it("returns each question once", () => {
    const ids = rankCramQuestions([q("a", 1, 1), q("b", 0, 0), q("c", 2, 0)], 10);
    expect(new Set(ids).size).toBe(3);
  });

  it("shuffles questions that tie, using the random source", () => {
    const unseen = [q("a", 0, 0), q("b", 0, 0), q("c", 0, 0), q("d", 0, 0)];
    const first = rankCramQuestions(unseen, 4, noShuffle);
    const other = rankCramQuestions(unseen, 4, () => 0);
    expect(first).not.toEqual(other);
    expect([...other].sort()).toEqual(["a", "b", "c", "d"]);
  });
});
