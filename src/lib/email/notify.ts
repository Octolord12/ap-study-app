import { afterResponse } from "@/lib/after-response";
import { isEmailConfigured } from "@/lib/email/config";
import { sendEmail } from "@/lib/email/send";
import { passwordChangedEmail } from "@/lib/email/templates";

// A heads-up to the account's own address after its password changed (from Settings or a reset). It is
// only sent when email is really set up, so a missing key never turns a password change into an error.
export function notifyPasswordChanged(email: string): void {
  if (!isEmailConfigured()) return;
  afterResponse(() => sendEmail(passwordChangedEmail(email)));
}
