import { describe, expect, it } from "vitest";
import type { BarGraphDiagram, CladogramDiagram, CladogramNode, DataTableDiagram } from "@/lib/content/diagram-schema";
import { GROUP_FRACTION, layoutBars, shouldRotateLabels, yPixel } from "@/lib/diagrams/bar-layout";
import { CLADOGRAM_CHAR_WIDTH, CLADOGRAM_DIMS, CLADOGRAM_LEVEL_WIDTH, layoutCladogram, tipCount, tipLabels, treeDepth } from "@/lib/diagrams/cladogram-layout";
import { describeBarGraph, describeCladogram, describeDataTable, nestedGroups } from "@/lib/diagrams/describe";
import { axisTicks, formatTick, type PixelDims } from "@/lib/diagrams/geometry";
import { layoutLegend, LEGEND_ROW_HEIGHT, legendLabels } from "@/lib/diagrams/legend";

const DIMS: PixelDims = { width: 420, height: 300, marginLeft: 50, marginRight: 20, marginTop: 20, marginBottom: 50 };
// plot area: x 50..400 (350 wide), y 20..250 (230 tall)

describe("bar layout", () => {
  it("maps values to pixels: yMin at the bottom of the plot, yMax at the top", () => {
    expect(yPixel(0, 0, 20, DIMS)).toBe(250);
    expect(yPixel(20, 0, 20, DIMS)).toBe(20);
    expect(yPixel(10, 0, 20, DIMS)).toBe(135);
  });

  it("draws each bar from the zero line up to its value", () => {
    const { bars, baselineY } = layoutBars([{ values: [10, 20] }], 2, 0, 20, DIMS);
    expect(baselineY).toBe(250);
    expect(bars[0]).toMatchObject({ y: 135, height: 115, value: 10 });
    expect(bars[1]).toMatchObject({ y: 20, height: 230 });
  });

  it("draws a negative bar down from a zero line that is inside the plot", () => {
    const { bars, baselineY } = layoutBars([{ values: [-10, 10] }], 2, -20, 20, DIMS);
    expect(baselineY).toBe(135);
    expect(bars[0]).toMatchObject({ y: 135, height: 57.5 });
    expect(bars[1]).toMatchObject({ y: 77.5, height: 57.5 });
  });

  it("centers each category's group in its slot and splits the group between series", () => {
    const { bars, categoryCenters } = layoutBars([{ values: [1, 1] }, { values: [1, 1] }], 2, 0, 2, DIMS);
    const slot = 350 / 2;
    expect(categoryCenters).toEqual([50 + slot / 2, 50 + slot * 1.5]);
    const first = bars.filter((b) => b.category === 0);
    expect(first[0].width).toBeCloseTo((slot * GROUP_FRACTION) / 2);
    expect(first[1].x).toBeCloseTo(first[0].x + first[0].width);
    expect((first[0].x + first[1].x + first[1].width) / 2).toBeCloseTo(categoryCenters[0]);
  });

  it("puts error bars on the centre of their bar, value minus and plus the error, and skips zero or missing ones", () => {
    const { bars, errorBars } = layoutBars([{ values: [10, 10, 10], errors: [2, 0, undefined as unknown as number] }], 3, 0, 20, DIMS);
    expect(errorBars).toHaveLength(1);
    const e = errorBars[0];
    expect(e.x).toBeCloseTo(bars[0].x + bars[0].width / 2);
    expect(e.yTop).toBeCloseTo(yPixel(12, 0, 20, DIMS));
    expect(e.yBottom).toBeCloseTo(yPixel(8, 0, 20, DIMS));
    expect(e.capHalfWidth).toBeGreaterThan(0);
  });

  it("tilts the category names only when the longest would run into its neighbours", () => {
    expect(shouldRotateLabels(["Control", "Shade"], 80)).toBe(false);
    expect(shouldRotateLabels(["Control", "Fertilizer + shade"], 40)).toBe(true);
    expect(shouldRotateLabels(["Control", "Fertilizer + shade"], 200)).toBe(false);
  });
});

const tip = (label: string, extra: Partial<CladogramNode> = {}): CladogramNode => ({ label, ...extra });

