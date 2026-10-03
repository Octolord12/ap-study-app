import { ImageResponse } from "next/og";

export const size = { width: 180, height: 180 };
export const contentType = "image/png";

export default function AppleIcon() {
  return new ImageResponse(
    (
      <div style={{ width: "100%", height: "100%", display: "flex", alignItems: "center", justifyContent: "center", background: "#f7f8f6" }}>
        <div
          style={{
            width: 124,
            height: 124,
            borderRadius: 62,
            background: "#ffe24a",
            border: "12px solid #1f2328",
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
          }}
        >
          <div style={{ width: 36, height: 36, borderRadius: 18, background: "#1f2328" }} />
        </div>
      </div>
    ),
    size,
  );
}
