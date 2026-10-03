"use client";

import { Moon, Sun } from "lucide-react";
import { isDarkMode, useThemeStore } from "@/lib/theme/theme-store";
import { Button } from "@/components/ui/button";

export function ThemeToggle() {
  const mode = useThemeStore((s) => s.mode);
  const hasHydrated = useThemeStore((s) => s.hasHydrated);
  const toggleMode = useThemeStore((s) => s.toggleMode);
  // Before hydration the store only has its default, so don't claim a mode
  // the inline script may have overridden.
  const dark = hasHydrated && isDarkMode(mode);
  const label = dark ? "Switch to light mode" : "Switch to dark mode";

  return (
    <Button type="button" variant="ghost" size="icon" nativeButton onClick={toggleMode} aria-label={label} title={label}>
      {dark ? <Sun aria-hidden /> : <Moon aria-hidden />}
    </Button>
  );
}
