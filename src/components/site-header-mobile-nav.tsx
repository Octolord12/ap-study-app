"use client";

import { useState } from "react";
import { usePathname } from "next/navigation";
import { Menu, X } from "lucide-react";

export function SiteHeaderMobileNav({ children }: { children: React.ReactNode }) {
  const [open, setOpen] = useState(false);
  const [lastPathname, setLastPathname] = useState<string | null>(null);
  const pathname = usePathname();

  // Render-phase state adjustment (React-sanctioned, not an effect): closes
  // the menu whenever the route changes, so it doesn't linger open and
  // cover the page the user just navigated to.
  if (pathname !== lastPathname) {
    setLastPathname(pathname);
    if (open) setOpen(false);
  }

  return (
    <>
      <button
        type="button"
        className="rounded-lg p-1.5 text-muted-foreground hover:bg-muted hover:text-foreground sm:hidden"
        aria-expanded={open}
        aria-controls="site-nav"
        onClick={() => setOpen((o) => !o)}
      >
        <span className="sr-only">{open ? "Close menu" : "Open menu"}</span>
        {open ? <X className="size-5" /> : <Menu className="size-5" />}
      </button>
      <nav
        id="site-nav"
        className={`${open ? "flex" : "hidden"} absolute top-full right-0 left-0 flex-col items-start gap-3 border-b border-border bg-background px-4 py-4 text-sm sm:static sm:flex sm:flex-row sm:flex-wrap sm:items-center sm:justify-end sm:gap-x-4 sm:gap-y-1 sm:border-none sm:px-0 sm:py-0`}
      >
        {children}
      </nav>
    </>
  );
}
