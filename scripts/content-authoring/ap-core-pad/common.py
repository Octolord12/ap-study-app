"""Shared helpers for the answer-length overlays of AP Calculus AB, AP Physics 1 and AP CSA (core question sets only).

Same idea as ap-world-pad: in the first drafts the right answer was often the longest choice. Each <course>/pad_uN.py holds
  PAD[id]  = the wrong choices' new texts in the order they appear in the file (None keeps one as is)
  PADC[id] = the right answer's new text
  PADW     = {text of a wrong choice: longer text}, a second pass
and apply.py writes them into content/<course>/questions/unit-N.json. Only a choice's `text` changes.
The hard sets (unit-N-hard.json) were generated with computed distractors and are already balanced; they are not touched.
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CONTENT = os.path.normpath(os.path.join(HERE, "../../../content"))
PREFIX = {"ap-calc": "ap-calc", "ap-physics-1": "ap-phys1", "ap-csa": "ap-csa"}
UNITS = {"ap-calc": 8, "ap-physics-1": 8, "ap-csa": 10}


def core_path(course, unit):
    return f"{CONTENT}/{course}/questions/unit-{unit}.json"


def qid(course, unit, n):
    return f"{PREFIX[course]}-u{unit}-mcq-{n}"


def vis(text):
    """Visible length: the $ math delimiters are not shown."""
    return len(text.replace("$", ""))


def load_core(course, unit):
    return json.load(open(core_path(course, unit), encoding="utf-8"))


def units_from_args(course, args):
    return [int(a) for a in args] if args else list(range(1, UNITS[course] + 1))


def tell_questions(questions):
    """Questions where length is a usable tell: the right answer is strictly the longest, and either it is long
    (>= 30 visible characters) or it is much longer than every wrong choice (an explanatory tail on a short answer)."""
    out = []
    for q in questions:
        cor = vis(next(c["text"] for c in q["choices"] if c["isCorrect"]))
        wr = [vis(c["text"]) for c in q["choices"] if not c["isCorrect"]]
        if cor > max(wr) and (cor >= 30 or (cor >= 12 and cor >= 2 * max(wr))):
            out.append(q)
    return out


def overlay(course, unit):
    import importlib
    sys.path.insert(0, os.path.join(HERE, course))
    name = f"pad_u{unit}"
    if os.path.exists(os.path.join(HERE, course, name + ".py")):
        mod = importlib.import_module(name)
        sys.path.pop(0)
        return getattr(mod, "PAD", {}), getattr(mod, "PADC", {}), getattr(mod, "PADW", {})
    sys.path.pop(0)
    return {}, {}, {}
