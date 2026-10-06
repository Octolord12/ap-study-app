const DEFAULT_SITE_URL = "https://ap-study-app-pi.vercel.app";

// The base of every link we put in an email. It comes from configuration and never from the request:
// building a reset link from the Host header would let anyone who can forge that header point a
// student's reset email at their own site.
export function siteUrl(): string {
  return (process.env.SITE_URL ?? process.env.NEXT_PUBLIC_SITE_URL ?? DEFAULT_SITE_URL).replace(/\/+$/, "");
}

export function isEmailConfigured(): boolean {
  return Boolean(process.env.RESEND_API_KEY && process.env.EMAIL_FROM);
}

// In production the reset flow is offered only when mail can really be sent. In development it is
// always on, and the email is printed to the server console instead of sent.
export function isPasswordResetAvailable(): boolean {
  return isEmailConfigured() || process.env.NODE_ENV !== "production";
}
