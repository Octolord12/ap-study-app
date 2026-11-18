import { courseAccent, courseTabLabel } from "@/lib/content/course-accent"
import { cn } from "cn"

// A course's divider tab: its short name on its color. Used wherever a list names a course.
export function CourseTab({ slug, name, className }: { slug: string; name: string; className?: string }) {
  return (
    <span data-c={courseAccent(slug)} className={cn("tab-chip min-w-[4.5rem]", className)}>
      {courseTabLabel(slug, name)}
    </span>
  )
}

// The eight tabs side by side: the app's signature, used as a thin band across the top of the header.
export function TabStripe({ keys, className }: { keys: readonly string[]; className?: string }) {
  return (
    <div aria-hidden className={cn("flex", className)}>
      {keys.map((key) => (
        <i key={key} data-c={key} className="block h-full flex-1 bg-course" />
      ))}
    </div>
  )
}
