"use client";

import { useActionState } from "react";
import { joinWaitlist } from "@/lib/marketing/actions";
import { WAITLIST_IDLE } from "@/lib/marketing/waitlist";
import { MINIMUM_AGE } from "@/lib/age";
import styles from "./landing.module.css";

// The landing page's own look for the same joinWaitlist action WaitlistForm uses (the honeypot included).
export function LandingWaitlist() {
  const [state, formAction, isPending] = useActionState(joinWaitlist, WAITLIST_IDLE);

  if (state.status === "done") {
    return (
      <p role="status" className={styles.news}>
        <strong>You&apos;re on the list.</strong> We&apos;ll email you once, when a new subject is ready.
      </p>
    );
  }

  const errorId = "landing-waitlist-error";
  return (
    <form action={formAction} className={styles.news}>
      <label htmlFor="landing-waitlist-email">Email for notices of new subjects</label>
      <input
        id="landing-waitlist-email"
        name="email"
        type="email"
        required
        autoComplete="email"
        inputMode="email"
        maxLength={254}
        aria-describedby={state.status === "error" ? errorId : undefined}
      />
      {state.status === "error" ? (
        <p id={errorId} className={styles.err}>
          {state.message}
        </p>
      ) : (
        <p className={styles.hint}>One email when a new subject launches. Nothing else. You must be {MINIMUM_AGE} or older.</p>
      )}
      <div aria-hidden className={styles.honey}>
        <label>
          Leave this empty
          <input type="text" name="website" tabIndex={-1} autoComplete="off" />
        </label>
      </div>
      <div className={styles.btnRow}>
        <button type="submit" className={`${styles.btn} ${styles.btnGhost}`} disabled={isPending}>
          {isPending ? "Joining…" : "Subscribe"}
        </button>
      </div>
    </form>
  );
}
