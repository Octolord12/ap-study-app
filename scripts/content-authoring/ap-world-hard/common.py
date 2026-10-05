import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from authoring import *


def src(attribution, text):
    """A source excerpt in the same convention as the DBQ pool: original passages with a generic attribution."""
    return f"> {text}\n>\n> *Source: {attribution}*"


def bank(n, slug):
    return Bank("ap-world", "ap-world", n, slug)


def saq(B, topic, prompt, parts, sample):
    """Short-answer item: `parts` is a list of (points, description), usually one point per part."""
    B.frq(topic, prompt, parts, sample, ftype="SAQ")


def leq(B, topic, prompt, sample, thesis, context, evidence, analysis):
    """Long-essay item scored 6 points: thesis 1, contextualization 1, evidence 2, analysis and reasoning 2."""
    B.frq(topic, prompt, [(1, thesis), (1, context), (2, evidence), (2, analysis)], sample, ftype="LEQ")
