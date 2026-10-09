# Content authoring scripts

Python (sympy) scripts that *generate* hand-designed JSON content. They are authoring
tools, not part of the app: nothing in `src/` reads them and `npm run build` ignores them.

`ap-calc-hard/` writes the hard Calc AB set (`content/ap-calc/questions/unit-N-hard.json`
and `frqs/unit-N-hard.json`). Every number in a stem, choice or explanation is produced
from the same sympy objects that the answer is computed from, with `assert`s that the
correct answer is right and that no two choices are equal, so a typo can't make a wrong
answer look right. The wrong choices are each a named, specific mistake.

```bash
pip3 install --user sympy            # not a project dependency
cd scripts/content-authoring/ap-calc-hard
python3 u1.py                        # rewrites unit 1's two hard files and prints a proofreading dump
npm run content:validate             # then validate (from the repo root)
```

Running a script **overwrites** its output files, so don't hand-edit the generated JSON
without also editing the script (or the next run discards the edit). `lib.py` is the shared
helper (`Bank`, `ch`, `LIM`, `graph`) and is reusable for another course.

## The other three courses

`authoring.py` is the course-independent version of the same helpers (`Bank`, `ch`, `graph`,
`force_diagram`); each `Bank.mcq` refuses duplicate or numerically equal choices, and
`Bank.save()` writes the two JSON files.

- `ap-physics-1-hard/u1.py..u8.py`: plain Python. Each computed answer comes from the arithmetic
  in the script, with `assert`s on the keyed answer.
- `ap-world-hard/common.py, u1.py..u9.py`: hand-written history items (nothing to compute).
  Passages are original, with generic attributions. `saq()` and `leq()` set the prompt's `type`
  (`Bank.frq(..., ftype=)`); a course whose exam has SAQ/DBQ/LEQ sections needs every prompt typed.
- `ap-csa-hard/common.py, u1.py..u10.py`: **needs a JDK** (`JAVA_HOME`, or edit `SCRATCH` in
  `common.py`). `trace()` compiles and runs the displayed program for the correct output and runs
  mutated copies for the wrong choices; `compile_error()` checks compile-error questions;
  `verify()` runs each FRQ sample solution against tests.

Checks to run after (re)generating any course, from the repo root:

```bash
npm run content:validate
npx tsx scripts/content-authoring/render-audit.ts <course-slug>   # KaTeX errors and raw LaTeX leaks
npx vitest run --exclude ".claude/**" --exclude "node_modules/**"  # includes the choice-letter audit
```

## AP U.S. History

`ap-us-history/` is the fifth course and is written entirely by scripts (core set and hard set):
`u1_base.py..u9_base.py` (30 MCQs + 3 SAQs per unit, `unit-N.json`), `u1_hard.py..u9_hard.py` (15 MCQs +
an SAQ + an LEQ, `unit-N-hard.json`) and `pool.py` (4 DBQs + 4 LEQs). Passages and documents are original.

- `pad_u1.py..pad_u9.py` hold overlays that even out answer lengths (see "AP U.S. History" in CLAUDE.md for
  why): `PAD` replaces the wrong choices, `PADC` the right one, `PADW` single choices. `python3 stats.py`
  prints how often the right answer is the longest; `python3 flag.py 5` lists the questions in unit 5 where
  it still is; `DUMP=1 python3 u5_base.py` prints each question's choice lengths.
- `python3 facts.py` checks every event-plus-year in the content against a date table.

```bash
cd scripts/content-authoring/ap-us-history
python3 u1_base.py && python3 u1_hard.py     # rewrites unit 1's JSON (do this for any unit you edit)
python3 pool.py                              # rewrites the DBQ/LEQ pool
python3 stats.py && python3 facts.py
```

## AP World History answer lengths

`ap-world-pad/` evens out choice lengths in the existing World History JSON (see "Hard AP World History set"
in CLAUDE.md). `pad_u1.py..pad_u9.py` are the overlays (`PAD`, `PADC`, `PADW`); `apply.py` writes them into
`content/ap-world/questions/unit-N.json` and `unit-N-hard.json`, changing only each choice's `text`.

```bash
cd scripts/content-authoring/ap-world-pad
python3 apply.py        # all units (idempotent); run it again after regenerating an ap-world-hard script
python3 stats.py        # how often the right answer is the longest / shortest
python3 flag.py 5       # questions in unit 5 where it is still the longest
```

## Calc AB, Physics 1 and CSA answer lengths

`ap-core-pad/` does the same for the core question sets of the other three courses (the hard sets were already
balanced). `ap-core-pad/<course>/pad_uN.py` are the overlays; every script takes the course slug first.

