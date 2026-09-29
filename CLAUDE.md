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
| UI primitives | Base UI (via shadcn) | shadcn's default base for this project's registry version. Polymorphic rendering uses a `render` prop (`<Button render={<Link .../>} />`), **not** Radix's `asChild` — see the gotcha below. |
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

### Gotcha: scripts need `DATABASE_URL`, and need `dotenv-cli` to get it

`tsx` (used for `scripts/*.ts`) doesn't auto-load `.env.local` the way Next.js
does. `content:seed` runs through `dotenv -e .env.local --` for this reason.
If you add a new script that touches the database, wrap it the same way rather
than adding another ad hoc env-loading mechanism.

### Gotcha: env vars live in `.env.local`, not `.env`

This project is linked to Vercel (`vercel link`) with Neon provisioned through
the Marketplace. `vercel env pull` writes to `.env.local` (Next.js's own
convention), but Prisma's CLI only auto-loads `.env` by default. `prisma7.config.ts`
explicitly loads `.env.local` to bridge this — don't add a separate `.env`
with real values, it'll get out of sync.

### Gotcha: `session.user.id` needs explicit callbacks

Auth.js's default JWT session only carries `name`/`email`/`image` on
`session.user` -- **not `id`**, even though `authorize()` returns one. Every
`requireUserId()` call and Server Action reads `session.user.id`, so without
the `jwt`/`session` callbacks in `src/lib/auth/config.ts` that copy it from
the token, auth silently looks broken: `auth()` returns a real, truthy session,
so surface-level checks (`session?.user`, displaying the name in the header)
work fine, while anything checking `.id` specifically redirects to `/login` in
a loop. This is exactly what happened building Milestone 3 and cost real time
to track down -- don't remove those callbacks. The type augmentation for
`session.user.id` lives in `src/lib/auth/types.d.ts`.

One more wrinkle if you hit this again: fixing the callbacks doesn't fix
*already-issued* session cookies (the old JWT was encoded without `id` in the
first place) -- you have to log out and back in to get a token minted under
the fixed callbacks.

### Gotcha: no middleware/proxy.ts for route protection

We tried protecting `/courses` and `/dashboard` with `proxy.ts` (Next.js 16's
renamed `middleware.ts`) wrapping Auth.js's `auth()` HOF, the standard v5
pattern. It consistently redirected *authenticated* users away (`req.auth` was
falsy in the proxy context even though `auth()` elsewhere on the same request
found a valid session) -- reproducible, and `trustHost: true` didn't fix it.
Rather than debug a next-auth-v5-beta × Next-16-proxy.ts interaction further,
we removed proxy.ts: every protected page already calls `requireUserId()`
itself (`src/lib/auth/session.ts`), which works correctly and is sufficient
protection on its own. If you want edge-level protection back, treat this as
an open bug to isolate, not a config tweak -- confirm what `req.auth` actually
contains at the proxy boundary before assuming it's fixed.

### Gotcha: Base UI's `render` prop, not `asChild`

This shadcn setup uses Base UI, not Radix. To render a component as a
different element (e.g. a `Button` as a `Link`), use `render={<Link href="..." />}`
with the children staying on the outer component -- not Radix's `asChild`
wrapper-child pattern. When the target isn't a real `<button>` (e.g. it's a
link), also pass `nativeButton={false}`, or Base UI logs a console warning
about losing native button semantics.

## Conventions

- Server Components by default; add `"use client"` only where interactivity
  requires it (gamification UI, forms).
- Node.js runtime everywhere (never `export const runtime = "edge"`) — Prisma
  and bcrypt need it, and Fluid Compute makes edge unnecessary anyway.
- Next.js 16: `params`/`searchParams`/`cookies()`/`headers()` are all `async`.
  Route protection is per-page via `requireUserId()`, not middleware/proxy.ts
  (see the gotcha above).
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
npm run content:validate # check /content against the schema (see below)
npm run content:seed     # load validated /content into Postgres (idempotent)
npm run db:seed           # validate, then seed
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
  `SpacedRepetitionState` (simplified SM-2, drives weak-spot review; the actual
  scheduling logic is `src/lib/study/spaced-repetition.ts`, pure and unit-tested),
  `ExamAttempt` (`questionIds`/`frqPromptIds` JSON arrays fix the exam's content
  at start time so a reload doesn't reshuffle it mid-exam; `sectionScores`/
  `estimatedScore` are null until submitted).
