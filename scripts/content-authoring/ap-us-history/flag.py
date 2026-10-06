import json, glob, sys
u = sys.argv[1]
for p in sorted(glob.glob(f"../../../content/ap-us-history/questions/unit-{u}*.json")):
    for x in json.load(open(p)):
        cs = [(len(c["text"]), c["isCorrect"], c["text"]) for c in x["choices"]]
        cl = [l for l, ok, t in cs if ok][0]
        ws = sorted([(l, t) for l, ok, t in cs if not ok], reverse=True)
        if cl > ws[0][0]:
            print(x["id"].split("-", 2)[2], "C", cl, "| longest wrong", ws[0][0], "|", ws[0][1])
