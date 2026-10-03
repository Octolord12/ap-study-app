import { isMathCourse } from "@/lib/content/math-courses";

// Courses whose question cards get the "paper-lined" notebook background
// (the `.paper-lined` CSS class in globals.css) -- the math-heavy courses,
// where a ruled-paper look reads naturally.
export function isPaperLinedCourse(courseSlug: string): boolean {
  return isMathCourse(courseSlug);
}
