import type { MetadataRoute } from "next";

export default function manifest(): MetadataRoute.Manifest {
  return {
    name: "AP Study App",
    short_name: "AP Study",
    description: "Practice for AP Calculus AB, Physics 1, Computer Science A, World History and U.S. History.",
    start_url: "/",
    display: "standalone",
    background_color: "#f7f8f6",
    theme_color: "#f7f8f6",
  };
}
