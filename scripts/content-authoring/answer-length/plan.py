"""Chooses the questions to edit and prints worksheets for writing the longer wrong choice.

    python3 plan.py select <selection.json>                       # freeze the choice (deterministic from the current content)
    python3 plan.py show <selection.json> <course> <core|hard> [start] [count]

A question is chosen when exactly one wrong choice is as short as or shorter than the right answer (so lengthening that one makes the
right answer strictly shortest), cheapest first, until the right answer is the shortest in about 18% of the set's prose-choice questions.
"""
import json, math, sys
from lib import *


def select():
    out = {}
    for course in COURSES:
        texts = [c["text"] for q in load(course) for c in q["choices"]]
        for hard in sets(course):
            qs = [q for q in load(course, hard) if is_prose(q)]
            now = sum(strictly_shortest(q) for q in qs)
            need = max(0, math.ceil(TARGET * len(qs)) - now)
            cands = []
            for q in qs:
                if strictly_shortest(q):
                    continue
                w = single_edit(q)
                if w and texts.count(w[1]) == 1:
                    cor, _ = analyze(q)
                    cands.append((cor + 2 - w[0], q["id"]))
            cands.sort()
            out[f"{course}:{'hard' if hard else 'core'}"] = {"need": need, "available": len(cands), "ids": [i for _, i in cands[:need]]}
    return out


def show(sel, course, which, start=0, count=15):
    qs = {q["id"]: q for q in load(course, which == "hard")}
    ids = sel[f"{course}:{which}"]["ids"][start:start + count]
    for qid in ids:
        q = qs[qid]
        cor, wr = analyze(q)
        short = single_edit(q)
        lo, hi = window(q)
        right = next(c for c in q["choices"] if c["isCorrect"])
        print(f"=== {qid}  [{q['topic']}]  lengthen to {lo}-{hi} visible chars (now {short[0]})")
        print("STEM :", " ".join(q["stem"].split())[:260])
        print(f"RIGHT [{cor}]: {right['text']}")
        for n, t, c in wr:
            mark = "  <== LENGTHEN" if c is short[2] else ""
            print(f"  wrong [{n}]: {t}{mark}")
            if c is short[2]:
                print(f"     why it is wrong: {' '.join(c['explanation'].split())[:300]}")
        print()


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "select":
        sel = select()
        json.dump(sel, open(sys.argv[2], "w"), indent=1)
        for k, v in sel.items():
            print(f"{k:22} need {v['need']:2d}  available {v['available']:2d}  chosen {len(v['ids']):2d}")
        print("total chosen:", sum(len(v["ids"]) for v in sel.values()))
    else:
        sel = json.load(open(sys.argv[2]))
        show(sel, sys.argv[3], sys.argv[4], int(sys.argv[5]) if len(sys.argv) > 5 else 0, int(sys.argv[6]) if len(sys.argv) > 6 else 15)
