import * as React from "react"
import { cn } from "cn"

// The one boxed object in the system: a sheet of paper. Everything else is
// laid out with rules and whitespace. `lined` switches it to ruled notebook
// paper (Calc AB / Physics 1 question sheets, see .paper-lined in
// globals.css). The notebook padding lives on the outer element and the
// body padding inside it, so the margin line never touches text.
export function Sheet({
  lined = false,
  className,
  bodyClassName,
  children,
  ...props
}: React.ComponentProps<"div"> & { lined?: boolean; bodyClassName?: string }) {
  return (
    <div
      data-slot="sheet"
      className={cn("rounded-sm border border-border bg-card text-card-foreground", lined && "paper-lined", className)}
      {...props}
    >
      <div className={cn("p-4 sm:p-6", bodyClassName)}>{children}</div>
    </div>
  )
}
