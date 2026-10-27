import { describe, expect, it } from "vitest";
import { DiagramSchema, type BoxplotDiagram, type DensityCurveDiagram, type DotplotDiagram, type HistogramDiagram, type ScatterplotDiagram } from "@/lib/content/diagram-schema";
import { validateDiagram } from "@/lib/content/validate";

const histogram = (o: Partial<HistogramDiagram> = {}): HistogramDiagram => ({
  type: "histogram",
  xLabel: "Commute time (minutes)",
  yLabel: "Frequency",
  edges: [0, 10, 20, 30, 40],
  values: [3, 8, 5, 1],
  yMax: 10,
  yStep: 2,
  tickAt: "edges",
  labelEvery: 1,
  ...o,
});

const boxplot = (o: Partial<BoxplotDiagram> = {}): BoxplotDiagram => ({
  type: "boxplot",
  xLabel: "Session duration (seconds)",
  axisMin: 0,
  axisMax: 100,
  axisStep: 20,
  groups: [{ min: 10, q1: 30, median: 45, q3: 60, max: 90, outliers: [98] }],
  ...o,
});

const dotplot = (o: Partial<DotplotDiagram> = {}): DotplotDiagram => ({
  type: "dotplot",
  xLabel: "Number of pets",
  axisMin: 0,
  axisMax: 6,
  axisStep: 1,
  dots: [{ x: 0, count: 3 }, { x: 1, count: 6 }, { x: 2, count: 4 }],
  ...o,
});

const scatter = (o: Partial<ScatterplotDiagram> = {}): ScatterplotDiagram => ({
  type: "scatterplot",
  xLabel: "Dash time (s)",
  yLabel: "Long jump (in)",
  xMin: 6,
  xMax: 10,
  xStep: 1,
  yMin: 60,
  yMax: 140,
  yStep: 20,
  points: [{ x: 7, y: 120 }, { x: 8, y: 100 }, { x: 9, y: 80 }],
  zeroLine: false,
  ...o,
});

const curvePoints = Array.from({ length: 41 }, (_, i) => {
  const x = -4 + i * 0.2;
  return { x: Math.round(x * 10) / 10, y: Math.exp((-x * x) / 2) / Math.sqrt(2 * Math.PI) };
});
const curve = (o: Partial<DensityCurveDiagram> = {}): DensityCurveDiagram => ({
  type: "density-curve",
  points: curvePoints,
  shade: [{ from: 1.2, to: 4 }],
  ticks: [{ x: 0, label: "0" }, { x: 1.2, label: "z = 1.2" }],
  ...o,
});

const messages = (d: Parameters<typeof validateDiagram>[0]) => validateDiagram(d).map((p) => p.message);

describe("histogram", () => {
  it("is accepted by the schema and has no problems; yLabel defaults to Frequency", () => {
    expect(DiagramSchema.safeParse(histogram()).success).toBe(true);
    expect(validateDiagram(histogram())).toEqual([]);
    const { yLabel: _omit, ...rest } = histogram();
    void _omit;
    const parsed = DiagramSchema.parse(rest);
    expect(parsed.type === "histogram" && parsed.yLabel).toBe("Frequency");
  });

  it("needs one more edge than bars", () => {
    expect(messages(histogram({ edges: [0, 10, 20, 30] }))).toEqual(["histogram: 4 bar(s) need 5 edges, but there are 4"]);
  });

  it("flags edges that do not increase and bars of different widths", () => {
    expect(messages(histogram({ edges: [0, 10, 10, 30, 40] }))).toEqual(["histogram: edges must increase"]);
    expect(messages(histogram({ edges: [0, 10, 20, 40, 50] }))).toEqual(["histogram: bars must all be the same width"]);
  });

  it("flags a bar above the top of the axis and a step that does not divide it", () => {
    expect(messages(histogram({ values: [3, 12, 5, 1] }))).toEqual(["histogram: the tallest bar (12) is above yMax (10)"]);
    expect(messages(histogram({ yStep: 3 }))).toEqual(["histogram: y axis step 3 does not divide [0, 10] evenly"]);
  });

  it("rejects a histogram with a single bar, a negative height, or too many bins", () => {
    expect(DiagramSchema.safeParse(histogram({ edges: [0, 10], values: [4] })).success).toBe(false);
    expect(DiagramSchema.safeParse(histogram({ values: [3, -1, 5, 1] })).success).toBe(false);
    expect(DiagramSchema.safeParse(histogram({ edges: Array.from({ length: 27 }, (_, i) => i), values: Array(26).fill(1) })).success).toBe(false);
  });
});

