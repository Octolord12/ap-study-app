import { Page } from "@/components/ui/page";

// Shown while a route's data loads. Static rules and a mono label: the page
// shape appears immediately, nothing shimmers or bounces.
export default function Loading() {
  return (
    <Page aria-busy="true">
      <p role="status" className="eyebrow">
        Loading
      </p>
      <div className="mt-6 border-b-2 border-foreground pb-8">
        <div className="h-12 w-3/5 max-w-md bg-muted motion-safe:animate-pulse" />
      </div>
      <div className="mt-8 space-y-0 border-b border-border">
        {[0, 1, 2, 3].map((i) => (
          <div key={i} className="border-t border-border py-5">
            <div className="h-4 w-2/5 bg-muted motion-safe:animate-pulse" />
            <div className="mt-3 h-3 w-4/5 bg-muted motion-safe:animate-pulse" />
          </div>
        ))}
      </div>
    </Page>
  );
}
