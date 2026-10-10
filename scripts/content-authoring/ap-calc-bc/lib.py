"""Authoring helpers for the BC-only Calc items. Every number in a stem, choice or explanation is
produced by sympy from the same objects the answer is computed from, and `Bank.mcq` refuses duplicate
or mathematically equal choices. Built on ../authoring.py (the course-independent Bank)."""
import os, sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import authoring
from sympy import *

x, y, t, h, a, b, c, k, u, n = symbols("x y t h a b c k u n", real=True)

COURSE = "ap-calc-bc"
PREFIX = "ap-calcbc"


def L(e):
    """Sympy object (or plain string) -> LaTeX, no dollar signs."""
    if isinstance(e, str):
        return e
    s = latex(e, ln_notation=True)
    s = s.replace(r"\operatorname{atan}", r"\arctan").replace(r"\operatorname{asin}", r"\arcsin").replace(r"\operatorname{acos}", r"\arccos")
    return s.replace("\\,", " ")


def M(e):
    return "$" + L(e) + "$"


def same(p, q):
    try:
        return simplify(p - q) == 0
    except Exception:
        return False


def ch(text, expl, val=None):
    """A choice. `text` may be a sympy object (shown as math) or a string (shown as given)."""
    shown = M(text) if not isinstance(text, str) else text
    return {"text": shown, "expl": expl, "val": val if val is not None else (text if not isinstance(text, str) else None)}


def chv(tex, expl, val):
    """A choice shown as the given LaTeX (so it reads the way the explanation writes it), checked against `val`."""
    return {"text": "$" + tex + "$", "expl": expl, "val": val}


def chCt(tex, expl, val):
    """Same, for an antiderivative: the given LaTeX plus + C."""
    return {"text": "$" + tex + " + C$", "expl": expl, "val": val}


def chC(expr, expl):
    """An antiderivative choice: the expression plus + C, all in math."""
    return {"text": "$" + L(expr) + " + C$", "expl": expl, "val": expr}


def num(e, places=3):
    """Decimal string with a fixed number of places, for calculator-style answers."""
    return f"{float(N(e, 20)):.{places}f}"


def graph(*args, **kw):
    return authoring.graph(*args, **kw)


class Bank(authoring.Bank):
    """One unit's BC-only items, written to unit-N-bc.json. Ids continue after the copied AB items:
    questions from 46 (AB has 1-45), free-response prompts from 6 (AB has 1-5)."""

    def __init__(self, unit_num, unit_slug):
        super().__init__(COURSE, PREFIX, unit_num, unit_slug, mcq_start=46, frq_start=6, suffix="-bc")

    def mcq(self, topic, stem, correct, wrongs, explanation, diagram=None, difficulty="medium"):
        allc = [correct] + list(wrongs)
        vals = [c_.get("val") for c_ in allc]
        if all(v is not None for v in vals):
            from itertools import combinations
            for i, j in combinations(range(len(vals)), 2):
                assert not same(vals[i], vals[j]), f"choices {i} and {j} are equal in {stem[:60]}"
        plain = lambda c_: {"text": c_["text"], "expl": c_["expl"], "val": None}
        super().mcq(topic, stem, plain(correct), [plain(w) for w in wrongs], explanation, diagram=diagram, difficulty=difficulty)


def vec(*parts):
    """LaTeX for an angle-bracket vector from sympy expressions or strings."""
    return r"\langle " + ", ".join(L(p_) for p_ in parts) + r" \rangle"


def chvec(parts, expl):
    """A vector-valued choice: `parts` is a tuple of sympy expressions."""
    return {"text": "$" + vec(*parts) + "$", "expl": expl, "val": Matrix(parts)}
