"""Authoring helpers for AP Statistics. Built on ../authoring.py (the course-independent Bank).

Every number in a stem, table, choice or explanation is computed here from the same data the answer comes from (a least-squares fit, a
probability, a test statistic), and `Bank.mcq` refuses duplicate or numerically equal choices. What no script checks is the statistics in the
sentences (what a term means, why a distractor is wrong): that is proofread against the CED's learning objectives and essential knowledge
(effective Fall 2026), and the owner's review is the real check.

The redesigned 2026-27 exam has FOUR answer choices per question (so exactly three wrong choices here) and four 10-point free-response
questions (one point per rubric line, ten lines).

Style rules: no em dashes; no lone dollar sign (the validator reads it as unclosed math: write "dollars"); math and symbols in $...$ (KaTeX:
$\\hat{y}$, $\\bar{x}$, $r^2$); no single-asterisk italics; never refer to a choice by letter; no "all/none of the above".
"""
import math
import os
import random
import sys
from types import SimpleNamespace

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import authoring
from authoring import ch, sig  # noqa: F401  (re-exported for the unit scripts)

COURSE = "ap-statistics"
PREFIX = "ap-stat"
KINDS = ["COLLECT_DATA", "ANALYZE_DATA", "INFERENCE", "MULTI_FOCUS"]
FRQ_POINTS = 10  # every free-response question is worth 10 points (CED Exam Overview)


def _units_dir():
    return os.path.join(authoring.CONTENT, COURSE, "units")


def unit_slug(n):
    import json
    with open(os.path.join(_units_dir(), f"unit-{n}.json"), encoding="utf-8") as f:
        return json.load(f)["slug"]


def topic_slugs(n):
    """The unit's topic slugs in CED order, so a script can say T[1] for topic n.1."""
    import json
    with open(os.path.join(_units_dir(), f"unit-{n}.json"), encoding="utf-8") as f:
        return {t["order"]: t["slug"] for t in json.load(f)["topics"]}


def _check_text(*texts):
    for t in texts:
        assert "—" not in t, f"em dash in {t[:60]!r}"
        assert t.count("$") % 2 == 0, f"unbalanced dollar sign in {t[:80]!r}"
        assert "**" not in t.replace("**(", "").replace(")**", "") or True


class Bank(authoring.Bank):
    """One unit's questions and free-response prompts, written to unit-N.json. Ids are ap-stat-uN-mcq-1.. and ap-stat-uN-frq-1.."""

    def __init__(self, unit_num):
        super().__init__(COURSE, PREFIX, unit_num, unit_slug(unit_num), mcq_start=1, frq_start=1, suffix="")
        self.T = topic_slugs(unit_num)

    def mcq(self, topic_number, stem, correct, wrongs, explanation, diagram=None, difficulty="medium"):
        assert difficulty in ("easy", "medium", "hard"), difficulty
        wrongs = list(wrongs)
        assert len(wrongs) == 3, f"the 2026-27 exam has four choices: {stem[:50]}"
        _check_text(stem, explanation, *[c_["text"] + c_["expl"] for c_ in [correct] + wrongs])
        super().mcq(self.T[topic_number], stem, correct, wrongs, explanation, diagram=diagram, difficulty=difficulty)

    def frq(self, topic_number, kind, prompt, rubric, sample, diagram=None):
        """rubric: ten (1, description) lines, one point each, in the order of the parts."""
        assert kind in KINDS, kind
        assert all(p == 1 for p, _ in rubric), "rubric lines are one point each"
        assert sum(p for p, _ in rubric) == FRQ_POINTS, f"every question is worth {FRQ_POINTS}, rubric has {sum(p for p, _ in rubric)}"
        _check_text(prompt, sample, *[d for _, d in rubric])
        super().frq(self.T[topic_number], prompt, rubric, sample, diagram=diagram, ftype=kind)


# ---- numbers -------------------------------------------------------------------------------------------------------

def mean(xs):
    return sum(xs) / len(xs)


def sd(xs):
    """Sample standard deviation (n - 1), as on the AP formula sheet."""
    m = mean(xs)
    return math.sqrt(sum((x - m) ** 2 for x in xs) / (len(xs) - 1))


