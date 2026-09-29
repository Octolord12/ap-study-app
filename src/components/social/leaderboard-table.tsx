import Link from "next/link";
import type { LeaderboardEntry } from "@/lib/social/leaderboard";

const MEDALS = ["🥇", "🥈", "🥉"];

// Server Component: the week/all-time toggle is two plain links to
// `?period=`, not client state -- no JS needed for something this simple.
export function LeaderboardTable({
  entries,
  currentUserId,
  period,
  basePath,
}: {
  entries: LeaderboardEntry[];
  currentUserId: string;
  period: "week" | "all";
  basePath: string;
}) {
  return (
    <div>
      <div className="mb-3 flex gap-2 text-sm">
        <Link
          href={`${basePath}?period=week`}
          className={period === "week" ? "font-semibold underline underline-offset-4" : "text-muted-foreground"}
        >
          This week
        </Link>
        <Link
          href={`${basePath}?period=all`}
          className={period === "all" ? "font-semibold underline underline-offset-4" : "text-muted-foreground"}
        >
          All time
        </Link>
      </div>

      {entries.length === 0 ? (
        <p className="text-sm text-muted-foreground">No one to rank yet.</p>
      ) : (
        <ul className="divide-y divide-border rounded-lg border border-border">
          {entries.map((entry) => (
            <li
              key={entry.userId}
              className={`flex items-center justify-between px-4 py-2 text-sm ${
                entry.userId === currentUserId ? "bg-muted" : ""
              }`}
            >
              <span>
                <span className="mr-2 inline-block w-6 text-muted-foreground">{MEDALS[entry.rank - 1] ?? entry.rank}</span>
                {entry.username}
                {entry.userId === currentUserId ? " (you)" : ""}
              </span>
              <span className="font-medium">{entry.totalXp} XP</span>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
