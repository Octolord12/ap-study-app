# Scripts

- `validate-content.ts` — walks `/content` and checks every file against the
  schema and semantic rules (exactly one correct choice per MCQ, rubric points
  summing to the FRQ's point value, concept links resolving to a real unit/topic,
  balanced LaTeX/code fences, no duplicate ids). The rules themselves live in
  `src/lib/content/validate.ts` as pure, unit-tested functions; this script is
  just the directory-walking wrapper. Run: `npm run content:validate`.
- `seed.ts` — upserts validated content into Postgres via Prisma. Idempotent
  (keyed by slug/id), safe to re-run after editing content. Needs `DATABASE_URL`,
  so run it via `npm run content:seed` (wraps it with `dotenv-cli`), not directly
  with `tsx`.
- `npm run db:seed` runs both, in order.
