"use client";

import { useEffect } from "react";
import { isDarkMode, useThemeStore } from "@/lib/theme/theme-store";

// Renders nothing -- keeps <html>'s `dark` class in sync with the theme store
// whenever it changes (toggle, settings picker, or the device setting while
// in "system" mode). Waits for hasHydrated so it never overwrites the
// beforeInteractive inline script's initial paint with the store's
// not-yet-rehydrated default state (see theme-store.ts and inline-script.ts).
export function ThemeSync() {
  const mode = useThemeStore((s) => s.mode);
  const hasHydrated = useThemeStore((s) => s.hasHydrated);

  useEffect(() => {
    if (!hasHydrated) return;
    const root = document.documentElement;
    const apply = () => root.classList.toggle("dark", isDarkMode(mode));
    apply();
    if (mode !== "system") return;
    const query = window.matchMedia("(prefers-color-scheme: dark)");
    query.addEventListener("change", apply);
    return () => query.removeEventListener("change", apply);
  }, [mode, hasHydrated]);

  return null;
}
