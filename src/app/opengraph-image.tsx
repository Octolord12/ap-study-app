import { readFile } from "node:fs/promises";
import path from "node:path";
import { ImageResponse } from "next/og";

export const alt = "AP Study App: practice for AP exams, every incorrect answer analyzed";
export const size = { width: 1200, height: 630 };
export const contentType = "image/png";

const INK = "#1f2328";
const PAPER = "#f7f8f6";
const MARK = "#ffe24a";
const GRAPHITE = "#59606a";

function Tally() {
  return (
    <div style={{ display: "flex", position: "relative", width: 150, height: 64 }}>
      {[0, 1, 2, 3].map((i) => (
        <div key={i} style={{ position: "absolute", left: 14 + i * 28, top: 4, width: 8, height: 56, borderRadius: 4, background: INK }} />
      ))}
      <div style={{ position: "absolute", left: 0, top: 28, width: 132, height: 8, borderRadius: 4, background: INK, transform: "rotate(-24deg)" }} />
    </div>
  );
}

// Type on paper with the one highlighter stroke: the same system as the app.
// ImageResponse can't read next/font, so the headline uses the bold sans that
// ships with KaTeX (already a dependency, so nothing is downloaded or added).
export default async function OpengraphImage() {
  const font = await readFile(path.join(process.cwd(), "node_modules/katex/dist/fonts/KaTeX_SansSerif-Bold.ttf"));
  const line = { display: "flex", whiteSpace: "nowrap" as const, fontSize: 84, lineHeight: 1.1, letterSpacing: -1.5 };

  return new ImageResponse(
    (
      <div
        style={{
          width: "100%",
          height: "100%",
          display: "flex",
          flexDirection: "column",
          justifyContent: "space-between",
          background: PAPER,
          color: INK,
          padding: "52px 72px 56px",
          borderTop: `14px solid ${INK}`,
          fontFamily: "KaTeX Sans",
          fontWeight: 700,
        }}
      >
        <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between" }}>
          <div style={{ display: "flex", alignItems: "center", gap: 16, fontSize: 30, letterSpacing: 3 }}>
            <div style={{ display: "flex", width: 28, height: 28, borderRadius: 14, background: MARK, border: `4px solid ${INK}` }} />
            AP STUDY APP
          </div>
          <Tally />
        </div>
        <div style={{ display: "flex", flexDirection: "column" }}>
          <div style={line}>Practice for AP exams.</div>
          <div style={{ display: "flex", marginTop: 6 }}>
            <div style={{ ...line, background: MARK, padding: "0 16px 0 0", marginLeft: -2 }}>Every incorrect answer</div>
          </div>
          <div style={line}>analyzed.</div>
        </div>
        <div style={{ display: "flex", fontSize: 24, color: GRAPHITE, gap: 24 }}>
          <div>Calculus AB</div>
          <div>Physics 1</div>
          <div>Computer Science A</div>
          <div>World History</div>
          <div>U.S. History</div>
        </div>
      </div>
    ),
    { ...size, fonts: [{ name: "KaTeX Sans", data: font, weight: 700, style: "normal" }] },
  );
}
