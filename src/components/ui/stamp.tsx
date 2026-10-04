import { cn } from "cn"

// Badge art, drawn in code so it follows the theme and stays crisp at any
// size. Keyed by the badge slug from src/lib/gamification/badges.ts -- the
// emoji stored in the database `icon` column is no longer displayed.
// Two-tone: currentColor ink plus the highlighter, one stamp per badge.

const RING = <circle cx="32" cy="32" r="29" />

function Art({ slug }: { slug: string }) {
  switch (slug) {
    case "first_quiz":
      return (
        <>
          {RING}
          <circle cx="32" cy="32" r="19" fill="currentColor" stroke="none" />
          <path d="M23 33l6 6 12-13" stroke="var(--card)" strokeWidth={3.5} strokeLinecap="round" strokeLinejoin="round" />
        </>
      )
    case "streak_7":
      return (
        <>
          <circle cx="32" cy="32" r="29" fill="var(--mark)" />
          <g stroke="var(--on-mark)" strokeWidth={3} strokeLinecap="round">
            <path d="M20 20v24M27 20v24M34 20v24M41 20v24M16 38L45 26" />
          </g>
        </>
      )
    case "unit_mastery":
      return (
        <>
          {RING}
          <g fill="currentColor" stroke="none">
            {[20, 32, 44].flatMap((cx) => [20, 32, 44].map((cy) => <circle key={`${cx}-${cy}`} cx={cx} cy={cy} r={4} fill={cx === 32 && cy === 32 ? "var(--mark)" : "currentColor"} stroke={cx === 32 && cy === 32 ? "currentColor" : "none"} strokeWidth={1.5} />))}
          </g>
        </>
      )
    case "perfect_ten":
      return (
        <>
          {RING}
          <g fill="currentColor" stroke="none">
            {[18, 25, 32, 39, 46].flatMap((cx) => [26, 38].map((cy) => <circle key={`${cx}-${cy}`} cx={cx} cy={cy} r={3.2} />))}
          </g>
        </>
      )
    case "exam_finisher":
      return (
        <>
          {RING}
          <rect x="21" y="16" width="22" height="32" rx="1.5" fill="var(--card)" />
          <path d="M26 24h12M26 30h12M26 36h7" strokeWidth={2} strokeLinecap="round" />
          <circle cx="40" cy="40" r="6" fill="var(--mark)" />
          <path d="M37.5 40l2 2 3.5-4" stroke="var(--on-mark)" strokeWidth={2} strokeLinecap="round" strokeLinejoin="round" />
        </>
      )
    case "boss_slayer":
      return (
        <>
          {RING}
          <g strokeWidth={2} strokeLinejoin="round">
            <g transform="rotate(45 32 32)">
              <path d="M28 14h8v26h-8z" fill="var(--mark)" />
              <path d="M28 40h8l-4 9z" fill="currentColor" />
            </g>
            <g transform="rotate(-45 32 32)">
              <path d="M28 14h8v26h-8z" fill="var(--card)" />
              <path d="M28 40h8l-4 9z" fill="currentColor" />
            </g>
          </g>
        </>
      )
    default:
      return RING
  }
}

export function BadgeStamp({ slug, earned = true, className }: { slug: string; earned?: boolean; className?: string }) {
  return (
    <svg
      viewBox="0 0 64 64"
      fill="none"
      stroke="currentColor"
      strokeWidth={2.5}
      aria-hidden
      className={cn("size-16", !earned && "opacity-30", className)}
    >
      <Art slug={slug} />
    </svg>
  )
}

// The boss-battle title for one unit: a ring around the unit's number on the
// highlighter. Drawn per number, so every unit's title has its own stamp.
export function TitleStamp({ unitNumber, className }: { unitNumber: number; className?: string }) {
  const label = String(unitNumber)
  return (
    <svg
      viewBox="0 0 64 64"
      fill="none"
      stroke="currentColor"
      strokeWidth={2.5}
      aria-hidden
      className={cn("size-16", className)}
    >
      {RING}
      <circle cx="32" cy="32" r="21" fill="var(--mark)" />
      <text
        x="32"
        y={label.length > 1 ? 39.5 : 41}
        textAnchor="middle"
        fontSize={label.length > 1 ? 22 : 28}
        fontWeight={800}
        fill="var(--on-mark)"
        stroke="none"
        style={{ fontFamily: "var(--font-archivo), sans-serif" }}
      >
        {label}
      </text>
    </svg>
  )
}