describe("boxplot", () => {
  it("is accepted and has no problems, with one group (no label) or several (labelled)", () => {
    expect(DiagramSchema.safeParse(boxplot()).success).toBe(true);
    expect(validateDiagram(boxplot())).toEqual([]);
    const two = boxplot({ groups: [{ label: "DES", min: 10, q1: 30, median: 45, q3: 60, max: 90 }, { label: "AES", min: 5, q1: 25, median: 50, q3: 70, max: 95 }] });
    expect(validateDiagram(two)).toEqual([]);
  });

  it("needs a label on each group once there are several", () => {
    const two = boxplot({ groups: [{ label: "DES", min: 10, q1: 30, median: 45, q3: 60, max: 90 }, { min: 5, q1: 25, median: 50, q3: 70, max: 95 }] });
    expect(messages(two)).toEqual(["boxplot: group 2 needs a label (several boxplots share the axis)"]);
    const same = boxplot({ groups: [{ label: "A", min: 1, q1: 2, median: 3, q3: 4, max: 5 }, { label: "A", min: 1, q1: 2, median: 3, q3: 4, max: 5 }] });
    expect(messages(same)).toEqual(["boxplot: duplicate group label"]);
  });

  it("flags a five-number summary that is out of order", () => {
    expect(messages(boxplot({ groups: [{ min: 10, q1: 50, median: 45, q3: 60, max: 90 }] }))).toEqual(["boxplot: group 1: min, Q1, median, Q3, max must not decrease"]);
  });

  it("flags values off the axis and an outlier that lies between the whiskers", () => {
    expect(messages(boxplot({ groups: [{ min: 10, q1: 30, median: 45, q3: 60, max: 90, outliers: [120] }] }))).toEqual(["boxplot: group 1: 120 is outside the axis [0, 100]"]);
    expect(messages(boxplot({ groups: [{ min: 10, q1: 30, median: 45, q3: 60, max: 90, outliers: [50] }] }))).toEqual(["boxplot: group 1: outlier 50 lies between the whiskers (10 and 90)"]);
  });

  it("flags an axis step that does not divide the axis", () => {
    expect(messages(boxplot({ axisStep: 30 }))).toEqual(["boxplot: axis step 30 does not divide [0, 100] evenly"]);
  });
});

describe("dotplot", () => {
  it("is accepted and has no problems", () => {
    expect(DiagramSchema.safeParse(dotplot()).success).toBe(true);
    expect(validateDiagram(dotplot())).toEqual([]);
  });

  it("flags a value off the axis and a value given twice", () => {
    expect(messages(dotplot({ dots: [{ x: 9, count: 2 }] }))).toEqual(["dotplot: x=9 is outside the axis [0, 6]"]);
    expect(messages(dotplot({ dots: [{ x: 1, count: 2 }, { x: 1, count: 3 }] }))).toEqual(["dotplot: x=1 appears twice; give one stack its total count"]);
  });

  it("rejects a stack taller than 16, a count of zero or a fraction", () => {
    expect(DiagramSchema.safeParse(dotplot({ dots: [{ x: 1, count: 17 }] })).success).toBe(false);
    expect(DiagramSchema.safeParse(dotplot({ dots: [{ x: 1, count: 0 }] })).success).toBe(false);
    expect(DiagramSchema.safeParse(dotplot({ dots: [{ x: 1, count: 2.5 }] })).success).toBe(false);
  });
});

