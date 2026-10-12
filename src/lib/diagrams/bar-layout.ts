// Pure layout for the bar graph: data in, pixel rectangles and error bars out, so the geometry is unit-testable
// without rendering (like geometry.ts for the line graph).
import type { PixelDims } from "./geometry";

export interface BarSeriesInput {
  values: readonly number[];
  errors?: readonly number[];
}

export interface BarRect {
  series: number;
  category: number;
  x: number;
  y: number;
  width: number;
  height: number;
  value: number;
}

export interface ErrorBarLine {
  series: number;
  category: number;
  x: number;
  yTop: number;
  yBottom: number;
  capHalfWidth: number;
}

export interface BarLayout {
  bars: BarRect[];
  errorBars: ErrorBarLine[];
  baselineY: number;
  categoryCenters: number[];
}

// A category's slot is split into a group of bars with a gap on each side; one series fills the whole group.
export const GROUP_FRACTION = 0.7;

export function yPixel(value: number, yMin: number, yMax: number, dims: PixelDims): number {
  const plotHeight = dims.height - dims.marginTop - dims.marginBottom;
  return dims.height - dims.marginBottom - ((value - yMin) / (yMax - yMin)) * plotHeight;
}

export function layoutBars(series: readonly BarSeriesInput[], categoryCount: number, yMin: number, yMax: number, dims: PixelDims): BarLayout {
  const plotWidth = dims.width - dims.marginLeft - dims.marginRight;
  const slot = plotWidth / categoryCount;
  const group = slot * GROUP_FRACTION;
  const barWidth = group / series.length;
  // Bars grow from zero, or from the nearest edge when zero is off the axis.
  const baselineY = yPixel(Math.min(Math.max(0, yMin), yMax), yMin, yMax, dims);

  const bars: BarRect[] = [];
  const errorBars: ErrorBarLine[] = [];
  series.forEach((s, si) => {
    s.values.forEach((value, ci) => {
      const x = dims.marginLeft + slot * ci + (slot - group) / 2 + barWidth * si;
      const top = yPixel(value, yMin, yMax, dims);
      bars.push({ series: si, category: ci, x, y: Math.min(top, baselineY), width: barWidth, height: Math.abs(top - baselineY), value });
      const error = s.errors?.[ci];
      if (error !== undefined && error > 0) {
        errorBars.push({
          series: si,
          category: ci,
          x: x + barWidth / 2,
          yTop: yPixel(value + error, yMin, yMax, dims),
          yBottom: yPixel(value - error, yMin, yMax, dims),
          capHalfWidth: Math.min(barWidth / 4, 8),
        });
      }
    });
  });

  const categoryCenters = Array.from({ length: categoryCount }, (_, ci) => dims.marginLeft + slot * ci + slot / 2);
  return { bars, errorBars, baselineY, categoryCenters };
}

// Category names are written under their bars; when the longest would run into its neighbours, tilt them all.
const APPROX_CHAR_WIDTH = 6.4; // px at the 11px label size
export function shouldRotateLabels(categories: readonly string[], slotWidth: number): boolean {
  const longest = Math.max(...categories.map((c) => c.length));
  return longest * APPROX_CHAR_WIDTH > slotWidth - 4;
}
