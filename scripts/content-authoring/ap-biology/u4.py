"""Builds all of Unit 4 (Cell Communication and Cell Cycle): 61 questions and 6 free-response prompts -> content/ap-biology/{questions,frqs}/unit-4.json.
Edit the scripts, not the JSON. Run: python3 u4.py"""
import collections

from lib import Bank
import u4_comm, u4_cycle, u4_frq

B = Bank(4)
for part in (u4_comm, u4_cycle, u4_frq):
    part.build(B)

per_topic = collections.Counter(q["topic"] for q in B.mcqs)
print({k: v for k, v in sorted(per_topic.items())})
print("difficulty:", dict(collections.Counter(q["difficulty"] for q in B.mcqs)), "| with a diagram:", sum(1 for q in B.mcqs if q.get("diagram")), "of", len(B.mcqs))
assert len(B.mcqs) == 61, len(B.mcqs)
assert [per_topic[B.T[i]] for i in range(1, 7)] == [8, 11, 10, 9, 13, 10], per_topic
assert [f["type"] for f in B.frqs] == ["RESULTS", "RESULTS_GRAPH", "INVESTIGATION", "CONCEPT", "MODEL", "DATA"]
B.save()
