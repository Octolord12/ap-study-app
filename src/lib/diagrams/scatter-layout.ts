// Pure layout for the scatterplot, with the fitted line clipped to the plot and the zero line of a residual plot.
import { compactNumber, stepTicks } from "./axis";
import { projectPoint, type PixelDims } from "./geometry";

export interface ScatterInput {
  xMin: number;
  xMax: number;
  xStep: number;
  yMin: number;
  yMax: number;
  yStep: number;
  points: readonly { x: number; y: number }[];
  line?: { intercept: number; slope: number };
  zeroLine?: boolean;
  highlights?: readonly { index: number; label: string }[];
}

export interface ScatterLayout {
  points: { cx: number; cy: number; index: number }[];
  line: { x1: number; y1: number; x2: number; y2: number } | null;
  zeroLineY: number | null;
  xTicks: { x: number; text: string }[];
  yTicks: { y: number; text: string }[];
  highlights: { cx: number; cy: number; label: string }[];
}

// The part of y = intercept + slope * x that lies inside the plot, in data coordinates; null when none of it does.
export function clipLineToBox(intercept: number, slope: number, xMin: number, xMax: number, yMin: number, yMax: number): { x1: number; y1: number; x2: number; y2: number } | null {
  let lo = xMin;
  let hi = xMax;
  if (slope === 0) {
    if (intercept < yMin || intercept > yMax) return null;
  } else {
    const atMin = (yMin - intercept) / slope;
    const atMax = (yMax - intercept) / slope;
    lo = Math.max(lo, Math.min(atMin, atMax));
    hi = Math.min(hi, Math.max(atMin, atMax));
  }
  if (lo > hi) return null;
  return { x1: lo, y1: intercept + slope * lo, x2: hi, y2: intercept + slope * hi };
}

export function layoutScatter(d: ScatterInput, dims: PixelDims): ScatterLayout {
  const bounds = { xMin: d.xMin, xMax: d.xMax, yMin: d.yMin, yMax: d.yMax };
  const at = (x: number, y: number) => projectPoint({ x, y }, bounds, dims);

  const clipped = d.line ? clipLineToBox(d.line.intercept, d.line.slope, d.xMin, d.xMax, d.yMin, d.yMax) : null;
  const line = clipped ? { x1: at(clipped.x1, clipped.y1).px, y1: at(clipped.x1, clipped.y1).py, x2: at(clipped.x2, clipped.y2).px, y2: at(clipped.x2, clipped.y2).py } : null;

  return {
    points: d.points.map((p, index) => ({ cx: at(p.x, p.y).px, cy: at(p.x, p.y).py, index })),
    line,
    zeroLineY: d.zeroLine && d.yMin < 0 && d.yMax > 0 ? at(d.xMin, 0).py : null,
    xTicks: stepTicks(d.xMin, d.xMax, d.xStep).map((t) => ({ x: at(t, d.yMin).px, text: compactNumber(t) })),
    yTicks: stepTicks(d.yMin, d.yMax, d.yStep).map((t) => ({ y: at(d.xMin, t).py, text: compactNumber(t) })),
    highlights: (d.highlights ?? []).map((h) => ({ cx: at(d.points[h.index].x, d.points[h.index].y).px, cy: at(d.points[h.index].x, d.points[h.index].y).py, label: h.label })),
  };
}
