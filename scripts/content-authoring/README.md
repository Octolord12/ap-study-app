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
  Passages are original, with generic attributions.
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
