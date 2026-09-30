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

**Bug found and fixed post-launch**: `sendFriendRequest` looked up the target
by exact-case `username` (`findUnique`), but signup (`auth/schema.ts`) never
normalizes case, so searching `johndoe` silently failed to find an account
registered as `JohnDoe` ("No user found with that username" even though it
exists) — reported by the owner while testing. Fixed by switching the lookup
to `findFirst` with `mode: "insensitive"` (`src/lib/social/actions.ts`).
Signup's own username-uniqueness check (`src/lib/auth/actions.ts`) got the
same case-insensitive treatment, so two accounts can't register case-variant
usernames (e.g. `JohnDoe` and `johndoe`) that would make the now-insensitive
friend search ambiguous. Verified end-to-end with two scratch accounts
(mixed-case and lowercase usernames, both cleaned up after): case-insensitive
search found the target, request sent/appeared/accepted correctly, and both
users showed up in each other's friends list and leaderboard.

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

**Sample bank seeded so far**: all four launch courses are fully authored —
AP CSA (10 units, 300 MCQs + 30 FRQs), AP World History: Modern (9 units,
270 MCQs + 35 FRQs), AP Calculus AB (8 units, 240 MCQs + 24 FRQs), and AP
Physics 1 (8 units, 240 MCQs + 24 FRQs). See the Milestone 7 section below.

### Content generation at scale (Milestone 7, done)

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
explanations, rather than trusting a plausible-looking trace.

