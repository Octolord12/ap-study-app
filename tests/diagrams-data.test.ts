import { describe, expect, it } from "vitest";
import { DiagramSchema, type BarGraphDiagram, type CladogramDiagram, type CladogramNode, type DataTableDiagram } from "@/lib/content/diagram-schema";
import { validateDiagram } from "@/lib/content/validate";

const table = (o: Partial<DataTableDiagram> = {}): DataTableDiagram => ({
  type: "data-table",
  columns: ["Treatment", "Mean mass (g)"],
  rows: [["Control", 12.1], ["Fertilizer", 15.4]],
  rowHeaders: false,
  ...o,
});

const bars = (o: Partial<BarGraphDiagram> = {}): BarGraphDiagram => ({
  type: "bar-graph",
  xLabel: "Treatment",
  yLabel: "Mean mass (g)",
  yMin: 0,
  yMax: 20,
  categories: ["Control", "Fertilizer", "Shade"],
  series: [{ values: [12, 15, 8], errors: [1, 1.5, 0.5], color: "blue" }],
  ...o,
});

const tip = (label: string, extra: Partial<CladogramNode> = {}): CladogramNode => ({ label, ...extra });
const tree = (root: CladogramNode): CladogramDiagram => ({ type: "cladogram", root });
const simple = tree({ children: [tip("Annelida"), { children: [tip("Chiton"), tip("Clam")] }] });

describe("data-table", () => {
  it("is accepted by the schema and has no problems when every row is as long as the columns", () => {
    expect(DiagramSchema.safeParse(table()).success).toBe(true);
    expect(validateDiagram(table())).toEqual([]);
  });

  it("allows an empty header cell, for the corner of a Punnett square", () => {
    const punnett = table({ columns: ["", "R", "r"], rows: [["R", "RR", "Rr"], ["r", "Rr", "rr"]], rowHeaders: true });
    expect(DiagramSchema.safeParse(punnett).success).toBe(true);
    expect(validateDiagram(punnett)).toEqual([]);
  });

  it("flags a row with the wrong number of cells, naming the row", () => {
    const problems = validateDiagram(table({ rows: [["Control", 12.1], ["Fertilizer"]] }));
    expect(problems).toHaveLength(1);
    expect(problems[0].message).toMatch(/row 2 has 1 cell\(s\) but there are 2 column/);
  });

  it("rejects a table with no rows, no columns, or too many of either", () => {
    expect(DiagramSchema.safeParse(table({ rows: [] })).success).toBe(false);
    expect(DiagramSchema.safeParse(table({ columns: [] })).success).toBe(false);
    expect(DiagramSchema.safeParse(table({ columns: Array(9).fill("c") })).success).toBe(false);
    expect(DiagramSchema.safeParse(table({ rows: Array(21).fill(["a", 1]) })).success).toBe(false);
  });
});

