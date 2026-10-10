"""Unit 9, BC-only: parametric equations, polar coordinates, vector-valued functions.
Builds the bank from u9_a.py (parametric derivatives, arc length), u9_b.py (vector-valued functions,
motion in the plane) and u9_c.py (polar). Writes content/ap-calc-bc/{questions,frqs}/unit-9-bc.json."""
from lib import *
import u9_a, u9_b, u9_c, u9_frq

B = Bank(9, "unit-9-parametric-polar-and-vector-valued-functions")
# unit 9 is all new, so its ids start at 1 (the other units continue after the copied Calc AB items)
B.mcq_start, B.frq_start = 1, 1
for part in (u9_a, u9_b, u9_c, u9_frq):
    part.add(B)
B.save()
B.brief()
