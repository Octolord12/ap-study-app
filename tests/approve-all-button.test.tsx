import { fireEvent, render, screen, waitFor } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";
import { ApproveAllButton } from "@/components/admin/approve-all-button";

describe("ApproveAllButton", () => {
  it("does nothing on the first click, only asks", () => {
    const action = vi.fn(async () => ({ approved: 12 }));
    render(<ApproveAllButton count={12} action={action} />);
    fireEvent.click(screen.getByRole("button", { name: "Approve all 12 in this unit" }));
    expect(action).not.toHaveBeenCalled();
    expect(screen.getByText(/Mark all 12 items below as checked by a person/)).toBeTruthy();
  });

  it("runs the action once on confirmation", async () => {
    const action = vi.fn(async () => ({ approved: 12 }));
    render(<ApproveAllButton count={12} action={action} />);
    fireEvent.click(screen.getByRole("button", { name: "Approve all 12 in this unit" }));
    fireEvent.click(screen.getByRole("button", { name: "Yes, approve all 12" }));
    await waitFor(() => expect(action).toHaveBeenCalledTimes(1));
  });

  it("cancel goes back without running anything", () => {
    const action = vi.fn(async () => ({ approved: 0 }));
    render(<ApproveAllButton count={3} action={action} />);
    fireEvent.click(screen.getByRole("button", { name: "Approve all 3 in this unit" }));
    fireEvent.click(screen.getByRole("button", { name: "Cancel" }));
    expect(screen.getByRole("button", { name: "Approve all 3 in this unit" })).toBeTruthy();
    expect(action).not.toHaveBeenCalled();
  });

  it("says nothing was changed when the action fails, and lets the person retry", async () => {
    const action = vi.fn(async () => {
      throw new Error("boom");
    });
    render(<ApproveAllButton count={1} action={action} />);
    fireEvent.click(screen.getByRole("button", { name: "Approve all 1 in this unit" }));
    fireEvent.click(screen.getByRole("button", { name: "Yes, approve all 1" }));
    expect((await screen.findByRole("alert")).textContent).toMatch(/Nothing was changed/);
    expect(screen.getByRole("button", { name: "Yes, approve all 1" })).toBeTruthy();
  });

  it("uses the singular for one item", () => {
    render(<ApproveAllButton count={1} action={vi.fn(async () => ({}))} />);
    fireEvent.click(screen.getByRole("button", { name: "Approve all 1 in this unit" }));
    expect(screen.getByText(/Mark all 1 item below/)).toBeTruthy();
  });
});
