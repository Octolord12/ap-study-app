import { beforeEach, describe, expect, it, vi } from "vitest";

// grantTeacherRole and revokeTeacherRole against an in-memory user table that honors the query's meaning (the id, the *current role*, the
// case-insensitive username), so the tests show what they can NOT change: an admin's role, or anyone not in the role being changed. The fake
// throws on a filter it does not understand, so a new condition can't be silently ignored.

type Row = { id: string; username: string; role: "STUDENT" | "TEACHER" | "ADMIN" };

const mocks = vi.hoisted(() => {
  const state = { isAdmin: true, rows: [] as { id: string; username: string; role: "STUDENT" | "TEACHER" | "ADMIN" }[] };
  const db = {
    user: {
      findFirst: vi.fn(async ({ where }: { where: { username: { equals: string; mode: string } } }) => {
        if (Object.keys(where).join() !== "username" || where.username.mode !== "insensitive") throw new Error("fake does not understand this where");
        return state.rows.find((r) => r.username.toLowerCase() === where.username.equals.toLowerCase()) ?? null;
      }),
      updateMany: vi.fn(async ({ where, data }: { where: { id?: string; role?: string }; data: { role: Row["role"] } }) => {
        for (const k of Object.keys(where)) if (k !== "id" && k !== "role") throw new Error(`fake does not understand where.${k}`);
        let count = 0;
        for (const r of state.rows) {
          if ((where.id !== undefined && r.id !== where.id) || (where.role !== undefined && r.role !== where.role)) continue;
          r.role = data.role;
          count++;
        }
        return { count };
      }),
    },
  };
  return { state, db, revalidatePath: vi.fn() };
});

vi.mock("@/lib/db", () => ({ getDb: () => mocks.db }));
vi.mock("next/cache", () => ({ revalidatePath: mocks.revalidatePath }));
vi.mock("next/navigation", () => ({
  redirect: (to: string) => {
    throw new Error(`redirect:${to}`);
  },
}));
vi.mock("@/lib/admin/session", () => ({
  requireAdminUserId: async () => {
    if (!mocks.state.isAdmin) throw new Error("NEXT_NOT_FOUND");
    return "admin1";
  },
}));

import { grantTeacherRole, revokeTeacherRole } from "@/lib/admin/actions";

const form = (username: string | null) => {
  const f = new FormData();
  if (username !== null) f.set("username", username);
  return f;
};
const roles = () => Object.fromEntries(mocks.state.rows.map((r: Row) => [r.username, r.role]));
async function grant(username: string | null) {
  try {
    await grantTeacherRole(form(username));
  } catch (e) {
    return (e as Error).message;
  }
  return "no redirect";
}

describe("grantTeacherRole", () => {
  beforeEach(() => {
    vi.clearAllMocks();
    mocks.state.isAdmin = true;
    mocks.state.rows = [
      { id: "s1", username: "Alice", role: "STUDENT" },
      { id: "s2", username: "bob", role: "STUDENT" },
      { id: "t1", username: "carol", role: "TEACHER" },
      { id: "a1", username: "viraj1", role: "ADMIN" },
    ];
  });

  it("makes a student a teacher and says who", async () => {
    expect(await grant("bob")).toBe("redirect:/admin/teachers?granted=bob");
    expect(roles().bob).toBe("TEACHER");
  });

  it("finds the username in any case, and trims it, like the friend search", async () => {
    expect(await grant("  aLiCe ")).toBe("redirect:/admin/teachers?granted=Alice");
    expect(roles().Alice).toBe("TEACHER");
  });

  it("changes only that account", async () => {
    await grant("bob");
    expect(roles()).toEqual({ Alice: "STUDENT", bob: "TEACHER", carol: "TEACHER", viraj1: "ADMIN" });
  });

  it("never touches an admin: it says so, and the role stays ADMIN", async () => {
    expect(await grant("viraj1")).toBe("redirect:/admin/teachers?error=admin");
    expect(roles().viraj1).toBe("ADMIN");
  });

  it("says when the account is a teacher already, and for an unknown or blank username changes nothing", async () => {
    expect(await grant("carol")).toBe("redirect:/admin/teachers?error=already");
    expect(await grant("nobody")).toBe("redirect:/admin/teachers?error=not-found");
    expect(await grant("   ")).toBe("redirect:/admin/teachers?error=missing");
    expect(await grant(null)).toBe("redirect:/admin/teachers?error=missing");
    expect(roles()).toEqual({ Alice: "STUDENT", bob: "STUDENT", carol: "TEACHER", viraj1: "ADMIN" });
  });

  it("scopes the write to a STUDENT, so a role that changed between the lookup and the write is not overwritten", async () => {
    await grant("bob");
    expect(mocks.db.user.updateMany.mock.calls[0][0].where).toEqual({ id: "s2", role: "STUDENT" });
  });

  it("is refused for anyone who is not an admin, and writes nothing", async () => {
    mocks.state.isAdmin = false;
    expect(await grant("bob")).toBe("NEXT_NOT_FOUND");
    expect(mocks.db.user.updateMany).not.toHaveBeenCalled();
    expect(roles().bob).toBe("STUDENT");
  });

  it("encodes the username in the redirect", async () => {
    mocks.state.rows.push({ id: "s3", username: "a&b=c", role: "STUDENT" });
    expect(await grant("a&b=c")).toBe("redirect:/admin/teachers?granted=a%26b%3Dc");
  });
});

// revokeTeacherRole ends in redirect(); the mock turns that into a throw so the destination can be asserted.
async function revoke(userId: string) {
  try {
    await revokeTeacherRole(userId);
  } catch (e) {
    return (e as Error).message;
  }
  return "no redirect";
}

describe("revokeTeacherRole", () => {
  beforeEach(() => {
    vi.clearAllMocks();
    mocks.state.isAdmin = true;
    mocks.state.rows = [
      { id: "s1", username: "alice", role: "STUDENT" },
      { id: "t1", username: "carol", role: "TEACHER" },
      { id: "a1", username: "viraj1", role: "ADMIN" },
    ];
  });

  it("takes the teacher role away: the account is a student again", async () => {
    await revoke("t1");
    expect(roles().carol).toBe("STUDENT");
    expect(mocks.revalidatePath).toHaveBeenCalledWith("/admin/teachers");
  });

  it("returns to the bare page, so a 'was made a teacher' message from an earlier grant does not linger (found in the browser)", async () => {
    expect(await revoke("t1")).toBe("redirect:/admin/teachers");
  });

  it("can never demote an admin, nor change a student", async () => {
    await revoke("a1");
    await revoke("s1");
    await revoke("nobody");
    expect(roles()).toEqual({ alice: "STUDENT", carol: "TEACHER", viraj1: "ADMIN" });
  });

  it("is refused for anyone who is not an admin, and writes nothing", async () => {
    mocks.state.isAdmin = false;
    expect(await revoke("t1")).toBe("NEXT_NOT_FOUND");
    expect(mocks.db.user.updateMany).not.toHaveBeenCalled();
    expect(roles().carol).toBe("TEACHER");
  });
});
