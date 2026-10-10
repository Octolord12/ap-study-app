"""Writes content/ap-calc-bc/course.json and units/unit-1..10.json.

Units 1-8 start from Calc AB's unit files (BC contains all of AB) and add the topics the AP Central
Course and Exam Description marks "BC only" or that AB's grouping left out; units 9 and 10 are BC-only.
The weightings are the BC multiple-choice weightings from AP Central (checked 2026-10-09).
Edit this script, not the JSON.
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "../../../content"))
AB = os.path.join(ROOT, "ap-calc", "units")
OUT = os.path.join(ROOT, "ap-calc-bc")

WEIGHTS = {1: (5, 10), 2: (5, 10), 3: (5, 10), 4: (5, 10), 5: (10, 15), 6: (15, 20), 7: (5, 10), 8: (5, 10), 9: (10, 15), 10: (15, 20)}

# (after the AB topic with this slug, new topic). CED numbers in the comments.
EXTRA = {
    6: [
        ("u-substitution", ("long-division-and-completing-the-square", "Long Division and Completing the Square")),  # 6.10
        ("long-division-and-completing-the-square", ("integration-by-parts", "Integration by Parts")),  # 6.11, BC only
        ("integration-by-parts", ("partial-fractions", "Integration Using Linear Partial Fractions")),  # 6.12, BC only
        ("partial-fractions", ("improper-integrals", "Improper Integrals")),  # 6.13, BC only
    ],
    7: [
        ("slope-fields", ("eulers-method", "Euler's Method")),  # 7.5, BC only
        ("exponential-growth-and-decay", ("logistic-models", "Logistic Models")),  # 7.9, BC only
    ],
    8: [
        ("volume-by-disc-washer", ("arc-length-and-distance-traveled", "Arc Length and Distance Traveled")),  # 8.13, BC only
    ],
}

NEW_UNITS = {
    9: ("unit-9-parametric-polar-and-vector-valued-functions", "Parametric Equations, Polar Coordinates, and Vector-Valued Functions", [
        ("parametric-derivatives", "Parametric Equations and Their Derivatives"),  # 9.1, 9.2
        ("parametric-arc-length", "Arc Length of Parametric Curves"),  # 9.3
        ("vector-valued-functions", "Vector-Valued Functions"),  # 9.4, 9.5
        ("motion-in-the-plane", "Motion in the Plane"),  # 9.6
        ("polar-coordinates-and-derivatives", "Polar Coordinates and Their Derivatives"),  # 9.7
        ("area-in-polar-coordinates", "Area in Polar Coordinates"),  # 9.8, 9.9
    ]),
    10: ("unit-10-infinite-sequences-and-series", "Infinite Sequences and Series", [
        ("convergent-and-geometric-series", "Convergent Series and Geometric Series"),  # 10.1, 10.2
        ("divergence-integral-and-p-series", "The nth-Term Test, the Integral Test, and p-Series"),  # 10.3-10.5
        ("comparison-tests", "Comparison Tests"),  # 10.6
        ("alternating-series-and-error-bound", "Alternating Series and the Error Bound"),  # 10.7, 10.10
        ("ratio-test-and-absolute-convergence", "The Ratio Test and Absolute Convergence"),  # 10.8, 10.9
        ("taylor-polynomials", "Taylor Polynomial Approximations"),  # 10.11
        ("lagrange-error-bound", "The Lagrange Error Bound"),  # 10.12
        ("radius-and-interval-of-convergence", "Radius and Interval of Convergence"),  # 10.13
        ("taylor-and-maclaurin-series", "Taylor and Maclaurin Series"),  # 10.14
        ("power-series-representations", "Representing Functions as Power Series"),  # 10.15
    ]),
}


def build_unit(n):
    if n in NEW_UNITS:
        slug, name, topics = NEW_UNITS[n]
        pairs = list(topics)
    else:
        with open(os.path.join(AB, f"unit-{n}.json")) as f:
            ab = json.load(f)
        slug, name = ab["slug"], ab["name"]
        pairs = [(t["slug"], t["name"]) for t in ab["topics"]]
        for after, new in EXTRA.get(n, []):
            at = [s for s, _ in pairs].index(after)
            pairs.insert(at + 1, new)
    lo, hi = WEIGHTS[n]
    return {
        "slug": slug, "order": n, "name": name, "weightingMin": lo, "weightingMax": hi,
        "topics": [{"slug": s, "order": i + 1, "name": t} for i, (s, t) in enumerate(pairs)],
    }


def main():
    os.makedirs(os.path.join(OUT, "units"), exist_ok=True)
    course = {
        "slug": "ap-calc-bc",
        "name": "AP Calculus BC",
        "description": "The full single-variable calculus sequence: everything in AB plus further integration techniques, parametric, polar and vector-valued functions, and infinite sequences and series, aligned to the College Board Course and Exam Description.",
        "colorTheme": "violet",
        "examFormat": {
            "totalDurationMinutes": 190,
            "sections": [
                {"type": "MCQ", "questionCount": 42, "durationMinutes": 100, "scoreWeight": 0.5},
                {"type": "FRQ", "questionCount": 6, "durationMinutes": 90, "scoreWeight": 0.5, "calculatorAllowed": True},
            ],
        },
    }
    with open(os.path.join(OUT, "course.json"), "w") as f:
        json.dump(course, f, indent=2); f.write("\n")
    total = 0
    for n in range(1, 11):
        unit = build_unit(n)
        total += len(unit["topics"])
        with open(os.path.join(OUT, "units", f"unit-{n}.json"), "w") as f:
            json.dump(unit, f, indent=2); f.write("\n")
        print(n, unit["slug"], len(unit["topics"]), "topics")
    print("total topics:", total)


main()
