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
| Client state | Zustand | The mute preference (`src/lib/gamification/sound-store.ts`, localStorage-persisted); boss-battle/quiz UI state is plain `useState`. |
| Animations/sound | Framer Motion, canvas-confetti | Level-up/badge/boss-defeat feedback, with a mute toggle. Sound is synthesized Web Audio tones, not Howler/audio files — see the gotcha below. |
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

### Gotcha: sound effects are synthesized, not audio files

`howler` was in the original stack plan but we never added actual sound
assets (no files to source/license this way). `src/lib/gamification/sound.ts`
generates simple tones with the raw Web Audio API instead -- a correct-answer
ding, a level-up arpeggio, a badge fanfare. If real sound design ever gets
added (actual audio files), Howler is the natural place to bring in, but for
now it's an unused dependency; don't be surprised it's not wired to anything.
The mute check lives inside `sound.ts` itself (reads `useSoundStore.getState()`
directly, works outside React), so every call site is automatically silent
when muted -- no need to check `muted` before calling these.

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
- **Gamification**: `XPEvent` (append-only ledger — level is always *derived*
  from this, never stored), `Badge`, `UserBadge`, `BossBattleAttempt`. Streak
  state (`currentStreak`/`longestStreak`/`lastActiveDate`/`streakFreezesAvailable`)
  lives directly on `User`, updated incrementally rather than derived — see
  the Gamification section below for why that's different from the XP/level
  philosophy.
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

### Gamification (Milestone 5)

XP, levels, and streaks are pure, unit-tested functions wired into one
DB-touching entry point:

- `src/lib/gamification/xp.ts` — `xpForCorrectAnswer(difficulty, streak)` and
  `xpForFrqPoints(points, streak)`, both difficulty/point-scaled plus a capped
  streak bonus.
- `src/lib/gamification/level.ts` — `computeLevel(totalXp)`. Cost to clear
  level *n* is `100n` XP (level 1→2 costs 100, 2→3 costs 200, ...); level is
  *always derived* from the `XPEvent` sum, never stored, matching the XP
  ledger's own append-only philosophy.
- `src/lib/gamification/streak.ts` — `updateStreakOnActivity(state, today)`.
  Updates `User.currentStreak`/`longestStreak`/`lastActiveDate`/
  `streakFreezesAvailable` *incrementally*, once per day's first activity, not
  recomputed from full history -- see the schema comment on `User` before
  changing this. A single skipped day auto-consumes a freeze (starts at 1, no
  replenishment yet); a longer gap breaks the streak regardless.
