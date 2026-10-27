import type { DotplotDiagram } from "@/lib/content/diagram-schema";
import { describeDotplot } from "@/lib/diagrams/describe";
import { layoutDotplot } from "@/lib/diagrams/dotplot-layout";
import { SERIES_COLOR } from "@/lib/diagrams/palette";

const WIDTH = 420;

export function Dotplot({ diagram }: { diagram: DotplotDiagram }) {
  const layout = layoutDotplot(diagram, WIDTH);
  const label = diagram.altText ?? describeDotplot(diagram);

  return (
    <svg viewBox={`0 0 ${layout.width} ${layout.height}`} role="img" aria-label={label} className="w-full max-w-md text-neutral-500 dark:text-neutral-400">
      {layout.dots.map((dot, i) => (
        <circle key={i} cx={dot.cx} cy={dot.cy} r={layout.radius} fill={SERIES_COLOR.blue} />
      ))}
      <line x1={layout.axisLeft} y1={layout.axisY} x2={layout.axisRight} y2={layout.axisY} stroke="currentColor" strokeWidth={1.5} />
      {layout.ticks.map((t) => (
        <g key={t.x}>
          <line x1={t.x} y1={layout.axisY} x2={t.x} y2={layout.axisY + 4} stroke="currentColor" strokeWidth={1} />
          <text x={t.x} y={layout.axisY + 16} fontSize={11} textAnchor="middle" fill="currentColor">
            {t.text}
          </text>
        </g>
      ))}
      <text x={(layout.axisLeft + layout.axisRight) / 2} y={layout.height - 6} fontSize={12} textAnchor="middle" fill="currentColor" className="font-medium">
        {diagram.xLabel}
      </text>
    </svg>
  );
}
