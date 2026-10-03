import * as React from "react"
import { cn } from "cn"

// Native <select> (so the OS picker and keyboard behavior come for free),
// sized and ruled like Input.
function Select({ className, ...props }: React.ComponentProps<"select">) {
  return (
    <select
      data-slot="select"
      className={cn(
        "h-11 w-full min-w-0 rounded-sm border border-input bg-card px-3 text-base text-card-foreground disabled:cursor-not-allowed disabled:opacity-50",
        className
      )}
      {...props}
    />
  )
}

export { Select }
