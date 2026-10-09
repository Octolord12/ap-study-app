import { fireEvent, render, screen, waitFor } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";
import { RegenerateInviteCodeButton } from "@/components/social/regenerate-invite-code-button";

const TRIGGER = "Make a new invite code for this class";

describe("RegenerateInviteCodeButton", () => {
  it("reads 'New code', not the removal wording the shared button defaults to", () => {
    render(<RegenerateInviteCodeButton action={vi.fn(async () => {})} />);
    expect(screen.getByRole("button", { name: TRIGGER }).textContent).toBe("New code");
  });

  it("does nothing on the first click, only asks, and says the old code stops working and members stay", () => {
    const action = vi.fn(async () => {});
    render(<RegenerateInviteCodeButton action={action} />);
    fireEvent.click(screen.getByRole("button", { name: TRIGGER }));
    expect(action).not.toHaveBeenCalled();
    expect(screen.getByText(/The current one stops working right away/)).toBeTruthy();
    expect(screen.getByText(/People already in the class stay/)).toBeTruthy();
  });

  it("runs the action once on confirmation", async () => {
    const action = vi.fn(async () => {});
    render(<RegenerateInviteCodeButton action={action} />);
    fireEvent.click(screen.getByRole("button", { name: TRIGGER }));
    fireEvent.click(screen.getByRole("button", { name: "Yes, make a new code" }));
    await waitFor(() => expect(action).toHaveBeenCalledTimes(1));
  });

  it("'Keep' goes back without running anything", () => {
    const action = vi.fn(async () => {});
    render(<RegenerateInviteCodeButton action={action} />);
    fireEvent.click(screen.getByRole("button", { name: TRIGGER }));
    fireEvent.click(screen.getByRole("button", { name: "Keep" }));
    expect(screen.getByRole("button", { name: TRIGGER })).toBeTruthy();
    expect(action).not.toHaveBeenCalled();
  });

  it("says nothing was changed, in its own words, when the action fails", async () => {
    const action = vi.fn(async () => {
      throw new Error("boom");
    });
    render(<RegenerateInviteCodeButton action={action} />);
    fireEvent.click(screen.getByRole("button", { name: TRIGGER }));
    fireEvent.click(screen.getByRole("button", { name: "Yes, make a new code" }));
    expect((await screen.findByRole("alert")).textContent).toBe("Could not change the code. Nothing was changed; try again.");
  });
});
