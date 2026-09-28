# AP Study App

A mobile-first, gamified web app for studying AP exams. See [CLAUDE.md](./CLAUDE.md)
for the full architecture, conventions, data model, and milestone status.

## Getting started

```bash
npm install
cp .env.example .env.local   # then fill in DATABASE_URL / AUTH_SECRET
# or, if this checkout is linked to Vercel:
vercel env pull .env.local

npx prisma migrate dev  # first time, or after a schema change
npm run dev              # http://localhost:3000
```

Run `npm test` for the test suite, `npm run lint` for linting.
