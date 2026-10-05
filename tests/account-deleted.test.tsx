import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";
import AccountDeletedPage, { metadata } from "@/app/account-deleted/page";

describe("account deleted page", () => {
  it("confirms the deletion and points back home", () => {
    render(<AccountDeletedPage />);
    expect(screen.getByRole("heading", { name: "Your account has been deleted." })).toBeInTheDocument();
    expect(screen.getByRole("link", { name: "Back to the home page" })).toHaveAttribute("href", "/");
  });

  it("is not for search engines", () => {
    expect(metadata.robots).toEqual({ index: false });
  });
});
