import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";

// The reset flow against an in-memory database, the real after-response helper (with Next's `after`
// replaced by something we can await) and a fake mailer. What matters: the answer to "send me a link"
// is the same for every address, a link works once and for an hour, and a bad link or password
// changes nothing.

const mocks = vi.hoisted(() => {
  const state = {
    users: [] as { id: string; email: string; passwordHash: string | null }[],
    tokens: [] as { id: string; userId: string; tokenHash: string; minuteSlot: number; expiresAt: Date; usedAt: Date | null; createdAt: Date }[],
    deferred: [] as (() => Promise<void>)[],
    sent: [] as { to: string; subject: string; text: string }[],
    notified: [] as string[],
    nextId: 1,
  };
  const matches = (row: Record<string, unknown>, where: Record<string, unknown>): boolean =>
    Object.entries(where).every(([key, cond]) => {
      const value = row[key];
      if (cond !== null && typeof cond === "object" && !(cond instanceof Date)) {
        const c = cond as { gt?: Date; lt?: Date; not?: unknown; equals?: string; mode?: string };
        if (c.not !== undefined) return value !== c.not;
        if (c.gt) return (value as Date) > c.gt;
        if (c.lt) return (value as Date) < c.lt;
        if (c.equals !== undefined) return c.mode === "insensitive" ? String(value).toLowerCase() === c.equals.toLowerCase() : value === c.equals;
      }
      return value === cond;
    });
  const db = {
    user: {
      findFirst: vi.fn(async ({ where }: { where: Record<string, unknown> }) => state.users.find((u) => matches(u, where)) ?? null),
      update: vi.fn(async ({ where, data }: { where: { id: string }; data: { passwordHash: string } }) => {
        const user = state.users.find((u) => u.id === where.id)!;
        user.passwordHash = data.passwordHash;
        return { email: user.email };
      }),
    },
    passwordResetToken: {
      count: vi.fn(async ({ where }: { where: Record<string, unknown> }) => state.tokens.filter((t) => matches(t, where)).length),
      create: vi.fn(async ({ data }: { data: { userId: string; tokenHash: string; expiresAt: Date; minuteSlot: number } }) => {
        // What the unique (userId, minuteSlot) index does in Postgres.
        if (state.tokens.some((t) => t.userId === data.userId && t.minuteSlot === data.minuteSlot)) throw Object.assign(new Error("Unique constraint failed"), { code: "P2002" });
        state.tokens.push({ id: `t${state.nextId++}`, ...data, usedAt: null, createdAt: new Date() });
        return {};
      }),
      updateMany: vi.fn(async ({ where, data }: { where: Record<string, unknown>; data: { usedAt: Date } }) => {
        const hits = state.tokens.filter((t) => matches(t, where));
        hits.forEach((t) => (t.usedAt = data.usedAt));
        return { count: hits.length };
      }),
      deleteMany: vi.fn(async ({ where }: { where: Record<string, unknown> }) => {
        const before = state.tokens.length;
        state.tokens = state.tokens.filter((t) => !matches(t, where));
        return { count: before - state.tokens.length };
      }),
      findUnique: vi.fn(async ({ where }: { where: { tokenHash: string } }) => state.tokens.find((t) => t.tokenHash === where.tokenHash) ?? null),
    },
  };
  return { state, db };
});

vi.mock("@/lib/db", () => ({ getDb: () => mocks.db }));
// Next runs `after` work once the response is out; here it waits until the test calls flush().
vi.mock("next/server", () => ({
  after: (task: () => Promise<void>) => {
    mocks.state.deferred.push(task);
  },
}));
vi.mock("@/lib/email/send", () => ({
  sendEmail: vi.fn(async (m: { to: string; subject: string; text: string }) => {
    mocks.state.sent.push(m);
  }),
}));
vi.mock("@/lib/email/notify", () => ({ notifyPasswordChanged: (email: string) => mocks.state.notified.push(email) }));
vi.mock("bcryptjs", () => ({ default: { hash: vi.fn(async (pw: string) => `hashed:${pw}`) } }));

