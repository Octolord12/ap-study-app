import { fireEvent, render, screen, waitFor } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";
import { RemoveClassMemberButton } from "@/components/social/remove-class-member-button";

describe("RemoveClassMemberButton", () => {
  it("names the member and the class on the button, so a list of them is not a row of identical 'Remove's", () => {
    render(<RemoveClassMemberButton username="alice" action={vi.fn(async () => {})} blockAction={vi.fn(async () => {})} />);
    expect(screen.getByRole("button", { name: "Remove alice from this class" })).toBeTruthy();
  });

  it("does nothing on the first click, only asks, and says they can rejoin with the invite code", () => {
    const action = vi.fn(async () => {});
    render(<RemoveClassMemberButton username="alice" action={action} blockAction={vi.fn(async () => {})} />);
    fireEvent.click(screen.getByRole("button", { name: "Remove alice from this class" }));
    expect(action).not.toHaveBeenCalled();
    expect(screen.getByText(/lets\s+them join again with the invite code/)).toBeTruthy();
  });

  it("runs the action once on confirmation", async () => {
    const action = vi.fn(async () => {});
    render(<RemoveClassMemberButton username="alice" action={action} blockAction={vi.fn(async () => {})} />);
    fireEvent.click(screen.getByRole("button", { name: "Remove alice from this class" }));
    fireEvent.click(screen.getByRole("button", { name: "Yes, remove" }));
    await waitFor(() => expect(action).toHaveBeenCalledTimes(1));
  });

  it("'Keep' goes back without running anything", () => {
    const action = vi.fn(async () => {});
    render(<RemoveClassMemberButton username="alice" action={action} blockAction={vi.fn(async () => {})} />);
    fireEvent.click(screen.getByRole("button", { name: "Remove alice from this class" }));
    fireEvent.click(screen.getByRole("button", { name: "Keep" }));
    expect(screen.getByRole("button", { name: "Remove alice from this class" })).toBeTruthy();
    expect(action).not.toHaveBeenCalled();
  });

  it("says nothing was changed when the action fails", async () => {
    const action = vi.fn(async () => {
      throw new Error("boom");
    });
    render(<RemoveClassMemberButton username="alice" action={action} blockAction={vi.fn(async () => {})} />);
    fireEvent.click(screen.getByRole("button", { name: "Remove alice from this class" }));
    fireEvent.click(screen.getByRole("button", { name: "Yes, remove" }));
    expect((await screen.findByRole("alert")).textContent).toMatch(/Nothing was changed/);
  });

  it("offers 'Remove and block' as a second way to confirm, which runs the block action and not the plain one", async () => {
    const action = vi.fn(async () => {});
    const blockAction = vi.fn(async () => {});
    render(<RemoveClassMemberButton username="alice" action={action} blockAction={blockAction} />);
    fireEvent.click(screen.getByRole("button", { name: "Remove alice from this class" }));
    fireEvent.click(screen.getByRole("button", { name: "Remove and block" }));
    await waitFor(() => expect(blockAction).toHaveBeenCalledTimes(1));
    expect(action).not.toHaveBeenCalled();
  });

  it("'Yes, remove' runs only the plain action", async () => {
    const action = vi.fn(async () => {});
    const blockAction = vi.fn(async () => {});
    render(<RemoveClassMemberButton username="alice" action={action} blockAction={blockAction} />);
    fireEvent.click(screen.getByRole("button", { name: "Remove alice from this class" }));
    fireEvent.click(screen.getByRole("button", { name: "Yes, remove" }));
    await waitFor(() => expect(action).toHaveBeenCalledTimes(1));
    expect(blockAction).not.toHaveBeenCalled();
  });

  it("says nothing was changed when blocking fails, and lets the person try again", async () => {
    const blockAction = vi.fn(async () => {
      throw new Error("boom");
    });
    render(<RemoveClassMemberButton username="alice" action={vi.fn(async () => {})} blockAction={blockAction} />);
    fireEvent.click(screen.getByRole("button", { name: "Remove alice from this class" }));
    fireEvent.click(screen.getByRole("button", { name: "Remove and block" }));
    expect((await screen.findByRole("alert")).textContent).toMatch(/Nothing was changed/);
    expect(screen.getByRole("button", { name: "Remove and block" })).toBeTruthy();
  });
});
