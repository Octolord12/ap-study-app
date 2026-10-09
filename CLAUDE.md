@AGENTS.md

# AP Study App

A mobile-first, gamified web app for studying AP exams (quizzes, timed practice
tests, FRQ practice, streaks/XP/badges, friend & class leaderboards). Starts as
a tool for one family; built so it can scale into a public product later
without a rewrite, but not over-engineered for that future.

Launch courses: AP Computer Science A, AP World History: Modern, AP Calculus
AB, AP Physics 1. AP U.S. History was added afterwards as a fifth course (see "AP U.S. History").

## Stack (and why)

| Layer | Choice | Why |
|---|---|---|
| Framework | Next.js 16 (App Router, TypeScript), deployed on Vercel | One codebase for frontend + backend, mobile-first, best-documented React framework for a solo maintainer. |
| Styling/UI | Tailwind CSS v4 + shadcn/ui primitives, one custom design system on top | Components you own the code for (not a black box). The look (graphite on paper, one highlighter accent) lives in `globals.css` tokens and a small shared component set -- see "Visual design system" below. |
| Database | Postgres via Neon (Vercel Marketplace) | Serverless, scales to zero, free tier, relational data fits the course→unit→topic→question hierarchy. |
| ORM | Prisma 7 (with `@prisma/adapter-neon` driver adapter) | Gentlest learning curve for a solo maintainer; declarative schema + migrations. Prisma 7's generated client *requires* a driver adapter now (no more bare `new PrismaClient()` reading `DATABASE_URL` implicitly) — see `src/lib/db/index.ts`. |
| Auth | Auth.js (NextAuth v5 beta), Credentials provider, self-hosted | No third party holding user emails (some users may be minors); free; full control. Chosen over Clerk for privacy, per project decision. |
| UI primitives | Base UI (via shadcn) | shadcn's default base for this project's registry version. Polymorphic rendering uses a `render` prop (`<Button render={<Link .../>} />`), **not** Radix's `asChild` — see the gotcha below. |
| Math rendering | KaTeX via `rehype-katex` / `remark-math` | Renders `$...$` / `$$...$$` written directly in content. |
| Code highlighting | Shiki via `rehype-pretty-code` | Same engine as VS Code. **Loads its highlighter asynchronously** — see the gotcha below. |
| Client state | Zustand | The mute preference (`src/lib/gamification/sound-store.ts`) and the light/dark/system mode (`src/lib/theme/theme-store.ts`), both localStorage-persisted; boss-battle/quiz UI state is plain `useState`. |
| Animations/sound | Framer Motion, canvas-confetti | Level-up/badge/boss-defeat feedback, with a mute toggle. Sound is synthesized Web Audio tones, not Howler/audio files — see the gotcha below. |
| Testing | Vitest + React Testing Library | Fast, Jest-compatible, first-class Next.js support. |

### Gotcha: markdown rendering can't use `react-markdown` directly

