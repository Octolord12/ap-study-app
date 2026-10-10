import { getDb } from "@/lib/db";
import { hashShareToken, isShareUsable, looksLikeShareToken } from "@/lib/share/token";

const HOUR_MS = 60 * 60 * 1000;

// What the student's own settings page shows about their live link (never the secret; only its hash exists).
export function getActiveParentShare(userId: string, now: Date = new Date()) {
  return getDb().parentShare.findFirst({
    where: { userId, revokedAt: null, expiresAt: { gt: now } },
    orderBy: { createdAt: "desc" },
    select: { createdAt: true, expiresAt: true, lastViewedAt: true },
  });
}

// The share a link points at, or null for anything that is not a live link: malformed, unknown, revoked or expired all look the same to the
// caller (and so to the visitor). Returns only the owner's id and username, never their name or email.
export async function findUsableShare(token: string, now: Date = new Date()) {
  if (!looksLikeShareToken(token)) return null;
  const share = await getDb().parentShare.findUnique({
    where: { tokenHash: hashShareToken(token) },
    select: { id: true, expiresAt: true, revokedAt: true, user: { select: { id: true, username: true } } },
  });
  if (!share || !isShareUsable(share, now)) return null;
  return { id: share.id, expiresAt: share.expiresAt, userId: share.user.id, username: share.user.username };
}

// So the student can see whether the link has been opened. At most once an hour, so a refresh loop or a link preview is not a write each time.
export function recordShareView(shareId: string, now: Date = new Date()) {
  return getDb().parentShare.updateMany({
    where: { id: shareId, OR: [{ lastViewedAt: null }, { lastViewedAt: { lt: new Date(now.getTime() - HOUR_MS) } }] },
    data: { lastViewedAt: now },
  });
}
