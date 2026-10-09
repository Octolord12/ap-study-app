"""Writes content/ap-world/refreshers/unit-N.json from the u1.py..u9.py scripts in this folder (see ../refreshers_lib.py).

Layout of every refresher: ### The idea, ### Key facts, ### Watch out for, ### Worked example. As in U.S. History, the
worked example is a short-answer prompt and a sketch of a strong response (a claim, specific evidence, the link between them).
Nothing here can be machine-checked: claims are kept to well-established, CED-level facts, and `facts.py` in this folder
checks every named event that is followed by a year against its date table. The owner's review in /admin/review is the
real check. Edit the scripts, not the JSON.
Avoid `$` (a lone dollar sign trips the validator), single-asterisk italics and em dashes.
"""
import os, sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import refreshers_lib


def write(unit_number, entries):
    refreshers_lib.write("ap-world", unit_number, entries)
