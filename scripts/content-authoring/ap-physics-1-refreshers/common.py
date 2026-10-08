"""Writes content/ap-physics-1/refreshers/unit-N.json from the u1.py..u8.py scripts in this folder (see ../refreshers_lib.py).

Each script holds one refresher per topic (markdown, KaTeX in $...$) and re-computes its worked examples in Python
before writing (`eq`), so a number in the text cannot drift from the arithmetic. g = 9.8 m/s^2 throughout, as in the
question bank. Edit the scripts, not the JSON.
Layout of every refresher: ### The idea, ### Key facts, ### Watch out for, ### Worked example.
"""
import math, os, sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import refreshers_lib

g = 9.8
G = 6.67e-11
M_EARTH = 5.97e24
R_EARTH = 6.37e6
sin, cos, sqrt, pi = math.sin, math.cos, math.sqrt, math.pi
rad = math.radians


def eq(value, shown, digits=None):
    """Assert that a computed value equals the number printed in the text, to `digits` decimal places
    (or to `shown`'s own precision when digits is None)."""
    if digits is None:
        digits = max(0, len(str(shown).split(".")[1])) if "." in str(shown) else 0
    assert round(value, digits) == shown, f"computed {value!r}, text says {shown!r}"


def sig(value, shown, figures):
    """Same, to a number of significant figures (for answers such as 8.0e-8 or 7670)."""
    assert float(f"{value:.{figures - 1}e}") == shown, f"computed {value!r}, text says {shown!r}"


def write(unit_number, entries):
    refreshers_lib.write("ap-physics-1", unit_number, entries)
