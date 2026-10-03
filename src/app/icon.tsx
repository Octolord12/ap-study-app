import { ImageResponse } from "next/og";

export const size = { width: 32, height: 32 };
export const contentType = "image/png";

// A filled answer bubble in highlighter yellow: the same mark as the wordmark.
export default function Icon() {
  return new ImageResponse(
    (
      <div style={{ width: "100%", height: "100%", display: "flex", alignItems: "center", justifyContent: "center", background: "#f7f8f6" }}>
        <div
          style={{
            width: 26,
            height: 26,
            borderRadius: 13,
            background: "#ffe24a",
            border: "3px solid #1f2328",
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
          }}
        >
          <div style={{ width: 8, height: 8, borderRadius: 4, background: "#1f2328" }} />
        </div>
      </div>
    ),
    size,
  );
}
