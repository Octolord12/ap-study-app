// Pure layout for a dotplot: a stack of dots above each value, sized so neighbouring stacks do not touch.
import { compactNumber, scaleLinear, stepTicks } from "./axis";

const MARGIN_LEFT = 24;
const MARGIN_RIGHT = 20;
const MARGIN_TOP = 12;
const MARGIN_BOTTOM = 48;
export const MIN_DOT_RADIUS = 2.5;
export const MAX_DOT_RADIUS = 7;

export interface DotplotInput {
  axisMin: number;
  axisMax: number;
  axisStep: number;
  dots: readonly { x: number; count: number }[];
}

export interface DotplotLayout {
  radius: number;
  dots: { cx: number; cy: number }[];
  axisY: number;
  axisLeft: number;
  axisRight: number;
  ticks: { x: number; text: string }[];
  width: number;
  height: number;
}

// As large as fits between the closest two stacks, within sensible limits.
export function dotRadius(xsInPixels: readonly number[]): number {
  const sorted = [...xsInPixels].sort((a, b) => a - b);
  let gap = Infinity;
  for (let i = 1; i < sorted.length; i++) gap = Math.min(gap, sorted[i] - sorted[i - 1]);
  return Math.min(MAX_DOT_RADIUS, Math.max(MIN_DOT_RADIUS, gap / 2 - 0.75));
}

export function layoutDotplot(d: DotplotInput, width: number): DotplotLayout {
  const xOf = scaleLinear(d.axisMin, d.axisMax, MARGIN_LEFT, width - MARGIN_RIGHT);
  const radius = dotRadius(d.dots.map((dot) => xOf(dot.x)));
  const pitch = 2 * radius + 1;
  const tallest = Math.max(...d.dots.map((dot) => dot.count));
  const axisY = MARGIN_TOP + tallest * pitch + 6;
  const dots: DotplotLayout["dots"] = [];
  for (const dot of d.dots) {
    for (let k = 0; k < dot.count; k++) dots.push({ cx: xOf(dot.x), cy: axisY - 2 - radius - k * pitch });
  }
  return {
    radius,
    dots,
    axisY,
    axisLeft: MARGIN_LEFT,
    axisRight: width - MARGIN_RIGHT,
    ticks: stepTicks(d.axisMin, d.axisMax, d.axisStep).map((t) => ({ x: xOf(t), text: compactNumber(t) })),
    width,
    height: axisY + MARGIN_BOTTOM,
  };
}
