import { render, screen, within } from "@testing-library/react";
import { describe, expect, it } from "vitest";
import { DiagramRenderer } from "@/components/diagrams/diagram-renderer";
import type { BarGraphDiagram, CladogramDiagram, DataTableDiagram, Diagram } from "@/lib/content/diagram-schema";

const table: DataTableDiagram = {
  type: "data-table",
  caption: "Mass of potato cores after 24 hours",
  columns: ["Solution (M sucrose)", "Change in mass (%)"],
  rows: [["0.0", -2], ["0.4", 8.5], ["0.8", 21]],
  rowHeaders: false,
};

const bar: BarGraphDiagram = {
  type: "bar-graph",
  xLabel: "Treatment",
  yLabel: "Mean mass (g)",
  yMin: 0,
  yMax: 20,
  categories: ["Control", "Fertilizer", "Shade"],
  series: [{ values: [12, 15, 8], errors: [1, 1.5, 0], color: "blue" }],
};

const clade: CladogramDiagram = {
  type: "cladogram",
  root: { children: [{ label: "Annelida", mark: "1" }, { trait: "mantle", mark: "2", children: [{ label: "Chiton" }, { label: "Clam" }] }] },
};

describe("data-table", () => {
  it("renders a real table: caption, column headers with scope, and one row per row of data", () => {
    render(<DiagramRenderer diagram={table} />);
    expect(screen.getByRole("table")).toBeInTheDocument();
    expect(screen.getByText("Mass of potato cores after 24 hours")).toBeInTheDocument();
    const headers = screen.getAllByRole("columnheader");
    expect(headers.map((h) => h.textContent)).toEqual(["Solution (M sucrose)", "Change in mass (%)"]);
    headers.forEach((h) => expect(h).toHaveAttribute("scope", "col"));
    expect(screen.getAllByRole("row")).toHaveLength(4);
    expect(screen.getByText("8.5")).toBeInTheDocument();
    expect(screen.getByText("-2")).toBeInTheDocument();
  });

  it("makes the first cell of each row a row header when asked (a Punnett square)", () => {
    render(<DiagramRenderer diagram={{ ...table, columns: ["", "R", "r"], rows: [["R", "RR", "Rr"], ["r", "Rr", "rr"]], rowHeaders: true }} />);
    const rowHeaders = screen.getAllByRole("rowheader");
    expect(rowHeaders.map((h) => h.textContent)).toEqual(["R", "r"]);
    rowHeaders.forEach((h) => expect(h).toHaveAttribute("scope", "row"));
  });

  it("scrolls inside its own labelled, focusable region instead of widening the page", () => {
    render(<DiagramRenderer diagram={table} />);
    const region = screen.getByRole("region");
    expect(region).toHaveAttribute("tabindex", "0");
    expect(region).toHaveClass("overflow-x-auto");
    expect(region).toHaveAccessibleName(/Table with 3 rows/);
    expect(within(region).getByRole("table")).toBeInTheDocument();
  });

  it("shows cell text as text: markup in a cell is not turned into elements", () => {
    const hostile = '<img src=x onerror="alert(1)"><script>alert(2)</script>';
    const { container } = render(<DiagramRenderer diagram={{ ...table, rows: [[hostile, 1]] }} />);
    expect(container.querySelector("img, script")).toBeNull();
    expect(screen.getByText(hostile)).toBeInTheDocument();
  });

  it("still draws a short row (content that failed validation) instead of crashing", () => {
    render(<DiagramRenderer diagram={{ ...table, rows: [["only one cell"]] }} />);
    expect(screen.getAllByRole("cell")).toHaveLength(2);
  });
});

describe("bar-graph", () => {
  it("is one image with a text equivalent built from its data", () => {
    render(<DiagramRenderer diagram={bar} />);
    expect(screen.getByRole("img")).toHaveAccessibleName("Bar graph of Mean mass (g) by Treatment. Control 12 plus or minus 1, Fertilizer 15 plus or minus 1.5, Shade 8.");
  });

  it("uses the content's own alt text when it has one", () => {
    render(<DiagramRenderer diagram={{ ...bar, altText: "Fertilized plants were heaviest" }} />);
    expect(screen.getByRole("img")).toHaveAccessibleName("Fertilized plants were heaviest");
  });

  it("draws one bar per value and error bars only where the error is above zero", () => {
    const { container } = render(<DiagramRenderer diagram={bar} />);
    expect(container.querySelectorAll("rect")).toHaveLength(3);
    // two error bars (the third has error 0), each a stem and two caps
    expect(container.querySelectorAll("g[stroke-width='1.5'] > line")).toHaveLength(6);
  });

  it("names the categories and the axes, and the series when there are several", () => {
    const two: BarGraphDiagram = { ...bar, series: [{ label: "2022", values: [12, 15, 8], color: "blue" }, { label: "2023", values: [10, 11, 9], color: "red" }] };
    const { container } = render(<DiagramRenderer diagram={two} />);
    for (const text of ["Control", "Fertilizer", "Shade", "Treatment", "Mean mass (g)", "2022", "2023"]) expect(screen.getByText(text)).toBeInTheDocument();
    // 6 bars + 2 legend swatches
    expect(container.querySelectorAll("rect")).toHaveLength(8);
  });

  it("tilts long category names", () => {
    const { container } = render(<DiagramRenderer diagram={{ ...bar, categories: ["Control group", "Fertilizer and shade", "Shade only"] }} />);
    expect(container.querySelector("text[transform^='rotate(-35']")).not.toBeNull();
  });
});

