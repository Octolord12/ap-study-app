"""Unit 10, BC-only: infinite sequences and series. Builds the bank from u10_a.py (geometric series, divergence /
integral / p-series tests, comparison tests, alternating series), u10_b.py (ratio test, Taylor polynomials, Lagrange
error bound, radius and interval of convergence), u10_c.py (Maclaurin series, power-series representations) and
u10_frq.py. Writes content/ap-calc-bc/{questions,frqs}/unit-10-bc.json."""
from lib import *
import u10_a, u10_b, u10_c, u10_frq

B = Bank(10, "unit-10-infinite-sequences-and-series")
B.mcq_start, B.frq_start = 1, 1  # unit 10 is all new
for part in (u10_a, u10_b, u10_c, u10_frq):
    part.add(B)
B.save()
B.brief()
