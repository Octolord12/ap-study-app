export const CLASS_NAME_MAX = 80;

// One rule for creating and renaming a class: trimmed, 1 to CLASS_NAME_MAX characters. Null when the value can't be used as a name.
export function normalizeClassName(raw: FormDataEntryValue | null): string | null {
  if (typeof raw !== "string") return null;
  const name = raw.trim();
  return name.length >= 1 && name.length <= CLASS_NAME_MAX ? name : null;
}
