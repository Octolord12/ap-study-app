"""Builds all of Unit 3 (Cellular Energetics): 60 questions and 6 free-response prompts -> content/ap-biology/{questions,frqs}/unit-3.json.
Edit the scripts, not the JSON. Run: python3 u3.py"""
import collections
import os

from lib import Bank
import u3_enzymes, u3_energy, u3_photo, u3_resp, u3_frq

os.makedirs(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../content/ap-biology/questions"), exist_ok=True)
os.makedirs(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../content/ap-biology/frqs"), exist_ok=True)

B = Bank(3)
for part in (u3_enzymes, u3_energy, u3_photo, u3_resp, u3_frq):
    part.build(B)

per_topic = collections.Counter(q["topic"] for q in B.mcqs)
print({k: v for k, v in sorted(per_topic.items())})
print("difficulty:", dict(collections.Counter(q["difficulty"] for q in B.mcqs)))
print("with a diagram:", sum(1 for q in B.mcqs if q.get("diagram")), "of", len(B.mcqs))
assert len(B.mcqs) == 60, len(B.mcqs)
assert [per_topic[B.T[i]] for i in range(1, 6)] == [12, 14, 10, 12, 12], per_topic
assert len(B.frqs) == 6 and [f["type"] for f in B.frqs] == ["RESULTS", "RESULTS_GRAPH", "INVESTIGATION", "CONCEPT", "MODEL", "DATA"]
B.save()
