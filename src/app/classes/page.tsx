import Link from "next/link";
import { requireUserId } from "@/lib/auth/session";
import { listCourses } from "@/lib/study/queries";
import { getMyClasses } from "@/lib/social/queries";
import { createClass, joinClass } from "@/lib/social/actions";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";

const ERROR_MESSAGES: Record<string, string> = {
  "missing-code": "Enter an invite code.",
  "not-found": "No class found with that invite code.",
};

export default async function ClassesPage({ searchParams }: { searchParams: Promise<{ error?: string }> }) {
  const userId = await requireUserId();
  const { error } = await searchParams;

  const [classes, courses] = await Promise.all([getMyClasses(userId), listCourses()]);

  return (
    <div className="mx-auto w-full max-w-2xl px-6 py-10">
      <h1 className="mb-6 text-2xl font-bold tracking-tight">Classes</h1>

      {classes.length > 0 ? (
        <div className="mb-8 space-y-3">
          {classes.map((c) => (
            <Link key={c.id} href={`/classes/${c.id}`}>
              <Card className="transition-colors hover:border-foreground/30">
                <CardHeader>
                  <CardTitle className="text-base">{c.name}</CardTitle>
                </CardHeader>
                <CardContent>
                  <p className="text-xs text-muted-foreground">
                    {c._count.memberships} member{c._count.memberships === 1 ? "" : "s"}
                    {c.course ? ` · ${c.course.name}` : ""} · {c.myRole === "OWNER" ? "You own this class" : "Member"}
                  </p>
                </CardContent>
              </Card>
            </Link>
          ))}
        </div>
      ) : (
        <p className="mb-8 text-sm text-muted-foreground">You&apos;re not in any classes yet.</p>
      )}

      <div className="grid gap-4 sm:grid-cols-2">
        <Card>
          <CardHeader>
            <CardTitle className="text-base">Create a class</CardTitle>
          </CardHeader>
          <CardContent>
            <form action={createClass} className="space-y-3">
              <div className="space-y-2">
                <Label htmlFor="name">Name</Label>
                <Input id="name" name="name" required placeholder="Period 3 AP CSA" />
              </div>
              <div className="space-y-2">
                <Label htmlFor="courseId">Course (optional)</Label>
                <select
                  id="courseId"
                  name="courseId"
                  defaultValue=""
                  className="w-full rounded-md border border-input bg-background px-2 py-1.5 text-sm"
                >
                  <option value="">Any</option>
                  {courses.map((course) => (
                    <option key={course.id} value={course.id}>
                      {course.name}
                    </option>
                  ))}
                </select>
              </div>
              <Button type="submit" className="w-full">
                Create
              </Button>
            </form>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle className="text-base">Join a class</CardTitle>
          </CardHeader>
          <CardContent>
            <form action={joinClass} className="space-y-3">
              <div className="space-y-2">
                <Label htmlFor="inviteCode">Invite code</Label>
                <Input id="inviteCode" name="inviteCode" required placeholder="ABC123" className="uppercase" />
              </div>
              {error ? <p className="text-sm text-destructive">{ERROR_MESSAGES[error] ?? "Something went wrong."}</p> : null}
              <Button type="submit" className="w-full">
                Join
              </Button>
            </form>
          </CardContent>
        </Card>
      </div>
    </div>
  );
}
