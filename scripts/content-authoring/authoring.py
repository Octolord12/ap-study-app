"""Course-independent authoring helpers (the Calc AB scripts use their own sympy-based lib.py).

A script builds a Bank for one unit, adds MCQs and FRQs, and saves two JSON files into
content/<course>/{questions,frqs}/unit-N-hard.json. Every distractor is a named mistake, and
`mcq` refuses duplicate choice text or numerically equal choices."""
import itertools, json, math, os, random

CONTENT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../content"))


def sig(v, n=3):
    """Format with n significant figures, no exponent, trailing zeros kept only if needed."""
    if v == 0:
        return "0"
    s = f"{v:.{n}g}"
    if "e" in s:
        s = f"{float(s):f}".rstrip("0").rstrip(".")
    return s


def ch(text, expl, val=None):
    return {"text": text, "expl": expl, "val": val}


def graph(xLabel, yLabel, xMin, xMax, yMin, yMax, series, altText):
    return {"type": "xy-graph", "altText": altText, "xLabel": xLabel, "yLabel": yLabel, "xMin": xMin, "xMax": xMax, "yMin": yMin, "yMax": yMax, "series": series}


def force_diagram(vectors, altText, objectLabel=None, incline=None):
    d = {"type": "force-diagram", "altText": altText, "vectors": vectors}
    if objectLabel:
        d["objectLabel"] = objectLabel
    if incline is not None:
        d["inclineAngleDegrees"] = incline
    return d


class Bank:
    def __init__(self, course, id_prefix, unit_num, unit_slug, mcq_start=31, frq_start=4, suffix="-hard"):
        self.course, self.prefix, self.n, self.unit = course, id_prefix, unit_num, unit_slug
        self.suffix = suffix
        self.mcq_start, self.frq_start = mcq_start, frq_start
        self.mcqs, self.frqs = [], []

    def mcq(self, topic, stem, correct, wrongs, explanation, diagram=None, difficulty="hard"):
        assert 3 <= len(wrongs) <= 4, f"need 3 or 4 wrong choices: {stem[:50]}"
        allc = [dict(correct, ok=True)] + [dict(w, ok=False) for w in wrongs]
        texts = [c["text"] for c in allc]
        assert len(set(texts)) == len(texts), f"duplicate choice text in {stem[:60]}: {texts}"
        vals = [c["val"] for c in allc]
        if all(isinstance(v, (int, float)) for v in vals):
            for i, j in itertools.combinations(range(len(vals)), 2):
                assert abs(vals[i] - vals[j]) > 1e-9 * max(1, abs(vals[i])), f"choices {i},{j} equal in {stem[:60]}"
        for c in allc:
            assert c["expl"].strip(), "empty explanation"
        qid = f"{self.prefix}-u{self.n}-mcq-{self.mcq_start - 1 + len(self.mcqs) + 1}"
        order = list(range(len(allc)))
        random.Random(qid).shuffle(order)
        choices = [{"label": "ABCDE"[pos], "text": allc[i]["text"], "isCorrect": allc[i]["ok"], "explanation": allc[i]["expl"]} for pos, i in enumerate(order)]
        q = {"id": qid, "unit": self.unit, "topic": topic, "difficulty": difficulty, "stem": stem, "choices": choices,
             "explanation": explanation, "conceptLink": f"{self.course}/{self.unit}/{topic}", "reviewed": False}
        if diagram:
            q["diagram"] = diagram
        self.mcqs.append(q)

    def frq(self, topic, prompt, rubric, sample, diagram=None, ftype=None):
        """ftype: SAQ, DBQ or LEQ for a course whose exam has those sections; leave None for a plain FRQ."""
        fid = f"{self.prefix}-u{self.n}-frq-{self.frq_start + len(self.frqs)}"
        f = {"id": fid, "unit": self.unit, "topic": topic}
        if ftype:
            f["type"] = ftype
        f.update({"prompt": prompt, "pointValue": sum(p for p, _ in rubric),
             "rubric": [{"id": f"r{i + 1}", "points": p, "description": d} for i, (p, d) in enumerate(rubric)],
             "sampleResponse": sample, "reviewed": False})
        if diagram:
            f["diagram"] = diagram
        self.frqs.append(f)

    def save(self):
        base = os.path.join(CONTENT, self.course)
        with open(os.path.join(base, "questions", f"unit-{self.n}{self.suffix}.json"), "w") as fh:
            json.dump(self.mcqs, fh, indent=2, ensure_ascii=False)
            fh.write("\n")
        with open(os.path.join(base, "frqs", f"unit-{self.n}{self.suffix}.json"), "w") as fh:
            json.dump(self.frqs, fh, indent=2, ensure_ascii=False)
            fh.write("\n")
        print(f"{self.course} unit {self.n}: wrote {len(self.mcqs)} MCQs and {len(self.frqs)} FRQs")

    def brief(self):
        for q in self.mcqs:
            right = next(c["text"] for c in q["choices"] if c["isCorrect"])
            print(f'{q["id"].split("-")[-3]}-{q["id"].split("-")[-1]} {q["topic"][:22]:22} | {q["stem"][:90]!r} -> {right[:50]}')
        for f in self.frqs:
            print(f'{f["id"]} {f["pointValue"]}pts {f["topic"]}: {f["prompt"][:80]!r}')

    def show(self):
        for q in self.mcqs:
            print("\n" + q["id"], "|", q["topic"])
            print("  Q:", q["stem"])
            for c in q["choices"]:
                print("   ", c["label"], "*" if c["isCorrect"] else " ", c["text"])
        for f in self.frqs:
            print("\n" + f["id"], f["pointValue"], "pts |", f["topic"])
            print(f["prompt"])