`rehype-pretty-code` loads a Shiki highlighter asynchronously on first use.
`react-markdown` renders synchronously. Combining them crashes Next's static
prerender with `runSync finished async`. Fix: `src/lib/content/render.ts`
(`renderContentToHtml`) runs the `unified` pipeline directly with
`.process()` (awaited) instead of going through `react-markdown`. Server
Components call it and hand the HTML string to `<Html>`
(`src/components/ui/html.tsx`), or pass it down as a prop to a Client
Component (which can't run the pipeline itself). Don't swap it back to
`react-markdown` without re-testing `next build`.

### Gotcha: the KaTeX we import must be the KaTeX that renders

Math is drawn by the KaTeX that `rehype-katex` / `micromark-extension-math` depend
on (0.16.x), but the stylesheet and fonts come from *our* `katex` dependency
(`@import "katex/dist/katex.min.css"` in `globals.css`). KaTeX renames CSS classes
between versions (`.inner` became `.katex-inner`), so with `katex@0.18` installed
beside a 0.16 renderer, every symbol built from an overlay (`\neq`, `\ne`, `\not`)
lost its positioning and showed as **"x /= 2"**. A reviewer caught it; it had been
live since launch. `katex` is therefore pinned to the renderer's line (`^0.16.47`,
deduped to one copy: `npm ls katex` should show a single version). **Don't bump
`katex` on its own**; move it together with `rehype-katex`. `tests/katex-consistency.test.ts`
fails if the versions differ or the stylesheet lacks the rule for the rendered HTML.

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
npm run content:seed     # load validated /content into Postgres (idempotent); add "-- <course-slug>" to seed one course
npm run db:seed           # validate, then seed
```

Env vars live in `.env.local` (gitignored). `vercel env pull .env.local` re-syncs
them if they ever drift; `.env.example` documents what's needed.

## Data model

Full schema: `prisma/schema.prisma`. Summary:

- **Content** (authored in `/content` as JSON → validated → seeded here; the
  app only reads from the DB at runtime): `Course` → `Unit` → `Topic` →
  `Question` (+ `Choice`) / `FRQPrompt` (with a `type`: `FRQ`, `SAQ`, `DBQ` or `LEQ`, see
  "Exam simulation" below). `Topic.refresher` (markdown, nullable) and `Topic.refresherReviewed` hold the
  topic's written refresher: see "Topic refreshers".
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
- `Enrollment.examDate` (optional, date only): see "Exam date and study plan".
- `PasswordResetToken` (hash of the emailed code, expiry, used-at, a per-minute slot that is unique
  per user, cascades with the user): see "Forgot password and email".
- **Marketing**: `WaitlistSignup` (`email` unique, stored lowercased; deliberately
  not tied to `User`). Added by migration `20261004163500_add_waitlist_signup`.

A topic with a written refresher has its own page (`/courses/<course>/units/<unit>/topics/<topic>`, see
"Topic refreshers"). Without one, "browse by topic" is the unit page's topic filter (`?topic=<slug>`), which is
also what a question's "Review this concept" link falls back to.

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

**Which free-response prompts an exam gets** (`pickExamFrqIds`, `lib/study/exam-selection.ts`,
pure and tested): for each non-MCQ section of the course's `examFormat`, in the order listed,
`questionCount` prompts drawn at random from the prompts whose `FRQPrompt.type` equals the
section's type. CSA, Calc and Physics have one `FRQ` section (4, 6, 4 prompts); World History
has `SAQ` 3, `DBQ` 1, `LEQ` 1, so every World simulation is 55 MCQ + 3 SAQ + 1 DBQ + 1 LEQ in
that order. The runner and results page label each prompt ("Short answer 2 of 3",
"Document-based question", "Long essay"). A type with too few prompts gives a short exam rather
than an error, and `validate-content` fails if a shipped course would be short.
**Bug this replaced (found 2026-10-05, never hit by a student)**: the old code looked only for a
section named `FRQ`; World History has none, so the target was undefined and it fell back to
"use every prompt", which would have been all 53 in one exam. The MCQ draw also used
`sort(() => Math.random() - 0.5)`, which is biased; both draws now use the uniform `shuffled()`.
Still true: one 195-minute clock for the whole exam (sections are not timed separately), no
choice among LEQ prompts, and the score estimate uses MCQ accuracy only.

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
  conquered, `passed` never reverts even if a later attempt does worse). **The
  score is counted on the server, never sent by the browser** -- see "Boss
  battle scoring is server-side" below.

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

**Update 2026-10-04:** the minimum age is now 13 and signup enforces a confirmation; see "Footer, contact and privacy". That is a self-declaration, not a COPPA compliance program.

### Content pipeline (Milestone 2)

`/content/<course-slug>/{course.json, units/*.json, questions/*.json, frqs/*.json, refreshers/*.json}`
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
id, unit, topic,
type (optional: FRQ | SAQ | DBQ | LEQ; omitted means FRQ. Must be one of the course's exam
      section types, so every World History prompt has to say SAQ, DBQ or LEQ),
prompt, pointValue,
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
Physics 1 (8 units, 240 MCQs + 24 FRQs). Each course has since gained a second, harder
set added alongside (see "Hard sets" below): the files named `unit-N-hard.json`. Totals
now: CSA 450 MCQs + 50 FRQs, World 405 + 53, Calc AB 360 + 40, Physics 1 360 + 40. A fifth
course, AP U.S. History (405 + 53), was written later, base and hard sets together (see
"AP U.S. History"). See the Milestone 7 section below.

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

**Known gap this surfaced (fixed 2026-10-05)**: `FRQPrompt` had no field distinguishing
SAQ/DBQ/LEQ, so the exam simulator could not give World History the 3 SAQ + 1 DBQ + 1 LEQ the
real exam has (in fact it would have given every prompt). Now `FRQPrompt.type` exists
(migration `20261006000000_add_frq_type`), every World prompt is typed (36 SAQ, 4 DBQ, 13 LEQ),
and exam selection draws by section type; see "Exam simulation" above. The World course's
`SAQ` section is `questionCount: 3` (it was a placeholder 1 while nothing read it), and
`describeExamFormat` now prints every section's count.

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
`src/lib/admin/actions.ts`, simple `reviewed: true` updates). Each unit page also has an
**"Approve all N in this unit"** button (top and bottom, `ApproveAllButton`, two steps: it asks
first because approval is what the About page counts as "checked by a person").
`approveUnitContent(unitId, questionIds, frqPromptIds)` approves exactly the ids the page
rendered, only those still in that unit and still unreviewed, and is admin-gated; it does not
mean "everything unreviewed at click time", so a seed that lands while the page is open can't get
unseen content approved. There is deliberately no course-level approve-all (it would approve
content nobody opened). **Promoting someone to admin** is a direct database write
(`User.role = ADMIN`): ask first. `viraj1` (the owner's account) was promoted on 2026-10-05.

**Approvals survive a re-seed unless the content changed.** Approvals live only in the
database, and the seed used to write `reviewed: false` over every row. Now `scripts/seed.ts`
reads what is stored first and `nextReviewedFlag` (`lib/content/review-state.ts`, pure and
tested) keeps an approval while the stored content (stem/prompt, choices, explanations, rubric,
diagram, difficulty, type, point value) is the same as the file's, and resets it to unreviewed
when the seed would change it. The seed prints `approvals kept: N, reset because the content
changed: M` per course. A file that says `reviewed: true` always wins. So editing a question
and re-seeding sends it back for review, which is the point.

**Review status (2026-10-05): the owner approved everything** in `/admin/review`: all 1,758
items (1,575 questions + 183 free-response prompts), checked directly in the database
afterwards (0 unreviewed, the About page reads "1,758 of 1,758 have been checked by a person").
The JSON files still say `reviewed: false` (they are the authored state); the approval lives only
in the database and survives re-seeds as described above. Anything new or edited starts
unreviewed again, so the About page count will drop below 100% until it is approved.

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
`deploy_smoketest`) in the shared Neon database. It and the other early test
accounts were deleted on 2026-10-05 (see "Test accounts" in known issues).

## Visual design system (post-launch overhaul)

The owner found the UI generic (shadcn defaults, a stock mint-teal palette,
emoji icons, one centered column on every page) and asked for it to look like
a person with a point of view designed it. Process: audit first, one proposed
direction shown as a working specimen (an Artifact, "Graphite and
Highlighter"), approved, then built in six committed steps (foundation, shell,
landing/Today/auth, study pages, runners, social/settings/admin). The earlier
four-palette theme picker (Fresh Mint / Sunrise / Deep Study / Playground)
was **retired at the owner's request**: one identity reads as designed, four
interchangeable palettes read as a template.

**The idea**: the objects around an exam -- bubble sheets, ruled notebook
paper, a graphite pencil -- plus one accent, a highlighter yellow, that only
ever marks what you are working on (the picked answer, the current nav item,
today's streak). It is always a *background* behind ink text (`--mark` with
`--on-mark`), never a text color, never a glow. Light is the default; dark is
a user choice. Contrast: every text pair is >= 5.6:1 in both modes.

- **Tokens** (`src/app/globals.css`): the shadcn semantic names
  (`background`, `foreground`, `muted`, ...) are the contract the UI
  primitives are written against; design names are Tailwind aliases onto them
  (`bg-mark`, `text-on-mark`, `text-correct`, `text-incorrect`). `--background`
  is paper `#f7f8f6`, `--foreground` ink `#1f2328`, `--muted-foreground`
  graphite `#59606a`, `--mark` `#ffe24a`; `.dark` redefines all of them. Radius
  is 2px everywhere (paper has square corners), borders are 1px rules, no
  shadows. The `--nb-*` tokens drive the notebook-paper look (below).
- **Type** (loaded in `layout.tsx` with `next/font/google`): Archivo (variable,
  width axis) for display and UI, Source Serif 4 for everything read at length
  (stems, explanations, descriptions), IBM Plex Mono for labels and code.
  Roles are classes in `globals.css`: `.display` (800, 75% width), `.heading`,
  `.numeral` (tabular, for scores/levels/timers), `.eyebrow` (mono caps
  label), `.hl` (highlighter swipe), `.reading` (+ `.reading-sm`).
  **Bug this replaced**: `--font-sans: var(--font-sans)` pointed at itself, so
  `font-sans` resolved to nothing and the *entire app had rendered in the
  browser's default Times since launch*. next/font variable names
  (`--font-archivo`, ...) now differ from Tailwind's `--font-sans/serif/mono`
  on purpose -- never alias a variable to itself.
- **Layout components** (`src/components/ui/page.tsx`): `Page` (width and
  gutters), `PageHeader` (breadcrumb/kicker in a left margin column, display
  title, one sentence, actions), `Section` (mono label + optional note in the
  margin column, content on the right; stacks on phones), `RuledList`,
  `Breadcrumb`, `ActionRow`. Pages never hand-write container classes. The
  margin column is `10.5rem`, the page max width `67.5rem`.
- **Other shared pieces**: `Sheet` (the one boxed object; `lined` gives
  notebook paper), `Field`/`Input`/`Select`/`Textarea`/`Label`, `.check` (a
  square checkbox class), `Html` (renders `renderContentToHtml` output; `inline`
  flattens the block `<p>` for choice text), `Choice`/`ChoiceRow`/
  `ChoiceList`, `Bubbles` (unit mastery as ten bubbles), `XpBar`, `WeightBar`,
  `Tally` (streak as tally marks), `BadgeStamp` (drawn SVG badges),
  `Ledger` (leaderboards). `Button` hover is the highlighter on every variant.
- **Answer choices** (`ui/choice.tsx` + `.choice` in `globals.css`) are one
  component for quiz, boss battle, exam, exam review and admin: a native
  radio (so arrow keys and form semantics work) styled as a bubble-sheet row.
  Selected = highlighter row; revealed = `data-state="correct" | "wrong"`
  with an icon *and* a word ("Correct", "Your answer"), never color alone.
  Three gotchas, each found by testing in the browser: (1) the highlight
  rules are scoped to `[data-revealed="false"]` because `:has(> input:checked)`
  outranks a plain "revealed" reset and left the wrong pick yellow after
  submit; (2) `.choice .reading { color: inherit }` because on notebook
  paper in dark mode the sheet's light text color stayed on the yellow row and
  vanished; (3) `Choice` handles `onClick` as well as `onChange`, because a tap
  before hydration leaves the radio natively checked and a re-tap fires no
  change event.
- **Navigation**: `site-header.tsx` (wordmark, five links, streak + level, an
  `AccountMenu` holding Settings / dark mode / sound / log out) and a phone
  `TabBar` (Today, Courses, Progress, Friends, Classes) in place of the old
  hamburger. The inline nav shows from `lg` (1024px), and the tab bar stays
  through tablet widths: at 768px the inline nav plus status plus account
  name overflowed the page by ~100px, found only by measuring
  `scrollWidth` at each width, not by eye. The "Dashboard" route is labelled
  "Progress" in the UI; the URL is unchanged.
- **Theme** (`src/lib/theme/*`, `components/theme/*`): modes `light | dark |
  system`, default **light** (a new account never starts dark just because the
  device is). Zustand persist store (`mode`), a `beforeInteractive` inline
  script paints `.dark` before hydration (no flash), `ThemeSync` keeps `<html>`
  in step and follows the device in `system` mode. The same `hasHydrated`
  pattern and TDZ caveat as before apply (see `theme-store.ts`). The old
  `colorTheme` key in localStorage is ignored.
- **Landing page and Today screen** (both at `/`, chosen by session):
  signed out, `components/marketing/landing.tsx` -- a full-width headline,
  counts read from the database (never hard-coded), exam formats from each
  course's `examFormat` (`lib/content/exam-format.ts`), and a *working*
  sample question (a real Calc AB item copied into
  `lib/marketing/sample-question.ts`, local state only, nothing recorded).
  Signed in, `components/today/today-screen.tsx` -- daily challenge and due
  reviews per enrolled course, last unit, level; fed by `lib/study/today.ts`,
  which reuses the practice hub's own queries so the two never disagree. Login
  now lands on `/` (Today); signup still lands on `/courses`. `/login` and
  `/signup` redirect signed-in visitors to `/`.
- **Streak shown is the live value**: `getUserGamificationStats` now returns
  `displayStreak()` (`lib/gamification/streak.ts`), not the stored
  `currentStreak`. The stored value only changes on the next activity, so after
  a long gap it still held the old run and the header claimed a streak the
  next answer would reset. Same gap rules as `updateStreakOnActivity` (one
  missed day counts only while a freeze is left). Unit-tested.
- **Exam runner additions** (new behavior, not just restyling): a question
  grid in the margin (jump anywhere, answered ones filled), a sticky clock on
  phones, hours in the clock (`3:09:59`, not `189:59`), and a two-step submit
  that states how many questions are unanswered -- before, one stray tap on
  "Submit exam" ended the exam.
- **Badges**: `BadgeStamp` draws all six by slug. The emoji in
  `BADGE_DEFINITIONS[].icon` / the `Badge.icon` column are no longer displayed
  anywhere (left in place to avoid a migration/reseed).
- **Metadata**: title template `%s · AP Study App`, per-page titles, a
  description, Open Graph + Twitter card, theme-color, `metadataBase`
  (override with `NEXT_PUBLIC_SITE_URL`), and `icon.tsx` / `apple-icon.tsx` /
  `opengraph-image.tsx` / `manifest.ts` generated in code with `next/og` (the
  OG image uses ImageResponse's default font). The default Next favicon and
  the five scaffold SVGs in `public/` were removed. `error.tsx`,
  `global-error.tsx` (inline styles only, since it replaces the root layout)
  and `not-found.tsx` share the same voice. The loading skeleton is
  `PageSkeleton` (`components/ui/page-skeleton.tsx`), re-exported by a
  `loading.tsx` in each section (`courses`, `dashboard`, `friends`, `classes`,
  `settings`, `admin`, `teacher`). **There is deliberately no
  `app/loading.tsx`** -- see "Landing page renders finished HTML" below.
- **Footer** (`site-footer.tsx`): trademark and non-affiliation notice
  (confirmed by the owner), plus "may contain mistakes" (still true and protective: the
  questions are practice material not reviewed by College Board, and the owner's review in
  `/admin/review` is a person's check, not a guarantee), a "Report a mistake or send
  a suggestion" mail link, and a Privacy link. See "Footer, contact and privacy".
- **Copy rules**: plain, concrete, no em dashes, no invented numbers. Counts
  come from the database; the only hard-coded figures are the XP ranges and
  exam formats, which come from `xp.ts` and `examFormat`. Spaced repetition is
  described accurately: every answered question returns on a schedule (a miss
  is due in a day), not only missed ones.
- **Verification habit for UI work here**: test the real flows signed in
  (answer, reveal, reward, exam, results), at 320 / 375 / 768 / 1024 / 1440,
  in light and dark, and *measure* overflow (`scrollWidth > innerWidth`)
  instead of eyeballing it. Four of this overhaul's bugs (the dark-mode
  highlighted-row text, the stuck yellow after reveal, the pre-hydration tap,
  the 768px header overflow) were invisible in a first screenshot.

### "Paper-lined" question cards for Calc AB / Physics 1

A ruled-notebook-paper background for question cards, requested by the
owner specifically for the two math-heavy courses -- shown as a live
preview on a real Calc AB question first (not a mockup, since this reskins
an existing component rather than proposing a new one), iterated once on
feedback (the margin line originally overlapped the question text -- fixed
by moving the line into the card's own padding and giving the actual
content real left inset, ~24px of daylight between the line and anything
written), then approved and wired in everywhere.

- **The look**: `.paper-lined` in `globals.css` -- cream background, blue
  horizontal rule lines, a red margin line (a muted rust tone in dark mode,
  on a dark "chalkboard-ledger" background), all plain CSS gradients, no
  images, driven by the `--nb-*` tokens. Unlayered (like the existing `pre`
  rule) so it wins over Tailwind's `bg-card` utility by cascade-layer
  priority, not specificity. After the design overhaul it is the one warm
  object on a cool page -- the notebook the student works in -- and is applied
  through `<Sheet lined>`.
- **Scope**: `isPaperLinedCourse()` (`src/lib/content/paper-lined.ts`, a
  pure function checking `courseSlug` against `["ap-calc",
  "ap-physics-1"]`) -- AP CSA and AP World History stay on the plain card
  background. Computed once per page (every call site is already under
  `/courses/[courseSlug]/...` or `/admin/review/[courseSlug]/...`, so
  `courseSlug` is always available) and threaded in as either a
  `paperLined` prop or, for `BossBattleRunner`/`ExamRunner` (which already
  received `courseSlug` as a prop), computed internally.
- **Wired into every question-rendering surface**, matching how the
  diagram feature (Milestone 7) was wired in rather than just the one
  component the owner happened to test: `QuizRunner` (unit/custom/
  weak-spot/daily quizzes), `BossBattleRunner`, `ExamRunner`,
  `ExamMcqReview` (exam results' MCQ section), `FrqSelfGrade` (standalone
  FRQ practice and exam results), and `/admin/review`'s question/FRQ
  cards. Non-question cards (quiz "done" screen, boss battle result
  screen, exam's empty state) deliberately stay plain -- the ask was for
  question cards, not every surface in these components.
- **Gotcha if you touch `FrqSelfGrade` again**: it has no sheet of its own
  by default and is used two different ways -- standalone FRQ practice
  renders it as a sibling *after* its own separately-boxed prompt, while the
  exam results page nests it *inside* the same `<Sheet>` as the prompt. Its
  `paperLined` prop only self-wraps (in `<Sheet lined>`) for the standalone
  case; the exam results page instead paper-lines the shared outer `Sheet`
  and leaves `FrqSelfGrade`'s own prop at its `false` default. Passing `paperLined` to `FrqSelfGrade` in the
  exam-results nested case would paint the ruled-line pattern twice,
  independently, from two different coordinate origins -- the join between
  the prompt area and the self-grade area would show a visible seam where
  the lines don't align. Decide per call site which one owns the
  background, never both.

### Bug fix: MCQ answer choices never rendered LaTeX/markdown

*(Since the design overhaul, every render site below shares `ui/choice.tsx`;
the data-path notes still apply.)*

Spotted live while smoke-testing the paper-lined cards on a Calc AB exam
question: choices showed raw `$\lim_{h \to 0} \dfrac{f(a+h) - f(a)}{h}$`
instead of typeset math. Root cause: `stem`/`explanation`/FRQ `prompt`/
`sampleResponse` always went through `renderContentToHtml` (the Shiki/KaTeX
pipeline), but choice `text` never did, in either data path -- silently
inconsistent since launch, not something the paper-lined work introduced.

- **`src/lib/study/render-quiz.ts`** (feeds `QuizRunner`, `BossBattleRunner`,
  and `ExamMcqReview`, which all share the `RenderedQuestion`/`RenderedChoice`
  types from `quiz-runner.tsx`) and **the exam-attempt start page**
  (`courses/[courseSlug]/exam/[examAttemptId]/page.tsx`, which builds
  `ExamMcqItem` independently -- it reads straight from the DB, not through
  `renderQuizQuestions`) both now render `c.text` through
  `renderContentToHtml`. `RenderedChoice.text` / `ExamMcqItem.choices[].text`
  renamed to `textHtml` everywhere to match the `stemHtml`/`explanationHtml`
  convention and make "this is pre-rendered HTML" explicit at the type level.
- Also fixed in `/admin/review` (same bug, separate code path -- raw DB rows
  with plain `{choice.text}` for choices). Pre-renders each unit's questions' choices via `Promise.all`
  before the JSX return, same pattern the exam-results page already used for
  FRQ sections.
- **Rendering gotcha**: `renderContentToHtml`'s output is always wrapped in a
  block-level `<p>` (remark-rehype's default for any paragraph, even a
  one-line string), but choice text needs to sit inline next to the "A."
  label on one line. Fixed with a `[&_p]:m-0 [&_p]:inline` Tailwind arbitrary
  variant on the wrapping span rather than restructuring to a two-line
  layout -- keeps the existing compact look. Watch for this if choice text
  content ever needs block math (`$$...$$`) or a code fence; neither appears
  in any authored content today, so it wasn't specifically handled.
- **Caught while fixing, not initially**: the first pass separated the "A."
  label and the rendered-HTML span into two flex children for layout, which
  silently dropped the implicit space JSX had been inserting between them
  (`<span>A.</span> {text}` -- that's a real space text node). Choice
  `textContent` read as `"A.5"` instead of `"A. 5"`, confirmed via direct DOM
  inspection (not the screenshot, which looked identical either way) --
  harmless visually but a real degradation for screen readers. Fixed with an
  explicit `{" "}` between the two spans in all five render sites.

**Follow-up: "typewriter math" outside `$...$`** (the owner pushed back that
the choices still weren't *readable*, not just rendered). Piping choices
through KaTeX only fixes content that was authored with `$...$`. A full
audit of every authored string (10,726 across all four courses) found a
second, much larger class that was never wrapped in math delimiters at all:
`m/s^2` in 60 Physics answer choices, and `x^3`, `e^(2x)`, `F_net`,
`sqrt(...)`, `->` throughout the explanations, FRQ samples, and so on.
Markdown showed all of that literally.

- **`src/lib/content/plain-math.ts`** -- `normalizePlainMath(markdown,
  { mathCourse })`, pure and unit-tested (`tests/plain-math.test.ts`), run
  inside `renderContentToHtml` before the markdown pipeline, so it applies
  to every field (stem, explanation, choices, choice explanations, FRQ
  prompt/sample) with no per-call-site work and **no database change**. It
  only rewrites text outside `$...$`, `$$...$$`, inline code, and fenced
  code, so it's idempotent and safe on already-correct content. Digit
  exponents become plain unicode superscripts (`x^2` -> `x²`, `m/s^2` ->
  `m/s²`) -- matching what much of the content already hand-wrote and
  staying in the body font; everything needing real typesetting (`e^(2x)`,
  `F_net`, `sqrt(...)`, `lim_{x->3}`, `->`) is wrapped in `$...$` for KaTeX.
- **Only the digit-exponent rule runs for AP CSA / World History.** The rest
  is gated on `isMathCourse()` (`src/lib/content/math-courses.ts`, also what
  `isPaperLinedCourse` now delegates to -- one list, not two) because in
  CSA an underscore is an identifier (`total_score`) and `->` is code
  (`myDog->bark()`), not math. `renderContentToHtml` therefore now takes an
  optional `courseSlug`; every call site passes it.
- **Verified by rendering everything, not by sampling**: all 10,726 strings
  through the converter + KaTeX -- 311 rewritten, 0 KaTeX errors, 0 raw
  notation left in the math courses' pipeline fields. The first pass left 12
  (subscripts attached to a coefficient like `5v_f`, long subscripts like
  `KE_before`, a `lim_{x->3^-}`), caught only because the audit re-checked
  its own output instead of stopping at "no errors".
- **Choice-only: `renderChoiceTextToHtml`** also turns a literal `\n` into a
  line break, since AP CSA writes multi-line program output as `A\nB` (19
  choices) -- shown as the separate lines a student would see printed.
- **Seven authored strings fixed in the content JSON instead** -- six Calc
  choices that were plain text next to typeset siblings (e.g. `f(a)/a`
  beside three `$\lim...$` choices; a render-time heuristic for those would
  also mangle Physics unit choices like `20 m/s`) and one rubric line with a
  bare `\sqrt{3}` and no `$`. **Content is read from the database, so these
  7 only show up after a reseed** (`npm run content:seed`); everything else
  in this section is render-time and needs no reseed.
- **FRQ rubric lines now go through the same pipeline.** They were plain
  React text (`{line.description}`), so ~66 Calc/Physics lines showed `x^2`
  literally. `renderRubric()` (`src/lib/study/render-rubric.ts`) pre-renders
  each line server-side -- same reason as `renderQuizQuestions`, a Client
  Component can't run Shiki -- and `RubricLineView` gained `descriptionHtml`
  (`description` stays as the plain text). Used by `FrqSelfGrade` (practice
  and exam results) and the admin review list.
- **Bug found while doing that, and it was already live: bare `*` was being
  eaten as markdown italics.** Authors write multiplication as `4*pi*r^2 *
  dr/dt`; markdown pairs the asterisks into emphasis, drops them, and
  italicizes `pi` -- in 32 existing explanations, before rubrics were
  involved at all. Routing rubrics through markdown would have added more.
  `fixAsterisks()` in `plain-math.ts` converts a bare `*` to `·` in the math
  courses and escapes it (`\*`) elsewhere (AP CSA, where `*` is Java's
  operator). **A passage's `*Source: ...*` attribution line is preserved too** (found 2026-10-06 while testing
  AP U.S. History in the browser: it printed with literal asterisks under every History passage, World
  History's hard set included, because non-math courses escape asterisks). Separately, the typography
  plugin wrapped every blockquote in typographic quotes, doubling the opening mark of our own curly quotes
  and putting a closing one after the Source line; `globals.css` now turns that off for `.reading.prose
  blockquote`. Both are render-time fixes, no reseed. **Intentional `**bold**` is preserved** -- confirmed by audit
  that no content anywhere uses single-asterisk italics, only 247 bold
  spans, and that count is identical before and after.
- Final full-content audit (11,135 strings incl. rubrics, every course):
  426 rewritten, 0 KaTeX errors, 0 raw notation left in the math courses,
  accidental italics 32 -> 0, bold 247 -> 247. When changing
  `plain-math.ts`, re-run an audit like that (render everything, count
  `<strong>`/`<em>`/`katex-error`, re-scan the *output* for leftovers) --
  unit tests alone missed the asterisk bug entirely, and a first-pass
  audit that only counted errors missed 12 leftovers.

## Post-launch growth features (Cram Mode, mastery, titles, waitlist, /teacher)

Built from a product-feedback brief, one local commit per phase. Where the
brief didn't match the code, the code won: the landing page was already
server-rendered, mastery bars and a Boss Slayer badge already existed, and the
app uses Server Actions everywhere, so the waitlist is one too, not an API route.

### Landing page renders finished HTML

A crawler or link preview that doesn't run JavaScript was seeing "Loading"
(`aria-busy`) on `/`. Cause: a root `app/loading.tsx` wraps every page in
`<Suspense>`, and `/` reads the session so it renders per request: the
skeleton streamed first and the real page arrived later in a hidden block that
JS swaps in (`<h1>` at byte ~51.5k, behind the skeleton at ~6.7k). Fix: no
root `loading.tsx`; each section has its own; `/` shows the landing page
unwrapped and only the signed-in Today screen sits in its own `<Suspense>`.
Verified on a production build (`<h1>` at ~6.7k, no `aria-busy`, no hidden
swap blocks). A fully *static* `/` isn't possible while the header and the home
page read the session; don't spend time on that without a different design.
**Don't add `app/loading.tsx` back.** One side effect worth knowing: under a
`loading.tsx`, a `notFound()` thrown in the page returns status 200 (the
status is already sent) with the not-found UI and a noindex meta, e.g.
`/teacher` for a non-owner and `/admin/review` for a non-admin. The page
content is not exposed.

### Waitlist, "Coming soon", testimonials

- `components/marketing/{coming-soon,waitlist-form,testimonials}.tsx`,
  `lib/marketing/{actions,waitlist,testimonials}.ts`. `joinWaitlist` is a
  Server Action: zod validates (trim + lowercase + max 254), a hidden
  `website` honeypot field answers like a success, `createMany({ skipDuplicates })`
  (ON CONFLICT DO NOTHING) so an existing address gets the same answer as a new
  one, and failures log only the error *code*, never the email.
- No rate limiting beyond that (no Redis here). If the table gets spammed, add
  a Vercel Firewall rate-limit rule on `POST /`.
- The waitlist collects emails and there is no age gate: see the COPPA note in
  the Social section before promoting this to under-13s.
- The "Coming soon" section (`ComingSoon`) is shown in two places: the bottom of
  the signed-out landing page and the bottom of the signed-in Today screen (both
  its first-course picker and its main view), so its copy must not refer to
  anything else on the page. Subjects listed in it are the owner's examples (AP Biology, AP Calculus BC),
  marked "Planned", no dates. AP U.S. History was on the list until it shipped. The copy states no
  count of exams (the component has no data of its own); the landing page and the courses page
  headline derive "five exams" from the course list (`countWord`, `lib/count-word.ts`).
- **Testimonials are real quotes only.** `lib/marketing/testimonials.ts` renders
  nothing while empty. It started empty, and now holds one quote the owner
  supplied (Phu Vo, 2026-10-04, verbatim, no course or score because none was
  given). Add more only with the student's (and a parent's, if under 18)
  permission, worded as they wrote them, and never add an AP score or course
  the student didn't state. No invented testimonials: nobody had scored anything
  with this app, and fabricated ones are deceptive (and the FTC's 2024 rule
  covers them). `tests/testimonials.test.tsx` checks shape, and that this quote
  has no invented score or course.

### Cram Mode

Toggle on the Progress page. While on, "review" ignores spaced-repetition due
dates and serves, per course, the student's most-missed questions (most misses
first, then worst miss rate), then questions never seen, then the rest, 20 at a
time (`lib/study/cram.ts`, pure and tested; ties are shuffled).

- One function decides what review means everywhere: `getReviewQueueIds`
  (`lib/study/queries.ts`), used by the weak-spot page, the practice hub and the
  Today screen, so their counts can't disagree. Today's count in cram mode is the
  cram queue's length.
- State is an **HTTP-only cookie** (`ap-cram`), not a column: no migration, and
  "temporary" is literal (it lapses after 7 days). Its value is the **user id**,
  so on a shared device a second student doesn't inherit the first's cram mode.
  `isCramModeOn(userId)` reads it; `setCramMode` (Server Action) writes it.
- Cram attempts still use `source: WEAK_SPOT` and update spaced-repetition state
  normally, so turning cram off leaves nothing inconsistent.

### Unit mastery

`rateUnitMastery` (`lib/study/mastery.ts`): **Proficient = at least 80% correct
on what you've tried AND at least half the unit tried**, compared on the rounded
percentages shown (a unit never reads "80%" and yet isn't proficient). Below that
it's Building; no attempts is Not started. The thresholds are exported constants:
tune them there. `UnitMasteryList` draws a two-stroke bar (light = tried, dark =
currently correct, both as a share of the whole unit) so 100% on two questions
no longer looks like mastery. Bars, not donut charts, to match the design system.

### Boss battle titles

Defeating a unit's boss battle earns "Unit N Conqueror" (N = `Unit.order`).
**Titles aren't stored**: they're derived from `BossBattleAttempt.passed`, which
already persists and never reverts, so there's no table and no migration
(`lib/gamification/titles.ts`, `getUserUnitTitles`). Shown on Progress, grouped
by course, with a `TitleStamp` (the unit number on the highlighter), and
announced once, the first time a unit is conquered, via `RewardToast` and a
"New title" line on the result screen (`submitBossBattle` returns `newTitle`).

**Bug fixed with it**: the boss result screen returned early and never rendered
`RewardToast`, so anything awarded at submission time (Boss Slayer included)
was never shown. It's rendered on the result screen now.

### /teacher (skeleton)

`/teacher` is gated to **anyone who owns a class** (`requireOwnedClasses`;
everyone else gets `notFound()`). There is **no teacher role**: classes are open
to every student, so "owns a class" is the only distinction that exists. Before
real student data goes in here, replace this with an explicit role. It's
reached from the "Teacher view" button on a class page you own, not the nav.
The "Class-wide weaknesses" panel takes `ClassWeakness[]` and shows an honest
empty state (no invented numbers) until an aggregation exists; "Assign Daily 5
set" is a disabled button that says it isn't built. FERPA/COPPA considerations
(see the Social section) apply the moment per-student data appears here.

### Applying migrations here

`npm run db:migrate` is `prisma migrate dev` (needs a shadow database, awkward on
Neon). What worked: generate the SQL offline with
`npx prisma migrate diff --config prisma7.config.ts --from-schema <old schema from git> --to-schema prisma/schema.prisma --script`,
save it as `prisma/migrations/<timestamp>_<name>/migration.sql`, review it, then
`npx prisma migrate deploy --config prisma7.config.ts` (applies only pending
migrations; never resets). Vercel does **not** run migrations on deploy, so
apply a migration *before* pushing code that needs it.

Order for a change that adds a column *and* needs content re-seeded (the `FRQPrompt.type` change
was one): migrate, then `npm run content:seed`, then push. The new column has a default, so the
old code keeps working in between; the new code must never see rows the seed hasn't typed yet.

## Answer choices are shuffled on every showing

Every time a question is shown, in every course and every mode (practice quiz,
custom, weak-spot, daily, boss battle, exam, exam review, the landing page's
sample), its choices are shuffled and re-lettered A, B, C, D (E). Reload, retry,
or see it again later and the order is different. Added because the authored
content put the right answer in slot A for ~99% of Calculus and 100% of Physics
questions, so always picking A would have scored almost perfectly.

- **Identity vs display.** A choice keeps its authored `label` as its identity:
  it's the radio's value, what the runners send as `chosenLabel`, what is stored
  on `QuestionAttempt.chosenLabel`, and what the server grades against
  `Choice.label` (so `recordAttempt`, `submitExamAttempt`, spaced repetition,
  mastery and the exam results lookup are all unchanged). Only the *order* and
  `displayLabel` (the letter drawn for the slot) change. `Choice`/`ChoiceRow`
  take `label` and `displayLabel`; **never use `displayLabel` for logic**.
- **Where it happens.** Server-side, per request, in `renderQuizQuestions`
  (`lib/study/render-quiz.ts`: quiz, boss, exam review), the exam attempt page,
  and the landing page. Not in a client component: a client-side random shuffle
  would differ between server render and hydration. `shuffleChoices` is a
  uniform Fisher-Yates (`lib/study/shuffle-choices.ts`); it can return the
  authored order by chance (1 in 24), on purpose, since forcing a change would
  bias it. A page re-render on the server (a manual refresh) reshuffles, which is
  the intended "every time".
- **Letters inside text.** One authored string points at a choice by letter
  ("even fewer than option A", `ap-csa-u4-mcq-30`). `remapChoiceLetters`
  rewrites "choice/option/answer/response/statement/letter X" to the letter now
  on screen, in the stem, explanations and choice text. It deliberately ignores a
  bare "A" or "(a)", which in this content is math or code (`f(a)`,
  `a.equals(b)`). `tests/choice-letters-audit.test.ts` reads all of `/content`
  and fails if any text uses another way of pointing at a choice ("(B)", "both A
  and B", "all of the above"), or a letter the question doesn't have. **When
  authoring: don't refer to choices by letter** (or use "option X"), and don't
  write "all/none of the above" (it would break under shuffling; no existing
  question has one).
- Tests: `tests/shuffle-choices.test.ts` (permutation, even spread of the correct
  answer across slots, remap rules), `tests/render-quiz-shuffle.test.ts` (label,
  correctness and text stay together; the right answer reaches every slot),
  `tests/choice.test.tsx` (shown letter vs submitted label).

## Boss battle scoring is server-side

`submitBossBattle` used to take `{ unitId, correctCount, total }` from the
browser, so a crafted request could claim a perfect score and win the battle
(`passed`, `bestScore`, the Boss Slayer badge and the unit title all followed
from those two numbers). Now it takes only a **signed battle token** and counts
the result itself:

1. When the boss page renders, `startBossBattle(userId, unitId)`
   (`lib/study/boss-battle-token.ts`) returns an HMAC-signed token holding the
   user, the unit and the start time. The secret is `AUTH_SECRET`, domain-separated
   (`boss-battle:v1:`) from Auth.js's use of it. Tokens expire after 4 hours.
   The page therefore **needs `AUTH_SECRET` at runtime** (it is set in Vercel and
   in `.env.local`); without it the boss page throws.
2. Each answer is already graded server-side by `recordAttempt`. On submit the
   server verifies the token (and that it belongs to the signed-in user), takes
   the unit's questions from the database, and counts those whose *latest*
   attempt **at or after the start time** is correct (`scoreBossBattle`,
   `lib/study/boss-battle-rules.ts`, pure). Earlier practice doesn't count, an
   unanswered question counts as not correct, and nothing the client says about
   its own score is read. `total` is the unit's question count.
3. The result screen shows the *server's* `correctCount` / `total`. A bad or
   expired token returns `{ status: "invalid" | "expired" }` and the runner offers
   "Start a new battle"; the answers were still saved as ordinary practice.

The runner keeps the token in `useState` so a re-render with a newer token can't
move the start time mid-battle. The pass threshold is integer math
(`hasPassedBossBattle`), not `correct / total >= 0.7`.

**What this does not fix**: a student can still read the correct answers out of
the page payload (see "The correct answer is in the page payload" in known
issues) and answer correctly through the real action. That costs answering every
question, and each answer is graded and recorded; it is a different, larger
problem than forging a score.

Tests: `tests/boss-battle.test.ts` (rule, scoring, token tampering/expiry/skew) and
`tests/submit-boss-battle.test.ts` (the action with a faked DB: the old
`{ correctCount: 30, total: 30 }` forgery scores 0, other users' tokens and
answers are refused, a conquered unit stays conquered).

## Exam resume, daily challenge, reporting problems (review follow-ups)

From a parent's-eye review of the app (2026-10-05).

- **Exam clock and saved answers.** The clock is derived from the attempt's own
  `ExamAttempt.startedAt` (`lib/study/exam-clock.ts`), computed on the server and passed
  as `initialSecondsLeft`; no migration was needed (the column already existed, and the
  old note saying it didn't was wrong). The client counts down against a fixed
  wall-clock deadline, so a throttled tab can't drift. A reload therefore resumes the real
  clock. Answers and the current question are saved **on the student's device**
  (`lib/study/exam-draft.ts`, localStorage `ap-study-app:exam-draft:<attempt>`, never sent
  to the server until submit), keyed by the choice's *authored label*, so the right bubble
  is refilled even though choices reshuffle on reload. Drafts are validated on read
  (only this exam's questions, sane values), expire after a day, stale ones are purged,
  and the results page clears the submitted one. The runner shows a "Welcome back" note
  when it restored something. The privacy page says answers are kept on the device.
- **Fixed in passing, serious:** the auto-submit when the clock hit zero ran from an
  interval created once at mount, whose `handleSubmit` had closed over the *initial empty*
  answers, so **a timed-out exam was submitted with no answers at all**. The interval now
  calls a ref that is refreshed every render. `tests/exam-runner.test.tsx` pins it (and
  fails against the old code), including under StrictMode, which runs effects twice and
  is what makes the "don't save before restoring" guard necessary.
- A reload while the clock is at zero submits whatever was saved. An exam left open for
  days therefore submits itself when reopened; that follows the clock, not a bug.
- **Daily challenge** goes straight into the questions (`/daily` redirects when there is a
  set to start) instead of showing a "5 questions" page that asked for a second click. It
  still renders for "done today" and "no questions".
- **Per-question "Report a problem"** (`ReportProblem`, `reportMailto` in `lib/site-contact.ts`):
  a mail link whose subject and body carry the question or prompt id, shown after answering
  a question, in the exam review, and on the FRQ page. Like the footer link it never prints
  the owner's address.
- **"Only usernames are shown... no chat and no messaging"** (`lib/social/copy.ts`) is
  stated on the Friends and Classes pages. Keep it true: if chat or any messaging is ever
  added, change that sentence first.

## Progress over time, exam breakdown, About page (review follow-ups, part 2)

- **Progress** gets "Last 7 days" (days studied, questions answered, % correct, time
  answering, 7 bars) and "Weakest topics" (latest answer per question, at least 3 questions
  tried, under the 80% proficiency line, with a Practice link). No database change. The week
  is bucketed **in the browser** (`WeekActivity`, `lib/study/week-activity.ts`) because "today"
  is the student's local day, not the server's; the server sends raw timestamps for eight days.
  Time = seconds spent choosing answers (each capped at 10 min) plus completed exams' length
  (capped at 4 h); reading explanations isn't measured, and the page says so.
- **Exam results** gets "Where you lost points": units ranked by questions missed or skipped,
  each with a quiz (max 20) of exactly those questions (`lib/study/exam-breakdown.ts`).
- **/about** ("About and FAQ", linked from the footer): one-person, no name, and **no pricing**
  (owner's choices, 2026-10-05). It states the questions were written with AI help and, for
  math/physics, calculated answers were checked with software. The "checked by a person" count
  is read from the `reviewed` flags, so it stays true on its own. **Owner: confirm you are happy
  with the AI-disclosure sentence.**
- Not done from the review (needs decisions or something other than code): exam date and study
  plan (small migration), read-only parent link (new table), self-serve change password / delete
  account, forgot password and parent email (need an email service), real teacher review,
  testimonials, a real `/teacher` role, refresher videos (refresher *notes* are built, see "Topic refreshers"), an AI check for free-response answers.
- Verified signed in end to end on 2026-10-05 with a scratch account (deleted afterwards): exam
  resume after reload, auto-submit at zero carrying the saved answers, the Progress sections,
  and the exam breakdown link. The About page and part-2 components have unit tests and were
  checked in the browser; no full `next build` was run after part 2 (run it before deploying).

## Exam date and study plan

Each student can set an exam date per course; the app counts down and paces them.

- **Data**: `Enrollment.examDate DateTime? @db.Date`, a calendar date with no time, so no
  timezone can shift it. Migration `20261005200000_add_enrollment_exam_date` adds one
  nullable column (`ALTER TABLE "Enrollment" ADD COLUMN "examDate" DATE`). **Apply it before
  deploying code that reads it** (the old code is unaffected by the extra column).
- **Where**: a form + countdown on the course page (`#exam-date`, enrolled students only) and a
  countdown per course on the Today screen. `setExamDate` (Server Action) updates only the
  signed-in student's own enrollment (keyed on the session, never on form fields), validates
  server-side (real date; not in the past, tolerating the server being a timezone behind;
  within ~2 years), and can clear the date. Past dates are refused, but a stored date can still
  pass later, and the UI then says so.
- **The plan** (`lib/study/exam-plan.ts`, pure and tested): days left = exam date minus the
  viewer's *local* date (UTC calendar arithmetic, so DST/timezones can't skew it); today counts
  as a study day, the exam day doesn't. New questions per day = untried / days left, rounded up;
  minutes = that x `PLAN_SECONDS_PER_QUESTION` (90 s, answering plus reading the explanation;
  an assumption, tune it there). Pace compares the last 7 days' *first-time* questions per day
  (`getCourseCoverage`) with what's needed: "on pace" / "behind", and "not started" is
  encouraged rather than judged. In the last 14 days it points at Cram Mode.
- Worked out **in the browser** (`ExamCountdown`), because only the browser knows the student's
  date; the server renders the date and a placeholder.
- The exam date is stored personal data, so the privacy page lists it.
- The AP exam dates themselves are **not** looked up or stored: the student enters their own
  (their school or the College Board's schedule has it).

## Settings: change password and delete account

Both live on `/settings` (`ChangePasswordForm`, `DeleteAccountForm`), backed by
`lib/auth/account-actions.ts`.

- Both act only on the **session's own account** (never on a form field) and both **re-ask
  for the password**, so a session left open on a shared computer isn't enough to lock
  someone out or erase them. Neither returns any password to the browser (tested), so the
  fields always come back empty.
- **Change password**: current + new + confirm; the new one is held to the signup rules
  (min 8, and now **at most 72 bytes**, since bcrypt silently ignores anything past that;
  `lib/auth/password.ts` is the single source, applied to signup too), must differ from
  the current one, and is hashed with bcrypt (12 rounds).
- **Delete account**: needs the password and a confirmation tick (checked server-side).
  One transaction deletes the user, which removes everything tied to it through the schema's
  cascades (answers, spaced repetition, XP, badges, boss results, exams, free-response work,
  friendships, memberships, **and any class they own**), plus the `WaitlistSignup` row with
  the same email (it isn't tied to a user). Then `signOut` redirects to `/account-deleted`.
- **Owned classes are deleted for everyone in them.** Classes can't be handed over, and an
  owner can't leave one, so blocking would trap the owner. The form names each owned class
  and how many other students it affects before they confirm. If class ownership transfer
  or a delete-class feature is ever built, revisit this.
- **Sign-in tokens die with the password.** Sessions are stateless JWTs, so on their own
  they stayed valid on other devices after a password change (and after the account was
  deleted). Now each token carries a **stamp**, a fingerprint of the account's password hash
  (`lib/auth/credentials-stamp.ts`), and the `jwt` callback in `lib/auth/config.ts` compares
  it with the database on every session read: a different stamp, or no such account, returns
  `null`, which signs the token out and clears its cookie. **No migration**: bcrypt re-salts
  every hash, so even re-saving the same password retires old tokens. Costs one primary-key
  read per `auth()` call (deduped within a request by `cache()`, keyed by user *and* stamp so a
  change inside one request isn't answered from before it).
  - **The device that changed the password signs itself in again from the browser**
    (`ChangePasswordForm` calls `next-auth/react`'s `signIn` with the new password it still
    holds; the action returns `signInAs` = the email). **Don't move that into the Server
    Action**: setting a cookie there makes Next re-render the page in the same request from the
    *old* cookie header, which redirected the student to /login (found by testing in the browser).
  - **The `jwt` callback ignores `trigger: "update"` on purpose.** A client can post that to
    `/api/auth/session` itself, so letting it refresh the stamp would let a stale token revive
    itself. Don't use `unstable_update` for this.
  - Tokens issued before this shipped have no stamp; they are accepted and stamped on first
    use (so nobody was signed out by the deploy). A device signed in *before* the deploy is
    therefore only covered once its token has been refreshed.
  - A database error while checking keeps the person signed in (logged by error name only)
    instead of signing everyone out; the pages that need the database fail on their own.
- **Limits, known**: there is no rate limit on password *attempts* (the form re-checks the
  current password with bcrypt's ~250 ms cost as the only brake; a Vercel Firewall rule on
  login/reset requests would add the per-IP limit the app can't do without Redis). A password change
  sends a notice email once email is configured (see "Forgot password and email"); deleting an
  account sends none.
- The privacy page says deletion and password change are in Settings; it also still
  promises access/correction and waitlist removal without an account by request.

## Topic refreshers

A short written read on each topic, for a student who just missed a question or is starting a unit. Built
2026-10-06 (owner's request: "let's do the concept refreshers"). **All five courses are written and live: Calc AB (35
topics), CSA (39), Physics 1 (32), U.S. History (46) and World History (43), 195 refreshers in all.** The owner dismissed the scoping questions, so these defaults were chosen and stated:
one course first, the same review as questions, a page per topic.

- **Data**: `Topic.refresher String? @db.Text` and `Topic.refresherReviewed Boolean @default(false)`,
  migration `20261006200000_add_topic_refresher` (two columns, additive). **Apply it before deploying code
  that reads Topic**: Prisma selects every column, so with the new client against an un-migrated database
  every Topic query fails, including the seed's. Order: migrate, seed, push.
- **Content**: `content/<course>/refreshers/unit-N.json`, an array of `{ unit, topic, body, reviewed }`
  (`RefresherSchema`). `validateRefresher` (`lib/content/validate.ts`): the topic exists, 400 to 3,500
  characters, no `#`/`##` headings (the page title is the topic name; use `###`), no markdown table (the
  renderer has no GFM, so a table prints as pipes), balanced `$` and code fences. A course may have some
  topics without one (the validate script says so); a topic without one keeps the old "Review this
  concept" behavior.
- **Layout of a refresher** (a convention, not enforced): `### The idea`, `### Key facts`,
  `### Watch out for`, `### Worked example`. About 1,000 to 1,700 characters; math in `$...$`.
- **Seed** (`scripts/seed.ts`): writes `refresher` and `refresherReviewed` per topic through
  `nextRefresherState` (`lib/content/review-state.ts`, pure and tested), the same rule as questions: an
  approval stays while the text is exactly what was approved and resets when it changes, and a topic whose
  file entry is gone has its refresher cleared. The summary line prints `N refreshers (approvals kept: x,
  reset because the text changed: y)`.
- **Where students meet it**: the topic page (`app/courses/[courseSlug]/units/[unitSlug]/topics/[topicSlug]`)
  shows the refresher, a "Practice this topic" button (a quiz of up to 10 of the topic's questions through the
  generic `/courses/<c>/quiz` route, with the back link pointing at the refresher), the student's own tally
  for the topic, previous/next topic, a "Report a problem with this refresher" mail link (`reportMailto`
  gained a `refresher` kind, id `<course>/<unit>/<topic>`), and, while unreviewed, a line saying it has not
  been checked by a person. A topic with no refresher redirects to the unit page's topic filter. Links in:
  every question's "Review this concept" (`topicHref` in `lib/study/concept-link.ts`, which decides between
  the two destinations; `renderQuizQuestions` asks `getTopicKeysWithRefreshers` once per render), a
  "Refreshers" section on the unit page, and a "Refresher" link beside "Practice" in Progress's Weakest topics.
- **Review**: `/admin/review` lists each unit's unreviewed refreshers (rendered, with Approve) above its
  questions; "Approve all" and the pending counts include them (`approveUnitContent` gained an optional
  fourth argument, the topic ids; `markRefresherReviewed` approves one). The About page counts refreshers
  with the questions in "N of M have been checked by a person" and says they were written with AI help.
- **Live 2026-10-06.** Migration applied, Calc AB seeded (35 refreshers, all unreviewed; the 400 Calc
  questions/prompts kept their approvals), then pushed. Checked in the browser with a scratch account: the
  topic page (desktop and 375px, no overflow, no KaTeX errors), Practice this topic, "Review this concept" from
  a missed question, the unit page's Refreshers list, Progress's "Refresher" link, a topic without a refresher
  (redirects to the unit's question list), the admin review pages and the About count (2,216 of 2,251, the 35
  refreshers in the total). Equations written `$$...$$` on one line render inline, so the authoring helper
  expands them to display blocks (`$$` on their own lines).
- **Authoring** (CSA): `scripts/content-authoring/ap-csa-refreshers/u1.py..u10.py`. Every Java example goes
  through `code(...)`, which returns the fenced block and records the full program with the output the text
  claims; `finish()` writes the JSON and, **when a JDK is available** (`JAVA_HOME`, or a Temurin JDK unpacked in
  the session scratch folder), compiles and runs every recorded program and fails if the real output differs.
  **All 44 CSA examples were compiled and run with Temurin JDK 21 (downloaded into the session scratch
  folder, not the project) and every printed output matched the text.** They had been hand-traced first and
  every trace was right. Without a JDK the scripts still write the JSON and print how many examples were not
  checked, so re-run them with one after editing an example. Avoid `$` in examples (the validator reads it as
  unclosed math).
- **Authoring** (Calc AB): `scripts/content-authoring/ap-calc-refreshers/u1.py..u8.py` write the JSON.
  Both courses write through `scripts/content-authoring/refreshers_lib.py`.
  Each script re-checks its worked examples with sympy before writing, so a number in the text can't drift
  from the maths; edit the scripts, not the JSON. `render-audit.ts` now also renders every refresher
  (35 for Calc AB: 0 KaTeX errors, 0 raw LaTeX).
- **Authoring** (Physics 1): `scripts/content-authoring/ap-physics-1-refreshers/u1.py..u8.py`, same helper. Each script
  recomputes its worked examples in plain Python before writing: `eq()` / `sig()` (`common.py`) assert that the number
  printed in the text is the computed one (`g = 9.8 m/s^2`, `G`, Earth's mass and radius as the question bank uses them),
  so a number cannot drift. What is *not* machine-checked is the physics in the sentences (what a quantity means, which
  way a force points); that was proofread, and it is what the owner's review is for. 32 refreshers: 0 KaTeX errors, 0 raw
  LaTeX. Write a chain of steps as an `aligned` block, one step per line, never `\quad\Rightarrow\quad` on one line (see below).
- **Wide equations on a phone** (found 2026-10-07, testing Physics 1): KaTeX sets a display equation to `nowrap` and
  nothing handled overflow, so a long one made the page wider than the screen (the mobile browser zooms out to fit it,
  which is also why a `scrollWidth > innerWidth` check at 375px said "fine": the viewport had grown to fit). The text
  column on a 375px phone is **343px**. 12 of Physics 1's first 21 display equations were wider (up to 682px), as are
  8 of Calc AB's 23 (up to 476px). `globals.css` now gives `.katex-display` `overflow-x: auto` so a long one scrolls
  inside its own block. Scrolling clips the box, and fractions and big brackets stick out of it by up to 6px, so it also
  has `padding-block: 0.5em` (taken from KaTeX's 1em margin, so spacing is unchanged); measured 0 clipped of 33 equations.
  Physics 1's were rewritten as aligned lines so none needs scrolling, and **Calc AB's 8 were split the same way
  (2026-10-08)**: all 23 of its display equations now measure at most 343px with none clipped. To measure, put each
  `.katex-display` into a 343px `.reading.prose` box and read `scrollWidth`. **That works before any reseed**: render the
  content with `renderContentToHtml`, write the equations' HTML to a temporary `public/__tmp-displays.json` (the repo has no
  `public/` folder, so create it and delete it afterwards), and fetch it from any page that loads the global CSS, such as
  `/privacy`, with no sign-in. On a seeded page, fetch it as the signed-in user instead and query `body`, not `main` (the
  refresher body is in the streamed, hidden block, so `main` is empty in the fetched copy), and strip `annotation` and
  `.katex-mathml` before searching the text for raw TeX (they hold the TeX source and look like a leak).
- **Authoring** (U.S. History): `scripts/content-authoring/ap-us-history-refreshers/u1.py..u9.py`, same helper. History has
  nothing to compute or compile, so **none of it is machine-verified**. Claims are kept to well-established CED-level
  facts; `ap-us-history/facts.py` (which now also reads refreshers: it falls back to unit/topic when an item has no `id`)
  checks every named event followed by a year against its date table and found no real disagreement (its 5 hits are all the
  known "Georgia" false positive in *Worcester v. Georgia*); and every one of the 391 year mentions was read in context.
  That catches wrong dates and wording slips, not every framing problem, so the owner's review is the real check. The
  fourth section is a short-answer prompt with a sketch of a strong response (claim, specific evidence, the link between
  them) instead of a calculation. Rounded figures to look at first: about 120,000 Japanese Americans interned, about
  180,000 Black Union soldiers, at least 620,000 Civil War deaths, nearly 3,000 on 9/11, 150 or more at Wounded Knee.
  Authoring slips the validator caught or I fixed while proofreading: a lone `$15 million` (the validator reads a single
  `$` as unclosed math, so write "15 million dollars"), Salem (about 20 executions, not 19), the 1808 slave-trade ban
  (Congress ended it; the Constitution only allowed that), Gettysburg ("bloodiest", not "largest"), and the Knights of
  Labor (they excluded Chinese workers, so not "many races").
- **Authoring** (World History): `scripts/content-authoring/ap-world-refreshers/u1.py..u9.py`, same helper and layout as
  U.S. History (the worked example is a short-answer prompt and a sketch of a strong response). Nothing is machine-verified:
  claims were kept to well-established CED-level facts, all 302 year mentions were read in context, and `facts.py` (a World date
  table that scans the refreshers *and* the existing World questions and prompts) found no disagreement in the refreshers.
  Its 5 hits are false positives in existing content: a document dated 1793 inside the Haitian Revolution, "Opium War, 1840s",
  the Fourth Crusade in 1204, and the UN adopting the Declaration of Human Rights in 1948. A new flag in a refresher is real.
  Corrections made while proofreading: the Maya "decline" line (Postclassic Maya cities continued), "millions died" on the
  Middle Passage (well over a million), Brazil's 1822 independence being from Portugal, and the 1973 oil embargo being by
  OPEC's Arab members. The owner's review is the real check; figures to look at first: about 12 million Africans embarked on
  the Atlantic slave trade, about six million Jews killed in the Holocaust, "roughly a million or more" Armenians, and the
  world population of about 1.6 billion in 1900 against more than 8 billion in the 2020s.
- **Approved 2026-10-09.** The owner said they had looked through everything and asked for the approvals to be set
  directly instead of clicking "Approve all" on every unit page. They had approved 5 Calc AB refreshers themselves in
  `/admin/review`; the other 190 were set with one `updateMany` on `Topic.refresherReviewed` (only topics that have a
  refresher and were not yet approved; no other column or table was touched, and every per-user and per-table count was
  identical before and after). The live About page then read "2,411 of 2,411 have been checked by a person" (2,216 questions
  and prompts plus 195 refreshers). **Approvals still reset when a refresher's text changes and is reseeded**, so editing
  one sends it back for review. The About page has three wordings (`app/about/page.tsx`): none reviewed ("None of them has been
  checked by a teacher yet..."), some reviewed ("N of M ... The rest have not..."), and, since 2026-10-09, all reviewed ("All N
  have been checked by a person. A check is not a guarantee, so a mistake can still get through."). Tested in
  `tests/about-page.test.tsx`.
- **Not done**: no refresher videos; no search. Whether a student has read a refresher is not tracked.

## Hard sets (harder questions, added alongside)

All four courses have one: 15 MCQs and 2 FRQs per unit in `questions/unit-N-hard.json` and
`frqs/unit-N-hard.json`, ids `<course>-uN-mcq-31..45` and `-frq-4..5`, tagged
`difficulty: "hard"`, authored `reviewed: false` (approved in the database since, see below). Calc AB first (below), then CSA, World History
and Physics 1 (sections after it). Generators live in `scripts/content-authoring/<course>-hard/`
(see its README); re-running one overwrites its output, so **edit the script, not the JSON**.

### Hard Calc AB set

The owner found the existing banks too easy (the items tagged `hard` were things like "find
f'(3) for x² from the difference quotient") and supplied three pages of a real Calc AB
class's quizzes as the *difficulty* reference (questions only; student work and marks were
ignored on purpose). The new items are **additional**, not replacements, so no existing
question id, attempt or history changed.

- **Size and files**: per unit, 15 MCQs (`ap-calc-uN-mcq-31..45`) and 2 FRQs
  (`ap-calc-uN-frq-4..5`), tagged `difficulty: "hard"`, in `questions/unit-N-hard.json` and
  `frqs/unit-N-hard.json`. 120 MCQs + 16 FRQs in all, all `reviewed: false`. The Calc AB
  bank is now 360 MCQs + 40 FRQs.
- **What "hard" means here** (the reference's style): several steps, a trap, a justification.
  Simplify then differentiate; tangent *and normal* lines; give the *point*, not just the
  x-value; a double root is a zero but not a sign change; continuous does not mean
  differentiable (one-sided derivatives); a limit-definition derivation; L'Hôpital that does
  not apply; "exactly" versus "at least" in the IVT; setup-only washer integrals. No
  calculator needed. Several use the diagram support (a graph of f' or f).
- **How correctness is established**: the items are *generated* by
  `scripts/content-authoring/ap-calc-hard/u1.py..u8.py` (see its README). Each answer is
  computed in sympy from the same objects the stem is printed from, every wrong choice is
  a named mistake whose value is also computed, and asserts fail if two choices coincide
  or the keyed answer is wrong. Also verified: `content:validate`, the letter-reference
  audit (`tests/choice-letters-audit.test.ts`), and all 1,342 new strings rendered through the
  real KaTeX pipeline with 0 errors and no raw LaTeX left visible. **Hand-written parts** (the
  explanation of why each wrong choice is wrong, and the FRQ rubrics and sample responses)
  were proofread but are not machine-checked; they are the likeliest place for a slip, which
  is why the files say `reviewed: false` and a person approves them in `/admin/review`.
- **Editing**: re-running a script overwrites its output, so change the script, not the
  JSON. The owner judged the Calc AB difficulty and asked for the other three courses to
  follow (next sections).
- **Effects to know**: exam simulations draw from the whole pool, so about a third of an
  exam's Calc AB questions are now from the hard set. Hard items earn the highest XP tier.
  The landing page and course pages read counts from the database, so they change when
  the content is seeded (`npm run content:seed`; a direct database write, ask first).

### Hard AP CSA set

150 MCQs + 20 FRQs (`scripts/content-authoring/ap-csa-hard/u1.py..u10.py`, shared `common.py`).
Same standard as Calc: multi-step traces with a trap (aliasing, `String` immutability and `==`,
integer division and casting, short-circuiting, off-by-one loops, removal while traversing an
`ArrayList`, row/column order in 2D arrays, constructor chaining, field initializers running
after `super()`, overload versus override, `static` shared state, recursion call trees).

- **Correctness is established by running real Java.** Each output shown in a question is what
  a JDK printed when the displayed program was compiled and run; each wrong choice is the real
  output of a *mutated* copy of that program (or, where a mistake can't be produced by one
  small edit, a named "manual" mistake that the script asserts differs from every real output).
  Compile-error questions are checked with `javac` (exactly one option fails to compile), and
  every FRQ sample solution was compiled and run against tests (`verify()`), so the sample
  responses are known to work.
- **A JDK is not a project dependency.** The scripts look for `JAVA_HOME`, else a Temurin JDK
  unpacked in the session scratch folder (`common.py`, `SCRATCH`); to regenerate, download a
  JDK 21 and set `JAVA_HOME`. The generated JSON is what the app uses, so nothing needs Java
  at build or run time.
- Code-in-stem convention: fenced ```java blocks, class definitions first and the run segment
  second (`shown()` dedents methods). Choice text that is multi-line program output uses real
  newlines. `$` is avoided in prompts (the content validator counts it as unclosed LaTeX even
  inside inline code).
- **Not machine-checked**: the hand-written explanations of why each wrong choice is wrong and
  the FRQ rubrics. Proofread by the generator's author, then approved by the owner in `/admin/review`.

### Hard AP World History set

135 MCQs + 18 FRQs (`scripts/content-authoring/ap-world-hard/`): per unit, 15 MCQs
(a mix of passage-based items and "which best explains" causation/comparison items) and two FRQs:
a **3-part SAQ on a passage** (3 points) and a **6-point LEQ** (thesis 1, contextualization 1,
evidence 2, analysis and reasoning 2). Sources are *original* passages with generic
attributions, not quotations from real documents or from any College Board exam. **Historical facts cannot be machine-verified**; they were written from
well-established, CED-level knowledge and kept to claims that are not disputed, but a human
reviewer should check them (the owner has since approved them in `/admin/review`). These items are typed `SAQ`
and `LEQ` (the generator helpers `saq()`/`leq()` set it), so exam simulations draw from them
correctly (the pool is now 36 SAQs, 4 DBQs, 13 LEQs).

**Answer lengths were evened out afterwards (2026-10-06).** The right answer was the longest choice in 87%
of the 405 questions (core 81%, hard 99%; median length ratio 2.19), so always picking the longest scored
well without knowing any history. `scripts/content-authoring/ap-world-pad/` holds `pad_u1.py..pad_u9.py`
(`PAD` = the wrong choices' new text in file order, `PADC` = the right one, `PADW` = single wrong choices,
matched by text) and `apply.py`, which writes them into `content/ap-world/questions/` (the core files line
by line, since they keep one choice per line and don't round-trip through `json.dump`; the `-hard` files
through json). Only a choice's `text` changed: labels, which choice is correct and every explanation are
as before (checked against `git HEAD` for all 405 questions; 1,298 choice texts changed). Result: the
right answer is the longest in 26% of questions (chance is 25%), the shortest in 13%, median ratio 1.04.
`python3 stats.py` measures it, `python3 flag.py <unit>` lists the questions where it is still the
longest, and `extend_longest.py` was the second-pass helper. **Re-run `python3 apply.py` after
regenerating an `ap-world-hard` script** (it rewrites that file from scratch and would undo the padding;
the overlay is idempotent).
- One factual slip was fixed on the way: `ap-world-u4-mcq-5` credited da Gama where the question is
  about Dias rounding the Cape (stem and explanation corrected).
- **Seeded and pushed 2026-10-06** (`0a65b34`). The seed kept 91 approvals and reset 367 (the questions
  whose text changed; see "Approvals survive a re-seed unless the content changed"), so the World unit
  pages in `/admin/review` need their "Approve all" buttons again until the About page's "checked by a
  person" count is back to 100%. The 53 free-response prompts are unchanged and stay approved. Checked
  afterwards: all 405 database questions equal the files, and every per-user and per-table count matched
  the pre-seed snapshot.

### Hard AP Physics 1 set

120 MCQs + 16 FRQs (`scripts/content-authoring/ap-physics-1-hard/`). Multi-step problems
(impulse from a force graph, sticking and elastic collisions, center of mass, a hinged beam held
by a cable, rolling races, angular momentum on a rotating stool, the minimum speed at the top of
a loop, orbits and gravity on other planets). `g = 9.8 m/s^2`; each computed answer is produced by
Python arithmetic in the script, with `assert`s for the keyed answer and for distinct choices, and
each wrong choice is a specific mistake (a missing factor, the wrong quantity). Eight items use the
diagram support (motion graphs and free-body diagrams); the rest are word problems.

### Effects of all four hard sets

Exam simulations draw from the whole pool, so roughly a third of the questions are now from the
hard set in every course, and hard items earn the top XP tier. The landing page and course pages
read counts from the database, so they change when the content is seeded. Seeding is
`npm run content:seed` (a direct database write; ask first). It is **slow** (the whole bank takes
10+ minutes) and **stops at the first connection error**, so run it in the background and check the
row counts against the files afterwards (an interrupted run is safe to repeat: it upserts).

## AP U.S. History (the fifth course)

Added 2026-10-05 at full size (owner's request: "full size", then take it off Coming soon). Same shape
as World History, so no engine change: the exam builder already draws SAQ/DBQ/LEQ by type.

- **Structure**: slug `ap-us-history`, id prefix `ap-ush`, nine units (the CED's nine periods,
  1491 to the present; weightings 4-6, 6-8, 10-17 x6, 4-6) and 46 topics. Per unit 30 MCQs + 3 SAQs
  (`unit-N.json`: `ap-ush-uN-mcq-1..30`, `frq-1..3`) and a hard set (`unit-N-hard.json`: MCQs 31..45,
  one SAQ and one 6-point LEQ as `frq-4..5`), plus a course pool of 4 DBQs + 4 LEQs
  (`frqs/dbq-leq-pool.json`, `ap-ush-dbq-1..4`, `ap-ush-leq-1..4`). Totals: **405 MCQs** (47 easy,
  137 medium, 221 hard) and **53 free-response** (36 SAQ, 4 DBQ, 13 LEQ), the same as World.
  Exam format: 55 MCQ + 3 SAQ + 1 DBQ + 1 LEQ, 195 minutes, the *current* structure; the College Board
  has announced revisions to the short-answer and long-essay questions for May 2027 but not published
  details, so this stays as is until it does.
- **Authoring**: `scripts/content-authoring/ap-us-history/` (`common.py`, `uN_base.py`, `uN_hard.py`,
  `pool.py`). Edit the scripts, not the JSON. `authoring.Bank` gained a `suffix` argument (default
  `"-hard"`, so the other courses are unchanged) so a core set writes `unit-N.json`.
- **Sources are original** with generic attributions ("A Massachusetts minister's sermon, 1630s"), never
  quotations from real documents or exams: a quote written from memory could be wrong. Stimuli are text
  only; there are no cartoons or maps because diagram support covers only graphs and force diagrams.
- **Correctness**: history can't be machine-verified. Claims are kept to well-established CED-level
  facts. `facts.py` checks that every named event followed by a year ("Stamp Act of 1765", "Fort Mose in
  1738") agrees with a ~200-event date table (it only catches disagreement with the table, which was
  itself written from standard dates; its 3 hits were false positives). The usual checks pass
  (`content:validate`, the choice-letter audit, `render-audit.ts`: 0 problems). **The owner's review in
  `/admin/review` is the real check**; the course is visible to students as soon as it is seeded,
  so "checked by a person" on the About page falls below 100% until it is approved.
- **A tell found and fixed while writing it: the right answer was the longest choice in 97% of
  questions** (it is the one with the qualifying clauses), which a student can exploit without knowing any
  history. `pad_uN.py` overlays, loaded by `common.py`, lengthen the wrong choices (`PAD`, in the order the
  script lists them), trim the right ones (`PADC`) and patch single choices (`PADW`, matched by their
  current text) until length says nothing; explanations are unchanged. Result: the right answer is the
  longest in 29% of questions (chance with four choices is 25%), the shortest in 12%, median length ratio
  1.03. `stats.py` measures it and `flag.py <unit>` lists the questions where it is still the longest.
  Run `python3 stats.py` after any edit to a question. `PaddedBank.mcq` prints each question's
  lengths when `DUMP=1`.
- **Effects**: exam simulations draw from the whole pool (so a third of a U.S. History exam's questions
  are hard-set items), hard items earn the top XP tier, and the course appears for students on seeding.

## Forgot password and email

Built 2026-10-05 and **not live until a domain is verified** (see "Turning it on"). Resend is the
only email integration on the Vercel Marketplace, so it is the provider; it is called with one
`fetch` (`lib/email/send.ts`), no SDK.

- **Flow**: `/forgot-password` (`requestPasswordResetAction`) -> email with
  `<SITE_URL>/reset-password?token=<code>` -> `/reset-password` (`resetPasswordAction`) sets the new
  password under the usual rules. The login page shows "Forgot your password?" only when
  `isPasswordResetAvailable()` (email configured, or any non-production run); `/forgot-password` says
  "isn't available yet" otherwise. After a reset the person logs in again; every other device is
  already signed out because the password hash changed (`credentials-stamp.ts`).
- **No account enumeration**: the request answers identically for every address, and everything that
  depends on whether the address has an account (lookup, throttle, token, email) runs in
  `afterResponse()` (`lib/after-response.ts`, Next's `after`), so neither the words nor the response time
  differ. Tested (`tests/reset-actions.test.ts`).
- **The token**: 32 random bytes as base64url (`lib/auth/reset-token.ts`); only its SHA-256 is stored,
  valid 60 minutes, used once. Claiming it is one atomic `updateMany` on an unused, unexpired row, so
  two simultaneous submissions can't both succeed. A wrong new password does not use the link up. A
  newer request retires older links, but only after the new one is safely stored.
- **Throttle**: at most 3 requests per account per hour *and* one per minute. The per-minute part is
  `@@unique([userId, minuteSlot])` on `PasswordResetToken`: a count-then-insert limit lets a burst of
  simultaneous requests all pass (a test caught exactly that), the unique index does not. Rows older
  than a day are deleted opportunistically on the next request. Per-IP limiting would be a Vercel
  Firewall rate-limit rule on `POST /forgot-password` (not set up).
- **Links come from configuration, never the request**: `siteUrl()` (`SITE_URL`, else
  `NEXT_PUBLIC_SITE_URL`, else the production URL). A link built from the Host header could be pointed
  at an attacker's site. The reset page sets `referrer: no-referrer` and `noindex` because the secret is
  in its address.
- **Notice emails**: `notifyPasswordChanged` (`lib/email/notify.ts`) emails the account's own address
  after a password change in Settings or a reset, only when email is configured, so a missing key never
  turns a password change into an error.
- **`"use server"` files may export only async functions** (Next fails the build otherwise, and anything
  exported is callable from the browser). That is why `RESET_LINK_INVALID`, `RESET_TOKEN_MINUTES`
  (`reset-constants.ts`, also kept apart from `reset-token.ts` because that imports `node:crypto` and
  can't be bundled for the client) and `isResetLinkUsable` (`reset-queries.ts`) live outside
  `reset-actions.ts`. `tsc` does not catch this; `npm run build` does.
- **Env** (`.env.example`): `RESEND_API_KEY`, `EMAIL_FROM` (an address on a domain verified in Resend),
  optional `EMAIL_REPLY_TO`, optional `SITE_URL`. Without the first two, development prints the email
  (link included) to the server console instead of sending; production sends nothing and hides the link.
- **Turning it on** (needs the owner): a domain (the Vercel account had none; `vercel.app` can't be
  verified for sending, and without a verified domain Resend delivers only to its owner), the Resend
  integration installed (`vercel integration add resend/resend-email`, which sets the env vars), and the
  migration `20261006100000_add_password_reset_token` applied *before* pushing code that reads the table.
- **Not built**: email verification at signup (anyone can register an address they don't own; a reset
  only ever emails the stored address, so this can't take an account over, but it can squat an address),
  and a notice when an account is deleted.

## Footer, contact and privacy

- **Contact is a prefilled `mailto:` link, never a printed address.**
  `lib/site-contact.ts` (`feedbackMailto`, `privacyMailto`) builds
  `mailto:<owner address>?subject=...&body=...` with `encodeURIComponent` (not
  `URLSearchParams`: mail apps read `+` literally). The visitor sees "Report a
  mistake or send a suggestion"; their mail app opens addressed to the owner with
  a subject and a prompt for what to write. The address *is* in the link's `href`,
  so it isn't hidden from someone viewing the source or from scrapers; a contact
  form would hide it but needs an email service this app doesn't have. The owner's
  choice, 2026-10-04; tests assert the address never appears as visible text.
- **`/privacy` (`app/privacy/page.tsx`) states only what the code does**: what is
  collected (account, study activity, FRQ text, friends/classes, waitlist email,
  host server logs), who sees it (usernames and XP, never names or email), no ads,
  no analytics or tracking scripts, the sign-in cookie, the `ap-cram` cookie
  (7 days, holds the user id), local storage for theme and sound, Neon (US) and
  Vercel. **Keep it true:** `tests/privacy-page.test.tsx` ties the cookie name and
  lifetime to `cram-mode.ts` and fails if an analytics/tracking package is added
  to `package.json`. Update the page and its `UPDATED` date whenever you add
  tracking, a cookie, or a new kind of stored data.
- **Commitments the page makes on the owner's behalf**, to honor or edit: access and
  correction *by request*, waitlist removal for someone *without an account* by request,
  deleting an under-13's data if one turns up, and "we don't sell your information".
  Deleting your own account and changing your password are now self-serve in Settings.
- **Minimum age: 13 (owner decision, 2026-10-04).** `MINIMUM_AGE` in `lib/age.ts` is
  the single source. Signup requires a checked "I am 13 or older" box
  (`ageConfirmed`, value `yes`), enforced **server-side** in `SignUpSchema`, so
  omitting the field from a hand-made request doesn't skip it (tested in
  `tests/signup-age-gate.test.ts`, which also checks no user is created and nothing
  is stored). The waitlist form says it, and `/privacy` has a "Who it's for"
  section: no birth date is asked for, no knowing retention of under-13 data,
  deletion on request. This is a self-declaration, not verification: we
  deliberately don't collect a birth date, since that would mean storing more
  personal data. Accounts created before the check existed were not asked; the
  owner confirmed on 2026-10-04 that all of them belong to people over 13 (their
  statement, not something the app can verify).
- **Privacy page reviewed**: the owner reported on 2026-10-04 that it has been
  reviewed. Nothing is open on it now; re-review it if the site starts collecting or
  sharing anything new (the page's `UPDATED` date and the guard tests in
  `tests/privacy-page.test.tsx` are the reminders).
- Test setup note: `tests/setup.ts` now runs Testing Library's `cleanup()` after each
  test (vitest runs without globals, so it wasn't happening, and `getBy*` found
  duplicates left over from earlier renders in the same file).

### Auth forms keep what you typed after a rejected submit

React 19 empties an uncontrolled `<form action={fn}>` when its action finishes, so
a rejected signup or failed login used to wipe every field. Now `signUpAction` and
`loginAction` return `{ error, values }` (`SignUpFormState` / `LoginFormState` in
`lib/auth/schema.ts`), and the forms use `values` as each field's `defaultValue`, so
the automatic reset puts the same text back. **The password is never part of
`values`** (a test asserts the response doesn't contain it), so it is emptied on
every error, as it should be. Echoed values are capped at 254 characters. Each
refilled `<Input>` has `key={its value}`: Base UI's `Input` logs a dev-console
error if the `defaultValue` of an already-mounted field changes, and a changed key
mounts a fresh field instead. Keep both when adding fields to these forms.
`tests/auth-forms.test.tsx` runs the real forms through React's reset (it fails
without the fix) and `tests/auth-form-state.test.ts` covers the actions.

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
| AP U.S. History | 9 units, 1491 to the present | 55 MCQ + 3 SAQ (all required) + 1 DBQ + 1 LEQ, 3h15m | **May 2027**: short-answer and long-essay questions revised (the College Board has not published details). |

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
      type items total; typed SAQ/DBQ/LEQ since 2026-10-05 so the exam sim draws the
      right mix). **AP Calculus AB**: 8/8 units, 240
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

- [x] **Post-launch: visual design overhaul.** Audit, one approved direction
      (graphite on paper with a highlighter accent), the four-theme picker
      retired, and every page moved onto one token set and a shared component
      set; new landing page with a working sample question and a Today screen
      at `/`. See "Visual design system" above.
- [x] **Post-launch: growth features.** Landing page now ships finished HTML
      (root skeleton removed), waitlist + "Coming soon" + an empty-by-design
      testimonials scaffold, Cram Mode, proficiency-rated mastery bars, boss
      battle titles (and a missing boss-result toast fixed), and a `/teacher`
      skeleton for class owners. See "Post-launch growth features" above.
- [x] **Post-launch: hard question sets.** 15 hard MCQs + 2 hard FRQs per unit in all four
      courses (Calc AB 120 + 16, CSA 150 + 20, World 135 + 18, Physics 1 120 + 16), added
      alongside the originals. All four are seeded into the database and deployed (2026-10-05;
      row counts and per-question correct-answer/difficulty/diagram checked against the files after
      seeding). See "Hard sets" above.
- [x] **Post-launch: topic refreshers.** Engine built and tested (schema, validation, seed, topic page,
      links, review, About count) and Calc AB's 35 refreshers written, seeded and live (they start unreviewed; **all 195
      refreshers across the five courses were approved 2026-10-09**, see "Topic refreshers"). CSA's 39 followed (seeded 2026-10-06 after its Java examples were
      compiled and run; its 500 approvals were kept). Physics 1's 32 followed (2026-10-07, seeded twice: the second time
      after the long equations were split; its 400 approvals were kept). U.S. History's 46 followed (2026-10-07; written from well-established facts and proofread, not machine-checked; its 458
      approvals were kept). World History's 43 followed (2026-10-08, same standard; its 458 approvals were kept), which completes the set. The 8 Calc AB equations were
      split in the same pass. See "Topic refreshers".
- [x] **Post-launch: AP U.S. History.** A fifth course at full size (405 MCQs + 53 free-response,
      base and hard sets in one pass), the existing 2026-10-05 length-tell fix applied while
      writing it, `Coming soon` updated, headlines that said "four exams" now derived from the course
      count. See "AP U.S. History" above.

## Known issues / follow-ups

- **DBQ document layout (fixed and live 2026-10-09).** Each DBQ document was three consecutive lines (`**Document 1**`,
  `Source: ...`, the quotation), which markdown joined into one paragraph ("Document 1 Source: ... "quote""). Now every
  document is a bold label, a `Source:` line and the quotation as a blockquote (the multiple-choice passages' treatment),
  separated by blank lines, in all 8 DBQs (4 World, 4 U.S. History). Only line breaks changed (checked field by field against
  the previous version). `scripts/content-authoring/dbq-layout/apply.py` does the rewrite (idempotent; edits raw text so
  World's hand-formatted pool is not reformatted; `--check` lists prompts still in the old form), U.S. History's `pool.py`
  `docs()` helper emits the new layout, and `tests/dbq-layout.test.ts` fails on the old one (verified). Seeding reset the 8
  prompts' approvals (the content changed) and the owner asked for them to be re-approved directly, which was done by id.
  All four places that show a prompt (practice page, exam, exam results, admin review) use `renderContentToHtml`, so the fix
  applies to each; the practice page was checked on the real pages at desktop and 375px. Nothing else in the prompts changed,
  and no other free-response prompt had the problem.

- **Answer lengths in Calc AB, Physics 1 and CSA (core sets) were evened out 2026-10-06**, with the same
  overlay approach as World History (`scripts/content-authoring/ap-core-pad/`: `<course>/pad_uN.py` holding
  `PAD` / `PADC` / `PADW`, `apply.py <course>`, `stats.py`, `flag.py`, `dump.py`, plus `extend_longest.py`
  for second passes). Only a choice's `text` changed (921 texts in 280 questions; labels, correctness and
  every explanation as before, checked against `git HEAD`). Before -> after, the right answer being the
  longest of its choices: Calc AB 51% -> 22%, Physics 1 47% -> 19%, CSA 35% -> 17% (counting only
  questions with prose choices, where length can be a tell: 76% -> 24%, 75% -> 28%, 66% -> 24%). The
  hard sets (`unit-N-hard.json`) were generated with computed distractors and were already balanced (12%,
  5%, 6%), so they were not touched. The core files were written straight to JSON, so unlike World's
  hard set there is no generator to re-run. Short math and code choices (`$p = mv$`, a line of Java)
  are left alone: their lengths mean nothing, except that a trailing "where m is mass..." on the right
  formula was trimmed, since that was a tell on its own.
  **Left as is, on purpose**: the right answer is rarely the *shortest* choice now (Calc 4%, Physics 10%,
  CSA 5% of all questions; World and U.S. History are 12-13%), a small reverse tell. Lengthening the
  shortest wrong choice in more questions would fix it if it ever matters.
  **Seeded and pushed 2026-10-06** (`1d0acd0`). The seed reset the approval of the 280 changed questions
  (Calc AB 91, Physics 1 104, CSA 85; the rest kept theirs), so those units' pages in `/admin/review` need
  "Approve all" again. Checked afterwards: every database question equals its file, and every per-user and
  per-table count matched the pre-seed snapshot.

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
- **Only one admin** (`viraj1`, promoted 2026-10-05), so `/admin/review` is reachable by the
  owner only. Promoting anyone else is a direct DB write: needs explicit sign-off first.
- **The authored content still has the correct answer in slot A ~60% of the
  time** (Calc 99%, Physics 100%, CSA 30% A / 56% B, World 26% A / 72% B). It no
  longer matters to students because choices are shuffled on every showing (see
  "Answer choices are shuffled" above), but don't read the JSON's order as
  meaningful, and `/admin/review` deliberately shows the *authored* order so a
  reviewer can compare it with the content files.
- **The correct answer is in the page payload.** `RenderedChoice.isCorrect` goes
  to the client for every choice before the student answers (the runners need it
  to reveal instantly), so someone who opens the browser's dev tools can read it.
  Shuffling stops position-guessing, not inspection. Pre-existing. The fix would
  be a server-side reveal (ship choices without correctness/explanations; have
  `recordAttempt` return the correct label and explanations after each answer).
  **Owner decision, 2026-10-04: not wanted. Don't propose it again** unless the
  owner raises cheating (leaderboards, titles, classes) as a problem. Browsers
  can't be stopped from showing page data, so "block dev tools" tricks are not an
  option either.
- **`npm run lint` ignores `.claude/worktrees/**`** (`eslint.config.mjs`). The desktop app creates git worktrees there, each a
  whole extra copy of the repo, and before the ignore they produced 505 errors that were not this project's code.
- **Dev/testing gotchas.** (1) This folder produces duplicate "`<name> 2`"
  files (seen in `.next/` and `node_modules/next/dist/docs/`): Turbopack then
  refuses to start ("Unexpected file in persistence directory") and `tsc` reports
  duplicate identifiers. `rm -rf .next` fixes it. (2) In the desktop app's
  Browser pane, a hidden pane never fires `requestAnimationFrame`, so streamed
  Suspense content stays behind its skeleton; to test a page that streams,
  temporarily move that section's `loading.tsx` aside (then `git checkout` it).
- **Test accounts.** The design overhaul was verified signed in against the
  shared Neon database with a scratch account (`design_scratch`,
  `design-scratch@example.com`); it and everything it created are deleted when
  the work finished. If that user ever appears in the list, it is leftover.
  The growth-features work used `scratch_phase2` / `scratch-phase2@example.com`
  the same way; deleted afterwards and row counts compared to a pre-test
  baseline (identical). The exam-mix fix used `scratch_frqtype` /
  `scratch-frqtype@example.com`: one real World History exam in the browser (60 items: 55 MCQ,
  3 short answer, 1 document-based, 1 long essay, labelled and listed in order on the results
  page), then deleted; all 12 table counts matched the baseline afterwards. With other students
  using the app, compare counts per user, not just totals. The forgot-password work used
  `scratch_reset` / `scratch-reset@example.com` (2026-10-05) and was verified end to end in the browser against
  the shared database: a second session made before the reset was signed out by it, the old password stopped
  working and the new one worked, a same-minute repeat sent no second email, an unregistered address got the
  identical page and no email, the link refused a second use, and the stored token was a 64-character hash.
  Deleted afterwards (its reset row cascaded); every table count matched the baseline.
  The AP U.S. History seed was verified in the browser with `scratch_ush` / `scratch-ush@example.com`
  (2026-10-06): signed up, enrolled, answered a quiz question (reveal, per-choice explanations, XP), started a
  real exam (60 items: 55 multiple choice, then Short answer 1-3 of 3, Document-based question, Long essay;
  3:15 clock), submitted it blank and read the results page. Deleted afterwards; every count, including each
  real student's, matched the post-seed snapshot.
  The DBQ layout fix was checked with `scratch_dbq` / `scratch-dbq@example.com` (2026-10-09): all 8 DBQ practice pages fetched
  as that user (7 labels, 7 source lines and 7 blockquotes each, no joined paragraphs, no leftover markup), one at desktop and
  one at 375px (no overflow). Deleted afterwards (not promoted to ADMIN); every per-user and per-table count matched the
  pre-seed snapshot.
  The World History refreshers (and the 8 reworked Calc AB pages) were checked with `scratch_world` / `scratch-world@example.com`
  (2026-10-08): all 43 World pages fetched as that user (four sections, rendered lists, no leftover markup, a practice link, the
  report link and the "not checked by a person" notice on every page), the 8 Calc pages (0 KaTeX errors, every display
  equation at most 343px, none clipped), a World page and a Calc page at 375px (no overflow), "Practice this topic", "Review
  this concept" from an answered question, and the unit page's Refreshers list. Deleted afterwards (not promoted to ADMIN);
  every per-user and per-table count matched the pre-seed snapshot.
  The Physics 1 refreshers were checked with `scratch_phys` / `scratch-phys@example.com` (2026-10-07): all 32 topic
  pages fetched as that user (485 formulas, 21 display equations, 0 KaTeX errors, all four sections on every page), a
  phone-width look at Rotational Equilibrium, "Practice this topic", "Review this concept" from a missed question, and
  the unit page's Refreshers list. Deleted afterwards (it was not promoted to ADMIN); every per-user and per-table count
  matched the pre-seed snapshot.
  The U.S. History refreshers were checked with `scratch_hist` / `scratch-hist@example.com` (2026-10-07): all 46 topic pages
  fetched as that user (four sections, rendered lists, no leftover markup, a practice link, the report link and the
  "not checked by a person" notice on every page), the topic page at desktop and 375px (no overflow), "Practice this
  topic", "Review this concept" from an answered question, and the unit page's Refreshers list. Deleted afterwards (not
  promoted to ADMIN); every per-user and per-table count matched the pre-seed snapshot, compared with keys sorted (the
  snapshot lists courses in database order, which can change after a seed).
  The CSA refreshers were checked the same way with a second `scratch_refresh` account (the topic page with
  syntax-highlighted code at desktop and 375px, no overflow, and the unit page's links), deleted afterwards
  with every count matching the baseline.
  The refreshers were verified in the browser with `scratch_refresh` / `scratch-refresh@example.com`
  (2026-10-06), temporarily promoted to ADMIN (that scratch account only) to open the review pages without
  approving anything; deleted afterwards, and every per-user and per-table count matched the pre-migration
  snapshot.
  **Old test accounts deleted 2026-10-05** (owner's request): `viraj_test`, `alex_test`,
  `deploy_smoketest`, `latex_verify_tmp`, `finalscopecheck` (all `@example.com` students). Checked first
  that nothing a real student owned hung off them: the one class they owned ("Period 3 AP CSA") had only
  those accounts as members, and their one friendship was between two of them. The delete removed 5 users,
  1 class, 2 memberships, 1 friendship and their 26 answers, 3 free-response attempts, 17 XP events, 3 exams,
  3 enrollments, 1 boss result, 1 bookmark, 12 review states and 7 badges; content tables were untouched, and
  every per-user count for the four real accounts (`viraj1`, `brian`, `Arjun1`, `queenshaheen`) was identical
  before and after. Anyone not listed here that shows up as an `@example.com` user is leftover.