- `src/lib/gamification/activity.ts` — `grantXpForActivity(userId, xpFormula)`
  ties the above together: updates the streak if this is the day's first
  activity, computes XP using the (possibly just-updated) streak, writes the
  `XPEvent`, and detects a level-up by comparing `computeLevel()` before/after.
  Called from every scoring path (`recordAttempt`, `submitFrqAttempt`,
  `updateFrqGrade`, `submitExamAttempt`'s MCQ loop) in `src/lib/study/actions.ts`.
  A zero-point FRQ grade earns no XP/streak credit (see `grantFrqXpIfEarned`),
  and re-grading an already-graded FRQ attempt (revisiting exam results) can't
  re-farm XP -- both guard against the obvious ways to game a system that's
  otherwise "any correct answer earns something."
- `src/lib/gamification/badges.ts` — a fixed catalog (`BADGE_DEFINITIONS`) and
  `checkAndAwardBadges(userId)`, called after every scoring action. It checks
  *all* not-yet-earned badges against current state each time (small, indexed
  queries against a 6-badge catalog -- cheap enough not to need an event-driven
  system at this scale), so a badge whose criteria were already met by past
  activity gets awarded retroactively the first time this runs, not just on
  the specific action that would have triggered it live. "Perfect score" is
  approximated as `perfect_ten` (10 correct in a row, since there's no
  quiz-session entity to check a single quiz's score against) and "unit
  mastery" as 100% correct on every attempted question in some unit.
- **Boss battles** (`src/components/study/boss-battle-runner.tsx`,
  `/courses/[courseSlug]/units/[unitSlug]/boss`) reuse `recordAttempt` per
  question (same XP/streak/badge path as any quiz, `source: "QUIZ"` -- no
  dedicated `AttemptSource` variant) and add `submitBossBattle` on completion,
  which upserts `BossBattleAttempt` (pass threshold: 70% correct; once
  conquered, `passed` never reverts even if a later attempt does worse).

`RewardToast` (`src/components/gamification/reward-toast.tsx`) is the shared
UI for all of this -- XP/level-up/badge feedback, sound, and confetti in one
component, rendered by `QuizRunner`, `FrqSelfGrade`, and `BossBattleRunner`
after each scoring server action returns. It respects `prefers-reduced-motion`
via `useReducedMotion()`.

**Bug found and fixed while wiring this in**: `QuizRunner`'s "done" screen was
derived from `results.length === questions.length`, which goes true the
instant the *last* question's answer is recorded -- before the student ever
saw its reveal/explanation. Practice mode was silently skipping the final
question's explanation for every quiz. Fixed by tracking `finished` as its own
state, set only when the student clicks past the last question, not inferred
from the results array. If you're touching quiz-completion logic, keep this
distinction (an array reaching its final length is not the same event as "the
user has seen the last item").

### Social (Milestone 6)

`Class`/`ClassMembership`/`Friendship`/`User.leaderboardOptOut` were all
already in the schema from Milestone 1 -- this milestone is pure feature work,
no migration.

- `src/lib/social/leaderboard.ts` — `rankLeaderboard(candidates)`, pure and
  unit-tested: filters out opted-out users *entirely* (they don't occupy a
  rank, they're not just hidden) and sorts by XP descending. The DB
  aggregation that produces candidates (`src/lib/social/queries.ts`,
  `computeLeaderboard`) is a thin wrapper — sums `XPEvent.amount` via Prisma's
  `groupBy`, windowed to the last 7 days for "weekly" or unwindowed for
  "all time." "Weekly" is a rolling 7-day window ending now, not a
  calendar week — simpler than getting timezone/week-start right for a
  one-family app at this scale.
- `src/lib/social/invite-code.ts` — 6-character codes, alphabet deliberately
  excludes `0/O/1/I/L` (visually ambiguous when read aloud or copied by hand).
  `createClass` retries a few times on a collision before giving up.
- **Both leaderboard scopes reuse the same query + `LeaderboardTable`
  component**: `getFriendsLeaderboard` sums XP across the user + their
  accepted friends, `getClassLeaderboard` across a class's members. The
  week/all-time toggle is two plain `?period=` links, not client state — the
  whole page is a Server Component.
- Privacy default: leaderboards and member/friend lists always show
  `username`, never `displayName` (which the signup form's "Your name" field
  lets a student fill with anything, including a real name) — see the
  `/settings` copy, which says this explicitly so it's not just an implicit
  behavior.
- **Anti-abuse**: `respondToFriendRequest` checks the *current* session user
  is actually the request's addressee before accepting/declining (not just
  "some logged-in user") — the obvious authorization hole to get right here.
  `sendFriendRequest` blocks self-requests and duplicate requests in either
  direction. Beyond that, the main anti-abuse property was already true
  before this milestone and doesn't need anything new: XP is always computed
  server-side from stored attempts (never trusted from the client — see
  Milestone 5's `grantXpForActivity`), so leaderboard standings can't be
  faked by a client sending a bogus XP number, because no such number is ever
  accepted from a client anywhere in the app.

**Not built**: unfriending, deleting/renaming a class, removing a member, or
transferring class ownership. `leaveClass` exists for members but explicitly
refuses to let an `OWNER` leave (would orphan the class) — noted in that
function rather than silently allowed.

**Compliance note for the owner** (not legally binding, just what to look
into before this leaves the family): now that there's cross-user visibility
(leaderboards, class rosters, friend requests by username), review COPPA
before adding anyone under 13 as a user — friend requests and class rosters
that expose a minor's chosen username to other users may count as
"collection" under COPPA depending on what's visible to whom, even though no
real names or contact info are shown. If a class is ever used in an actual
school setting, FERPA and state student-privacy laws (e.g. California's
SOPIPA) may also apply to how member lists and progress data are handled.

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

**Sample bank seeded so far**: AP CSA is fully authored (all 10 units, 300
MCQs + 30 FRQs) — see the Milestone 7 section below. AP World History:
Modern, AP Calculus AB, and AP Physics 1 have no content yet.

### Content generation at scale (Milestone 7, in progress)

Scope decision (asked the owner directly given the volume — ~1,050 MCQs +
105 FRQs across all four courses): generate **one course at a time, full
scope, pause for review** rather than a thin pass across all four courses.
AP CSA went first since 2 of its 10 units already existed from Milestone 2.

**AP CSA — done.** All 10 units (official, stable CED: Primitive Types →
Using Objects → Boolean Expressions/if → Iteration → Writing Classes → Array
→ ArrayList → 2D Array → Inheritance → Recursion), each with 30 MCQs + 3 FRQs
(300 MCQs + 30 FRQs total), validated and seeded. Every question/FRQ was
authored with `reviewed: false` per the spec. Deliberately scoped to CSA's
tested primitive types only (`int`/`double`/`boolean`/`char`/`String` —
`byte`/`short`/`long`/`float` are out of the CED and don't appear anywhere).
Correctness approach for a CS course (the spec's "verify programmatically
where possible" is really aimed at Calc/Physics numerics): every Java
snippet was hand-traced before writing the "correct" answer and distractor
explanations, rather than trusting a plausible-looking trace. Not yet
started: AP World History: Modern, AP Calculus AB, AP Physics 1 — each is
its own pass through this same process, one at a time, pausing for review
after each.

**Review workflow** (the spec's "simple admin/review view" requirement):
`/admin/review` (`src/app/admin/review/`), gated by `src/lib/admin/session.ts`'s
`requireAdminUserId()` — `requireUserId()` plus a `User.role === "ADMIN"` DB
check (role isn't on the session; see the gotcha above about what *is*).
Non-admins get a 404 (`notFound()`), matching this codebase's existing
authorization-failure convention rather than a dedicated 403 page. Drill-down
mirrors the student-facing course→unit structure: course list with pending
counts → unit list with pending counts → actual unreviewed questions/FRQs
with an "Approve" button (`markQuestionReviewed`/`markFrqReviewed` in
`src/lib/admin/actions.ts`, simple `reviewed: true` updates). No user has
`role: ADMIN` yet — promote one via `db:studio` or a one-off script (ask
before running anything that writes to the DB directly, per the safety
rules this session operates under).

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
- [x] **Milestone 5 — Gamification.** XP (difficulty + capped streak bonus),
      levels (derived from the XP ledger), streaks with single-day freeze
      bridging, a 6-badge catalog checked retroactively after every scoring
      action, unit boss battles (health-bar UI, 70% pass threshold, "conquered"
      never reverts), synthesized-tone sound effects with a mute toggle, and
      reduced-motion-aware reward toasts (XP/level-up/badge). Found and fixed a
      real pre-existing bug while wiring this in: `QuizRunner` was skipping the
      last question's explanation reveal (see the gotcha above). 15 tests added
      (44 total). Verified end-to-end in-browser: XP toast on a correct answer,
      streak going from 0→1 with the header updating live, two badges awarded
      *retroactively* from Milestone 4's leftover activity (proving the "check
      all criteria against current state" design works, not just live triggers),
      a full 7-question boss battle (health bar draining, level-up mid-battle,
      victory screen, "Unit conquered" on the unit page, Boss Slayer + Unit
      Master badges), and the mute toggle.
- [x] **Milestone 6 — Social.** Friend requests (send/accept/decline, with
      server-side authorization on who can respond), classes with
      generated invite codes, weekly (rolling 7-day) and all-time leaderboards
      shared between friends/class scopes, a `/settings` page for the
      leaderboard opt-out. No schema changes needed -- the models existed
      since Milestone 1. 8 tests added (52 total). Verified end-to-end with
      two real accounts: created a class and got an invite code, joined it
      from the second account and saw the leaderboard rank both correctly,
      sent/accepted a friend request across accounts, and confirmed opting
      out actually removes a user from the leaderboard (not just visually)
      while leaving them in the friends list.
- [ ] **Milestone 7 — Content at scale (in progress).** Full starter banks
      (~30 MCQ + 3 FRQ per unit), validated, plus a review workflow. Scope
      decision: one course at a time, pausing for owner review after each
      (see the Content generation section above). **AP CSA done**: 10/10
      units, 300 MCQs + 30 FRQs, seeded and validated. Admin review UI built
      (`/admin/review`). Still to do: AP World History: Modern, AP Calculus
      AB, AP Physics 1 (each its own pass, same process).
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
- **No user has `role: ADMIN` yet**, so `/admin/review` (Milestone 7) isn't
  actually reachable by anyone right now. Promote a user via `db:studio` or
  ask Claude to run a one-off script — this is a direct DB write, so it needs
  explicit sign-off first, same as any other mutating action.
