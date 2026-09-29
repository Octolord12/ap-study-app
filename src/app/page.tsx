import Link from "next/link";
import { auth } from "@/lib/auth/config";
import { Button } from "@/components/ui/button";

export default async function Home() {
  const session = await auth();

  return (
    <div className="mx-auto flex max-w-2xl flex-1 flex-col items-center justify-center gap-6 px-6 text-center">
      <h1 className="text-4xl font-bold tracking-tight">Study smarter for your AP exams</h1>
      <p className="max-w-md text-muted-foreground">
        Quizzes, timed practice, and FRQ practice with streaks, XP, and leaderboards to keep you going.
      </p>
      <div className="flex gap-3">
        {session?.user ? (
          <Button render={<Link href="/courses" />} nativeButton={false} size="lg">
            Go to courses
          </Button>
        ) : (
          <>
            <Button render={<Link href="/signup" />} nativeButton={false} size="lg">
              Get started
            </Button>
            <Button render={<Link href="/login" />} nativeButton={false} size="lg" variant="outline">
              Log in
            </Button>
          </>
        )}
      </div>
    </div>
  );
}
