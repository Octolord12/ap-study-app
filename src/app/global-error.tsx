"use client";

// Replaces the root layout when the layout itself throws, so it can't lean on
// the shared components, fonts or stylesheet: plain inline styles on purpose.
export default function GlobalError({ reset }: { error: Error & { digest?: string }; reset: () => void }) {
  return (
    <html lang="en">
      <body style={{ margin: 0, background: "#e3e7f0", color: "#1b2438", fontFamily: "system-ui, -apple-system, 'Segoe UI', sans-serif" }}>
        <main style={{ maxWidth: 640, margin: "0 auto", padding: "96px 24px" }}>
          <p style={{ fontSize: 14, fontWeight: 600, color: "#475069", margin: 0 }}>Something broke</p>
          <h1 style={{ fontSize: 44, lineHeight: 1, margin: "12px 0 16px", fontWeight: 800 }}>The app didn&apos;t load.</h1>
          <p style={{ fontSize: 18, lineHeight: 1.5, margin: "0 0 28px" }}>Reload the page. If it keeps happening, try again in a few minutes.</p>
          <button
            type="button"
            onClick={() => reset()}
            style={{ background: "#1b2438", color: "#ffffff", border: "1px solid #1b2438", borderRadius: 6, padding: "12px 20px", fontSize: 15, fontWeight: 600, cursor: "pointer" }}
          >
            Try again
          </button>
        </main>
      </body>
    </html>
  );
}
