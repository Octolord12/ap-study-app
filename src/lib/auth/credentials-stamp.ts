import { createHash } from "node:crypto";

// A short fingerprint of an account's password hash. Every sign-in token carries the
// fingerprint it was issued with, and the token is only honoured while it still matches
// the account's current one. Changing the password changes the hash (bcrypt salts every
// hash, so even re-using the old password gives a new one), which retires every token
// issued before, on every device. The fingerprint travels inside the encrypted token
// and is never shown to the browser.
export function credentialsStamp(passwordHash: string | null): string {
  return createHash("sha256")
    .update(passwordHash ?? "")
    .digest("hex")
    .slice(0, 24);
}

export type StampVerdict = { ok: true; stamp: string } | { ok: false };

// `currentStamp` is null when the account no longer exists (deleted). A token with no
// stamp predates this check: it is accepted and stamped from now on, so shipping the
// check didn't sign everyone out, but it also means a device signed in before then isn't
// covered by a password change until it next refreshes its token.
export function judgeStamp(tokenStamp: string | undefined, currentStamp: string | null): StampVerdict {
  if (currentStamp === null) return { ok: false };
  if (!tokenStamp) return { ok: true, stamp: currentStamp };
  return tokenStamp === currentStamp ? { ok: true, stamp: tokenStamp } : { ok: false };
}
