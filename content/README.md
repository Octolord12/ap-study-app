# Content

Source-of-truth question/course data, authored as JSON, one folder per course:

```
content/
  ap-csa/
    course.json        # name, colorTheme, examFormat
    units/unit-1.json  # units + topics for the course
    questions/*.json    # MCQs
    frqs/*.json          # FRQ prompts
```

Nothing here is read directly by the app. `scripts/validate-content.ts` checks it
(exactly one correct choice, an explanation for every choice, valid LaTeX, etc.),
then `scripts/seed.ts` loads it into Postgres via Prisma. The app only ever reads
from the database.

Schema + validation landed in Milestone 2, along with a small sample bank
(AP CSA, Units 1 and 4). The full starter banks for all four courses (~30 MCQ +
3 FRQ per unit) are Milestone 7. See `CLAUDE.md` for the exact JSON schema per
question/FRQ field.
