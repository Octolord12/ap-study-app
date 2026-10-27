// Pure layout for horizontal boxplots sharing one axis (the way AP Statistics draws them).
import { compactNumber, scaleLinear, stepTicks } from "./axis";

export const BOX_HEIGHT = 28;
export const BOX_ROW_HEIGHT = 54;
const MARGIN_RIGHT = 20;
const MARGIN_TOP = 14;
const MARGIN_BOTTOM = 48;
const APPROX_CHAR_WIDTH = 6.2; // px at the 11px label size

export interface BoxplotInput {
  axisMin: number;
  axisMax: number;
  axisStep: number;
  groups: readonly { label?: string; min: number; q1: number; median: number; q3: number; max: number; outliers?: readonly number[] }[];
}

export interface BoxRow {
  label?: string;
  cy: number;
  boxTop: number;
  boxBottom: number;
  min: number;
  q1: number;
  median: number;
  q3: number;
  max: number;
  outliers: number[];
}

export interface BoxplotLayout {
  rows: BoxRow[];
  axisY: number;
  axisLeft: number;
  axisRight: number;
  ticks: { x: number; text: string }[];
  width: number;
  height: number;
}

// Room on the left for the group names, which sit beside their boxes; a single plot needs none.
export function boxplotMarginLeft(labels: readonly (string | undefined)[], several: boolean): number {
  if (!several) return 24;
  const longest = Math.max(...labels.map((l) => l?.length ?? 0));
  return Math.min(150, Math.max(60, 14 + longest * APPROX_CHAR_WIDTH));
}

export function layoutBoxplot(d: BoxplotInput, width: number): BoxplotLayout {
  const marginLeft = boxplotMarginLeft(d.groups.map((g) => g.label), d.groups.length > 1);
  const xOf = scaleLinear(d.axisMin, d.axisMax, marginLeft, width - MARGIN_RIGHT);
  const rows = d.groups.map((g, i): BoxRow => {
    const cy = MARGIN_TOP + BOX_ROW_HEIGHT * i + BOX_ROW_HEIGHT / 2;
    return {
      label: g.label,
      cy,
      boxTop: cy - BOX_HEIGHT / 2,
      boxBottom: cy + BOX_HEIGHT / 2,
      min: xOf(g.min),
      q1: xOf(g.q1),
      median: xOf(g.median),
      q3: xOf(g.q3),
      max: xOf(g.max),
      outliers: (g.outliers ?? []).map(xOf),
    };
  });
  const axisY = MARGIN_TOP + BOX_ROW_HEIGHT * d.groups.length;
  return {
    rows,
    axisY,
    axisLeft: marginLeft,
    axisRight: width - MARGIN_RIGHT,
    ticks: stepTicks(d.axisMin, d.axisMax, d.axisStep).map((t) => ({ x: xOf(t), text: compactNumber(t) })),
    width,
    height: axisY + MARGIN_BOTTOM,
  };
}
