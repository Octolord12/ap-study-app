// A rough, unvalidated heuristic mapping raw MCQ accuracy to an AP score
// range (1-5). Real AP scoring uses a weighted composite of MCQ + FRQ with
// per-year curves College Board doesn't publish in advance -- this is
// deliberately coarse and always shown to the student labeled "estimate."
// FRQ points aren't factored in yet since self-grading happens after the
// exam; revisit once there's real score data to calibrate against.
export function estimateApScoreRange(mcqAccuracy: number): string {
  if (mcqAccuracy >= 0.85) return "4-5";
  if (mcqAccuracy >= 0.7) return "3-4";
  if (mcqAccuracy >= 0.55) return "3";
  if (mcqAccuracy >= 0.4) return "2-3";
  return "1-2";
}
