import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";
import { DiagramRenderer } from "@/components/diagrams/diagram-renderer";
import type { BoxplotDiagram, DensityCurveDiagram, DotplotDiagram, HistogramDiagram, ScatterplotDiagram } from "@/lib/content/diagram-schema";
import { describeBoxplot, describeDensityCurve, describeDotplot, describeHistogram, describeScatterplot } from "@/lib/diagrams/describe";

const hist: HistogramDiagram = { type: "histogram", xLabel: "Commute time (min)", yLabel: "Frequency", edges: [0, 10, 20, 30, 40], values: [3, 8, 5, 1], yMax: 10, yStep: 2, tickAt: "edges", labelEvery: 1 };
const box: BoxplotDiagram = {
  type: "boxplot",
  xLabel: "Session duration (s)",
  axisMin: 0,
  axisMax: 100,
  axisStep: 20,
  groups: [{ label: "DES", min: 10, q1: 30, median: 45, q3: 60, max: 90, outliers: [96, 99] }, { label: "AES", min: 5, q1: 25, median: 50, q3: 70, max: 95 }],
};
const dots: DotplotDiagram = { type: "dotplot", xLabel: "Pets", axisMin: 0, axisMax: 6, axisStep: 1, dots: [{ x: 0, count: 3 }, { x: 1, count: 6 }, { x: 2, count: 4 }] };
const scatter: ScatterplotDiagram = {
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
};
const pts = Array.from({ length: 41 }, (_, i) => {
  const x = Math.round((-4 + i * 0.2) * 10) / 10;
  return { x, y: Math.exp((-x * x) / 2) / Math.sqrt(2 * Math.PI) };
});
const curve: DensityCurveDiagram = { type: "density-curve", xLabel: "z", points: pts, shade: [{ from: 1.2, to: 4 }], ticks: [{ x: 0, label: "0" }, { x: 1.2, label: "1.2" }] };

const svg = (container: HTMLElement) => container.querySelector("svg")!;

describe("histogram", () => {
  it("is an image named by its own data, with one touching bar per interval and labelled axes", () => {
    const { container } = render(<DiagramRenderer diagram={hist} />);
    expect(screen.getByRole("img")).toHaveAttribute("aria-label", describeHistogram(hist));
    expect(container.querySelectorAll("rect")).toHaveLength(4);
    expect(container.textContent).toContain("Commute time (min)");
    expect(container.textContent).toContain("Frequency");
    for (const tick of ["0", "10", "20", "30", "40"]) expect(Array.from(container.querySelectorAll("text")).some((t) => t.textContent === tick)).toBe(true);
  });

  it("uses the author's alt text when there is one", () => {
    render(<DiagramRenderer diagram={{ ...hist, altText: "Right-skewed commute times" }} />);
    expect(screen.getByRole("img")).toHaveAttribute("aria-label", "Right-skewed commute times");
  });
});

describe("boxplot", () => {
  it("draws a box per group, a dot per outlier, and names the groups", () => {
    const { container } = render(<DiagramRenderer diagram={box} />);
    expect(screen.getByRole("img")).toHaveAttribute("aria-label", describeBoxplot(box));
    expect(container.querySelectorAll("rect")).toHaveLength(2);
    expect(container.querySelectorAll("circle")).toHaveLength(2);
    expect(container.textContent).toContain("DES");
    expect(container.textContent).toContain("AES");
    expect(container.textContent).toContain("Session duration (s)");
  });

  it("names no group when there is only one", () => {
    const { container } = render(<DiagramRenderer diagram={{ ...box, groups: [{ min: 10, q1: 30, median: 45, q3: 60, max: 90 }] }} />);
    expect(container.querySelectorAll("rect")).toHaveLength(1);
    expect(container.textContent).not.toContain("DES");
  });
});

describe("dotplot", () => {
  it("draws one dot for each count", () => {
    const { container } = render(<DiagramRenderer diagram={dots} />);
    expect(screen.getByRole("img")).toHaveAttribute("aria-label", describeDotplot(dots));
    expect(container.querySelectorAll("circle")).toHaveLength(13);
    expect(container.textContent).toContain("Pets");
  });
});

describe("scatterplot", () => {
  it("draws a point for each pair, with no line unless asked", () => {
    const { container } = render(<DiagramRenderer diagram={scatter} />);
    expect(screen.getByRole("img")).toHaveAttribute("aria-label", describeScatterplot(scatter));
    expect(container.querySelectorAll("circle")).toHaveLength(3);
    expect(container.querySelectorAll("line[stroke='#ef4444']")).toHaveLength(0);
  });

  it("draws the least-squares line in red when given one", () => {
    const { container } = render(<DiagramRenderer diagram={{ ...scatter, line: { intercept: 313, slope: -30 } }} />);
    expect(container.querySelectorAll("line[stroke='#ef4444']")).toHaveLength(1);
  });

  it("draws a dashed zero line for a residual plot", () => {
    const { container } = render(<DiagramRenderer diagram={{ ...scatter, yMin: -20, yMax: 20, yStep: 10, points: [{ x: 7, y: -5 }, { x: 8, y: 9 }], zeroLine: true }} />);
    expect(container.querySelectorAll("line[stroke-dasharray]")).toHaveLength(1);
    expect(screen.getByRole("img").getAttribute("aria-label")).toMatch(/^Residual plot/);
  });

  it("circles and labels a highlighted point", () => {
    const { container } = render(<DiagramRenderer diagram={{ ...scatter, highlights: [{ index: 1, label: "A" }] }} />);
    expect(container.querySelectorAll("circle")).toHaveLength(4);
    expect(Array.from(container.querySelectorAll("text")).some((t) => t.textContent === "A")).toBe(true);
  });
});

describe("density curve", () => {
  it("draws the curve and one shaded area per region, with the marked values under the axis", () => {
    const { container } = render(<DiagramRenderer diagram={curve} />);
    expect(screen.getByRole("img")).toHaveAttribute("aria-label", describeDensityCurve(curve));
    expect(container.querySelectorAll("path")).toHaveLength(2);
    expect(container.querySelectorAll("path[fill-opacity]")).toHaveLength(1);
    expect(Array.from(container.querySelectorAll("text")).map((t) => t.textContent)).toEqual(expect.arrayContaining(["0", "1.2", "z"]));
  });

  it("has no shaded area when nothing is shaded", () => {
    const { container } = render(<DiagramRenderer diagram={{ ...curve, shade: undefined }} />);
    expect(container.querySelectorAll("path")).toHaveLength(1);
  });
});

describe("all five", () => {
  it("scale to the column instead of widening the page", () => {
    for (const d of [hist, box, dots, scatter, curve]) {
      const { container, unmount } = render(<DiagramRenderer diagram={d} />);
      expect(svg(container).getAttribute("class")).toContain("w-full");
      expect(svg(container).getAttribute("viewBox")).toMatch(/^0 0 \d+(\.\d+)? \d+(\.\d+)?$/);
      unmount();
    }
  });
});
