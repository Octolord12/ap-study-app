import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";
import { ReportProblem } from "@/components/study/report-problem";

describe("ReportProblem", () => {
  it("is a mail link that names the question and never shows an address", () => {
    const { container } = render(<ReportProblem id="ap-calc-u1-mcq-4" />);
    const link = screen.getByRole("link", { name: "Report a problem with this question" });
    expect(link.getAttribute("href")).toMatch(/^mailto:/);
    expect(decodeURIComponent(link.getAttribute("href")!)).toContain("ap-calc-u1-mcq-4");
    expect(container.textContent).not.toMatch(/@|gmail/i);
  });

  it("says 'prompt' for a free-response prompt", () => {
    render(<ReportProblem id="ap-calc-u1-frq-1" kind="free-response prompt" />);
    expect(screen.getByRole("link", { name: "Report a problem with this prompt" })).toBeInTheDocument();
  });
});
