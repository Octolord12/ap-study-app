import { fireEvent, render, screen, waitFor } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";
import { RemoveClassMemberButton } from "@/components/social/remove-class-member-button";

describe("RemoveClassMemberButton", () => {
  it("names the member and the class on the button, so a list of them is not a row of identical 'Remove's", () => {
    render(<RemoveClassMemberButton username="alice" action={vi.fn(async () => {})} />);
    expect(screen.getByRole("button", { name: "Remove alice from this class" })).toBeTruthy();
  });

  it("does nothing on the first click, only asks, and says they can rejoin with the invite code", () => {
    const action = vi.fn(async () => {});
    render(<RemoveClassMemberButton username="alice" action={action} />);
    fireEvent.click(screen.getByRole("button", { name: "Remove alice from this class" }));
    expect(action).not.toHaveBeenCalled();
    expect(screen.getByText(/anyone with the invite code can\s+join again/)).toBeTruthy();
  });

  it("runs the action once on confirmation", async () => {
    const action = vi.fn(async () => {});
    render(<RemoveClassMemberButton username="alice" action={action} />);
    fireEvent.click(screen.getByRole("button", { name: "Remove alice from this class" }));
    fireEvent.click(screen.getByRole("button", { name: "Yes, remove" }));
    await waitFor(() => expect(action).toHaveBeenCalledTimes(1));
  });

  it("'Keep' goes back without running anything", () => {
    const action = vi.fn(async () => {});
    render(<RemoveClassMemberButton username="alice" action={action} />);
    fireEvent.click(screen.getByRole("button", { name: "Remove alice from this class" }));
    fireEvent.click(screen.getByRole("button", { name: "Keep" }));
    expect(screen.getByRole("button", { name: "Remove alice from this class" })).toBeTruthy();
    expect(action).not.toHaveBeenCalled();
  });

  it("says nothing was changed when the action fails", async () => {
    const action = vi.fn(async () => {
      throw new Error("boom");
    });
    render(<RemoveClassMemberButton username="alice" action={action} />);
    fireEvent.click(screen.getByRole("button", { name: "Remove alice from this class" }));
    fireEvent.click(screen.getByRole("button", { name: "Yes, remove" }));
    expect((await screen.findByRole("alert")).textContent).toMatch(/Nothing was changed/);
  });
});
