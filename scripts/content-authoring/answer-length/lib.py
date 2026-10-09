"""Shared by plan.py / record.py / stats.py: where each course keeps its questions and its PADW overlay.

The right answer used to be the longest choice; the overlays in ap-core-pad, ap-world-pad and ap-us-history fixed that (see
CLAUDE.md). What was left is the other end: the right answer is almost never the SHORTEST choice (3 to 12% of the questions where
length can be a tell, against 25% by chance), so a student can drop the shortest choice and guess among the rest. The fix is to lengthen
the one wrong choice that is as short as the right answer, with more specific wording that keeps the same claim, through the same
PADW overlays (PADW = {a wrong choice's current text: its longer text}; the generators or apply.py replay them).
"""
import glob, importlib.util, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
AUTH = os.path.normpath(os.path.join(HERE, ".."))
CONTENT = os.path.normpath(os.path.join(HERE, "../../../content"))
CORE_ONLY = ("ap-calc", "ap-physics-1", "ap-csa")   # their hard sets are generated with computed distractors and are almost all math or code
COURSES = ["ap-calc", "ap-physics-1", "ap-csa", "ap-world", "ap-us-history"]
TARGET = 0.18
PROSE = 30          # a question is "prose" (length can be a tell) when its longest choice has at least this many visible characters


def vis(text):
    return len(text.replace("$", ""))


def unit_of(qid):
    return int(re.search(r"-u(\d+)-mcq-", qid).group(1))


def is_hard(qid):
    return int(qid.rsplit("-", 1)[1]) > 30


def pad_path(course, unit):
    if course in CORE_ONLY:
        return os.path.join(AUTH, "ap-core-pad", course, f"pad_u{unit}.py")
    if course == "ap-world":
        return os.path.join(AUTH, "ap-world-pad", f"pad_u{unit}.py")
    return os.path.join(AUTH, "ap-us-history", f"pad_u{unit}.py")


def question_files(course, hard=None):
    out = []
    for f in sorted(glob.glob(f"{CONTENT}/{course}/questions/unit-*.json")):
        if hard is None or f.endswith("-hard.json") == hard:
            out.append(f)
    return out


def load(course, hard=None):
    qs = []
    for f in question_files(course, hard):
        qs += json.load(open(f, encoding="utf-8"))
    return qs


def sets(course):
    return [False] if course in CORE_ONLY else [False, True]


def analyze(q):
    """(visible length of the right answer, wrong choices as (length, text, choice) sorted shortest first)."""
    cor = vis(next(c["text"] for c in q["choices"] if c["isCorrect"]))
    wr = sorted(((vis(c["text"]), c["text"], c) for c in q["choices"] if not c["isCorrect"]), key=lambda t: t[0])
    return cor, wr


def is_prose(q):
    return max(vis(c["text"]) for c in q["choices"]) >= PROSE


def strictly_shortest(q):
    cor, wr = analyze(q)
    return cor < wr[0][0]


def single_edit(q):
    """The wrong choice to lengthen, if lengthening just that one makes the right answer strictly shortest; else None."""
    cor, wr = analyze(q)
    le = [w for w in wr if w[0] <= cor]
    return le[0] if len(le) == 1 else None


def window(q):
    """Allowed visible length for the lengthened choice: longer than the right answer, and not much longer than the longest wrong choice."""
    cor, wr = analyze(q)
    others = [w[0] for w in wr if w[0] > cor]
    return cor + 2, max(max(others), cor + 8) + 3


def read_padw(path):
    if not os.path.exists(path):
        return {}
    spec = importlib.util.spec_from_file_location("padmod", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return dict(getattr(mod, "PADW", {}))


def render_padw(path, padw, prefix):
    """The pad file's new source with PADW replaced (PADW must be the last statement; `PADW = {}` on one line is fine)."""
    src = open(path, encoding="utf-8").read() if os.path.exists(path) else f'P = "{prefix}"\n\nPAD = {{}}\nPADC = {{}}\n'
    cut = src.find("PADW = {")
    if cut != -1:
        tail = src[cut:]
        if tail.startswith("PADW = {}"):
            rest = tail[len("PADW = {}"):]
        else:
            end = tail.find("\n}\n")
            assert end != -1, f"{path}: cannot find the end of PADW; edit by hand"
            rest = tail[end + 3:]
        assert not rest.strip(), f"{path}: PADW is not the last statement; edit by hand"
        src = src[:cut]
    return src.rstrip("\n") + "\n\nPADW = {\n" + "".join(f"    {json.dumps(k, ensure_ascii=False)}: {json.dumps(v, ensure_ascii=False)},\n" for k, v in padw.items()) + "}\n"
