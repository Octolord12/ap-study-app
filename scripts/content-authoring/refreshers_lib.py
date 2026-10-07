"""Shared by the per-course refresher authoring folders (ap-calc-refreshers, ap-csa-refreshers, ...).

`write(course, unit_number, entries)` turns a unit's (topic_slug, markdown) pairs into content/<course>/refreshers/unit-N.json,
checking that every topic of the unit has exactly one, in order. Edit the scripts, not the JSON.
"""
import json, os, re

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../content"))


def display_blocks(body):
    """remark-math only makes a centered display equation from $$ on lines of their own; one-line $$...$$ is
    rendered as inline math. Authors write the short form, and this expands it."""
    return re.sub(r"^\$\$(.+)\$\$$", lambda m: "$$\n" + m.group(1).strip() + "\n$$", body, flags=re.M)


def write(course, unit_number, entries):
    unit = json.load(open(f"{ROOT}/{course}/units/unit-{unit_number}.json", encoding="utf-8"))
    slugs = [t["slug"] for t in unit["topics"]]
    assert [slug for slug, _ in entries] == slugs, f"unit {unit_number}: topics {[s for s, _ in entries]} != {slugs}"
    out = [{"unit": unit["slug"], "topic": slug, "body": display_blocks(body.strip()), "reviewed": False} for slug, body in entries]
    os.makedirs(f"{ROOT}/{course}/refreshers", exist_ok=True)
    path = f"{ROOT}/{course}/refreshers/unit-{unit_number}.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"{course} unit {unit_number}: {len(out)} refreshers, {[len(b) for _, b in entries]} characters")
