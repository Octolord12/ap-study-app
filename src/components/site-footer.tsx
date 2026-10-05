import Link from "next/link";
import { feedbackMailto } from "@/lib/site-contact";

const LINK = "underline underline-offset-4 hover:bg-mark hover:text-on-mark hover:no-underline";

export function SiteFooter() {
  return (
    <footer className="border-t border-border">
      <div className="mx-auto w-full max-w-[67.5rem] px-4 py-6 sm:px-6">
        <p className="max-w-[70ch] text-xs leading-relaxed text-muted-foreground">
          AP® and Advanced Placement® are registered trademarks of College Board, which is not affiliated with this site
          and does not endorse it. Questions here are written for practice. They have not been reviewed by College Board and
          may contain mistakes.
        </p>
        <p className="mt-3 flex flex-wrap gap-x-5 gap-y-1 text-xs font-medium">
          <a href={feedbackMailto()} className={LINK}>
            Report a mistake or send a suggestion
          </a>
          <Link href="/privacy" className={LINK}>
            Privacy
          </Link>
        </p>
      </div>
    </footer>
  );
}
