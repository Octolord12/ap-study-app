// The two courses whose content is genuinely math: it gets the extra
// plain-text-math typesetting in plain-math.ts and the paper-lined card
// styling in paper-lined.ts. AP CSA and AP World History are excluded.
const MATH_COURSE_SLUGS: readonly string[] = ["ap-calc", "ap-physics-1"];

export function isMathCourse(courseSlug: string): boolean {
  return MATH_COURSE_SLUGS.includes(courseSlug);
}
