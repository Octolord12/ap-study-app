import { ImageResponse } from "next/og";

export const size = { width: 180, height: 180 };
export const contentType = "image/png";

export default function AppleIcon() {
  return new ImageResponse(
    (
      <div style={{ width: "100%", height: "100%", display: "flex", alignItems: "center", justifyContent: "center", background: "#62a7ea" }}>
        <div style={{ width: 132, height: 132, borderRadius: 66, background: "#f2ea1e", border: "12px solid #0c1b48" }} />
      </div>
    ),
    size,
  );
}
