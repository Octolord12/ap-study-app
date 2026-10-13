"""Helpers for Unit 6: the standard genetic code (used only to compute answers; the memorization of the code is outside the AP exam, so any
question that needs it prints the codons it uses in a table) and strand arithmetic (complement, transcription, translation)."""
from lib import table

_BASES = "UCAG"
_AAS = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
CODON = {a + b + c: _AAS[16 * i + 4 * j + k] for i, a in enumerate(_BASES) for j, b in enumerate(_BASES) for k, c in enumerate(_BASES)}
NAME = {"F": "Phe", "L": "Leu", "S": "Ser", "Y": "Tyr", "C": "Cys", "W": "Trp", "P": "Pro", "H": "His", "Q": "Gln", "R": "Arg", "I": "Ile",
        "M": "Met", "T": "Thr", "N": "Asn", "K": "Lys", "V": "Val", "A": "Ala", "D": "Asp", "E": "Glu", "G": "Gly", "*": "Stop"}

assert len(CODON) == 64 and CODON["AUG"] == "M" and CODON["UGG"] == "W" and {CODON[c] for c in ("UAA", "UAG", "UGA")} == {"*"}
assert sum(1 for v in CODON.values() if v == "L") == 6 and sum(1 for v in CODON.values() if v == "M") == 1


def amino(codon):
    """Three-letter name of the amino acid (or 'Stop') for an RNA codon."""
    return NAME[CODON[codon]]


def codons(mrna):
    return [mrna[i:i + 3] for i in range(0, len(mrna) - len(mrna) % 3, 3)]


def translate(mrna, from_start=True):
    """Three-letter names from the first AUG (or from the first base) until a stop codon; the stop is not included."""
    s = mrna
    if from_start:
        s = mrna[mrna.index("AUG"):]
    out = []
    for c in codons(s):
        a = amino(c)
        if a == "Stop":
            break
        out.append(a)
    return out


def complement_dna(s):
    return s.translate(str.maketrans("ACGT", "TGCA"))


def reverse_complement(s):
    return complement_dna(s)[::-1]


def transcribe(template_3_to_5):
    """The mRNA, written 5' to 3', made from a template strand that is written 3' to 5'."""
    return template_3_to_5.translate(str.maketrans("ACGT", "UGCA"))


def codon_table(cds, caption="Some mRNA codons and the amino acids that they code for"):
    """A data-table diagram listing exactly the codons in `cds` (a list of mRNA codons), in the order given."""
    rows = [(c, amino(c)) for c in cds]
    return table(["mRNA codon (5' to 3')", "Amino acid"], rows, caption=caption, row_headers=True)
