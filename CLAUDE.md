@AGENTS.md

# AP Study App

A mobile-first, gamified web app for studying AP exams (quizzes, timed practice
tests, FRQ practice, streaks/XP/badges, friend & class leaderboards). Starts as
a tool for one family; built so it can scale into a public product later
without a rewrite, but not over-engineered for that future.

Launch courses: AP Computer Science A, AP World History: Modern, AP Calculus
AB, AP Physics 1.

## Stack (and why)

| Layer | Choice | Why |
|---|---|---|
| Framework | Next.js 16 (App Router, TypeScript), deployed on Vercel | One codebase for frontend + backend, mobile-first, best-documented React framework for a solo maintainer. |
| Styling/UI | Tailwind CSS v4 + shadcn/ui | Components you own the code for (not a black box), easy to theme per-course. |
| Database | Postgres via Neon (Vercel Marketplace) | Serverless, scales to zero, free tier, relational data fits the course→unit→topic→question hierarchy. |
| ORM | Prisma 7 (with `@prisma/adapter-neon` driver adapter) | Gentlest learning curve for a solo maintainer; declarative schema + migrations. Prisma 7's generated client *requires* a driver adapter now (no more bare `new PrismaClient()` reading `DATABASE_URL` implicitly) — see `src/lib/db/index.ts`. |
| Auth | Auth.js (NextAuth v5 beta), Credentials provider, self-hosted | No third party holding user emails (some users may be minors); free; full control. Chosen over Clerk for privacy, per project decision. |
| Math rendering | KaTeX via `rehype-katex` / `remark-math` | Renders `$...$` / `$$...$$` written directly in content. |
| Code highlighting | Shiki via `rehype-pretty-code` | Same engine as VS Code. **Loads its highlighter asynchronously** — see the gotcha below. |
| Client state | Zustand | Minimal boilerplate for streak/mute/boss-battle-health UI state. |
| Animations/sound | Framer Motion, canvas-confetti, Howler.js | Level-up/badge/correct-answer feedback, with a mute toggle. |
| Testing | Vitest + React Testing Library | Fast, Jest-compatible, first-class Next.js support. |

### Gotcha: `ContentRenderer` can't use `react-markdown` directly

`rehype-pretty-code` loads a Shiki highlighter asynchronously on first use.
`react-markdown` renders synchronously. Combining them crashes Next's static
prerender with `runSync finished async`. Fix: `src/components/content-renderer.tsx`
runs the `unified` pipeline directly with `.process()` (awaited, since it's an
async Server Component) instead of going through `react-markdown`. Don't swap
it back to `react-markdown` without re-testing `next build`.

### Gotcha: Prisma client needs a driver adapter

Prisma 7's generated client (`src/generated/prisma/`, gitignored — regenerated
by `npx prisma generate`, which also runs automatically via the `postinstall`
script) requires a driver adapter or Accelerate URL in its constructor; it no
longer reads `DATABASE_URL` implicitly. We use `@prisma/adapter-neon`. Always
get the client via `getDb()` in `src/lib/db/index.ts` — never construct
`PrismaClient` elsewhere, and never wrap it in a `Proxy` (breaks Auth.js's
Prisma adapter, which inspects the client object directly).

### Gotcha: env vars live in `.env.local`, not `.env`

This project is linked to Vercel (`vercel link`) with Neon provisioned through
the Marketplace. `vercel env pull` writes to `.env.local` (Next.js's own
convention), but Prisma's CLI only auto-loads `.env` by default. `prisma7.config.ts`
explicitly loads `.env.local` to bridge this — don't add a separate `.env`
with real values, it'll get out of sync.

## Conventions

- Server Components by default; add `"use client"` only where interactivity
  requires it (gamification UI, forms).
- Node.js runtime everywhere (never `export const runtime = "edge"`) — Prisma
  and bcrypt need it, and Fluid Compute makes edge unnecessary anyway.
- Next.js 16: middleware is `proxy.ts`, not `middleware.ts`; `params`/`searchParams`/
  `cookies()`/`headers()` are all `async`.
- No comments explaining *what* code does; only *why*, when it's non-obvious
  (see the gotchas above for examples).
- All XP/score-affecting writes happen in server-side route handlers, computed
  from stored attempt rows — never trust an XP amount sent from the client.

## Commands

```bash
npm run dev          # start the dev server (localhost:3000)
npm run build         # production build
npm run test          # run tests once
npm run test:watch    # run tests in watch mode
npm run lint           # eslint
npx tsc --noEmit       # typecheck (route types need a prior dev/build run)
npm run db:migrate     # prisma migrate dev
npm run db:studio      # prisma studio (browse the DB)
npx tsx scripts/seed.ts            # (Milestone 2) seed /content into Postgres
npx tsx scripts/validate-content.ts # (Milestone 2) validate /content
```

Env vars live in `.env.local` (gitignored). `vercel env pull .env.local` re-syncs
them if they ever drift; `.env.example` documents what's needed.

## Data model

Full schema: `prisma/schema.prisma`. Summary:

- **Content** (authored in `/content` as JSON → validated → seeded here; the
  app only reads from the DB at runtime): `Course` → `Unit` → `Topic` →
  `Question` (+ `Choice`) / `FRQPrompt`.