```bash
cd scripts/content-authoring/ap-core-pad
python3 apply.py ap-calc            # writes the overlays into content/ap-calc/questions/unit-N.json (idempotent)
python3 stats.py ap-calc            # how often the right answer is the longest / shortest (all, and prose-choice questions)
python3 dump.py ap-calc 5           # unit 5's questions that still show the tell, wrong choices in file order
python3 flag.py ap-calc 5           # the same, one line each
python3 extend_longest.py ap-calc 5 '{"13": ", since the areas add up"}'   # second-pass: lengthen one question's longest wrong choice
```

## Topic refreshers (Calc AB)

`ap-calc-refreshers/u1.py..u8.py` write `content/ap-calc/refreshers/unit-N.json` (one refresher per topic; see
"Topic refreshers" in CLAUDE.md). Each script checks its worked examples with sympy first. Edit the script, not
the JSON; `common.py` asserts that a unit has exactly one entry per topic, in order.

```bash
cd scripts/content-authoring/ap-calc-refreshers
for u in 1 2 3 4 5 6 7 8; do python3 u$u.py; done
cd ../../.. && npm run content:validate && npx tsx scripts/content-authoring/render-audit.ts ap-calc
```

## Topic refreshers (CSA)

`ap-csa-refreshers/u1.py..u10.py` write `content/ap-csa/refreshers/unit-N.json`. Java examples go through `code()`,
which records the program and the output the text claims; with a JDK (`JAVA_HOME`) `finish()` compiles and runs every
one and fails on a mismatch. Without one it says how many examples were not machine-checked.

```bash
cd scripts/content-authoring/ap-csa-refreshers
for u in 1 2 3 4 5 6 7 8 9 10; do python3 u$u.py; done
cd ../../.. && npm run content:validate && npx tsx scripts/content-authoring/render-audit.ts ap-csa
```


## Topic refreshers (Physics 1)

`ap-physics-1-refreshers/u1.py..u8.py` write `content/ap-physics-1/refreshers/unit-N.json`. Each script recomputes
its worked examples in Python first (`eq()` asserts the value equals the number printed in the text, `sig()` does
the same to significant figures), using `g = 9.8 m/s^2` and the constants from `common.py`, so a number in the text
cannot drift from the arithmetic. Rotational inertia and similar formulas are written as the question bank writes them.

```bash
cd scripts/content-authoring/ap-physics-1-refreshers
for u in 1 2 3 4 5 6 7 8; do python3 u$u.py; done
cd ../../.. && npm run content:validate && npx tsx scripts/content-authoring/render-audit.ts ap-physics-1
```

## Topic refreshers (U.S. History)

`ap-us-history-refreshers/u1.py..u9.py` write `content/ap-us-history/refreshers/unit-N.json`. History has nothing to
compute or compile, so none of it is machine-verified: claims are kept to well-established, CED-level facts, and
`ap-us-history/facts.py` (which now also reads the refreshers) checks every named event followed by a year against its
date table. The "Worked example" is a short-answer prompt with a sketch of a strong response. Avoid `$` (a lone dollar
amount trips the validator's unclosed-math check; write "15 million dollars"), single-asterisk italics and em dashes.

```bash
cd scripts/content-authoring/ap-us-history-refreshers
for u in 1 2 3 4 5 6 7 8 9; do python3 u$u.py; done
cd ../ap-us-history && python3 facts.py          # expect only the known "Georgia" / "Monroe Doctrine" / "farewell address" false positives
cd ../../.. && npm run content:validate && npx tsx scripts/content-authoring/render-audit.ts ap-us-history
```

## Topic refreshers (World History)

`ap-world-refreshers/u1.py..u9.py` write `content/ap-world/refreshers/unit-N.json`, in the same four-section layout as
U.S. History (the worked example is a short-answer prompt and a sketch of a strong response). Nothing is machine-verified:
claims are kept to well-established CED-level facts, and `ap-world-refreshers/facts.py` checks every named event followed
by a year against its date table across the refreshers **and** the existing World questions and prompts. Its known false
positives are all in existing content ("Haitian Revolution, 1793" for a document dated inside the revolution, "Opium War,
1840s", the Fourth Crusade in 1204, the UN adopting the Declaration of Human Rights in 1948); a new flag in a refresher is real.

```bash
cd scripts/content-authoring/ap-world-refreshers
for u in 1 2 3 4 5 6 7 8 9; do python3 u$u.py; done
python3 facts.py
cd ../../.. && npm run content:validate && npx tsx scripts/content-authoring/render-audit.ts ap-world
```
