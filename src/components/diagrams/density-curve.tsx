import type { DensityCurveDiagram } from "@/lib/content/diagram-schema";
import { layoutCurve } from "@/lib/diagrams/curve-layout";
import { describeDensityCurve } from "@/lib/diagrams/describe";
import type { PixelDims } from "@/lib/diagrams/geometry";
import { SERIES_COLOR } from "@/lib/diagrams/palette";

const DIMS: PixelDims = { width: 420, height: 230, marginLeft: 20, marginRight: 20, marginTop: 14, marginBottom: 48 };

export function DensityCurve({ diagram }: { diagram: DensityCurveDiagram }) {
  const layout = layoutCurve(diagram, DIMS);
  const label = diagram.altText ?? describeDensityCurve(diagram);

  return (
    <svg viewBox={`0 0 ${DIMS.width} ${DIMS.height}`} role="img" aria-label={label} className="w-full max-w-md text-neutral-500 dark:text-neutral-400">
      {layout.areas.map((d, i) => (
        <path key={i} d={d} fill={SERIES_COLOR.blue} fillOpacity={0.45} stroke="none" />
      ))}
      <path d={layout.path} fill="none" className="stroke-neutral-900 dark:stroke-neutral-100" strokeWidth={2} strokeLinejoin="round" />
      <line x1={layout.axisLeft} y1={layout.baselineY} x2={layout.axisRight} y2={layout.baselineY} stroke="currentColor" strokeWidth={1.5} />
      {layout.ticks.map((t, i) => (
        <g key={i}>
          <line x1={t.x} y1={layout.baselineY} x2={t.x} y2={layout.baselineY + 5} stroke="currentColor" strokeWidth={1.25} />
          <text x={t.x} y={layout.baselineY + 18} fontSize={11} textAnchor="middle" fill="currentColor">
            {t.text}
          </text>
        </g>
      ))}
      {diagram.xLabel && (
        <text x={(layout.axisLeft + layout.axisRight) / 2} y={DIMS.height - 6} fontSize={12} textAnchor="middle" fill="currentColor" className="font-medium">
          {diagram.xLabel}
        </text>
      )}
    </svg>
  );
}
