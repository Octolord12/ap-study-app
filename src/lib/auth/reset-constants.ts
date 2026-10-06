// Kept apart from reset-token.ts, which imports node:crypto and so can't be bundled for the browser.
export const RESET_TOKEN_MINUTES = 60;
// Requests (not successes) per account per hour. Stops someone using the form to flood a student's inbox.
export const MAX_RESET_REQUESTS_PER_HOUR = 3;

export const RESET_LINK_INVALID = "This link has expired or was already used. Ask for a new one.";
