"""How often the right answer is uniquely the longest or shortest choice in AP Biology's questions, among the questions where length can be a tell
(the longest choice has at least 30 visible characters). Chance with four choices is 25 percent for each. Aim: longest 20-28 percent, shortest 15-20 percent.

    python3 length_stats.py            # whole course
    python3 length_stats.py 3          # one unit

Unit 3 as first written was longest in 70 percent and shortest in 6 percent (the correct answer carried the qualifying clauses), so write every wrong
choice about as long as the right one while drafting, and run this before moving on. Reuses the measuring helpers of ../answer-length."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "../answer-length"))
from lib import analyze, is_prose, load  # noqa: E402

unit = sys.argv[1] if len(sys.argv) > 1 else None
qs = [q for q in load("ap-biology") if unit is None or f"-u{unit}-" in q["id"]]
prose = [q for q in qs if is_prose(q)]
n = len(prose)
longest = [q for q in prose if analyze(q)[0] > max(w[0] for w in analyze(q)[1])]
shortest = [q for q in prose if all(analyze(q)[0] < w[0] for w in analyze(q)[1])]
chance = sum(1 / len(q["choices"]) for q in prose)
print(f"{len(qs)} questions, {n} where length can be a tell: right is uniquely longest {len(longest)} ({100 * len(longest) / n:.0f}%), shortest {len(shortest)} ({100 * len(shortest) / n:.0f}%), chance {100 * chance / n:.0f}%")
