"use server";

import { cookies } from "next/headers";
import { revalidatePath } from "next/cache";
import { auth } from "@/lib/auth/config";
import { CRAM_COOKIE, CRAM_DAYS } from "@/lib/study/cram-mode";

export async function setCramMode(on: boolean) {
  const session = await auth();
  if (!session?.user?.id) throw new Error("Not authenticated");

  const jar = await cookies();
  if (on) {
    jar.set(CRAM_COOKIE, session.user.id, {
      path: "/",
      maxAge: CRAM_DAYS * 24 * 60 * 60,
      httpOnly: true,
      sameSite: "lax",
      secure: process.env.NODE_ENV === "production",
    });
  } else {
    jar.delete(CRAM_COOKIE);
  }
  // Today, the practice hub and weak-spot page all change with this.
  revalidatePath("/", "layout");
}
