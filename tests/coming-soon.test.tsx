import { render, screen } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";

vi.mock("@/lib/marketing/actions", () => ({ joinWaitlist: vi.fn() }));

import { ComingSoon } from "@/components/marketing/coming-soon";

describe("ComingSoon", () => {
  it("is headed 'Coming soon', lists the planned subjects, and has the waitlist form", () => {
    render(<ComingSoon />);
    expect(screen.getByText("Coming soon")).toBeInTheDocument();
    for (const subject of ["AP U.S. History", "AP Biology", "AP Calculus BC"]) {
      expect(screen.getByText(subject)).toBeInTheDocument();
    }
    expect(screen.getAllByText("Planned")).toHaveLength(3);
    expect(screen.getByLabelText("Email")).toBeInTheDocument();
    expect(screen.getByRole("button", { name: "Join the list" })).toBeInTheDocument();
  });

  it("does not refer to other parts of the page, since it appears on two different pages", () => {
    const { container } = render(<ComingSoon />);
    expect(container.textContent).not.toMatch(/\babove\b|\bbelow\b/i);
  });
});
