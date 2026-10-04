import Link from "next/link";
import { setCramMode } from "@/lib/study/cram-actions";
import { CRAM_DAYS } from "@/lib/study/cram-mode";
import { Button } from "@/components/ui/button";

export function CramToggle({ on }: { on: boolean }) {
  return (
    <div className="flex flex-wrap items-center justify-between gap-x-8 gap-y-4">
      <div className="min-w-0 max-w-[52ch]">
        <p className="heading text-xl">{on ? "Cram mode is on" : "Cram mode is off"}</p>
        <p className="reading mt-1 text-[1.0625rem]">
          Review ignores due dates. It gives you the questions you have missed most, then ones you have never seen, in each
          course. {on ? `It turns itself off ${CRAM_DAYS} days after you switched it on.` : "Meant for the days before an exam."}
        </p>
      </div>
      <form action={setCramMode.bind(null, !on)} className="shrink-0">
        <Button type="submit" size="lg" variant={on ? "outline" : "default"}>
          {on ? "Turn off" : "Turn on"}
        </Button>
      </form>
    </div>
  );
}

// A reminder shown wherever review behaves differently because of cram mode.
export function CramNotice({ className }: { className?: string }) {
  return (
    <p className={className} role="note">
      <span className="eyebrow !text-on-mark bg-mark px-1.5 py-0.5">Cram mode on</span>{" "}
      <span className="text-sm text-muted-foreground">
        Review ignores due dates.{" "}
        <Link href="/dashboard" className="font-semibold underline underline-offset-4 hover:bg-mark hover:text-on-mark hover:no-underline">
          Turn it off
        </Link>
      </span>
    </p>
  );
}
