import { describe, expect, it } from "vitest";
import type { BoxplotDiagram, DensityCurveDiagram, DotplotDiagram, HistogramDiagram, ScatterplotDiagram } from "@/lib/content/diagram-schema";
import { compactNumber, decimalsOf, roundTo, scaleLinear, stepTicks } from "@/lib/diagrams/axis";
import { BOX_HEIGHT, BOX_ROW_HEIGHT, boxplotMarginLeft, layoutBoxplot } from "@/lib/diagrams/boxplot-layout";
import { interpolateY, layoutCurve } from "@/lib/diagrams/curve-layout";
import { describeBoxplot, describeDensityCurve, describeDotplot, describeHistogram, describeScatterplot } from "@/lib/diagrams/describe";
import { dotRadius, layoutDotplot, MAX_DOT_RADIUS, MIN_DOT_RADIUS } from "@/lib/diagrams/dotplot-layout";
import type { PixelDims } from "@/lib/diagrams/geometry";
import { layoutHistogram } from "@/lib/diagrams/histogram-layout";
import { clipLineToBox, layoutScatter } from "@/lib/diagrams/scatter-layout";

const DIMS: PixelDims = { width: 420, height: 300, marginLeft: 50, marginRight: 20, marginTop: 20, marginBottom: 50 };
// plot area: x 50..400 (350 wide), y 20..250 (230 tall)

describe("axis helpers", () => {
  it("rounds away floating point noise", () => {
    expect(0.1 + 0.2).not.toBe(0.3);
    expect(roundTo(0.1 + 0.2, 6)).toBe(0.3);
  });

  it("counts the decimals of a step, including very small ones", () => {
    expect(decimalsOf(5)).toBe(0);
    expect(decimalsOf(0.05)).toBe(2);
    expect(decimalsOf(2.5)).toBe(1);
    expect(decimalsOf(1e-7)).toBe(7);
  });

  it("makes ticks at the step from min to max inclusive, with clean numbers", () => {
    expect(stepTicks(0, 10, 2)).toEqual([0, 2, 4, 6, 8, 10]);
    expect(stepTicks(0, 1, 0.25)).toEqual([0, 0.25, 0.5, 0.75, 1]);
    expect(stepTicks(-2, 2, 1)).toEqual([-2, -1, 0, 1, 2]);
    const tenths = stepTicks(0, 1, 0.1);
    expect(tenths).toHaveLength(11);
    expect(tenths[3]).toBe(0.3);
  });

  it("makes no ticks when the step does not divide the range, or the range is empty", () => {
    expect(stepTicks(0, 10, 3)).toEqual([]);
    expect(stepTicks(5, 5, 1)).toEqual([]);
  });

  it("prints numbers the way a textbook does", () => {
    expect(compactNumber(2)).toBe("2");
    expect(compactNumber(2.5)).toBe("2.5");
    expect(compactNumber(0.1 + 0.2)).toBe("0.3");
    expect(compactNumber(0.05)).toBe("0.05");
    expect(compactNumber(1000)).toBe("1000");
    expect(compactNumber(-1.96)).toBe("-1.96");
  });

  it("scales a value linearly into a pixel range (and can run backwards)", () => {
    expect(scaleLinear(0, 10, 100, 200)(5)).toBe(150);
    expect(scaleLinear(0, 4, 250, 20)(2)).toBe(135);
  });
});

describe("histogram layout", () => {
  const h = { edges: [0, 10, 20, 30], values: [2, 4, 1], yMax: 4, yStep: 1, tickAt: "edges" as const, labelEvery: 1 };

  it("draws touching bars of equal width from the baseline up to each value", () => {
    const { bars, baselineY } = layoutHistogram(h, DIMS);
    expect(baselineY).toBe(250);
    expect(bars.map((b) => b.width)).toEqual([350 / 3, 350 / 3, 350 / 3]);
    expect(bars[1].x).toBeCloseTo(bars[0].x + bars[0].width);
    expect(bars[0]).toMatchObject({ x: 50, y: 135, height: 115, value: 2, from: 0, to: 10 });
    expect(bars[1]).toMatchObject({ y: 20, height: 230 });
    expect(bars[2]).toMatchObject({ y: 192.5, height: 57.5 });
  });

  it("labels the edges, so the last label is at the right end of the last bar", () => {
    const { xLabels } = layoutHistogram(h, DIMS);
    expect(xLabels.map((l) => l.text)).toEqual(["0", "10", "20", "30"]);
    expect(xLabels[0].x).toBe(50);
    expect(xLabels[3].x).toBeCloseTo(400);
  });

  it("labels the middle of each bar when the variable takes whole values", () => {
    const { xLabels } = layoutHistogram({ ...h, edges: [-0.5, 0.5, 1.5, 2.5], tickAt: "centers" }, DIMS);
    expect(xLabels.map((l) => l.text)).toEqual(["0", "1", "2"]);
    expect(xLabels[0].x).toBeCloseTo(50 + 350 / 6);
  });

  it("labels only every nth edge when asked", () => {
    const { xLabels } = layoutHistogram({ ...h, edges: [0, 10, 20, 30, 40], values: [1, 2, 3, 4], labelEvery: 2 }, DIMS);
    expect(xLabels.map((l) => l.text)).toEqual(["0", "20", "40"]);
  });

  it("puts a tick on the y axis at each step", () => {
    const { yTicks } = layoutHistogram(h, DIMS);
    expect(yTicks.map((t) => t.text)).toEqual(["0", "1", "2", "3", "4"]);
    expect(yTicks.map((t) => t.y)).toEqual([250, 192.5, 135, 77.5, 20]);
  });
});

