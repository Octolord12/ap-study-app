"""Writes content/ap-calc/refreshers/unit-N.json from the u1.py..u8.py scripts in this folder (see ../refreshers_lib.py).

Each script holds one refresher per topic (markdown, KaTeX in $...$) and re-checks its worked examples with sympy
before writing, so a number in the text cannot drift from the maths. Edit the scripts, not the JSON.
Layout of every refresher: ### The idea, ### Key facts, ### Watch out for, ### Worked example.
"""
import os, sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import refreshers_lib


def write(unit_number, entries):
    refreshers_lib.write("ap-calc", unit_number, entries)
