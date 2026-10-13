import type { CladogramDiagram } from "@/lib/content/diagram-schema";
import { layoutCladogram } from "@/lib/diagrams/cladogram-layout";
import { describeCladogram } from "@/lib/diagrams/describe";

export function Cladogram({ diagram }: { diagram: CladogramDiagram }) {
  const layout = layoutCladogram(diagram.root);
  const label = diagram.altText ?? describeCladogram(diagram);
  const stemStart = 4;
  return (
    // Below about 420px the labels would be too small to read, so the tree keeps that width and the box scrolls
    // sideways (focusable, so a keyboard user can scroll it), like a wide table.
    <div
      role="region"
      aria-label="Diagram. Scrolls sideways on a narrow screen."
      tabIndex={0}
      className="max-w-xl overflow-x-auto"
    >
      <svg
        viewBox={`0 0 ${layout.width} ${layout.height}`}
        role="img"
        aria-label={label}
        className="w-full min-w-[26rem] text-neutral-600 dark:text-neutral-300"
      >
        <g stroke="currentColor" strokeWidth={2} fill="none">
          {layout.connectors.map((c, i) => (
            <line key={`v-${i}`} x1={c.x} y1={c.yTop} x2={c.x} y2={c.yBottom} />
          ))}
          {layout.nodes.map((n, i) => (
            <line
              key={`h-${i}`}
              x1={n.branchFromX === 0 ? stemStart : n.branchFromX}
              y1={n.y}
              x2={n.x}
              y2={n.y}
            />
          ))}
        </g>

        {layout.nodes.map((n, i) => {
          if (!n.trait) return null;
          const from = n.branchFromX === 0 ? stemStart : n.branchFromX;
          const tx = (from + n.x) / 2;
          return (
            <g key={`t-${i}`}>
              <line
                x1={tx}
                y1={n.y - 6}
                x2={tx}
                y2={n.y + 6}
                stroke="currentColor"
                strokeWidth={2}
              />
              {/* A halo in the card's color, so a label wider than its branch stays legible where it crosses a connector. */}
              <text
                x={tx}
                y={n.y - 11}
                fontSize={11}
                textAnchor="middle"
                fill="currentColor"
                stroke="var(--card)"
                strokeWidth={4}
                strokeLinejoin="round"
                paintOrder="stroke"
              >
                {n.trait}
              </text>
            </g>
          );
        })}

        {layout.nodes.map((n, i) =>
          n.mark ? (
            <g key={`m-${i}`}>
              <circle
                cx={n.x}
                cy={n.y}
                r={9}
                className="fill-card stroke-neutral-900 dark:stroke-neutral-100"
                strokeWidth={1.5}
              />
              <text
                x={n.x}
                y={n.y + 4}
                fontSize={11}
                textAnchor="middle"
                className="fill-neutral-900 font-medium dark:fill-neutral-100"
              >
                {n.mark}
              </text>
            </g>
          ) : null,
        )}

        {layout.nodes
          .filter((n) => n.isTip)
          .map((n, i) => (
            <text
              key={`l-${i}`}
              x={n.x + (n.mark ? 15 : 8)}
              y={n.y + 4}
              fontSize={13}
              fill="currentColor"
            >
              {n.label}
            </text>
          ))}
      </svg>
    </div>
  );
}
