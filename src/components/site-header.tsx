import Link from "next/link";
import { auth } from "@/lib/auth/config";
import { logoutAction } from "@/lib/auth/actions";
import { getUserGamificationStats } from "@/lib/gamification/queries";
import { Button } from "@/components/ui/button";
import { Tally } from "@/components/ui/tally";
import { ThemeToggle } from "@/components/theme/theme-toggle";
import { NavLink } from "@/components/nav/nav-link";
import { AccountMenu } from "@/components/nav/account-menu";

export function Wordmark() {
  return (
    <Link href="/" className="display flex shrink-0 items-center gap-2 text-lg whitespace-nowrap uppercase sm:text-[1.375rem]">
      <span aria-hidden className="block size-3.5 rounded-full border-2 border-foreground bg-mark" />
      AP Study App
    </Link>
  );
}

export async function SiteHeader() {
  const session = await auth();
  const stats = session?.user?.id ? await getUserGamificationStats(session.user.id) : null;
  const signedIn = Boolean(session?.user && stats);

  return (
    <header className="border-b-2 border-foreground bg-background">
      <div className="mx-auto flex h-14 w-full max-w-[67.5rem] items-center justify-between gap-4 px-4 sm:px-6">
        <div className="flex items-center gap-8">
          <Wordmark />
          {signedIn ? (
            <nav aria-label="Primary" className="hidden items-center gap-1 lg:flex">
              <NavLink href="/" exact>
                Today
              </NavLink>
              <NavLink href="/courses">Courses</NavLink>
              <NavLink href="/dashboard">Progress</NavLink>
              <NavLink href="/friends">Friends</NavLink>
              <NavLink href="/classes">Classes</NavLink>
            </nav>
          ) : null}
        </div>

        {signedIn && stats ? (
          <div className="flex items-center gap-3 sm:gap-5">
            <Link
              href="/dashboard"
              aria-label={`Level ${stats.level}, ${stats.currentStreak}-day streak. Open progress`}
              className="flex items-center gap-3 sm:gap-4"
            >
              {stats.currentStreak > 0 ? (
                <span className="flex items-center gap-2">
                  <Tally count={stats.currentStreak} className="hidden h-6 w-auto lg:block" />
                  <span className="numeral text-xl">{stats.currentStreak}</span>
                  <span className="eyebrow">
                      day<span className="hidden sm:inline"> streak</span>
                    </span>
                </span>
              ) : null}
              <span className="flex items-baseline gap-1.5">
                <span className="eyebrow">Lvl</span>
                <span className="numeral text-2xl">{stats.level}</span>
              </span>
            </Link>
            <AccountMenu name={session?.user?.name ?? "Account"}>
              <form action={logoutAction}>
                <button
                  type="submit"
                  className="flex min-h-11 w-full items-center px-3 text-left text-sm font-semibold hover:bg-mark hover:text-on-mark"
                >
                  Log out
                </button>
              </form>
            </AccountMenu>
          </div>
        ) : (
          <div className="flex items-center gap-2">
            <span className="hidden sm:block">
              <ThemeToggle />
            </span>
            <Link href="/login" className="px-2 text-sm font-semibold whitespace-nowrap underline-offset-4 hover:underline">
              Log in
            </Link>
            <Button render={<Link href="/signup" />} nativeButton={false} size="sm">
              Sign up
            </Button>
          </div>
        )}
      </div>
    </header>
  );
}
