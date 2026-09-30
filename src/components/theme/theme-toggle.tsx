"use client";

import { useThemeStore } from "@/lib/theme/theme-store";
import { Button } from "@/components/ui/button";

export function ThemeToggle() {
  const mode = useThemeStore((s) => s.mode);
  const toggleMode = useThemeStore((s) => s.toggleMode);

  return (
    <Button
      type="button"
      variant="ghost"
      size="icon"
      nativeButton
      onClick={toggleMode}
      aria-label={mode === "dark" ? "Switch to light mode" : "Switch to dark mode"}
      title={mode === "dark" ? "Switch to light mode" : "Switch to dark mode"}
    >
      {mode === "dark" ? "☀️" : "🌙"}
    </Button>
  );
}
