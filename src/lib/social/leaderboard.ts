export interface LeaderboardCandidate {
  userId: string;
  username: string;
  totalXp: number;
  optedOut: boolean;
}

export interface LeaderboardEntry {
  rank: number;
  userId: string;
  username: string;
  totalXp: number;
}

// Pure ranking/filtering, separate from the DB aggregation that produces
// candidates (src/lib/social/queries.ts) -- opted-out users are excluded
// entirely, not just hidden, so this is the one place that rule lives.
export function rankLeaderboard(candidates: LeaderboardCandidate[]): LeaderboardEntry[] {
  return candidates
    .filter((c) => !c.optedOut)
    .sort((a, b) => b.totalXp - a.totalXp)
    .map((c, i) => ({ rank: i + 1, userId: c.userId, username: c.username, totalXp: c.totalXp }));
}
