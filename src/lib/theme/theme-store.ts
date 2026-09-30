"use client";

import { create } from "zustand";
import { persist } from "zustand/middleware";
import { DEFAULT_COLOR_THEME, DEFAULT_THEME_MODE, THEME_STORAGE_KEY, type ColorTheme, type ThemeMode } from "@/lib/theme/constants";

interface ThemeStore {
  colorTheme: ColorTheme;
  mode: ThemeMode;
  // False until zustand's persist middleware has read localStorage on the
  // client. ThemeSync waits for this before touching the DOM, so it never
  // clobbers what the beforeInteractive inline script (inline-script.ts)
  // already painted with the real persisted values.
  hasHydrated: boolean;
  setColorTheme: (colorTheme: ColorTheme) => void;
  setMode: (mode: ThemeMode) => void;
  toggleMode: () => void;
  setHasHydrated: (hasHydrated: boolean) => void;
}

// Per-device UI preference, same reasoning as sound-store.ts: localStorage,
// never server state.
export const useThemeStore = create<ThemeStore>()(
  persist(
    (set) => ({
      colorTheme: DEFAULT_COLOR_THEME,
      mode: DEFAULT_THEME_MODE,
      hasHydrated: false,
      setColorTheme: (colorTheme) => set({ colorTheme }),
      setMode: (mode) => set({ mode }),
      toggleMode: () => set((s) => ({ mode: s.mode === "dark" ? "light" : "dark" })),
      setHasHydrated: (hasHydrated) => set({ hasHydrated }),
    }),
    {
      name: THEME_STORAGE_KEY,
      partialize: (state) => ({ colorTheme: state.colorTheme, mode: state.mode }),
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
