"use client";

import { useSoundStore } from "@/lib/gamification/sound-store";
import { Button } from "@/components/ui/button";

export function SoundToggle() {
  const muted = useSoundStore((s) => s.muted);
  const toggleMuted = useSoundStore((s) => s.toggleMuted);

  return (
    <Button
      type="button"
      variant="ghost"
      size="icon"
      nativeButton
      onClick={toggleMuted}
      aria-label={muted ? "Unmute sound effects" : "Mute sound effects"}
      title={muted ? "Unmute sound effects" : "Mute sound effects"}
    >
      {muted ? "🔇" : "🔊"}
    </Button>
  );
}
