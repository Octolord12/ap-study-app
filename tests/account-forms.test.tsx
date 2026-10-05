import { fireEvent, render, screen, waitFor } from "@testing-library/react";
import { beforeEach, describe, expect, it, vi } from "vitest";

const actions = vi.hoisted(() => ({ changePasswordAction: vi.fn(), deleteAccountAction: vi.fn() }));
vi.mock("@/lib/auth/account-actions", () => actions);

import { ChangePasswordForm } from "@/components/account/change-password-form";
import { DeleteAccountForm } from "@/components/account/delete-account-form";

describe("ChangePasswordForm", () => {
  beforeEach(() => vi.clearAllMocks());

  it("asks for the current password and the new one twice, as password fields", () => {
    render(<ChangePasswordForm />);
    for (const label of ["Current password", "New password", "New password again"]) {
      expect(screen.getByLabelText(label)).toHaveAttribute("type", "password");
      expect(screen.getByLabelText(label)).toBeRequired();
    }
    expect(screen.getByLabelText("New password")).toHaveAttribute("autocomplete", "new-password");
  });

  it("shows the server's error, and leaves every password field empty afterwards", async () => {
    actions.changePasswordAction.mockResolvedValue({ error: "That isn't your current password." });
    render(<ChangePasswordForm />);
    fireEvent.change(screen.getByLabelText("Current password"), { target: { value: "wrong-one" } });
    fireEvent.change(screen.getByLabelText("New password"), { target: { value: "brand-new-pass" } });
    fireEvent.change(screen.getByLabelText("New password again"), { target: { value: "brand-new-pass" } });
    fireEvent.submit(screen.getByLabelText("Current password").closest("form")!);

    await waitFor(() => expect(screen.getByRole("alert")).toHaveTextContent("That isn't your current password."));
    for (const label of ["Current password", "New password", "New password again"]) expect((screen.getByLabelText(label) as HTMLInputElement).value).toBe("");
  });

  it("confirms a change", async () => {
    actions.changePasswordAction.mockResolvedValue({ message: "Password changed." });
    render(<ChangePasswordForm />);
    fireEvent.submit(screen.getByLabelText("Current password").closest("form")!);
    await waitFor(() => expect(screen.getByRole("status")).toHaveTextContent("Password changed."));
  });
});

describe("DeleteAccountForm", () => {
  beforeEach(() => vi.clearAllMocks());

  it("lists what is deleted, says it can't be undone, and needs the password and a tick", () => {
    render(<DeleteAccountForm ownedClasses={[]} />);
    expect(screen.getByText(/your waitlist signup, if you used the same email/)).toBeInTheDocument();
    expect(screen.getByText(/can.t be undone/)).toBeInTheDocument();
    expect(screen.getByLabelText("Your password")).toBeRequired();
    expect(screen.getByRole("checkbox", { name: /I understand my account and its data will be deleted for good/ })).toBeRequired();
    expect(screen.getByRole("button", { name: "Delete my account" })).toBeInTheDocument();
    expect(screen.queryByRole("note")).not.toBeInTheDocument();
  });

  it("warns, with numbers, that an owned class is deleted for the other students in it", () => {
    render(<DeleteAccountForm ownedClasses={[{ id: "c1", name: "Period 3 AP CSA", otherMembers: 4 }]} />);
    expect(screen.getByRole("note")).toHaveTextContent("You own a class (Period 3 AP CSA). Classes can't be handed over, so deleting your account deletes it for everyone in it: 4 other students.");
  });

  it("handles several classes, one other student, and a class with nobody else in it", () => {
    const { unmount } = render(
      <DeleteAccountForm
        ownedClasses={[
          { id: "a", name: "A", otherMembers: 1 },
          { id: "b", name: "B", otherMembers: 0 },
        ]}
      />,
    );
    expect(screen.getByRole("note")).toHaveTextContent("You own 2 classes (A, B). Classes can't be handed over, so deleting your account deletes them for everyone in them: 1 other student.");
    unmount();
    render(<DeleteAccountForm ownedClasses={[{ id: "a", name: "Solo", otherMembers: 0 }]} />);
    expect(screen.getByRole("note")).toHaveTextContent("deletes it, though nobody else is in it.");
  });

  it("shows the server's error and clears the password field", async () => {
    actions.deleteAccountAction.mockResolvedValue({ error: "That isn't your password." });
    render(<DeleteAccountForm ownedClasses={[]} />);
    fireEvent.change(screen.getByLabelText("Your password"), { target: { value: "nope" } });
    fireEvent.submit(screen.getByLabelText("Your password").closest("form")!);
    await waitFor(() => expect(screen.getByRole("alert")).toHaveTextContent("That isn't your password."));
    expect((screen.getByLabelText("Your password") as HTMLInputElement).value).toBe("");
  });
});
