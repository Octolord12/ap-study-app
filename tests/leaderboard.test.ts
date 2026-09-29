import { describe, expect, it } from "vitest";
import { rankLeaderboard, type LeaderboardCandidate } from "@/lib/social/leaderboard";

function candidate(overrides: Partial<LeaderboardCandidate>): LeaderboardCandidate {
  return { userId: "u1", username: "user1", totalXp: 0, optedOut: false, ...overrides };
}

describe("rankLeaderboard", () => {
  it("sorts by XP descending", () => {
    const result = rankLeaderboard([
      candidate({ userId: "a", totalXp: 50 }),
      candidate({ userId: "b", totalXp: 200 }),
      candidate({ userId: "c", totalXp: 100 }),
    ]);
    expect(result.map((r) => r.userId)).toEqual(["b", "c", "a"]);
  });

  it("assigns sequential ranks starting at 1", () => {
    const result = rankLeaderboard([candidate({ userId: "a", totalXp: 10 }), candidate({ userId: "b", totalXp: 5 })]);
    expect(result[0].rank).toBe(1);
    expect(result[1].rank).toBe(2);
  });

  it("excludes opted-out users entirely", () => {
    const result = rankLeaderboard([
      candidate({ userId: "a", totalXp: 999, optedOut: true }),
      candidate({ userId: "b", totalXp: 10 }),
    ]);
    expect(result).toHaveLength(1);
    expect(result[0].userId).toBe("b");
    expect(result[0].rank).toBe(1); // not 2 -- the opted-out user isn't just hidden, they don't occupy a rank
  });

  it("returns an empty list when everyone opted out", () => {
    expect(rankLeaderboard([candidate({ optedOut: true })])).toEqual([]);
  });
});
