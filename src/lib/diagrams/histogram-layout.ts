// Pure layout for the histogram: data in, pixel rectangles and axis labels out (like bar-layout.ts).
import { compactNumber, scaleLinear, stepTicks } from "./axis";
import type { PixelDims } from "./geometry";

export interface HistogramInput {
  edges: readonly number[];
  values: readonly number[];
  yMax: number;
  yStep: number;
  tickAt: "edges" | "centers";
  labelEvery: number;
}

export interface HistogramBarRect {
  x: number;
  y: number;
  width: number;
  height: number;
  value: number;
  from: number;
  to: number;
}

export interface HistogramLayout {
  bars: HistogramBarRect[];
  baselineY: number;
  xLabels: { x: number; text: string }[];
  yTicks: { y: number; text: string }[];
}

export function layoutHistogram(d: HistogramInput, dims: PixelDims): HistogramLayout {
  const plotWidth = dims.width - dims.marginLeft - dims.marginRight;
  const barWidth = plotWidth / d.values.length;
  const baselineY = dims.height - dims.marginBottom;
  const yOf = scaleLinear(0, d.yMax, baselineY, dims.marginTop);

  const bars = d.values.map((value, i) => ({
    x: dims.marginLeft + i * barWidth,
    y: yOf(value),
    width: barWidth,
    height: baselineY - yOf(value),
    value,
    from: d.edges[i],
    to: d.edges[i + 1],
  }));

  const xLabels: HistogramLayout["xLabels"] = [];
  if (d.tickAt === "edges") {
    for (let i = 0; i < d.edges.length; i += d.labelEvery) xLabels.push({ x: dims.marginLeft + i * barWidth, text: compactNumber(d.edges[i]) });
  } else {
    for (let i = 0; i < d.values.length; i += d.labelEvery) xLabels.push({ x: dims.marginLeft + (i + 0.5) * barWidth, text: compactNumber((d.edges[i] + d.edges[i + 1]) / 2) });
  }

  const yTicks = stepTicks(0, d.yMax, d.yStep).map((t) => ({ y: yOf(t), text: compactNumber(t) }));
  return { bars, baselineY, xLabels, yTicks };
}
