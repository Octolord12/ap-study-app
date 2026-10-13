"""Builds all of Unit 2 (Cells): 81 questions and 6 free-response prompts -> content/ap-biology/{questions,frqs}/unit-2.json.
Edit the scripts, not the JSON. Run: python3 u2.py"""
import collections

from lib import Bank
import u2_cells, u2_membrane, u2_transport, u2_compart, u2_frq

B = Bank(2)
for part in (u2_cells, u2_membrane, u2_transport, u2_compart, u2_frq):
    part.build(B)

per_topic = collections.Counter(q["topic"] for q in B.mcqs)
print({k: v for k, v in sorted(per_topic.items())})
print("difficulty:", dict(collections.Counter(q["difficulty"] for q in B.mcqs)), "| with a diagram:", sum(1 for q in B.mcqs if q.get("diagram")), "of", len(B.mcqs))
assert len(B.mcqs) == 81, len(B.mcqs)
assert [per_topic[B.T[i]] for i in range(1, 11)] == [12, 8, 8, 8, 8, 8, 12, 6, 6, 5], per_topic
assert [f["type"] for f in B.frqs] == ["RESULTS", "RESULTS_GRAPH", "INVESTIGATION", "CONCEPT", "MODEL", "DATA"]
B.save()
