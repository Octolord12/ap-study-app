import type { ScatterplotDiagram } from "@/lib/content/diagram-schema";
import { describeScatterplot } from "@/lib/diagrams/describe";
import type { PixelDims } from "@/lib/diagrams/geometry";
import { SERIES_COLOR } from "@/lib/diagrams/palette";
import { layoutScatter } from "@/lib/diagrams/scatter-layout";

const DIMS: PixelDims = { width: 420, height: 300, marginLeft: 55, marginRight: 20, marginTop: 20, marginBottom: 50 };

export function Scatterplot({ diagram }: { diagram: ScatterplotDiagram }) {
  const layout = layoutScatter(diagram, DIMS);
  const bottom = DIMS.height - DIMS.marginBottom;
  const label = diagram.altText ?? describeScatterplot(diagram);

  return (
    <svg viewBox={`0 0 ${DIMS.width} ${DIMS.height}`} role="img" aria-label={label} className="w-full max-w-md text-neutral-500 dark:text-neutral-400">
      <line x1={DIMS.marginLeft} y1={DIMS.marginTop} x2={DIMS.marginLeft} y2={bottom} stroke="currentColor" strokeWidth={1.5} />
      <line x1={DIMS.marginLeft} y1={bottom} x2={DIMS.width - DIMS.marginRight} y2={bottom} stroke="currentColor" strokeWidth={1.5} />

      {layout.xTicks.map((t) => (
        <g key={`x-${t.x}`}>
          <line x1={t.x} y1={bottom - 3} x2={t.x} y2={bottom + 3} stroke="currentColor" strokeWidth={1} />
          <text x={t.x} y={bottom + 16} fontSize={11} textAnchor="middle" fill="currentColor">
            {t.text}
          </text>
        </g>
      ))}
      {layout.yTicks.map((t) => (
        <g key={`y-${t.y}`}>
          <line x1={DIMS.marginLeft - 3} y1={t.y} x2={DIMS.marginLeft + 3} y2={t.y} stroke="currentColor" strokeWidth={1} />
          <text x={DIMS.marginLeft - 8} y={t.y + 3} fontSize={11} textAnchor="end" fill="currentColor">
            {t.text}
          </text>
        </g>
      ))}

      {layout.zeroLineY !== null && (
        <line x1={DIMS.marginLeft} y1={layout.zeroLineY} x2={DIMS.width - DIMS.marginRight} y2={layout.zeroLineY} stroke="currentColor" strokeWidth={1.25} strokeDasharray="5 4" />
      )}
      {layout.line && <line x1={layout.line.x1} y1={layout.line.y1} x2={layout.line.x2} y2={layout.line.y2} stroke={SERIES_COLOR.red} strokeWidth={2} />}

      {layout.points.map((p) => (
        <circle key={p.index} cx={p.cx} cy={p.cy} r={3.5} fill={SERIES_COLOR.blue} fillOpacity={0.85} />
      ))}
      {layout.highlights.map((h) => (
        <g key={h.label}>
          <circle cx={h.cx} cy={h.cy} r={7} fill="none" className="stroke-neutral-900 dark:stroke-neutral-100" strokeWidth={1.5} />
          <text x={h.cx + 11} y={h.cy + 4} fontSize={12} fill="currentColor" className="font-semibold">
            {h.label}
          </text>
        </g>
      ))}

      <text x={(DIMS.marginLeft + DIMS.width - DIMS.marginRight) / 2} y={DIMS.height - 6} fontSize={12} textAnchor="middle" fill="currentColor" className="font-medium">
        {diagram.xLabel}
      </text>
      <text x={14} y={(DIMS.marginTop + bottom) / 2} fontSize={12} textAnchor="middle" fill="currentColor" className="font-medium" transform={`rotate(-90, 14, ${(DIMS.marginTop + bottom) / 2})`}>
        {diagram.yLabel}
      </text>
    </svg>
  );
}
