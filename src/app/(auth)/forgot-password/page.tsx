import type { Metadata } from "next";
import Link from "next/link";
import { redirect } from "next/navigation";
import { auth } from "@/lib/auth/config";
import { ForgotPasswordForm } from "@/components/auth/forgot-password-form";
import { Page, PageHeader, Section } from "@/components/ui/page";
import { isPasswordResetAvailable } from "@/lib/email/config";

export const metadata: Metadata = { title: "Forgot your password" };

export default async function ForgotPasswordPage() {
  const session = await auth();
  if (session?.user?.id) redirect("/settings");

  return (
    <Page>
      <PageHeader eyebrow="Account" title="Forgot your password?" description="Enter your email and we will send you a link to choose a new one." />
      <Section>
        {isPasswordResetAvailable() ? (
          <ForgotPasswordForm />
        ) : (
          <div className="max-w-md space-y-4">
            <p className="reading">Password reset isn&apos;t available yet.</p>
            <Link href="/login" className="text-sm font-semibold underline underline-offset-4 hover:bg-mark hover:text-on-mark hover:no-underline">
              Back to log in
            </Link>
          </div>
        )}
      </Section>
    </Page>
  );
}
