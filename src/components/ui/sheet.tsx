import * as React from "react"
import { cn } from "cn"

// The one boxed object in the system: a sheet of paper (white, ink edge, the edge of the sheet behind it).
// `binder` punches three holes in the left margin and makes room for them, for the sheets a student works on
// (a question, a free-response prompt). `band` puts the current course color across the top, like the divider
// the sheet sits behind. `stack` is how many sheets show underneath.
export function Sheet({
  binder = false,
  band = false,
  stack = 1,
  className,
  bodyClassName,
  children,
  ...props
}: React.ComponentProps<"div"> & { binder?: boolean; band?: boolean; stack?: 1 | 2; bodyClassName?: string }) {
  return (
    <div data-slot="sheet" data-stack={stack} className={cn("sheet", className)} {...props}>
      {band ? <div className="sheet-band" aria-hidden /> : null}
      {binder ? (
        <div className="sheet-holes" aria-hidden>
          <i />
          <i />
          <i />
        </div>
      ) : null}
      <div className={cn("p-4 sm:p-6", binder && "pl-11 sm:pl-14", bodyClassName)}>{children}</div>
    </div>
  )
}
