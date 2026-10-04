// Titles are earned by defeating a unit's boss battle. They are not stored:
// BossBattleAttempt.passed already records it, never reverts once true, and
// the title is a pure function of the unit's number -- so there is nothing to
// drift out of sync and no migration. See getUserUnitTitles in queries.ts.

export interface UnitTitle {
  unitId: string;
  unitSlug: string;
  unitName: string;
  unitNumber: number;
  courseSlug: string;
  courseName: string;
  title: string;
}

export function unitConquerorTitle(unitNumber: number): string {
  return `Unit ${unitNumber} Conqueror`;
}

// Course by course (alphabetical, like every other course list), units in order.
export function sortUnitTitles(titles: UnitTitle[]): UnitTitle[] {
  return [...titles].sort((a, b) => a.courseName.localeCompare(b.courseName) || a.unitNumber - b.unitNumber);
}

export function groupTitlesByCourse(titles: UnitTitle[]): { courseSlug: string; courseName: string; titles: UnitTitle[] }[] {
  const groups = new Map<string, { courseSlug: string; courseName: string; titles: UnitTitle[] }>();
  for (const title of sortUnitTitles(titles)) {
    const group = groups.get(title.courseSlug) ?? { courseSlug: title.courseSlug, courseName: title.courseName, titles: [] };
    group.titles.push(title);
    groups.set(title.courseSlug, group);
  }
  return [...groups.values()];
}
