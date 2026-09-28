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

Built out in Milestone 2 (schema + validation + a sample bank for one course) and
Milestone 7 (full starter banks for all four courses). See `CLAUDE.md` for the
exact JSON schema per question/FRQ field.
