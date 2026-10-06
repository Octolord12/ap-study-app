"""Evens out answer lengths in the AP World History questions (see "AP U.S. History" in CLAUDE.md for why).

In the first drafts the right answer was the longest choice in 87% of questions. Each pad_uN.py holds, per question id,
  PAD[id]  = the wrong choices' new texts in the order they appear in the file (None keeps one as is)
  PADC[id] = the right answer's new text
  PADW     = {text of a wrong choice: longer text}, a second pass for the questions PAD left with the right answer longest
and this script writes them into content/ap-world/questions/unit-N.json (rewritten line by line, because those files keep
one choice per line) and unit-N-hard.json (through json, which round-trips them exactly). Only the `text` of a choice
changes: labels, which one is correct and every explanation stay as they were. Safe to run twice. Run it again after
re-running an ap-world-hard generator, which rewrites its file from scratch.

    python3 apply.py           # apply every unit
    python3 apply.py 3         # one unit
"""
import importlib, json, os, re, sys

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../content/ap-world/questions"))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
CHOICE_LINE = re.compile(r'^(\s*\{ "label": "[A-E]", "text": )("(?:[^"\\]|\\.)*")(, "isCorrect": )(true|false)(.*)$')


def plan(qid, choices_correct_flags, pad, padc, current, padw):
    """new texts for one question's choices, in file order: a list of None (keep) or the new string.
    PADW patches one wrong choice, matched by its text after PAD has been applied."""
    wrongs = pad.get(qid)
    out, w = [], 0
    n_wrong = sum(1 for c in choices_correct_flags if not c)
    if wrongs is not None:
        assert len(wrongs) == n_wrong, f"{qid}: {len(wrongs)} wrong texts for {n_wrong} wrong choices"
    for is_correct, now in zip(choices_correct_flags, current):
        if is_correct:
            out.append(padc.get(qid))
        else:
            text = wrongs[w] if wrongs is not None and wrongs[w] is not None else now
            text = padw.get(text, text)
            out.append(None if text == now else text)
            w += 1
    return out


def patch_core(path, pad, padc, padw):
    lines = open(path, encoding="utf-8").read().split("\n")
    qid, flags, idx, current = None, [], [], []
    result = list(lines)

    def flush():
        if qid is None or not flags:
            return
        new = plan(qid, flags, pad, padc, current, padw)
        for line_no, text in zip(idx, new):
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


def patch_hard(path, pad, padc, padw):
    data = json.load(open(path, encoding="utf-8"))
    for q in data:
        flags = [c["isCorrect"] for c in q["choices"]]
        current = [c["text"] for c in q["choices"]]
        for c, text in zip(q["choices"], plan(q["id"], flags, pad, padc, current, padw)):
            if text is not None:
                c["text"] = text
    open(path, "w", encoding="utf-8").write(json.dumps(data, indent=2, ensure_ascii=False) + "\n")


def check(path):
    for q in json.load(open(path, encoding="utf-8")):
        texts = [c["text"] for c in q["choices"]]
        assert len(set(texts)) == len(texts), f"duplicate choice text in {q['id']}"
        assert sum(c["isCorrect"] for c in q["choices"]) == 1, q["id"]


def main():
    units = [int(a) for a in sys.argv[1:]] or range(1, 10)
    for n in units:
        try:
            mod = importlib.import_module(f"pad_u{n}")
        except ModuleNotFoundError:
            continue
        for suffix, patch in (("", patch_core), ("-hard", patch_hard)):
            path = os.path.join(ROOT, f"unit-{n}{suffix}.json")
            patch(path, mod.PAD, mod.PADC, getattr(mod, "PADW", {}))
            check(path)
        print(f"unit {n}: padded")


main()
