import type { Metadata } from "next";
import Link from "next/link";
import { requireUserId } from "@/lib/auth/session";
import { listCourses } from "@/lib/study/queries";
import { getMyClasses } from "@/lib/social/queries";
import { createClass, joinClass } from "@/lib/social/actions";
import { Button } from "@/components/ui/button";
import { Field } from "@/components/ui/field";
import { Input } from "@/components/ui/input";
import { Select } from "@/components/ui/select";
import { Page, PageHeader, RuledList, Section } from "@/components/ui/page";

export const metadata: Metadata = { title: "Classes" };

const ERROR_MESSAGES: Record<string, string> = {
  "missing-code": "Enter an invite code.",
  "not-found": "No class found with that invite code.",
};

export default async function ClassesPage({ searchParams }: { searchParams: Promise<{ error?: string }> }) {
  const userId = await requireUserId();
  const { error } = await searchParams;

  const [classes, courses] = await Promise.all([getMyClasses(userId), listCourses()]);

  return (
    <Page>
      <PageHeader eyebrow="Classes" title="Classes" description="A class is a shared leaderboard for a group, joined with a six-character invite code." />

      <Section label="Your classes">
        {classes.length > 0 ? (
          <RuledList>
            {classes.map((c) => (
              <li key={c.id}>
                <Link href={`/classes/${c.id}`} className="group flex flex-wrap items-baseline justify-between gap-x-6 gap-y-1 py-4">
                  <span className="heading text-xl underline-offset-4 decoration-2 group-hover:underline">{c.name}</span>
                  <span className="eyebrow">
                    {c._count.memberships} member{c._count.memberships === 1 ? "" : "s"}
                    {c.course ? ` · ${c.course.name}` : ""} · {c.myRole === "OWNER" ? "You own this class" : "Member"}
                  </span>
                </Link>
              </li>
            ))}
          </RuledList>
        ) : (
          <p className="reading max-w-[52ch]">You&apos;re not in any classes yet. Join one with a code, or create your own.</p>
        )}
      </Section>

      <Section label="Join a class">
        <form action={joinClass} className="flex max-w-md flex-wrap items-end gap-3">
          <Field id="inviteCode" label="Invite code" className="min-w-40 flex-1">
            <Input id="inviteCode" name="inviteCode" required autoComplete="off" autoCapitalize="characters" maxLength={6} className="font-mono tracking-widest uppercase" />
          </Field>
          <Button type="submit" size="lg">
            Join
          </Button>
        </form>
        {error ? (
          <p role="alert" className="mt-3 text-sm font-medium text-incorrect">
            {ERROR_MESSAGES[error] ?? "Something went wrong."}
          </p>
        ) : null}
      </Section>

      <Section label="Create a class">
        <form action={createClass} className="grid max-w-sm gap-5">
          <Field id="name" label="Name">
            <Input id="name" name="name" required placeholder="Period 3 AP CSA" />
          </Field>
          <Field id="courseId" label="Course" hint="Optional.">
            <Select id="courseId" name="courseId" defaultValue="">
              <option value="">Any</option>
              {courses.map((course) => (
                <option key={course.id} value={course.id}>
                  {course.name}
                </option>
              ))}
            </Select>
          </Field>
          <div>
            <Button type="submit" size="lg">
              Create class
            </Button>
          </div>
        </form>
      </Section>
    </Page>
  );
}
