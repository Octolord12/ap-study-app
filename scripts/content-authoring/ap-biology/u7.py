"""Builds all of Unit 7 (Natural Selection): 100 questions and 6 free-response prompts -> content/ap-biology/{questions,frqs}/unit-7.json.
Edit the scripts, not the JSON. Run: python3 u7.py"""
import collections

from lib import Bank
import u7_sel, u7_pop, u7_evid, u7_phylo, u7_var, u7_frq

B = Bank(7)
for part in (u7_sel, u7_pop, u7_evid, u7_phylo, u7_var, u7_frq):
    part.build(B)

per_topic = collections.Counter(q["topic"] for q in B.mcqs)
print({k: v for k, v in sorted(per_topic.items())})
print("difficulty:", dict(collections.Counter(q["difficulty"] for q in B.mcqs)), "| with a diagram:", sum(1 for q in B.mcqs if q.get("diagram")), "of", len(B.mcqs))
assert len(B.mcqs) == 100, len(B.mcqs)
assert [per_topic[B.T[i]] for i in range(1, 13)] == [8, 9, 6, 10, 10, 9, 6, 8, 10, 10, 7, 7], per_topic
assert [f["type"] for f in B.frqs] == ["RESULTS", "RESULTS_GRAPH", "INVESTIGATION", "CONCEPT", "MODEL", "DATA"]
B.save()