- **Gamification**: `XPEvent` (append-only ledger — level/streak/totals are
  always *derived* from this, never stored/trusted directly), `Badge`,
  `UserBadge`, `BossBattleAttempt`.
- **Social**: `Class`, `ClassMembership`, `Friendship`, `User.leaderboardOptOut`.

There's no dedicated topic-detail route: "browse by topic" is the unit page's
topic filter (`?topic=<slug>`), which is also what a question's "review this
concept" link points at. Revisit only if topics need their own content beyond
filtering (e.g. topic-level notes).

### Practice modes (Milestone 4)

Two quiz entry points share one `QuizRunner` (`src/components/study/quiz-runner.tsx`)
and one server-side rendering helper (`src/lib/study/render-quiz.ts`):

- `courses/[courseSlug]/units/[unitSlug]/quiz` — unit practice from the
  question-browser filters, "back" goes to the unit.
- `courses/[courseSlug]/quiz` — generic, takes `?ids=&source=&back=&backLabel=`;
  everything else (custom quiz, weak-spot review, daily challenge) redirects
  here after picking which questions belong in the quiz. `source` is the
  `AttemptSource` recorded on each `QuestionAttempt` (QUIZ/WEAK_SPOT/DAILY).

Custom quiz, weak-spot review, and the daily challenge are all **course-scoped**
(`/courses/[courseSlug]/practice/...`), not global — deliberately, to keep
routing simple (no quiz spans multiple courses). The daily challenge's
"completed today" check is just `QuestionAttempt` rows with `source: DAILY`
created since midnight — no separate table.

**Exam simulation** (`courses/[courseSlug]/exam`) is its own flow, not a
`QuizRunner` variant, because the UX is genuinely different: sequential
MCQ-then-FRQ with a countdown timer and *no* per-question reveal (`ExamRunner`,
`src/components/study/exam-runner.tsx`), submitted all at once
(`submitExamAttempt`), with explanations/grading deferred to the results page.
`estimateApScoreRange` (`src/lib/study/exam-scoring.ts`) is a deliberately
crude, unit-tested heuristic from MCQ accuracy alone — always labeled
"estimate" in the UI, not a real predictor. Known approximation: the results
page's "what did you pick on this exam" lookup matches `QuestionAttempt` rows
by user+question+`source: EXAM` (there's no FK from `QuestionAttempt` to a
specific `ExamAttempt`), so it can't perfectly disambiguate two attempts at
the same course's exam close together. Fine for now; revisit if that matters.

**FRQ self-grading** (`src/components/study/frq-self-grade.tsx`) finally puts
Milestone 1's `SelfGradingStrategy` (`src/lib/scoring/grading.ts`) to use, and
is shared between two contexts: standalone practice (write + grade in one
sitting, `submitFrqAttempt` creates the attempt already graded) and exam
results (the response was already saved un-graded at submission time, so
`updateFrqGrade` grades the existing `FRQAttempt` instead of creating a new one).

### Content pipeline (Milestone 2)

`/content/<course-slug>/{course.json, units/*.json, questions/*.json, frqs/*.json}`
is the source of truth, authored by hand or generated. Nothing in the app reads
these files directly.

```
npm run content:validate   # Zod shape + semantic checks, see below
npm run content:seed       # upserts validated content into Postgres (idempotent, keyed by slug/id)
npm run db:seed            # both, in order
```

The Zod schemas live in `src/lib/content/schema.ts`. The semantic rules (not
expressible in Zod alone) live in `src/lib/content/validate.ts` as pure,
unit-tested functions (`tests/content-validate.test.ts`) — `scripts/validate-content.ts`
just walks `/content` and calls them:

- exactly one `isCorrect` choice per question, labels sequential (A, B, C, ...)
- `conceptLink` matches `<course>/<unit>/<topic>` exactly
- every `unit`/`topic` a question or FRQ references actually exists in that
  course's `units/*.json`
- FRQ rubric points sum to exactly `pointValue`
- no duplicate ids (MCQs and FRQs share one id space per course)
- balanced `$...$` and ` ```...``` ` delimiters in markdown fields (catches the
  most common authoring slip: an unclosed fence)

