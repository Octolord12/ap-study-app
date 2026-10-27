import { z } from "zod";

// Diagrams are a structured sibling field to markdown stem/prompt content --
// not embedded inline in markdown -- so they stay fully typed/validated and
// never touch the unified/remark/rehype pipeline in render.ts. See CLAUDE.md
// for the word-description-vs-diagram scope boundary.

const PointSchema = z.object({ x: z.number(), y: z.number() });

const GraphSeriesSchema = z.object({
  label: z.string().min(1).optional(),
  points: z.array(PointSchema).min(2), // connected as straight segments -- matches how AP graphs are typically piecewise
  color: z.enum(["blue", "red", "green", "purple"]).default("blue"),
});

export const XYGraphDiagramSchema = z.object({
  type: z.literal("xy-graph"),
  altText: z.string().min(1).optional(),
  xLabel: z.string().min(1),
  yLabel: z.string().min(1),
  xMin: z.number(),
  xMax: z.number(),
  yMin: z.number(),
  yMax: z.number(),
  series: z.array(GraphSeriesSchema).min(1).max(3),
});

const ForceVectorSchema = z.object({
  label: z.string().min(1),
  // standard math convention: 0 = +x (right), 90 = +y (up), counterclockwise
  angleDegrees: z.number().min(-360).max(360),
  magnitude: z.number().positive().max(10), // relative, not physically scaled
  color: z.enum(["blue", "red", "green", "purple", "orange"]).default("red"),
});

export const ForceDiagramSchema = z.object({
  type: z.literal("force-diagram"),
  altText: z.string().min(1).optional(),
  objectLabel: z.string().min(1).optional(),
  inclineAngleDegrees: z.number().min(0).max(89).optional(),
  vectors: z.array(ForceVectorSchema).min(1).max(6),
});

// A table of values: an experiment's results, a Punnett square. Cells are plain text (or numbers), never markdown
// or HTML, so there is nothing to sanitize. Every row must be as long as `columns`; validateDiagram checks that.
export const DataTableDiagramSchema = z.object({
  type: z.literal("data-table"),
  altText: z.string().min(1).optional(),
  caption: z.string().min(1).optional(),
  columns: z.array(z.string()).min(1).max(8), // an empty string is allowed: the corner cell of a Punnett square
  rows: z.array(z.array(z.union([z.string(), z.number()])).min(1).max(8)).min(1).max(20),
  rowHeaders: z.boolean().default(false), // the first cell of each row is its header, not data
});

const BarSeriesSchema = z.object({
  label: z.string().min(1).optional(),
  values: z.array(z.number()).min(2).max(8), // one per category; validateDiagram checks the count
  errors: z.array(z.number().min(0)).min(2).max(8).optional(), // half-length of the error bar (the SE or SD), one per category
  color: z.enum(["blue", "red", "green", "purple"]).default("blue"),
});

export const BarGraphDiagramSchema = z.object({
  type: z.literal("bar-graph"),
  altText: z.string().min(1).optional(),
  xLabel: z.string().min(1),
  yLabel: z.string().min(1),
  yMin: z.number().default(0), // below zero for data such as a percent change in mass
  yMax: z.number(),
  categories: z.array(z.string().min(1).max(24)).min(2).max(8),
  series: z.array(BarSeriesSchema).min(1).max(3),
});

// A tree drawn left to right with every tip lined up on the right. Only tips have labels; `mark` is a short
// marker (a number) drawn on a node for "which number shows..." questions; `trait` labels a tick on the branch
// leading *into* the node (on the stem, for the root), e.g. the derived character that arose there.
// A type alias, not an interface: Prisma's JSON input type only accepts types with an implicit index signature.
export type CladogramNode = {
  label?: string;
  mark?: string;
  trait?: string;
  children?: CladogramNode[];
};

const CladogramNodeSchema: z.ZodType<CladogramNode> = z.lazy(() =>
  z.object({
    label: z.string().min(1).max(28).optional(),
    mark: z.string().min(1).max(3).optional(),
    trait: z.string().min(1).max(18).optional(),
    children: z.array(CladogramNodeSchema).min(2).max(6).optional(),
  }),
);

export const CladogramDiagramSchema = z.object({
  type: z.literal("cladogram"),
  altText: z.string().min(1).optional(),
  root: CladogramNodeSchema,
});

// The statistics graphs. Axis ranges and steps are written out (not worked out from the data) so a graph shows
// exactly the scale a question needs; validateDiagram checks that the data fit the axis and the step divides it.

const AxisSchema = {
  axisMin: z.number(),
  axisMax: z.number(),
  axisStep: z.number().positive(),
};

