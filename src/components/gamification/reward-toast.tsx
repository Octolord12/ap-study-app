"use client";

import { useEffect } from "react";
import { motion, useReducedMotion } from "framer-motion";
import confetti from "canvas-confetti";
import { playBadgeSound, playCorrectSound, playLevelUpSound } from "@/lib/gamification/sound";
import type { BadgeDefinition } from "@/lib/gamification/badges";

export interface Reward {
  xpAwarded: number;
  leveledUp: boolean;
  newLevel: number;
  newBadges: BadgeDefinition[];
}

export function hasReward(reward: Reward | null): reward is Reward {
  return reward !== null && (reward.xpAwarded > 0 || reward.leveledUp || reward.newBadges.length > 0);
}

// Renders one reward "burst" and auto-dismisses. The parent should key this
// by something unique per reward (e.g. an incrementing counter) so a second
// reward while one is still showing mounts a fresh instance and re-fires the
// sound/confetti/timer rather than reusing stale state.
export function RewardToast({ reward, onDismiss }: { reward: Reward; onDismiss: () => void }) {
  const shouldReduceMotion = useReducedMotion();
  const big = reward.leveledUp || reward.newBadges.length > 0;

  useEffect(() => {
    if (reward.newBadges.length > 0) {
      playBadgeSound();
      confetti({ particleCount: 80, spread: 70, origin: { y: 0.3 } });
    } else if (reward.leveledUp) {
      playLevelUpSound();
      confetti({ particleCount: 60, spread: 60, origin: { y: 0.3 } });
    } else if (reward.xpAwarded > 0) {
      playCorrectSound();
    }

    const timeout = setTimeout(onDismiss, big ? 4000 : 1800);
    return () => clearTimeout(timeout);
    // eslint-disable-next-line react-hooks/exhaustive-deps -- fire once per mounted reward, not on every render
  }, []);

  return (
    <motion.div
      initial={shouldReduceMotion ? false : { opacity: 0, y: -12, scale: 0.95 }}
      animate={{ opacity: 1, y: 0, scale: 1 }}
      exit={shouldReduceMotion ? { opacity: 0 } : { opacity: 0, y: -12 }}
      className="fixed top-4 left-1/2 z-50 flex w-[calc(100vw-2rem)] max-w-xs -translate-x-1/2 flex-col items-center gap-2"
    >
      {reward.xpAwarded > 0 ? (
        <div className="rounded-full bg-foreground px-4 py-2 text-sm font-medium text-background shadow-lg">
          +{reward.xpAwarded} XP
        </div>
      ) : null}
      {reward.leveledUp ? (
        <div className="rounded-lg bg-primary px-4 py-3 text-center text-sm font-bold text-primary-foreground shadow-lg">
          🎉 Level up! You&apos;re now level {reward.newLevel}
        </div>
      ) : null}
      {reward.newBadges.map((badge) => (
        <div key={badge.slug} className="rounded-lg border border-border bg-card px-4 py-3 text-center shadow-lg">
          <div className="text-2xl">{badge.icon}</div>
          <div className="text-sm font-semibold">{badge.name}</div>
          <div className="text-xs text-muted-foreground">{badge.description}</div>
        </div>
      ))}
    </motion.div>
  );
}
