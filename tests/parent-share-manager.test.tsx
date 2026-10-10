import { fireEvent, render, screen, waitFor } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";
import { ParentShareManager, type ParentShareStatus } from "@/components/share/parent-share-manager";

const ACTIVE: ParentShareStatus = { created: "October 9, 2026", expires: "January 7, 2027", lastViewed: null };

function setup(over: { active?: ParentShareStatus | null; create?: () => Promise<{ url: string }>; revoke?: () => Promise<void> } = {}) {
  const create = vi.fn(over.create ?? (async () => ({ url: "https://study.example/share/abc" })));
  const revoke = vi.fn(over.revoke ?? (async () => {}));
  render(<ParentShareManager active={over.active === undefined ? null : over.active} days={90} createAction={create} revokeAction={revoke} />);
  return { create, revoke };
}

describe("ParentShareManager", () => {
  it("explains what is shared, what is not, the 90 days, and that anyone with the link can open it", () => {
    setup();
    const text = document.body.textContent ?? "";
    expect(text).toMatch(/your username, not your name or email/);
    expect(text).toMatch(/none of your answers, friends or classes/);
    expect(text).toMatch(/90 days, or until you turn it off/);
    expect(text).toMatch(/Anyone who has the link can open it/);
  });

  it("with no link: says so, and offers only 'Make a link'", () => {
    setup();
    expect(screen.getByRole("status").textContent).toBe("No link is on.");
    expect(screen.getByRole("button", { name: "Make a link" })).toBeTruthy();
    expect(screen.queryByRole("button", { name: "Turn off" })).toBeNull();
  });

  it("with a live link: shows when it was made, when it ends and that it has not been opened, and offers a new one or turning it off", () => {
    setup({ active: ACTIVE });
    expect(screen.getByRole("status").textContent).toBe("A link is on. Made October 9, 2026, works until January 7, 2027. Not opened yet.");
    expect(screen.getByRole("button", { name: "Make a new link" })).toBeTruthy();
    expect(screen.getByRole("button", { name: "Turn off" })).toBeTruthy();
    expect(screen.getByText("Making a new link turns the old one off.")).toBeTruthy();
  });

  it("says when the link was last opened", () => {
    setup({ active: { ...ACTIVE, lastViewed: "October 12, 2026" } });
    expect(screen.getByRole("status").textContent).toContain("Last opened October 12, 2026.");
  });

  it("shows the new link once, in a box that is selectable, with a way to copy it", async () => {
    const { create } = setup();
    fireEvent.click(screen.getByRole("button", { name: "Make a link" }));
    const box = (await screen.findByLabelText(/Your link/)) as HTMLInputElement;
    expect(create).toHaveBeenCalledTimes(1);
    expect(box.value).toBe("https://study.example/share/abc");
    expect(box.readOnly).toBe(true);
    expect(screen.getByText(/shown only now/i)).toBeTruthy();
  });

  it("copies the link to the clipboard and says so", async () => {
    const writeText = vi.fn(async () => {});
    Object.assign(navigator, { clipboard: { writeText } });
    setup();
    fireEvent.click(screen.getByRole("button", { name: "Make a link" }));
    await screen.findByLabelText(/Your link/);
    fireEvent.click(screen.getByRole("button", { name: "Copy" }));
    await waitFor(() => expect(writeText).toHaveBeenCalledWith("https://study.example/share/abc"));
    expect(await screen.findByRole("button", { name: "Copied" })).toBeTruthy();
  });

  it("does not claim 'Copied' when the browser refuses the clipboard", async () => {
    Object.assign(navigator, { clipboard: { writeText: vi.fn(async () => { throw new Error("denied"); }) } });
    setup();
    fireEvent.click(screen.getByRole("button", { name: "Make a link" }));
    await screen.findByLabelText(/Your link/);
    fireEvent.click(screen.getByRole("button", { name: "Copy" }));
    await waitFor(() => expect(screen.getByRole("button", { name: "Copy" })).toBeTruthy());
    expect(screen.queryByRole("button", { name: "Copied" })).toBeNull();
  });

  it("turning it off runs the revoke action and clears a link that was on screen", async () => {
    const { revoke } = setup({ active: ACTIVE });
    fireEvent.click(screen.getByRole("button", { name: "Make a new link" }));
    await screen.findByLabelText(/Your link/);
    fireEvent.click(screen.getByRole("button", { name: "Turn off" }));
    await waitFor(() => expect(revoke).toHaveBeenCalledTimes(1));
    await waitFor(() => expect(screen.queryByLabelText(/Your link/)).toBeNull());
  });

  it("says nothing was changed, and shows no link, when making one fails", async () => {
    setup({
      create: async () => {
        throw new Error("boom");
      },
    });
    fireEvent.click(screen.getByRole("button", { name: "Make a link" }));
    expect((await screen.findByRole("alert")).textContent).toBe("Could not make a link. Nothing was changed; try again.");
    expect(screen.queryByLabelText(/Your link/)).toBeNull();
    expect(screen.getByRole("button", { name: "Make a link" })).toBeTruthy();
  });

  it("says so when turning it off fails", async () => {
    setup({
      active: ACTIVE,
      revoke: async () => {
        throw new Error("boom");
      },
    });
    fireEvent.click(screen.getByRole("button", { name: "Turn off" }));
    expect((await screen.findByRole("alert")).textContent).toBe("Could not turn the link off. Try again.");
  });
});
