import { requireUserId } from "@/lib/auth/session";
import { getFriendsLeaderboard, getFriendsList, getPendingFriendRequests } from "@/lib/social/queries";
import { respondToFriendRequest, sendFriendRequest } from "@/lib/social/actions";
import { LeaderboardTable } from "@/components/social/leaderboard-table";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";

const ERROR_MESSAGES: Record<string, string> = {
  "missing-username": "Enter a username.",
  "not-found": "No user found with that username.",
  self: "You can't friend yourself.",
  exists: "A friend request already exists between you two.",
};

export default async function FriendsPage({
  searchParams,
}: {
  searchParams: Promise<{ period?: string; error?: string; sent?: string }>;
}) {
  const userId = await requireUserId();
  const { period: periodParam, error, sent } = await searchParams;
  const period = periodParam === "all" ? "all" : "week";

  const [leaderboard, friends, requests] = await Promise.all([
    getFriendsLeaderboard(userId, period),
    getFriendsList(userId),
    getPendingFriendRequests(userId),
  ]);

  return (
    <div className="mx-auto w-full max-w-2xl px-6 py-10">
      <h1 className="mb-6 text-2xl font-bold tracking-tight">Friends</h1>

      <Card className="mb-8">
        <CardHeader>
          <CardTitle className="text-base">Add a friend</CardTitle>
        </CardHeader>
        <CardContent>
          <form action={sendFriendRequest} className="flex gap-2">
            <div className="flex-1 space-y-2">
              <Label htmlFor="username" className="sr-only">
                Username
              </Label>
              <Input id="username" name="username" required placeholder="Their username" />
            </div>
            <Button type="submit">Send request</Button>
          </form>
          {error ? <p className="mt-2 text-sm text-destructive">{ERROR_MESSAGES[error] ?? "Something went wrong."}</p> : null}
          {sent ? <p className="mt-2 text-sm text-primary">Friend request sent.</p> : null}
        </CardContent>
      </Card>

      {requests.incoming.length > 0 ? (
        <div className="mb-8">
          <h2 className="mb-3 text-sm font-semibold uppercase tracking-wide text-muted-foreground">
            Friend requests
          </h2>
          <ul className="divide-y divide-border rounded-lg border border-border">
            {requests.incoming.map((r) => {
              const accept = respondToFriendRequest.bind(null, r.requesterId, true);
              const decline = respondToFriendRequest.bind(null, r.requesterId, false);
              return (
                <li key={r.requesterId} className="flex items-center justify-between px-4 py-2 text-sm">
                  <span>{r.requester.username}</span>
                  <div className="flex gap-2">
                    <form action={accept}>
                      <Button type="submit" size="sm">
                        Accept
                      </Button>
                    </form>
                    <form action={decline}>
                      <Button type="submit" size="sm" variant="outline">
                        Decline
                      </Button>
                    </form>
                  </div>
                </li>
              );
            })}
          </ul>
        </div>
      ) : null}

      {requests.outgoing.length > 0 ? (
        <div className="mb-8">
          <h2 className="mb-3 text-sm font-semibold uppercase tracking-wide text-muted-foreground">
            Sent requests
          </h2>
          <ul className="divide-y divide-border rounded-lg border border-border">
            {requests.outgoing.map((r) => (
              <li key={r.addresseeId} className="px-4 py-2 text-sm text-muted-foreground">
                {r.addressee.username} · pending
              </li>
            ))}
          </ul>
        </div>
      ) : null}

      <h2 className="mb-3 text-sm font-semibold uppercase tracking-wide text-muted-foreground">Leaderboard</h2>
      <div className="mb-8">
        <LeaderboardTable entries={leaderboard} currentUserId={userId} period={period} basePath="/friends" />
      </div>

      <h2 className="mb-3 text-sm font-semibold uppercase tracking-wide text-muted-foreground">
        Friends ({friends.length})
      </h2>
      {friends.length === 0 ? (
        <p className="text-sm text-muted-foreground">No friends yet -- send a request above.</p>
      ) : (
        <ul className="divide-y divide-border rounded-lg border border-border">
          {friends.map((f) => (
            <li key={f.id} className="px-4 py-2 text-sm">
              {f.username}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
