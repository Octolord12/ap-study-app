"""Builds all of Unit 8 (Ecology): 66 questions and 6 free-response prompts -> content/ap-biology/{questions,frqs}/unit-8.json.
Edit the scripts, not the JSON. Run: python3 u8.py"""
import collections

from lib import Bank
import u8_org, u8_pop, u8_comm, u8_frq

B = Bank(8)
for part in (u8_org, u8_pop, u8_comm, u8_frq):
    part.build(B)

per_topic = collections.Counter(q["topic"] for q in B.mcqs)
print({k: v for k, v in sorted(per_topic.items())})
print("difficulty:", dict(collections.Counter(q["difficulty"] for q in B.mcqs)), "| with a diagram:", sum(1 for q in B.mcqs if q.get("diagram")), "of", len(B.mcqs))
assert len(B.mcqs) == 66, len(B.mcqs)
assert [per_topic[B.T[i]] for i in range(1, 8)] == [9, 14, 9, 8, 10, 7, 9], per_topic
assert [f["type"] for f in B.frqs] == ["RESULTS", "RESULTS_GRAPH", "INVESTIGATION", "CONCEPT", "MODEL", "DATA"]
B.save()
