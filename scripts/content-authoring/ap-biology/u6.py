"""Builds all of Unit 6 (Gene Expression and Regulation): 70 questions and 6 free-response prompts -> content/ap-biology/{questions,frqs}/unit-6.json.
Edit the scripts, not the JSON. Run: python3 u6.py"""
import collections

from lib import Bank
import u6_dna, u6_expr, u6_reg, u6_mut, u6_frq

B = Bank(6)
for part in (u6_dna, u6_expr, u6_reg, u6_mut, u6_frq):
    part.build(B)

per_topic = collections.Counter(q["topic"] for q in B.mcqs)
print({k: v for k, v in sorted(per_topic.items())})
print("difficulty:", dict(collections.Counter(q["difficulty"] for q in B.mcqs)), "| with a diagram:", sum(1 for q in B.mcqs if q.get("diagram")), "of", len(B.mcqs))
assert len(B.mcqs) == 70, len(B.mcqs)
assert [per_topic[B.T[i]] for i in range(1, 9)] == [8, 9, 9, 10, 9, 8, 10, 7], per_topic
assert [f["type"] for f in B.frqs] == ["RESULTS", "RESULTS_GRAPH", "INVESTIGATION", "CONCEPT", "MODEL", "DATA"]
B.save()
