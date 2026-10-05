import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";
import { SiteFooter } from "@/components/site-footer";

describe("SiteFooter", () => {
  it("keeps the trademark and non-affiliation notice and says questions may contain mistakes", () => {
    const { container } = render(<SiteFooter />);
    expect(container.textContent).toMatch(/registered trademarks of College Board/);
    expect(container.textContent).toMatch(/not affiliated with this site/);
    expect(container.textContent).toMatch(/not been reviewed by College Board and\s+may contain mistakes/);
  });

  it("links to a prefilled email without ever showing the address", () => {
    const { container } = render(<SiteFooter />);
    const link = screen.getByRole("link", { name: "Report a mistake or send a suggestion" });
    expect(link.getAttribute("href")).toMatch(/^mailto:/);
    expect(link.getAttribute("href")).toContain("subject=");
    expect(container.textContent).not.toMatch(/@|gmail/i);
  });

  it("links to the about page", () => {
    render(<SiteFooter />);
    expect(screen.getByRole("link", { name: "About" })).toHaveAttribute("href", "/about");
  });

  it("links to the privacy page", () => {
    render(<SiteFooter />);
    expect(screen.getByRole("link", { name: "Privacy" })).toHaveAttribute("href", "/privacy");
  });
});
