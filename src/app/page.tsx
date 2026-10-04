import { Suspense } from "react";
import { auth } from "@/lib/auth/config";
import { Landing } from "@/components/marketing/landing";
import { TodayScreen } from "@/components/today/today-screen";
import { PageSkeleton } from "@/components/ui/page-skeleton";

// One URL, two pages: signed-out visitors get the landing page, signed-in
// students get their Today screen. Only the Today screen sits behind a
// fallback: the landing page is the first thing a crawler or a visitor on a
// slow connection sees, so it must arrive as finished HTML, not a skeleton.
export default async function Home() {
  const session = await auth();
  if (session?.user?.id) {
    return (
      <Suspense fallback={<PageSkeleton />}>
        <TodayScreen userId={session.user.id} />
      </Suspense>
    );
  }
  return <Landing />;
}
