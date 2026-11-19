import { ImageResponse } from "next/og";

export const size = { width: 32, height: 32 };
export const contentType = "image/png";

// The sticker from the landing page: a lemon disc with a navy outline on sky blue.
export default function Icon() {
  return new ImageResponse(
    (
      <div style={{ width: "100%", height: "100%", display: "flex", alignItems: "center", justifyContent: "center", background: "#62a7ea" }}>
        <div style={{ width: 24, height: 24, borderRadius: 12, background: "#f2ea1e", border: "3px solid #0c1b48" }} />
      </div>
    ),
    size,
  );
}
