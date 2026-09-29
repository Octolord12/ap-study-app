// Pure coordinate-transform math for the SVG diagram components. Kept
// separate from rendering so the transforms are directly unit-testable
// (mirrors src/lib/gamification/xp.ts, src/lib/study/spaced-repetition.ts).

export interface AxisBounds {
  xMin: number;
  xMax: number;
  yMin: number;
  yMax: number;
}

export interface PixelDims {
  width: number;
  height: number;
  marginLeft: number;
  marginRight: number;
  marginTop: number;
  marginBottom: number;
}

export interface Pixel {
  px: number;
  py: number;
}

// Data space -> pixel space, for the xy-graph. SVG y grows downward, so the
// y-axis direction is flipped relative to standard graph orientation.
export function projectPoint(point: { x: number; y: number }, bounds: AxisBounds, dims: PixelDims): Pixel {
  const plotWidth = dims.width - dims.marginLeft - dims.marginRight;
  const plotHeight = dims.height - dims.marginTop - dims.marginBottom;

  const xFraction = (point.x - bounds.xMin) / (bounds.xMax - bounds.xMin);
  const yFraction = (point.y - bounds.yMin) / (bounds.yMax - bounds.yMin);

  return {
    px: dims.marginLeft + xFraction * plotWidth,
    py: dims.height - dims.marginBottom - yFraction * plotHeight,
  };
}

// Polar (angleDegrees, magnitude) -> cartesian pixel offset, for force-vector
// arrows. Standard math convention: 0 = +x (right), 90 = +y (up),
// counterclockwise. Flipped for SVG's downward-growing y-axis.
export function vectorEndpoint(angleDegrees: number, magnitude: number, scale: number): { dx: number; dy: number } {
  const radians = (angleDegrees * Math.PI) / 180;
  return {
    dx: scale * magnitude * Math.cos(radians),
    dy: -scale * magnitude * Math.sin(radians),
  };
}

function angularDistance(a: number, b: number): number {
  const diff = Math.abs(a - b) % 360;
  return diff > 180 ? 360 - diff : diff;
}

const LABEL_DIRECTION_CANDIDATES = [0, 45, 90, 135, 180, 225, 270, 315];

// SVG text-anchor for a label offset in the given direction, so the label
// text grows away from its anchor point instead of straddling it -- e.g. a
// label placed to the right of a marker should start at that point and grow
// rightward ("start"), not be horizontally centered on it.
export function textAnchorForAngle(angleDegrees: number): "start" | "middle" | "end" {
  const cos = Math.cos((angleDegrees * Math.PI) / 180);
  if (cos > 0.35) return "start";
  if (cos < -0.35) return "end";
  return "middle";
}

// Picks the compass direction (degrees, same convention as vectorEndpoint)
// with the greatest angular distance from every given occupied angle -- used
// to place the force-diagram's object label somewhere not already claimed by
// a vector's own label, since a fixed position (e.g. always south) can
// collide with whichever vector happens to point that way.
export function bestLabelDirection(occupiedAngles: number[]): number {
  if (occupiedAngles.length === 0) return LABEL_DIRECTION_CANDIDATES[0];

  let best = LABEL_DIRECTION_CANDIDATES[0];
  let bestMinDistance = -1;
  for (const candidate of LABEL_DIRECTION_CANDIDATES) {
    const minDistance = Math.min(...occupiedAngles.map((angle) => angularDistance(candidate, angle)));
    if (minDistance > bestMinDistance) {
      bestMinDistance = minDistance;
      best = candidate;
    }
  }
  return best;
}
