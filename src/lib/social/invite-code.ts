import { randomInt } from "node:crypto";

// Excludes visually ambiguous characters (0/O, 1/I/L) since these get read
// aloud or copied by hand between students.
const INVITE_CODE_CHARS = "ABCDEFGHJKMNPQRSTUVWXYZ23456789";
const INVITE_CODE_LENGTH = 6;

// A code is what lets someone into a class, so it comes from the OS's secure random source (randomInt is also free of modulo bias),
// not Math.random, whose later outputs can be worked out from earlier ones.
export function generateInviteCode(): string {
  let code = "";
  for (let i = 0; i < INVITE_CODE_LENGTH; i++) {
    code += INVITE_CODE_CHARS[randomInt(INVITE_CODE_CHARS.length)];
  }
  return code;
}

export function normalizeInviteCode(input: string): string {
  return input.trim().toUpperCase();
}
