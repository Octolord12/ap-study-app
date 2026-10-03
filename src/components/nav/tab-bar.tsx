"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { BookOpen, CalendarCheck, GraduationCap, LayoutDashboard, Users } from "lucide-react";
import { cn } from "cn";
import { isActive } from "@/components/nav/nav-link";

const TABS = [
  { href: "/", label: "Today", Icon: CalendarCheck, exact: true },
  { href: "/courses", label: "Courses", Icon: BookOpen },
  { href: "/dashboard", label: "Progress", Icon: LayoutDashboard },
  { href: "/friends", label: "Friends", Icon: Users },
  { href: "/classes", label: "Classes", Icon: GraduationCap },
] as const;

// Phone navigation. A study app is used in short sessions on a phone, so the
// five places you go sit under the thumb instead of behind a menu.
export function TabBar() {
  const pathname = usePathname();
  return (
    <>
      <nav
        aria-label="Primary"
        className="fixed inset-x-0 bottom-0 z-40 border-t-2 border-foreground bg-background pb-[env(safe-area-inset-bottom)] lg:hidden"
      >
        <ul className="grid grid-cols-5">
          {TABS.map(({ href, label, Icon, ...rest }) => {
            const active = isActive(pathname, href, "exact" in rest ? rest.exact : false);
            return (
              <li key={href}>
                <Link
                  href={href}
                  aria-current={active ? "page" : undefined}
                  className="flex min-h-14 flex-col items-center justify-center gap-1 text-[0.6875rem] font-semibold"
                >
                  <Icon className="size-5" strokeWidth={active ? 2.25 : 1.75} aria-hidden />
                  <span className={cn("px-1", active && "bg-mark text-on-mark")}>{label}</span>
                </Link>
              </li>
            );
          })}
        </ul>
      </nav>
      <div className="h-[calc(3.5rem+env(safe-area-inset-bottom))] lg:hidden" aria-hidden />
    </>
  );
}
