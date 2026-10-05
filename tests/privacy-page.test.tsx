import fs from "node:fs";
import path from "node:path";
import { render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";
import PrivacyPage from "@/app/privacy/page";
import { MINIMUM_AGE } from "@/lib/age";
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

  it("says that a timed exam's answers are kept on the device, since they are", () => {
    const { container } = render(<PrivacyPage />);
    expect(container.textContent).toMatch(/timed exam it also keeps your answers/);
    expect(container.textContent).toMatch(/removed when you submit/);
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
