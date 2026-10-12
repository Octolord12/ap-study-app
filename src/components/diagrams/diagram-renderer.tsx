import type { Diagram } from "@/lib/content/diagram-schema";
import { XYGraph } from "./xy-graph";
import { ForceDiagram } from "./force-diagram";
import { DataTable } from "./data-table";
import { BarGraph } from "./bar-graph";
import { Cladogram } from "./cladogram";

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
  }
}
