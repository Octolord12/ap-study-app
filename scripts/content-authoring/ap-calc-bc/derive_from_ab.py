"""Copies Calc AB's units 1-8 (questions, hard sets, free-response prompts and refreshers) into
content/ap-calc-bc/ for AP Calculus BC, which contains all of AB's content.

Only identity changes: every id gets the `ap-calcbc-` prefix instead of `ap-calc-`, every conceptLink
points at `ap-calc-bc/`, and `reviewed` is reset to false (an approval belongs to a row in the database,
and the owner decides when to carry approvals over). Unit and topic slugs are unchanged: they are unique
per course, and make_units.py kept AB's.

Run make_units.py first. Re-running overwrites the copied files, so edit the AB originals (or this
script), never the copies. The new BC-only items live in separate files (`unit-N-bc.json`) written by
u6_bc.py, u7_bc.py, u8_bc.py, u9_bc.py and u10_bc.py, which this script never touches.
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "../../../content"))
SRC, DST = os.path.join(ROOT, "ap-calc"), os.path.join(ROOT, "ap-calc-bc")
OLD_ID, NEW_ID = "ap-calc-", "ap-calcbc-"
OLD_COURSE, NEW_COURSE = "ap-calc/", "ap-calc-bc/"


def convert(item):
    out = dict(item)
    if "id" in out:
        assert out["id"].startswith(OLD_ID), out["id"]
        out["id"] = NEW_ID + out["id"][len(OLD_ID):]
    if "conceptLink" in out:
        assert out["conceptLink"].startswith(OLD_COURSE), out["conceptLink"]
        out["conceptLink"] = NEW_COURSE + out["conceptLink"][len(OLD_COURSE):]
    out["reviewed"] = False
    return out


def main():
    counts = {}
    for kind in ("questions", "frqs", "refreshers"):
        os.makedirs(os.path.join(DST, kind), exist_ok=True)
        for name in sorted(os.listdir(os.path.join(SRC, kind))):
            with open(os.path.join(SRC, kind, name)) as f:
                items = json.load(f)
            converted = [convert(i) for i in items]
            with open(os.path.join(DST, kind, name), "w") as f:
                json.dump(converted, f, indent=2, ensure_ascii=False)
                f.write("\n")
            counts[kind] = counts.get(kind, 0) + len(converted)
    print(counts)


main()
