"""Writes content/ap-us-history/refreshers/unit-N.json from the u1.py..u9.py scripts in this folder (see ../refreshers_lib.py).

Layout of every refresher: ### The idea, ### Key facts, ### Watch out for, ### Worked example. In history the worked
example is a short-answer prompt and a sketch of a strong response (a claim, specific evidence, the link between them).
Nothing here can be machine-checked the way Calc/Physics/CSA are: claims are kept to well-established, CED-level facts, and
`../ap-us-history/facts.py` checks every named event that is followed by a year against its date table (it now reads the
refreshers too). The owner's review in /admin/review is the real check. Edit the scripts, not the JSON.
Avoid single-asterisk italics (the renderer prints the asterisks) and em dashes.
"""
import os, sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import refreshers_lib


def write(unit_number, entries):
    refreshers_lib.write("ap-us-history", unit_number, entries)
