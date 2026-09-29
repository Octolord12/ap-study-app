import { notFound } from "next/navigation";
import { requireUserId } from "@/lib/auth/session";
import { getCourseUnitsWithQuestionCounts } from "@/lib/study/queries";
import { startCustomQuiz } from "@/lib/study/actions";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Label } from "@/components/ui/label";
import { Input } from "@/components/ui/input";

const ERROR_MESSAGES: Record<string, string> = {
  "no-units": "Pick at least one unit.",
  "no-matches": "No questions match that combination -- try a different difficulty or more units.",
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
    <div className="mx-auto w-full max-w-2xl px-6 py-10">
      <Card>
        <CardHeader>
          <CardTitle>Custom quiz</CardTitle>
        </CardHeader>
        <CardContent>
          <form action={startCustomQuiz} className="space-y-5">
            <input type="hidden" name="courseId" value={course.id} />
            <input type="hidden" name="courseSlug" value={course.slug} />

            <div>
              <Label className="mb-2 block">Units</Label>
              <div className="space-y-2">
                {course.units.map((unit) => (
                  <label key={unit.id} className="flex items-center gap-2 text-sm">
                    <input type="checkbox" name="unitId" value={unit.id} defaultChecked disabled={unit._count.questions === 0} />
                    {unit.name}
                    <span className="text-xs text-muted-foreground">({unit._count.questions} questions)</span>
                  </label>
                ))}
              </div>
            </div>

            <div className="space-y-2">
              <Label htmlFor="difficulty">Difficulty</Label>
              <select
                id="difficulty"
                name="difficulty"
                defaultValue="ANY"
                className="w-full rounded-md border border-input bg-background px-2 py-1.5 text-sm"
              >
                <option value="ANY">Any</option>
                <option value="EASY">Easy</option>
                <option value="MEDIUM">Medium</option>
                <option value="HARD">Hard</option>
              </select>
            </div>

            <div className="space-y-2">
              <Label htmlFor="length">Number of questions</Label>
              <Input id="length" name="length" type="number" min={1} max={50} defaultValue={10} />
            </div>

            {error ? <p className="text-sm text-destructive">{ERROR_MESSAGES[error] ?? "Something went wrong."}</p> : null}

            <Button type="submit" className="w-full">
              Start quiz
            </Button>
          </form>
        </CardContent>
      </Card>
    </div>
  );
}
