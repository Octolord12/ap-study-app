import type { Metadata } from "next";
import Link from "next/link";
import { ResetPasswordForm } from "@/components/auth/reset-password-form";
import { Page, PageHeader, Section } from "@/components/ui/page";
import { RESET_LINK_INVALID } from "@/lib/auth/reset-constants";
import { isResetLinkUsable } from "@/lib/auth/reset-queries";

// The link carries the secret in its address, so don't let it travel in a Referer header or into a search index.
export const metadata: Metadata = { title: "Choose a new password", referrer: "no-referrer", robots: { index: false, follow: false } };

export default async function ResetPasswordPage({ searchParams }: { searchParams: Promise<{ token?: string }> }) {
  const { token } = await searchParams;
  const usable = typeof token === "string" && (await isResetLinkUsable(token));

  return (
    <Page>
      <PageHeader eyebrow="Account" title="Choose a new password" description={usable ? "You will be signed out everywhere else." : undefined} />
      <Section>
        {usable ? (
          <ResetPasswordForm token={token} />
        ) : (
          <div className="max-w-md space-y-4" role="alert">
            <p className="reading text-lg">{RESET_LINK_INVALID}</p>
            <Link href="/forgot-password" className="text-sm font-semibold underline underline-offset-4 hover:bg-mark hover:text-on-mark hover:no-underline">
              Ask for a new link
            </Link>
          </div>
        )}
      </Section>
    </Page>
  );
}
