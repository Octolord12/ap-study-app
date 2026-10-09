import { beforeEach, describe, expect, it, vi } from "vitest";

// renameClass against an in-memory class table that honors the query's meaning (the class id AND its owner), so the tests show who can NOT
// rename as well as who can. The fake throws on a filter it does not understand, so a new condition can't be silently ignored.

type Row = { id: string; ownerId: string; name: string };
type Where = { id?: string; ownerId?: string };

const mocks = vi.hoisted(() => {
  const state = { userId: "owner1" as string | null, rows: [] as { id: string; ownerId: string; name: string }[] };
  const matches = (r: { id: string; ownerId: string }, where: Where) => {
    for (const key of Object.keys(where)) if (key !== "id" && key !== "ownerId") throw new Error(`fake does not understand where.${key}`);
    return (where.id === undefined || r.id === where.id) && (where.ownerId === undefined || r.ownerId === where.ownerId);
  };
  const db = {
    class: {
      updateMany: vi.fn(async ({ where, data }: { where: Where; data: { name: string } }) => {
        let count = 0;
        for (const r of state.rows) {
          if (!matches(r, where)) continue;
          r.name = data.name;
          count++;
        }
        return { count };
      }),
      findUnique: vi.fn(async () => null),
      create: vi.fn(async (args: { data: { name: string } }) => ({ id: "new", name: args.data.name })),
    },
    classMembership: { create: vi.fn(async () => ({})) },
  };
  return { state, db, revalidatePath: vi.fn() };
});

vi.mock("@/lib/db", () => ({ getDb: () => mocks.db }));
vi.mock("@/lib/auth/config", () => ({ auth: async () => (mocks.state.userId ? { user: { id: mocks.state.userId } } : null) }));
vi.mock("next/cache", () => ({ revalidatePath: mocks.revalidatePath }));
vi.mock("next/navigation", () => ({
  redirect: (to: string) => {
    throw new Error(`redirect:${to}`);
  },
}));

import { createClass, renameClass } from "@/lib/social/actions";

const form = (name: string | null) => {
  const f = new FormData();
  if (name !== null) f.set("name", name);
  return f;
};
const names = () => Object.fromEntries(mocks.state.rows.map((r: Row) => [r.id, r.name]));

// renameClass always ends in redirect(); the mock turns that into a throw so the destination can be asserted.
async function rename(classId: string, name: string | null) {
  try {
    await renameClass(classId, form(name));
  } catch (e) {
    return (e as Error).message;
  }
  return "no redirect";
}

describe("renameClass", () => {
  beforeEach(() => {
    vi.clearAllMocks();
    mocks.state.userId = "owner1";
    mocks.state.rows = [
      { id: "c1", ownerId: "owner1", name: "Period 3" },
      { id: "c2", ownerId: "owner2", name: "Period 4" },
      { id: "c3", ownerId: "owner1", name: "Period 5" },
    ];
  });

  it("renames a class the signed-in user owns, and sends them back to its bare page", async () => {
    expect(await rename("c1", "AP Calc, period 3")).toBe("redirect:/classes/c1");
    expect(names().c1).toBe("AP Calc, period 3");
  });

  it("trims the new name", async () => {
    await rename("c1", "  Tidy  ");
    expect(names().c1).toBe("Tidy");
  });

  it("changes only that class: another class the same owner runs, and other owners' classes, keep their names", async () => {
    await rename("c1", "New");
    expect(names()).toEqual({ c1: "New", c2: "Period 4", c3: "Period 5" });
  });

  it("does nothing to a class someone else owns (a member, or a stranger who guessed the id)", async () => {
    expect(await rename("c2", "Hijacked")).toBe("redirect:/classes/c2");
    expect(names().c2).toBe("Period 4");
  });

  it("does nothing, without an error, for a class that does not exist", async () => {
    expect(await rename("nope", "Anything")).toBe("redirect:/classes/nope");
    expect(names()).toEqual({ c1: "Period 3", c2: "Period 4", c3: "Period 5" });
  });

  it("an empty, whitespace-only or missing name changes nothing and returns to the page with the error", async () => {
    for (const bad of ["", "   ", null]) expect(await rename("c1", bad)).toBe("redirect:/classes/c1?error=name");
    expect(names().c1).toBe("Period 3");
    expect(mocks.db.class.updateMany).not.toHaveBeenCalled();
  });

  it("a name over the limit changes nothing and returns with the error", async () => {
    expect(await rename("c1", "a".repeat(81))).toBe("redirect:/classes/c1?error=name");
    expect(names().c1).toBe("Period 3");
  });

  it("refreshes the class page and the class list", async () => {
    await rename("c1", "New");
    expect(mocks.revalidatePath).toHaveBeenCalledWith("/classes/c1");
    expect(mocks.revalidatePath).toHaveBeenCalledWith("/classes");
  });

  it("refuses when nobody is signed in, and changes nothing", async () => {
    mocks.state.userId = null;
    expect(await rename("c1", "New")).toBe("Not authenticated");
    expect(mocks.db.class.updateMany).not.toHaveBeenCalled();
    expect(names().c1).toBe("Period 3");
  });
});

describe("createClass uses the same name rule", () => {
  beforeEach(() => {
    vi.clearAllMocks();
    mocks.state.userId = "owner1";
  });

  it("refuses a name over the limit and creates nothing", async () => {
    await expect(createClass(form("a".repeat(81)))).rejects.toThrow("Class name is required");
    expect(mocks.db.class.create).not.toHaveBeenCalled();
  });

  it("refuses a whitespace-only name, and stores a trimmed one", async () => {
    await expect(createClass(form("   "))).rejects.toThrow("Class name is required");
    await expect(createClass(form("  Period 1  "))).rejects.toThrow("redirect:/classes/new");
    expect(mocks.db.class.create).toHaveBeenCalledTimes(1);
    expect(mocks.db.class.create.mock.calls[0][0].data.name).toBe("Period 1");
  });
});
