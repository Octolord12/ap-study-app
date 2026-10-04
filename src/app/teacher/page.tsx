import type { Metadata } from "next";
import Link from "next/link";
import { requireOwnedClasses } from "@/lib/teacher/classes";
import { selectClass } from "@/lib/teacher/select-class";
import type { ClassWeakness } from "@/lib/teacher/types";
import { AssignDailyFive } from "@/components/teacher/assign-daily-five";
import { ClassPicker } from "@/components/teacher/class-picker";
import { ClassWeaknesses } from "@/components/teacher/class-weaknesses";
import { Page, PageHeader, Section } from "@/components/ui/page";

export const metadata: Metadata = { title: "Teacher" };

export default async function TeacherPage({ searchParams }: { searchParams: Promise<{ class?: string }> }) {
  const { classes } = await requireOwnedClasses();
  const { class: requestedId } = await searchParams;
  const selected = selectClass(classes, requestedId)!;

  // No aggregation behind this yet, so the panel shows its empty state.
  const weaknesses: ClassWeakness[] = [];

  return (
    <Page>
      <PageHeader
        eyebrow="Teacher"
        title="Teacher dashboard"
        description="A first look at the tools for running a class. The panels below are not connected to student data yet."
      />

      <Section label="Class" note={classes.length > 1 ? "Choose a class." : undefined}>
        <ClassPicker classes={classes} selectedId={selected.id} />
        <p className="mt-5 text-sm text-muted-foreground">
          {selected.courseName ?? "Any course"} · invite code <span className="font-mono text-foreground">{selected.inviteCode}</span> ·{" "}
          <Link href={`/classes/${selected.id}`} className="font-semibold underline underline-offset-4 hover:bg-mark hover:text-on-mark hover:no-underline">
            Leaderboard and members
          </Link>
        </p>
      </Section>

      <Section label="Class-wide weaknesses" note="Where the class is struggling.">
        <ClassWeaknesses items={weaknesses} />
      </Section>

      <Section label="Daily 5" note="One set for the whole class.">
        <AssignDailyFive />
      </Section>
    </Page>
  );
}
