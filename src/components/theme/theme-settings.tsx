"use client";

import { COLOR_THEMES } from "@/lib/theme/constants";
import { useThemeStore } from "@/lib/theme/theme-store";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

export function ThemeSettings() {
  const colorTheme = useThemeStore((s) => s.colorTheme);
  const mode = useThemeStore((s) => s.mode);
  const setColorTheme = useThemeStore((s) => s.setColorTheme);
  const setMode = useThemeStore((s) => s.setMode);

  return (
    <Card className="mb-8">
      <CardHeader>
        <CardTitle className="text-base">Appearance</CardTitle>
      </CardHeader>
      <CardContent className="space-y-5">
        <div>
          <p className="mb-2 text-sm font-medium">Mode</p>
          <div className="inline-flex rounded-lg border border-border p-1">
            <Button
              type="button"
              size="sm"
              variant={mode === "light" ? "default" : "ghost"}
              nativeButton
              onClick={() => setMode("light")}
              aria-pressed={mode === "light"}
            >
              Light
            </Button>
            <Button
              type="button"
              size="sm"
              variant={mode === "dark" ? "default" : "ghost"}
              nativeButton
              onClick={() => setMode("dark")}
              aria-pressed={mode === "dark"}
            >
              Dark
            </Button>
          </div>
        </div>

        <div>
          <p className="mb-2 text-sm font-medium">Color theme</p>
          <div className="grid grid-cols-2 gap-3 sm:grid-cols-4">
            {COLOR_THEMES.map((theme) => {
              const selected = colorTheme === theme.id;
              return (
                <button
                  key={theme.id}
                  type="button"
                  onClick={() => setColorTheme(theme.id)}
                  aria-pressed={selected}
                  className={`flex flex-col items-center gap-2 rounded-lg border p-3 text-xs font-medium transition-colors ${
                    selected ? "border-foreground" : "border-border hover:border-foreground/40"
                  }`}
                >
                  <span
                    className="flex h-10 w-10 items-center justify-center rounded-full border border-black/10"
                    style={{ background: theme.swatch.bg }}
                  >
                    <span
                      className="h-4 w-4 rounded-full border border-black/10"
                      style={{ background: theme.swatch.primary }}
                    />
                  </span>
                  {theme.label}
                </button>
              );
            })}
          </div>
        </div>
      </CardContent>
    </Card>
  );
}
