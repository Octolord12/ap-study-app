"use client";

import { useEffect, useRef, useState } from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { ChevronDown, Moon, Settings, Sun, Volume2, VolumeX } from "lucide-react";
import { useSoundStore } from "@/lib/gamification/sound-store";
import { isDarkMode, useThemeStore } from "@/lib/theme/theme-store";

const ROW =
  "flex min-h-11 w-full items-center justify-between gap-3 px-3 text-left text-sm font-semibold hover:bg-mark hover:text-on-mark";

// Everything that isn't a place you navigate to: settings, appearance, sound,
// log out. `children` is the log-out form (a Server Action, so it has to be
// rendered by the server header and passed in).
export function AccountMenu({ name, children }: { name: string; children: React.ReactNode }) {
  const [open, setOpen] = useState(false);
  const [lastPathname, setLastPathname] = useState<string | null>(null);
  const pathname = usePathname();
  const rootRef = useRef<HTMLDivElement>(null);
  const buttonRef = useRef<HTMLButtonElement>(null);

  const mode = useThemeStore((s) => s.mode);
  const hasHydrated = useThemeStore((s) => s.hasHydrated);
  const toggleMode = useThemeStore((s) => s.toggleMode);
  const muted = useSoundStore((s) => s.muted);
  const toggleMuted = useSoundStore((s) => s.toggleMuted);
  const dark = hasHydrated && isDarkMode(mode);

  // Render-phase state adjustment (not an effect): close the panel whenever
  // the route changes so it doesn't linger over the page just navigated to.
  if (pathname !== lastPathname) {
    setLastPathname(pathname);
    if (open) setOpen(false);
  }

  useEffect(() => {
    if (!open) return;
    const onPointerDown = (e: PointerEvent) => {
      if (!rootRef.current?.contains(e.target as Node)) setOpen(false);
    };
    const onKeyDown = (e: KeyboardEvent) => {
      if (e.key === "Escape") {
        setOpen(false);
        buttonRef.current?.focus();
      }
    };
    document.addEventListener("pointerdown", onPointerDown);
    document.addEventListener("keydown", onKeyDown);
    return () => {
      document.removeEventListener("pointerdown", onPointerDown);
      document.removeEventListener("keydown", onKeyDown);
    };
  }, [open]);

  const initial = name.trim().charAt(0).toUpperCase() || "?";

  return (
    <div ref={rootRef} className="relative">
      <button
        ref={buttonRef}
        type="button"
        aria-expanded={open}
        aria-controls="account-panel"
        onClick={() => setOpen((o) => !o)}
        className="flex h-11 items-center gap-2 pr-1 text-sm font-semibold hover:bg-mark hover:text-on-mark md:pl-2"
      >
        <span className="sr-only">Account menu for {name}</span>
        <span aria-hidden className="grid size-9 place-items-center rounded-full border-[1.5px] border-current">
          {initial}
        </span>
        <span aria-hidden className="hidden max-w-32 truncate md:block">
          {name}
        </span>
        <ChevronDown aria-hidden className="hidden size-4 md:block" />
      </button>
      {open ? (
        <div
          id="account-panel"
          className="absolute top-full right-0 z-50 mt-1 w-64 border border-foreground bg-card py-1 text-card-foreground"
        >
          <p className="eyebrow truncate px-3 py-2">Signed in as {name}</p>
          <Link href="/settings" className={ROW}>
            Settings
            <Settings aria-hidden className="size-4" />
          </Link>
          <button type="button" onClick={toggleMode} className={ROW}>
            {dark ? "Switch to light" : "Switch to dark"}
            {dark ? <Sun aria-hidden className="size-4" /> : <Moon aria-hidden className="size-4" />}
          </button>
          <button type="button" onClick={toggleMuted} className={ROW}>
            {muted ? "Sound is off" : "Sound is on"}
            {muted ? <VolumeX aria-hidden className="size-4" /> : <Volume2 aria-hidden className="size-4" />}
          </button>
          <div className="mt-1 border-t border-border pt-1 [&_button]:w-full [&_button]:justify-between">{children}</div>
        </div>
      ) : null}
    </div>
  );
}
