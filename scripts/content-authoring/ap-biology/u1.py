"""Builds all of Unit 1 (Chemistry of Life): 54 questions and 6 free-response prompts -> content/ap-biology/{questions,frqs}/unit-1.json.
Edit the scripts, not the JSON. Run: python3 u1.py"""
import collections

from lib import Bank
import u1_water, u1_macro, u1_lipid_nuc, u1_protein, u1_frq

B = Bank(1)
for part in (u1_water, u1_macro, u1_lipid_nuc, u1_protein, u1_frq):
    part.build(B)

per_topic = collections.Counter(q["topic"] for q in B.mcqs)
print({k: v for k, v in sorted(per_topic.items())})
print("difficulty:", dict(collections.Counter(q["difficulty"] for q in B.mcqs)), "| with a diagram:", sum(1 for q in B.mcqs if q.get("diagram")), "of", len(B.mcqs))
assert len(B.mcqs) == 54, len(B.mcqs)
assert [per_topic[B.T[i]] for i in range(1, 8)] == [9, 6, 8, 7, 8, 8, 8], per_topic
assert [f["type"] for f in B.frqs] == ["RESULTS", "RESULTS_GRAPH", "INVESTIGATION", "CONCEPT", "MODEL", "DATA"]
B.save()
