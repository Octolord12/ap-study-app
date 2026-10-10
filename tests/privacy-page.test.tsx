import fs from "node:fs";
import path from "node:path";
import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";
import PrivacyPage from "@/app/privacy/page";
import { MINIMUM_AGE } from "@/lib/age";
import { PARENT_LINK_DAYS } from "@/lib/share/constants";
import { CRAM_COOKIE, CRAM_DAYS } from "@/lib/study/cram-mode";

describe("privacy page", () => {
  it("renders its sections and a contact link that doesn't print the address", () => {
    const { container } = render(<PrivacyPage />);
    for (const label of ["What we collect", "Who can see it", "What we don't do", "Cookies and storage", "Your choices"]) {
      expect(screen.getByText(label)).toBeInTheDocument();
    }
    const link = screen.getByRole("link", { name: "Write to us about privacy" });
    expect(link.getAttribute("href")).toMatch(/^mailto:/);
    expect(container.textContent).not.toMatch(/@|gmail/i);
  });

  it("states the minimum age that signup enforces, and that no birth date is collected", () => {
    const { container } = render(<PrivacyPage />);
    expect(screen.getByText("Who it's for")).toBeInTheDocument();
    expect(container.textContent).toContain(`${MINIMUM_AGE} or older`);
    expect(container.textContent).toMatch(/don't ask for your birth\s+date/);
  });

  it("says a student can change their password and delete their account in Settings, and no longer says it is by request", () => {
    const { container } = render(<PrivacyPage />);
    expect(container.textContent).toMatch(/Change your password, or delete your account and everything tied to it, in Settings/);
    expect(container.textContent).not.toMatch(/There is no button/);
  });

  it("says the password-reset email exists, that only a fingerprint of its code is kept, and who sends it", () => {
    const { container } = render(<PrivacyPage />);
    expect(container.textContent).toMatch(/ask to reset your password: your email address is used to send you a one-time link that works for an hour/);
    expect(container.textContent).toMatch(/only a fingerprint of the link's code/);
    expect(container.textContent).toContain("Resend");
  });

  it("lists the exam date among what is collected, since it is stored", () => {
    const { container } = render(<PrivacyPage />);
    expect(container.textContent).toMatch(/set an exam date for a course: that date/);
  });

  it("says that a timed exam's answers are kept on the device, since they are", () => {
    const { container } = render(<PrivacyPage />);
    expect(container.textContent).toMatch(/timed exam it also keeps your answers/);
    expect(container.textContent).toMatch(/removed when you submit/);
  });

  it("describes the parent link as it really works: what it shows, what it never shows, how long it lasts, and that the student controls it", () => {
    const { container } = render(<PrivacyPage />);
    const text = container.textContent ?? "";
    expect(text).toMatch(/A link you make for a parent shows whoever has it a read-only summary of your study/);
    expect(text).toMatch(/never shows your name, your email, your answers, your friends or your classes/);
    expect(text).toContain(`It works for ${PARENT_LINK_DAYS} days, or until you turn it off`);
    expect(text).toMatch(/make or turn off a link for a parent, in Settings/);
  });

  it("says what is stored about a parent link and a class block, and that the link's secret is not kept", () => {
    const { container } = render(<PrivacyPage />);
    const text = container.textContent ?? "";
    expect(text).toMatch(/a fingerprint of the link's secret. We don't keep the secret itself/);
    expect(text).toMatch(/a class owner blocks you from rejoining their class, a record of that block/);
    expect(text).toMatch(/block them from rejoining, and sees the usernames of the people they blocked/);
  });

  it("describes the cookie the app really sets, and for as long as it really lasts", () => {
    const { container } = render(<PrivacyPage />);
    expect(container.textContent).toContain(CRAM_COOKIE);
    expect(container.textContent).toContain(`${CRAM_DAYS} days`);
  });

  // The page says there is no tracking. If you add one, update the page first.
  it("is still true that no analytics or tracking package is installed", () => {
    const pkg = JSON.parse(fs.readFileSync(path.resolve(import.meta.dirname, "../package.json"), "utf8"));
    const installed = Object.keys({ ...pkg.dependencies, ...pkg.devDependencies });
    const tracking = ["@vercel/analytics", "@vercel/speed-insights", "posthog-js", "react-ga4", "react-ga", "@sentry/nextjs", "@sentry/browser", "mixpanel-browser", "@segment/analytics-next", "@amplitude/analytics-browser", "logrocket", "hotjar"];
    expect(installed.filter((name) => tracking.includes(name))).toEqual([]);
  });
});
