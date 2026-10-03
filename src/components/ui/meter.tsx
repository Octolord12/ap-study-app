import { cn } from "cn"

// Unit mastery as a row of ten bubbles, one per 10% -- the answer sheet,
// filled in. `percent` is null for "not started".
export function Bubbles({ percent, className }: { percent: number | null; className?: string }) {
  const filled = percent === null ? 0 : Math.round(percent / 10)
  return (
    <span
      role="img"
      aria-label={percent === null ? "Not started" : `${percent} percent correct`}
      className={cn("inline-flex gap-1", className)}
    >
      {Array.from({ length: 10 }, (_, i) => (
        <i
          key={i}
          aria-hidden
          className={cn("block size-3 rounded-full border-[1.5px] border-foreground", i < filled && "bg-foreground")}
        />
      ))}
    </span>
  )
}

// Progress toward the next level: a highlighter stroke over a thin rule.
export function XpBar({ value, max, label, className }: { value: number; max: number; label: string; className?: string }) {
  const pct = max > 0 ? Math.min(100, Math.round((value / max) * 100)) : 0
  return (
    <div role="img" aria-label={label} className={cn("relative h-2.5 w-full bg-border", className)}>
      <i className="absolute inset-y-0 left-0 block border-b-2 border-foreground bg-mark" style={{ width: `${pct}%` }} />
    </div>
  )
}

// Share of the exam, as a bar on a rule. Used for unit weighting.
export function WeightBar({ min, max, label }: { min: number; max: number; label: string }) {
  return (
    <div role="img" aria-label={label} className="relative h-2 w-full max-w-40 bg-border">
      <i
        className="absolute inset-y-0 block bg-foreground"
        style={{ left: `${Math.min(100, min * 4)}%`, width: `${Math.max(2, (max - min) * 4)}%` }}
      />
    </div>
  )
}
