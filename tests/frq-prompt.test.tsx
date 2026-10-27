import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";
import { FrqPrompt } from "@/components/study/frq-prompt";
import type { DataTableDiagram } from "@/lib/content/diagram-schema";

const table: DataTableDiagram = { type: "data-table", caption: "Results table", columns: ["Trial", "Rate"], rows: [["1", 2]], rowHeaders: false };
const follows = (a: Node, b: Node) => Boolean(a.compareDocumentPosition(b) & Node.DOCUMENT_POSITION_FOLLOWING);

describe("FrqPrompt", () => {
  it("puts the figure between the set-up text and the lettered parts", () => {
    render(<FrqPrompt prompt={{ introHtml: "<p>Set-up</p>", partsHtml: "<p>Part A</p>" }} diagram={table} />);
    expect(follows(screen.getByText("Set-up"), screen.getByRole("table"))).toBe(true);
    expect(follows(screen.getByRole("table"), screen.getByText("Part A"))).toBe(true);
  });

  it("puts a figure after the text of a prompt that could not be split", () => {
    render(<FrqPrompt prompt={{ introHtml: "<p>The whole prompt</p>", partsHtml: "" }} diagram={table} />);
    expect(follows(screen.getByText("The whole prompt"), screen.getByRole("table"))).toBe(true);
  });

  it("shows the parts even when there is no figure", () => {
    render(<FrqPrompt prompt={{ introHtml: "<p>Set-up</p>", partsHtml: "<p>Part A</p>" }} diagram={null} />);
    expect(screen.queryByRole("table")).toBeNull();
    expect(screen.getByText("Part A")).toBeInTheDocument();
  });

  it("applies the class to the first block only", () => {
    const { container } = render(<FrqPrompt prompt={{ introHtml: "<p>Set-up</p>", partsHtml: "<p>Part A</p>" }} diagram={table} className="mt-2" />);
    expect(container.querySelectorAll(".mt-2")).toHaveLength(1);
  });
});