import { requestPasswordResetAction, resetPasswordAction } from "@/lib/auth/reset-actions";
import { RESET_LINK_INVALID } from "@/lib/auth/reset-constants";
import { hashResetToken } from "@/lib/auth/reset-token";
import { isResetLinkUsable } from "@/lib/auth/reset-queries";

const env = process.env as Record<string, string | undefined>;
const form = (fields: Record<string, string>) => {
  const data = new FormData();
  for (const [k, v] of Object.entries(fields)) data.set(k, v);
  return data;
};
// Run everything deferred so far, all at once like simultaneous requests would, and wait for it.
const flush = async () => {
  const tasks = mocks.state.deferred;
  mocks.state.deferred = [];
  await Promise.all(tasks.map((task) => task()));
};
const ask = (email: string) => requestPasswordResetAction({}, form({ email }));
// The raw code only ever exists in the emailed link.
const tokenFromLastEmail = () => {
  const last = mocks.state.sent[mocks.state.sent.length - 1];
  return /token=([A-Za-z0-9_-]{43})/.exec(last.text)![1];
};
const reset = (token: string, over: Record<string, string> = {}) =>
  resetPasswordAction({}, form({ token, newPassword: "brand-new-pass", confirmPassword: "brand-new-pass", ...over }));

beforeEach(() => {
  vi.clearAllMocks();
  vi.useFakeTimers({ toFake: ["Date"] });
  vi.setSystemTime(new Date("2026-10-05T12:00:00Z"));
  mocks.state.users = [
    { id: "u1", email: "Sam@Example.com", passwordHash: "hashed:old-password" },
    { id: "u2", email: "nopass@example.com", passwordHash: null },
  ];
  mocks.state.tokens = [];
  mocks.state.deferred = [];
  mocks.state.sent = [];
  mocks.state.notified = [];
  env.RESEND_API_KEY = "key";
  env.EMAIL_FROM = "noreply@example.org";
  env.SITE_URL = "https://site.example";
});
afterEach(() => {
  vi.useRealTimers();
  delete env.RESEND_API_KEY;
  delete env.EMAIL_FROM;
  delete env.SITE_URL;
});

