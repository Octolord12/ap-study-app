// What the "Class-wide weaknesses" panel will show once there is an
// aggregation behind it: one row per unit, from the members' attempts.
export interface ClassWeakness {
  unitId: string;
  unitName: string;
  classAccuracyPercent: number;
  studentsBelowProficient: number;
  studentsTried: number;
}

export interface OwnedClass {
  id: string;
  name: string;
  inviteCode: string;
  courseName: string | null;
  memberCount: number;
}
