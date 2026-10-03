export type ThemeMode = "light" | "dark" | "system";

// New accounts start in light, regardless of the device setting; "system" is
// an explicit opt-in from Settings > Appearance.
export const DEFAULT_THEME_MODE: ThemeMode = "light";

export const THEME_STORAGE_KEY = "ap-study-app:theme";
