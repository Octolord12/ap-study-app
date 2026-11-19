import type { MetadataRoute } from "next";

export default function manifest(): MetadataRoute.Manifest {
  return {
    name: "AP Study App",
    short_name: "AP Study",
    description: "Practice for AP Calculus AB, Physics 1, Computer Science A, World History and U.S. History.",
    start_url: "/",
    display: "standalone",
    background_color: "#62a7ea",
    theme_color: "#62a7ea",
  };
}
