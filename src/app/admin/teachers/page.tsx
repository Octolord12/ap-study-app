import type { Metadata } from "next";
import { requireAdminUserId } from "@/lib/admin/session";
import { grantTeacherRole, revokeTeacherRole } from "@/lib/admin/actions";
import { listTeachers } from "@/lib/admin/queries";
import { Button } from "@/components/ui/button";
import { Field } from "@/components/ui/field";
import { Input } from "@/components/ui/input";
import { Breadcrumb, Page, PageHeader, RuledList, Section } from "@/components/ui/page";

export const metadata: Metadata = { title: "Teachers" };

const ERRORS: Record<string, string> = {
  missing: "Enter a username.",
  "not-found": "No account has that username.",
  admin: "That account is an admin already, which includes everything a teacher can do.",
  already: "That account is a teacher already.",
};

export default async function AdminTeachersPage({ searchParams }: { searchParams: Promise<{ error?: string; granted?: string }> }) {
  await requireAdminUserId();
  const { error, granted } = await searchParams;
  const teachers = await listTeachers();

  return (
    <Page>
      <PageHeader
        eyebrow={<Breadcrumb items={[{ label: "Content review", href: "/admin/review" }, { label: "Teachers" }]} />}
        title="Teachers"
        description="Only a teacher can open the teacher area, and only an admin can make one. Owning a class does not."
      />

      <Section label="Make a teacher" note="By username.">
        <form action={grantTeacherRole} className="flex max-w-md flex-wrap items-end gap-3">
          <Field id="username" label="Username" className="min-w-48 flex-1">
            <Input id="username" name="username" required autoComplete="off" autoCapitalize="none" />
          </Field>
          <Button type="submit" size="lg">
            Make teacher
          </Button>
        </form>
        {error ? (
          <p role="alert" className="mt-3 text-sm font-medium text-incorrect">
            {ERRORS[error] ?? "Something went wrong."}
          </p>
        ) : null}
        {granted ? (
          <p role="status" className="mt-3 text-sm font-medium">
            <span className="font-mono">{granted}</span> is a teacher now.
          </p>
        ) : null}
      </Section>

      <Section label={`Teachers (${teachers.length})`}>
        {teachers.length === 0 ? (
          <p className="reading max-w-[52ch]">Nobody yet.</p>
        ) : (
          <RuledList>
            {teachers.map((t) => (
              <li key={t.id} className="flex flex-wrap items-center justify-between gap-3 py-3">
                <span className="font-mono text-sm">{t.username}</span>
                <div className="flex items-center gap-3">
                  <span className="eyebrow">
                    {t._count.ownedClasses} class{t._count.ownedClasses === 1 ? "" : "es"}
                  </span>
                  <form action={revokeTeacherRole.bind(null, t.id)}>
                    <Button type="submit" size="sm" variant="outline" aria-label={`Take the teacher role from ${t.username}`}>
                      Revoke
                    </Button>
                  </form>
                </div>
              </li>
            ))}
          </RuledList>
        )}
      </Section>
    </Page>
  );
}
