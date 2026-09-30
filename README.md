# AP Study App

A mobile-first, gamified web app for studying AP exams — built as a tool for
one family, with four full launch courses (AP Computer Science A, AP World
History: Modern, AP Calculus AB, AP Physics 1).

**Live:** [ap-study-app-pi.vercel.app](https://ap-study-app-pi.vercel.app)

## Features

- **Practice modes**: unit quizzes, custom quizzes (pick units/difficulty/
  length), spaced-repetition weak-spot review, a daily challenge, and
  free-response (FRQ/SAQ/DBQ/LEQ) practice with self-grading against a
  rubric.
- **Full exam simulation**: timed, sectioned (MCQ then FRQ), no reveal until
  submission, with an estimated AP score range on the results page.
- **Gamification**: XP and levels, daily streaks with a freeze mechanic, a
  badge catalog, and unit "boss battles" — all backed by synthesized sound
  effects and reduced-motion-aware reward animations.
- **Social**: friend requests, classes with invite codes, and weekly/all-time
  leaderboards.
- **Diagrams**: motion graphs and free-body diagrams render as plain SVG,
  generated from structured content (no images, no diagram-drawing tools
  needed to author them).

See [CLAUDE.md](./CLAUDE.md) for the full architecture, stack rationale,
conventions, data model, and milestone-by-milestone build history.

## Tech stack

Next.js 16 (App Router) + TypeScript, Tailwind CSS v4 + shadcn/ui (Base UI),
Postgres via Neon, Prisma 7, Auth.js (Credentials, self-hosted — no
third-party auth provider holds user data), deployed on Vercel.

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

## Content

Course content (questions, FRQs, unit/topic structure) lives in `/content`
as JSON, validated and seeded into Postgres — the app never reads these
files directly at runtime. See `npm run content:validate` / `npm run
content:seed` and the "Content pipeline" section of CLAUDE.md.
