"""Builds all of Unit 2 (Probability, Random Variables, and Probability Distributions): 110 questions and 8 free-response prompts -> content/ap-statistics/{questions,frqs}/unit-2.json.
Edit the scripts, not the JSON. Run: python3 u2.py"""
import collections

from lib import Bank
import u2_a, u2_b, u2_c, u2_d, u2_frq

B = Bank(2)
for part in (u2_a, u2_b, u2_c, u2_d, u2_frq):
    part.build(B)

per_topic = collections.Counter(q["topic"] for q in B.mcqs)
print({k: v for k, v in sorted(per_topic.items())})
print("difficulty:", dict(collections.Counter(q["difficulty"] for q in B.mcqs)), "| with a diagram:", sum(1 for q in B.mcqs if q.get("diagram")), "of", len(B.mcqs))
print("free response:", dict(collections.Counter(f["type"] for f in B.frqs)))
assert len(B.mcqs) == 110, len(B.mcqs)
assert [per_topic[B.T[i]] for i in range(1, 13)] == [7, 10, 8, 9, 7, 10, 10, 8, 9, 12, 12, 8], per_topic
assert collections.Counter(f["type"] for f in B.frqs) == {"COLLECT_DATA": 1, "ANALYZE_DATA": 5, "MULTI_FOCUS": 2}
assert all(f["pointValue"] == 10 for f in B.frqs)
B.save()