describe("boxplot layout", () => {
  const b: BoxplotDiagram = { type: "boxplot", xLabel: "x", axisMin: 0, axisMax: 16, axisStep: 4, groups: [{ min: 2, q1: 4, median: 6, q3: 8, max: 10, outliers: [14] }] };

  it("maps the five numbers and the outliers onto the axis", () => {
    const l = layoutBoxplot(b, 420);
    // one plot: no room for names on the left, so the axis runs from x=24 to x=400 (23.5 px per unit)
    expect(l.axisLeft).toBe(24);
    expect(l.axisRight).toBe(400);
    expect(l.rows[0]).toMatchObject({ min: 71, q1: 118, median: 165, q3: 212, max: 259, outliers: [353] });
  });

  it("centres the box in its row, above the axis", () => {
    const l = layoutBoxplot(b, 420);
    expect(l.rows[0].cy).toBe(14 + BOX_ROW_HEIGHT / 2);
    expect(l.rows[0].boxBottom - l.rows[0].boxTop).toBe(BOX_HEIGHT);
    expect(l.axisY).toBe(14 + BOX_ROW_HEIGHT);
    expect(l.height).toBe(l.axisY + 48);
  });

  it("puts a tick at each step of the axis", () => {
    const l = layoutBoxplot(b, 420);
    expect(l.ticks.map((t) => t.text)).toEqual(["0", "4", "8", "12", "16"]);
    expect(l.ticks.map((t) => t.x)).toEqual([24, 118, 212, 306, 400]);
  });

  it("stacks several boxplots on one axis and leaves room on the left for their names", () => {
    const two: BoxplotDiagram = { ...b, groups: [{ label: "Treatment group", min: 2, q1: 4, median: 6, q3: 8, max: 10 }, { label: "Control", min: 1, q1: 3, median: 5, q3: 7, max: 9 }] };
    const l = layoutBoxplot(two, 420);
    expect(l.rows).toHaveLength(2);
    expect(l.rows[1].cy - l.rows[0].cy).toBe(BOX_ROW_HEIGHT);
    expect(l.axisLeft).toBe(boxplotMarginLeft(["Treatment group", "Control"], true));
    expect(l.axisLeft).toBeGreaterThan(24);
    expect(l.axisY).toBe(14 + 2 * BOX_ROW_HEIGHT);
  });

  it("keeps the room for names between 60 and 150 px", () => {
    expect(boxplotMarginLeft(["A", "B"], true)).toBe(60);
    expect(boxplotMarginLeft(["x".repeat(60), "B"], true)).toBe(150);
  });
});

describe("dotplot layout", () => {
  const d = { axisMin: 0, axisMax: 10, axisStep: 1, dots: [{ x: 3, count: 2 }, { x: 4, count: 1 }] };

  it("stacks the dots above their value, bottom one first", () => {
    const l = layoutDotplot(d, 420);
    // 37.6 px per unit between x=24 and x=400; the gap between stacks allows the largest dots
    expect(l.radius).toBe(MAX_DOT_RADIUS);
    expect(l.axisY).toBe(12 + 2 * (2 * 7 + 1) + 6);
    const first = l.dots.filter((dot) => Math.abs(dot.cx - (24 + 3 * 37.6)) < 0.01);
    expect(first).toHaveLength(2);
    expect(first[0].cy).toBe(l.axisY - 2 - 7);
    expect(first[1].cy).toBe(first[0].cy - 15);
    expect(l.dots).toHaveLength(3);
  });

  it("draws one dot per count, in total", () => {
    expect(layoutDotplot({ ...d, dots: [{ x: 1, count: 5 }, { x: 2, count: 3 }, { x: 5, count: 7 }] }, 420).dots).toHaveLength(15);
  });

  it("shrinks the dots when two stacks are close, but never below the minimum", () => {
    expect(dotRadius([100, 120, 300])).toBe(MAX_DOT_RADIUS);
    expect(dotRadius([100, 108])).toBeCloseTo(4 - 0.75);
    expect(dotRadius([100, 101])).toBe(MIN_DOT_RADIUS);
    expect(dotRadius([100])).toBe(MAX_DOT_RADIUS);
  });

  it("makes the picture as tall as the tallest stack needs", () => {
    const short = layoutDotplot({ ...d, dots: [{ x: 3, count: 1 }] }, 420);
    const tall = layoutDotplot({ ...d, dots: [{ x: 3, count: 10 }] }, 420);
    expect(tall.height - short.height).toBe(9 * 15);
    expect(tall.height).toBe(tall.axisY + 48);
  });

  it("puts a tick at each step of the axis", () => {
    expect(layoutDotplot(d, 420).ticks.map((t) => t.text)).toEqual(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]);
  });
});

