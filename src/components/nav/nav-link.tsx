"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { cn } from "cn";

function isActive(pathname: string, href: string, exact?: boolean) {
  return exact ? pathname === href : pathname === href || pathname.startsWith(`${href}/`);
}

// Desktop nav link. The current page is the highlighted word, same device as
// everywhere else in the app.
export function NavLink({ href, exact, children }: { href: string; exact?: boolean; children: React.ReactNode }) {
  const active = isActive(usePathname(), href, exact);
  return (
    <Link
      href={href}
      aria-current={active ? "page" : undefined}
      className={cn(
        "px-1.5 py-1 text-sm font-semibold",
        active ? "bg-mark text-on-mark" : "text-foreground underline-offset-4 hover:underline"
      )}
    >
      {children}
    </Link>
  );
}

export { isActive };
