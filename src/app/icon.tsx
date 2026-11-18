import { ImageResponse } from "next/og";

export const size = { width: 32, height: 32 };
export const contentType = "image/png";

// A divider tab: the binder's mark, in the default course color.
export default function Icon() {
  return new ImageResponse(
    (
      <div style={{ width: "100%", height: "100%", display: "flex", alignItems: "center", justifyContent: "center", background: "#e3e7f0" }}>
        <div
          style={{
            width: 22,
            height: 26,
            borderRadius: "8px 8px 0 0",
            background: "#9aa6f2",
            border: "3px solid #1b2438",
            borderBottom: "0",
            marginTop: 6,
          }}
        />
      </div>
    ),
    size,
  );
}
