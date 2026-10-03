import { Button as ButtonPrimitive } from "@base-ui/react/button"
import { cva, type VariantProps } from "class-variance-authority"
import { cn } from "cn"

// Hover on every variant is the highlighter: the control gets the mark color
// behind ink text. No lift, scale or shadow.
const buttonVariants = cva(
  "inline-flex shrink-0 items-center justify-center gap-2 rounded-sm border border-transparent text-sm font-semibold whitespace-nowrap transition-colors select-none disabled:pointer-events-none disabled:opacity-40 aria-invalid:border-destructive [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4",
  {
    variants: {
      variant: {
        default: "border-foreground bg-foreground text-background hover:bg-mark hover:text-on-mark",
        outline: "border-foreground bg-transparent text-foreground hover:bg-mark hover:text-on-mark",
        secondary: "border-border bg-muted text-foreground hover:border-foreground hover:bg-mark hover:text-on-mark",
        ghost: "text-foreground hover:bg-mark hover:text-on-mark",
        destructive: "border-destructive bg-transparent text-destructive hover:bg-destructive hover:text-background",
        link: "h-auto rounded-none px-0 text-foreground underline underline-offset-4 decoration-1 hover:bg-mark hover:text-on-mark hover:no-underline",
      },
      size: {
        default: "h-11 px-4",
        xs: "h-7 px-2 text-xs",
        sm: "h-9 px-3 text-[0.8125rem]",
        lg: "h-12 px-5 text-[0.9375rem]",
        icon: "size-11",
        "icon-xs": "size-7",
        "icon-sm": "size-9",
        "icon-lg": "size-12",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  }
)

function Button({
  className,
  variant = "default",
  size = "default",
  ...props
}: ButtonPrimitive.Props & VariantProps<typeof buttonVariants>) {
  return (
    <ButtonPrimitive
      data-slot="button"
      className={cn(buttonVariants({ variant, size, className }))}
      {...props}
    />
  )
}

export { Button, buttonVariants }
