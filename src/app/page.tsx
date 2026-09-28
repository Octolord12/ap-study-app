import { Button } from "@/components/ui/button";
import { ContentRenderer } from "@/components/content-renderer";

// Milestone 1 smoke-test page: proves Tailwind/shadcn, KaTeX math rendering, and
// Shiki code highlighting all work together. Replaced by the real dashboard/course
// browser in Milestone 3.
const SAMPLE_STEM = `
What is printed after the following code runs?

\`\`\`java
int total = 0;
for (int i = 1; i <= 4; i++) {
  total += i;
}
System.out.println(total);
\`\`\`

This tests the same idea as the closed-form sum $\\sum_{i=1}^{n} i = \\frac{n(n+1)}{2}$.
`;

export default function Home() {
  return (
    <div className="mx-auto flex min-h-screen max-w-2xl flex-col gap-8 px-6 py-16">
      <header className="space-y-2">
        <h1 className="text-3xl font-bold tracking-tight">AP Study App</h1>
        <p className="text-muted-foreground">
          Milestone 1 scaffold — Next.js, Tailwind/shadcn, Prisma + Neon, KaTeX, and Shiki all wired up.
        </p>
      </header>

      <section className="rounded-xl border border-border bg-card p-6 shadow-sm">
        <h2 className="mb-4 text-sm font-semibold uppercase tracking-wide text-muted-foreground">
          Sample question stem (math + code rendering)
        </h2>
        <ContentRenderer>{SAMPLE_STEM}</ContentRenderer>
      </section>

      <Button>shadcn/ui button works</Button>
    </div>
  );
}
