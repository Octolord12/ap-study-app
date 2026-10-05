import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";
import { Testimonials } from "@/components/marketing/testimonials";
import { TESTIMONIALS } from "@/lib/marketing/testimonials";

describe("Testimonials", () => {
  it("renders nothing while there are no real testimonials", () => {
    const { container } = render(<Testimonials items={[]} />);
    expect(container).toBeEmptyDOMElement();
  });

  it("only ships testimonials that have a quote and a name", () => {
    for (const t of TESTIMONIALS) {
      expect(t.quote.trim().length).toBeGreaterThan(0);
      expect(t.name.trim().length).toBeGreaterThan(0);
    }
  });

  it("shows a real quote exactly as given, with no invented score or course", () => {
    const quote = TESTIMONIALS.find((t) => t.name === "Phu Vo");
    expect(quote?.quote).toBe("Wait this is actually tuff. I actually might use it later.");
    expect(quote?.apScore).toBeUndefined();
    expect(quote?.course).toBeUndefined();
  });

  it("shows the quote and attribution, and the score only when one is given", () => {
    render(
      <Testimonials
        items={[
          { quote: "The explanations are why I stopped repeating mistakes.", name: "Test A.", course: "AP Calculus AB", apScore: 5 },
          { quote: "Short and useful.", name: "Test B." },
        ]}
      />,
    );
    expect(screen.getByText(/stopped repeating mistakes/)).toBeInTheDocument();
    expect(screen.getByText(/Test A\. · AP Calculus AB · Scored 5/)).toBeInTheDocument();
    expect(screen.getByText("Test B.")).toBeInTheDocument();
    expect(screen.queryAllByText(/Scored/)).toHaveLength(1);
  });
});
