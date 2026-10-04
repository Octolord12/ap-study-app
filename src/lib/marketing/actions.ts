"use server";

import { getDb } from "@/lib/db";
import { WaitlistSchema, type WaitlistState } from "@/lib/marketing/waitlist";

const DONE: WaitlistState = { status: "done" };

export async function joinWaitlist(_prev: WaitlistState, formData: FormData): Promise<WaitlistState> {
  // Bots fill every field; the "website" input is hidden from people. Answer
  // exactly like a success so a bot learns nothing.
  if (formData.get("website")) return DONE;

  const parsed = WaitlistSchema.safeParse({ email: formData.get("email") });
  if (!parsed.success) {
    return { status: "error", message: parsed.error.issues[0]?.message ?? "Enter a valid email address." };
  }

  try {
    // ON CONFLICT DO NOTHING: an address that is already on the list gets the
    // same answer as a new one, so the form can't be used to check who signed up.
    await getDb().waitlistSignup.createMany({ data: [{ email: parsed.data.email }], skipDuplicates: true });
  } catch (error) {
    // Code only: error messages can echo the query's values, and this one holds an email.
    console.error("waitlist signup failed", (error as { code?: string }).code ?? (error as Error).name);
    return { status: "error", message: "Something went wrong. Please try again in a moment." };
  }
  return DONE;
}
