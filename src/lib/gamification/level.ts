export interface LevelProgress {
  level: number;
  xpIntoLevel: number;
  xpForNextLevel: number;
}

// Cost to go from level n to n+1 is 100*n XP (level 1->2 costs 100, 2->3
// costs 200, ...), so cumulative XP to REACH level L is 100 * (L-1)*L/2 --
// a gentle, easy-to-explain ramp rather than a steep exponential one.
function cumulativeXpForLevel(level: number): number {
  return 100 * ((level - 1) * level) / 2;
}

export function computeLevel(totalXp: number): LevelProgress {
  let level = 1;
  while (cumulativeXpForLevel(level + 1) <= totalXp) {
    level++;
  }

  const xpIntoLevel = totalXp - cumulativeXpForLevel(level);
  const xpForNextLevel = cumulativeXpForLevel(level + 1) - cumulativeXpForLevel(level);
  return { level, xpIntoLevel, xpForNextLevel };
}
