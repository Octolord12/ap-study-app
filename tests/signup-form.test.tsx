import { render, screen } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";

vi.mock("@/lib/auth/actions", () => ({ signUpAction: vi.fn() }));

import { SignupForm } from "@/components/auth/signup-form";

describe("SignupForm age confirmation", () => {
  it("has a required checkbox named by its label, submitted as 'yes'", () => {
    render(<SignupForm />);
    const box = screen.getByRole("checkbox", { name: "I am 13 or older." });
    expect(box).toBeRequired();
    expect(box).not.toBeChecked();
    expect(box).toHaveAttribute("name", "ageConfirmed");
    expect(box).toHaveAttribute("value", "yes");
  });
});
