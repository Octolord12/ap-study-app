import { fireEvent, render, screen, waitFor } from "@testing-library/react";
import { beforeEach, describe, expect, it, vi } from "vitest";

const actions = vi.hoisted(() => ({ loginAction: vi.fn(), signUpAction: vi.fn() }));
vi.mock("@/lib/auth/actions", () => actions);

import { LoginForm } from "@/components/auth/login-form";
import { SignupForm } from "@/components/auth/signup-form";

const field = (label: string) => screen.getByLabelText(label) as HTMLInputElement;

describe("auth forms keep what was typed after a rejected submit", () => {
  beforeEach(() => vi.clearAllMocks());

  it("login: keeps the email, empties the password, shows the error", async () => {
    actions.loginAction.mockResolvedValue({ error: "Incorrect email or password.", values: { email: "sam@example.com" } });
    render(<LoginForm />);

    fireEvent.change(field("Email"), { target: { value: "sam@example.com" } });
    fireEvent.change(field("Password"), { target: { value: "not-the-password" } });
    fireEvent.submit(field("Email").closest("form")!);

    await waitFor(() => expect(screen.getByRole("alert")).toHaveTextContent("Incorrect email or password."));
    expect(field("Email").value).toBe("sam@example.com");
    expect(field("Password").value).toBe("");
  });

  it("signup: keeps name, username, email and the age box; empties the password", async () => {
    actions.signUpAction.mockResolvedValue({
      error: "That username is taken.",
      values: { displayName: "Sam Student", username: "sam_s", email: "sam@example.com", ageConfirmed: true },
    });
    render(<SignupForm />);

    fireEvent.change(field("Your name"), { target: { value: "Sam Student" } });
    fireEvent.change(field("Username"), { target: { value: "sam_s" } });
    fireEvent.change(field("Email"), { target: { value: "sam@example.com" } });
    fireEvent.change(field("Password"), { target: { value: "long-enough-pw" } });
    fireEvent.click(screen.getByRole("checkbox", { name: "I am 13 or older." }));
    fireEvent.submit(field("Email").closest("form")!);

    await waitFor(() => expect(screen.getByRole("alert")).toHaveTextContent("That username is taken."));
    expect(field("Your name").value).toBe("Sam Student");
    expect(field("Username").value).toBe("sam_s");
    expect(field("Email").value).toBe("sam@example.com");
    expect(screen.getByRole("checkbox", { name: "I am 13 or older." })).toBeChecked();
    expect(field("Password").value).toBe("");
  });
});
