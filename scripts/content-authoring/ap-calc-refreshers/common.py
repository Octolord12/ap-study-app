"""Writes content/ap-calc/refreshers/unit-N.json from the u1.py..u8.py scripts in this folder.

Each script holds one refresher per topic (markdown, KaTeX in $...$) and re-checks its worked examples with sympy
before writing, so a number in the text cannot drift from the maths. Edit the scripts, not the JSON.
Layout of every refresher: ### The idea, ### Key facts, ### Watch out for, ### Worked example.
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
CONTENT = os.path.normpath(os.path.join(HERE, "../../../content/ap-calc"))


def write(unit_number, entries):
    """entries: list of (topic_slug, markdown body). Every topic of the unit needs exactly one."""
    unit = json.load(open(f"{CONTENT}/units/unit-{unit_number}.json", encoding="utf-8"))
    slugs = [t["slug"] for t in unit["topics"]]
    assert [slug for slug, _ in entries] == slugs, f"unit {unit_number}: topics {[s for s, _ in entries]} != {slugs}"
    out = [{"unit": unit["slug"], "topic": slug, "body": body.strip(), "reviewed": False} for slug, body in entries]
    os.makedirs(f"{CONTENT}/refreshers", exist_ok=True)
    path = f"{CONTENT}/refreshers/unit-{unit_number}.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"unit {unit_number}: {len(out)} refreshers, {[len(b) for _, b in entries]} characters")
