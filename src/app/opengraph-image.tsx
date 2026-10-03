import { ImageResponse } from "next/og";

export const alt = "AP Study App: practice for four AP exams, every wrong answer explained";
export const size = { width: 1200, height: 630 };
export const contentType = "image/png";

const INK = "#1f2328";
const PAPER = "#f7f8f6";
const MARK = "#ffe24a";
const GRAPHITE = "#59606a";

function Tally() {
  const strokes = [0, 1, 2, 3];
  return (
    <div style={{ display: "flex", position: "relative", width: 150, height: 64 }}>
      {strokes.map((i) => (
        <div key={i} style={{ position: "absolute", left: 14 + i * 28, top: 4, width: 8, height: 56, borderRadius: 4, background: INK }} />
      ))}
      <div
        style={{ position: "absolute", left: 0, top: 28, width: 132, height: 8, borderRadius: 4, background: INK, transform: "rotate(-24deg)" }}
      />
    </div>
  );
}

// Type on paper, with the one highlighter stroke: the same system as the app.
export default function OpengraphImage() {
  return new ImageResponse(
    (
      <div style={{ width: "100%", height: "100%", display: "flex", flexDirection: "column", justifyContent: "space-between", background: PAPER, color: INK, padding: "56px 72px", borderTop: `14px solid ${INK}` }}>
        <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between" }}>
          <div style={{ display: "flex", alignItems: "center", gap: 16, fontSize: 34, fontWeight: 800, letterSpacing: 2 }}>
            <div style={{ width: 28, height: 28, borderRadius: 14, background: MARK, border: `4px solid ${INK}` }} />
            AP STUDY APP
          </div>
          <Tally />
        </div>
        <div style={{ display: "flex", flexDirection: "column", fontSize: 104, fontWeight: 800, lineHeight: 1.0, letterSpacing: -3 }}>
          <div style={{ display: "flex" }}>Practice for four AP exams.</div>
          <div style={{ display: "flex", marginTop: 12 }}>
            <div style={{ display: "flex", background: MARK, padding: "0 14px" }}>Every wrong answer</div>
            <div style={{ display: "flex", marginLeft: 22 }}>explained.</div>
          </div>
        </div>
        <div style={{ display: "flex", fontSize: 30, color: GRAPHITE, gap: 28 }}>
          <div>Calculus AB</div>
          <div>Physics 1</div>
          <div>Computer Science A</div>
          <div>World History</div>
        </div>
      </div>
    ),
    size,
  );
}
