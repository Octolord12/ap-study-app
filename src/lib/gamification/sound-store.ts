"use client";

import { create } from "zustand";
import { persist } from "zustand/middleware";

interface SoundStore {
  muted: boolean;
  toggleMuted: () => void;
}

// Purely a per-device UI preference -- localStorage is the right place for
// this (never server state, never something Claude/the app needs to read back).
export const useSoundStore = create<SoundStore>()(
  persist(
    (set) => ({
      muted: false,
      toggleMuted: () => set((s) => ({ muted: !s.muted })),
    }),
    { name: "ap-study-app:sound-muted" },
  ),
);
