import { render, screen } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";
import { Choice, ChoiceRow } from "@/components/ui/choice";

describe("Choice letters", () => {
  it("shows the displayed letter but submits the authored label", () => {
    const onSelect = vi.fn();
    render(<Choice name="q" label="A" displayLabel="C" textHtml="<p>answer text</p>" checked={false} revealed={false} onSelect={onSelect} />);
    const radio = screen.getByRole("radio");
    expect(radio).toHaveAttribute("value", "A");
    expect(screen.getByText("C.")).toBeInTheDocument();
    expect(screen.queryByText("A.")).not.toBeInTheDocument();
  });

  it("falls back to the label when no displayLabel is given (authored order)", () => {
    render(<Choice name="q" label="B" textHtml="<p>x</p>" checked={false} revealed={false} onSelect={() => {}} />);
    expect(screen.getByText("B.")).toBeInTheDocument();
  });

  it("review rows show the displayed letter too", () => {
    render(<ChoiceRow label="D" displayLabel="A" textHtml="<p>x</p>" />);
    expect(screen.getByText("A.")).toBeInTheDocument();
  });
});
