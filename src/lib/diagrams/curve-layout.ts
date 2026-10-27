// Pure layout for a density curve with shaded regions (a probability, a p-value, a critical region).
import { scaleLinear } from "./axis";
import type { PixelDims } from "./geometry";

export interface CurveInput {
  points: readonly { x: number; y: number }[];
  shade?: readonly { from: number; to: number }[];
  ticks: readonly { x: number; label: string }[];
}

export interface CurveLayout {
  path: string;
  areas: string[];
  baselineY: number;
  axisLeft: number;
  axisRight: number;
  ticks: { x: number; text: string }[];
}

// The curve's height at x, by straight lines between the given points.
export function interpolateY(points: readonly { x: number; y: number }[], x: number): number {
  if (x <= points[0].x) return points[0].y;
  const last = points[points.length - 1];
  if (x >= last.x) return last.y;
  const i = points.findIndex((p) => p.x >= x);
  const a = points[i - 1];
  const b = points[i];
  return a.y + ((x - a.x) / (b.x - a.x)) * (b.y - a.y);
}

const fmt = (n: number) => n.toFixed(1);

export function layoutCurve(d: CurveInput, dims: PixelDims): CurveLayout {
  const xMin = d.points[0].x;
  const xMax = d.points[d.points.length - 1].x;
  const tallest = Math.max(...d.points.map((p) => p.y));
  const baselineY = dims.height - dims.marginBottom;
  const xOf = scaleLinear(xMin, xMax, dims.marginLeft, dims.width - dims.marginRight);
  const yOf = scaleLinear(0, tallest * 1.08, baselineY, dims.marginTop);

  const path = d.points.map((p, i) => `${i === 0 ? "M" : "L"}${fmt(xOf(p.x))} ${fmt(yOf(p.y))}`).join(" ");

  const areas = (d.shade ?? []).map(({ from, to }) => {
    const inside = d.points.filter((p) => p.x > from && p.x < to);
    const edge = [{ x: from, y: interpolateY(d.points, from) }, ...inside, { x: to, y: interpolateY(d.points, to) }];
    const top = edge.map((p) => `L${fmt(xOf(p.x))} ${fmt(yOf(p.y))}`).join(" ");
    return `M${fmt(xOf(from))} ${fmt(baselineY)} ${top} L${fmt(xOf(to))} ${fmt(baselineY)} Z`;
  });

  return {
    path,
    areas,
    baselineY,
    axisLeft: dims.marginLeft,
    axisRight: dims.width - dims.marginRight,
    ticks: d.ticks.map((t) => ({ x: xOf(t.x), text: t.label })),
  };
}