// Bars side by side with no gaps: `edges` has one more entry than `values`. Labels go under the edges (a measured
// variable) or under the middle of each bar (a variable that takes whole values, such as a count of successes).
export const HistogramDiagramSchema = z.object({
  type: z.literal("histogram"),
  altText: z.string().min(1).optional(),
  xLabel: z.string().min(1),
  yLabel: z.string().min(1).default("Frequency"),
  edges: z.array(z.number()).min(3).max(26),
  values: z.array(z.number().min(0)).min(2).max(25),
  yMax: z.number().positive(),
  yStep: z.number().positive(),
  tickAt: z.enum(["edges", "centers"]).default("edges"),
  labelEvery: z.number().int().min(1).max(10).default(1), // label every nth edge when there are many bins
});

const BoxplotGroupSchema = z.object({
  label: z.string().min(1).max(40).optional(), // required when there are several groups
  min: z.number(), // the lower whisker: the smallest value that is not an outlier
  q1: z.number(),
  median: z.number(),
  q3: z.number(),
  max: z.number(), // the upper whisker
  outliers: z.array(z.number()).max(12).optional(),
});

export const BoxplotDiagramSchema = z.object({
  type: z.literal("boxplot"),
  altText: z.string().min(1).optional(),
  xLabel: z.string().min(1),
  ...AxisSchema,
  groups: z.array(BoxplotGroupSchema).min(1).max(4),
});

// `count` dots stacked above `x`.
export const DotplotDiagramSchema = z.object({
  type: z.literal("dotplot"),
  altText: z.string().min(1).optional(),
  xLabel: z.string().min(1),
  ...AxisSchema,
  dots: z.array(z.object({ x: z.number(), count: z.number().int().min(1).max(16) })).min(1).max(60),
});

const ScatterPointSchema = z.object({ x: z.number(), y: z.number() });

// Points, optionally with the least-squares line drawn through the plot, and a dashed line at zero for a residual plot.
export const ScatterplotDiagramSchema = z.object({
  type: z.literal("scatterplot"),
  altText: z.string().min(1).optional(),
  xLabel: z.string().min(1),
  yLabel: z.string().min(1),
  xMin: z.number(),
  xMax: z.number(),
  xStep: z.number().positive(),
  yMin: z.number(),
  yMax: z.number(),
  yStep: z.number().positive(),
  points: z.array(ScatterPointSchema).min(2).max(80),
  line: z.object({ intercept: z.number(), slope: z.number() }).optional(),
  zeroLine: z.boolean().default(false),
  highlights: z.array(z.object({ index: z.number().int().min(0), label: z.string().min(1).max(6) })).max(4).optional(),
});

// A smooth curve given as points (worked out when the content is written, with scipy), with regions shaded under it
// and labelled values on the axis: a normal, t or chi-square curve for a probability, a critical value or a p-value.
export const DensityCurveDiagramSchema = z.object({
  type: z.literal("density-curve"),
  altText: z.string().min(1).optional(),
  xLabel: z.string().min(1).optional(),
  points: z.array(ScatterPointSchema).min(20).max(400),
  shade: z.array(z.object({ from: z.number(), to: z.number() })).max(2).optional(),
  ticks: z.array(z.object({ x: z.number(), label: z.string().min(1).max(14) })).max(8),
});

export const DiagramSchema = z.discriminatedUnion("type", [
  XYGraphDiagramSchema,
  ForceDiagramSchema,
  DataTableDiagramSchema,
  BarGraphDiagramSchema,
  CladogramDiagramSchema,
  HistogramDiagramSchema,
  BoxplotDiagramSchema,
  DotplotDiagramSchema,
  ScatterplotDiagramSchema,
  DensityCurveDiagramSchema,
]);

export type GraphSeries = z.infer<typeof GraphSeriesSchema>;
export type XYGraphDiagram = z.infer<typeof XYGraphDiagramSchema>;
export type ForceVector = z.infer<typeof ForceVectorSchema>;
export type ForceDiagram = z.infer<typeof ForceDiagramSchema>;
export type DataTableDiagram = z.infer<typeof DataTableDiagramSchema>;
export type BarSeries = z.infer<typeof BarSeriesSchema>;
export type BarGraphDiagram = z.infer<typeof BarGraphDiagramSchema>;
export type CladogramDiagram = z.infer<typeof CladogramDiagramSchema>;
export type HistogramDiagram = z.infer<typeof HistogramDiagramSchema>;
export type BoxplotGroup = z.infer<typeof BoxplotGroupSchema>;
export type BoxplotDiagram = z.infer<typeof BoxplotDiagramSchema>;
export type DotplotDiagram = z.infer<typeof DotplotDiagramSchema>;
export type ScatterplotDiagram = z.infer<typeof ScatterplotDiagramSchema>;
export type DensityCurveDiagram = z.infer<typeof DensityCurveDiagramSchema>;
export type Diagram = z.infer<typeof DiagramSchema>;
