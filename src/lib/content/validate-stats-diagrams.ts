import { stepTicks } from "../diagrams/axis";
import type { BoxplotDiagram, DensityCurveDiagram, DotplotDiagram, HistogramDiagram, ScatterplotDiagram } from "./diagram-schema";

type Problem = { message: string };

const MAX_TICKS = 21;

function axisProblems(kind: string, name: string, min: number, max: number, step: number): Problem[] {
  if (!(max > min)) return [{ message: `${kind}: ${name} max (${max}) must be greater than min (${min})` }];
  const ticks = stepTicks(min, max, step);
  if (ticks.length === 0) return [{ message: `${kind}: ${name} step ${step} does not divide [${min}, ${max}] evenly` }];
  if (ticks.length > MAX_TICKS) return [{ message: `${kind}: ${name} has ${ticks.length} tick marks; use a bigger step` }];
  return [];
}

export function validateHistogram(d: HistogramDiagram): Problem[] {
  const problems: Problem[] = [];
  if (d.edges.length !== d.values.length + 1) {
    problems.push({ message: `histogram: ${d.values.length} bar(s) need ${d.values.length + 1} edges, but there are ${d.edges.length}` });
    return problems;
  }
  const widths = d.edges.slice(1).map((e, i) => e - d.edges[i]);
  if (widths.some((w) => !(w > 0))) problems.push({ message: "histogram: edges must increase" });
  else if (widths.some((w) => Math.abs(w - widths[0]) > widths[0] * 1e-6)) problems.push({ message: "histogram: bars must all be the same width" });
  problems.push(...axisProblems("histogram", "y axis", 0, d.yMax, d.yStep));
  const tallest = Math.max(...d.values);
  if (tallest > d.yMax) problems.push({ message: `histogram: the tallest bar (${tallest}) is above yMax (${d.yMax})` });
  return problems;
}

export function validateBoxplot(d: BoxplotDiagram): Problem[] {
  const problems = axisProblems("boxplot", "axis", d.axisMin, d.axisMax, d.axisStep);
  const labels = d.groups.map((g) => g.label);
  d.groups.forEach((g, i) => {
    const name = g.label ?? `group ${i + 1}`;
    if (d.groups.length > 1 && !g.label) problems.push({ message: `boxplot: group ${i + 1} needs a label (several boxplots share the axis)` });
    const five = [g.min, g.q1, g.median, g.q3, g.max];
    if (five.some((v, k) => k > 0 && v < five[k - 1])) problems.push({ message: `boxplot: ${name}: min, Q1, median, Q3, max must not decrease` });
    const outliers = g.outliers ?? [];
    for (const value of [...five, ...outliers]) {
      if (value < d.axisMin || value > d.axisMax) problems.push({ message: `boxplot: ${name}: ${value} is outside the axis [${d.axisMin}, ${d.axisMax}]` });
    }
    for (const o of outliers) {
      if (o >= g.min && o <= g.max) problems.push({ message: `boxplot: ${name}: outlier ${o} lies between the whiskers (${g.min} and ${g.max})` });
    }
  });
  if (new Set(labels.filter(Boolean)).size !== labels.filter(Boolean).length) problems.push({ message: "boxplot: duplicate group label" });
  return problems;
}

export function validateDotplot(d: DotplotDiagram): Problem[] {
  const problems = axisProblems("dotplot", "axis", d.axisMin, d.axisMax, d.axisStep);
  const seen = new Set<number>();
  for (const dot of d.dots) {
    if (dot.x < d.axisMin || dot.x > d.axisMax) problems.push({ message: `dotplot: x=${dot.x} is outside the axis [${d.axisMin}, ${d.axisMax}]` });
    if (seen.has(dot.x)) problems.push({ message: `dotplot: x=${dot.x} appears twice; give one stack its total count` });
    seen.add(dot.x);
  }
  return problems;
}

export function validateScatterplot(d: ScatterplotDiagram): Problem[] {
  const problems = [...axisProblems("scatterplot", "x axis", d.xMin, d.xMax, d.xStep), ...axisProblems("scatterplot", "y axis", d.yMin, d.yMax, d.yStep)];
  d.points.forEach((p, i) => {
    if (p.x < d.xMin || p.x > d.xMax) problems.push({ message: `scatterplot: point ${i} has x=${p.x}, outside [${d.xMin}, ${d.xMax}]` });
    if (p.y < d.yMin || p.y > d.yMax) problems.push({ message: `scatterplot: point ${i} has y=${p.y}, outside [${d.yMin}, ${d.yMax}]` });
  });
  if (d.zeroLine && !(d.yMin < 0 && d.yMax > 0)) problems.push({ message: "scatterplot: zeroLine needs 0 to be inside the y axis" });
  const marked = new Set<number>();
  for (const h of d.highlights ?? []) {
    if (h.index >= d.points.length) problems.push({ message: `scatterplot: highlight index ${h.index} is not a point` });
    if (marked.has(h.index)) problems.push({ message: `scatterplot: point ${h.index} is highlighted twice` });
    marked.add(h.index);
  }
  return problems;
}

export function validateDensityCurve(d: DensityCurveDiagram): Problem[] {
  const problems: Problem[] = [];
  d.points.forEach((p, i) => {
    if (i > 0 && !(p.x > d.points[i - 1].x)) problems.push({ message: `density-curve: x must increase (point ${i})` });
    if (p.y < 0) problems.push({ message: `density-curve: point ${i} is below the axis` });
  });
  const lo = d.points[0].x;
  const hi = d.points[d.points.length - 1].x;
  for (const s of d.shade ?? []) {
    if (!(s.from < s.to)) problems.push({ message: `density-curve: shaded region [${s.from}, ${s.to}] must run from the smaller to the larger value` });
    if (s.from < lo || s.to > hi) problems.push({ message: `density-curve: shaded region [${s.from}, ${s.to}] is outside the curve [${lo}, ${hi}]` });
  }
  for (const t of d.ticks) {
    if (t.x < lo || t.x > hi) problems.push({ message: `density-curve: tick "${t.label}" at ${t.x} is outside the curve [${lo}, ${hi}]` });
  }
  return problems;
}
