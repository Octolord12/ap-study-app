"""Builds all of Unit 5 (Regression Analysis): 60 questions and 6 free-response prompts -> content/ap-statistics/{questions,frqs}/unit-5.json.
Edit the scripts, not the JSON. Run: python3 u5.py"""
import collections

from lib import Bank
import u5_scatter, u5_corr, u5_model, u5_resid, u5_lsrl, u5_frq

B = Bank(5)
for part in (u5_scatter, u5_corr, u5_model, u5_resid, u5_lsrl, u5_frq):
    part.build(B)

per_topic = collections.Counter(q["topic"] for q in B.mcqs)
print({k: v for k, v in sorted(per_topic.items())})
print("difficulty:", dict(collections.Counter(q["difficulty"] for q in B.mcqs)), "| with a diagram:", sum(1 for q in B.mcqs if q.get("diagram")), "of", len(B.mcqs))
assert len(B.mcqs) == 60, len(B.mcqs)
assert [per_topic[B.T[i]] for i in range(1, 6)] == [12, 12, 12, 12, 12], per_topic
assert [f["type"] for f in B.frqs] == ["ANALYZE_DATA"] * 3 + ["MULTI_FOCUS"] * 3
assert all(f["pointValue"] == 10 for f in B.frqs)
B.save()
