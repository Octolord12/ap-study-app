"use client";

import { useSoundStore } from "@/lib/gamification/sound-store";

// Synthesized tones via the Web Audio API rather than audio files -- no
// assets to source/license, and the effects we need (a ding, a little
// arpeggio) are simple enough that a few oscillators sound fine. Swap in
// real audio files later if the sound design needs to get fancier.
let audioContext: AudioContext | null = null;

function getContext(): AudioContext | null {
  if (typeof window === "undefined") return null;
  if (!audioContext) {
    const AudioContextClass = window.AudioContext ?? (window as unknown as { webkitAudioContext?: typeof AudioContext }).webkitAudioContext;
    if (!AudioContextClass) return null;
    audioContext = new AudioContextClass();
  }
  return audioContext;
}

function playTone(frequency: number, startTime: number, duration: number, gain = 0.15) {
  if (useSoundStore.getState().muted) return;

  const ctx = getContext();
  if (!ctx) return;

  const osc = ctx.createOscillator();
  const gainNode = ctx.createGain();
  osc.type = "sine";
  osc.frequency.value = frequency;
  gainNode.gain.setValueAtTime(gain, ctx.currentTime + startTime);
  gainNode.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + startTime + duration);
  osc.connect(gainNode);
  gainNode.connect(ctx.destination);
  osc.start(ctx.currentTime + startTime);
  osc.stop(ctx.currentTime + startTime + duration);
}

export function playCorrectSound() {
  playTone(880, 0, 0.15);
}

export function playLevelUpSound() {
  [523.25, 659.25, 783.99, 1046.5].forEach((freq, i) => playTone(freq, i * 0.1, 0.2));
}

export function playBadgeSound() {
  [659.25, 783.99, 987.77].forEach((freq, i) => playTone(freq, i * 0.08, 0.25));
}

export function playBossHitSound() {
  playTone(220, 0, 0.1, 0.2);
}

export function playBossDefeatedSound() {
  [392, 523.25, 659.25, 783.99, 1046.5].forEach((freq, i) => playTone(freq, i * 0.12, 0.3));
}
