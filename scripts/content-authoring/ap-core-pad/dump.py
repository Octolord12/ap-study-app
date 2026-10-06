"""Prints the questions of a unit where length is a usable tell, wrong choices in file order with lengths.

    python3 dump.py ap-calc 3        # only the questions still showing the tell (what an overlay still has to fix)
    python3 dump.py ap-calc 3 all    # every question of the unit
"""
import sys, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import load_core, tell_questions, vis

course, unit = sys.argv[1], int(sys.argv[2])
qs = load_core(course, unit)
if "all" not in sys.argv[3:]:
    qs = tell_questions(qs)
for q in qs:
    n = q["id"].rsplit("-", 1)[1]
    print(f"{n} [{q['difficulty'][0]}] {q['stem'][:150].replace(chr(10), ' ')}")
    for c in q["choices"]:
        print(f"   {'C' if c['isCorrect'] else 'w'}{vis(c['text'])}: {c['text'].replace(chr(10), chr(92) + 'n')}")
    print()
print(f"-- {len(qs)} questions")
