import type { Metadata } from "next";
import Link from "next/link";
import { Page, PageHeader } from "@/components/ui/page";

export const metadata: Metadata = { title: "Account deleted", robots: { index: false } };

export default function AccountDeletedPage() {
  return (
    <Page>
      <PageHeader
        eyebrow="Account"
        title="Your account has been deleted."
        description="Your answers, progress and everything else tied to the account are gone. Ordinary server logs kept by the site's host are not part of the account."
      />
      <p className="reading mt-8 max-w-[56ch]">
        You are welcome back any time with a new account.{" "}
        <Link href="/" className="font-semibold underline underline-offset-4 hover:bg-mark hover:text-on-mark hover:no-underline">
          Back to the home page
        </Link>
        .
      </p>
    </Page>
  );
}
