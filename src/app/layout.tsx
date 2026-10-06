import type { Metadata, Viewport } from "next";
import Script from "next/script";
import { Archivo, IBM_Plex_Mono, Source_Serif_4 } from "next/font/google";
import { SiteHeader } from "@/components/site-header";
import { SiteFooter } from "@/components/site-footer";
import { SiteTabBar } from "@/components/nav/site-tab-bar";
import { ThemeSync } from "@/components/theme/theme-sync";
import { THEME_INIT_SCRIPT } from "@/lib/theme/inline-script";
import "./globals.css";

// Variable names deliberately differ from Tailwind's own --font-sans /
// --font-serif / --font-mono (mapped in globals.css): pointing one of those at
// itself made every page fall back to the browser's default serif.
const archivo = Archivo({
  variable: "--font-archivo",
  subsets: ["latin"],
  axes: ["wdth"],
  display: "swap",
});

const sourceSerif = Source_Serif_4({
  variable: "--font-source-serif",
  subsets: ["latin"],
  style: ["normal", "italic"],
  axes: ["opsz"],
  display: "swap",
});

const plexMono = IBM_Plex_Mono({
  variable: "--font-plex-mono",
  subsets: ["latin"],
  weight: ["400", "500"],
  display: "swap",
});

const SITE_NAME = "AP Study App";
const DESCRIPTION =
  "Practice for AP Calculus AB, Physics 1, Computer Science A, World History and U.S. History. Multiple-choice questions that analyze every answer choice, timed exams, and free-response practice.";

export const metadata: Metadata = {
  metadataBase: new URL(process.env.NEXT_PUBLIC_SITE_URL ?? "https://ap-study-app-pi.vercel.app"),
  title: { default: `${SITE_NAME}: AP practice that analyzes incorrect answers`, template: `%s · ${SITE_NAME}` },
  description: DESCRIPTION,
  applicationName: SITE_NAME,
  openGraph: {
    type: "website",
    siteName: SITE_NAME,
    title: "Practice for AP exams. Every incorrect answer analyzed.",
    description: DESCRIPTION,
  },
  twitter: { card: "summary_large_image" },
};

export const viewport: Viewport = {
  themeColor: [
    { media: "(prefers-color-scheme: light)", color: "#f7f8f6" },
    { media: "(prefers-color-scheme: dark)", color: "#14161a" },
  ],
};

export default function RootLayout({ children }: LayoutProps<"/">) {
  return (
    <html
      lang="en"
      className={`${archivo.variable} ${sourceSerif.variable} ${plexMono.variable} h-full antialiased`}
      suppressHydrationWarning
    >
      <body className="flex min-h-full flex-col">
        <Script id="theme-init" strategy="beforeInteractive">
          {THEME_INIT_SCRIPT}
        </Script>
        <ThemeSync />
        <a
          href="#main-content"
          className="sr-only focus:not-sr-only focus:absolute focus:top-2 focus:left-2 focus:z-50 focus:bg-mark focus:px-4 focus:py-2 focus:text-sm focus:font-semibold focus:text-on-mark"
        >
          Skip to content
        </a>
        <SiteHeader />
        <main id="main-content" className="flex flex-1 flex-col">
          {children}
        </main>
        <SiteFooter />
        <SiteTabBar />
      </body>
    </html>
  );
}
