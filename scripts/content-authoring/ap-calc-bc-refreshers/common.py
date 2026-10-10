"""Writes the BC refreshers. Units 1-8 reuse Calc AB's (copied by ../ap-calc-bc/derive_from_ab.py); the topics that are new
to BC in units 6-8 are written to content/ap-calc-bc/refreshers/unit-N-bc.json, and units 9 and 10 (all new) to unit-N.json.
Each script re-checks its worked examples with sympy before writing, so a number in the text cannot drift from the maths.
Layout of every refresher: ### The idea, ### Key facts, ### Watch out for, ### Worked example. Edit the scripts, not the JSON.
"""
import json, os, sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import refreshers_lib

COURSE = "ap-calc-bc"
ROOT = refreshers_lib.ROOT


def write(unit_number, entries):
    unit = json.load(open(f"{ROOT}/{COURSE}/units/unit-{unit_number}.json", encoding="utf-8"))
    slugs = [t["slug"] for t in unit["topics"]]
    if unit_number >= 9:
        refreshers_lib.write(COURSE, unit_number, entries)
        return
    assert all(s in slugs for s, _ in entries), f"unit {unit_number}: unknown topic in {[s for s, _ in entries]}"
    assert [s for s, _ in entries] == [s for s in slugs if s in {e for e, _ in entries}], "entries must be in the unit's topic order"
    ab_file = f"{ROOT}/{COURSE}/refreshers/unit-{unit_number}.json"
    have = {r["topic"] for r in json.load(open(ab_file, encoding="utf-8"))}
    assert not have & {s for s, _ in entries}, f"unit {unit_number}: {have & {s for s, _ in entries}} already has a refresher in {ab_file}"
    out = [{"unit": unit["slug"], "topic": s, "body": refreshers_lib.display_blocks(b.strip()), "reviewed": False} for s, b in entries]
    path = f"{ROOT}/{COURSE}/refreshers/unit-{unit_number}-bc.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"{COURSE} unit {unit_number} (BC-only topics): {len(out)} refreshers, {[len(b) for _, b in entries]} characters")
