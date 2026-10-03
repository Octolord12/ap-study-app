import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { requireUserId } from "@/lib/auth/session";
import { getCourseUnitsWithQuestionCounts } from "@/lib/study/queries";
import { startCustomQuiz } from "@/lib/study/actions";
import { Button } from "@/components/ui/button";
import { Field } from "@/components/ui/field";
import { Input } from "@/components/ui/input";
import { Select } from "@/components/ui/select";
import { Breadcrumb, Page, PageHeader, Section } from "@/components/ui/page";

export const metadata: Metadata = { title: "Custom quiz" };

const ERROR_MESSAGES: Record<string, string> = {
  "no-units": "Pick at least one unit.",
  "no-matches": "No questions match that combination. Try a different difficulty or more units.",
};

export default async function CustomQuizPage({
  params,
  searchParams,
}: {
  params: Promise<{ courseSlug: string }>;
  searchParams: Promise<{ error?: string }>;
}) {
  await requireUserId();
  const { courseSlug } = await params;
  const { error } = await searchParams;

  const course = await getCourseUnitsWithQuestionCounts(courseSlug);
  if (!course) notFound();

  return (
    <Page>
      <PageHeader
        eyebrow={
          <Breadcrumb
            items={[
              { label: course.name, href: `/courses/${course.slug}` },
              { label: "Practice", href: `/courses/${course.slug}/practice` },
              { label: "Custom quiz" },
            ]}
          />
        }
        title="Custom quiz"
        description="Choose what goes in, and the quiz is drawn at random from it."
      />

      <form action={startCustomQuiz}>
        <input type="hidden" name="courseId" value={course.id} />
        <input type="hidden" name="courseSlug" value={course.slug} />

        <Section label="Units" note="Units with no questions are greyed out.">
          <fieldset className="m-0 min-w-0 border-0 p-0">
            <legend className="sr-only">Units</legend>
            <ul className="border-b border-border [&>li]:border-t [&>li]:border-border">
              {course.units.map((unit) => (
                <li key={unit.id}>
                  <label className="flex min-h-12 cursor-pointer items-center gap-3 py-2 text-sm font-medium">
                    <input type="checkbox" className="check" name="unitId" value={unit.id} defaultChecked disabled={unit._count.questions === 0} />
                    <span className="min-w-0 flex-1">{unit.name}</span>
                    <span className="eyebrow shrink-0">{unit._count.questions} questions</span>
                  </label>
                </li>
              ))}
            </ul>
          </fieldset>
        </Section>

        <Section label="Settings">
          <div className="grid max-w-sm gap-5">
            <Field id="difficulty" label="Difficulty">
              <Select id="difficulty" name="difficulty" defaultValue="ANY">
                <option value="ANY">Any</option>
                <option value="EASY">Easy</option>
                <option value="MEDIUM">Medium</option>
                <option value="HARD">Hard</option>
              </Select>
            </Field>
            <Field id="length" label="Number of questions" hint="1 to 50.">
              <Input id="length" name="length" type="number" min={1} max={50} defaultValue={10} />
            </Field>
            {error ? (
              <p role="alert" className="text-sm font-medium text-incorrect">
                {ERROR_MESSAGES[error] ?? "Something went wrong."}
              </p>
            ) : null}
            <div>
              <Button type="submit" size="lg">
                Start quiz
              </Button>
            </div>
          </div>
        </Section>
      </form>
    </Page>
  );
}
