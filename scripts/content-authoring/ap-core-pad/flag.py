"""Lists the questions of a course where the right answer is still strictly the longest, with its longest wrong choice.

    python3 flag.py ap-calc 7
"""
import sys, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import load_core, tell_questions, units_from_args, vis

course = sys.argv[1]
for u in units_from_args(course, sys.argv[2:]):
    for q in tell_questions(load_core(course, u)):
        n = q["id"].rsplit("-", 1)[1]
        cor = vis(next(c["text"] for c in q["choices"] if c["isCorrect"]))
        wrong = max((c["text"] for c in q["choices"] if not c["isCorrect"]), key=vis)
        print(f"u{u}-{n} C {cor} | longest wrong {vis(wrong)} | {wrong}")
