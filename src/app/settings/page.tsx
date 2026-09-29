import { requireUserId } from "@/lib/auth/session";
import { getDb } from "@/lib/db";
import { updateLeaderboardOptOut } from "@/lib/social/actions";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

export default async function SettingsPage() {
  const userId = await requireUserId();
  const user = await getDb().user.findUniqueOrThrow({
    where: { id: userId },
    select: { leaderboardOptOut: true, username: true, displayName: true },
  });

  const setOptOut = updateLeaderboardOptOut.bind(null, !user.leaderboardOptOut);

  return (
    <div className="mx-auto w-full max-w-2xl px-6 py-10">
      <h1 className="mb-6 text-2xl font-bold tracking-tight">Settings</h1>

      <Card>
        <CardHeader>
          <CardTitle className="text-base">Privacy</CardTitle>
        </CardHeader>
        <CardContent className="space-y-4">
          <p className="text-sm text-muted-foreground">
            Leaderboards show your username ({user.username}), never your name ({user.displayName}).
          </p>
          <div className="flex items-center justify-between rounded-lg border border-border p-4">
            <div>
              <p className="text-sm font-medium">Appear on leaderboards</p>
              <p className="text-xs text-muted-foreground">
                {user.leaderboardOptOut
                  ? "You're currently hidden from friend and class leaderboards."
                  : "You're currently visible on friend and class leaderboards you're part of."}
              </p>
            </div>
            <form action={setOptOut}>
              <Button type="submit" variant={user.leaderboardOptOut ? "default" : "outline"} size="sm">
                {user.leaderboardOptOut ? "Show me" : "Hide me"}
              </Button>
            </form>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
