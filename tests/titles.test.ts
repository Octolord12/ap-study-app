import { describe, expect, it } from "vitest";
import { groupTitlesByCourse, sortUnitTitles, unitConquerorTitle, type UnitTitle } from "@/lib/gamification/titles";

function title(courseName: string, unitNumber: number): UnitTitle {
  return {
    unitId: `${courseName}-${unitNumber}`,
    unitSlug: `u${unitNumber}`,
    unitName: `Unit ${unitNumber} name`,
    unitNumber,
    courseSlug: courseName.toLowerCase().replace(/\s+/g, "-"),
    courseName,
    title: unitConquerorTitle(unitNumber),
  };
}

describe("unitConquerorTitle", () => {
  it("names the title after the unit's number", () => {
    expect(unitConquerorTitle(2)).toBe("Unit 2 Conqueror");
    expect(unitConquerorTitle(10)).toBe("Unit 10 Conqueror");
  });
});

describe("sortUnitTitles / groupTitlesByCourse", () => {
  const input = [title("AP Physics 1", 3), title("AP Calculus AB", 6), title("AP Calculus AB", 2), title("AP Physics 1", 1)];

  it("sorts by course name, then unit number (numerically, so 10 follows 9)", () => {
    expect(sortUnitTitles(input).map((t) => `${t.courseName} ${t.unitNumber}`)).toEqual([
      "AP Calculus AB 2",
      "AP Calculus AB 6",
      "AP Physics 1 1",
      "AP Physics 1 3",
    ]);
    expect(sortUnitTitles([title("X", 10), title("X", 9)]).map((t) => t.unitNumber)).toEqual([9, 10]);
  });

  it("does not mutate its input", () => {
    const copy = [...input];
    sortUnitTitles(input);
    expect(input).toEqual(copy);
  });

  it("groups titles under their course, in order", () => {
    const groups = groupTitlesByCourse(input);
    expect(groups.map((g) => g.courseName)).toEqual(["AP Calculus AB", "AP Physics 1"]);
    expect(groups[0].titles.map((t) => t.title)).toEqual(["Unit 2 Conqueror", "Unit 6 Conqueror"]);
  });

  it("returns no groups when nothing is conquered", () => {
    expect(groupTitlesByCourse([])).toEqual([]);
  });
});
