// One place for how passwords are stored and limited.
export const BCRYPT_ROUNDS = 12;
export const PASSWORD_MIN_LENGTH = 8;
// bcrypt only reads the first 72 *bytes*, so two longer passwords that agree up to
// there would be the same password. Refusing them is clearer than silently
// truncating. (An accented letter is 2 bytes and an emoji 4, so this is not the same
// as 72 characters.)
export const PASSWORD_MAX_BYTES = 72;

export const isPasswordTooLong = (password: string): boolean => new TextEncoder().encode(password).length > PASSWORD_MAX_BYTES;