**AP World History: Modern — done.** All 9 units of the stable CED (The
Global Tapestry → Networks of Exchange → Land-Based Empires → Transoceanic
Interconnections → Revolutions → Consequences of Industrialization → Global
Conflict → Cold War and Decolonization → Globalization), each with 30 MCQs +
3 SAQs (270 MCQs + 27 SAQs total), plus a separate course-level pool of 4
DBQs + 4 LEQs (`content/ap-world/frqs/dbq-leq-pool.json`) not tied to a
single unit's narrow time period — 35 FRQ-type items total. Unlike CSA,
this course's exam has three distinct non-MCQ item types (SAQ/DBQ/LEQ), not
one uniform FRQ, so this was an explicit scope decision (asked the owner via
AskUserQuestion before writing 9 units' worth of content): SAQs are
per-unit since they're naturally unit-scoped on the real exam, while DBQs
and LEQs — which typically synthesize across broader time periods rather
than fitting one unit — got their own pool, each still tagged to whichever
unit its theme most centers on (a required FK, since `FRQPrompt.unitId` is
non-optional). DBQ documents are original, invented-but-plausible excerpts
with realistic attributions (not verbatim quotes from real historical
sources or from any College Board exam) to stay clearly original while
still exercising the document-analysis skill. `examFormat` in
`content/ap-world/course.json` reflects the *current* (pre-May-2027) exam
structure per the table below, not the upcoming change.

**Known gap this surfaced**: `FRQPrompt` has no field distinguishing
SAQ/DBQ/LEQ (or, for CSA, there was never a need to distinguish types at
all). The exam simulator (Milestone 4) picks `questionCount` FRQPrompts at
random from a course's whole pool to fill a section — for CSA that's fine
(one homogeneous type), but for AP World History it means an exam sim run
could hand a student 3 SAQs and no DBQ/LEQ, or any other mix, rather than
reliably the 1 SAQ + 1 DBQ + 1 LEQ the real exam gives. Fixing this would
mean adding an item-type field to the schema/model and updating the exam
selection logic — an app-engine change, out of scope for a content-only
milestone. Flagging it here rather than either silently building it
unasked or silently shipping content that won't exercise correctly.

**AP Calculus AB — done.** All 8 units of the current (pre-May-2027) CED
(Limits and Continuity → Differentiation: Definition and Fundamental
Properties → Differentiation: Composite, Implicit, and Inverse Functions →
Contextual Applications of Differentiation → Analytical Applications of
Differentiation → Integration and Accumulation of Change → Differential
Equations → Applications of Integration), each with 30 MCQs + 3 FRQs (240
MCQs + 24 FRQs total), validated and seeded. `FRQPrompt`'s generic shape
needed no changes here — unlike AP World History, Calc AB's FRQs are
uniformly "FRQ" on the real exam, so the CSA-era model fit directly.
Correctness approach (this is the course the spec's "extra scrutiny for
numerical correctness... verified programmatically where possible" is
squarely aimed at): every non-trivial computed answer — derivatives,
antiderivatives/definite integrals, limits, and differential-equation
solutions — was checked with `sympy` (`pip3 install --user sympy`; not a
project dependency, just a local verification aid, so nothing was added to
`package.json`) before being written into the question/choice/explanation
text, rather than trusting hand arithmetic. This was adopted as a direct,
lower-overhead substitute for a dedicated numeric-verification script that
had been separately discussed but never built — sympy-checking each answer
inline satisfies the same "verified programmatically" requirement without
that extra tooling investment. No changes needed to `examFormat` in
`content/ap-calc/course.json` beyond what was already set from the verified
course-info table (42 MCQ + 6 FRQ, 3h10m) — note the table's flagged
**May 2027 format change** isn't yet published in enough detail to encode,
so this remains the current-format data until College Board publishes specifics.

**AP Physics 1 — content not yet started; diagram infra built first.** Asked
the owner how to scope this given Physics 1 leans heavily on diagrams
(free-body diagrams, motion graphs) that the markdown+LaTeX+code content
pipeline can't render — chosen answer: build minimal SVG diagram support in
the app before writing any Physics content, rather than word-describing
everything or skipping diagram-dependent problems. This landed as its own
app-engine change (schema + rendering), planned and reviewed separately from
the content-only Milestone 7 pattern.

**Diagram support**: `Question`/`FRQPrompt` gained an optional `diagram Json?`
column (migration `20260929215128_add_diagram_field`), typed via a Zod
discriminated union in `src/lib/content/diagram-schema.ts` — `xy-graph`
(labeled axes + up to 3 piecewise-linear series; for position/velocity/
acceleration-vs-time, force-vs-time, etc.) and `force-diagram` (an object
marker with labeled force vectors at angle/magnitude, optional incline). This
is a **sibling structured field to `stem`/`prompt`, not embedded in the
markdown itself** — deliberately, so it stays fully typed/validated instead
of hand-authored raw SVG, and never touches the `unified`/remark/rehype
pipeline in `src/lib/content/render.ts` (no `rehype-raw`/sanitize step
needed, no XSS surface). Rendering is plain SVG built on pure, unit-tested
coordinate-transform math (`src/lib/diagrams/geometry.ts`) — no charting
library — via `src/components/diagrams/{xy-graph,force-diagram,diagram-renderer}.tsx`,
dark-mode-aware (`currentColor`/Tailwind `dark:` classes, matching the
`prose dark:prose-invert` convention used everywhere else) and wired into
every question/FRQ render path (unit quiz, boss battles, exam-taking, exam
results, standalone FRQ practice, admin review — 8 call sites across 4
independent data-fetch paths, since there's no single shared "render a
question" function covering all of them).

**Scope boundary** (documented rather than silently expanded, same as the
World History SAQ/DBQ/LEQ gap): only two diagram categories are supported —
reading a given graph (the graph *is* the given data, not word-equivalent)
and force-vector diagrams (directions/magnitudes are awkward to specify
unambiguously in prose). Mechanical scene layouts (inclines, pulleys,
springs, pendulums as physical arrangements) stay word-described in the stem,
as before.

**Bug found and fixed while building this**: the force-diagram's object
label was placed at a fixed position (directly south of the marker), which
could collide with whichever vector's own label happened to land nearby —
first surfaced by a short-magnitude friction vector whose label overlapped
the object label. Fixed with `bestLabelDirection()` (`geometry.ts`), which
places the object label wherever is angularly farthest from every vector on
that diagram, plus `textAnchorForAngle()` so a label anchors away from its
point (not centered on it) when offset mostly left/right — both pure,
unit-tested functions, not a one-off tweak to this test case.

**AP Physics 1 — content done.** All 8 units of the redesigned (2024-25) CED
(Kinematics → Dynamics → Circular Motion and Gravitation → Energy → Momentum
→ Simple Harmonic Motion → Torque and Rotational Motion → Fluids), each with
30 MCQs + 3 FRQs (240 MCQs + 24 FRQs total), validated and seeded. `g=9.8
m/s²` used throughout (not the g=10 shortcut), with realistic decimal
answers rounded to 2-3 significant figures — unlike Calc AB's exact symbolic
answers, this matches how real AP Physics 1 problems are conventionally
solved and graded. Every non-trivial computed answer (kinematics, forces,
energy, momentum, circular motion, gravitation, SHM periods, torque,
rotational inertia, fluids) was checked with a Python arithmetic/sympy
script before being written into the question/choice/explanation text, same
verification discipline as Calc AB. A handful of "nice-angle" problems use
the standard AP approximation sin37°≈0.6/cos37°≈0.8 (3-4-5 triangle),
flagged explicitly in the stem rather than left implicit.

The new diagram infrastructure (`xy-graph`/`force-diagram`, see above) is
used where it's the natural fit per the scope boundary already
established — motion graphs in Unit 1's representations-of-motion topic and
free-body diagrams in Unit 2's free-body-diagrams topic, plus a few FRQs
elsewhere (Unit 1 motion graph, Unit 2 incline FBD). Not overused: the large
majority of MCQs/FRQs across all 8 units are still plain word problems,
since most physics content (kinematics equations, force calculations, energy
conservation, circular motion, gravitation, SHM, torque, fluids) is fully
expressible in prose without a diagram — matching the deliberately narrow
scope decided before building the diagram feature.

**Caught and fixed a real content bug during authoring**: Unit 4's roller
coaster MCQ (`ap-phys1-u4-mcq-18`) initially had the correct numeric answer
(≈16.6 m/s, from Δh=14m via v=√(2gΔh)) written into the wrong choice's
`isCorrect` flag, with a garbled self-correcting explanation left in the
"correct" choice. Caught by re-verifying the computation against the
Python-checked value before moving on, not by a later pass — rewrote the
question's choices/explanations cleanly rather than leaving the contradiction
in place.

This completes Milestone 7 — all four launch courses now have full content
banks (see the Milestone status table below).

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

### Polish and launch prep (Milestone 8, done)

Before scoping this milestone, investigated the actual current state of each
area (two Explore agents plus direct verification) rather than assuming what
was missing — several things that looked necessary turned out fine (viewport
meta is already correct, Next injects it by default even with no explicit
`viewport` export), while a few real gaps and two live bugs surfaced during
manual testing.

**Error handling**: `src/app/error.tsx`, `not-found.tsx`, and
`global-error.tsx` added — none existed before, so any uncaught error (a
failed Prisma call, an unauthenticated Server Action) fell through to
Next's default, unstyled pages. `global-error.tsx` renders its own
`<html>`/`<body>` per Next's convention (it replaces the root layout when
the error originates there) and deliberately avoids the shared `Button`/
`SiteHeader` — anything that could itself be part of what crashed.
Investigated whether the duplicated `requireUserId()` in
`study/actions.ts`/`social/actions.ts` (throws `Error("Not authenticated")`
instead of the canonical `redirect("/login")` in `auth/session.ts`) was an
accidental bug — it isn't: the comment in `auth/session.ts` documents this
as deliberate ("redirect() isn't the right tool mid-mutation"). Left it
alone; `error.tsx` now gives whatever it throws a graceful fallback instead
of Next's raw default, without relitigating that decision.

**Accessibility**: skip-to-content link in `layout.tsx` (`sr-only
focus:not-sr-only`, jumps to a new `id="main-content"` on `<main>`). The
exam countdown timer (`exam-runner.tsx`) gained a visually-hidden
`aria-live="polite"` region -- deliberately *not* wired to update every
second (would spam screen readers with the ticking countdown); a
`checkpointAnnouncement()` helper only returns a message at whole-minute
marks, then every 10s in the final minute, and the state update happens
during render (comparing against the last announcement) rather than in a
`useEffect`, to satisfy the `react-hooks/set-state-in-effect` lint rule
without cascading renders.

**Mobile testing**: walked the golden path (signup → courses → dashboard →
unit → quiz → exam → friends → classes) at the Browser pane's mobile
preset (375px) and found two real bugs, not just theoretical risks:
1. The header (`site-header.tsx`) had no mobile nav pattern at all -- at
   375px the "AP Study App" wordmark wrapped onto 3 lines and the 5 nav
   links wrapped ungracefully, since the only mobile handling was
   `flex-wrap`. Fixed with a proper hamburger menu
   (`site-header-mobile-nav.tsx`, a small client component using
   `lucide-react`'s `Menu`/`X` icons, already an installed-but-unused
   dependency) that shows a vertical dropdown below `sm:`, and keeps the
   original row layout at `sm:` and above.
2. The mobile menu didn't auto-close after tapping a nav link, since
   `SiteHeader` lives in the persistent root layout and doesn't remount on
   client-side navigation -- the menu would stay open, covering the page
   just navigated to. Fixed by comparing `usePathname()` against the last-
   seen pathname and closing the menu when it changes -- again during
   render (not a `useEffect`) for the same lint reason as the exam timer.

Also found the level/streak badge and username were needlessly hidden below
`sm:`/`md:` (`hidden ... sm:flex` etc.) -- leftover from when the only
mobile handling was wrapping in a cramped single row. Now that there's a
proper dropdown with room to show everything, removed those hides.

Preventive (not empirically triggered, but a real gap on inspection):
`RewardToast`'s badge-earned card has no width constraint, and the longest
badge description ("Get every attempted question in a unit correct", 46
chars at `text-xs`) sits right at the edge of a 375px viewport with no
margin for smaller phones. Added `w-[calc(100vw-2rem)] max-w-xs` to the
toast's outer container so it can never exceed the viewport regardless of
future badge copy.

**Performance**: `renderContentToHtml` (`src/lib/content/render.ts`, the
Shiki/KaTeX pipeline) wrapped in React's `cache()` for per-request
memoization -- `render-quiz.ts` calls it once per stem, explanation, and
choice explanation, per question, every request, and the same markdown
always produces the same HTML, so re-running the full pipeline on a cache
hit was pure waste. Cross-request caching (`unstable_cache`) would be a
bigger win but needs invalidation handling on content re-seed; not pursued,
consistent with not over-engineering for this app's scale. `RewardToast`
(and its only real dependency, `framer-motion`) is now `next/dynamic`-
imported with `ssr: false` from `quiz-runner.tsx` and `frq-self-grade.tsx`
-- the two shared, high-traffic components that only pulled it in
transitively (unlike `boss-battle-runner.tsx`, which uses `framer-motion`
directly for its own health-bar animation and so gets no benefit from this).

**README**: expanded from a stub deferring everything to CLAUDE.md into a
proper feature list + tech stack summary + setup steps, while still
pointing to CLAUDE.md as the single source of deep architecture/data-model
detail.

**Deployment — done.** Investigated via `vercel env ls` / `vercel project
inspect` before touching anything (see above), then got explicit owner
sign-off before each Vercel-touching step: generated a real `AUTH_SECRET`
and added it to all three Vercel environments (`vercel env add ... --value`,
non-interactive), connected the GitHub repo (`vercel git connect`, pushes to
`main` now auto-deploy), and triggered the first production deployment
(`vercel deploy --prod`). Live at
[ap-study-app-pi.vercel.app](https://ap-study-app-pi.vercel.app). Smoke-tested
end-to-end on the production URL itself (not just locally): signup, session
cookie/`session.user.id` (the exact thing the `jwt`/`session` callbacks
gotcha above is about), reading the seeded course/unit/question data,
answering and submitting a quiz question, and the XP/badge/reward-toast path
all confirmed working against the real production build and database. This
created one real test account (`deploy-smoketest@example.com` / username
`deploy_smoketest`) in the shared Neon database -- harmless, but worth
knowing it's there if the user list ever looks unfamiliar.

## Appearance: color themes and dark mode (post-launch)

The original UI shipped in the shadcn default grayscale palette (`--primary`
etc. all `oklch(... 0 0)`, zero chroma). The owner asked for color, reviewed 4
mockups (a Design canvas Artifact), and picked all 4 to ship as
user-selectable themes, plus a light/dark toggle -- **Fresh Mint, light** is
the product default (not the old grayscale, which no longer exists).

- **4 themes × 2 modes = 8 palettes**, defined as CSS custom properties in
  `globals.css`: Fresh Mint (teal/coral, the default -- lives directly in
  `:root`/`.dark` rather than behind an attribute selector, so the app still
  renders correctly before the theme store hydrates or with JS disabled),
  Sunrise (warm coral/amber), Deep Study (navy/gold), Playground
  (violet/pink) -- the latter 3 override via `[data-color-theme="..."]` /
  `.dark[data-color-theme="..."]` on `<html>`.
- **State**: `src/lib/theme/theme-store.ts`, a zustand `persist` store
  (`colorTheme`, `mode`), same pattern and same reasoning as
  `sound-store.ts` -- per-device localStorage preference, never server
  state, key `ap-study-app:theme`.
- **No flash of the wrong theme on load**: a `next/script`
  `strategy="beforeInteractive"` tag in `layout.tsx`
  (`src/lib/theme/inline-script.ts`) reads that same localStorage key and
  paints `<html>`'s `class`/`data-color-theme` before hydration; `<html>`
  needs `suppressHydrationWarning` since this is an intentional DOM mutation
  React didn't render. `src/components/theme/theme-sync.tsx` (mounted once
  in the root layout) takes over from there, applying the store's state to
  `<html>` on every subsequent change (toggle, settings picker) -- gated on
  a `hasHydrated` flag so it never overwrites the inline script's correct
  initial paint with the store's not-yet-rehydrated default.
- **UI**: a header icon toggle (`theme-toggle.tsx`, next to the existing
  `SoundToggle`) for quick light/dark switching, and a full "Appearance"
  card on `/settings` (`theme-settings.tsx`) with a mode segmented control
  and 4 theme swatches -- this is the "settings menu" the owner asked for.
- **Bug found and fixed while building this**: `onRehydrateStorage`'s
  callback threw `ReferenceError: Cannot access 'useThemeStore' before
  initialization` every time -- it referenced the outer `useThemeStore`
  const to call `.setState()`, but for synchronous storage (localStorage),
  zustand's persist rehydration completes *inside* the `create()` call
  itself, before that `const` assignment finishes. Net effect: `hasHydrated`
  silently never became `true`, so `ThemeSync` never applied any live
  change -- the toggle/settings picker updated localStorage correctly but
  the page didn't visually update until a hard reload. Only surfaced by
  checking actual DOM state after a click, not just the screenshot (which
  looked unchanged either way) or localStorage (which was already correct).
  Fixed by following zustand's own documented pattern: a `setHasHydrated`
  store action, called via the live store instance zustand passes as
  `onRehydrateStorage`'s callback argument, never the outer const.
  Verified end-to-end after the fix: fresh page load in each of the 8
  palettes (no flash), the header toggle and the settings picker both
  updating the page live, and the choice persisting across a hard reload.

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
      `tsc` all clean. Vercel project linked (`ap-study-app`). GitHub repo
      created at [github.com/Octolord12/ap-study-app](https://github.com/Octolord12/ap-study-app)
      (Milestone 7).
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
- [x] **Milestone 7 — Content at scale.** Full starter banks (~30 MCQ + 3
      FRQ-type items per unit), validated, plus a review workflow. Scope
      decision: one course at a time, pausing for owner review after each
      (see the Content generation section above). **AP CSA**: 10/10 units,
      300 MCQs + 30 FRQs. **AP World History: Modern**: 9/9 units, 270 MCQs +
      27 SAQs, plus a separate course-level pool of 4 DBQs + 4 LEQs (35 FRQ-
      type items total) — see the known exam-engine gap (no SAQ/DBQ/LEQ type
      field on `FRQPrompt`) noted above. **AP Calculus AB**: 8/8 units, 240
      MCQs + 24 FRQs, every computed answer sympy-verified. **AP Physics 1**:
      8/8 units, 240 MCQs + 24 FRQs, every computed answer Python-verified;
      required building minimal SVG diagram support first (its own
      app-engine change, see above) since this course leans on motion graphs
      and free-body diagrams the markdown pipeline couldn't render. All four
      courses seeded and validated. Admin review UI built (`/admin/review`),
      covering all four courses.
- [x] **Milestone 8 — Polish and launch prep.** Investigated actual current
      state before scoping rather than assuming (viewport meta was already
      correct; the duplicated `requireUserId()` in Server Actions turned out
      to be a deliberate design decision, not a bug). Error handling
      (`error.tsx`/`not-found.tsx`/`global-error.tsx`, none existed before).
      Accessibility (skip-to-content link, checkpoint-based `aria-live` on
      the exam timer). Mobile testing found and fixed two real bugs during a
      golden-path walkthrough at 375px (no mobile nav pattern at all; the
      new mobile menu not auto-closing after navigation) plus a defensive
      reward-toast width fix. Performance (`renderContentToHtml` wrapped in
      React's `cache()`; `RewardToast`/`framer-motion` `next/dynamic`-
      imported from its two transitive-only consumers). README expanded
      from a stub into a proper feature list + setup guide. Deployed to
      production on Vercel (`AUTH_SECRET` generated and set, GitHub repo
      connected for auto-deploy, first deploy triggered) and smoke-tested
      end-to-end on the live URL itself — signup, session, seeded content,
      a full quiz question with XP/badge/reward-toast, all confirmed
      working against the real production build and database. Live at
      [ap-study-app-pi.vercel.app](https://ap-study-app-pi.vercel.app).

## Known issues / follow-ups

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
