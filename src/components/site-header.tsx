import Link from "next/link";
import { auth } from "@/lib/auth/config";
import { logoutAction } from "@/lib/auth/actions";
import { getUserGamificationStats } from "@/lib/gamification/queries";
import { Button } from "@/components/ui/button";
import { SoundToggle } from "@/components/gamification/sound-toggle";
import { ThemeToggle } from "@/components/theme/theme-toggle";
import { SiteHeaderMobileNav } from "@/components/site-header-mobile-nav";

export async function SiteHeader() {
  const session = await auth();
  const stats = session?.user?.id ? await getUserGamificationStats(session.user.id) : null;

  return (
    <header className="relative border-b border-border">
      <div className="mx-auto flex max-w-4xl items-center justify-between px-4 py-3 sm:px-6 sm:py-4">
        <Link href="/" className="shrink-0 font-bold tracking-tight whitespace-nowrap">
          AP Study App
        </Link>
        <SiteHeaderMobileNav>
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
              <span className="flex items-center gap-2 text-xs font-medium text-muted-foreground">
                <span title={`Level ${stats.level}`}>🎓 Lvl {stats.level}</span>
                {stats.currentStreak > 0 ? (
                  <span title={`${stats.currentStreak}-day streak`}>🔥 {stats.currentStreak}</span>
                ) : null}
              </span>
              <SoundToggle />
              <ThemeToggle />
              <span className="text-muted-foreground">{session.user.name}</span>
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
        </SiteHeaderMobileNav>
      </div>
    </header>
  );
}
