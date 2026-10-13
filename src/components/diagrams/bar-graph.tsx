import type { BarGraphDiagram } from "@/lib/content/diagram-schema";
import { layoutBars, shouldRotateLabels } from "@/lib/diagrams/bar-layout";
import { describeBarGraph } from "@/lib/diagrams/describe";
import { axisTicks, formatTick, type PixelDims } from "@/lib/diagrams/geometry";
import { layoutLegend, LEGEND_ROW_HEIGHT, legendLabels } from "@/lib/diagrams/legend";
import { SERIES_COLOR } from "@/lib/diagrams/palette";

const PLOT_HEIGHT = 232;
const TICK_COUNT = 5;

export function BarGraph({ diagram }: { diagram: BarGraphDiagram }) {
  const width = 420;
  const marginLeft = 55;
  const marginRight = 20;
  const labels = legendLabels(diagram.series);
  const legend = layoutLegend(labels, width - marginLeft - marginRight);
  const slot = (width - marginLeft - marginRight) / diagram.categories.length;
  const rotate = shouldRotateLabels(diagram.categories, slot);
  const marginTop = 20 + legend.height;
  const marginBottom = rotate ? 96 : 48;
  const dims: PixelDims = { width, height: PLOT_HEIGHT + marginTop + marginBottom, marginLeft, marginRight, marginTop, marginBottom };
  const layout = layoutBars(diagram.series, diagram.categories.length, diagram.yMin, diagram.yMax, dims);
  const yTicks = axisTicks(diagram.yMin, diagram.yMax, TICK_COUNT);
  const plotTop = marginTop;
  const plotBottom = dims.height - marginBottom;
  const yOf = (v: number) => plotBottom - ((v - diagram.yMin) / (diagram.yMax - diagram.yMin)) * PLOT_HEIGHT;
  const label = diagram.altText ?? describeBarGraph(diagram);

  return (
    <svg viewBox={`0 0 ${dims.width} ${dims.height}`} role="img" aria-label={label} className="w-full max-w-md text-neutral-500 dark:text-neutral-400">
      <line x1={marginLeft} y1={plotTop} x2={marginLeft} y2={plotBottom} stroke="currentColor" strokeWidth={1.5} />
      <line x1={marginLeft} y1={layout.baselineY} x2={width - marginRight} y2={layout.baselineY} stroke="currentColor" strokeWidth={1.5} />

      {yTicks.map((t) => (
        <g key={`y-${t}`}>
          <line x1={marginLeft - 3} y1={yOf(t)} x2={marginLeft + 3} y2={yOf(t)} stroke="currentColor" strokeWidth={1} />
          <text x={marginLeft - 8} y={yOf(t) + 3} fontSize={11} textAnchor="end" fill="currentColor">
            {formatTick(t)}
          </text>
        </g>
      ))}

      {diagram.categories.map((category, ci) => {
        const cx = layout.categoryCenters[ci];
        const y = plotBottom + 16;
        return rotate ? (
          <text key={category} x={cx} y={y} fontSize={11} textAnchor="end" fill="currentColor" transform={`rotate(-35, ${cx}, ${y})`}>
            {category}
          </text>
        ) : (
          <text key={category} x={cx} y={y} fontSize={11} textAnchor="middle" fill="currentColor">
            {category}
          </text>
        );
      })}

      {layout.bars.map((bar) => (
        <rect key={`${bar.series}-${bar.category}`} x={bar.x} y={bar.y} width={bar.width} height={bar.height} fill={SERIES_COLOR[diagram.series[bar.series].color]} />
      ))}

      {layout.errorBars.map((e) => (
        <g key={`e-${e.series}-${e.category}`} className="stroke-neutral-900 dark:stroke-neutral-100" strokeWidth={1.5}>
          <line x1={e.x} y1={e.yTop} x2={e.x} y2={e.yBottom} />
          <line x1={e.x - e.capHalfWidth} y1={e.yTop} x2={e.x + e.capHalfWidth} y2={e.yTop} />
          <line x1={e.x - e.capHalfWidth} y1={e.yBottom} x2={e.x + e.capHalfWidth} y2={e.yBottom} />
        </g>
      ))}

      <text x={(marginLeft + width - marginRight) / 2} y={dims.height - 6} fontSize={12} textAnchor="middle" fill="currentColor" className="font-medium">
        {diagram.xLabel}
      </text>
      <text x={14} y={(plotTop + plotBottom) / 2} fontSize={12} textAnchor="middle" fill="currentColor" className="font-medium" transform={`rotate(-90, 14, ${(plotTop + plotBottom) / 2})`}>
        {diagram.yLabel}
      </text>

      {labels.map((label, i) => (
        <g key={i} transform={`translate(${marginLeft + legend.items[i].x}, ${10 + legend.items[i].row * LEGEND_ROW_HEIGHT})`}>
          <rect width={12} height={12} fill={SERIES_COLOR[diagram.series[i].color]} />
          <text x={18} y={10} fontSize={11} fill="currentColor">
            {label}
          </text>
        </g>
      ))}
    </svg>
  );
}
