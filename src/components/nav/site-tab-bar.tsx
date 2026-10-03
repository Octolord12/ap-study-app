import { auth } from "@/lib/auth/config";
import { TabBar } from "@/components/nav/tab-bar";

// Rendered at the end of the page so its spacer pushes the footer clear of
// the fixed bar; only for signed-in users, since logged-out pages have no
// app sections to jump between.
export async function SiteTabBar() {
  const session = await auth();
  return session?.user?.id ? <TabBar /> : null;
}
