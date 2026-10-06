"""Second-pass helper: lengthens the longest wrong choice of a question by a short clause, so the right answer stops being
the longest, and records it in that unit's PADW (so `apply.py` reproduces it). Used while balancing; not needed afterwards.

    python3 extend_longest.py 3 '{"31": ", which opened the gates to the sultan's army"}'
"""
import importlib, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "../../../content/ap-world/questions"))
sys.path.insert(0, HERE)


def load(unit):
    out = {}
    for suffix in ("", "-hard"):
        for q in json.load(open(f"{ROOT}/unit-{unit}{suffix}.json", encoding="utf-8")):
            out[q["id"]] = q
    return out


def main():
    unit, edits = int(sys.argv[1]), json.loads(sys.argv[2])
    questions = load(unit)
    mod = importlib.import_module(f"pad_u{unit}")
    padw = dict(getattr(mod, "PADW", {}))
    for num, clause in edits.items():
        q = questions[f"ap-world-u{unit}-mcq-{num}"]
        wrongs = [c["text"] for c in q["choices"] if not c["isCorrect"]]
        longest = max(wrongs, key=len)
        new = longest[:-1] + clause + "." if longest.endswith(".") else longest + clause
        padw[longest] = new
    path = os.path.join(HERE, f"pad_u{unit}.py")
    src = open(path, encoding="utf-8").read()
    cut = src.find("PADW = {")
    if cut != -1:
        src = src[:cut]
    src = src.rstrip("\n") + "\n\nPADW = {\n" + "".join(f"    {json.dumps(k, ensure_ascii=False)}: {json.dumps(v, ensure_ascii=False)},\n" for k, v in padw.items()) + "}\n"
    open(path, "w", encoding="utf-8").write(src)


main()
