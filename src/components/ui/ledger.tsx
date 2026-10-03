import Link from "next/link"
import type { LeaderboardEntry } from "@/lib/social/leaderboard"
import { cn } from "cn"

// A leaderboard as a ledger: rank numeral, username, XP. The viewer's own row
// is the highlighted one. Server Component: the week/all-time toggle is two
// plain links to `?period=`, not client state.
export function Ledger({
  entries,
  currentUserId,
  period,
  basePath,
}: {
  entries: LeaderboardEntry[]
  currentUserId: string
  period: "week" | "all"
  basePath: string
}) {
  return (
    <div>
      <nav aria-label="Leaderboard period" className="mb-4 flex gap-4 text-sm">
        {(
          [
            ["week", "This week"],
            ["all", "All time"],
          ] as const
        ).map(([value, text]) => (
          <Link
            key={value}
            href={`${basePath}?period=${value}`}
            aria-current={period === value ? "page" : undefined}
            className={cn(
              "px-0.5 py-1 font-semibold",
              period === value ? "bg-mark text-on-mark" : "text-muted-foreground hover:text-foreground"
            )}
          >
            {text}
          </Link>
        ))}
      </nav>

      {entries.length === 0 ? (
        <p className="text-sm text-muted-foreground">No one to rank yet.</p>
      ) : (
        <ol className="border-b border-border">
          {entries.map((entry) => {
            const me = entry.userId === currentUserId
            return (
              <li
                key={entry.userId}
                className={cn(
                  "grid grid-cols-[2.5rem_minmax(0,1fr)_auto] items-baseline gap-3 border-t border-border px-2 py-2.5",
                  me && "bg-mark text-on-mark"
                )}
              >
                <span className="numeral text-2xl">{entry.rank}</span>
                <span className="truncate font-mono text-sm">
                  {entry.username}
                  {me ? <span className="eyebrow ml-2 !text-current">you</span> : null}
                </span>
                <span className="text-sm font-semibold tabular-nums">{entry.totalXp} XP</span>
              </li>
            )
          })}
        </ol>
      )}
    </div>
  )
}