describe("cladogram layout", () => {
  const root: CladogramNode = { children: [tip("A"), { children: [tip("B"), { children: [tip("C"), tip("D")] }] }] };

  it("counts tips and levels, and lists tips top to bottom", () => {
    expect(tipCount(root)).toBe(4);
    expect(treeDepth(root)).toBe(3);
    expect(tipLabels(root)).toEqual(["A", "B", "C", "D"]);
  });

  it("draws a deep tree wide enough that every level has room for a trait label, and leaves a shallow tree at the minimum width", () => {
    const ladder: CladogramNode = { children: [tip("A"), { mark: "1", children: [tip("B"), { mark: "2", children: [tip("C"), { mark: "3", children: [tip("D"), { mark: "4", children: [tip("E"), tip("F")] }] }] }] }] };
    expect(treeDepth(ladder)).toBe(5);
    const { nodes } = layoutCladogram(ladder);
    const xs = [...new Set(nodes.filter((n) => !n.isTip).map((n) => n.x))].sort((a, b) => a - b);
    for (let i = 1; i < xs.length; i++) expect(xs[i] - xs[i - 1]).toBeGreaterThanOrEqual(CLADOGRAM_LEVEL_WIDTH);
    const shallow = layoutCladogram(root).nodes.filter((n) => n.isTip)[0].x;
    expect(shallow).toBe(CLADOGRAM_DIMS.stem + CLADOGRAM_DIMS.treeWidth);
  });

  it("sizes the room for the tip names to the longest name, up to the most that is allowed", () => {
    const short = layoutCladogram({ children: [tip("Cat"), tip("Dog")] });
    const medium = layoutCladogram({ children: [tip("Salamander"), tip("Dog")] });
    const long = layoutCladogram({ children: [tip("A name that is much too long for the room"), tip("Dog")] });
    const tipX = CLADOGRAM_DIMS.stem + CLADOGRAM_DIMS.treeWidth;
    expect(medium.width - tipX).toBe(Math.ceil(10 * CLADOGRAM_CHAR_WIDTH) + 24);
    expect(short.width).toBeLessThan(medium.width);
    expect(long.width - tipX).toBe(CLADOGRAM_DIMS.labelRoom);
  });

  it("gives every tip its own row, evenly spaced from the top, all at the right edge", () => {
    const { nodes } = layoutCladogram(root);
    const tips = nodes.filter((n) => n.isTip);
    expect(tips.map((n) => n.label)).toEqual(["A", "B", "C", "D"]);
    expect(tips.map((n) => n.y)).toEqual([0, 1, 2, 3].map((i) => CLADOGRAM_DIMS.marginTop + i * CLADOGRAM_DIMS.rowHeight));
    expect(new Set(tips.map((n) => n.x))).toEqual(new Set([CLADOGRAM_DIMS.stem + CLADOGRAM_DIMS.treeWidth]));
  });

  it("puts a branching point halfway between its first and last child, and at its depth along the tree", () => {
    const { nodes, connectors } = layoutCladogram(root);
    const internal = nodes.filter((n) => !n.isTip);
    const rootNode = internal.find((n) => n.branchFromX === 0)!;
    expect(rootNode.x).toBe(CLADOGRAM_DIMS.stem);
    const cd = internal.find((n) => n.y === CLADOGRAM_DIMS.marginTop + 2.5 * CLADOGRAM_DIMS.rowHeight)!;
    expect(cd.x).toBeCloseTo(CLADOGRAM_DIMS.stem + (2 / 3) * CLADOGRAM_DIMS.treeWidth);
    expect(connectors).toHaveLength(3);
    // rows: A 0, B 1, C 2, D 3. (C, D) sits at 2.5; (B, (C, D)) at 1.75; the root halfway between A (0) and that, 0.875.
    const row = (r: number) => CLADOGRAM_DIMS.marginTop + r * CLADOGRAM_DIMS.rowHeight;
    expect(rootNode.y).toBeCloseTo(row(0.875));
    const rootConnector = connectors.find((c) => c.x === CLADOGRAM_DIMS.stem)!;
    expect(rootConnector.yTop).toBe(row(0));
    expect(rootConnector.yBottom).toBeCloseTo(row(1.75));
  });

  it("starts each branch at its parent, and a tip's branch can be long when the tip is shallow", () => {
    const { nodes } = layoutCladogram(root);
    const a = nodes.find((n) => n.label === "A")!;
    expect(a.branchFromX).toBe(CLADOGRAM_DIMS.stem);
    expect(a.x - a.branchFromX).toBe(CLADOGRAM_DIMS.treeWidth);
  });

  it("carries marks and traits through, and sizes the picture to the tips", () => {
    const marked = layoutCladogram({ children: [tip("A", { mark: "1" }), { trait: "mantle", mark: "2", children: [tip("B"), tip("C")] }] });
    expect(marked.nodes.filter((n) => n.mark).map((n) => n.mark).sort()).toEqual(["1", "2"]);
    expect(marked.nodes.find((n) => n.trait)!.trait).toBe("mantle");
    expect(marked.height).toBe(CLADOGRAM_DIMS.marginTop + 2 * CLADOGRAM_DIMS.rowHeight + CLADOGRAM_DIMS.marginBottom + 14);
  });
});

