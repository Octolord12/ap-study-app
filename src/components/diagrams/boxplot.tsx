import type { BoxplotDiagram } from "@/lib/content/diagram-schema";
import { layoutBoxplot } from "@/lib/diagrams/boxplot-layout";
import { describeBoxplot } from "@/lib/diagrams/describe";

const WIDTH = 420;

export function Boxplot({ diagram }: { diagram: BoxplotDiagram }) {
  const layout = layoutBoxplot(diagram, WIDTH);
  const label = diagram.altText ?? describeBoxplot(diagram);

  return (
    <svg viewBox={`0 0 ${layout.width} ${layout.height}`} role="img" aria-label={label} className="w-full max-w-md text-neutral-500 dark:text-neutral-400">
      {layout.rows.map((row, i) => (
        <g key={i} className="stroke-neutral-900 dark:stroke-neutral-100" strokeWidth={1.5} fill="none">
          <line x1={row.min} y1={row.cy} x2={row.q1} y2={row.cy} />
          <line x1={row.q3} y1={row.cy} x2={row.max} y2={row.cy} />
          <line x1={row.min} y1={row.cy - 7} x2={row.min} y2={row.cy + 7} />
          <line x1={row.max} y1={row.cy - 7} x2={row.max} y2={row.cy + 7} />
          <rect x={row.q1} y={row.boxTop} width={row.q3 - row.q1} height={row.boxBottom - row.boxTop} />
          <line x1={row.median} y1={row.boxTop} x2={row.median} y2={row.boxBottom} strokeWidth={2.5} />
          {row.outliers.map((x) => (
            <circle key={x} cx={x} cy={row.cy} r={3.5} className="fill-neutral-900 dark:fill-neutral-100" stroke="none" />
          ))}
        </g>
      ))}
      {layout.rows.map(
        (row, i) =>
          row.label && (
            <text key={`l-${i}`} x={layout.axisLeft - 10} y={row.cy + 4} fontSize={11} textAnchor="end" fill="currentColor">
              {row.label}
            </text>
          ),
      )}

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
