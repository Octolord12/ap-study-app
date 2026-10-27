// Text equivalents of the three data diagrams, used as their accessible names unless the content supplies an
// `altText`. They are built from the same data the picture is, so the two cannot disagree.
import type {
  BarGraphDiagram,
  BoxplotDiagram,
  CladogramDiagram,
  CladogramNode,
  DataTableDiagram,
  DensityCurveDiagram,
  DotplotDiagram,
  HistogramDiagram,
  ScatterplotDiagram,
} from "@/lib/content/diagram-schema";
import { compactNumber } from "./axis";
import { tipLabels } from "./cladogram-layout";

const join = (items: string[]) => items.join("; ");

export function describeDataTable(diagram: DataTableDiagram): string {
  const lead = diagram.caption ? `${diagram.caption}. ` : "";
  const columns = diagram.columns.filter((c) => c !== "").join(", ");
  return `${lead}Table with ${diagram.rows.length} row${diagram.rows.length === 1 ? "" : "s"} and the columns ${columns}.`;
}

export function describeBarGraph(diagram: BarGraphDiagram): string {
  const several = diagram.series.length > 1;
  const parts = diagram.series.map((s, si) => {
    const bars = diagram.categories.map((c, ci) => {
      const err = s.errors?.[ci];
      return `${c} ${s.values[ci]}${err !== undefined && err > 0 ? ` plus or minus ${err}` : ""}`;
    });
    return `${several ? `${s.label ?? `Series ${si + 1}`}: ` : ""}${bars.join(", ")}`;
  });
  return `Bar graph of ${diagram.yLabel} by ${diagram.xLabel}. ${join(parts)}.`;
}

// (A, (B, C)): each pair of parentheses is a group that shares a common ancestor.
export function nestedGroups(node: CladogramNode): string {
  return node.children?.length ? `(${node.children.map(nestedGroups).join(", ")})` : (node.label ?? "");
}

function walk(node: CladogramNode, visit: (n: CladogramNode) => void) {
  visit(node);
  node.children?.forEach((c) => walk(c, visit));
}

export function describeCladogram(diagram: CladogramDiagram): string {
  const marks: string[] = [];
  const traits: string[] = [];
  walk(diagram.root, (n) => {
    const where = n.children?.length ? `the common ancestor of ${tipLabels(n).join(", ")}` : `the tip ${n.label}`;
    if (n.mark) marks.push(`point ${n.mark} is ${where}`);
    if (n.trait) traits.push(`"${n.trait}" arises on the branch leading to ${nestedGroups(n)}`);
  });
  const extra = [marks.length ? `Marked: ${marks.join(", ")}.` : "", traits.length ? `Characters: ${traits.join(", ")}.` : ""].filter(Boolean).join(" ");
  return `Cladogram, written as nested groups: ${nestedGroups(diagram.root)}. ${extra}`.trim();
}

export function describeHistogram(d: HistogramDiagram): string {
  const bars = d.values.map((v, i) => `${compactNumber(d.edges[i])} to ${compactNumber(d.edges[i + 1])}: ${compactNumber(v)}`);
  return `Histogram of ${d.xLabel}. ${d.yLabel} by interval: ${join(bars)}.`;
}

export function describeBoxplot(d: BoxplotDiagram): string {
  const parts = d.groups.map((g) => {
    const five = `minimum ${compactNumber(g.min)}, Q1 ${compactNumber(g.q1)}, median ${compactNumber(g.median)}, Q3 ${compactNumber(g.q3)}, maximum ${compactNumber(g.max)}`;
    const out = g.outliers?.length ? `, outliers at ${g.outliers.map(compactNumber).join(", ")}` : "";
    return `${g.label ? `${g.label}: ` : ""}${five}${out}`;
  });
  return `Boxplot${d.groups.length > 1 ? "s" : ""} of ${d.xLabel}. ${join(parts)}.`;
}

export function describeDotplot(d: DotplotDiagram): string {
  const stacks = [...d.dots].sort((a, b) => a.x - b.x).map((dot) => `${compactNumber(dot.x)} (${dot.count})`);
  return `Dotplot of ${d.xLabel}, with the number of dots at each value: ${stacks.join(", ")}.`;
}

export function describeScatterplot(d: ScatterplotDiagram): string {
  const points = d.points.map((p) => `(${compactNumber(p.x)}, ${compactNumber(p.y)})`);
  const line = d.line ? ` The least-squares line y = ${compactNumber(d.line.intercept)} ${d.line.slope < 0 ? "-" : "+"} ${compactNumber(Math.abs(d.line.slope))}x is drawn.` : "";
  const zero = d.zeroLine ? " A dashed line marks zero." : "";
  return `${d.zeroLine ? "Residual plot" : "Scatterplot"} of ${d.yLabel} against ${d.xLabel}, ${d.points.length} points: ${points.join(", ")}.${line}${zero}`;
}

export function describeDensityCurve(d: DensityCurveDiagram): string {
  const shade = d.shade?.length ? ` Shaded: ${d.shade.map((s) => `from ${compactNumber(s.from)} to ${compactNumber(s.to)}`).join(" and ")}.` : "";
  const marks = d.ticks.length ? ` Marked on the axis: ${d.ticks.map((t) => `${t.label} at ${compactNumber(t.x)}`).join(", ")}.` : "";
  return `Density curve${d.xLabel ? ` of ${d.xLabel}` : ""}.${shade}${marks}`;
}
