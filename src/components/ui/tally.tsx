import { cn } from "cn"

const GROUP_WIDTH = 34

// A streak as tally marks: four strokes and a slash per group of five, the
// latest stroke highlighted. Past 30 days it stops drawing (the count beside
// it carries the number) so it never grows wider than the header.
export function Tally({ count, className }: { count: number; className?: string }) {
  if (count <= 0 || count > 30) return null
  const groups = Math.ceil(count / 5)
  const width = groups * GROUP_WIDTH - 4
  const strokes: React.ReactNode[] = []

  for (let g = 0; g < groups; g++) {
    const inGroup = Math.min(5, count - g * 5)
    const x = g * GROUP_WIDTH
    for (let i = 0; i < Math.min(inGroup, 4); i++) {
      const sx = x + 6 + i * 6
      const isLast = g * 5 + i + 1 === count
      if (isLast) strokes.push(<rect key={`m${g}-${i}`} x={sx - 3} y={1} width={6} height={30} fill="var(--mark)" stroke="none" />)
      strokes.push(<line key={`s${g}-${i}`} x1={sx} y1={4} x2={sx} y2={28} />)
    }
    if (inGroup === 5) {
      if (g * 5 + 5 === count) strokes.push(<line key={`m${g}-5`} x1={x} y1={23} x2={x + 30} y2={9} stroke="var(--mark)" strokeWidth={9} />)
      strokes.push(<line key={`s${g}-5`} x1={x} y1={23} x2={x + 30} y2={9} />)
    }
  }

  return (
    <svg
      role="img"
      aria-label={`${count}-day streak`}
      width={width}
      height={32}
      viewBox={`0 0 ${width} 32`}
      fill="none"
      stroke="currentColor"
      strokeWidth={2.5}
      strokeLinecap="round"
      className={cn("shrink-0", className)}
    >
      {strokes}
    </svg>
  )
}
