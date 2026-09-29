import Link from "next/link";
import { auth } from "@/lib/auth/config";
import { logoutAction } from "@/lib/auth/actions";
import { Button } from "@/components/ui/button";

export async function SiteHeader() {
  const session = await auth();

  return (
    <header className="border-b border-border">
      <div className="mx-auto flex max-w-4xl items-center justify-between px-6 py-4">
        <Link href="/" className="font-bold tracking-tight">
          AP Study App
        </Link>
        <nav className="flex items-center gap-4 text-sm">
          {session?.user ? (
            <>
              <Link href="/courses" className="text-muted-foreground hover:text-foreground">
                Courses
              </Link>
              <Link href="/dashboard" className="text-muted-foreground hover:text-foreground">
                Dashboard
              </Link>
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
        </nav>
      </div>
    </header>
  );
}
