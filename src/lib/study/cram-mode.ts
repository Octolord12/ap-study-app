import { cookies } from "next/headers";

export const CRAM_COOKIE = "ap-cram";
// Cramming is for the last stretch before an exam, so it lapses by itself
// rather than staying on for someone who forgot about it.
export const CRAM_DAYS = 7;

// The cookie holds the user's id, not "1": on a shared device, a second
// student logging in must not inherit the first student's cram mode.
export async function isCramModeOn(userId: string): Promise<boolean> {
  return (await cookies()).get(CRAM_COOKIE)?.value === userId;
}
