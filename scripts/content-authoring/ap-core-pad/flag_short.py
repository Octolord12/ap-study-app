"""Questions where the right answer is not the shortest but the shortest wrong choice is within `margin` characters of it
(candidates for making the right answer the shortest now and then; the ideal share is about a quarter).

    python3 flag_short.py ap-calc 3 [margin]
"""
import sys, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import load_core, units_from_args, vis

course = sys.argv[1]
args = [a for a in sys.argv[2:] if not a.isdigit() or int(a) <= 12]
margin = 14
for u in units_from_args(course, [a for a in sys.argv[2:] if a.isdigit() and int(a) <= 12][:1] or None):
    for q in load_core(course, u):
        cs = q["choices"]
        cor = vis(next(c["text"] for c in cs if c["isCorrect"]))
        wr = sorted((c for c in cs if not c["isCorrect"]), key=lambda c: vis(c["text"]))
        if max(vis(c["text"]) for c in cs) < 30:
            continue
        if cor > vis(wr[0]["text"]) and cor - vis(wr[0]["text"]) <= margin and cor <= max(vis(c["text"]) for c in wr):
            print(f"u{u}-{q['id'].rsplit('-', 1)[1]} C {cor} | shortest wrong {vis(wr[0]['text'])} | {wr[0]['text']}")
