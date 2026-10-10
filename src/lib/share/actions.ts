"use server";

import { revalidatePath } from "next/cache";
import { auth } from "@/lib/auth/config";
import { getDb } from "@/lib/db";
import { siteUrl } from "@/lib/email/config";
import { newShareToken } from "@/lib/share/token";

// Like the other Server Actions, these act on the signed-in student's own links, taken from the session and never from anything the browser sends.
async function requireUserId(): Promise<string> {
  const session = await auth();
  if (!session?.user?.id) throw new Error("Not authenticated");
  return session.user.id;
}

// Makes the student's one live link. Any earlier link stops working in the same transaction, so there is never more than one. The address
// comes from configuration, not from the request's Host header (a link built from the Host header could be pointed at someone else's site),
// and the secret is returned only here: afterwards only its hash exists.
export async function createParentShare(): Promise<{ url: string }> {
  const userId = await requireUserId();
  const { token, tokenHash, expiresAt } = newShareToken();

  await getDb().$transaction(async (tx) => {
    await tx.parentShare.updateMany({ where: { userId, revokedAt: null }, data: { revokedAt: new Date() } });
    await tx.parentShare.create({ data: { userId, tokenHash, expiresAt } });
  });
  revalidatePath("/settings");
  return { url: `${siteUrl()}/share/${token}` };
}

export async function revokeParentShare(): Promise<void> {
  const userId = await requireUserId();
  await getDb().parentShare.updateMany({ where: { userId, revokedAt: null }, data: { revokedAt: new Date() } });
  revalidatePath("/settings");
}