describe("scatterplot layout", () => {
  const s: ScatterplotDiagram = {
    type: "scatterplot",
    xLabel: "x",
    yLabel: "y",
    xMin: 0,
    xMax: 10,
    xStep: 5,
    yMin: 0,
    yMax: 10,
    yStep: 5,
    points: [{ x: 5, y: 5 }, { x: 0, y: 0 }],
    zeroLine: false,
  };

  it("projects each point into the plot, y growing upward", () => {
    const l = layoutScatter(s, DIMS);
    expect(l.points[0]).toMatchObject({ cx: 225, cy: 135, index: 0 });
    expect(l.points[1]).toMatchObject({ cx: 50, cy: 250, index: 1 });
  });

  it("clips the fitted line where it leaves the plot", () => {
    expect(clipLineToBox(1, 1, 0, 10, 0, 10)).toEqual({ x1: 0, y1: 1, x2: 9, y2: 10 });
    expect(clipLineToBox(10, -2, 0, 10, 0, 10)).toEqual({ x1: 0, y1: 10, x2: 5, y2: 0 });
    expect(clipLineToBox(5, 0, 0, 10, 0, 10)).toEqual({ x1: 0, y1: 5, x2: 10, y2: 5 });
  });

  it("draws no line when it never passes through the plot", () => {
    expect(clipLineToBox(20, 1, 0, 10, 0, 10)).toBeNull();
    expect(clipLineToBox(12, 0, 0, 10, 0, 10)).toBeNull();
    expect(layoutScatter({ ...s, line: { intercept: 20, slope: 1 } }, DIMS).line).toBeNull();
  });

  it("converts the clipped line to pixels", () => {
    const l = layoutScatter({ ...s, line: { intercept: 0, slope: 1 } }, DIMS);
    expect(l.line).toEqual({ x1: 50, y1: 250, x2: 400, y2: 20 });
  });

  it("draws the zero line of a residual plot only when zero is on the axis", () => {
    expect(layoutScatter({ ...s, yMin: -5, yMax: 5, zeroLine: true }, DIMS).zeroLineY).toBe(135);
    expect(layoutScatter(s, DIMS).zeroLineY).toBeNull();
    expect(layoutScatter({ ...s, zeroLine: true }, DIMS).zeroLineY).toBeNull();
  });

  it("puts the highlight label at its point", () => {
    const l = layoutScatter({ ...s, highlights: [{ index: 1, label: "A" }] }, DIMS);
    expect(l.highlights).toEqual([{ cx: 50, cy: 250, label: "A" }]);
  });

  it("ticks both axes at their steps", () => {
    const l = layoutScatter(s, DIMS);
    expect(l.xTicks.map((t) => t.text)).toEqual(["0", "5", "10"]);
    expect(l.yTicks.map((t) => [t.text, t.y])).toEqual([["0", 250], ["5", 135], ["10", 20]]);
  });
});

