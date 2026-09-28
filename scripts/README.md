# Scripts

- `validate-content.ts` (Milestone 2) — checks every file in `/content` against
  the schema: exactly one correct choice per MCQ, an explanation for every
  choice, a concept link that resolves to a real unit/topic, valid LaTeX/code
  fences, rubric points summing to the FRQ's point value.
- `seed.ts` (Milestone 2) — loads validated content into Postgres via Prisma.

Run with `npx tsx scripts/<name>.ts` (already installed as a dev dependency).
