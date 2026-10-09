"""How often the right answer is uniquely the longest / shortest choice, per course and set, among the questions where length can be a tell.

    python3 stats.py
"""
from lib import *

for course in COURSES:
    for hard in sets(course):
        qs = [q for q in load(course, hard) if is_prose(q)]
        n = len(qs)
        longest = sum(analyze(q)[0] > max(w[0] for w in analyze(q)[1]) for q in qs)
        shortest = sum(strictly_shortest(q) for q in qs)
        chance = sum(1 / len(q["choices"]) for q in qs)
        print(f"{course:13} {'hard' if hard else 'core'} n={n:3d}  right is longest {100*longest/n:4.1f}%  shortest {100*shortest/n:4.1f}%  (chance {100*chance/n:4.1f}%)")
