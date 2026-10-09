"""Records the longer text of a question's too-short wrong choice in that unit's PADW overlay.

    python3 record.py <course> <edits.json>        edits.json: {"<question id>": "<the lengthened wrong choice, whole>"}

Checks each edit: the question's one short wrong choice is the one being replaced, the new text is longer than the right answer and not
much longer than the longest wrong choice, nothing in the course shares the old text (PADW matches by text), and the new text is not
already another choice. Then run the course's apply step (core: ap-core-pad/apply.py; World: ap-world-pad/apply.py; U.S. History:
re-run the unit's uN_base.py and uN_hard.py) so the content picks it up.
"""
import json, sys
from lib import *


def main():
    course, edits = sys.argv[1], json.load(open(sys.argv[2]))
    qs = {q["id"]: q for q in load(course)}
    texts = [c["text"] for q in qs.values() for c in q["choices"]]
    by_unit, errors = {}, []
    for qid, new in edits.items():
        q = qs[qid]
        short = single_edit(q)
        if not short:
            errors.append(f"{qid}: not a single-edit question")
            continue
        old = short[1]
        lo, hi = window(q)
        problems = []
        if not lo <= vis(new) <= hi:
            problems.append(f"new text is {vis(new)} visible chars, wanted {lo}-{hi}")
        if new == old or texts.count(old) != 1:
            problems.append(f"old text is shared by {texts.count(old)} choices")
        if new in [c["text"] for c in q["choices"]]:
            problems.append("duplicate choice text")
        if new.count("$") % 2:
            problems.append("unbalanced $")
        if problems:
            errors.append(f"{qid}: " + "; ".join(problems) + f"\n      old: {old}\n      new: {new}")
            continue
        by_unit.setdefault(unit_of(qid), {})[old] = new
    if errors:
        print("\n".join(errors))
        sys.exit(f"{len(errors)} of {len(edits)} edits rejected; nothing written")
    writes = []
    for unit, add in sorted(by_unit.items()):
        path = pad_path(course, unit)
        padw = read_padw(path)
        clash = {k for k in add if k in padw and padw[k] != add[k]}
        assert not clash, f"{course} unit {unit}: PADW already maps {clash} to something else"
        fresh = {k: v for k, v in add.items() if k not in padw}   # already recorded with the same text: nothing to do
        if fresh:
            padw.update(fresh)
            writes.append((path, render_padw(path, padw, f"{'ap-phys1' if course == 'ap-physics-1' else course}-u{unit}-mcq-"), unit, len(fresh)))
    for path, src, unit, n in writes:      # nothing is written unless every file rendered
        open(path, "w", encoding="utf-8").write(src)
        print(f"{course} unit {unit}: {n} recorded in {os.path.relpath(path, AUTH)}")
    print(f"{sum(w[3] for w in writes)} new, {len(edits) - sum(w[3] for w in writes)} already recorded")


main()