describe("density curve layout", () => {
  const tent = [{ x: 0, y: 0 }, { x: 1, y: 1 }, { x: 2, y: 0 }];
  const CDIMS: PixelDims = { width: 420, height: 230, marginLeft: 20, marginRight: 20, marginTop: 14, marginBottom: 48 };

  it("reads the curve's height between its points by straight lines", () => {
    expect(interpolateY(tent, 0.5)).toBe(0.5);
    expect(interpolateY(tent, 1.5)).toBe(0.5);
    expect(interpolateY(tent, 1)).toBe(1);
    expect(interpolateY([{ x: 0, y: 0 }, { x: 4, y: 8 }], 1)).toBe(2);
    expect(interpolateY([{ x: 0, y: 0 }, { x: 4, y: 8 }, { x: 6, y: 0 }], 5)).toBe(4);
    expect(interpolateY(tent, -3)).toBe(0);
    expect(interpolateY(tent, 9)).toBe(0);
  });

  it("draws the curve as one path through every point", () => {
    const { path } = layoutCurve({ points: tent, ticks: [] }, CDIMS);
    expect(path.startsWith("M")).toBe(true);
    expect((path.match(/L/g) ?? []).length).toBe(2);
  });

  it("closes a shaded region down to the axis, with its edges cut exactly at the ends", () => {
    const { areas, baselineY } = layoutCurve({ points: tent, shade: [{ from: 0.5, to: 1.5 }], ticks: [] }, CDIMS);
    expect(baselineY).toBe(230 - 48);
    expect(areas).toHaveLength(1);
    // along the axis, up to the curve at 0.5, over the peak, down at 1.5, back to the axis, close
    expect((areas[0].match(/L/g) ?? []).length).toBe(4);
    expect(areas[0].endsWith("Z")).toBe(true);
    expect(areas[0].startsWith(`M${(20 + 0.25 * 380).toFixed(1)} ${baselineY.toFixed(1)}`)).toBe(true);
  });

  it("makes one area per shaded region and none when nothing is shaded", () => {
    expect(layoutCurve({ points: tent, shade: [{ from: 0, to: 0.5 }, { from: 1.5, to: 2 }], ticks: [] }, CDIMS).areas).toHaveLength(2);
    expect(layoutCurve({ points: tent, ticks: [] }, CDIMS).areas).toEqual([]);
  });

  it("places each labelled tick at its value", () => {
    const { ticks } = layoutCurve({ points: tent, ticks: [{ x: 0, label: "a" }, { x: 1, label: "b" }, { x: 2, label: "c" }] }, CDIMS);
    expect(ticks).toEqual([{ x: 20, text: "a" }, { x: 210, text: "b" }, { x: 400, text: "c" }]);
  });
});

describe("text equivalents", () => {
  const hist: HistogramDiagram = { type: "histogram", xLabel: "Commute (min)", yLabel: "Frequency", edges: [0, 10, 20], values: [3, 8], yMax: 10, yStep: 2, tickAt: "edges", labelEvery: 1 };
  it("describes a histogram bar by bar", () => {
    expect(describeHistogram(hist)).toBe("Histogram of Commute (min). Frequency by interval: 0 to 10: 3; 10 to 20: 8.");
  });

  const box: BoxplotDiagram = { type: "boxplot", xLabel: "Duration (s)", axisMin: 0, axisMax: 100, axisStep: 20, groups: [{ label: "DES", min: 1, q1: 22.6, median: 54, q3: 110.7, max: 695, outliers: [800] }] };
  it("describes each boxplot's five numbers and outliers", () => {
    expect(describeBoxplot(box)).toBe("Boxplot of Duration (s). DES: minimum 1, Q1 22.6, median 54, Q3 110.7, maximum 695, outliers at 800.");
    expect(describeBoxplot({ ...box, groups: [...box.groups, { label: "AES", min: 2, q1: 3, median: 4, q3: 5, max: 6 }] })).toMatch(/^Boxplots of Duration/);
  });

  const dots: DotplotDiagram = { type: "dotplot", xLabel: "Pets", axisMin: 0, axisMax: 5, axisStep: 1, dots: [{ x: 2, count: 4 }, { x: 0, count: 3 }] };
  it("describes a dotplot in order of value", () => {
    expect(describeDotplot(dots)).toBe("Dotplot of Pets, with the number of dots at each value: 0 (3), 2 (4).");
  });

  const sc: ScatterplotDiagram = { type: "scatterplot", xLabel: "Dash time", yLabel: "Jump", xMin: 6, xMax: 10, xStep: 1, yMin: -20, yMax: 20, yStep: 10, points: [{ x: 7, y: 5.5 }, { x: 8, y: -4 }], zeroLine: false };
  it("describes a scatterplot's points, its line, and a residual plot", () => {
    expect(describeScatterplot({ ...sc, line: { intercept: 313.875, slope: -30.805 } })).toBe(
      "Scatterplot of Jump against Dash time, 2 points: (7, 5.5), (8, -4). The least-squares line y = 313.875 - 30.805x is drawn.",
    );
    expect(describeScatterplot({ ...sc, zeroLine: true })).toBe("Residual plot of Jump against Dash time, 2 points: (7, 5.5), (8, -4). A dashed line marks zero.");
  });

  const pts = Array.from({ length: 20 }, (_, i) => ({ x: i, y: i }));
  const curve: DensityCurveDiagram = { type: "density-curve", xLabel: "z", points: pts, shade: [{ from: 1.5, to: 19 }], ticks: [{ x: 0, label: "0" }, { x: 1.5, label: "z = 1.5" }] };
  it("describes a density curve with its shaded regions and marked values", () => {
    expect(describeDensityCurve(curve)).toBe("Density curve of z. Shaded: from 1.5 to 19. Marked on the axis: 0 at 0, z = 1.5 at 1.5.");
    expect(describeDensityCurve({ type: "density-curve", points: pts, ticks: [] })).toBe("Density curve.");
  });
});
