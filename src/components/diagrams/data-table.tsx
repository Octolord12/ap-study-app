import type { DataTableDiagram } from "@/lib/content/diagram-schema";
import { describeDataTable } from "@/lib/diagrams/describe";

// Cells are rendered as React text, never as HTML. The box scrolls sideways on a narrow screen instead of
// widening the page, and is focusable so a keyboard user can scroll it.
export function DataTable({ diagram }: { diagram: DataTableDiagram }) {
  const label = diagram.altText ?? describeDataTable(diagram);
  return (
    <figure className="my-4 max-w-full">
      <div role="region" aria-label={label} tabIndex={0} className="overflow-x-auto border border-border">
        <table className="w-full border-collapse text-sm">
          {diagram.caption && <caption className="px-3 py-2 text-left text-xs font-medium text-muted-foreground">{diagram.caption}</caption>}
          <thead>
            <tr className="bg-muted">
              {diagram.columns.map((column, i) => (
                <th key={i} scope="col" className={`border-b border-border px-3 py-1.5 font-medium ${i === 0 ? "text-left" : "text-center"}`}>
                  {column}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {diagram.rows.map((row, r) => (
              <tr key={r} className="border-b border-border last:border-b-0">
                {diagram.columns.map((_, c) =>
                  c === 0 && diagram.rowHeaders ? (
                    <th key={c} scope="row" className="px-3 py-1.5 text-left font-medium">
                      {row[c] ?? ""}
                    </th>
                  ) : (
                    <td key={c} className={`px-3 py-1.5 tabular-nums ${c === 0 ? "text-left" : "text-center"}`}>
                      {row[c] ?? ""}
                    </td>
                  ),
                )}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </figure>
  );
}
