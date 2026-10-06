"""Second-pass helper: appends a short clause to a question's longest wrong choice (before a final period, if any), so the
right answer stops being the longest, and records it in that unit's PADW so apply.py reproduces it.

    python3 extend_longest.py ap-calc 7 '{"13": ", since the signed areas add up"}'
    python3 extend_longest.py ap-calc 7 '{"13": " ..."}' shortest
"""
import importlib, json, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import HERE, load_core, qid, vis

course, unit, edits = sys.argv[1], int(sys.argv[2]), json.loads(sys.argv[3])
pick = min if "shortest" in sys.argv[4:] else max   # "shortest": lengthen the shortest wrong choice (to stop the right one being never the shortest)
questions = {q["id"]: q for q in load_core(course, unit)}
sys.path.insert(0, os.path.join(HERE, course))
modname = f"pad_u{unit}"
padw = dict(importlib.import_module(modname).PADW) if os.path.exists(os.path.join(HERE, course, modname + ".py")) else {}
for num, clause in edits.items():
    q = questions[qid(course, unit, num)]
    longest = pick((c["text"] for c in q["choices"] if not c["isCorrect"]), key=vis)
    padw[longest] = longest[:-1] + clause + "." if longest.endswith(".") else longest + clause
path = os.path.join(HERE, course, modname + ".py")
src = open(path, encoding="utf-8").read() if os.path.exists(path) else f'P = "{qid(course, unit, "")}"\n\nPAD = {{}}\nPADC = {{}}\n'
cut = src.find("PADW = {")
if cut != -1:
    src = src[:cut]
src = src.rstrip("\n") + "\n\nPADW = {\n" + "".join(f"    {json.dumps(k, ensure_ascii=False)}: {json.dumps(v, ensure_ascii=False)},\n" for k, v in padw.items()) + "}\n"
open(path, "w", encoding="utf-8").write(src)