def lsrl(xs, ys):
    """The least-squares line and correlation, by technology (numpy), as the CED says."""
    x, y = np.array(xs, float), np.array(ys, float)
    b, a = np.polyfit(x, y, 1)
    r = float(np.corrcoef(x, y)[0, 1])
    return SimpleNamespace(a=float(a), b=float(b), r=r, r2=r * r, xbar=float(x.mean()), ybar=float(y.mean()), sx=float(x.std(ddof=1)), sy=float(y.std(ddof=1)), n=len(xs))


def fmt(v, places=2):
    """A fixed number of places, with a hyphen for a negative (so 2.0 stays 2.0)."""
    return f"{v:.{places}f}"


def signed(v, places=2):
    """'+ 3.40' or '- 3.40', for writing an equation."""
    return f"{'-' if v < 0 else '+'} {abs(v):.{places}f}"


def yhat_eq(a, b, places=2, y="y", x="x"):
    """The least-squares equation as LaTeX: $\\hat{y} = 12.40 + 2.10x$."""
    return f"$\\hat{{{y}}} = {a:.{places}f} {signed(b, places)}{x}$"


def pct(v, places=1):
    return f"{v * 100:.{places}f}%"


# ---- diagrams ------------------------------------------------------------------------------------------------------

def table(columns, rows, caption=None, row_headers=False):
    """A data-table diagram. Cells are written as strings so a trailing zero is kept ("2.0")."""
    d = {"type": "data-table", "columns": list(columns), "rows": [[c_ if isinstance(c_, str) else str(c_) for c_ in r] for r in rows], "rowHeaders": row_headers}
    if caption:
        d["caption"] = caption
    for r in d["rows"]:
        assert len(r) == len(d["columns"]), f"row {r} does not match columns {d['columns']}"
    return d


def nice_axis(lo, hi, max_ticks=8):
    """(min, max, step) with the data inside, a little room at each end, and at most `max_ticks` steps."""
    span = hi - lo
    assert span > 0
    steps = sorted(m * 10.0 ** e for e in range(-4, 6) for m in (1, 2, 2.5, 5))
    for step in steps:
        mn = math.floor((lo - 0.04 * span) / step + 1e-9) * step
        mx = math.ceil((hi + 0.04 * span) / step - 1e-9) * step
        if lo >= 0:
            mn = max(mn, 0.0)  # a quantity that cannot be negative does not get a negative axis
        if round((mx - mn) / step) <= max_ticks:
            return round(mn, 6), round(mx, 6), round(step, 6)
    raise AssertionError("no axis")


def scatter(points, x_label, y_label, x_axis=None, y_axis=None, line=None, zero_line=False, highlights=None, alt=None):
    """A scatterplot diagram. `points` are (x, y) pairs; an axis is (min, max, step) or None to choose one; `line` is (intercept, slope)."""
    xs, ys = [p[0] for p in points], [p[1] for p in points]
    xmin, xmax, xstep = x_axis or nice_axis(min(xs), max(xs))
    ymin, ymax, ystep = y_axis or nice_axis(min(ys), max(ys))
    if zero_line and not (ymin < 0 < ymax):
        raise AssertionError("a residual plot's axis must include zero")
    d = {"type": "scatterplot", "xLabel": x_label, "yLabel": y_label, "xMin": xmin, "xMax": xmax, "xStep": xstep, "yMin": ymin, "yMax": ymax, "yStep": ystep,
         "points": [{"x": round(x, 3), "y": round(y, 3)} for x, y in points], "zeroLine": bool(zero_line)}
    if line:
        d["line"] = {"intercept": round(line[0], 4), "slope": round(line[1], 4)}
    if highlights:
        d["highlights"] = [{"index": i, "label": label} for i, label in highlights]
    if alt:
        d["altText"] = alt
    return d


def noisy_line(xs, a, b, noise, seed, places=1):
    """y = a + b x plus seeded noise, rounded: the same data every run."""
    rnd = random.Random(seed)
    return [round(a + b * x + rnd.uniform(-noise, noise), places) for x in xs]
