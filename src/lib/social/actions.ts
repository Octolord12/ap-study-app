"use server";

import { revalidatePath } from "next/cache";
import { redirect } from "next/navigation";
import { auth } from "@/lib/auth/config";
import { getDb } from "@/lib/db";
import { normalizeClassName } from "@/lib/social/class-name";
import { generateInviteCode, normalizeInviteCode } from "@/lib/social/invite-code";

async function requireUserId(): Promise<string> {
  const session = await auth();
  if (!session?.user?.id) throw new Error("Not authenticated");
  return session.user.id;
}

const MAX_INVITE_CODE_ATTEMPTS = 5;

// A code no class has now. Not exported: a "use server" file may only export server actions.
async function uniqueInviteCode(db: ReturnType<typeof getDb>): Promise<string> {
  for (let attempt = 0; attempt < MAX_INVITE_CODE_ATTEMPTS; attempt++) {
    const candidate = generateInviteCode();
    const existing = await db.class.findUnique({ where: { inviteCode: candidate } });
    if (!existing) return candidate;
  }
  throw new Error("Could not generate a unique invite code, try again");
}

export async function createClass(formData: FormData): Promise<void> {
  const userId = await requireUserId();
  const db = getDb();

  const name = normalizeClassName(formData.get("name"));
  const courseId = (formData.get("courseId") as string) || null;
  if (!name) throw new Error("Class name is required");

  const inviteCode = await uniqueInviteCode(db);

  const newClass = await db.class.create({
    data: { name, inviteCode, ownerId: userId, courseId },
  });
  await db.classMembership.create({
    data: { classId: newClass.id, userId, role: "OWNER" },
  });

  revalidatePath("/classes");
  redirect(`/classes/${newClass.id}`);
}

export async function renameClass(classId: string, formData: FormData): Promise<void> {
  const userId = await requireUserId();

  const name = normalizeClassName(formData.get("name"));
  if (!name) redirect(`/classes/${classId}?error=name`);

  // Scoped to a class this user owns, so anyone else (a member, or a stranger who guessed an id) matches nothing and nothing changes.
  await getDb().class.updateMany({ where: { id: classId, ownerId: userId }, data: { name } });
  revalidatePath(`/classes/${classId}`);
  revalidatePath("/classes");
  // To the bare page, so an earlier ?error=name doesn't stay on screen after a good save.
  redirect(`/classes/${classId}`);
}

// Remove a member AND stop them rejoining with the invite code. Both writes happen together or not at all, and only when the signed-in user
// owns the class and the person is currently a plain MEMBER (so it can't block the owner, a stranger, or someone in another class).
export async function blockClassMember(classId: string, memberId: string): Promise<void> {
  const userId = await requireUserId();

  await getDb().$transaction(async (tx) => {
    const removed = await tx.classMembership.deleteMany({ where: { classId, userId: memberId, role: "MEMBER", class: { ownerId: userId } } });
    if (removed.count === 0) return;
    await tx.classBan.upsert({ where: { classId_userId: { classId, userId: memberId } }, create: { classId, userId: memberId }, update: {} });
  });
  revalidatePath(`/classes/${classId}`);
  revalidatePath("/classes");
}

export async function unblockClassMember(classId: string, blockedUserId: string): Promise<void> {
  const userId = await requireUserId();

  // Unblocking lets them join again with the invite code; it does not add them back. Only the class's owner can.
  await getDb().classBan.deleteMany({ where: { classId, userId: blockedUserId, class: { ownerId: userId } } });
  revalidatePath(`/classes/${classId}`);
}

export async function transferClassOwnership(classId: string, newOwnerId: string): Promise<void> {
  const userId = await requireUserId();
  if (newOwnerId === userId) return;

  // The class's owner and both memberships' roles change together or not at all (a half-done swap would leave a class with two owners, or
  // none). It only moves a class this user owns, and only to someone who is currently a plain member of it, so a stranger, a non-member, a
  // blocked person or someone else's class matches nothing and nothing changes.
  await getDb().$transaction(async (tx) => {
    const moved = await tx.class.updateMany({
      where: { id: classId, ownerId: userId, memberships: { some: { userId: newOwnerId, role: "MEMBER" } } },
      data: { ownerId: newOwnerId },
    });
    if (moved.count === 0) return;
    await tx.classMembership.updateMany({ where: { classId, userId: newOwnerId }, data: { role: "OWNER" } });
    await tx.classMembership.updateMany({ where: { classId, userId }, data: { role: "MEMBER" } });
  });
  revalidatePath(`/classes/${classId}`);
  revalidatePath("/classes");
}

export async function regenerateInviteCode(classId: string): Promise<void> {
  const userId = await requireUserId();
  const db = getDb();

  // The old code stops working at once (join looks classes up by code). Scoped to a class this user owns, so anyone else matches nothing.
  const inviteCode = await uniqueInviteCode(db);
  await db.class.updateMany({ where: { id: classId, ownerId: userId }, data: { inviteCode } });
  revalidatePath(`/classes/${classId}`);
}

export async function deleteClass(classId: string): Promise<void> {
  const userId = await requireUserId();

  // Scoped to a class this user owns, so anyone else matches nothing. Its memberships go with it (onDelete: Cascade on ClassMembership.class);
  // nobody's study data is touched, a class only groups people for a leaderboard.
  await getDb().class.deleteMany({ where: { id: classId, ownerId: userId } });
  revalidatePath("/classes");
  redirect("/classes");
}

