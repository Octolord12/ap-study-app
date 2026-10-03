import type { Metadata } from "next";
import Link from "next/link";
import { Button } from "@/components/ui/button";
import { Page } from "@/components/ui/page";

export const metadata: Metadata = { title: "Page not found" };

export default function NotFound() {
  return (
    <Page className="flex flex-col justify-center">
      <p className="eyebrow">Error 404</p>
      <p aria-hidden className="display mt-2 flex items-center text-[clamp(6rem,24vw,13rem)]">
        4
        <span className="mx-[0.04em] inline-block size-[0.62em] rounded-full border-[0.1em] border-foreground bg-mark" />4
      </p>
      <h1 className="heading mt-2 text-3xl">That page isn&apos;t here.</h1>
      <p className="reading mt-3 max-w-[48ch] text-lg">
        The link may be old, or the address mistyped. Your courses and progress are one click away.
      </p>
      <div className="mt-8 flex flex-wrap gap-3">
        <Button render={<Link href="/" />} nativeButton={false} size="lg">
          Back to the start
        </Button>
        <Button render={<Link href="/courses" />} nativeButton={false} size="lg" variant="outline">
          Browse courses
        </Button>
      </div>
    </Page>
  );
}
