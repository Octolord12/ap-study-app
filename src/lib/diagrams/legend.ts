// Pure layout for a graph legend: a row of colour swatches with labels that wraps to the next row when the labels would
// not fit the width, so a long label cannot run off the picture. Shared by the line and bar graphs.
export const LEGEND_ROW_HEIGHT = 18;
const SWATCH = 12;
const GAP = 6;
const SPACING = 18;
const APPROX_CHAR_WIDTH = 6.2; // px at the 11px label size

export interface LegendLayout {
  items: { x: number; row: number }[];
  rows: number;
  height: number; // room to leave above the plot
}

export function layoutLegend(labels: readonly string[], maxWidth: number): LegendLayout {
  const items: LegendLayout["items"] = [];
  let x = 0;
  let row = 0;
  for (const label of labels) {
    const width = SWATCH + GAP + label.length * APPROX_CHAR_WIDTH;
    if (x > 0 && x + width > maxWidth) {
      row += 1;
      x = 0;
    }
    items.push({ x, row });
    x += width + SPACING;
  }
  const rows = labels.length ? row + 1 : 0;
  return { items, rows, height: rows ? rows * LEGEND_ROW_HEIGHT + 8 : 0 };
}

// A legend is shown only when it tells the series apart: more than one, and at least one of them named.
export function legendLabels(series: readonly { label?: string }[]): string[] {
  return series.length > 1 && series.some((s) => s.label) ? series.map((s, i) => s.label ?? `Series ${i + 1}`) : [];
}
