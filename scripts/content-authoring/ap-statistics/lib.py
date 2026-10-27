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
import collections
import math
import os
import random
import re
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


_SINGLE_ASTERISK = re.compile(r"(?<![*\\])\*(?!\*)[^*\n]+(?<!\*)\*(?!\*)")


def check_markdown(t):
    """The text rules every string must follow (a math course turns a single-asterisk emphasis into a multiplication dot)."""
    assert "—" not in t, f"em dash in {t[:60]!r}"
    assert t.count("$") % 2 == 0, f"unbalanced dollar sign in {t[:80]!r}"
    plain = re.sub(r"\*\*[^*]+\*\*", "", re.sub(r"\$[^$]*\$", "", t))
    assert not _SINGLE_ASTERISK.search(plain), f"single-asterisk italics (use plain words or **bold**) in {t[:80]!r}"
    assert "_" not in re.sub(r"\$[^$]*\$", "", t) or "_" not in t, f"underscore outside math in {t[:80]!r}"


def _check_text(*texts):
    for t in texts:
        check_markdown(t)


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


# ---- one-variable data and its graphs (Unit 1 and later) ------------------------------------------------------------

def quartiles(data):
    """Five-number summary by the usual AP method: Q1 and Q3 are the medians of the lower and upper halves (the median is left out of both halves when n is odd)."""
    d = sorted(data)
    n = len(d)

    def med(a):
        m = len(a)
        return a[m // 2] if m % 2 else (a[m // 2 - 1] + a[m // 2]) / 2

    lower, upper = d[: n // 2], d[(n + 1) // 2:]
    return SimpleNamespace(min=d[0], q1=med(lower), median=med(d), q3=med(upper), max=d[-1], iqr=med(upper) - med(lower), n=n)


def outliers_iqr(data):
    """Values more than 1.5 IQR below Q1 or above Q3 (CED 1.7.D.1.i)."""
    f = quartiles(data)
    lo, hi = f.q1 - 1.5 * f.iqr, f.q3 + 1.5 * f.iqr
    return [x for x in sorted(data) if x < lo or x > hi]


def draw(kind, n, seed, lo=0.0, hi=100.0, places=0):
    """n values with a known shape, seeded: 'right', 'left', 'symmetric', 'bimodal', 'uniform'. Values are clipped into [lo, hi]."""
    rnd = random.Random(seed)
    span = hi - lo
    if kind == "right":
        raw = [lo + span * min(0.97, rnd.lognormvariate(-1.45, 0.62)) for _ in range(n)]
    elif kind == "left":
        raw = [hi - span * min(0.97, rnd.lognormvariate(-1.45, 0.62)) for _ in range(n)]
    elif kind == "symmetric":
        raw = [lo + span * min(0.97, max(0.03, rnd.gauss(0.5, 0.15))) for _ in range(n)]
    elif kind == "bimodal":
        raw = [lo + span * min(0.97, max(0.03, rnd.gauss(0.25 if rnd.random() < 0.5 else 0.75, 0.07))) for _ in range(n)]
    elif kind == "uniform":
        raw = [rnd.uniform(lo + 0.02 * span, hi - 0.02 * span) for _ in range(n)]
    else:
        raise AssertionError(kind)
    vals = [round(v, places) for v in raw]
    return [int(v) for v in vals] if places == 0 else vals


def skewness(data):
    x = np.array(data, float)
    s = x.std()
    return float(((x - x.mean()) ** 3).mean() / s ** 3) if s else 0.0


def bin_counts(data, edges):
    """Counts in [e0, e1), [e1, e2), ..., the last bin including its right edge."""
    counts = [0] * (len(edges) - 1)
    for x in data:
        for i in range(len(edges) - 1):
            if edges[i] <= x < edges[i + 1] or (i == len(edges) - 2 and x == edges[-1]):
                counts[i] += 1
                break
        else:
            raise AssertionError(f"{x} is outside the bins")
    return counts


def count_axis(top):
    """(max, step) for a count axis: whole-number steps, the largest count inside, at most 10 steps."""
    for step in (1, 2, 5, 10, 20, 25, 50, 100, 200, 500, 1000):
        mx = math.ceil((top + 0.001) / step) * step
        if mx / step <= 10:
            return mx, step
    raise AssertionError(top)


def histogram(data, edges, x_label, y_label="Frequency", tick_at="edges", label_every=1, y_axis=None, alt=None):
    counts = bin_counts(data, edges)
    ymax, ystep = (y_axis[1], y_axis[2]) if y_axis else count_axis(max(counts))
    d = {"type": "histogram", "xLabel": x_label, "yLabel": y_label, "edges": [round(e, 6) for e in edges], "values": counts, "yMax": ymax, "yStep": ystep, "tickAt": tick_at, "labelEvery": label_every}
    if alt:
        d["altText"] = alt
    return d


def hist_from_counts(counts, edges, x_label, y_label="Frequency", tick_at="edges", label_every=1, y_axis=None, alt=None):
    ymax, ystep = (y_axis[1], y_axis[2]) if y_axis else count_axis(max(counts))
    d = {"type": "histogram", "xLabel": x_label, "yLabel": y_label, "edges": [round(e, 6) for e in edges], "values": list(counts), "yMax": ymax, "yStep": ystep, "tickAt": tick_at, "labelEvery": label_every}
    if alt:
        d["altText"] = alt
    return d


def box_group(data, label=None):
    """One boxplot group from raw data: whiskers go to the most extreme values that are not outliers by the 1.5 IQR rule."""
    f = quartiles(data)
    out = outliers_iqr(data)
    inside = [x for x in data if x not in out]
    g = {"min": min(inside), "q1": f.q1, "median": f.median, "q3": f.q3, "max": max(inside)}
    if label:
        g["label"] = label
    if out:
        g["outliers"] = out
    return g


def boxplot(groups, x_label, axis=None, alt=None):
    """`groups` are box_group() dicts; the axis is chosen to hold every value unless given as (min, max, step)."""
    vals = [v for g in groups for k in ("min", "q1", "median", "q3", "max") for v in [g[k]]] + [o for g in groups for o in g.get("outliers", [])]
    lo, hi, step = axis or nice_axis(min(vals), max(vals))
    d = {"type": "boxplot", "xLabel": x_label, "axisMin": lo, "axisMax": hi, "axisStep": step, "groups": groups}
    if alt:
        d["altText"] = alt
    return d


def dotplot(data, x_label, axis=None, alt=None):
    counts = collections.Counter(data)
    lo, hi, step = axis or nice_axis(min(data), max(data))
    d = {"type": "dotplot", "xLabel": x_label, "axisMin": lo, "axisMax": hi, "axisStep": step, "dots": [{"x": x, "count": c} for x, c in sorted(counts.items())]}
    if alt:
        d["altText"] = alt
    return d


def bars(categories, values, x_label, y_label, y_max=None, y_min=0, series_label=None, extra=None, alt=None):
    """A bar-graph diagram for one categorical variable (frequency or relative frequency); `extra` is a second series (list of values) with its label."""
    top = y_max if y_max is not None else (count_axis(max(values))[0] if all(float(v).is_integer() for v in values) else nice_axis(0, max(values))[1])
    series = [{"values": [round(v, 3) for v in values], "color": "blue"}]
    if series_label:
        series[0]["label"] = series_label
    if extra:
        series.append({"values": [round(v, 3) for v in extra[0]], "color": "red", "label": extra[1]})
    d = {"type": "bar-graph", "xLabel": x_label, "yLabel": y_label, "yMin": y_min, "yMax": top, "categories": list(categories), "series": series}
    if alt:
        d["altText"] = alt
    return d


def stemplot(data, caption, unit_digits=1):
    """A stem-and-leaf plot as a table (columns Stem and Leaf, the key in the caption). Values are integers; the last digit is the leaf."""
    rows = collections.defaultdict(list)
    for x in sorted(data):
        rows[x // 10].append(x % 10)
    return table(["Stem", "Leaf"], [(str(s), " ".join(str(l) for l in rows[s])) for s in range(min(rows), max(rows) + 1)], caption=caption, row_headers=True)


def z(x, mu, sigma):
    return (x - mu) / sigma


# ---- Unit 2 helpers: two-way tables, probability tables, density curves --------------------------------------------------

def twoway(corner, col_names, row_names, counts, caption=None, totals=True, hide=None):
    """A two-way table of counts as a data-table. `counts[r][c]`; `hide` is a set of (r, c) cells shown as "?" (a missing-entry question);
    row totals are on the right and column totals in a last row when `totals` is true (use row index len(row_names) for the totals row)."""
    hide = hide or set()
    rn, cn = len(row_names), len(col_names)
    grid = [list(r) for r in counts]
    if totals:
        for r in grid:
            r.append(sum(r))
        grid.append([sum(grid[r][c] for r in range(rn)) for c in range(cn)] + [sum(sum(r) for r in counts)])
    names = list(row_names) + (["Total"] if totals else [])
    cols = [corner] + list(col_names) + (["Total"] if totals else [])
    rows = [[names[r]] + ["?" if (r, c) in hide else str(v) for c, v in enumerate(row)] for r, row in enumerate(grid)]
    return table(cols, rows, caption=caption, row_headers=True)


def chi2_density(df, xmax, ticks, shade=(), x_label=None, alt=None):
    """A chi-square curve as a density-curve diagram (worked out with scipy), from 0.05 to xmax."""
    from scipy import stats as _sps
    xs = np.linspace(0.05, xmax, 73)
    pts = [{"x": round(float(x), 4), "y": round(float(_sps.chi2.pdf(x, df)), 6)} for x in xs]
    for a, b in shade:
        assert 0.05 <= a < b <= xmax, (a, b)
    d = {"type": "density-curve", "points": pts, "shade": [{"from": round(a, 4), "to": round(b, 4)} for a, b in shade], "ticks": [{"x": round(x, 4), "label": t} for x, t in ticks]}
    if x_label:
        d["xLabel"] = x_label
    if alt:
        d["altText"] = alt
    return d


def density(mu, sigma, ticks, shade=(), x_label=None, alt=None, span=3.6):
    """A normal curve as a density-curve diagram, worked out with scipy. `ticks` are (x, label) pairs, `shade` (from, to) pairs; the curve runs from mu - span*sigma to mu + span*sigma."""
    from scipy import stats as _sps
    lo, hi = mu - span * sigma, mu + span * sigma
    xs = np.linspace(lo, hi, 73)
    pts = [{"x": round(float(x), 4), "y": round(float(_sps.norm.pdf(x, mu, sigma)), 6)} for x in xs]
    for a, b in shade:
        assert lo <= a < b <= hi, (a, b, lo, hi)
    d = {"type": "density-curve", "points": pts, "shade": [{"from": round(a, 4), "to": round(b, 4)} for a, b in shade], "ticks": [{"x": round(x, 4), "label": t} for x, t in ticks]}
    if x_label:
        d["xLabel"] = x_label
    if alt:
        d["altText"] = alt
    return d


# ---- Unit 3 helpers: inference for proportions and chi-square ---------------------------------------------------------------

def zstar(conf):
    """The critical value z* for a C% confidence level (conf as a fraction, e.g. 0.95)."""
    from scipy import stats as _sps
    return float(_sps.norm.ppf(1 - (1 - conf) / 2))


def prop_ci(x, n, conf=0.95):
    """One-sample z-interval for a proportion: a namespace with phat, se, z, moe, lo, hi."""
    phat = x / n
    se = math.sqrt(phat * (1 - phat) / n)
    zc = zstar(conf)
    moe = zc * se
    return SimpleNamespace(phat=phat, se=se, z=zc, moe=moe, lo=phat - moe, hi=phat + moe, n=n, x=x)


def prop_z(x, n, p0, alt="ne"):
    """One-sample z-test for a proportion: phat, the null standard deviation, z and the p-value; alt is "gt", "lt" or "ne"."""
    from scipy import stats as _sps
    phat = x / n
    se0 = math.sqrt(p0 * (1 - p0) / n)
    zz = (phat - p0) / se0
    pv = _sps.norm.sf(zz) if alt == "gt" else _sps.norm.cdf(zz) if alt == "lt" else 2 * _sps.norm.sf(abs(zz))
    return SimpleNamespace(phat=phat, se0=se0, z=zz, p=float(pv), n=n, x=x, p0=p0)


def two_prop_ci(x1, n1, x2, n2, conf=0.95):
    p1, p2 = x1 / n1, x2 / n2
    se = math.sqrt(p1 * (1 - p1) / n1 + p2 * (1 - p2) / n2)
    zc = zstar(conf)
    d = p1 - p2
    return SimpleNamespace(p1=p1, p2=p2, diff=d, se=se, z=zc, moe=zc * se, lo=d - zc * se, hi=d + zc * se)


def two_prop_z(x1, n1, x2, n2, alt="ne"):
    from scipy import stats as _sps
    p1, p2 = x1 / n1, x2 / n2
    pc = (x1 + x2) / (n1 + n2)
    se0 = math.sqrt(pc * (1 - pc) * (1 / n1 + 1 / n2))
    zz = (p1 - p2) / se0
    pv = _sps.norm.sf(zz) if alt == "gt" else _sps.norm.cdf(zz) if alt == "lt" else 2 * _sps.norm.sf(abs(zz))
    return SimpleNamespace(p1=p1, p2=p2, pc=pc, se0=se0, z=zz, p=float(pv))


def chi_square(counts):
    """Chi-square test on a two-way table of counts: expected counts, the statistic, degrees of freedom and the p-value."""
    from scipy import stats as _sps
    obs = np.array(counts, dtype=float)
    rows, cols = obs.sum(axis=1), obs.sum(axis=0)
    exp = np.outer(rows, cols) / obs.sum()
    chi2 = float(((obs - exp) ** 2 / exp).sum())
    df = (obs.shape[0] - 1) * (obs.shape[1] - 1)
    return SimpleNamespace(expected=exp, chi2=chi2, df=df, p=float(_sps.chi2.sf(chi2, df)), contrib=(obs - exp) ** 2 / exp)


# ---- Unit 4 helpers: t procedures for means --------------------------------------------------------------------------------

def tstar(conf, df):
    from scipy import stats as _sps
    return float(_sps.t.ppf(1 - (1 - conf) / 2, df))


def t_ci(xbar, s, n, conf=0.95):
    """One-sample t-interval (also for matched pairs, from the differences): xbar, se, df, t*, moe, lo, hi."""
    se = s / math.sqrt(n)
    tc = tstar(conf, n - 1)
    return SimpleNamespace(xbar=xbar, s=s, n=n, se=se, df=n - 1, t=tc, moe=tc * se, lo=xbar - tc * se, hi=xbar + tc * se)


def t_test(xbar, s, n, mu0, alt="ne"):
    """One-sample t-test (also matched pairs): the statistic, df and p-value; alt is "gt", "lt" or "ne"."""
    from scipy import stats as _sps
    se = s / math.sqrt(n)
    tt = (xbar - mu0) / se
    df = n - 1
    pv = _sps.t.sf(tt, df) if alt == "gt" else _sps.t.cdf(tt, df) if alt == "lt" else 2 * _sps.t.sf(abs(tt), df)
    return SimpleNamespace(xbar=xbar, s=s, n=n, mu0=mu0, se=se, t=tt, df=df, p=float(pv))


def welch_df(s1, n1, s2, n2):
    a, b = s1 ** 2 / n1, s2 ** 2 / n2
    return (a + b) ** 2 / (a ** 2 / (n1 - 1) + b ** 2 / (n2 - 1))


def t2_ci(x1, s1, n1, x2, s2, n2, conf=0.95):
    """Two-sample t-interval for mu1 - mu2 (degrees of freedom by the Welch formula, as technology gives them)."""
    se = math.sqrt(s1 ** 2 / n1 + s2 ** 2 / n2)
    df = welch_df(s1, n1, s2, n2)
    tc = tstar(conf, df)
    d = x1 - x2
    return SimpleNamespace(diff=d, se=se, df=df, t=tc, moe=tc * se, lo=d - tc * se, hi=d + tc * se)


def t2_test(x1, s1, n1, x2, s2, n2, alt="ne"):
    from scipy import stats as _sps
    se = math.sqrt(s1 ** 2 / n1 + s2 ** 2 / n2)
    df = welch_df(s1, n1, s2, n2)
    tt = (x1 - x2) / se
    pv = _sps.t.sf(tt, df) if alt == "gt" else _sps.t.cdf(tt, df) if alt == "lt" else 2 * _sps.t.sf(abs(tt), df)
    return SimpleNamespace(diff=x1 - x2, se=se, df=df, t=tt, p=float(pv))


def t_density(df, ticks, shade=(), x_label=None, alt=None, span=4.5):
    """A t curve as a density-curve diagram (scipy)."""
    from scipy import stats as _sps
    xs = np.linspace(-span, span, 73)
    pts = [{"x": round(float(x), 4), "y": round(float(_sps.t.pdf(x, df)), 6)} for x in xs]
    for a, b in shade:
        assert -span <= a < b <= span, (a, b)
    d = {"type": "density-curve", "points": pts, "shade": [{"from": round(a, 4), "to": round(b, 4)} for a, b in shade], "ticks": [{"x": round(x, 4), "label": t} for x, t in ticks]}
    if x_label:
        d["xLabel"] = x_label
    if alt:
        d["altText"] = alt
    return d


# ---- free response in the CED's layout ----------------------------------------------------------------------------------

INSTR = "Use the given information to respond to parts A, B, C, D, and E. Label any subparts (e.g., i and ii) that may be present."


def frq_text(setup, parts, answers):
    """prompt and sample response in the CED's layout: the set-up, the instruction line, then **A.** ... **E.**; the sample answers A. ... E. in order.
    `parts` and `answers` are lists of (letter, text); a part's text may contain its own (i), (ii) paragraphs."""
    assert [k for k, _ in parts] == [k for k, _ in answers], "answers must follow the parts"
    prompt = setup.strip() + "\n\n" + INSTR + "\n\n" + "\n\n".join(f"**{k}.** {v}" for k, v in parts)
    sample = "\n\n".join(f"{k}. {v}" for k, v in answers)
    return prompt, sample
