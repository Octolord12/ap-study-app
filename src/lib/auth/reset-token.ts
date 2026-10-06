import { createHash, randomBytes } from "node:crypto";
import { RESET_TOKEN_MINUTES } from "@/lib/auth/reset-constants";

const TOKEN_BYTES = 32;
const TOKEN_PATTERN = /^[A-Za-z0-9_-]{43}$/; // 32 bytes as base64url

// The emailed code is the secret. Only its hash is stored, so a copy of the table is not a set of working links.
export function hashResetToken(token: string): string {
  return createHash("sha256").update(token).digest("hex");
}

export function newResetToken(now: Date = new Date(), bytes: (n: number) => Buffer = randomBytes): { token: string; tokenHash: string; expiresAt: Date } {
  const token = bytes(TOKEN_BYTES).toString("base64url");
  return { token, tokenHash: hashResetToken(token), expiresAt: new Date(now.getTime() + RESET_TOKEN_MINUTES * 60_000) };
}

// Cheap shape check so junk in the URL never reaches the database.
export function looksLikeResetToken(value: unknown): value is string {
  return typeof value === "string" && TOKEN_PATTERN.test(value);
}