Numerical-answer verification (for Calculus/Physics, per the original content
sourcing rules) isn't built yet — there's no numerical content until Milestone 7.

**MCQ Question** (`content/<course>/questions/*.json`, one JSON array per file)
```
id, unit, topic, difficulty (easy|medium|hard),
stem (markdown; supports $latex$ and ```code``` fences),
choices: [{ label, text, isCorrect, explanation }]  (4 or 5 choices, exactly one isCorrect),
explanation (why the correct answer is right),
conceptLink ("<course-slug>/<unit-slug>/<topic-slug>"),
reviewed (bool, default false)
```

**FRQ Prompt** (`content/<course>/frqs/*.json`)
```
id, unit, topic, prompt, pointValue,
rubric: [{ id, points, description }]  (points must sum to pointValue),
sampleResponse,
reviewed (bool, default false)
```

**Course** (`content/<course>/course.json`) and **Unit** (`content/<course>/units/*.json`,
each with a nested `topics` array) match `CourseSchema`/`UnitSchema` in
`src/lib/content/schema.ts` — see that file for the exact shape, including
`examFormat` (why this must stay data, not hardcoded, is explained below).

**Sample bank seeded so far**: AP CSA, Units 1 and 4 only (14 MCQs, 2 FRQs) —
enough to prove the model end-to-end. The other 8 units and the other three
courses are Milestone 7.

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
- [x] **Milestone 2 — Content foundation.** Zod schema + pure, unit-tested
      validation rules (`src/lib/content/`), `validate-content`/`seed` scripts,
      sample AP CSA bank (2 units, 14 MCQs, 2 FRQs) authored, validated, and
      seeded into Neon — confirmed idempotent and checked directly against the
      DB. 13 tests added (16 total), all clean.
- [x] **Milestone 3 — Core study loop.** Email/password signup+login (Server
      Actions + `useActionState`), session-aware header, per-page
      `requireUserId()` route protection. Course list → course detail (units,
      enroll) → unit detail (topics, filterable question list: topic/
      difficulty/bookmarked/missed) → quiz (full explanations per choice, the
      concept-review link, results screen). Bookmarks and attempts persist to
      Postgres; dashboard shows per-unit mastery derived from attempt history.
      5 tests added (21 total). Verified end-to-end in-browser: signup, login,
      logout, enroll, filter, take a 7-question quiz, bookmark persistence
      across reload, dashboard accuracy matching the quiz result, and
      logged-out users correctly bounced from protected pages.
- [x] **Milestone 4 — Practice modes.** Custom quizzes (pick units/difficulty/
      length), weak-spot review (spaced-repetition scheduling now wired into
      `recordAttempt`), daily challenge (5 questions, prioritizes what's due),
      FRQ self-grading (standalone and reused for exam results), and full exam
      simulation (timed, sectioned, no reveal until submission, estimated AP
      score range). `ExamAttempt` gained `questionIds`/`frqPromptIds` columns
      (migrated). 8 tests added (29 total). Verified end-to-end in-browser:
      custom quiz across both units, spaced-repetition state confirmed correct
      directly against the DB after a hit and a miss, FRQ practice (checked
      rubric lines against a deliberately-buggy response, got a partial score),
      and a full exam run (timer, no-reveal MCQs, empty-FRQ handling, results
      page scoring/estimate/review, dashboard reflecting the exam's attempts).
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
- **`npm audit` reports vulnerabilities** in `hono`/`mysql2` — both transitive
  dev dependencies of the `prisma` CLI itself (bundled tooling for databases/
  features we don't use), not runtime/production code. `npm audit fix --force`
  would downgrade Prisma to 6.19.3, which is a step backward, not a fix — don't
  run it. Revisit when Prisma ships a clean fix upstream; not urgent.
- **Prisma 8 exists as a release candidate** (`8.0.0-rc.x`, currently tagged
  `latest` on npm) with a materially different CLI (`prisma.config.ts`, no more
  traditional `schema.prisma`-only flow). We deliberately pinned to the last
  stable release, **Prisma 7.10.0**. Don't `npm update` Prisma casually.
- **No middleware-level route protection** — see the proxy.ts gotcha above.
  Every protected page must call `requireUserId()` itself; there's no fallback
  if one forgets to.
