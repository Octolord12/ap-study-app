import json, glob, statistics, sys
units = sys.argv[1:] or [str(i) for i in range(1, 10)]
q = []
for u in units:
    for p in sorted(glob.glob(f"../../../content/ap-us-history/questions/unit-{u}*.json")):
        q += json.load(open(p))
L = sum(1 for x in q if max(x["choices"], key=lambda c: len(c["text"]))["isCorrect"])
r = [len(next(c for c in x["choices"] if c["isCorrect"])["text"]) / statistics.mean(len(c["text"]) for c in x["choices"] if not c["isCorrect"]) for x in q]
print(f"units {','.join(units)}: {len(q)} questions, correct is longest in {L} ({100 * L / len(q):.0f}%), median ratio {statistics.median(r):.2f}, mean {statistics.mean(r):.2f}")
