import { fireEvent, render, screen, waitFor } from "@testing-library/react";
import { beforeEach, describe, expect, it, vi } from "vitest";

const actions = vi.hoisted(() => ({ requestPasswordResetAction: vi.fn(), resetPasswordAction: vi.fn() }));
vi.mock("@/lib/auth/reset-actions", () => actions);
vi.mock("@/lib/auth/actions", () => ({ loginAction: vi.fn(), signUpAction: vi.fn() }));

import { ForgotPasswordForm } from "@/components/auth/forgot-password-form";
import { LoginForm } from "@/components/auth/login-form";
import { ResetPasswordForm } from "@/components/auth/reset-password-form";

const field = (label: string) => screen.getByLabelText(label) as HTMLInputElement;

describe("ForgotPasswordForm", () => {
  beforeEach(() => vi.clearAllMocks());

  it("after sending, says only that a link goes out if the address has an account", async () => {
    actions.requestPasswordResetAction.mockResolvedValue({ sent: true, values: { email: "sam@example.com" } });
    render(<ForgotPasswordForm />);
    fireEvent.change(field("Email"), { target: { value: "sam@example.com" } });
    fireEvent.submit(field("Email").closest("form")!);

    const note = await screen.findByRole("status");
    expect(note).toHaveTextContent("If sam@example.com has an account, we have sent a link");
    expect(note).toHaveTextContent("expires in 60 minutes");
    expect(note.textContent).not.toMatch(/no account|not registered|doesn't exist/i);
    expect(screen.getByRole("link", { name: "Back to log in" }).getAttribute("href")).toBe("/login");
  });

  it("keeps the email and shows the error for a malformed address", async () => {
    actions.requestPasswordResetAction.mockResolvedValue({ error: "Enter a valid email", values: { email: "sam@" } });
    render(<ForgotPasswordForm />);
    fireEvent.change(field("Email"), { target: { value: "sam@" } });
    fireEvent.submit(field("Email").closest("form")!);
    await waitFor(() => expect(screen.getByRole("alert")).toHaveTextContent("Enter a valid email"));
    expect(field("Email").value).toBe("sam@");
  });
});

describe("ResetPasswordForm", () => {
  beforeEach(() => vi.clearAllMocks());

  it("sends the code from the link along with the new password, and empties both password fields after an error", async () => {
    actions.resetPasswordAction.mockResolvedValue({ error: "The new passwords don't match." });
    const { container } = render(<ResetPasswordForm token={"T".repeat(43)} />);
    expect((container.querySelector('input[name="token"]') as HTMLInputElement).value).toBe("T".repeat(43));

    fireEvent.change(field("New password"), { target: { value: "brand-new-pass" } });
    fireEvent.change(field("New password again"), { target: { value: "different-pass" } });
    fireEvent.submit(field("New password").closest("form")!);

    await waitFor(() => expect(screen.getByRole("alert")).toHaveTextContent("The new passwords don't match."));
    expect(screen.getByRole("link", { name: "Ask for a new link" }).getAttribute("href")).toBe("/forgot-password");
    expect(field("New password").value).toBe("");
    expect(field("New password again").value).toBe("");
  });

  it("on success says other devices were signed out and offers the login", async () => {
    actions.resetPasswordAction.mockResolvedValue({ done: true });
    render(<ResetPasswordForm token={"T".repeat(43)} />);
    fireEvent.change(field("New password"), { target: { value: "brand-new-pass" } });
    fireEvent.change(field("New password again"), { target: { value: "brand-new-pass" } });
    fireEvent.submit(field("New password").closest("form")!);

    expect(await screen.findByRole("status")).toHaveTextContent("Your password is changed. Any device that was signed in has been signed out.");
    expect(screen.getByRole("link", { name: "Log in" }).getAttribute("href")).toBe("/login");
  });
});

describe("LoginForm", () => {
  it("offers 'Forgot your password?' only when told reset is available", () => {
    const { rerender } = render(<LoginForm />);
    expect(screen.queryByRole("link", { name: "Forgot your password?" })).toBeNull();
    rerender(<LoginForm showForgotPassword />);
    expect(screen.getByRole("link", { name: "Forgot your password?" }).getAttribute("href")).toBe("/forgot-password");
  });
});
