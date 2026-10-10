import { readFileSync } from "node:fs";
import { beforeEach, describe, expect, it, vi } from "vitest";

// deleteClass against an in-memory class table that honors the query's meaning (the class id AND its owner), so the tests show who can NOT
// delete a class as well as who can. The fake throws on a filter it does not understand, so a new condition can't be silently ignored.

type Where = { id?: string; ownerId?: string };

const mocks = vi.hoisted(() => {
  const state = { userId: "owner1" as string | null, rows: [] as { id: string; ownerId: string }[] };
  const db = {
    class: {
      deleteMany: vi.fn(async ({ where }: { where: Where }) => {
        for (const key of Object.keys(where)) if (key !== "id" && key !== "ownerId") throw new Error(`fake does not understand where.${key}`);
        const before = state.rows.length;
        state.rows = state.rows.filter((r) => !((where.id === undefined || r.id === where.id) && (where.ownerId === undefined || r.ownerId === where.ownerId)));
        return { count: before - state.rows.length };
      }),
    },
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

import { deleteClass, leaveClass } from "@/lib/social/actions";

const ids = () => mocks.state.rows.map((r) => r.id).sort();

// deleteClass always ends in redirect(); the mock turns that into a throw so the destination can be asserted.
async function remove(classId: string) {
  try {
    await deleteClass(classId);
  } catch (e) {
    return (e as Error).message;
  }
  return "no redirect";
}

describe("deleteClass", () => {
  beforeEach(() => {
    vi.clearAllMocks();
    mocks.state.userId = "owner1";
    mocks.state.rows = [
      { id: "c1", ownerId: "owner1" },
      { id: "c2", ownerId: "owner2" },
      { id: "c3", ownerId: "owner1" },
    ];
  });

  it("deletes a class the signed-in user owns and sends them to the class list", async () => {
    expect(await remove("c1")).toBe("redirect:/classes");
    expect(ids()).toEqual(["c2", "c3"]);
  });

  it("deletes only that class: another class the same owner runs, and other owners' classes, are untouched", async () => {
    await remove("c1");
    expect(ids()).toContain("c3");
    expect(ids()).toContain("c2");
  });

  it("does nothing to a class someone else owns (a member, or a stranger who guessed the id)", async () => {
    expect(await remove("c2")).toBe("redirect:/classes");
    expect(ids()).toEqual(["c1", "c2", "c3"]);
  });

  it("does nothing, without an error, for a class that does not exist", async () => {
    expect(await remove("nope")).toBe("redirect:/classes");
    expect(ids()).toEqual(["c1", "c2", "c3"]);
  });

  it("refreshes the class list", async () => {
    await remove("c1");
    expect(mocks.revalidatePath).toHaveBeenCalledWith("/classes");
  });

  it("refuses when nobody is signed in, and deletes nothing", async () => {
    mocks.state.userId = null;
    expect(await remove("c1")).toBe("Not authenticated");
    expect(mocks.db.class.deleteMany).not.toHaveBeenCalled();
    expect(ids()).toEqual(["c1", "c2", "c3"]);
  });
});

describe("what deleting a class takes with it", () => {
  const schema = readFileSync("prisma/schema.prisma", "utf8");

  it("memberships and blocks are removed by the database with their class, so the delete can't fail on, or orphan, them", () => {
    for (const model of ["ClassMembership", "ClassBan"]) {
      const body = schema.match(new RegExp(`model ${model} \\{[\\s\\S]*?\\n\\}`))?.[0] ?? "";
      expect(body, model).toMatch(/class\s+Class\s+@relation\(fields: \[classId\], references: \[id\], onDelete: Cascade\)/);
    }
  });

  it("nothing else in the schema points at a class (only the people in it and the people blocked from it), so no one's study data goes with it", () => {
    const referencing = [...schema.matchAll(/model (\w+) \{([\s\S]*?)\n\}/g)]
      .filter(([, name, body]) => name !== "Class" && /\bClass\??\s+@relation/.test(body))
      .map(([, name]) => name);
    expect(referencing).toEqual(["ClassMembership", "ClassBan"]);
  });

  it("the owner is told to hand the class over or delete it, instead of leaving it", async () => {
    mocks.state.userId = "owner1";
    const db = mocks.db as unknown as { classMembership: unknown };
    db.classMembership = { findUnique: async () => ({ role: "OWNER" }), delete: vi.fn() };
    await expect(leaveClass("c1")).rejects.toThrow("hand the class to another member, or delete it");
    expect((db.classMembership as { delete: ReturnType<typeof vi.fn> }).delete).not.toHaveBeenCalled();
  });
});
