import { describe, expect, it } from "vitest";
import { bestLabelDirection, projectPoint, textAnchorForAngle, vectorEndpoint } from "@/lib/diagrams/geometry";

const DIMS = { width: 400, height: 300, marginLeft: 50, marginRight: 20, marginTop: 20, marginBottom: 40 };
const BOUNDS = { xMin: 0, xMax: 10, yMin: 0, yMax: 10 };

describe("projectPoint", () => {
  it("maps the bottom-left data corner to the bottom-left plot pixel", () => {
    const { px, py } = projectPoint({ x: 0, y: 0 }, BOUNDS, DIMS);
    expect(px).toBe(DIMS.marginLeft);
    expect(py).toBe(DIMS.height - DIMS.marginBottom);
  });

  it("maps the top-right data corner to the top-right plot pixel (y flipped for SVG)", () => {
    const { px, py } = projectPoint({ x: 10, y: 10 }, BOUNDS, DIMS);
    expect(px).toBe(DIMS.width - DIMS.marginRight);
    expect(py).toBe(DIMS.marginTop);
  });

  it("maps the midpoint to the center of the plot area", () => {
    const { px, py } = projectPoint({ x: 5, y: 5 }, BOUNDS, DIMS);
    const plotWidth = DIMS.width - DIMS.marginLeft - DIMS.marginRight;
    const plotHeight = DIMS.height - DIMS.marginTop - DIMS.marginBottom;
    expect(px).toBe(DIMS.marginLeft + plotWidth / 2);
    expect(py).toBe(DIMS.height - DIMS.marginBottom - plotHeight / 2);
  });
});

describe("vectorEndpoint", () => {
  it("points right (+dx, 0) at angle 0", () => {
    const { dx, dy } = vectorEndpoint(0, 1, 10);
    expect(dx).toBeCloseTo(10);
    expect(dy).toBeCloseTo(0);
  });

  it("points up (0, -dy) at angle 90, since SVG y grows downward", () => {
    const { dx, dy } = vectorEndpoint(90, 1, 10);
    expect(dx).toBeCloseTo(0);
    expect(dy).toBeCloseTo(-10);
  });

  it("points left (-dx, 0) at angle 180", () => {
    const { dx, dy } = vectorEndpoint(180, 1, 10);
    expect(dx).toBeCloseTo(-10);
    expect(dy).toBeCloseTo(0);
  });

  it("points down (0, +dy) at angle 270", () => {
    const { dx, dy } = vectorEndpoint(270, 1, 10);
    expect(dx).toBeCloseTo(0);
    expect(dy).toBeCloseTo(10);
  });

  it("scales linearly with magnitude", () => {
    const single = vectorEndpoint(0, 1, 10);
    const triple = vectorEndpoint(0, 3, 10);
    expect(triple.dx).toBeCloseTo(single.dx * 3);
  });
});

describe("textAnchorForAngle", () => {
  it("anchors 'start' for a label offset to the right (regression: object label straddling the marker at angle 0)", () => {
    expect(textAnchorForAngle(0)).toBe("start");
  });

  it("anchors 'end' for a label offset to the left", () => {
    expect(textAnchorForAngle(180)).toBe("end");
  });

  it("anchors 'middle' for a label offset straight up or down", () => {
    expect(textAnchorForAngle(90)).toBe("middle");
    expect(textAnchorForAngle(270)).toBe("middle");
  });
});

describe("bestLabelDirection", () => {
  it("picks the opposite direction from a single occupied angle", () => {
    expect(bestLabelDirection([90])).toBe(270);
  });

  it("picks a direction clear of three clustered vectors (regression: force-diagram object label collision)", () => {
    // Normal at 120, Friction at 210, Weight at 270 -- all clustered on the
    // left/bottom. 0 (pointing right) is the most clear of the 8 candidates.
    expect(bestLabelDirection([120, 210, 270])).toBe(0);
  });

  it("defaults to the first candidate when there are no vectors", () => {
    expect(bestLabelDirection([])).toBe(0);
  });

  it("is symmetric: angles equally spaced around the circle have no single best answer, but the result is still maximally distant", () => {
    // 4 vectors at the cardinal directions -- every diagonal candidate (45,
    // 135, 225, 315) is equally 45 degrees from its two nearest occupied
    // angles, which is the best any candidate can do here.
    const direction = bestLabelDirection([0, 90, 180, 270]);
    expect([45, 135, 225, 315]).toContain(direction);
  });
});
