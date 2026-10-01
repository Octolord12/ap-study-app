// Courses whose question cards get the "paper-lined" notebook background
// (the `.paper-lined` CSS class in globals.css) -- picked for the two
// courses that are heavy on rendered math/LaTeX, where a ruled-paper look
// reads naturally. AP CSA and AP World History stay on the plain card
// background.
const PAPER_LINED_COURSE_SLUGS: readonly string[] = ["ap-calc", "ap-physics-1"];

export function isPaperLinedCourse(courseSlug: string): boolean {
  return PAPER_LINED_COURSE_SLUGS.includes(courseSlug);
}
