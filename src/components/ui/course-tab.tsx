import { courseAccent, courseTabLabel } from "@/lib/content/course-accent"
import { cn } from "cn"

// A course's chip: its short name on its color. Used wherever a list names a course.
export function CourseTab({ slug, name, className }: { slug: string; name: string; className?: string }) {
  return (
    <span data-c={courseAccent(slug)} className={cn("tab-chip min-w-[4.5rem]", className)}>
      {courseTabLabel(slug, name)}
    </span>
  )
}
