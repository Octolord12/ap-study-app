import type { Metadata } from "next";
import { requireUserId } from "@/lib/auth/session";
import { getDb } from "@/lib/db";
import { updateLeaderboardOptOut } from "@/lib/social/actions";
import { createParentShare, revokeParentShare } from "@/lib/share/actions";
import { PARENT_LINK_DAYS } from "@/lib/share/constants";
import { getActiveParentShare } from "@/lib/share/queries";
import { ParentShareManager } from "@/components/share/parent-share-manager";
import { Button } from "@/components/ui/button";
import { ActionRow, Page, PageHeader, Section } from "@/components/ui/page";
import { ThemeSettings } from "@/components/theme/theme-settings";
import { ChangePasswordForm } from "@/components/account/change-password-form";
import { DeleteAccountForm } from "@/components/account/delete-account-form";

export const metadata: Metadata = { title: "Settings" };

// Calendar dates in UTC, formatted on the server, so the server's render and the browser's agree.
const formatShareDate = (d: Date) => d.toLocaleDateString("en-US", { month: "long", day: "numeric", year: "numeric", timeZone: "UTC" });

export default async function SettingsPage() {
  const userId = await requireUserId();
  const db = getDb();
  const [user, ownedClasses, activeShare] = await Promise.all([
    db.user.findUniqueOrThrow({ where: { id: userId }, select: { leaderboardOptOut: true, username: true, displayName: true } }),
    db.class.findMany({ where: { ownerId: userId }, orderBy: { name: "asc" }, select: { id: true, name: true, _count: { select: { memberships: true } } } }),
    getActiveParentShare(userId),
  ]);

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

      <Section label="Share with a parent" note="Read-only. You control it.">
        <ParentShareManager
          active={
            activeShare
              ? {
                  created: formatShareDate(activeShare.createdAt),
                  expires: formatShareDate(activeShare.expiresAt),
                  lastViewed: activeShare.lastViewedAt ? formatShareDate(activeShare.lastViewedAt) : null,
                }
              : null
          }
          days={PARENT_LINK_DAYS}
          createAction={createParentShare}
          revokeAction={revokeParentShare}
        />
      </Section>

      <Section label="Password" note="You'll need your current one. Changing it signs out your other devices.">
        <ChangePasswordForm />
      </Section>

      <Section label="Delete account" note="Permanent.">
        <DeleteAccountForm ownedClasses={ownedClasses.map((c) => ({ id: c.id, name: c.name, otherMembers: Math.max(0, c._count.memberships - 1) }))} />
      </Section>
    </Page>
  );
}
