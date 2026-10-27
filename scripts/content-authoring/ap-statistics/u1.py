"""Builds all of Unit 1 (Exploring One-Variable Data): 121 questions and 14 free-response prompts -> content/ap-statistics/{questions,frqs}/unit-1.json.
Edit the scripts, not the JSON. Run: python3 u1.py"""
import collections

from lib import Bank
import u1_a, u1_b, u1_c, u1_d, u1_e, u1_frq_a, u1_frq_b

B = Bank(1)
for part in (u1_a, u1_b, u1_c, u1_d, u1_e, u1_frq_a, u1_frq_b):
    part.build(B)

per_topic = collections.Counter(q["topic"] for q in B.mcqs)
print({k: v for k, v in sorted(per_topic.items())})
print("difficulty:", dict(collections.Counter(q["difficulty"] for q in B.mcqs)), "| with a diagram:", sum(1 for q in B.mcqs if q.get("diagram")), "of", len(B.mcqs))
print("free response:", dict(collections.Counter(f["type"] for f in B.frqs)))
assert len(B.mcqs) == 121, len(B.mcqs)
assert len(B.frqs) == 14, len(B.frqs)
assert collections.Counter(f["type"] for f in B.frqs) == {"COLLECT_DATA": 8, "ANALYZE_DATA": 4, "MULTI_FOCUS": 2}
assert all(f["pointValue"] == 10 for f in B.frqs)
B.save()
