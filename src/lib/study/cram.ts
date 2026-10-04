export const CRAM_SIZE = 20;

export interface CramCandidate {
  id: string;
  attempts: number;
  misses: number;
}

function shuffled<T>(items: T[], random: () => number): T[] {
  const out = [...items];
  for (let i = out.length - 1; i > 0; i--) {
    const j = Math.floor(random() * (i + 1));
    [out[i], out[j]] = [out[j], out[i]];
  }
  return out;
}

// What cram mode studies, in order: questions the student has missed (most
// misses first, then the worse miss rate), then questions never seen, then the
// rest. Spaced-repetition due dates are ignored on purpose; that is the point
// of cramming. Ties are broken randomly so repeat sessions don't open on the
// same question every time.
export function rankCramQuestions(candidates: CramCandidate[], limit = CRAM_SIZE, random: () => number = Math.random): string[] {
  const order = shuffled(candidates, random);

  const missed = order
    .filter((c) => c.misses > 0)
    .sort((a, b) => b.misses - a.misses || b.misses / b.attempts - a.misses / a.attempts);
  const unseen = order.filter((c) => c.attempts === 0);
  const rest = order.filter((c) => c.attempts > 0 && c.misses === 0);

  return [...missed, ...unseen, ...rest].slice(0, limit).map((c) => c.id);
}
