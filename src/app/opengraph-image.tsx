import { readFile } from "node:fs/promises";
import path from "node:path";
import { ImageResponse } from "next/og";

export const alt = "AP Study App: practice for AP exams, every incorrect answer analyzed";
export const size = { width: 1200, height: 630 };
export const contentType = "image/png";

const INK = "#0c1b48";
const SKY = "#62a7ea";
const LEMON = "#f2ea1e";

// The course chips, in the same colors as the app (see globals.css).
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

// Huge navy type on sky blue, a lemon sticker and one chip per course: the same system as the app.
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
          background: SKY,
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
          <div
            style={{
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              width: 150,
              height: 150,
              borderRadius: 75,
              background: LEMON,
              border: `4px solid ${INK}`,
              fontSize: 34,
              lineHeight: 1.05,
              textAlign: "center",
              transform: "rotate(-8deg)",
            }}
          >
            8 AP exams
          </div>
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
                color: INK,
                border: `3px solid ${INK}`,
                borderRadius: 999,
                padding: "10px 22px",
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
