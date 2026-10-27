"""Builds all of Unit 4 (Inference for Quantitative Data: Means): 90 questions and 10 free-response prompts -> content/ap-statistics/{questions,frqs}/unit-4.json.
Edit the scripts, not the JSON. Run: python3 u4.py"""
import collections

from lib import Bank
import u4_a, u4_b, u4_c, u4_d, u4_frq

B = Bank(4)
for part in (u4_a, u4_b, u4_c, u4_d, u4_frq):
    part.build(B)

per_topic = collections.Counter(q["topic"] for q in B.mcqs)
print({k: v for k, v in sorted(per_topic.items())})
print("difficulty:", dict(collections.Counter(q["difficulty"] for q in B.mcqs)), "| with a diagram:", sum(1 for q in B.mcqs if q.get("diagram")), "of", len(B.mcqs))
print("free response:", dict(collections.Counter(f["type"] for f in B.frqs)))
assert len(B.mcqs) == 90, len(B.mcqs)
assert [per_topic[B.T[i]] for i in range(1, 11)] == [9, 10, 9, 9, 9, 9, 9, 8, 9, 9], per_topic
assert collections.Counter(f["type"] for f in B.frqs) == {"COLLECT_DATA": 2, "INFERENCE": 6, "MULTI_FOCUS": 2}
assert all(f["pointValue"] == 10 for f in B.frqs)
B.save()
