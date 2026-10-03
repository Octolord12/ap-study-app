import type { Metadata } from "next";
import { requireUserId } from "@/lib/auth/session";
import { getDb } from "@/lib/db";
import { updateLeaderboardOptOut } from "@/lib/social/actions";
import { Button } from "@/components/ui/button";
import { ActionRow, Page, PageHeader, Section } from "@/components/ui/page";
import { ThemeSettings } from "@/components/theme/theme-settings";

export const metadata: Metadata = { title: "Settings" };

export default async function SettingsPage() {
  const userId = await requireUserId();
  const user = await getDb().user.findUniqueOrThrow({
    where: { id: userId },
    select: { leaderboardOptOut: true, username: true, displayName: true },
  });

  const setOptOut = updateLeaderboardOptOut.bind(null, !user.leaderboardOptOut);

  return (
    <Page>
      <PageHeader eyebrow="Settings" title="Settings" />

      <Section label="Appearance" note="Saved on this device only.">
        <ThemeSettings />
      </Section>

      <Section label="Privacy" note="What other students can see.">
        <ActionRow
          action={
            <form action={setOptOut}>
              <Button type="submit" variant={user.leaderboardOptOut ? "default" : "outline"} size="lg">
                {user.leaderboardOptOut ? "Show me" : "Hide me"}
              </Button>
            </form>
          }
        >
          <p className="heading text-xl">Appear on leaderboards</p>
          <p className="mt-1 text-sm text-muted-foreground">
            {user.leaderboardOptOut
              ? "You're hidden from friend and class leaderboards."
              : "You're visible on the friend and class leaderboards you're part of."}{" "}
            Leaderboards show your username ({user.username}), never your name ({user.displayName}).
          </p>
        </ActionRow>
      </Section>
    </Page>
  );
}
