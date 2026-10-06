"""Writes the pad_uN.py overlays of one course into content/<course>/questions/unit-N.json (core sets only).

    python3 apply.py ap-calc            # every unit
    python3 apply.py ap-physics-1 3 4   # units 3 and 4

The core files keep one choice per line and do not round-trip through json.dump, so they are rewritten line by line.
Only the `text` of a choice changes. Safe to run twice. Run it again if a core file is ever regenerated.
"""
import json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import core_path, overlay, units_from_args

CHOICE_LINE = re.compile(r'^(\s*\{ "label": "[A-E]", "text": )("(?:[^"\\]|\\.)*")(, "isCorrect": )(true|false)(.*)$')


def plan(qid, flags, pad, padc, current, padw):
    wrongs = pad.get(qid)
    n_wrong = sum(1 for c in flags if not c)
    if wrongs is not None:
        assert len(wrongs) == n_wrong, f"{qid}: {len(wrongs)} wrong texts for {n_wrong} wrong choices"
    out, w = [], 0
    for is_correct, now in zip(flags, current):
        if is_correct:
            out.append(padc.get(qid))
        else:
            text = wrongs[w] if wrongs is not None and wrongs[w] is not None else now
            text = padw.get(text, text)
            out.append(None if text == now else text)
            w += 1
    return out


def patch(path, pad, padc, padw):
    lines = open(path, encoding="utf-8").read().split("\n")
    result = list(lines)
    qid, flags, idx, current = None, [], [], []

    def flush():
        if qid is None or not flags:
            return
        for line_no, text in zip(idx, plan(qid, flags, pad, padc, current, padw)):
            if text is None:
                continue
            m = CHOICE_LINE.match(result[line_no])
            result[line_no] = m.group(1) + json.dumps(text, ensure_ascii=False) + m.group(3) + m.group(4) + m.group(5)

    for i, line in enumerate(lines):
        m = re.match(r'^\s*"id": "([^"]+)"', line)
        if m:
            flush()
            qid, flags, idx, current = m.group(1), [], [], []
            continue
        m = CHOICE_LINE.match(line)
        if m:
            flags.append(m.group(4) == "true")
            idx.append(i)
            current.append(json.loads(m.group(2)))
    flush()
    open(path, "w", encoding="utf-8").write("\n".join(result))


def check(path):
    for q in json.load(open(path, encoding="utf-8")):
        texts = [c["text"] for c in q["choices"]]
        assert len(set(texts)) == len(texts), f"{q['id']}: duplicate choice text"
        assert sum(c["isCorrect"] for c in q["choices"]) == 1, f"{q['id']}: not exactly one correct choice"


def main():
    course = sys.argv[1]
    for u in units_from_args(course, sys.argv[2:]):
        pad, padc, padw = overlay(course, u)
        if not (pad or padc or padw):
            continue
        path = core_path(course, u)
        patch(path, pad, padc, padw)
        check(path)
        print(f"{course} unit {u}: padded")


main()
