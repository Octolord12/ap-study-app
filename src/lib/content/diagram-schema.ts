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

export const DiagramSchema = z.discriminatedUnion("type", [XYGraphDiagramSchema, ForceDiagramSchema]);

export type GraphSeries = z.infer<typeof GraphSeriesSchema>;
export type XYGraphDiagram = z.infer<typeof XYGraphDiagramSchema>;
export type ForceVector = z.infer<typeof ForceVectorSchema>;
export type ForceDiagram = z.infer<typeof ForceDiagramSchema>;
export type Diagram = z.infer<typeof DiagramSchema>;
