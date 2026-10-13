"""Builds all of Unit 5 (Heredity): 50 questions and 6 free-response prompts -> content/ap-biology/{questions,frqs}/unit-5.json.
Edit the scripts, not the JSON. Run: python3 u5.py"""
import collections

from lib import Bank
import u5_meiosis, u5_mendel, u5_nonmendel, u5_environment, u5_frq

B = Bank(5)
for part in (u5_meiosis, u5_mendel, u5_nonmendel, u5_environment, u5_frq):
    part.build(B)

per_topic = collections.Counter(q["topic"] for q in B.mcqs)
print({k: v for k, v in sorted(per_topic.items())})
print("difficulty:", dict(collections.Counter(q["difficulty"] for q in B.mcqs)), "| with a diagram:", sum(1 for q in B.mcqs if q.get("diagram")), "of", len(B.mcqs))
assert len(B.mcqs) == 50, len(B.mcqs)
assert [per_topic[B.T[i]] for i in range(1, 6)] == [10, 9, 12, 12, 7], per_topic
assert [f["type"] for f in B.frqs] == ["RESULTS", "RESULTS_GRAPH", "INVESTIGATION", "CONCEPT", "MODEL", "DATA"]
B.save()
