import { courseAccent } from "@/lib/content/course-accent";

// Everything under a course takes that course's color (--c, see globals.css): the band under the header, the
// picked answer, the button shadow, the highlighted nav item. A course the accent list doesn't know keeps the default.
export default async function CourseLayout({ children, params }: LayoutProps<"/courses/[courseSlug]">) {
  const { courseSlug } = await params;
  return (
    <div data-c={courseAccent(courseSlug)} className="flex flex-1 flex-col">
      <div aria-hidden className="h-2.5 border-b-[1.5px] border-foreground bg-course" />
      {children}
    </div>
  );
}
