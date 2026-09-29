import type { ForceDiagram as ForceDiagramData } from "@/lib/content/diagram-schema";
import { bestLabelDirection, textAnchorForAngle, vectorEndpoint } from "@/lib/diagrams/geometry";

const SIZE = 280;
const CENTER = SIZE / 2;
const SCALE = 16; // pixels per unit of relative magnitude
const ARROWHEAD_LENGTH = 8;
const LABEL_OFFSET = 16; // fixed pixel gap past the arrow tip, independent of vector length -- a short vector's label would otherwise land too close to the object marker
const OBJECT_LABEL_DISTANCE = 32;

const VECTOR_COLOR: Record<string, string> = {
  blue: "#3b82f6",
  red: "#ef4444",
  green: "#22c55e",
  purple: "#a855f7",
  orange: "#f97316",
};

function arrowheadPoints(tipX: number, tipY: number, angleDegrees: number): string {
  const radians = (angleDegrees * Math.PI) / 180;
  const backAngle1 = radians + Math.PI - Math.PI / 7;
  const backAngle2 = radians + Math.PI + Math.PI / 7;
  const x1 = tipX + ARROWHEAD_LENGTH * Math.cos(backAngle1);
  const y1 = tipY - ARROWHEAD_LENGTH * Math.sin(backAngle1);
  const x2 = tipX + ARROWHEAD_LENGTH * Math.cos(backAngle2);
  const y2 = tipY - ARROWHEAD_LENGTH * Math.sin(backAngle2);
  return `${tipX},${tipY} ${x1},${y1} ${x2},${y2}`;
}

export function ForceDiagram({ diagram }: { diagram: ForceDiagramData }) {
  const altText =
    diagram.altText ??
    `Force diagram${diagram.objectLabel ? ` of ${diagram.objectLabel}` : ""} showing ${diagram.vectors
      .map((v) => v.label)
      .join(", ")}`;

  const objectLabelAngle = bestLabelDirection(diagram.vectors.map((v) => v.angleDegrees));
  const objectLabelOffset = vectorEndpoint(objectLabelAngle, 1, OBJECT_LABEL_DISTANCE);

  return (
    <svg
      viewBox={`0 0 ${SIZE} ${SIZE}`}
      role="img"
      aria-label={altText}
      className="w-full max-w-xs text-neutral-500 dark:text-neutral-400"
    >
      {diagram.inclineAngleDegrees !== undefined && (
        <line
          x1={CENTER - 100}
          y1={CENTER + 100 * Math.tan((diagram.inclineAngleDegrees * Math.PI) / 180)}
          x2={CENTER + 100}
          y2={CENTER - 100 * Math.tan((diagram.inclineAngleDegrees * Math.PI) / 180)}
          stroke="currentColor"
          strokeWidth={1.5}
          strokeDasharray="4 3"
        />
      )}

      {/* Object marker */}
      <rect x={CENTER - 8} y={CENTER - 8} width={16} height={16} fill="currentColor" />
      {diagram.objectLabel && (
        <text
          x={CENTER + objectLabelOffset.dx}
          y={CENTER + objectLabelOffset.dy}
          fontSize={11}
          textAnchor={textAnchorForAngle(objectLabelAngle)}
          fill="currentColor"
        >
          {diagram.objectLabel}
        </text>
      )}

      {diagram.vectors.map((vector) => {
        const { dx, dy } = vectorEndpoint(vector.angleDegrees, vector.magnitude, SCALE);
        const tipX = CENTER + dx;
        const tipY = CENTER + dy;
        const color = VECTOR_COLOR[vector.color];
        const { dx: dirX, dy: dirY } = vectorEndpoint(vector.angleDegrees, 1, LABEL_OFFSET);
        const labelX = tipX + dirX;
        const labelY = tipY + dirY;

        return (
          <g key={vector.label}>
            <line x1={CENTER} y1={CENTER} x2={tipX} y2={tipY} stroke={color} strokeWidth={2.5} />
            <polygon points={arrowheadPoints(tipX, tipY, vector.angleDegrees)} fill={color} />
            <text
              x={labelX}
              y={labelY}
              fontSize={12}
              textAnchor={textAnchorForAngle(vector.angleDegrees)}
              fill={color}
              className="font-medium"
            >
              {vector.label}
            </text>
          </g>
        );
      })}
    </svg>
  );
}
