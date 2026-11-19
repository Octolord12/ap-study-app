import { courseAccent } from "@/lib/content/course-accent";

// Everything under a course carries that course's color (--c, see globals.css) as a thin band under the header and
// on its chips. The page itself keeps the Powder colors. A course the accent list doesn't know keeps the default.
export default async function CourseLayout({ children, params }: LayoutProps<"/courses/[courseSlug]">) {
  const { courseSlug } = await params;
  return (
    <div data-c={courseAccent(courseSlug)} className="flex flex-1 flex-col">
      <div aria-hidden className="h-2 border-b-2 border-foreground bg-course" />
      {children}
    </div>
  );
}
