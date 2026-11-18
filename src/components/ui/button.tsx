import { Button as ButtonPrimitive } from "@base-ui/react/button"
import { cva, type VariantProps } from "class-variance-authority"
import { cn } from "cn"

// Ink is the action. Filled and outlined buttons lift on hover and cast a hard shadow in the current
// course color (--c); ghost and link variants take the course color as a background behind ink text.
const buttonVariants = cva(
  "inline-flex shrink-0 items-center justify-center gap-2 rounded-md border-[1.5px] border-transparent text-sm font-bold whitespace-nowrap transition-[transform,box-shadow,background-color,color,border-color] select-none disabled:pointer-events-none disabled:opacity-40 aria-invalid:border-destructive [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4",
  {
    variants: {
      variant: {
        default: "border-foreground bg-foreground text-card hover:-translate-px hover:shadow-[3px_3px_0_0_var(--c)] active:translate-0 active:shadow-none",
        outline: "border-foreground bg-transparent text-foreground hover:-translate-px hover:shadow-[3px_3px_0_0_var(--c)] active:translate-0 active:shadow-none",
        secondary: "border-border bg-muted text-foreground hover:border-foreground hover:-translate-px hover:shadow-[3px_3px_0_0_var(--c)] active:translate-0 active:shadow-none",
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
