import * as React from "react"
import Link from "next/link"
import { cn } from "cn"

// Page chrome shared by every route, so pages can't drift apart: one outer
// width, one gutter, and a booklet-style margin column (labels on the left,
// content on the right at md and up; stacked on phones).

const GRID = "grid gap-x-10 gap-y-3 md:grid-cols-[10.5rem_minmax(0,1fr)]"

export function Breadcrumb({ items }: { items: { label: string; href?: string }[] }) {
  return (
    <nav aria-label="Breadcrumb">
      <ol className="flex flex-wrap gap-x-2">
        {items.map((item, i) => (
          <li key={item.label} className="flex gap-x-2">
            {item.href ? (
              <Link href={item.href} className="underline-offset-4 hover:bg-mark hover:text-on-mark hover:no-underline">
                {item.label}
              </Link>
            ) : (
              <span aria-current="page">{item.label}</span>
            )}
            {i < items.length - 1 ? <span aria-hidden>/</span> : null}
          </li>
        ))}
      </ol>
    </nav>
  )
}

export function Eyebrow({ className, ...props }: React.ComponentProps<"p">) {
  return <p className={cn("eyebrow", className)} {...props} />
}

export function Page({ className, ...props }: React.ComponentProps<"div">) {
  return <div className={cn("mx-auto w-full max-w-[67.5rem] flex-1 px-4 py-8 sm:px-6 md:py-12", className)} {...props} />
}

// Title block: the margin column carries where you are (breadcrumb / kicker),
// the content column carries the title, one sentence of context, and the
// page's primary actions.
export function PageHeader({
  eyebrow,
  title,
  description,
  actions,
  className,
}: {
  eyebrow?: React.ReactNode
  title: React.ReactNode
  description?: React.ReactNode
  actions?: React.ReactNode
  className?: string
}) {
  return (
    <header className={cn(GRID, "border-b-2 border-foreground pb-8", className)}>
      <div className="eyebrow md:pt-3">{eyebrow}</div>
      <div className="min-w-0">
        <h1 className="display text-[clamp(2.25rem,5.5vw,3.5rem)] text-balance">{title}</h1>
        {description ? <p className="reading mt-4 max-w-[60ch] text-base sm:text-lg">{description}</p> : null}
        {actions ? <div className="mt-6 flex flex-wrap items-center gap-3">{actions}</div> : null}
      </div>
    </header>
  )
}

// A titled block under a hairline rule. `label` sits in the margin column
// (mono caps); `note` is an optional line of explanation under it.
export function Section({
  label,
  note,
  id,
  className,
  children,
}: {
  label?: React.ReactNode
  note?: React.ReactNode
  id?: string
  className?: string
  children: React.ReactNode
}) {
  return (
    <section id={id} className={cn(GRID, "rule py-8 md:py-10 [header+&]:border-t-0", className)} aria-labelledby={id ? `${id}-label` : undefined}>
      <div className="min-w-0">
        {label ? (
          <h2 id={id ? `${id}-label` : undefined} className="eyebrow !text-foreground">
            {label}
          </h2>
        ) : null}
        {note ? <p className="mt-2 max-w-[24ch] text-[0.8125rem] leading-snug text-muted-foreground">{note}</p> : null}
      </div>
      <div className="min-w-0">{children}</div>
    </section>
  )
}

// Rows separated by hairlines, the app's list shape (no boxes around items).
export function RuledList({ className, ...props }: React.ComponentProps<"ul">) {
  return <ul className={cn("border-b border-border [&>li]:border-t [&>li]:border-border", className)} {...props} />
}

// "Here is the thing, and the button for it": one line of explanation on the
// left, the action on the right (stacked on phones).
export function ActionRow({ action, className, children }: { action: React.ReactNode; className?: string; children: React.ReactNode }) {
  return (
    <div className={cn("flex flex-wrap items-center justify-between gap-x-8 gap-y-4", className)}>
      <div className="min-w-0 max-w-[52ch]">{children}</div>
      <div className="shrink-0">{action}</div>
    </div>
  )
}
