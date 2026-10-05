import { beforeEach, describe, expect, it, vi } from "vitest";

// The real callbacks from config.ts, captured as NextAuth receives them, run against a
// faked users table: what matters here is which tokens survive a password change.
const mocks = vi.hoisted(() => ({
  config: null as null | {
    providers: { options?: { authorize?: unknown }; authorize?: unknown }[];
    callbacks: { jwt: (args: Record<string, unknown>) => Promise<Record<string, unknown> | null>; session: (args: Record<string, unknown>) => unknown };
  },
  users: new Map<string, { id: string; email: string; displayName: string; passwordHash: string | null }>(),
  findUnique: vi.fn(),
}));

vi.mock("next-auth", () => ({
  default: (config: unknown) => {
    mocks.config = config as typeof mocks.config;
    return { handlers: {}, auth: vi.fn(), signIn: vi.fn(), signOut: vi.fn() };
  },
}));
vi.mock("next-auth/providers/credentials", () => ({ default: (options: unknown) => ({ options, authorize: (options as { authorize: unknown }).authorize }) }));
vi.mock("@auth/prisma-adapter", () => ({ PrismaAdapter: () => ({}) }));
vi.mock("bcryptjs", () => ({ default: { compare: vi.fn(async (pw: string, hash: string) => hash === `hashed:${pw}`) } }));
vi.mock("@/lib/db", () => ({ getDb: () => ({ user: { findUnique: mocks.findUnique } }) }));

import "@/lib/auth/config";

type Authorize = (credentials: Record<string, string>) => Promise<{ id: string; stamp?: string } | null>;
const authorize = () => mocks.config!.providers[0].authorize as Authorize;
const jwt = (args: Record<string, unknown>) => mocks.config!.callbacks.jwt(args);

// What signing in does: authorize(), then the jwt callback with that user.
async function signIn(email: string, password: string) {
  const user = await authorize()({ email, password });
  expect(user).not.toBeNull();
  return (await jwt({ token: { name: "Sam" }, user }))!;
}

// What the change-password action does to the stored hash.
const setPassword = (id: string, password: string) => {
  mocks.users.get(id)!.passwordHash = `hashed:${password}`;
};

beforeEach(() => {
  mocks.users.clear();
  mocks.users.set("u1", { id: "u1", email: "sam@example.com", displayName: "Sam", passwordHash: "hashed:old-password" });
  mocks.users.set("u2", { id: "u2", email: "alex@example.com", displayName: "Alex", passwordHash: "hashed:other-password" });
  mocks.findUnique.mockReset();
  mocks.findUnique.mockImplementation(async ({ where }: { where: { id?: string; email?: string } }) => {
    const rows = [...mocks.users.values()];
    return (where.id ? rows.find((r) => r.id === where.id) : rows.find((r) => r.email === where.email)) ?? null;
  });
});

describe("signing in", () => {
  it("puts the user's id and a stamp of the password into the token", async () => {
    const token = await signIn("sam@example.com", "old-password");
    expect(token.id).toBe("u1");
    expect(token.stamp).toMatch(/^[0-9a-f]{24}$/);
  });

  it("never puts the password hash itself into the token", async () => {
    const token = await signIn("sam@example.com", "old-password");
    expect(JSON.stringify(token)).not.toContain("hashed:");
  });
});

describe("a signed-in device after the password changes elsewhere", () => {
  it("keeps working while nothing has changed", async () => {
    const token = await signIn("sam@example.com", "old-password");
    expect(await jwt({ token: { ...token } })).toMatchObject({ id: "u1", stamp: token.stamp });
  });

  it("is signed out on the next request once the password is changed", async () => {
    const phone = await signIn("sam@example.com", "old-password");
    const laptop = await signIn("sam@example.com", "old-password");

    setPassword("u1", "brand-new-password");
    // The device that made the change signs itself in again with the new password.
    const laptopAfter = await signIn("sam@example.com", "brand-new-password");

    expect(await jwt({ token: { ...phone } })).toBeNull();
    expect(await jwt({ token: { ...laptop } })).toBeNull();
    expect(await jwt({ token: { ...laptopAfter } })).toMatchObject({ id: "u1" });
  });

  it("is signed out even if the same password is saved again, because bcrypt gives it a new hash", async () => {
    const phone = await signIn("sam@example.com", "old-password");
    mocks.users.get("u1")!.passwordHash = "hashed:old-password-re-salted";
    expect(await jwt({ token: { ...phone } })).toBeNull();
  });

  it("only affects the account whose password changed", async () => {
    const sam = await signIn("sam@example.com", "old-password");
    const alex = await signIn("alex@example.com", "other-password");
    setPassword("u1", "brand-new-password");
    expect(await jwt({ token: { ...sam } })).toBeNull();
    expect(await jwt({ token: { ...alex } })).toMatchObject({ id: "u2" });
  });

  it("can't be revived by asking for a session update", async () => {
    const phone = await signIn("sam@example.com", "old-password");
    setPassword("u1", "brand-new-password");
    expect(await jwt({ token: { ...phone }, trigger: "update", session: { anything: true } })).toBeNull();
  });
});

describe("a signed-in device after the account is deleted", () => {
  it("is signed out", async () => {
    const phone = await signIn("sam@example.com", "old-password");
    mocks.users.delete("u1");
    expect(await jwt({ token: { ...phone } })).toBeNull();
  });
});

describe("a session from before stamps existed", () => {
  it("keeps working, and is stamped so a later password change does cover it", async () => {
    const legacy = { id: "u1", name: "Sam" };
    const stamped = await jwt({ token: { ...legacy } });
    expect(stamped).toMatchObject({ id: "u1" });
    expect(stamped!.stamp).toMatch(/^[0-9a-f]{24}$/);

    setPassword("u1", "brand-new-password");
    expect(await jwt({ token: { ...stamped! } })).toBeNull();
  });

  it("still ends when its account is gone", async () => {
    mocks.users.delete("u1");
    expect(await jwt({ token: { id: "u1" } })).toBeNull();
  });
});

describe("when the database can't be reached", () => {
  it("keeps the person signed in instead of signing everyone out, and logs only the kind of error", async () => {
    const token = await signIn("sam@example.com", "old-password");
    const log = vi.spyOn(console, "error").mockImplementation(() => {});
    mocks.findUnique.mockRejectedValueOnce(Object.assign(new Error("connect ECONNREFUSED postgres://secret@host"), { name: "PrismaClientInitializationError" }));

    expect(await jwt({ token: { ...token, id: "u1" } })).toMatchObject({ id: "u1" });
    expect(log).toHaveBeenCalledWith("session check failed", "PrismaClientInitializationError");
    expect(JSON.stringify(log.mock.calls)).not.toContain("secret");
    log.mockRestore();
  });
});

describe("a token with no user in it", () => {
  it("is passed through untouched rather than looked up", async () => {
    mocks.findUnique.mockClear();
    expect(await jwt({ token: { name: "x" } })).toEqual({ name: "x" });
    expect(mocks.findUnique).not.toHaveBeenCalled();
  });
});
