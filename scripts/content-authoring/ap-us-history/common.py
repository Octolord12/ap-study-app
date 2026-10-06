import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from authoring import *

COURSE = "ap-us-history"
PREFIX = "ap-ush"

UNIT_SLUGS = {
    1: "unit-1-contact-and-early-colonization",
    2: "unit-2-colonial-america",
    3: "unit-3-revolution-and-new-nation",
    4: "unit-4-democratic-republic",
    5: "unit-5-civil-war-era",
    6: "unit-6-gilded-age",
    7: "unit-7-imperialism-to-world-war-two",
    8: "unit-8-cold-war-and-civil-rights",
    9: "unit-9-contemporary-america",
}


def src(attribution, text):
    """A source excerpt: original passages with a generic attribution, never a quotation from a real document."""
    return f"> {text}\n>\n> *Source: {attribution}*"


import importlib


def _load_pad():
    """pad_uN.py holds PAD = {question id: [wrong choice texts in the order the script lists them]}, or
    {"c": new text for the right answer, "w": [...]} when the right answer is also tightened.
    The first drafts wrote the right answer much longer than the wrong ones in almost every question, which
    is a tell a student can use without knowing any history; these overlays lengthen the wrong choices
    (same claim, more specific wording) so length says nothing. The explanations are unchanged."""
    pad, padc, padw = {}, {}, {}
    for n in range(1, 10):
        try:
            mod = importlib.import_module(f"pad_u{n}")
        except ModuleNotFoundError:
            continue
        pad.update(mod.PAD)
        padc.update(getattr(mod, "PADC", {}))
        padw.update(getattr(mod, "PADW", {}))
    return pad, padc, padw


PAD, PADC, PADW = _load_pad()


class PaddedBank(Bank):
    def mcq(self, topic, stem, correct, wrongs, explanation, **kw):
        qid = f"{self.prefix}-u{self.n}-mcq-{self.mcq_start + len(self.mcqs)}"
        if os.environ.get("DUMP"):
            print(f"{qid} | C{len(correct['text'])} | " + " | ".join(f"[{len(w['text'])}] {w['text']}" for w in wrongs))
        if qid in PADC:
            correct = dict(correct, text=PADC[qid])
        pad = PAD.get(qid)
        if pad:
            if isinstance(pad, dict):
                if "c" in pad:
                    correct = dict(correct, text=pad["c"])
                pad = pad["w"]
            assert len(pad) == len(wrongs), f"{qid}: pad has {len(pad)} texts for {len(wrongs)} wrong choices"
            wrongs = [dict(w, text=t) for w, t in zip(wrongs, pad)]
        wrongs = [dict(w, text=PADW.get(w["text"], w["text"])) for w in wrongs]
        super().mcq(topic, stem, correct, wrongs, explanation, **kw)


def base(n):
    """The core set for unit n: ids mcq-1..30 and frq-1..3, written to unit-N.json."""
    return PaddedBank(COURSE, PREFIX, n, UNIT_SLUGS[n], mcq_start=1, frq_start=1, suffix="")


def hard(n):
    """The hard set for unit n: ids mcq-31..45 and frq-4..5, written to unit-N-hard.json."""
    return PaddedBank(COURSE, PREFIX, n, UNIT_SLUGS[n])


def saq(B, topic, prompt, parts, sample):
    """Short-answer item: `parts` is a list of (points, description), usually one point per part."""
    B.frq(topic, prompt, parts, sample, ftype="SAQ")


def leq(B, topic, prompt, sample, thesis, context, evidence, analysis):
    """Long-essay item scored 6 points: thesis 1, contextualization 1, evidence 2, analysis and reasoning 2."""
    B.frq(topic, prompt, [(1, thesis), (1, context), (2, evidence), (2, analysis)], sample, ftype="LEQ")


def dbq(B, topic, prompt, sample, thesis, context, docs, outside, sourcing, complexity):
    """Document-based item scored 7 points: thesis 1, contextualization 1, document evidence 2, outside evidence 1,
    sourcing 1, complexity 1."""
    B.frq(topic, prompt, [(1, thesis), (1, context), (2, docs), (1, outside), (1, sourcing), (1, complexity)], sample, ftype="DBQ")
