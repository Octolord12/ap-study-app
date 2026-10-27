import type { Diagram } from "@/lib/content/diagram-schema";
import { XYGraph } from "./xy-graph";
import { ForceDiagram } from "./force-diagram";
import { DataTable } from "./data-table";
import { BarGraph } from "./bar-graph";
import { Boxplot } from "./boxplot";
import { Cladogram } from "./cladogram";
import { DensityCurve } from "./density-curve";
import { Dotplot } from "./dotplot";
import { Histogram } from "./histogram";
import { Scatterplot } from "./scatterplot";

export function DiagramRenderer({ diagram }: { diagram: Diagram }) {
  switch (diagram.type) {
    case "xy-graph":
      return <XYGraph diagram={diagram} />;
    case "force-diagram":
      return <ForceDiagram diagram={diagram} />;
    case "data-table":
      return <DataTable diagram={diagram} />;
    case "bar-graph":
      return <BarGraph diagram={diagram} />;
    case "cladogram":
      return <Cladogram diagram={diagram} />;
    case "histogram":
      return <Histogram diagram={diagram} />;
    case "boxplot":
      return <Boxplot diagram={diagram} />;
    case "dotplot":
      return <Dotplot diagram={diagram} />;
    case "scatterplot":
      return <Scatterplot diagram={diagram} />;
    case "density-curve":
      return <DensityCurve diagram={diagram} />;
  }
}
