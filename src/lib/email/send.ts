import { isEmailConfigured } from "@/lib/email/config";

export interface EmailMessage {
  to: string;
  subject: string;
  text: string;
  html: string;
}

// Resend's REST API, called directly: one POST, so no SDK to depend on. Never logs the body or the
// recipient, only the status, since both can contain someone's address or a reset link.
export async function sendEmail(message: EmailMessage): Promise<void> {
  if (!isEmailConfigured()) {
    if (process.env.NODE_ENV !== "production") {
      console.info(`[email not sent: RESEND_API_KEY / EMAIL_FROM not set]\nTo: ${message.to}\nSubject: ${message.subject}\n\n${message.text}`);
    }
    return;
  }

  const response = await fetch("https://api.resend.com/emails", {
    method: "POST",
    headers: { Authorization: `Bearer ${process.env.RESEND_API_KEY}`, "Content-Type": "application/json" },
    body: JSON.stringify({
      from: process.env.EMAIL_FROM,
      to: [message.to],
      subject: message.subject,
      text: message.text,
      html: message.html,
      ...(process.env.EMAIL_REPLY_TO ? { reply_to: process.env.EMAIL_REPLY_TO } : {}),
    }),
  });
  if (!response.ok) throw new Error(`Email provider answered ${response.status}`);
}
