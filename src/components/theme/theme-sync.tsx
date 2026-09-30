"use client";

import { useEffect } from "react";
import { useThemeStore } from "@/lib/theme/theme-store";

// Renders nothing -- keeps <html>'s class/data-color-theme in sync with the
// theme store whenever it changes (toggle, settings picker). Waits for
// hasHydrated so it never overwrites the beforeInteractive inline script's
// initial paint with the store's not-yet-rehydrated default state (see
// theme-store.ts and inline-script.ts).
export function ThemeSync() {
  const colorTheme = useThemeStore((s) => s.colorTheme);
  const mode = useThemeStore((s) => s.mode);
  const hasHydrated = useThemeStore((s) => s.hasHydrated);

  useEffect(() => {
    if (!hasHydrated) return;
    const root = document.documentElement;
    root.classList.toggle("dark", mode === "dark");
    if (colorTheme === "fresh-mint") {
      root.removeAttribute("data-color-theme");
    } else {
      root.setAttribute("data-color-theme", colorTheme);
    }
  }, [colorTheme, mode, hasHydrated]);

  return null;
}