describe("text equivalents", () => {
  const bar: BarGraphDiagram = { type: "bar-graph", xLabel: "Treatment", yLabel: "Mean mass (g)", yMin: 0, yMax: 20, categories: ["Control", "Shade"], series: [{ values: [12, 8], errors: [1, 0], color: "blue" }] };
  it("describes a bar graph from its own numbers, with the error only where there is one", () => {
    expect(describeBarGraph(bar)).toBe("Bar graph of Mean mass (g) by Treatment. Control 12 plus or minus 1, Shade 8.");
  });
  it("names each series when there are several", () => {
    const two: BarGraphDiagram = { ...bar, series: [{ label: "2022", values: [12, 8], color: "blue" }, { label: "2023", values: [14, 9], color: "red" }] };
    expect(describeBarGraph(two)).toBe("Bar graph of Mean mass (g) by Treatment. 2022: Control 12, Shade 8; 2023: Control 14, Shade 9.");
  });
  it("describes a table by its caption, size and columns, leaving out an empty corner header", () => {
    const t: DataTableDiagram = { type: "data-table", caption: "Results", columns: ["", "R", "r"], rows: [["R", "RR", "Rr"], ["r", "Rr", "rr"]], rowHeaders: true };
    expect(describeDataTable(t)).toBe("Results. Table with 2 rows and the columns R, r.");
  });
  it("writes a tree as nested groups, and lists marked points and characters", () => {
    const c: CladogramDiagram = { type: "cladogram", root: { children: [tip("Annelida"), { mark: "2", trait: "mantle", children: [tip("Chiton"), tip("Clam")] }] } };
    expect(nestedGroups(c.root)).toBe("(Annelida, (Chiton, Clam))");
    expect(describeCladogram(c)).toBe('Cladogram, written as nested groups: (Annelida, (Chiton, Clam)). Marked: point 2 is the common ancestor of Chiton, Clam. Characters: "mantle" arises on the branch leading to (Chiton, Clam).');
  });
});

describe("axis helpers (shared by the line and bar graphs)", () => {
  it("makes evenly spaced ticks including both ends", () => {
    expect(axisTicks(0, 20, 5)).toEqual([0, 5, 10, 15, 20]);
    expect(axisTicks(-1, 1, 3)).toEqual([-1, 0, 1]);
  });
  it("writes whole numbers plainly and others to one decimal", () => {
    expect(formatTick(5)).toBe("5");
    expect(formatTick(2.5)).toBe("2.5");
  });
});

describe("legend layout", () => {
  it("puts labels in one row, left to right, when they fit, and leaves room for that row above the plot", () => {
    const { items, rows, height } = layoutLegend(["Control", "Treated"], 400);
    expect(rows).toBe(1);
    expect(items.map((i) => i.row)).toEqual([0, 0]);
    expect(items[0].x).toBe(0);
    expect(items[1].x).toBeGreaterThan(items[0].x + 18 + "Control".length * 6);
    expect(height).toBe(LEGEND_ROW_HEIGHT + 8);
  });

  it("wraps to the next row, from the left edge, when the next label would run past the width", () => {
    const { items, rows, height } = layoutLegend(["Human enzyme", "Hot-spring bacterial enzyme", "Fungal enzyme"], 250);
    expect(items[0]).toEqual({ x: 0, row: 0 });
    expect(items[1].row).toBe(1);
    expect(items[1].x).toBe(0);
    expect(rows).toBe(items[items.length - 1].row + 1);
    expect(height).toBe(rows * LEGEND_ROW_HEIGHT + 8);
  });

  it("never wraps a lone first label, however long, and takes no room for no labels", () => {
    expect(layoutLegend(["A very long series label that is wider than the plot"], 40).rows).toBe(1);
    expect(layoutLegend([], 400)).toEqual({ items: [], rows: 0, height: 0 });
  });

  it("shows a legend only when it tells series apart: more than one series and at least one name", () => {
    expect(legendLabels([{ label: "Only one" }])).toEqual([]);
    expect(legendLabels([{}, {}])).toEqual([]);
    expect(legendLabels([{ label: "2022" }, { label: "2023" }])).toEqual(["2022", "2023"]);
    expect(legendLabels([{ label: "2022" }, {}])).toEqual(["2022", "Series 2"]);
  });
});
