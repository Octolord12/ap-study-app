"use client";

// Replaces the root layout when the layout itself throws, so it can't lean on
// the shared components, fonts or stylesheet: plain inline styles on purpose.
export default function GlobalError({ reset }: { error: Error & { digest?: string }; reset: () => void }) {
  return (
    <html lang="en">
      <body style={{ margin: 0, background: "#f7f8f6", color: "#1f2328", fontFamily: "system-ui, -apple-system, 'Segoe UI', sans-serif" }}>
        <main style={{ maxWidth: 640, margin: "0 auto", padding: "96px 24px" }}>
          <p style={{ fontSize: 12, letterSpacing: "0.08em", textTransform: "uppercase", color: "#59606a", margin: 0 }}>Something broke</p>
          <h1 style={{ fontSize: 44, lineHeight: 1, margin: "12px 0 16px", fontWeight: 800 }}>The app didn&apos;t load.</h1>
          <p style={{ fontSize: 18, lineHeight: 1.5, margin: "0 0 28px" }}>Reload the page. If it keeps happening, try again in a few minutes.</p>
          <button
            type="button"
            onClick={() => reset()}
            style={{ background: "#1f2328", color: "#f7f8f6", border: "1px solid #1f2328", borderRadius: 2, padding: "12px 20px", fontSize: 15, fontWeight: 600, cursor: "pointer" }}
          >
            Try again
          </button>
        </main>
      </body>
    </html>
  );
}
