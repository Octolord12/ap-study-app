"""Authoring helpers for AP Biology. Built on ../authoring.py (the course-independent Bank).

Every number in a stem, table, choice or explanation is computed here from the same variables the answer comes from
(means, SE, rates, percent changes), and `Bank.mcq` refuses duplicate or numerically equal choices. What is NOT checked by
any script is the biology in the sentences (what a structure does, which way protons flow, why a distractor is wrong):
that is proofread against the CED's essential-knowledge statements, and the owner's review is the real check.

Style rules (shared with the other non-math courses): no em dashes; no lone dollar sign (the validator reads it as unclosed
math); no single-asterisk italics; never refer to a choice by letter; write chemical formulas with Unicode subscripts
(CO₂, H₂O, O₂, NADP⁺) and equations in $...$.
"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import authoring
from authoring import ch, sig, graph  # noqa: F401  (re-exported for the unit scripts)

COURSE = "ap-biology"
PREFIX = "ap-bio"

# The six free-response kinds and the points each is worth (CED Exam Overview).
KIND_POINTS = {"RESULTS": 9, "RESULTS_GRAPH": 9, "INVESTIGATION": 4, "CONCEPT": 4, "MODEL": 4, "DATA": 4}


def unit_slug(n):
    import json
    with open(os.path.join(authoring.CONTENT, COURSE, "units", f"unit-{n}.json"), encoding="utf-8") as f:
        return json.load(f)["slug"]


def topic_slugs(n):
    """The unit's topic slugs in CED order, so a script can say T[1] for topic n.1."""
    import json
    with open(os.path.join(authoring.CONTENT, COURSE, "units", f"unit-{n}.json"), encoding="utf-8") as f:
        return {t["order"]: t["slug"] for t in json.load(f)["topics"]}


class Bank(authoring.Bank):
    """One unit's questions and free-response prompts, written to unit-N.json. Ids are ap-bio-uN-mcq-1.. and ap-bio-uN-frq-1.."""

    def __init__(self, unit_num):
        super().__init__(COURSE, PREFIX, unit_num, unit_slug(unit_num), mcq_start=1, frq_start=1, suffix="")
        self.T = topic_slugs(unit_num)

    def mcq(self, topic_number, stem, correct, wrongs, explanation, diagram=None, difficulty="medium"):
        assert difficulty in ("easy", "medium", "hard"), difficulty
        for c_ in [correct] + list(wrongs):
            assert "—" not in c_["text"] + c_["expl"], "em dash"
        assert "—" not in stem + explanation, "em dash"
        super().mcq(self.T[topic_number], stem, correct, list(wrongs), explanation, diagram=diagram, difficulty=difficulty)

    def frq(self, topic_number, kind, prompt, rubric, sample, diagram=None):
        """rubric: one (1, description) line per point, in order. The total must be the kind's size (9, 9, 4, 4, 4, 4)."""
        assert kind in KIND_POINTS, kind
        assert all(p == 1 for p, _ in rubric), "rubric lines are one point each"
        assert sum(p for p, _ in rubric) == KIND_POINTS[kind], f"{kind} is worth {KIND_POINTS[kind]}, rubric has {sum(p for p, _ in rubric)}"
        assert "—" not in prompt + sample + "".join(d for _, d in rubric), "em dash"
        super().frq(self.T[topic_number], prompt, rubric, sample, diagram=diagram, ftype=kind)


# ---- numbers -------------------------------------------------------------------------------------------------------

def mean(xs):
    return sum(xs) / len(xs)


def sd(xs):
    """Sample standard deviation (n - 1), as on the AP equation sheet."""
    m = mean(xs)
    return math.sqrt(sum((x - m) ** 2 for x in xs) / (len(xs) - 1))


def se(xs):
    """Standard error of the mean: s / sqrt(n)."""
    return sd(xs) / math.sqrt(len(xs))


def fix(v, places=1):
    """Fixed number of places, as the table or answer should print it (so 2.0 stays 2.0)."""
    return f"{v:.{places}f}"


def pct_change(old, new):
    return (new - old) / old * 100


# ---- diagrams ------------------------------------------------------------------------------------------------------

def table(columns, rows, caption=None, row_headers=False):
    """A data-table diagram. Cells are written as strings so a trailing zero is kept ("2.0")."""
    d = {"type": "data-table", "columns": list(columns), "rows": [[c_ if isinstance(c_, str) else str(c_) for c_ in r] for r in rows], "rowHeaders": row_headers}
    if caption:
        d["caption"] = caption
    for r in d["rows"]:
        assert len(r) == len(d["columns"]), f"row {r} does not match columns {d['columns']}"
    return d


def bars(x_label, y_label, y_max, categories, series, y_min=0, alt=None):
    """A bar-graph diagram. `series` is a list of dicts: {values, errors?, label?, color?}."""
    s_out = []
    for s in series:
        o = {"values": [round(v, 3) for v in s["values"]], "color": s.get("color", "blue")}
        if "errors" in s:
            o["errors"] = [round(e, 3) for e in s["errors"]]
        if "label" in s:
            o["label"] = s["label"]
        s_out.append(o)
    d = {"type": "bar-graph", "xLabel": x_label, "yLabel": y_label, "yMin": y_min, "yMax": y_max, "categories": list(categories), "series": s_out}
    if alt:
        d["altText"] = alt
    return d


def tree(root, alt=None):
    d = {"type": "cladogram", "root": root}
    if alt:
        d["altText"] = alt
    return d


def line(label, points, color="blue"):
    """One series for authoring.graph (a piecewise-linear line)."""
    return {"label": label, "points": [{"x": x, "y": y} for x, y in points], "color": color}
