// Swatch previews are hardcoded hex, not CSS custom properties, because the
// settings picker needs to show all 4 themes' colors at once regardless of
// which one is currently active -- see globals.css for the real (CSS
// variable) values these mirror for each theme's light mode.
export const COLOR_THEMES = [
  { id: "fresh-mint", label: "Fresh Mint", swatch: { bg: "#F3FBF9", primary: "#0F9488", accent: "#FF6B5D" } },
  { id: "sunrise", label: "Sunrise", swatch: { bg: "#FFF9F2", primary: "#F2622E", accent: "#16A34A" } },
  { id: "deep-study", label: "Deep Study", swatch: { bg: "#F6F4EE", primary: "#1F3A5F", accent: "#C08A2E" } },
  { id: "playground", label: "Playground", swatch: { bg: "#FBF8FF", primary: "#7C3AED", accent: "#EC4899" } },
] as const;

export type ColorTheme = (typeof COLOR_THEMES)[number]["id"];
export type ThemeMode = "light" | "dark";

export const DEFAULT_COLOR_THEME: ColorTheme = "fresh-mint";
export const DEFAULT_THEME_MODE: ThemeMode = "light";

export const THEME_STORAGE_KEY = "ap-study-app:theme";
