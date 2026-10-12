import type { XYGraphDiagram } from "@/lib/content/diagram-schema";
import { axisTicks, formatTick, projectPoint, type PixelDims } from "@/lib/diagrams/geometry";
import { SERIES_COLOR } from "@/lib/diagrams/palette";

const DIMS: PixelDims = { width: 400, height: 280, marginLeft: 55, marginRight: 20, marginTop: 20, marginBottom: 45 };
const TICK_COUNT = 5;

export function XYGraph({ diagram }: { diagram: XYGraphDiagram }) {
  const bounds = diagram;
  const xTicks = axisTicks(diagram.xMin, diagram.xMax, TICK_COUNT);
  const yTicks = axisTicks(diagram.yMin, diagram.yMax, TICK_COUNT);

  const originPx = projectPoint({ x: diagram.xMin, y: diagram.yMin }, bounds, DIMS);
  const topRightPx = projectPoint({ x: diagram.xMax, y: diagram.yMax }, bounds, DIMS);

  const altText = diagram.altText ?? `Graph of ${diagram.yLabel} vs ${diagram.xLabel}`;

  return (
    <svg
      viewBox={`0 0 ${DIMS.width} ${DIMS.height}`}
      role="img"
      aria-label={altText}
      className="w-full max-w-md text-neutral-500 dark:text-neutral-400"
    >
      {/* Axis lines */}
      <line
        x1={originPx.px}
        y1={originPx.py}
        x2={topRightPx.px}
        y2={originPx.py}
        stroke="currentColor"
        strokeWidth={1.5}
      />
      <line
        x1={originPx.px}
        y1={originPx.py}
        x2={originPx.px}
        y2={topRightPx.py}
        stroke="currentColor"
        strokeWidth={1.5}
      />

      {/* Ticks + labels */}
      {xTicks.map((t) => {
        const { px, py } = projectPoint({ x: t, y: diagram.yMin }, bounds, DIMS);
        return (
          <g key={`x-${t}`}>
            <line x1={px} y1={py - 3} x2={px} y2={py + 3} stroke="currentColor" strokeWidth={1} />
            <text x={px} y={py + 16} fontSize={11} textAnchor="middle" fill="currentColor">
              {formatTick(t)}
            </text>
          </g>
        );
      })}
      {yTicks.map((t) => {
        const { px, py } = projectPoint({ x: diagram.xMin, y: t }, bounds, DIMS);
        return (
          <g key={`y-${t}`}>
            <line x1={px - 3} y1={py} x2={px + 3} y2={py} stroke="currentColor" strokeWidth={1} />
            <text x={px - 8} y={py + 3} fontSize={11} textAnchor="end" fill="currentColor">
              {formatTick(t)}
            </text>
          </g>
        );
      })}

      {/* Axis labels */}
      <text
        x={(originPx.px + topRightPx.px) / 2}
        y={DIMS.height - 6}
        fontSize={12}
        textAnchor="middle"
        fill="currentColor"
        className="font-medium"
      >
        {diagram.xLabel}
      </text>
      <text
        x={14}
        y={(originPx.py + topRightPx.py) / 2}
        fontSize={12}
        textAnchor="middle"
        fill="currentColor"
        className="font-medium"
        transform={`rotate(-90, 14, ${(originPx.py + topRightPx.py) / 2})`}
      >
        {diagram.yLabel}
      </text>

      {/* Series */}
      {diagram.series.map((series, i) => {
        const color = SERIES_COLOR[series.color];
        const pixelPoints = series.points.map((p) => projectPoint(p, bounds, DIMS));
        const polylinePoints = pixelPoints.map((p) => `${p.px},${p.py}`).join(" ");
        return (
          <g key={series.label ?? i}>
            <polyline points={polylinePoints} fill="none" stroke={color} strokeWidth={2.5} />
            {pixelPoints.map((p, j) => (
              <circle key={j} cx={p.px} cy={p.py} r={3.5} fill={color} />
            ))}
          </g>
        );
      })}
    </svg>
  );
}
