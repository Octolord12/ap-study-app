"""Writes content/ap-statistics/course.json and units/unit-1..5.json.

The unit and topic names, their order and the multiple-choice weightings are the AP Statistics Course and Exam
Description's, effective Fall 2026 (the course was redesigned for 2026-27: 5 units, 55 topics; checked 2026-10-26
against the Course at a Glance and the topic pages). A topic's number is its position here, so 3.7 is the seventh
topic of unit 3. The exam format is the CED's Exam Overview: 42 multiple choice and four 10-point free-response
questions as four kinds (see ExamSection.kinds in src/lib/content/schema.ts). Edit this script, not the JSON.
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.normpath(os.path.join(HERE, "../../../content/ap-statistics"))

UNITS = [
    ("Exploring One-Variable Data and Collecting Data", (20, 30), [
        "Introducing Statistics: What Can We Learn from Data?", "Variables", "Tabular Representation and Summary Statistics for One Categorical Variable",
        "Graphical Representations for One Categorical Variable", "Graphical Representations for One Quantitative Variable",
        "Descriptions for One Quantitative Variable Distributions", "Summary Statistics for One Quantitative Variable",
        "Graphical Representations of Summary Statistics for One Quantitative Variable", "Comparisons of the Distributions for One Quantitative Variable",
        "The Investigative Question Revisited and Data Collection", "Random Sampling", "Potential Problems with Sampling", "Experimental Design",
    ]),
    ("Probability, Random Variables, and Probability Distributions", (15, 25), [
        "Tabular and Graphical Representations for the Distributions of Two Categorical Variables", "Summary Statistics for Two Categorical Variables",
        "Estimating Probabilities Using Simulation", "Introduction to Probability", "Mutually Exclusive Events", "Conditional Probability",
        "Independent Events and Unions of Events", "Introduction to Random Variables and Probability Distributions", "Parameters of Random Variables",
        "The Binomial Distribution", "The Normal Distribution", "Sampling Distributions and the Central Limit Theorem",
    ]),
    ("Inference for Categorical Data: Proportions", (15, 25), [
        "Estimators", "Sampling Distributions for Sample Proportions", "Constructing a Confidence Interval for a Population Proportion",
        "Justifying a Claim Based on a Confidence Interval for a Population Proportion", "Setting Up a Test for a Population Proportion", "p-Values",
        "Carrying Out a Test for a Population Proportion", "Potential Errors When Performing Tests", "Sampling Distributions for the Difference Between Sample Proportions",
        "Constructing a Confidence Interval for the Difference Between Two Population Proportions",
        "Justifying a Claim Based on a Confidence Interval for the Difference Between Two Population Proportions",
        "Setting Up a Test for the Difference Between Two Population Proportions", "Carrying Out a Test for the Difference Between Two Population Proportions",
        "Setting Up a Chi-Square Test for Homogeneity or Independence", "Carrying Out a Chi-Square Test for Homogeneity or Independence",
    ]),
    ("Inference for Quantitative Data: Means", (10, 20), [
        "Sampling Distributions for Sample Means", "Constructing a Confidence Interval for a Population Mean or Population Mean Difference",
        "Justifying a Claim Based on a Confidence Interval for a Population Mean or Population Mean Difference",
        "Setting Up a Test for a Population Mean or Population Mean Difference", "Carrying Out a Test for a Population Mean or Population Mean Difference",
        "Sampling Distributions for the Difference Between Two Sample Means", "Constructing a Confidence Interval for the Difference Between Two Population Means",
        "Justifying a Claim Based on a Confidence Interval for the Difference Between Two Population Means",
        "Setting Up a Test for the Difference Between Two Population Means", "Carrying Out a Test for the Difference Between Two Population Means",
    ]),
    ("Regression Analysis", (10, 20), [
        "Graphical Representations Between Two Quantitative Variables", "Correlation", "Linear Regression Models", "Residuals", "Least-Squares Regression",
    ]),
]

# One prompt of each kind on every exam, in this order; each is worth 10 points (CED Exam Overview).
KINDS = ["COLLECT_DATA", "ANALYZE_DATA", "INFERENCE", "MULTI_FOCUS"]
EXPECTED_TOPICS = [13, 12, 15, 10, 5]


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
        "slug": "ap-statistics",
        "name": "AP Statistics",
        "description": "The redesigned 2026-27 course in five units: exploring one-variable data and collecting data, probability and probability distributions, inference for proportions, inference for means, and regression, aligned to the College Board Course and Exam Description.",
        "colorTheme": "indigo",
        "examFormat": {
            "totalDurationMinutes": 180,
            "sections": [
                {"type": "MCQ", "questionCount": 42, "durationMinutes": 90, "scoreWeight": 0.5, "calculatorAllowed": True},
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
        assert len(unit["topics"]) == EXPECTED_TOPICS[n - 1], (n, len(unit["topics"]))
        total += len(unit["topics"])
        with open(os.path.join(OUT, "units", f"unit-{n}.json"), "w") as f:
            json.dump(unit, f, indent=2, ensure_ascii=False)
            f.write("\n")
        print(n, unit["slug"], len(unit["topics"]), "topics")
    print("total topics:", total)
    assert total == 55, total


main()
