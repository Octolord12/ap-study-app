import { Host_Grotesk, JetBrains_Mono } from "next/font/google";

// Only the landing page uses these; the rest of the app keeps Bricolage and Literata.
// The variable names differ from Tailwind's --font-sans/--font-mono on purpose (see layout.tsx).
export const hostGrotesk = Host_Grotesk({ subsets: ["latin"], variable: "--font-host", display: "swap" });
export const jetbrainsMono = JetBrains_Mono({ subsets: ["latin"], variable: "--font-jbmono", display: "swap" });