describe("scatterplot", () => {
  it("is accepted and has no problems, with a line and as a residual plot", () => {
    expect(DiagramSchema.safeParse(scatter()).success).toBe(true);
    expect(validateDiagram(scatter({ line: { intercept: 313, slope: -30 } }))).toEqual([]);
    expect(validateDiagram(scatter({ yMin: -20, yMax: 20, yStep: 10, points: [{ x: 7, y: -5 }, { x: 8, y: 10 }], zeroLine: true }))).toEqual([]);
  });

  it("flags a point outside the axes, naming it", () => {
    expect(messages(scatter({ points: [{ x: 7, y: 120 }, { x: 12, y: 100 }] }))).toEqual(["scatterplot: point 1 has x=12, outside [6, 10]"]);
    expect(messages(scatter({ points: [{ x: 7, y: 150 }, { x: 8, y: 100 }] }))).toEqual(["scatterplot: point 0 has y=150, outside [60, 140]"]);
  });

  it("flags axis steps that do not divide the axes", () => {
    expect(messages(scatter({ xStep: 3 }))).toEqual(["scatterplot: x axis step 3 does not divide [6, 10] evenly"]);
    expect(messages(scatter({ yStep: 30 }))).toEqual(["scatterplot: y axis step 30 does not divide [60, 140] evenly"]);
  });

  it("needs zero inside the y axis for a zero line", () => {
    expect(messages(scatter({ zeroLine: true }))).toEqual(["scatterplot: zeroLine needs 0 to be inside the y axis"]);
  });

  it("flags a highlight that is not a point or is repeated", () => {
    expect(messages(scatter({ highlights: [{ index: 5, label: "A" }] }))).toEqual(["scatterplot: highlight index 5 is not a point"]);
    expect(messages(scatter({ highlights: [{ index: 1, label: "A" }, { index: 1, label: "B" }] }))).toEqual(["scatterplot: point 1 is highlighted twice"]);
  });

  it("rejects fewer than two points, more than 80, and a label that is too long", () => {
    expect(DiagramSchema.safeParse(scatter({ points: [{ x: 7, y: 100 }] })).success).toBe(false);
    expect(DiagramSchema.safeParse(scatter({ points: Array(81).fill({ x: 7, y: 100 }) })).success).toBe(false);
    expect(DiagramSchema.safeParse(scatter({ highlights: [{ index: 0, label: "Outlier!" }] })).success).toBe(false);
  });
});

describe("density-curve", () => {
  it("is accepted and has no problems", () => {
    expect(DiagramSchema.safeParse(curve()).success).toBe(true);
    expect(validateDiagram(curve())).toEqual([]);
  });

  it("flags x values that do not increase and a point below the axis", () => {
    const bad = [...curvePoints];
    bad[10] = { ...bad[10], x: bad[8].x };
    expect(messages(curve({ points: bad }))).toEqual(["density-curve: x must increase (point 10)"]);
    const below = [...curvePoints];
    below[3] = { ...below[3], y: -0.1 };
    expect(messages(curve({ points: below }))).toEqual(["density-curve: point 3 is below the axis"]);
  });

  it("flags a shaded region that is backwards or off the curve, and a tick off the curve", () => {
    expect(messages(curve({ shade: [{ from: 2, to: 1 }] }))).toEqual(["density-curve: shaded region [2, 1] must run from the smaller to the larger value"]);
    expect(messages(curve({ shade: [{ from: 1, to: 5 }] }))).toEqual(["density-curve: shaded region [1, 5] is outside the curve [-4, 4]"]);
    expect(messages(curve({ ticks: [{ x: 6, label: "far" }] }))).toEqual(['density-curve: tick "far" at 6 is outside the curve [-4, 4]']);
  });

  it("rejects too few points, more than two shaded regions, and a long tick label", () => {
    expect(DiagramSchema.safeParse(curve({ points: curvePoints.slice(0, 10) })).success).toBe(false);
    expect(DiagramSchema.safeParse(curve({ shade: [{ from: 0, to: 1 }, { from: 1, to: 2 }, { from: 2, to: 3 }] })).success).toBe(false);
    expect(DiagramSchema.safeParse(curve({ ticks: [{ x: 0, label: "a label that is far too long" }] })).success).toBe(false);
  });
});
