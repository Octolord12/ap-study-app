// Axis helpers shared by the statistics graphs (histogram, boxplot, dotplot, scatterplot, density curve): ticks at a
// chosen step, rather than the evenly divided five of the line graph, and numbers printed the way a textbook prints them.

// 0.30000000000000004 is not an axis label.
export function roundTo(value: number, decimals: number): number {
  const factor = 10 ** decimals;
  return Math.round(value * factor) / factor;
}

export function decimalsOf(step: number): number {
  const text = String(step);
  if (text.includes("e-")) return Number(text.split("e-")[1]) + (text.split("e-")[0].split(".")[1]?.length ?? 0);
  return text.split(".")[1]?.length ?? 0;
}

// min, min + step, ... up to max, inclusive; empty when the step does not divide the range (validateDiagram rejects that).
export function stepTicks(min: number, max: number, step: number): number[] {
  const count = Math.round((max - min) / step);
  if (count < 1 || Math.abs(min + count * step - max) > step * 1e-6) return [];
  const decimals = Math.max(decimalsOf(step), decimalsOf(min)) + 1;
  return Array.from({ length: count + 1 }, (_, i) => roundTo(min + i * step, decimals));
}

// 2 -> "2", 2.5 -> "2.5", 0.05 -> "0.05", 1000 -> "1000"
export function compactNumber(value: number): string {
  return String(roundTo(value, 6));
}

// A data value to a pixel position along one axis.
export function scaleLinear(domainMin: number, domainMax: number, rangeStart: number, rangeEnd: number): (value: number) => number {
  return (value) => rangeStart + ((value - domainMin) / (domainMax - domainMin)) * (rangeEnd - rangeStart);
}
