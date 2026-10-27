"""Builds all of Unit 3 (Inference for Categorical Data: Proportions): 121 questions and 9 free-response prompts -> content/ap-statistics/{questions,frqs}/unit-3.json.
Edit the scripts, not the JSON. Run: python3 u3.py"""
import collections

from lib import Bank
import u3_a, u3_b, u3_c, u3_d, u3_frq

B = Bank(3)
for part in (u3_a, u3_b, u3_c, u3_d, u3_frq):
    part.build(B)

per_topic = collections.Counter(q["topic"] for q in B.mcqs)
print({k: v for k, v in sorted(per_topic.items())})
print("difficulty:", dict(collections.Counter(q["difficulty"] for q in B.mcqs)), "| with a diagram:", sum(1 for q in B.mcqs if q.get("diagram")), "of", len(B.mcqs))
print("free response:", dict(collections.Counter(f["type"] for f in B.frqs)))
assert len(B.mcqs) == 121, len(B.mcqs)
assert [per_topic[B.T[i]] for i in range(1, 16)] == [6, 9, 9, 8, 8, 7, 9, 8, 7, 8, 7, 7, 8, 10, 10], per_topic
assert collections.Counter(f["type"] for f in B.frqs) == {"COLLECT_DATA": 1, "INFERENCE": 6, "MULTI_FOCUS": 2}
assert all(f["pointValue"] == 10 for f in B.frqs)
B.save()
