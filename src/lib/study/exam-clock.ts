// The exam's clock is derived from when the attempt started (ExamAttempt.startedAt),
// not from when the page happened to mount, so a reload resumes the real clock
// instead of handing out a fresh one.

export function secondsRemaining(startedAtMs: number, durationMinutes: number, nowMs: number): number {
  const totalMs = durationMinutes * 60_000;
  // A clock that runs behind the server's can't give anyone more than the full time.
  const elapsedMs = Math.max(0, nowMs - startedAtMs);
  return Math.max(0, Math.ceil((totalMs - elapsedMs) / 1000));
}

// Kept out of components: they must not call Date.now() while rendering.
export function examSecondsLeft(startedAt: Date, durationMinutes: number): number {
  return secondsRemaining(startedAt.getTime(), durationMinutes, Date.now());
}
