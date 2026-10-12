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

export const DiagramSchema = z.discriminatedUnion("type", [
  XYGraphDiagramSchema,
  ForceDiagramSchema,
  DataTableDiagramSchema,
  BarGraphDiagramSchema,
  CladogramDiagramSchema,
]);

export type GraphSeries = z.infer<typeof GraphSeriesSchema>;
export type XYGraphDiagram = z.infer<typeof XYGraphDiagramSchema>;
export type ForceVector = z.infer<typeof ForceVectorSchema>;
export type ForceDiagram = z.infer<typeof ForceDiagramSchema>;
export type DataTableDiagram = z.infer<typeof DataTableDiagramSchema>;
export type BarSeries = z.infer<typeof BarSeriesSchema>;
export type BarGraphDiagram = z.infer<typeof BarGraphDiagramSchema>;
export type CladogramDiagram = z.infer<typeof CladogramDiagramSchema>;
export type Diagram = z.infer<typeof DiagramSchema>;
