import { auth } from "@/lib/auth/config";
import { Landing } from "@/components/marketing/landing";
import { TodayScreen } from "@/components/today/today-screen";

// One URL, two pages: signed-out visitors get the landing page, signed-in
// students get their Today screen.
export default async function Home() {
  const session = await auth();
  if (session?.user?.id) return <TodayScreen userId={session.user.id} />;
  return <Landing />;
}