- **Auth.js tables**: `User`, `Account`, `Session`, `VerificationToken` (shapes
  fixed by `@auth/prisma-adapter`, don't rename fields).
- **Progress**: `Enrollment`, `QuestionAttempt`, `FRQAttempt`, `Bookmark`,
  `SpacedRepetitionState` (SM-2-style, drives weak-spot review), `ExamAttempt`.
- **Gamification**: `XPEvent` (append-only ledger — level/streak/totals are
  always *derived* from this, never stored/trusted directly), `Badge`,
  `UserBadge`, `BossBattleAttempt`.
- **Social**: `Class`, `ClassMembership`, `Friendship`, `User.leaderboardOptOut`.

### Content schema (for `/content/<course>/...` JSON, built out in Milestone 2)

**MCQ Question**
```
id, course, unit, topic, difficulty (easy|medium|hard),
stem (markdown; supports $latex$ and ```code``` fences),
choices: [{ label, text, isCorrect, explanation }]  (4 or 5 choices, exactly one isCorrect),
explanation (why the correct answer is right),
conceptLink (slug back to the relevant unit/topic page),
reviewed (bool, default false)
```

**FRQ Prompt**
```
id, course, unit, topic, prompt, pointValue,
rubric: [{ id, points, description }]  (points must sum to pointValue),
sampleResponse,
reviewed (bool, default false)
```

**Course exam format** (stored as `Course.examFormat` JSON — see below for why
this must stay data, not hardcoded)

## Verified AP course info (2026-27)

Exam formats change almost every year — 3 of our 4 launch courses have had a
change in the last two years. This is *why* `examFormat` and unit weightings
are data (`Course.examFormat` JSON / `Unit.weightingMin/Max`), not hardcoded
in app logic — updating them should be a data edit.

| Course | Units | Exam format | Recent/upcoming change |
|---|---|---|---|
| AP Computer Science A | 10 units (Primitive Types → Recursion) | 42 MCQ + 4 FRQ, 3h | Stable. |
| AP World History: Modern | 9 units, c.1200 CE–present | 55 MCQ + 3 SAQ (95min) + 1 DBQ + 1 LEQ (100min), 3h15m | **May 2027**: all 3 SAQs required (was pick 1 of 3), LEQ is a single required prompt (was pick 1 of 3). |
| AP Calculus AB | 8 units | Currently 42 MCQ + 6 FRQ, 3h10m | **May 2027**: College Board has confirmed MCQ count/timing will change; exact numbers not yet published — check before hardcoding exam-sim config for that year. |
| AP Physics 1 | 8 units (Fluids added as Unit 8) | 40 MCQ + 4 FRQ | **Already redesigned for 2024-25** — if referencing old prep material, it may predate this. |

## Milestone status

- [x] **Milestone 1 — Plan and setup.** Architecture proposed and approved.
      Next.js/Tailwind/shadcn scaffold, Prisma schema, Neon Postgres provisioned
      and migrated, Auth.js wired (no UI yet), KaTeX + Shiki content rendering
      proven end-to-end, Vitest configured with passing tests, `next build`/`lint`/
      `tsc` all clean. Vercel project linked (`ap-study-app`). GitHub repo not
      yet created (see Known issues).
- [ ] **Milestone 2 — Content foundation.** Validation script, seed pipeline,
      sample question bank for one course.
- [ ] **Milestone 3 — Core study loop.** Auth UI, course/unit/topic browsing,
      MCQ quizzes with explanations, filters, bookmarks, progress tracking.
- [ ] **Milestone 4 — Practice modes.** Custom quizzes, exam simulation, daily
      challenge, weak-spot review, FRQ self-grading.
- [ ] **Milestone 5 — Gamification.** XP, levels, streaks, badges, boss battles,
      animations.
- [ ] **Milestone 6 — Social.** Friends, classes, leaderboards, anti-abuse checks.
- [ ] **Milestone 7 — Content at scale.** Full starter banks (~30 MCQ + 3 FRQ
      per unit) for all four courses, validated, review workflow.
- [ ] **Milestone 8 — Polish and launch prep.** Accessibility, mobile testing,
      performance, error handling, deployment, README.

## Known issues / follow-ups

- **GitHub repo not yet created.** Neither `gh` nor Homebrew is installed on
  this machine, so the repo couldn't be created non-interactively. Local git
  history exists (`git log`); create the repo on github.com and add it as a
  remote, or install `gh`/Homebrew and ask to retry.
- **`npm audit` reports vulnerabilities** in `chevrotain`/`lodash`/`valibot` —
  all transitive dev dependencies of the `prisma` CLI's schema-formatting
  tooling, not runtime/production code. Revisit when Prisma ships a fix
  upstream; not urgent.
- **Prisma 8 exists as a release candidate** (`8.0.0-rc.x`, currently tagged
  `latest` on npm) with a materially different CLI (`prisma.config.ts`, no more
  traditional `schema.prisma`-only flow). We deliberately pinned to the last
  stable release, **Prisma 7.10.0**. Don't `npm update` Prisma casually.
- Auth.js is wired (provider, adapter, session strategy) but there's no
  login/signup UI yet — that's Milestone 3. Don't build features that assume a
  logged-in user until then.
