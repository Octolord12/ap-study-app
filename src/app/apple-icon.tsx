import { ImageResponse } from "next/og";

export const size = { width: 180, height: 180 };
export const contentType = "image/png";

export default function AppleIcon() {
  return new ImageResponse(
    (
      <div style={{ width: "100%", height: "100%", display: "flex", alignItems: "center", justifyContent: "center", background: "#e3e7f0" }}>
        <div
          style={{
            width: 112,
            height: 128,
            borderRadius: "40px 40px 0 0",
            background: "#9aa6f2",
            border: "12px solid #1b2438",
            borderBottom: "0",
            marginTop: 36,
          }}
        />
      </div>
    ),
    size,
  );
}
