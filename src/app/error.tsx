"use client";

import Link from "next/link";
import { Button } from "@/components/ui/button";
import { Page } from "@/components/ui/page";

export default function Error({ reset }: { error: Error & { digest?: string }; reset: () => void }) {
  return (
    <Page className="flex flex-col justify-center">
      <p className="eyebrow">Something broke</p>
      <h1 className="display mt-3 max-w-[14ch] text-[clamp(2.75rem,8vw,5rem)]">That page didn&apos;t load.</h1>
      <p className="reading mt-4 max-w-[48ch] text-lg">
        Try it again. If it keeps happening, go back to the start and open the page from there.
      </p>
      <div className="mt-8 flex flex-wrap gap-3">
        <Button onClick={() => reset()} size="lg">
          Try again
        </Button>
        <Button render={<Link href="/" />} nativeButton={false} size="lg" variant="outline">
          Back to the start
        </Button>
      </div>
    </Page>
  );
}
