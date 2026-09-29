import type { Diagram } from "@/lib/content/diagram-schema";
import { XYGraph } from "./xy-graph";
import { ForceDiagram } from "./force-diagram";

export function DiagramRenderer({ diagram }: { diagram: Diagram }) {
  switch (diagram.type) {
    case "xy-graph":
      return <XYGraph diagram={diagram} />;
    case "force-diagram":
      return <ForceDiagram diagram={diagram} />;
  }
}
