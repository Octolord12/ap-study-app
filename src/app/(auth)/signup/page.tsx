import type { Metadata } from "next";
import { redirect } from "next/navigation";
import { auth } from "@/lib/auth/config";
import { SignupForm } from "@/components/auth/signup-form";
import { Page, PageHeader, Section } from "@/components/ui/page";

export const metadata: Metadata = { title: "Create an account" };

export default async function SignupPage() {
  const session = await auth();
  if (session?.user?.id) redirect("/");

  return (
    <Page>
      <PageHeader eyebrow="Account" title="Create your account" description="It takes a minute. Then pick the exam you're studying for." />
      <Section>
        <SignupForm />
      </Section>
    </Page>
  );
}
