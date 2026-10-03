import type { Metadata } from "next";
import { requireUserId } from "@/lib/auth/session";
import { getFriendsLeaderboard, getFriendsList, getPendingFriendRequests } from "@/lib/social/queries";
import { respondToFriendRequest, sendFriendRequest } from "@/lib/social/actions";
import { Ledger } from "@/components/ui/ledger";
import { Button } from "@/components/ui/button";
import { Field } from "@/components/ui/field";
import { Input } from "@/components/ui/input";
import { Page, PageHeader, RuledList, Section } from "@/components/ui/page";

export const metadata: Metadata = { title: "Friends" };

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
    <Page>
      <PageHeader eyebrow="Friends" title="Friends" description="See where you stand against people you know. Everyone appears by username." />

      <Section label="Add a friend">
        <form action={sendFriendRequest} className="flex max-w-md flex-wrap items-end gap-3">
          <Field id="username" label="Their username" className="min-w-52 flex-1">
            <Input id="username" name="username" required autoComplete="off" autoCapitalize="none" />
          </Field>
          <Button type="submit" size="lg">
            Send request
          </Button>
        </form>
        {error ? (
          <p role="alert" className="mt-3 text-sm font-medium text-incorrect">
            {ERROR_MESSAGES[error] ?? "Something went wrong."}
          </p>
        ) : null}
        {sent ? (
          <p role="status" className="mt-3 text-sm font-medium">
            Friend request sent.
          </p>
        ) : null}
      </Section>

      {requests.incoming.length > 0 ? (
        <Section label="Requests" note="People who want to be your friend.">
          <RuledList>
            {requests.incoming.map((r) => {
              const accept = respondToFriendRequest.bind(null, r.requesterId, true);
              const decline = respondToFriendRequest.bind(null, r.requesterId, false);
              return (
                <li key={r.requesterId} className="flex flex-wrap items-center justify-between gap-3 py-3">
                  <span className="font-mono text-sm">{r.requester.username}</span>
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
          </RuledList>
        </Section>
      ) : null}

      {requests.outgoing.length > 0 ? (
        <Section label="Sent">
          <RuledList>
            {requests.outgoing.map((r) => (
              <li key={r.addresseeId} className="flex items-baseline justify-between gap-3 py-3 text-sm">
                <span className="font-mono">{r.addressee.username}</span>
                <span className="eyebrow">Pending</span>
              </li>
            ))}
          </RuledList>
        </Section>
      ) : null}

      <Section label="Leaderboard" note="You and your friends, by XP.">
        <Ledger entries={leaderboard} currentUserId={userId} period={period} basePath="/friends" />
      </Section>

      <Section label={`Friends (${friends.length})`}>
        {friends.length === 0 ? (
          <p className="reading max-w-[52ch]">No friends yet. Send a request above using their username.</p>
        ) : (
          <RuledList>
            {friends.map((f) => (
              <li key={f.id} className="py-3 font-mono text-sm">
                {f.username}
              </li>
            ))}
          </RuledList>
        )}
      </Section>
    </Page>
  );
}
