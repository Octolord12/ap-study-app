import type { HistogramDiagram } from "@/lib/content/diagram-schema";
import { describeHistogram } from "@/lib/diagrams/describe";
import type { PixelDims } from "@/lib/diagrams/geometry";
import { layoutHistogram } from "@/lib/diagrams/histogram-layout";
import { SERIES_COLOR } from "@/lib/diagrams/palette";

const DIMS: PixelDims = { width: 420, height: 280, marginLeft: 55, marginRight: 20, marginTop: 20, marginBottom: 50 };

export function Histogram({ diagram }: { diagram: HistogramDiagram }) {
  const layout = layoutHistogram(diagram, DIMS);
  const plotTop = DIMS.marginTop;
  const label = diagram.altText ?? describeHistogram(diagram);

  return (
    <svg viewBox={`0 0 ${DIMS.width} ${DIMS.height}`} role="img" aria-label={label} className="w-full max-w-md text-neutral-500 dark:text-neutral-400">
      <line x1={DIMS.marginLeft} y1={plotTop} x2={DIMS.marginLeft} y2={layout.baselineY} stroke="currentColor" strokeWidth={1.5} />
      <line x1={DIMS.marginLeft} y1={layout.baselineY} x2={DIMS.width - DIMS.marginRight} y2={layout.baselineY} stroke="currentColor" strokeWidth={1.5} />

      {layout.yTicks.map((t) => (
        <g key={`y-${t.text}`}>
          <line x1={DIMS.marginLeft - 3} y1={t.y} x2={DIMS.marginLeft + 3} y2={t.y} stroke="currentColor" strokeWidth={1} />
          <text x={DIMS.marginLeft - 8} y={t.y + 3} fontSize={11} textAnchor="end" fill="currentColor">
            {t.text}
          </text>
        </g>
      ))}

      {layout.bars.map((bar) => (
        <rect key={bar.from} x={bar.x} y={bar.y} width={bar.width} height={bar.height} fill={SERIES_COLOR.blue} stroke="currentColor" strokeWidth={1} />
      ))}

      {layout.xLabels.map((t) => (
        <g key={`x-${t.x}`}>
          <line x1={t.x} y1={layout.baselineY} x2={t.x} y2={layout.baselineY + 4} stroke="currentColor" strokeWidth={1} />
          <text x={t.x} y={layout.baselineY + 16} fontSize={11} textAnchor="middle" fill="currentColor">
            {t.text}
          </text>
        </g>
      ))}

      <text x={(DIMS.marginLeft + DIMS.width - DIMS.marginRight) / 2} y={DIMS.height - 6} fontSize={12} textAnchor="middle" fill="currentColor" className="font-medium">
        {diagram.xLabel}
      </text>
      <text x={14} y={(plotTop + layout.baselineY) / 2} fontSize={12} textAnchor="middle" fill="currentColor" className="font-medium" transform={`rotate(-90, 14, ${(plotTop + layout.baselineY) / 2})`}>
        {diagram.yLabel}
      </text>
    </svg>
  );
}