describe("bar-graph", () => {
  it("accepts a well-formed graph, including a series with no error bars", () => {
    expect(validateDiagram(bars())).toEqual([]);
    expect(validateDiagram(bars({ series: [{ values: [1, 2, 3], color: "red" }] }))).toEqual([]);
  });

  it("accepts negative values when the axis goes below zero (a percent change in mass)", () => {
    const negative = bars({ yMin: -20, yMax: 20, series: [{ values: [-12, 3, 9], errors: [2, 2, 2], color: "blue" }] });
    expect(DiagramSchema.safeParse(negative).success).toBe(true);
    expect(validateDiagram(negative)).toEqual([]);
  });

  it("flags a series with the wrong number of values or error values", () => {
    expect(validateDiagram(bars({ series: [{ values: [1, 2], color: "blue" }] }))[0].message).toMatch(/2 value\(s\) for 3 categories/);
    expect(validateDiagram(bars({ series: [{ values: [1, 2, 3], errors: [1, 1], color: "blue" }] }))[0].message).toMatch(/2 error value\(s\) for 3 categories/);
  });

  it("flags a bar, or its error bar, that does not fit on the axis", () => {
    expect(validateDiagram(bars({ series: [{ values: [12, 25, 8], color: "blue" }] }))[0].message).toMatch(/Fertilizer: 25 does not fit/);
    expect(validateDiagram(bars({ series: [{ values: [12, 19, 8], errors: [1, 2, 1], color: "blue" }] }))[0].message).toMatch(/19 ± 2 does not fit/);
  });

  it("needs a label on every series once there is more than one (the legend names them)", () => {
    const two = bars({ series: [{ label: "2022", values: [1, 2, 3], color: "blue" }, { values: [2, 3, 4], color: "red" }] });
    expect(validateDiagram(two).map((p) => p.message)).toEqual(["bar-graph: series 2 needs a label (the legend names them)"]);
  });

  it("flags an empty axis range and duplicate category names", () => {
    expect(validateDiagram(bars({ yMin: 5, yMax: 5, series: [{ values: [5, 5, 5], color: "blue" }] })).some((p) => /yMax/.test(p.message))).toBe(true);
    expect(validateDiagram(bars({ categories: ["A", "A", "B"] })).some((p) => /duplicate category/.test(p.message))).toBe(true);
  });

  it("rejects a negative error, one category, and more than three series at the schema", () => {
    expect(DiagramSchema.safeParse(bars({ series: [{ values: [1, 2, 3], errors: [-1, 1, 1], color: "blue" }] })).success).toBe(false);
    expect(DiagramSchema.safeParse(bars({ categories: ["A"] })).success).toBe(false);
    const four = Array.from({ length: 4 }, (_, i) => ({ label: `s${i}`, values: [1, 2, 3], color: "blue" as const }));
    expect(DiagramSchema.safeParse(bars({ series: four })).success).toBe(false);
  });
});

describe("cladogram", () => {
  it("accepts a well-formed tree, with marks and traits", () => {
    expect(DiagramSchema.safeParse(simple).success).toBe(true);
    expect(validateDiagram(simple)).toEqual([]);
    const marked = tree({ trait: "root", children: [tip("A", { mark: "1" }), { mark: "2", trait: "mantle", children: [tip("B"), tip("C")] }] });
    expect(DiagramSchema.safeParse(marked).success).toBe(true);
    expect(validateDiagram(marked)).toEqual([]);
  });

  it("rejects a branching point with one child at the schema (a tree has no unary nodes)", () => {
    expect(DiagramSchema.safeParse(tree({ children: [tip("A")] })).success).toBe(false);
  });

  it("flags a root with no branches, a tip with no label, and a labelled branching point", () => {
    expect(validateDiagram(tree(tip("A"))).some((p) => /root needs branches/.test(p.message))).toBe(true);
    expect(validateDiagram(tree({ children: [tip("A"), {}] })).some((p) => /tip has no label/.test(p.message))).toBe(true);
    expect(validateDiagram(tree({ children: [tip("A"), { label: "Clade", children: [tip("B"), tip("C")] }] })).some((p) => /only tips have labels/.test(p.message))).toBe(true);
  });

  it("flags too many tips, too deep a tree, and duplicate tip labels or marks", () => {
    const many = tree({ children: Array.from({ length: 13 }, (_, i) => tip(`T${i}`)).reduce<CladogramNode[][]>((groups, t, i) => { (groups[Math.floor(i / 5)] ??= []).push(t); return groups; }, []).map((g) => (g.length > 1 ? { children: g } : g[0])) });
    expect(validateDiagram(many).some((p) => /13 tips/.test(p.message))).toBe(true);

    let deep: CladogramNode = { children: [tip("a"), tip("b")] };
    for (let i = 0; i < 6; i++) deep = { children: [deep, tip(`x${i}`)] };
    expect(validateDiagram(tree(deep)).some((p) => /7 levels deep/.test(p.message))).toBe(true);

    expect(validateDiagram(tree({ children: [tip("A"), tip("A")] })).some((p) => /same label/.test(p.message))).toBe(true);
    expect(validateDiagram(tree({ children: [tip("A", { mark: "1" }), tip("B", { mark: "1" })] })).some((p) => /same mark/.test(p.message))).toBe(true);
  });
});
