import Link from "next/link";
import { auth } from "@/lib/auth/config";
import { logoutAction } from "@/lib/auth/actions";
import { getUserGamificationStats } from "@/lib/gamification/queries";
import { Button } from "@/components/ui/button";
import { SoundToggle } from "@/components/gamification/sound-toggle";

export async function SiteHeader() {
  const session = await auth();
  const stats = session?.user?.id ? await getUserGamificationStats(session.user.id) : null;

  return (
    <header className="border-b border-border">
      <div className="mx-auto flex max-w-4xl items-center justify-between px-6 py-4">
        <Link href="/" className="font-bold tracking-tight">
          AP Study App
        </Link>
        <nav className="flex flex-wrap items-center justify-end gap-x-4 gap-y-1 text-sm">
          {session?.user && stats ? (
            <>
              <Link href="/courses" className="text-muted-foreground hover:text-foreground">
                Courses
              </Link>
              <Link href="/dashboard" className="text-muted-foreground hover:text-foreground">
                Dashboard
              </Link>
              <Link href="/friends" className="text-muted-foreground hover:text-foreground">
                Friends
              </Link>
              <Link href="/classes" className="text-muted-foreground hover:text-foreground">
                Classes
              </Link>
              <Link href="/settings" className="text-muted-foreground hover:text-foreground">
                Settings
              </Link>
              <span className="hidden items-center gap-2 text-xs font-medium text-muted-foreground sm:flex">
                <span title={`Level ${stats.level}`}>🎓 Lvl {stats.level}</span>
                {stats.currentStreak > 0 ? (
                  <span title={`${stats.currentStreak}-day streak`}>🔥 {stats.currentStreak}</span>
                ) : null}
              </span>
              <SoundToggle />
              <span className="hidden text-muted-foreground md:inline">{session.user.name}</span>
              <form action={logoutAction}>
                <Button type="submit" variant="outline" size="sm">
                  Log out
                </Button>
              </form>
            </>
          ) : (
            <>
              <Link href="/login" className="text-muted-foreground hover:text-foreground">
                Log in
              </Link>
              <Button render={<Link href="/signup" />} nativeButton={false} size="sm">
                Sign up
              </Button>
            </>
          )}
        </nav>
      </div>
    </header>
  );
}
