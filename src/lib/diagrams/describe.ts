// Text equivalents of the three data diagrams, used as their accessible names unless the content supplies an
// `altText`. They are built from the same data the picture is, so the two cannot disagree.
import type { BarGraphDiagram, CladogramDiagram, CladogramNode, DataTableDiagram } from "@/lib/content/diagram-schema";
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
