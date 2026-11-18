import { readFile } from "node:fs/promises";
import path from "node:path";
import { ImageResponse } from "next/og";

export const alt = "AP Study App: practice for AP exams, every incorrect answer analyzed";
export const size = { width: 1200, height: 630 };
export const contentType = "image/png";

const INK = "#1b2438";
const PAPER = "#e3e7f0";

// One tab per course, in the same colors as the app (see globals.css).
const TABS = [
  { name: "CSA", color: "#62c7de" },
  { name: "World", color: "#f2a65a" },
  { name: "U.S.", color: "#ee7f76" },
  { name: "Calc AB", color: "#9aa6f2" },
  { name: "Calc BC", color: "#b98ceb" },
  { name: "Physics 1", color: "#f28db8" },
  { name: "Bio", color: "#7ed493" },
  { name: "Stats", color: "#ebcf55" },
];

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

// Type on the desk with one divider tab per course: the same system as the app.
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
          fontFamily: "KaTeX Sans",
          fontWeight: 700,
        }}
      >
        <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between" }}>
          <div style={{ display: "flex", alignItems: "center", gap: 16, fontSize: 34, letterSpacing: -0.5 }}>
            AP Study App
          </div>
          <Tally />
        </div>
        <div style={{ display: "flex", flexDirection: "column" }}>
          <div style={line}>Practice for AP exams.</div>
          <div style={line}>Every incorrect answer</div>
          <div style={line}>analyzed.</div>
        </div>
        <div style={{ display: "flex", gap: 10, alignItems: "flex-end" }}>
          {TABS.map((tab) => (
            <div
              key={tab.name}
              style={{
                display: "flex",
                background: tab.color,
                color: "#141b2d",
                border: `3px solid ${INK}`,
                borderBottom: "0",
                borderRadius: "14px 14px 0 0",
                padding: "14px 20px 10px",
                fontSize: 26,
              }}
            >
              {tab.name}
            </div>
          ))}
        </div>
      </div>
    ),
    { ...size, fonts: [{ name: "KaTeX Sans", data: font, weight: 700, style: "normal" }] },
  );
}
