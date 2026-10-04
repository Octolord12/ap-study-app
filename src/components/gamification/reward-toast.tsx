"use client";

import { useEffect } from "react";
import { motion, useReducedMotion } from "framer-motion";
import confetti from "canvas-confetti";
import { playBadgeSound, playCorrectSound, playLevelUpSound } from "@/lib/gamification/sound";
import type { BadgeDefinition } from "@/lib/gamification/badges";
import { BadgeStamp, TitleStamp } from "@/components/ui/stamp";

export interface Reward {
  xpAwarded: number;
  leveledUp: boolean;
  newLevel: number;
  newBadges: BadgeDefinition[];
  newTitle?: { title: string; unitNumber: number } | null;
}

export function hasReward(reward: Reward | null): reward is Reward {
  return reward !== null && (reward.xpAwarded > 0 || reward.leveledUp || reward.newBadges.length > 0 || Boolean(reward.newTitle));
}

// Renders one reward "burst" and auto-dismisses. The parent should key this
// by something unique per reward (e.g. an incrementing counter) so a second
// reward while one is still showing mounts a fresh instance and re-fires the
// sound/confetti/timer rather than reusing stale state.
export function RewardToast({ reward, onDismiss }: { reward: Reward; onDismiss: () => void }) {
  const shouldReduceMotion = useReducedMotion();
  // A title is as rare as a badge, so it gets the same fanfare.
  const earnedSomething = reward.newBadges.length > 0 || Boolean(reward.newTitle);
  const big = reward.leveledUp || earnedSomething;

  useEffect(() => {
    if (earnedSomething) {
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
      initial={shouldReduceMotion ? false : { opacity: 0, y: -12, scale: 0.97 }}
      animate={{ opacity: 1, y: 0, scale: 1 }}
      exit={shouldReduceMotion ? { opacity: 0 } : { opacity: 0, y: -12 }}
      role="status"
      className="fixed top-4 left-1/2 z-50 flex w-[calc(100vw-2rem)] max-w-xs -translate-x-1/2 flex-col items-stretch gap-2"
    >
      {reward.xpAwarded > 0 ? (
        <div className="flex items-baseline justify-center gap-2 bg-foreground px-4 py-2 text-background">
          <span className="numeral text-2xl">+{reward.xpAwarded}</span>
          <span className="eyebrow !text-background">XP</span>
        </div>
      ) : null}
      {reward.leveledUp ? (
        <div className="border-2 border-foreground bg-mark px-4 py-3 text-on-mark">
          <p className="eyebrow !text-on-mark">Level up</p>
          <p className="mt-1 flex items-baseline gap-2">
            <span className="numeral text-4xl">{reward.newLevel}</span>
            <span className="text-sm font-semibold">You&apos;re now level {reward.newLevel}.</span>
          </p>
        </div>
      ) : null}
      {reward.newTitle ? (
        <div className="flex items-center gap-3 border-2 border-foreground bg-card p-3 text-card-foreground">
          <TitleStamp unitNumber={reward.newTitle.unitNumber} className="size-14 shrink-0" />
          <div className="min-w-0">
            <p className="eyebrow">Title earned</p>
            <p className="heading text-lg">{reward.newTitle.title}</p>
          </div>
        </div>
      ) : null}
      {reward.newBadges.map((badge) => (
        <div key={badge.slug} className="flex items-center gap-3 border-2 border-foreground bg-card p-3 text-card-foreground">
          <BadgeStamp slug={badge.slug} className="size-14 shrink-0" />
          <div className="min-w-0">
            <p className="eyebrow">Badge earned</p>
            <p className="heading text-lg">{badge.name}</p>
            <p className="text-xs text-muted-foreground">{badge.description}</p>
          </div>
        </div>
      ))}
    </motion.div>
  );
}
