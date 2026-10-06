import { after } from "next/server";

// Runs work once the response has gone out. Two reasons: the person isn't kept waiting on an email
// provider, and a request that finds an account takes no longer than one that doesn't, so response
// time can't be used to tell whether an address is registered. Failures are logged by name only.
export function afterResponse(task: () => Promise<void>): void {
  after(async () => {
    try {
      await task();
    } catch (error) {
      console.error("background task failed:", error instanceof Error ? error.name : "unknown error");
    }
  });
}
