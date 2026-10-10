import { fireEvent, render, screen, waitFor } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";
import { TransferOwnershipButton } from "@/components/social/transfer-ownership-button";

const TRIGGER = "Make alice the owner of this class";

describe("TransferOwnershipButton", () => {
  it("names the member on the button and reads 'Make owner'", () => {
    render(<TransferOwnershipButton username="alice" action={vi.fn(async () => {})} />);
    expect(screen.getByRole("button", { name: TRIGGER }).textContent).toBe("Make owner");
  });

  it("does nothing on the first click, only asks, and says what the current owner gives up", () => {
    const action = vi.fn(async () => {});
    render(<TransferOwnershipButton username="alice" action={action} />);
    fireEvent.click(screen.getByRole("button", { name: TRIGGER }));
    expect(action).not.toHaveBeenCalled();
    expect(screen.getByText(/You become a regular member/)).toBeTruthy();
    expect(screen.getByText(/They could hand it back/)).toBeTruthy();
  });

  it("runs the action once on confirmation", async () => {
    const action = vi.fn(async () => {});
    render(<TransferOwnershipButton username="alice" action={action} />);
    fireEvent.click(screen.getByRole("button", { name: TRIGGER }));
    fireEvent.click(screen.getByRole("button", { name: "Yes, hand it over" }));
    await waitFor(() => expect(action).toHaveBeenCalledTimes(1));
  });

  it("'Keep' goes back without running anything", () => {
    const action = vi.fn(async () => {});
    render(<TransferOwnershipButton username="alice" action={action} />);
    fireEvent.click(screen.getByRole("button", { name: TRIGGER }));
    fireEvent.click(screen.getByRole("button", { name: "Keep" }));
    expect(screen.getByRole("button", { name: TRIGGER })).toBeTruthy();
    expect(action).not.toHaveBeenCalled();
  });

  it("says nothing was changed, in its own words, when the action fails", async () => {
    const action = vi.fn(async () => {
      throw new Error("boom");
    });
    render(<TransferOwnershipButton username="alice" action={action} />);
    fireEvent.click(screen.getByRole("button", { name: TRIGGER }));
    fireEvent.click(screen.getByRole("button", { name: "Yes, hand it over" }));
    expect((await screen.findByRole("alert")).textContent).toBe("Could not hand the class over. Nothing was changed; try again.");
  });
});
