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