describe("requestPasswordResetAction", () => {
  it("gives the same answer for a registered and an unregistered address", async () => {
    const known = await ask("sam@example.com");
    const unknown = await ask("nobody@example.com");
    expect(known).toEqual({ sent: true, values: { email: "sam@example.com" } });
    expect(unknown).toEqual({ sent: true, values: { email: "nobody@example.com" } });
    await flush();
  });

  it("does all the work that depends on the account after the response, so timing says nothing either", async () => {
    await ask("sam@example.com");
    expect(mocks.db.user.findFirst).not.toHaveBeenCalled();
    await flush();
    expect(mocks.db.user.findFirst).toHaveBeenCalledTimes(1);
  });

  it("emails a registered address a link built from configuration, and stores only the hash of its code", async () => {
    await ask("SAM@example.com"); // the lookup ignores case
    await flush();

    expect(mocks.state.sent).toHaveLength(1);
    expect(mocks.state.sent[0].to).toBe("Sam@Example.com");
    expect(mocks.state.sent[0].text).toContain("https://site.example/reset-password?token=");
    const token = tokenFromLastEmail();
    expect(mocks.state.tokens).toHaveLength(1);
    expect(mocks.state.tokens[0].tokenHash).toBe(hashResetToken(token));
    expect(JSON.stringify(mocks.state.tokens)).not.toContain(token);
    expect(mocks.state.tokens[0].expiresAt.getTime()).toBe(Date.now() + 60 * 60_000);
  });

  it("sends nothing for an unknown address or an account that has no password", async () => {
    await ask("nobody@example.com");
    await ask("nopass@example.com");
    await flush();
    expect(mocks.state.sent).toEqual([]);
    expect(mocks.state.tokens).toEqual([]);
  });

  it("answers a malformed address with an error, without looking anything up", async () => {
    expect(await ask("not-an-email")).toEqual({ error: "Enter a valid email", values: { email: "not-an-email" } });
    await flush();
    expect(mocks.db.user.findFirst).not.toHaveBeenCalled();
  });

  it("lets a burst of simultaneous requests through exactly once: the database allows one link a minute", async () => {
    for (let i = 0; i < 25; i++) await ask("sam@example.com");
    await flush(); // all 25 run at the same moment
    expect(mocks.state.sent).toHaveLength(1);
    expect(mocks.state.tokens).toHaveLength(1);
  });

  it("allows 3 an hour, one a minute, then starts again once the hour is up", async () => {
    for (let minute = 0; minute < 5; minute++) {
      vi.setSystemTime(new Date(Date.UTC(2026, 9, 5, 12, minute, 0)));
      await ask("sam@example.com");
      await flush();
    }
    expect(mocks.state.sent).toHaveLength(3);

    vi.setSystemTime(new Date("2026-10-05T13:01:00Z"));
    await ask("sam@example.com");
    await flush();
    expect(mocks.state.sent).toHaveLength(4);
  });

  it("doesn't retire the older link when the new request is the one that got dropped", async () => {
    await ask("sam@example.com");
    await flush();
    const first = tokenFromLastEmail();
    await ask("sam@example.com"); // same minute: dropped
    await flush();
    expect(await reset(first)).toEqual({ done: true });
  });

  it("retires the older link when a newer one is requested", async () => {
    await ask("sam@example.com");
    await flush();
    const first = tokenFromLastEmail();
    vi.setSystemTime(new Date("2026-10-05T12:01:00Z"));
    await ask("sam@example.com");
    await flush();
    const second = tokenFromLastEmail();
    expect(first).not.toBe(second);
    expect(await reset(first)).toEqual({ error: RESET_LINK_INVALID });
    expect(await reset(second)).toEqual({ done: true });
  });

  it("clears out rows older than a day", async () => {
    mocks.state.tokens.push({ id: "old", userId: "u1", tokenHash: "x", minuteSlot: 1, expiresAt: new Date("2026-10-03T00:00:00Z"), usedAt: null, createdAt: new Date("2026-10-03T00:00:00Z") });
    await ask("sam@example.com");
    await flush();
    expect(mocks.state.tokens.find((t) => t.id === "old")).toBeUndefined();
  });

  it("a failing mail provider doesn't change the answer, and nothing leaks into the logs", async () => {
    const { sendEmail } = await import("@/lib/email/send");
    vi.mocked(sendEmail).mockRejectedValueOnce(new Error("Email provider answered 500"));
    const logged = vi.spyOn(console, "error").mockImplementation(() => {});
    expect(await ask("sam@example.com")).toEqual({ sent: true, values: { email: "sam@example.com" } });
    await flush();
    expect(logged).toHaveBeenCalledWith("background task failed:", "Error");
    expect(JSON.stringify(logged.mock.calls)).not.toContain("sam@example.com");
    logged.mockRestore();
  });

  it("is unavailable in production until email is configured", async () => {
    delete env.RESEND_API_KEY;
    env.NODE_ENV = "production";
    expect(await ask("sam@example.com")).toEqual({ error: "Password reset isn't available yet." });
    await flush();
    expect(mocks.db.user.findFirst).not.toHaveBeenCalled();
    env.NODE_ENV = "test";
  });
});

