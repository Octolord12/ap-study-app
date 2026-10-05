"""Authoring helpers for the hard Calc AB set. Every number in a stem, choice or
explanation is produced by sympy from the same objects the answer is computed from."""
import json, random, re, itertools
from sympy import *

x, y, t, h, a, b, c, k, u = symbols("x y t h a b c k u", real=True)

import os
ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../content/ap-calc"))
COURSE = "ap-calc"


def L(e):
    """Sympy object (or plain string) -> LaTeX, no dollar signs."""
    if isinstance(e, str):
        return e
    s = latex(e, ln_notation=True)
    s = s.replace(r"\operatorname{atan}", r"\arctan").replace(r"\operatorname{asin}", r"\arcsin").replace(r"\operatorname{acos}", r"\arccos")
    s = s.replace(r"\left(", r"\left(").replace("\\,", " ")
    return s


def M(e):
    return "$" + L(e) + "$"


def fmt(template, **kw):
    out = template
    for key, val in kw.items():
        out = out.replace("[[" + key + "]]", val if isinstance(val, str) and val.startswith("$") else M(val))
    assert "[[" not in out, out
    return out


def ch(text, expl, val=None):
    """A choice. `text` may be a sympy object (shown as math) or a string (shown as given)."""
    shown = M(text) if not isinstance(text, str) else text
    return {"text": shown, "expl": expl, "val": val if val is not None else (text if not isinstance(text, str) else None)}


def same(p, q):
    try:
        return simplify(p - q) == 0
    except Exception:
        return False


class Bank:
    def __init__(self, unit_num, unit_slug):
        self.n = unit_num
        self.unit = unit_slug
        self.mcqs, self.frqs = [], []

    def mcq(self, topic, stem, correct, wrongs, explanation, diagram=None):
        assert 3 <= len(wrongs) <= 4, "need 3 or 4 wrong choices"
        allc = [dict(correct, ok=True)] + [dict(w, ok=False) for w in wrongs]
        texts = [c_["text"] for c_ in allc]
        assert len(set(texts)) == len(texts), f"duplicate choice text in {stem[:60]}: {texts}"
        vals = [c_["val"] for c_ in allc]
        if all(v is not None for v in vals):
            for i, j in itertools.combinations(range(len(vals)), 2):
                assert not same(vals[i], vals[j]), f"choices {i} and {j} are equal in {stem[:60]}"
        for c_ in allc:
            assert c_["expl"].strip(), "empty explanation"
        idx = len(self.mcqs) + 1
        qid = f"{COURSE}-u{self.n}-mcq-{30 + idx}"
        rng = random.Random(qid)
        order = list(range(len(allc)))
        rng.shuffle(order)
        labels = "ABCDE"
        choices = []
        for pos, i in enumerate(order):
            c_ = allc[i]
            choices.append({"label": labels[pos], "text": c_["text"], "isCorrect": c_["ok"], "explanation": c_["expl"]})
        q = {
            "id": qid,
            "unit": self.unit,
            "topic": topic,
            "difficulty": "hard",
            "stem": stem,
            "choices": choices,
            "explanation": explanation,
            "conceptLink": f"{COURSE}/{self.unit}/{topic}",
            "reviewed": False,
        }
        if diagram:
            q["diagram"] = diagram
        self.mcqs.append(q)

    def frq(self, topic, prompt, rubric, sample, diagram=None):
        idx = len(self.frqs) + 1
        pts = sum(p for p, _ in rubric)
        f = {
            "id": f"{COURSE}-u{self.n}-frq-{3 + idx}",
            "unit": self.unit,
            "topic": topic,
            "prompt": prompt,
            "pointValue": pts,
            "rubric": [{"id": f"r{i + 1}", "points": p, "description": d} for i, (p, d) in enumerate(rubric)],
            "sampleResponse": sample,
            "reviewed": False,
        }
        if diagram:
            f["diagram"] = diagram
        self.frqs.append(f)

    def save(self):
        with open(f"{ROOT}/questions/unit-{self.n}-hard.json", "w") as fh:
            json.dump(self.mcqs, fh, indent=2, ensure_ascii=False)
            fh.write("\n")
        with open(f"{ROOT}/frqs/unit-{self.n}-hard.json", "w") as fh:
            json.dump(self.frqs, fh, indent=2, ensure_ascii=False)
            fh.write("\n")
        print(f"unit {self.n}: wrote {len(self.mcqs)} MCQs and {len(self.frqs)} FRQs")

    def show(self):
        for q in self.mcqs:
            print("\n" + q["id"], "|", q["topic"])
            print("  Q:", q["stem"])
            for c_ in q["choices"]:
                print("   ", c_["label"], "*" if c_["isCorrect"] else " ", c_["text"])
        for f in self.frqs:
            print("\n" + f["id"], f["pointValue"], "pts |", f["topic"])
            print(f["prompt"])


def LIM(e, point, direction="", var="x"):
    pt = L(point)
    sign = {"+": "^{+}", "-": "^{-}", "": ""}[direction]
    return r"\lim_{" + var + r" \to " + pt + sign + "} " + L(e)


def graph(xLabel, yLabel, xMin, xMax, yMin, yMax, series, altText):
    return {"type": "xy-graph", "altText": altText, "xLabel": xLabel, "yLabel": yLabel, "xMin": xMin, "xMax": xMax, "yMin": yMin, "yMax": yMax, "series": series}
