import { createHmac, timingSafeEqual } from "node:crypto";

// A boss battle starts when its page is rendered. The server signs "this user
// started this unit's battle at this time" and the browser hands the token back
// on submit, so the start time (which decides which attempts count) can't be
// chosen by the client. Server-only: uses node:crypto, so don't import this from
// a Client Component.

export const BOSS_BATTLE_TOKEN_TTL_MS = 4 * 60 * 60 * 1000;
// Tolerance for the app server and the page's clock disagreeing.
const FUTURE_SKEW_MS = 60 * 1000;
// Keeps this HMAC from being valid anywhere else the same secret is used (Auth.js).
const DOMAIN = "boss-battle:v1:";

export interface BossBattleStart {
  userId: string;
  unitId: string;
  startedAtMs: number;
}

export type BossBattleTokenCheck = { ok: true; start: BossBattleStart } | { ok: false; reason: "invalid" | "expired" };

const b64 = (value: string | Buffer) => Buffer.from(value).toString("base64url");
const mac = (payload: string, secret: string) => createHmac("sha256", secret).update(DOMAIN + payload).digest();

export function signBossBattle(start: BossBattleStart, secret: string): string {
  const payload = b64(JSON.stringify({ u: start.userId, n: start.unitId, t: start.startedAtMs }));
  return `${payload}.${b64(mac(payload, secret))}`;
}

export function verifyBossBattle(token: unknown, secret: string, nowMs: number = Date.now()): BossBattleTokenCheck {
  if (typeof token !== "string") return { ok: false, reason: "invalid" };
  const parts = token.split(".");
  if (parts.length !== 2) return { ok: false, reason: "invalid" };
  const [payload, signature] = parts;

  const expected = mac(payload, secret);
  const given = Buffer.from(signature, "base64url");
  if (given.length !== expected.length || !timingSafeEqual(given, expected)) return { ok: false, reason: "invalid" };

  let data: { u?: unknown; n?: unknown; t?: unknown };
  try {
    data = JSON.parse(Buffer.from(payload, "base64url").toString("utf8"));
  } catch {
    return { ok: false, reason: "invalid" };
  }
  if (typeof data.u !== "string" || typeof data.n !== "string" || typeof data.t !== "number" || !Number.isFinite(data.t)) {
    return { ok: false, reason: "invalid" };
  }
  if (data.t > nowMs + FUTURE_SKEW_MS) return { ok: false, reason: "invalid" };
  if (nowMs - data.t > BOSS_BATTLE_TOKEN_TTL_MS) return { ok: false, reason: "expired" };

  return { ok: true, start: { userId: data.u, unitId: data.n, startedAtMs: data.t } };
}

export function bossBattleSecret(): string {
  const secret = process.env.AUTH_SECRET;
  if (!secret) throw new Error("AUTH_SECRET is not set");
  return secret;
}

// Called when the boss page renders: the battle starts now.
export function startBossBattle(userId: string, unitId: string): string {
  return signBossBattle({ userId, unitId, startedAtMs: Date.now() }, bossBattleSecret());
}
