import { RESET_TOKEN_MINUTES } from "@/lib/auth/reset-constants";
import { siteUrl } from "@/lib/email/config";
import type { EmailMessage } from "@/lib/email/send";

const escapeHtml = (text: string) => text.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");

function wrap(paragraphs: string[], link?: { href: string; label: string }): string {
  const body = paragraphs.map((p) => `<p style="margin:0 0 16px">${escapeHtml(p)}</p>`).join("");
  const button = link
    ? `<p style="margin:0 0 16px"><a href="${escapeHtml(link.href)}" style="display:inline-block;background:#1f2328;color:#ffffff;padding:12px 18px;text-decoration:none;font-weight:600">${escapeHtml(link.label)}</a></p>` +
      `<p style="margin:0 0 16px;font-size:13px;color:#59606a">If the button doesn't work, paste this into your browser:<br>${escapeHtml(link.href)}</p>`
    : "";
  return `<div style="font-family:Arial,Helvetica,sans-serif;font-size:16px;line-height:1.5;color:#1f2328;max-width:480px">${body}${button}</div>`;
}

export function passwordResetEmail(to: string, resetUrl: string): EmailMessage {
  const lines = [
    "Someone asked to reset the password for your AP Study App account.",
    `If that was you, use the link below within ${RESET_TOKEN_MINUTES} minutes. It works once.`,
  ];
  const after = "If it wasn't you, ignore this email. Your password has not changed.";
  return {
    to,
    subject: "Reset your AP Study App password",
    text: `${lines.join("\n")}\n\n${resetUrl}\n\n${after}\n`,
    html: wrap([...lines, after], { href: resetUrl, label: "Choose a new password" }),
  };
}

export function passwordChangedEmail(to: string): EmailMessage {
  const lines = [
    "The password for your AP Study App account was just changed, and you were signed out on your other devices.",
    "If you did this, there is nothing to do.",
    "If you didn't, reset your password now and then reply to this email so we know.",
  ];
  const href = `${siteUrl()}/forgot-password`;
  return {
    to,
    subject: "Your AP Study App password was changed",
    text: `${lines.join("\n")}\n\n${href}\n`,
    html: wrap(lines, { href, label: "Reset your password" }),
  };
}
