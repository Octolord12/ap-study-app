"""How often the right answer is the longest / shortest choice in a course's core questions.

    python3 stats.py ap-calc [units...]      # prints all questions and the prose-choice subset (longest choice >= 30 chars)
"""
import statistics, sys, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import load_core, units_from_args, vis

course = sys.argv[1]
units = units_from_args(course, sys.argv[2:])


def measure(qs):
    longest = shortest = 0
    ratios = []
    for q in qs:
        cor = vis(next(c["text"] for c in q["choices"] if c["isCorrect"]))
        wr = [vis(c["text"]) for c in q["choices"] if not c["isCorrect"]]
        longest += cor > max(wr)
        shortest += cor < min(wr)
        ratios.append(cor / max(1, statistics.median(wr)))
    n = len(qs)
    return f"{n} questions, correct longest in {longest} ({100 * longest // max(n, 1)}%), shortest in {shortest} ({100 * shortest // max(n, 1)}%), median ratio {statistics.median(ratios):.2f}"


allq = [q for u in units for q in load_core(course, u)]
prose = [q for q in allq if max(vis(c["text"]) for c in q["choices"]) >= 30]
print(f"{course} units {','.join(map(str, units))}")
print("  all:  ", measure(allq))
print("  prose:", measure(prose))
