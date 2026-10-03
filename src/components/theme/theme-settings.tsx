"use client";

import { useThemeStore } from "@/lib/theme/theme-store";
import type { ThemeMode } from "@/lib/theme/constants";
import { cn } from "cn";

const OPTIONS: { value: ThemeMode; label: string; hint: string }[] = [
  { value: "light", label: "Light", hint: "Paper background" },
  { value: "dark", label: "Dark", hint: "For late sessions" },
  { value: "system", label: "Match device", hint: "Follows your phone or laptop" },
];

export function ThemeSettings() {
  const mode = useThemeStore((s) => s.mode);
  const setMode = useThemeStore((s) => s.setMode);

  return (
    <fieldset className="m-0 min-w-0 border-0 p-0">
      <legend className="sr-only">Appearance</legend>
      <div className="grid max-w-xl gap-0 border border-foreground sm:grid-cols-3">
        {OPTIONS.map((option) => (
          <label
            key={option.value}
            className={cn(
              "flex cursor-pointer flex-col gap-0.5 border-b border-foreground px-4 py-3 last:border-b-0 has-[:focus-visible]:outline-2 has-[:focus-visible]:outline-offset-2 has-[:focus-visible]:outline-ring sm:border-r sm:border-b-0 sm:last:border-r-0",
              mode === option.value ? "bg-mark text-on-mark" : "hover:bg-muted"
            )}
          >
            <input
              type="radio"
              name="appearance"
              value={option.value}
              checked={mode === option.value}
              onChange={() => setMode(option.value)}
              className="sr-only"
            />
            <span className="text-sm font-semibold">{option.label}</span>
            <span className={cn("text-xs", mode === option.value ? "text-on-mark" : "text-muted-foreground")}>{option.hint}</span>
          </label>
        ))}
      </div>
    </fieldset>
  );
}
