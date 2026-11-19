import * as React from "react"
import { cn } from "cn"

// The one boxed object in the system: a white card with a navy outline. `band` puts the current course color
// across the top, like the strip on a folder.
export function Sheet({
  band = false,
  className,
  bodyClassName,
  children,
  ...props
}: React.ComponentProps<"div"> & { band?: boolean; bodyClassName?: string }) {
  return (
    <div data-slot="sheet" className={cn("sheet", className)} {...props}>
      {band ? <div className="sheet-band" aria-hidden /> : null}
      <div className={cn("p-4 sm:p-6", bodyClassName)}>{children}</div>
    </div>
  )
}