describe("resetPasswordAction", () => {
  async function linkFor(email = "sam@example.com") {
    await ask(email);
    await flush();
    return tokenFromLastEmail();
  }

  it("sets the new password, uses the link up, and tells the account's address", async () => {
    const token = await linkFor();
    expect(await reset(token)).toEqual({ done: true });
    expect(mocks.state.users[0].passwordHash).toBe("hashed:brand-new-pass");
    expect(mocks.state.tokens.every((t) => t.usedAt !== null)).toBe(true);
    expect(mocks.state.notified).toEqual(["Sam@Example.com"]);
  });

  it("works once: the same link a second time is refused and changes nothing", async () => {
    const token = await linkFor();
    await reset(token);
    mocks.state.users[0].passwordHash = "hashed:chosen-later";
    expect(await reset(token, { newPassword: "another-pass-1", confirmPassword: "another-pass-1" })).toEqual({ error: RESET_LINK_INVALID });
    expect(mocks.state.users[0].passwordHash).toBe("hashed:chosen-later");
  });

  it("refuses a link after its hour is up", async () => {
    const token = await linkFor();
    vi.setSystemTime(new Date("2026-10-05T13:00:01Z"));
    expect(await reset(token)).toEqual({ error: RESET_LINK_INVALID });
    expect(mocks.state.users[0].passwordHash).toBe("hashed:old-password");
  });

  it("refuses a code that was never issued, and junk, without touching the database for junk", async () => {
    expect(await reset("A".repeat(43))).toEqual({ error: RESET_LINK_INVALID });
    expect(await reset("short")).toEqual({ error: RESET_LINK_INVALID });
    expect(mocks.db.passwordResetToken.findUnique).toHaveBeenCalledTimes(1);
    expect(mocks.state.users[0].passwordHash).toBe("hashed:old-password");
  });

  it("keeps the link alive when the new password is rejected, so the person can fix it and try again", async () => {
    const token = await linkFor();
    expect(await reset(token, { confirmPassword: "different" })).toEqual({ error: "The new passwords don't match." });
    expect(await reset(token, { newPassword: "short", confirmPassword: "short" })).toEqual({ error: "At least 8 characters" });
    expect(await reset(token, { newPassword: "é".repeat(37), confirmPassword: "é".repeat(37) })).toEqual({ error: "That password is too long. Use a shorter one." });
    expect(mocks.state.tokens[0].usedAt).toBeNull();
    expect(await reset(token)).toEqual({ done: true });
  });

  it("lets only one of two simultaneous submissions of the same link through", async () => {
    const token = await linkFor();
    const results = await Promise.all([reset(token, { newPassword: "first-choice-1", confirmPassword: "first-choice-1" }), reset(token, { newPassword: "second-choice-2", confirmPassword: "second-choice-2" })]);
    expect(results.filter((r) => r.done)).toHaveLength(1);
    expect(results.filter((r) => r.error === RESET_LINK_INVALID)).toHaveLength(1);
    expect(mocks.state.notified).toHaveLength(1);
  });

  it("never returns a password or a code to the browser", async () => {
    const token = await linkFor();
    const bad = await reset(token, { confirmPassword: "different" });
    const ok = await reset(token);
    for (const result of [bad, ok]) {
      expect(JSON.stringify(result)).not.toContain("brand-new-pass");
      expect(JSON.stringify(result)).not.toContain(token);
    }
  });
});

describe("isResetLinkUsable", () => {
  it("is true for a fresh link and false once it is used, expired, unknown or malformed", async () => {
    await ask("sam@example.com");
    await flush();
    const token = tokenFromLastEmail();
    expect(await isResetLinkUsable(token)).toBe(true);
    expect(await isResetLinkUsable("A".repeat(43))).toBe(false);
    expect(await isResetLinkUsable("nope")).toBe(false);
    expect(await isResetLinkUsable(undefined)).toBe(false);

    vi.setSystemTime(new Date("2026-10-05T13:00:01Z"));
    expect(await isResetLinkUsable(token)).toBe(false);

    vi.setSystemTime(new Date("2026-10-05T12:00:30Z"));
    expect(await isResetLinkUsable(token)).toBe(true);
    await reset(token);
    expect(await isResetLinkUsable(token)).toBe(false);
  });
});
