import { createHash, randomBytes } from "node:crypto";
import { PARENT_LINK_DAYS } from "@/lib/share/constants";

const TOKEN_BYTES = 32;
const TOKEN_PATTERN = /^[A-Za-z0-9_-]{43}$/; // 32 bytes as base64url
const DAY_MS = 24 * 60 * 60 * 1000;

// Only this hash is stored, so a copy of the table is not a set of working links. The prefix keeps it from ever equalling another kind of
// token's hash (the password-reset codes use the same primitive).
export function hashShareToken(token: string): string {
  return createHash("sha256").update(`parent-share:v1:${token}`).digest("hex");
}

export function newShareToken(now: Date = new Date(), bytes: (n: number) => Buffer = randomBytes): { token: string; tokenHash: string; expiresAt: Date } {
  const token = bytes(TOKEN_BYTES).toString("base64url");
  return { token, tokenHash: hashShareToken(token), expiresAt: new Date(now.getTime() + PARENT_LINK_DAYS * DAY_MS) };
}

// Cheap shape check so junk in the URL never reaches the database.
export function looksLikeShareToken(value: unknown): value is string {
  return typeof value === "string" && TOKEN_PATTERN.test(value);
}

export function isShareUsable(share: { revokedAt: Date | null; expiresAt: Date }, now: Date = new Date()): boolean {
  return share.revokedAt === null && share.expiresAt.getTime() > now.getTime();
}
