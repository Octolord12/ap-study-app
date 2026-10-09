import { fireEvent, render, screen, waitFor } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";
import { DeleteClassButton } from "@/components/social/delete-class-button";

const TRIGGER = "Delete the class Period 3";

function renderButton(memberCount: number, action = vi.fn(async () => {})) {
  render(<DeleteClassButton name="Period 3" memberCount={memberCount} action={action} />);
  return action;
}

describe("DeleteClassButton", () => {
  it("names the class on the button and reads 'Delete class', not the removal wording the shared button defaults to", () => {
    renderButton(3);
    expect(screen.getByRole("button", { name: TRIGGER }).textContent).toBe("Delete class");
  });

  it("does nothing on the first click, only asks, and says it cannot be undone and nobody's answers are touched", () => {
    const action = renderButton(3);
    fireEvent.click(screen.getByRole("button", { name: TRIGGER }));
    expect(action).not.toHaveBeenCalled();
    expect(screen.getByText(/This cannot be undone/)).toBeTruthy();
    expect(screen.getByText(/Nobody's\s+answers or XP are touched/)).toBeTruthy();
  });

  it("says how many other people lose the class, with the right grammar for one, several and none", () => {
    const { unmount } = render(<DeleteClassButton name="Period 3" memberCount={4} action={vi.fn(async () => {})} />);
    fireEvent.click(screen.getByRole("button", { name: TRIGGER }));
    expect(screen.getByText(/The 3 other people in it lose the class/)).toBeTruthy();
    unmount();

    const two = render(<DeleteClassButton name="Period 3" memberCount={2} action={vi.fn(async () => {})} />);
    fireEvent.click(screen.getByRole("button", { name: TRIGGER }));
    expect(screen.getByText(/The 1 other person in it loses the class/)).toBeTruthy();
    two.unmount();

    render(<DeleteClassButton name="Period 3" memberCount={1} action={vi.fn(async () => {})} />);
    fireEvent.click(screen.getByRole("button", { name: TRIGGER }));
    expect(screen.getByText(/You lose the class/)).toBeTruthy();
  });

  it("runs the action once on confirmation", async () => {
    const action = renderButton(3);
    fireEvent.click(screen.getByRole("button", { name: TRIGGER }));
    fireEvent.click(screen.getByRole("button", { name: "Yes, delete it" }));
    await waitFor(() => expect(action).toHaveBeenCalledTimes(1));
  });

  it("'Keep' goes back without running anything", () => {
    const action = renderButton(3);
    fireEvent.click(screen.getByRole("button", { name: TRIGGER }));
    fireEvent.click(screen.getByRole("button", { name: "Keep" }));
    expect(screen.getByRole("button", { name: TRIGGER })).toBeTruthy();
    expect(action).not.toHaveBeenCalled();
  });

  it("says nothing was changed, in its own words, when the action fails", async () => {
    renderButton(
      3,
      vi.fn(async () => {
        throw new Error("boom");
      }),
    );
    fireEvent.click(screen.getByRole("button", { name: TRIGGER }));
    fireEvent.click(screen.getByRole("button", { name: "Yes, delete it" }));
    expect((await screen.findByRole("alert")).textContent).toBe("Could not delete the class. Nothing was changed; try again.");
  });
});
