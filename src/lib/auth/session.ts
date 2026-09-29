import { redirect } from "next/navigation";
import { auth } from "@/lib/auth/config";

// The only route guard -- there's no middleware/proxy.ts (see the gotcha in
// CLAUDE.md), so every protected Server Component must call this itself.
// Server Actions use their own requireUserId (in src/lib/study/actions.ts)
// since redirect() isn't the right tool mid-mutation.
export async function requireUserId(): Promise<string> {
  const session = await auth();
  if (!session?.user?.id) {
    redirect("/login");
  }
  return session.user.id;
}
