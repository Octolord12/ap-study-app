import { render, screen } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";

vi.mock("@/lib/marketing/actions", () => ({ joinWaitlist: vi.fn() }));

import { ComingSoon } from "@/components/marketing/coming-soon";

describe("ComingSoon", () => {
  it("keeps the waitlist and says that nothing is planned, now that every subject we planned is built", () => {
    render(<ComingSoon />);
    expect(screen.getByText("More subjects")).toBeInTheDocument();
    expect(screen.getByText(/None planned yet/)).toBeInTheDocument();
    expect(screen.queryByText("Planned")).not.toBeInTheDocument();
    for (const shipped of ["AP Biology", "AP U.S. History", "AP Calculus BC"]) {
      expect(screen.queryByText(shipped)).not.toBeInTheDocument();
    }
    expect(screen.getByLabelText("Email")).toBeInTheDocument();
    expect(screen.getByRole("button", { name: "Join the list" })).toBeInTheDocument();
  });

  it("tells people the minimum age for the waitlist", () => {
    render(<ComingSoon />);
    expect(screen.getByText(/You must be 13 or older/)).toBeInTheDocument();
  });

  it("does not refer to other parts of the page, since it appears on two different pages", () => {
    const { container } = render(<ComingSoon />);
    expect(container.textContent).not.toMatch(/\babove\b|\bbelow\b/i);
  });
});
