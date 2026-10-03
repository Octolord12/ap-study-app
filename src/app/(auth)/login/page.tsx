import type { Metadata } from "next";
import { redirect } from "next/navigation";
import { auth } from "@/lib/auth/config";
import { LoginForm } from "@/components/auth/login-form";
import { Page, PageHeader, Section } from "@/components/ui/page";

export const metadata: Metadata = { title: "Log in" };

export default async function LoginPage() {
  const session = await auth();
  if (session?.user?.id) redirect("/");

  return (
    <Page>
      <PageHeader eyebrow="Account" title="Log in" description="Pick up where you left off." />
      <Section>
        <LoginForm />
      </Section>
    </Page>
  );
}
