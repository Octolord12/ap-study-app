"""Writes content/ap-biology/course.json and units/unit-1..8.json.

The unit and topic names, their order and the multiple-choice weightings are the 2025-26 AP Biology Course and
Exam Description's (checked 2026-10-11: 8 units, 60 topics; a topic's number is its position here, so 7.5 is
the fifth topic of unit 7). The exam format is the CED's Exam Overview, with the six free-response questions
as six kinds (see ExamSection.kinds in src/lib/content/schema.ts). Edit this script, not the JSON.
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.normpath(os.path.join(HERE, "../../../content/ap-biology"))

UNITS = [
    ("Chemistry of Life", (8, 11), [
        "Structure of Water and Hydrogen Bonding", "Elements of Life", "Introduction to Macromolecules", "Carbohydrates", "Lipids",
        "Nucleic Acids", "Proteins",
    ]),
    ("Cells", (10, 13), [
        "Cell Structure and Function", "Cell Size", "Plasma Membrane", "Membrane Permeability", "Membrane Transport", "Facilitated Diffusion",
        "Tonicity and Osmoregulation", "Mechanisms of Transport", "Cell Compartmentalization", "Origins of Cell Compartmentalization",
    ]),
    ("Cellular Energetics", (12, 16), [
        "Enzymes", "Environmental Impacts on Enzyme Function", "Cellular Energy", "Photosynthesis", "Cellular Respiration",
    ]),
    ("Cell Communication and Cell Cycle", (10, 15), [
        "Cell Communication", "Introduction to Signal Transduction", "Signal Transduction Pathways", "Feedback", "Cell Cycle", "Regulation of Cell Cycle",
    ]),
    ("Heredity", (8, 11), [
        "Meiosis", "Meiosis and Genetic Diversity", "Mendelian Genetics", "Non-Mendelian Genetics", "Environmental Effects on Phenotype",
    ]),
    ("Gene Expression and Regulation", (12, 16), [
        "DNA and RNA Structure", "DNA Replication", "Transcription and RNA Processing", "Translation", "Regulation of Gene Expression",
        "Gene Expression and Cell Specialization", "Mutations", "Biotechnology",
    ]),
    ("Natural Selection", (13, 20), [
        "Introduction to Natural Selection", "Natural Selection", "Artificial Selection", "Population Genetics", "Hardy–Weinberg Equilibrium",
        "Evidence of Evolution", "Common Ancestry", "Continuing Evolution", "Phylogeny", "Speciation", "Variations in Populations",
        "Origins of Life on Earth",
    ]),
    ("Ecology", (10, 15), [
        "Responses to the Environment", "Energy Flow Through Ecosystems", "Population Ecology", "Effect of Density on Populations",
        "Community Ecology", "Biodiversity", "Disruptions in Ecosystems",
    ]),
]

# One prompt of each kind on every exam, in this order; Q1 and Q2 are worth 9 points, Q3-Q6 four.
KINDS = ["RESULTS", "RESULTS_GRAPH", "INVESTIGATION", "CONCEPT", "MODEL", "DATA"]


def slugify(text: str) -> str:
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", text.lower())).strip("-")


def build_unit(n: int):
    name, (lo, hi), topics = UNITS[n - 1]
    slugs = [slugify(t) for t in topics]
    assert len(set(slugs)) == len(slugs), f"duplicate topic slug in unit {n}"
    return {
        "slug": f"unit-{n}-{slugify(name)}", "order": n, "name": name, "weightingMin": lo, "weightingMax": hi,
        "topics": [{"slug": s, "order": i + 1, "name": t} for i, (s, t) in enumerate(zip(slugs, topics))],
    }


def main():
    os.makedirs(os.path.join(OUT, "units"), exist_ok=True)
    course = {
        "slug": "ap-biology",
        "name": "AP Biology",
        "description": "The full course in eight units, from the chemistry of life and cells through energetics, cell communication, heredity and gene expression to natural selection and ecology, aligned to the College Board Course and Exam Description.",
        "colorTheme": "teal",
        "examFormat": {
            "totalDurationMinutes": 180,
            "sections": [
                {"type": "MCQ", "questionCount": 60, "durationMinutes": 90, "scoreWeight": 0.5, "calculatorAllowed": True},
                {"type": "FRQ", "questionCount": len(KINDS), "durationMinutes": 90, "scoreWeight": 0.5, "calculatorAllowed": True, "kinds": KINDS},
            ],
        },
    }
    with open(os.path.join(OUT, "course.json"), "w") as f:
        json.dump(course, f, indent=2, ensure_ascii=False)
        f.write("\n")
    total = 0
    for n in range(1, len(UNITS) + 1):
        unit = build_unit(n)
        total += len(unit["topics"])
        with open(os.path.join(OUT, "units", f"unit-{n}.json"), "w") as f:
            json.dump(unit, f, indent=2, ensure_ascii=False)
            f.write("\n")
        print(n, unit["slug"], len(unit["topics"]), "topics")
    print("total topics:", total)
    assert total == 60, total


main()
