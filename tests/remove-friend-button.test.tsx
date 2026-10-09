import { fireEvent, render, screen, waitFor } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";
import { RemoveFriendButton } from "@/components/social/remove-friend-button";

describe("RemoveFriendButton", () => {
  it("names the friend on the button, so a list of them is not a row of identical 'Remove's", () => {
    render(<RemoveFriendButton username="alice" action={vi.fn(async () => {})} />);
    expect(screen.getByRole("button", { name: "Remove alice from your friends" })).toBeTruthy();
  });

  it("does nothing on the first click, only asks", () => {
    const action = vi.fn(async () => {});
    render(<RemoveFriendButton username="alice" action={action} />);
    fireEvent.click(screen.getByRole("button", { name: "Remove alice from your friends" }));
    expect(action).not.toHaveBeenCalled();
    expect(screen.getByText(/from your friends\? To add them again you would send a new request/)).toBeTruthy();
  });

  it("runs the action once on confirmation", async () => {
    const action = vi.fn(async () => {});
    render(<RemoveFriendButton username="alice" action={action} />);
    fireEvent.click(screen.getByRole("button", { name: "Remove alice from your friends" }));
    fireEvent.click(screen.getByRole("button", { name: "Yes, remove" }));
    await waitFor(() => expect(action).toHaveBeenCalledTimes(1));
  });

  it("'Keep' goes back without running anything", () => {
    const action = vi.fn(async () => {});
    render(<RemoveFriendButton username="alice" action={action} />);
    fireEvent.click(screen.getByRole("button", { name: "Remove alice from your friends" }));
    fireEvent.click(screen.getByRole("button", { name: "Keep" }));
    expect(screen.getByRole("button", { name: "Remove alice from your friends" })).toBeTruthy();
    expect(action).not.toHaveBeenCalled();
  });

  it("says nothing was changed when the action fails, and lets the person retry", async () => {
    const action = vi.fn(async () => {
      throw new Error("boom");
    });
    render(<RemoveFriendButton username="alice" action={action} />);
    fireEvent.click(screen.getByRole("button", { name: "Remove alice from your friends" }));
    fireEvent.click(screen.getByRole("button", { name: "Yes, remove" }));
    expect((await screen.findByRole("alert")).textContent).toMatch(/Nothing was changed/);
    expect(screen.getByRole("button", { name: "Yes, remove" })).toBeTruthy();
  });
});