export async function joinClass(formData: FormData): Promise<void> {
  const userId = await requireUserId();
  const db = getDb();

  const inviteCode = normalizeInviteCode((formData.get("inviteCode") as string) ?? "");
  if (!inviteCode) redirect("/classes?error=missing-code");

  const targetClass = await db.class.findUnique({ where: { inviteCode } });
  if (!targetClass) redirect("/classes?error=not-found");

  // Someone the owner blocked gets the same answer as a wrong code: it doesn't tell them there is a class, or that they were blocked.
  const blocked = await db.classBan.findUnique({ where: { classId_userId: { classId: targetClass.id, userId } } });
  if (blocked) redirect("/classes?error=not-found");

  await db.classMembership.upsert({
    where: { classId_userId: { classId: targetClass.id, userId } },
    create: { classId: targetClass.id, userId, role: "MEMBER" },
    update: {},
  });

  revalidatePath("/classes");
  redirect(`/classes/${targetClass.id}`);
}

export async function leaveClass(classId: string): Promise<void> {
  const userId = await requireUserId();
  const db = getDb();

  const membership = await db.classMembership.findUnique({ where: { classId_userId: { classId, userId } } });
  if (!membership) return;
  if (membership.role === "OWNER") {
    throw new Error("The class owner can't leave -- hand the class to another member, or delete it");
  }

  await db.classMembership.delete({ where: { classId_userId: { classId, userId } } });
  revalidatePath("/classes");
  redirect("/classes");
}

export async function removeClassMember(classId: string, memberId: string): Promise<void> {
  const userId = await requireUserId();

  // One delete scoped three ways: that class, a MEMBER row (so the owner's own OWNER row can't be removed this way), and only when the
  // signed-in user owns the class. Anyone else, or a person who isn't in the class, matches nothing and nothing happens.
  await getDb().classMembership.deleteMany({
    where: { classId, userId: memberId, role: "MEMBER", class: { ownerId: userId } },
  });
  revalidatePath(`/classes/${classId}`);
  revalidatePath("/classes");
}

export async function sendFriendRequest(formData: FormData): Promise<void> {
  const userId = await requireUserId();
  const db = getDb();

  const username = (formData.get("username") as string)?.trim();
  if (!username) redirect("/friends?error=missing-username");

  // Case-insensitive: usernames are stored case-preserved (see auth/schema.ts),
  // so an exact-case findUnique here would fail to find "JohnDoe" when someone
  // searches "johndoe" -- a real bug caught during testing.
  const target = await db.user.findFirst({ where: { username: { equals: username, mode: "insensitive" } } });
  if (!target) redirect(`/friends?error=not-found&username=${encodeURIComponent(username)}`);
  if (target.id === userId) redirect("/friends?error=self");

  const existing = await db.friendship.findFirst({
    where: {
      OR: [
        { requesterId: userId, addresseeId: target.id },
        { requesterId: target.id, addresseeId: userId },
      ],
    },
  });
  if (existing) redirect("/friends?error=exists");

  await db.friendship.create({ data: { requesterId: userId, addresseeId: target.id, status: "PENDING" } });
  revalidatePath("/friends");
  redirect("/friends?sent=1");
}

export async function respondToFriendRequest(requesterId: string, accept: boolean): Promise<void> {
  const userId = await requireUserId();
  const db = getDb();

  // Authorization check: only the addressee of the request can respond to it.
  const friendship = await db.friendship.findUnique({
    where: { requesterId_addresseeId: { requesterId, addresseeId: userId } },
  });
  if (!friendship || friendship.status !== "PENDING") return;

  if (accept) {
    await db.friendship.update({
      where: { requesterId_addresseeId: { requesterId, addresseeId: userId } },
      data: { status: "ACCEPTED" },
    });
  } else {
    await db.friendship.delete({ where: { requesterId_addresseeId: { requesterId, addresseeId: userId } } });
  }
  revalidatePath("/friends");
}

export async function removeFriend(friendId: string): Promise<void> {
  const userId = await requireUserId();

  // Scoped to an ACCEPTED friendship between exactly these two people, in either direction: it can only ever remove the signed-in
  // user's own friendship, never someone else's, and never a pending request (declining is respondToFriendRequest) or a blocked row.
  await getDb().friendship.deleteMany({
    where: {
      status: "ACCEPTED",
      OR: [
        { requesterId: userId, addresseeId: friendId },
        { requesterId: friendId, addresseeId: userId },
      ],
    },
  });
  revalidatePath("/friends");
}

export async function cancelFriendRequest(addresseeId: string): Promise<void> {
  const userId = await requireUserId();

  // Only a PENDING request this user sent: it can't cancel a request someone sent them (that is declined with respondToFriendRequest)
  // or an accepted friendship (that is removeFriend). Sending again is always possible, so there is no confirmation step.
  await getDb().friendship.deleteMany({ where: { status: "PENDING", requesterId: userId, addresseeId } });
  revalidatePath("/friends");
  // To the bare page, so a leftover "Friend request sent." (?sent=1) or an error from the earlier request doesn't stay on screen.
  redirect("/friends");
}

export async function updateLeaderboardOptOut(optOut: boolean): Promise<void> {
  const userId = await requireUserId();
  await getDb().user.update({ where: { id: userId }, data: { leaderboardOptOut: optOut } });
  revalidatePath("/settings");
  revalidatePath("/friends");
  revalidatePath("/classes");
}
