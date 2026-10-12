import { examDraws, type ExamSectionShape } from "@/lib/content/exam-sections";

export type ExamSectionLike = ExamSectionShape;

export interface FrqCandidate {
  id: string;
  type: string;
  unitId?: string;
}

export interface UnitCandidate {
  id: string;
  unitId?: string;
}

// unit id -> weight. A missing map, or a unit without a positive weight, means "no weighting": the draw is uniform.
export type UnitWeights = ReadonlyMap<string, number>;

// The CED publishes each unit's share of the multiple-choice section as a range; min + max is twice its midpoint, which keeps
// the weights whole numbers (the proportions are what matters, and they are normalized below).
export function unitWeightsFrom(units: readonly { id: string; weightingMin: number; weightingMax: number }[]): Map<string, number> {
  return new Map(units.map((u) => [u.id, u.weightingMin + u.weightingMax]));
}

// Uniform (Fisher-Yates). `sort(() => Math.random() - 0.5)` looks the same but is biased, and an exam
// draws 55 of ~400 questions, where the bias shows.
export function shuffled<T>(items: readonly T[], random: () => number = Math.random): T[] {
  const result = [...items];
  for (let i = result.length - 1; i > 0; i--) {
    const j = Math.floor(random() * (i + 1));
    [result[i], result[j]] = [result[j], result[i]];
  }
  return result;
}

interface WeightedUnit {
  key: string;
  weight: number;
  capacity: number;
}

// Splits `total` items across units in proportion to their weights, never giving a unit more than its capacity.
// Systematic sampling with a random start: along the line of cumulative shares, `total` evenly spaced points fall, and a
// unit gets the points inside its stretch. So every unit gets the floor or the ceiling of its exact share, the counts add up
// to exactly `total`, and a unit's average over many exams is exactly its share. Plain rounding of the shares would give the
// same split every time, and independent draws per item would sometimes leave a heavy unit with none. The units are
// shuffled first: in a fixed order two neighbours whose shares add to less than one could never both appear.
// A unit over its capacity is pinned there and the rest is split again among the others.
export function allocateByWeight(total: number, units: readonly WeightedUnit[], random: () => number = Math.random): Map<string, number> {
  const result = new Map<string, number>(units.map((u) => [u.key, 0]));
  let remaining = total;
  let active = units.filter((u) => u.weight > 0 && u.capacity > 0);
  while (remaining > 0 && active.length > 0) {
    const order = shuffled(active, random);
    const sum = order.reduce((n, u) => n + u.weight, 0);
    const start = random();
    const counts = new Map<string, number>();
    let cumulative = 0;
    let before = 0;
    order.forEach((unit, i) => {
      cumulative += unit.weight;
      // The last boundary is `remaining` itself, not a float that should equal it, so the counts always add up.
      const boundary = i === order.length - 1 ? remaining : Math.min(remaining, Math.floor((remaining * cumulative) / sum + start));
      counts.set(unit.key, Math.max(0, boundary - before));
      before = boundary;
    });
    const over = active.filter((u) => (counts.get(u.key) ?? 0) > u.capacity);
    if (over.length === 0) {
      for (const [key, n] of counts) result.set(key, (result.get(key) ?? 0) + n);
      return result;
    }
    for (const unit of over) {
      result.set(unit.key, (result.get(unit.key) ?? 0) + unit.capacity);
      remaining -= unit.capacity;
    }
    active = active.filter((u) => !over.includes(u));
  }
  return result;
}

// `count` of the candidates, spread over their units by weight (see allocateByWeight), uniformly within each unit, in a
// random order. Falls back to a uniform draw when there is nothing to weight by: no weights, a candidate with no unit, or a
// unit without a positive weight. A bank with fewer than `count` candidates gives all of them (a short exam, not an error).
export function pickByUnitWeight<T extends UnitCandidate>(candidates: readonly T[], count: number, weights: UnitWeights | undefined, random: () => number = Math.random): T[] {
  if (count <= 0) return [];
  if (candidates.length <= count) return shuffled(candidates, random);
  const byUnit = new Map<string, T[]>();
  for (const candidate of candidates) {
    const { unitId } = candidate;
    const weight = unitId === undefined ? undefined : weights?.get(unitId);
    if (unitId === undefined || weight === undefined || !(weight > 0)) return shuffled(candidates, random).slice(0, count);
    byUnit.set(unitId, [...(byUnit.get(unitId) ?? []), candidate]);
  }
  const allotted = allocateByWeight(
    count,
    [...byUnit].map(([key, items]) => ({ key, weight: weights!.get(key)!, capacity: items.length })),
    random,
  );
  const picked = [...byUnit].flatMap(([key, items]) => shuffled(items, random).slice(0, allotted.get(key) ?? 0));
  return shuffled(picked, random);
}

export function pickExamMcqIds(questions: readonly UnitCandidate[], count: number | undefined, weights?: UnitWeights, random: () => number = Math.random): string[] {
  return pickByUnitWeight(questions, count ?? questions.length, weights, random).map((q) => q.id);
}

// One draw per non-multiple-choice section, in the order the exam format lists them, each from the prompts
// of that section's type (a section with `kinds` is one draw per kind, see exam-sections.ts). If a type has fewer
// prompts than the section asks for, the exam gets fewer rather than failing (validate-content checks the
// shipped courses never are short). A section with no matching type draws nothing: before this existed, a
// course with no plain "FRQ" section (World History) got *every* free-response prompt it had.
export function pickExamFrqIds(sections: readonly ExamSectionLike[], prompts: readonly FrqCandidate[], random: () => number = Math.random, weights?: UnitWeights): string[] {
  const picked: string[] = [];
  const used = new Set<string>();
  for (const section of sections) {
    const unitsUsed = new Set<string>();
    for (const draw of examDraws([section])) {
      let pool = prompts.filter((p) => p.type === draw.type && !used.has(p.id));
      if (draw.spreadUnits) {
        // Keep to units this section has not used if enough prompts remain there; otherwise any unit is better than a short exam.
        const fresh = pool.filter((p) => p.unitId === undefined || !unitsUsed.has(p.unitId));
        if (fresh.length >= draw.count) pool = fresh;
      }
      for (const prompt of pickByUnitWeight(pool, draw.count, weights, random)) {
        picked.push(prompt.id);
        used.add(prompt.id);
        if (prompt.unitId !== undefined) unitsUsed.add(prompt.unitId);
      }
    }
  }
  return picked;
}
