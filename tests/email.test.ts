import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import { isEmailConfigured, isPasswordResetAvailable, siteUrl } from "@/lib/email/config";
import { sendEmail } from "@/lib/email/send";
import { passwordChangedEmail, passwordResetEmail } from "@/lib/email/templates";

const ENV_KEYS = ["RESEND_API_KEY", "EMAIL_FROM", "EMAIL_REPLY_TO", "SITE_URL", "NEXT_PUBLIC_SITE_URL", "NODE_ENV"] as const;
const saved: Record<string, string | undefined> = {};
const env = process.env as Record<string, string | undefined>;

beforeEach(() => {
  for (const k of ENV_KEYS) {
    saved[k] = env[k];
    delete env[k];
  }
});
afterEach(() => {
  for (const k of ENV_KEYS) {
    if (saved[k] === undefined) delete env[k];
    else env[k] = saved[k];
  }
  vi.restoreAllMocks();
  vi.unstubAllGlobals();
});

describe("config", () => {
  it("takes links from configuration, not from a request, and trims a trailing slash", () => {
    expect(siteUrl()).toBe("https://ap-study-app-pi.vercel.app");
    env.NEXT_PUBLIC_SITE_URL = "https://example.org/";
    expect(siteUrl()).toBe("https://example.org");
    env.SITE_URL = "https://site.example";
    expect(siteUrl()).toBe("https://site.example");
  });

  it("is configured only with both a key and a sender", () => {
    expect(isEmailConfigured()).toBe(false);
    env.RESEND_API_KEY = "key";
    expect(isEmailConfigured()).toBe(false);
    env.EMAIL_FROM = "AP Study App <noreply@example.org>";
    expect(isEmailConfigured()).toBe(true);
  });

  it("offers password reset in production only once email works, and always in development", () => {
    env.NODE_ENV = "production";
    expect(isPasswordResetAvailable()).toBe(false);
    env.RESEND_API_KEY = "key";
    env.EMAIL_FROM = "x@example.org";
    expect(isPasswordResetAvailable()).toBe(true);
    delete env.RESEND_API_KEY;
    env.NODE_ENV = "development";
    expect(isPasswordResetAvailable()).toBe(true);
  });
});

describe("sendEmail", () => {
  const message = { to: "sam@example.com", subject: "Subject", text: "Text body", html: "<p>Html body</p>" };

  it("posts to Resend with the key as a bearer token and the sender from configuration", async () => {
    env.RESEND_API_KEY = "re_test_key";
    env.EMAIL_FROM = "AP Study App <noreply@example.org>";
    env.EMAIL_REPLY_TO = "owner@example.org";
    const fetchMock = vi.fn(async () => new Response("{}", { status: 200 }));
    vi.stubGlobal("fetch", fetchMock);

    await sendEmail(message);

    const [url, init] = fetchMock.mock.calls[0] as unknown as [string, RequestInit];
    expect(url).toBe("https://api.resend.com/emails");
    expect((init.headers as Record<string, string>).Authorization).toBe("Bearer re_test_key");
    expect(JSON.parse(String(init.body))).toEqual({
      from: "AP Study App <noreply@example.org>",
      to: ["sam@example.com"],
      subject: "Subject",
      text: "Text body",
      html: "<p>Html body</p>",
      reply_to: "owner@example.org",
    });
  });

  it("throws on a failed send without putting the address or body in the error", async () => {
    env.RESEND_API_KEY = "k";
    env.EMAIL_FROM = "x@example.org";
    vi.stubGlobal("fetch", vi.fn(async () => new Response('{"message":"sam@example.com is invalid"}', { status: 422 })));
    const error = await sendEmail(message).catch((e: Error) => e);
    expect((error as Error).message).toBe("Email provider answered 422");
    expect((error as Error).message).not.toContain("sam@example.com");
  });

  it("without configuration, sends nothing and prints the message in development only", async () => {
    const fetchMock = vi.fn();
    vi.stubGlobal("fetch", fetchMock);
    const info = vi.spyOn(console, "info").mockImplementation(() => {});

    env.NODE_ENV = "development";
    await sendEmail(message);
    expect(info).toHaveBeenCalledTimes(1);

    info.mockClear();
    env.NODE_ENV = "production";
    await sendEmail(message);
    expect(info).not.toHaveBeenCalled();
    expect(fetchMock).not.toHaveBeenCalled();
  });
});

describe("templates", () => {
  it("puts the reset link, its lifetime and a 'not you' line in both the text and html parts", () => {
    const url = "https://example.org/reset-password?token=abc_DEF-123";
    const mail = passwordResetEmail("sam@example.com", url);
    expect(mail.to).toBe("sam@example.com");
    expect(mail.text).toContain(url);
    expect(mail.html).toContain(url);
    expect(mail.text).toMatch(/60 minutes/);
    expect(mail.text).toMatch(/ignore this email/);
    expect(mail.text).not.toContain("—");
  });

  it("escapes anything that ends up in the html", () => {
    const mail = passwordResetEmail("a@b.c", 'https://x.test/?a="1"&b=<script>');
    expect(mail.html).not.toContain("<script>");
    expect(mail.html).toContain("&lt;script&gt;");
    expect(mail.html).toContain("&quot;1&quot;");
  });

  it("the changed-password notice points at the configured site, not the request", () => {
    env.SITE_URL = "https://site.example";
    const mail = passwordChangedEmail("sam@example.com");
    expect(mail.text).toContain("https://site.example/forgot-password");
    expect(mail.subject).toBe("Your AP Study App password was changed");
  });
});
