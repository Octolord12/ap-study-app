import { render, screen } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";

vi.mock("@/lib/marketing/actions", () => ({ joinWaitlist: vi.fn() }));

import { ComingSoon } from "@/components/marketing/coming-soon";

describe("ComingSoon", () => {
  it("is headed 'Coming soon', lists the planned subjects, and has the waitlist form", () => {
    render(<ComingSoon />);
    expect(screen.getByText("Coming soon")).toBeInTheDocument();
    expect(screen.getByText("AP Biology")).toBeInTheDocument();
    expect(screen.getAllByText("Planned")).toHaveLength(1);
    for (const shipped of ["AP U.S. History", "AP Calculus BC"]) {
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
