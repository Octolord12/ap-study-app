// The class named by ?class=, or the first one if it is missing or not one of
// the teacher's own (never trust the id from the URL).
export function selectClass<T extends { id: string }>(classes: T[], requestedId: string | undefined): T | null {
  return classes.find((c) => c.id === requestedId) ?? classes[0] ?? null;
}
