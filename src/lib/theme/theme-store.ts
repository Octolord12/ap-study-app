"use client";

import { create } from "zustand";
import { persist } from "zustand/middleware";
import { DEFAULT_THEME_MODE, THEME_STORAGE_KEY, type ThemeMode } from "@/lib/theme/constants";

interface ThemeStore {
  mode: ThemeMode;
  // False until zustand's persist middleware has read localStorage on the
  // client. ThemeSync waits for this before touching the DOM, so it never
  // clobbers what the beforeInteractive inline script (inline-script.ts)
  // already painted with the real persisted values.
  hasHydrated: boolean;
  setMode: (mode: ThemeMode) => void;
  toggleMode: () => void;
  setHasHydrated: (hasHydrated: boolean) => void;
}

export function prefersDark(): boolean {
  return typeof window !== "undefined" && window.matchMedia("(prefers-color-scheme: dark)").matches;
}

export function isDarkMode(mode: ThemeMode): boolean {
  return mode === "dark" || (mode === "system" && prefersDark());
}

// Per-device UI preference, same reasoning as sound-store.ts: localStorage,
// never server state. Older installs also persisted a `colorTheme` (the
// retired four-palette picker); persist ignores keys it no longer knows.
export const useThemeStore = create<ThemeStore>()(
  persist(
    (set) => ({
      mode: DEFAULT_THEME_MODE,
      hasHydrated: false,
      setMode: (mode) => set({ mode }),
      // The header toggle always flips what the student is looking at right
      // now, so under "system" it picks the opposite of the device setting.
      toggleMode: () => set((s) => ({ mode: isDarkMode(s.mode) ? "light" : "dark" })),
      setHasHydrated: (hasHydrated) => set({ hasHydrated }),
    }),
    {
      name: THEME_STORAGE_KEY,
      partialize: (state) => ({ mode: state.mode }),
      // `state` here is the live store instance (actions included), not a
      // plain snapshot -- calling its own setter avoids referencing the
      // `useThemeStore` const above, which for synchronous storage like
      // localStorage is still in its temporal dead zone when this callback
      // first runs (rehydration completes inside the create() call itself).
      onRehydrateStorage: () => (state) => {
        state?.setHasHydrated(true);
      },
    },
  ),
);
