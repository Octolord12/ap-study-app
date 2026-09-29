// Excludes visually ambiguous characters (0/O, 1/I/L) since these get read
// aloud or copied by hand between students.
const INVITE_CODE_CHARS = "ABCDEFGHJKMNPQRSTUVWXYZ23456789";
const INVITE_CODE_LENGTH = 6;

export function generateInviteCode(): string {
  let code = "";
  for (let i = 0; i < INVITE_CODE_LENGTH; i++) {
    code += INVITE_CODE_CHARS[Math.floor(Math.random() * INVITE_CODE_CHARS.length)];
  }
  return code;
}

export function normalizeInviteCode(input: string): string {
  return input.trim().toUpperCase();
}
