"use client";

import { Volume2, VolumeX } from "lucide-react";
import { useSoundStore } from "@/lib/gamification/sound-store";
import { Button } from "@/components/ui/button";

export function SoundToggle() {
  const muted = useSoundStore((s) => s.muted);
  const toggleMuted = useSoundStore((s) => s.toggleMuted);
  const label = muted ? "Unmute sound effects" : "Mute sound effects";

  return (
    <Button type="button" variant="ghost" size="icon" nativeButton onClick={toggleMuted} aria-label={label} title={label}>
      {muted ? <VolumeX aria-hidden /> : <Volume2 aria-hidden />}
    </Button>
  );
}