describe("cladogram", () => {
  it("is one image whose text equivalent lists the groups, the marked points and the characters", () => {
    render(<DiagramRenderer diagram={clade} />);
    const name = screen.getByRole("img").getAttribute("aria-label")!;
    expect(name).toContain("(Annelida, (Chiton, Clam))");
    expect(name).toContain("point 2 is the common ancestor of Chiton, Clam");
    expect(name).toContain('"mantle" arises');
  });

  it("sits in a focusable box that scrolls sideways, and the tree keeps a minimum width so its labels stay readable on a phone", () => {
    render(<DiagramRenderer diagram={clade} />);
    const box = screen.getByRole("region", { name: /scrolls sideways/i });
    expect(box).toHaveAttribute("tabindex", "0");
    expect(box.className).toContain("overflow-x-auto");
    expect(screen.getByRole("img").getAttribute("class")).toContain("min-w-[26rem]");
  });

  it("writes every tip's name, the node marks and the branch character", () => {
    render(<DiagramRenderer diagram={clade} />);
    for (const text of ["Annelida", "Chiton", "Clam", "1", "2", "mantle"]) expect(screen.getByText(text)).toBeInTheDocument();
  });

  it("draws a horizontal branch into every node and a vertical connector for every branching point", () => {
    const { container } = render(<DiagramRenderer diagram={clade} />);
    // 5 nodes -> 5 branches; 2 branching points -> 2 connectors; 1 trait tick
    const lines = container.querySelectorAll("line");
    expect(lines).toHaveLength(5 + 2 + 1);
  });
});

describe("xy-graph legend", () => {
  const xy = (series: { label?: string; color: "blue" | "red" | "green" | "purple" }[]): Diagram => ({
    type: "xy-graph", xLabel: "S (mM)", yLabel: "Rate", xMin: 0, xMax: 10, yMin: 0, yMax: 10,
    series: series.map((s) => ({ ...s, points: [{ x: 0, y: 0 }, { x: 5, y: 5 }] })),
  });

  it("names each line when there are several, so a question can refer to them", () => {
    const { container } = render(<DiagramRenderer diagram={xy([{ label: "No inhibitor", color: "blue" }, { label: "Inhibitor X", color: "red" }])} />);
    expect(screen.getByText("No inhibitor")).toBeInTheDocument();
    expect(screen.getByText("Inhibitor X")).toBeInTheDocument();
    expect(container.querySelectorAll("svg rect")).toHaveLength(2);
  });

  it("draws no legend for a single line, even a named one, and keeps the original height", () => {
    const { container } = render(<DiagramRenderer diagram={xy([{ label: "Only line", color: "blue" }])} />);
    expect(screen.queryByText("Only line")).toBeNull();
    expect(container.querySelector("svg")!.getAttribute("viewBox")).toBe("0 0 400 280");
  });

  it("adds the legend's room above the plot, leaving the plot the same size", () => {
    const { container } = render(<DiagramRenderer diagram={xy([{ label: "A", color: "blue" }, { label: "B", color: "red" }])} />);
    expect(container.querySelector("svg")!.getAttribute("viewBox")).toBe("0 0 400 306");
  });
});

describe("DiagramRenderer", () => {
  it("still draws the original two kinds", () => {
    const xy: Diagram = { type: "xy-graph", xLabel: "t (s)", yLabel: "v (m/s)", xMin: 0, xMax: 10, yMin: 0, yMax: 10, series: [{ points: [{ x: 0, y: 0 }, { x: 5, y: 5 }], color: "blue" }] };
    const { unmount } = render(<DiagramRenderer diagram={xy} />);
    expect(screen.getByRole("img")).toHaveAccessibleName("Graph of v (m/s) vs t (s)");
    unmount();
    render(<DiagramRenderer diagram={{ type: "force-diagram", vectors: [{ label: "Weight", angleDegrees: 270, magnitude: 5, color: "red" }] }} />);
    expect(screen.getByRole("img")).toBeInTheDocument();
  });

  it("draws something for every kind the schema allows", () => {
    for (const diagram of [table, bar, clade]) {
      const { container, unmount } = render(<DiagramRenderer diagram={diagram} />);
      expect(container.firstChild).not.toBeNull();
      unmount();
    }
  });
});
