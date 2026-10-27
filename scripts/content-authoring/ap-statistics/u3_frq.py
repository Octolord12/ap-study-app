"""Unit 3 free response: one COLLECT_DATA prompt, six INFERENCE prompts (the exam's Question 3) and two MULTI_FOCUS prompts, 10 points each (one point per rubric line, in the order of the parts).

  C1 3.12 design a randomized experiment to compare two proportions          I1 3.3/3.4 a one-proportion z-interval and a claim          I2 3.7 a one-proportion z-test
  I3 3.10/3.11 a two-proportion z-interval and a claim                       I4 3.13 a two-proportion z-test in an experiment            I5 3.15 a chi-square test for independence
  I6 3.15 a chi-square test for homogeneity in an experiment                 M1 3.2/3.8 a sampling distribution, a probability and Type I and II errors   M2 3.3 sample size, a random sample and bias, an interval
Every number is computed here from the data that is shown or described.
"""
from scipy import stats as sps

from lib import *


def L(*lines):
    return [(1, t) for t in lines]


def fx(v, p=2):
    return f"{v:.{p}f}"


def build(B):
    # ----------------------------------------------------------------------------------------------------------- C1: design an experiment
    setup = ("A teacher wants to find out whether sending a text-message reminder the evening before an assignment is due increases the proportion of students who turn the assignment in on time. "
             "Sixty students in the teacher's classes agree to take part and to receive a text message on their phone if they are asked to.")
    parts = [("A", "Identify the experimental units, the treatments, and the response variable for an experiment that the teacher could carry out."),
             ("B", "Describe how the teacher could use a random process to assign the students to the treatments."),
             ("C", "Describe one way that the teacher could reduce the chance that other differences between the two groups, such as the assignment itself, affect the results."),
             ("D", "State the statistics that the teacher should calculate from the data, and say how the teacher should compare the two groups."),
             ("E", "Suppose that the difference in the proportions turned in on time is too large to be explained by chance alone. What conclusion can the teacher make, and for which students does it apply?")]
    ans = [("A", "The experimental units are the 60 students. The treatments are receiving the text-message reminder and not receiving a reminder (the control). The response variable is whether the student turns in the assignment on time."),
           ("B", "Number the students from 1 to 60. Use a random number generator to select 30 different numbers, and assign the students with those numbers to the reminder group. The other 30 students are the control group."),
           ("C", "Give both groups the same assignment with the same due date, and give both groups the same instructions, so that the only difference is the text message. (The teacher could also have someone who does not know the group record who turned in the work.)"),
           ("D", "Calculate the proportion of students who turned in the assignment on time in each group, p̂₁ for the reminder group and p̂₂ for the control group, and compare them using the difference p̂₁ - p̂₂."),
           ("E", "Because the students were randomly assigned to the treatments, the teacher can conclude that the reminder caused the greater proportion of students to turn in the assignment on time. The conclusion applies to students like those in the experiment (the volunteers), and not to all students.")]
    prompt, sample = frq_text(setup, parts, ans)
    B.frq(12, "COLLECT_DATA", prompt,
          L("A: Identifies the experimental units as the students.",
            "A: Identifies the treatments (a reminder and no reminder) and the response variable (turned in on time).",
            "B: Describes a random process for the assignment (such as a random number generator or drawing names).",
            "B: States that the students are divided into two groups, with each student having a chance of being in either group (for example 30 and 30).",
            "C: Describes a way to reduce other sources of variation (the same assignment and due date for both groups, or blinding).",
            "D: States that the proportion on time should be calculated in each group.",
            "D: States that the groups are compared with the difference in the proportions.",
            "E: States a cause-and-effect conclusion, because of random assignment.",
            "E: States that the conclusion applies to similar students (the volunteers), not to all students.",
            "E: Gives the conclusion in context, in terms of the reminder and turning in the assignment on time."),
          sample)

    # ----------------------------------------------------------------------------------------------------------- I1: one-proportion interval
    n1_, x1_ = 400, 172
    ci = prop_ci(x1_, n1_, 0.95)
    assert ci.hi < 0.50 and ci.x >= 10 and n1_ - ci.x >= 10
    setup = ("A city has about 120,000 adults. A transportation department selected a random sample of 400 adults from the city and asked each adult whether he or she rides a city bus at least once a week. In the sample, 172 of the adults said that they do.")
    parts = [("A", "Identify the appropriate inference procedure for estimating the proportion of all adults in the city who ride a city bus at least once a week, and state the parameter in context."),
             ("B", "Verify that the conditions for this procedure are met."),
             ("C", "Construct and show the work for a 95% confidence interval for the proportion of all adults in the city who ride a city bus at least once a week."),
             ("D", "Interpret the interval from part C in context."),
             ("E", "A city official claims that half of all adults in the city ride a city bus at least once a week. Does the interval provide convincing evidence against the claim? Justify your answer.")]
    ans = [("A", "A one-sample z-interval for a population proportion. The parameter is p, the proportion of all adults in the city who ride a city bus at least once a week."),
           ("B", f"Randomization: the adults are a random sample from the city. 10% condition: the sample size of 400 is less than 10% of the 120,000 adults in the city. Normality: the numbers of successes and failures are {x1_} and {n1_ - x1_}, which are both at least 10."),
           ("C", f"p̂ = {x1_} / {n1_} = {fx(ci.phat, 3)}. The interval is p̂ ± $z^*$√(p̂(1 - p̂) / n) = {fx(ci.phat, 3)} ± 1.96√({fx(ci.phat, 3)}(1 - {fx(ci.phat, 3)}) / {n1_}) = {fx(ci.phat, 3)} ± {fx(ci.moe, 4)}, which is ({fx(ci.lo, 3)}, {fx(ci.hi, 3)})."),
           ("D", f"We are 95% confident that the interval from {fx(ci.lo, 3)} to {fx(ci.hi, 3)} contains the proportion of all adults in the city who ride a city bus at least once a week."),
           ("E", f"Yes. The value 0.50 is not in the interval ({fx(ci.lo, 3)}, {fx(ci.hi, 3)}), so 0.50 is not a plausible value for the proportion. All plausible values are less than 0.50, so the interval provides convincing evidence that fewer than half of the adults ride a city bus at least once a week.")]
    prompt, sample = frq_text(setup, parts, ans)
    B.frq(3, "INFERENCE", prompt,
          L("A: Identifies a one-sample z-interval for a population proportion.",
            "A: States the parameter in context: the proportion of all adults in the city who ride a city bus at least once a week.",
            "B: Verifies the randomization condition and the 10% condition (400 is less than 10% of 120,000).",
            f"B: Verifies the normality condition with the counts {x1_} and {n1_ - x1_} (both at least 10).",
            f"C: Gives the correct formula with the values substituted (p̂ = {fx(ci.phat, 3)}, $z^*$ = 1.96, n = {n1_}).",
            f"C: Gives the interval ({fx(ci.lo, 3)}, {fx(ci.hi, 3)}).",
            "D: Interprets the confidence level (95% confident).",
            "D: States that the interval is for the proportion of all adults in the city who ride a city bus at least once a week.",
            "E: States that 0.50 is not in the interval, so it is not a plausible value.",
            "E: Concludes that there is convincing evidence against the claim (the proportion is less than 0.50)."),
          sample)

    # ----------------------------------------------------------------------------------------------------------- I2: one-proportion test
    n2_, x2_, p0 = 150, 71, 0.40
    t = prop_z(x2_, n2_, p0, "gt")
    assert t.p < 0.05 and n2_ * p0 >= 10 and n2_ * (1 - p0) >= 10
    setup = ("A company that runs a gym says that 40% of its members renew their membership each year. The manager thinks that the proportion has increased after a change in the price. The manager selected a random sample of 150 members from the company's very large membership list, and 71 of them renewed.")
    parts = [("A", "State the appropriate null and alternative hypotheses for a test of the manager's belief. Define any parameter that you use."),
             ("B", "Verify that the conditions for the test are met."),
             ("C", "Calculate the test statistic and the p-value for the test."),
             ("D", "Using a significance level of α = 0.05, state a conclusion for the test in context, and justify your conclusion."),
             ("E", "Describe a Type I error in the context of this test, and give its probability.")]
    ans = [("A", f"Let p be the proportion of all of the company's members who renew their membership. H₀: p = {fx(p0)} and Hₐ: p > {fx(p0)}."),
           ("B", f"Randomization: the members are a random sample from the membership list. 10% condition: 150 is less than 10% of a very large membership. Normality: n p₀ = {n2_}({fx(p0)}) = {n2_ * p0:.0f} and n(1 - p₀) = {n2_}({fx(1 - p0)}) = {n2_ * (1 - p0):.0f}, which are both at least 10."),
           ("C", f"p̂ = {x2_} / {n2_} = {fx(t.phat, 4)}. z = ({fx(t.phat, 4)} - {fx(p0)}) / √({fx(p0)}(1 - {fx(p0)}) / {n2_}) = {fx(t.z)}. The p-value is P(z ≥ {fx(t.z)}) = {fx(t.p, 3)}."),
           ("D", f"The p-value {fx(t.p, 3)} is less than α = 0.05, so reject the null hypothesis. There is convincing statistical evidence that the proportion of all of the company's members who renew their membership is greater than 0.40."),
           ("E", "A Type I error is concluding that there is convincing evidence that the proportion of all members who renew is greater than 0.40 when the proportion is actually 0.40. The probability of a Type I error is the significance level, α = 0.05.")]
    prompt, sample = frq_text(setup, parts, ans)
    B.frq(7, "INFERENCE", prompt,
          L(f"A: States the hypotheses H₀: p = {fx(p0)} and Hₐ: p > {fx(p0)}.",
            "A: Defines p as the proportion of all of the company's members who renew their membership.",
            "B: Verifies the randomization condition and the 10% condition.",
            f"B: Verifies the normality condition using the null value (n p₀ = {n2_ * p0:.0f} and n(1 - p₀) = {n2_ * (1 - p0):.0f}, both at least 10).",
            f"C: Calculates the test statistic z = {fx(t.z)}.",
            f"C: Calculates the p-value {fx(t.p, 3)}.",
            "D: Compares the p-value with α = 0.05 and rejects the null hypothesis.",
            "D: States a conclusion in context, in terms of the alternative (convincing evidence that the proportion who renew is greater than 0.40).",
            "E: Describes a Type I error in context (convincing evidence of an increase when the proportion is still 0.40).",
            "E: States that the probability of a Type I error is α = 0.05."),
          sample)

    # ----------------------------------------------------------------------------------------------------------- I3: two-proportion interval
    xa, na, xb, nb = 132, 220, 105, 240
    c2 = two_prop_ci(xa, na, xb, nb, 0.95)
    assert c2.lo > 0 and min(xa, na - xa, xb, nb - xb) >= 10
    setup = ("A district wants to compare how students at two large high schools feel about starting the school day later. A random sample of 220 students from School A and an independent random sample of 240 students from School B were each asked whether they favor a later start time. "
             f"In the School A sample, {xa} students favor a later start time, and in the School B sample, {xb} students favor it.")
    parts = [("A", "Identify the appropriate inference procedure for estimating the difference between the proportions of all students at the two schools who favor a later start time, and state the parameter in context."),
             ("B", "Verify that the conditions for the procedure are met."),
             ("C", "Construct and show the work for a 95% confidence interval for the difference in the proportions of all students at the two schools who favor a later start time, School A minus School B."),
             ("D", "Interpret the interval from part C in context."),
             ("E", "Does the interval provide convincing evidence of a difference between the proportions of all students at the two schools who favor a later start time? Justify your answer.")]
    ans = [("A", "A two-sample z-interval for a difference between population proportions. The parameter is p₁ - p₂, where p₁ is the proportion of all students at School A who favor a later start time and p₂ is the proportion of all students at School B who favor a later start time."),
           ("B", f"Randomization: the data come from two independent random samples. 10% condition: each sample is less than 10% of the students at its (large) school. Normality: the numbers of successes and failures are {xa} and {na - xa} for School A and {xb} and {nb - xb} for School B, all at least 10."),
           ("C", f"p̂₁ = {xa} / {na} = {fx(c2.p1, 3)} and p̂₂ = {xb} / {nb} = {fx(c2.p2, 4)}. The interval is ({fx(c2.p1, 3)} - {fx(c2.p2, 4)}) ± 1.96√({fx(c2.p1, 3)}(1 - {fx(c2.p1, 3)}) / {na} + {fx(c2.p2, 4)}(1 - {fx(c2.p2, 4)}) / {nb}) = {fx(c2.diff, 4)} ± {fx(c2.moe, 4)}, which is ({fx(c2.lo, 3)}, {fx(c2.hi, 3)})."),
           ("D", f"We are 95% confident that the interval from {fx(c2.lo, 3)} to {fx(c2.hi, 3)} contains the difference between the proportion of all students at School A and the proportion of all students at School B who favor a later start time."),
           ("E", f"Yes. The interval ({fx(c2.lo, 3)}, {fx(c2.hi, 3)}) does not contain 0, and all of its values are positive, so there is convincing evidence that the proportion of all students who favor a later start time is greater at School A than at School B.")]
    prompt, sample = frq_text(setup, parts, ans)
    B.frq(10, "INFERENCE", prompt,
          L("A: Identifies a two-sample z-interval for a difference between population proportions.",
            "A: States the parameter in context: the difference between the proportions of all students at School A and at School B who favor a later start time.",
            "B: Verifies the randomization condition (two independent random samples) and the 10% condition for each sample.",
            "B: Verifies the normality condition with the four counts (successes and failures in both samples, all at least 10).",
            f"C: Gives the correct formula with the values substituted (p̂₁ = {fx(c2.p1, 3)}, p̂₂ = {fx(c2.p2, 4)}, $z^*$ = 1.96).",
            f"C: Gives the interval ({fx(c2.lo, 3)}, {fx(c2.hi, 3)}).",
            "D: Interprets the confidence level (95% confident).",
            "D: States that the interval is for the difference in the two population proportions, in context.",
            "E: States that the interval does not contain 0.",
            "E: Concludes that the proportion is greater at School A (convincing evidence of a difference)."),
          sample)

    # ----------------------------------------------------------------------------------------------------------- I4: two-proportion test (experiment)
    x1e, n1e, x2e, n2e = 52, 80, 38, 80
    tz = two_prop_z(x1e, n1e, x2e, n2e, "gt")
    assert tz.p < 0.05
    setup = ("A teacher randomly assigned 160 volunteer students to two groups of 80. The students in Group 1 studied for a test with a new study app, and the students in Group 2 studied with a notebook. "
             f"Then all of the students took the same test. In Group 1, {x1e} of the 80 students passed the test, and in Group 2, {x2e} of the 80 students passed. The teacher believes that the app increases the proportion of students like these who pass.")
    parts = [("A", "State the appropriate null and alternative hypotheses for a test of the teacher's belief. Define any parameters that you use."),
             ("B", "Verify that the conditions for the test are met."),
             ("C", "Calculate the test statistic and the p-value for the test."),
             ("D", "Using a significance level of α = 0.05, state a conclusion for the test in context, and justify your conclusion."),
             ("E", "Can the teacher conclude that the app causes a greater proportion of students to pass? Can the conclusion be applied to all students? Justify your answers.")]
    ans = [("A", "Let p₁ be the proportion of students like these who would pass the test after studying with the app, and let p₂ be the proportion who would pass after studying with a notebook. H₀: p₁ - p₂ = 0 and Hₐ: p₁ - p₂ > 0."),
           ("B", f"Randomization: the students were randomly assigned to the two treatments (the 10% condition is not needed for an experiment). Normality: the combined proportion is $\\hat{{p}}_c$ = ({x1e} + {x2e}) / ({n1e} + {n2e}) = {fx(tz.pc, 4)}, and n$\\hat{{p}}_c$ = {n1e * tz.pc:.1f} and n(1 - $\\hat{{p}}_c$) = {n1e * (1 - tz.pc):.1f} for both groups, all at least 10."),
           ("C", f"p̂₁ = {fx(tz.p1, 4)} and p̂₂ = {fx(tz.p2, 4)}. z = ({fx(tz.p1, 4)} - {fx(tz.p2, 4)}) / √({fx(tz.pc, 4)}(1 - {fx(tz.pc, 4)})(1/{n1e} + 1/{n2e})) = {fx(tz.z)}. The p-value is P(z ≥ {fx(tz.z)}) = {fx(tz.p, 3)}."),
           ("D", f"The p-value {fx(tz.p, 3)} is less than α = 0.05, so reject the null hypothesis. There is convincing statistical evidence that the proportion of students like these who would pass after studying with the app is greater than the proportion who would pass after studying with a notebook."),
           ("E", "Yes, the teacher can conclude that the app causes the greater proportion to pass, because the students were randomly assigned to the two treatments. No, the conclusion cannot be applied to all students, because the students were volunteers and not a random sample of all students; it applies to students like those in the experiment.")]
    prompt, sample = frq_text(setup, parts, ans)
    B.frq(13, "INFERENCE", prompt,
          L("A: States H₀: p₁ - p₂ = 0 and Hₐ: p₁ - p₂ > 0.",
            "A: Defines the parameters in context (the proportions of students like these who would pass with the app and with a notebook).",
            "B: Verifies the randomization condition (random assignment; the 10% condition is not needed).",
            f"B: Verifies the normality condition using the combined proportion ({fx(tz.pc, 4)}); all four expected counts are at least 10.",
            f"C: Calculates the test statistic z = {fx(tz.z)}, using the combined proportion in the standard error.",
            f"C: Calculates the p-value {fx(tz.p, 3)}.",
            "D: Compares the p-value with α = 0.05 and rejects the null hypothesis.",
            "D: States a conclusion in context, in terms of the alternative (convincing evidence that the proportion who pass is greater with the app).",
            "E: States that a cause-and-effect conclusion is justified because of the random assignment.",
            "E: States that the conclusion applies to students like the volunteers, not to all students."),
          sample)

    # ----------------------------------------------------------------------------------------------------------- I5: chi-square independence
    obs5 = [[60, 25, 15], [45, 35, 20], [25, 35, 40]]
    k5 = chi_square(obs5)
    assert k5.expected.min() > 5 and k5.p < 0.0001
    _srt = sorted(k5.contrib.ravel())
    assert _srt[-1] - _srt[-2] > 0.3, _srt[-3:]
    tb5 = twoway("Age group", ["Online", "Television", "Print"], ["Under 30", "30 to 49", "50 or over"], obs5, caption="Main way of getting news, for 300 adults")
    top5 = np.unravel_index(k5.contrib.argmax(), k5.contrib.shape)
    names_r, names_c = ["under 30", "30 to 49", "50 or over"], ["online", "from television", "from print"]
    setup = ("A researcher selected a random sample of 300 adults from a large city and asked each adult for his or her age group and the main way that he or she gets news. The table shows the counts.")
    parts = [("A", "State the appropriate null and alternative hypotheses for a test of whether there is an association between age group and the main way of getting news for adults in the city."),
             ("B", "Verify that the conditions for the test are met."),
             ("C", "Calculate the expected count for the adults who are under 30 and get news mainly online, and calculate the test statistic and the degrees of freedom."),
             ("D", "The p-value for the test is less than 0.0001. Using a significance level of α = 0.05, state a conclusion for the test in context, and justify your conclusion."),
             ("E", "Which cell of the table contributes the most to the chi-square statistic? Justify your answer.")]
    e11 = k5.expected[0][0]
    ans = [("A", "H₀: There is no association between age group and the main way of getting news for the adults in the city (the variables are independent). Hₐ: There is an association between age group and the main way of getting news for the adults in the city."),
           ("B", f"Randomization: the data are a random sample of adults from the city. 10% condition: 300 is less than 10% of the adults in a large city. Expected counts: all of the expected counts are greater than 5 (the smallest is {k5.expected.min():.1f})."),
           ("C", f"Expected count = (100)(130) / 300 = {e11:.1f}. χ² = Σ (observed - expected)² / expected = {k5.chi2:.2f}, with df = (3 - 1)(3 - 1) = {k5.df}."),
           ("D", "The p-value is less than 0.0001, which is less than α = 0.05, so reject the null hypothesis. There is convincing statistical evidence of an association between age group and the main way of getting news for the adults in the city."),
           ("E", f"The adults who are {names_r[top5[0]]} and get news mainly {names_c[top5[1]]} contribute the most. The contribution (observed - expected)² / expected is ({obs5[top5[0]][top5[1]]} - {k5.expected[top5[0]][top5[1]]:.1f})² / {k5.expected[top5[0]][top5[1]]:.1f} = {k5.contrib.max():.2f}, the largest of the nine cells.")]
    prompt, sample = frq_text(setup, parts, ans)
    B.frq(15, "INFERENCE", prompt,
          L("A: States the null hypothesis: no association between age group and the main way of getting news (independence), in context.",
            "A: States the alternative hypothesis: there is an association, in context.",
            "B: Verifies the randomization condition and the 10% condition.",
            "B: Verifies the expected counts condition (all expected counts greater than 5), with the smallest expected count or a statement about the expected counts.",
            f"C: Calculates the expected count {e11:.1f}.",
            f"C: Calculates the test statistic {k5.chi2:.2f}.",
            f"C: Gives the degrees of freedom {k5.df}.",
            "D: Compares the p-value with α = 0.05 and rejects the null hypothesis.",
            "D: States a conclusion in context (convincing evidence of an association between age group and the main way of getting news).",
            f"E: Identifies the cell with the largest contribution ({names_r[top5[0]]}, {names_c[top5[1]]}: {k5.contrib.max():.2f}) with a justification."),
          sample, diagram=tb5)

    # ----------------------------------------------------------------------------------------------------------- I6: chi-square homogeneity (experiment)
    obs6 = [[30, 15, 5], [22, 18, 10], [12, 20, 18]]
    k6 = chi_square(obs6)
    assert k6.expected.min() > 5 and k6.p < 0.01
    tb6 = twoway("Treatment", ["Improved", "Stayed the same", "Got worse"], ["Treatment A", "Treatment B", "Treatment C"], obs6, caption="Outcomes of 150 patients")
    setup = ("In a study of three treatments for back pain, 150 volunteer patients were randomly assigned to Treatment A, Treatment B or Treatment C, 50 patients to each. After 6 weeks, each patient was classified as improved, stayed the same, or got worse. The table shows the counts.")
    parts = [("A", "Identify the appropriate test for determining whether the distribution of the outcome is different for the three treatments, and state the null and alternative hypotheses."),
             ("B", "Verify that the conditions for the test are met."),
             ("C", "Calculate the test statistic and the degrees of freedom."),
             ("D", f"The p-value for the test is {k6.p:.4f}. Using a significance level of α = 0.05, state a conclusion for the test in context, and justify your conclusion."),
             ("E", "Does the conclusion support a cause-and-effect relationship between the treatment and the outcome? Does it apply to all patients with back pain? Justify your answers.")]
    ans = [("A", "A chi-square test for homogeneity. H₀: There is no difference in the distribution of the outcome (improved, stayed the same, got worse) across the three treatments. Hₐ: There is a difference in the distribution of the outcome across the three treatments."),
           ("B", f"Randomization: the patients were randomly assigned to the treatments (the 10% condition is not needed for an experiment). Expected counts: all of the expected counts are greater than 5 (the smallest is {k6.expected.min():.1f})."),
           ("C", f"χ² = Σ (observed - expected)² / expected = {k6.chi2:.2f}, and df = (3 - 1)(3 - 1) = {k6.df}."),
           ("D", f"The p-value {k6.p:.4f} is less than α = 0.05, so reject the null hypothesis. There is convincing statistical evidence that the distribution of the outcome is different for at least one of the three treatments."),
           ("E", "Yes, because the patients were randomly assigned to the treatments, a difference in the distributions of the outcome that is too large to be due to chance can be attributed to the treatments. No, the patients were volunteers and not a random sample of all patients with back pain, so the conclusion applies to patients like those in the study.")]
    prompt, sample = frq_text(setup, parts, ans)
    B.frq(15, "INFERENCE", prompt,
          L("A: Identifies a chi-square test for homogeneity.",
            "A: States H₀ (no difference in the distribution of the outcome across the treatments) and Hₐ (a difference), in context.",
            "B: Verifies the randomization condition (random assignment; no 10% condition).",
            "B: Verifies the expected counts condition (all greater than 5).",
            f"C: Calculates the test statistic {k6.chi2:.2f}.",
            f"C: Gives the degrees of freedom {k6.df}.",
            "D: Compares the p-value with α = 0.05 and rejects the null hypothesis.",
            "D: States a conclusion in context (the distribution of the outcome is different for at least one treatment).",
            "E: Says a cause-and-effect conclusion is justified because of the random assignment.",
            "E: Says the conclusion applies to patients like the volunteers, not to all patients with back pain."),
          sample, diagram=tb6)

    # ----------------------------------------------------------------------------------------------------------- M1: sampling distribution and errors
    pM, nM = 0.30, 100
    sdM = math.sqrt(pM * (1 - pM) / nM)
    zM = (0.38 - pM) / sdM
    pgM = float(sps.norm.sf(zM))
    assert nM * pM >= 10 and nM * (1 - pM) >= 10
    setup = ("A company says that 30% of the visits to its website end with a click on an advertisement. A marketing analyst believes that the proportion is greater than 30%. "
             "The analyst plans to take a random sample of 100 visits from the very large number of visits to the website, and to test the company's claim at the significance level α = 0.05.")
    parts = [("A", "Suppose that the company's claim is correct. Find the mean and the standard deviation of the sampling distribution of the sample proportion $\\hat{p}$ for random samples of 100 visits."),
             ("B", "Verify that the sampling distribution of $\\hat{p}$ can be approximated by a normal distribution."),
             ("C", "Suppose that the company's claim is correct. Calculate the probability that the proportion of the 100 visits in the sample that end with a click is 0.38 or greater."),
             ("D", "Describe a Type I error in the context of this test, and give its probability."),
             ("E", "Describe a Type II error in the context of this test. State one change to the study that would decrease the probability of a Type II error.")]
    ans = [("A", f"μ = p = 0.30 and σ = √(p(1 - p) / n) = √(0.30(0.70) / 100) = {fx(sdM, 4)}."),
           ("B", f"The visits are a random sample, 100 is less than 10% of a very large number of visits, and n p = 100(0.30) = {nM * pM:.0f} and n(1 - p) = 100(0.70) = {nM * (1 - pM):.0f} are both at least 10, so the sampling distribution is approximately normal."),
           ("C", f"z = (0.38 - 0.30) / {fx(sdM, 4)} = {fx(zM)}, so P($\\hat{{p}}$ ≥ 0.38) = P(z ≥ {fx(zM)}) = {fx(pgM, 3)}."),
           ("D", "A Type I error is concluding that there is convincing evidence that the proportion of visits that end with a click is greater than 0.30, when the proportion is actually 0.30. Its probability is the significance level, 0.05."),
           ("E", "A Type II error is concluding that there is not convincing evidence that the proportion of visits that end with a click is greater than 0.30, when it is actually greater than 0.30. Increasing the sample size (or increasing the significance level) would decrease the probability of a Type II error.")]
    prompt, sample = frq_text(setup, parts, ans)
    B.frq(2, "MULTI_FOCUS", prompt,
          L("A: States the mean of the sampling distribution as 0.30.",
            f"A: Calculates the standard deviation {fx(sdM, 4)}.",
            "B: Verifies the randomization and 10% conditions.",
            f"B: Verifies that n p and n(1 - p) are both at least 10 ({nM * pM:.0f} and {nM * (1 - pM):.0f}).",
            f"C: Calculates the z-score {fx(zM)} using the mean and standard deviation from part A.",
            f"C: Calculates the probability {fx(pgM, 3)}.",
            "D: Describes a Type I error in context (evidence for a proportion greater than 0.30 when it is 0.30).",
            "D: States that the probability of a Type I error is 0.05.",
            "E: Describes a Type II error in context (no convincing evidence of a proportion greater than 0.30 when it is greater).",
            "E: States a valid change that decreases the probability of a Type II error (a larger sample size, or a larger α)."),
          sample)

    # ----------------------------------------------------------------------------------------------------------- M2: sample size, random sample, bias, interval
    moe_t = 0.04
    nreq = 1.96 ** 2 * 0.25 / moe_t ** 2
    nmin = math.ceil(nreq)
    xr, nr = 176, 320
    cr = prop_ci(xr, nr, 0.95)
    assert nreq > 600 and cr.x >= 10
    setup = ("A city council wants to estimate the proportion of the 5,000 registered voters in a neighborhood who support building a new park. The council has an alphabetical list of all 5,000 registered voters.")
    parts = [("A", "The council wants a 95% confidence interval with a margin of error of no more than 0.04, and has no earlier estimate of the proportion. Find the minimum sample size that is needed. Show your work."),
             ("B", "Describe how the council could select a simple random sample of voters of the size found in part A from the list."),
             ("C", "Instead, the council mails a survey to 800 randomly selected voters, and 320 of them return it. Identify a type of bias that could affect the result, and explain how it could affect the result."),
             ("D", f"Of the 320 voters who returned the survey, {xr} support building the park. Construct a 95% confidence interval for the proportion of all voters in the neighborhood who support building the park."),
             ("E", "Explain why the margin of error of the interval in part D does not take the bias from part C into account.")]
    ans = [("A", f"n = ($z^*$ / MOE)² p̂(1 - p̂) with p̂ = 0.5 (the value that gives the largest sample size): n = (1.96 / 0.04)²(0.5)(0.5) = {nreq:.2f}. The sample size must be a whole number, so round up: n = {nmin}."),
           ("B", f"Number the voters from 1 to 5,000 in the list. Use a random number generator to select {nmin} different numbers between 1 and 5,000. The voters with those numbers are the sample."),
           ("C", "Nonresponse bias: only 320 of the 800 voters responded (40%). The voters who returned the survey may differ from the voters who did not (for example, voters with a strong opinion about the park may be more likely to respond), so the result may be consistently too high or too low for the voters in the neighborhood."),
           ("D", f"p̂ = {xr} / {nr} = {fx(cr.phat, 3)}. The interval is {fx(cr.phat, 3)} ± 1.96√({fx(cr.phat, 3)}(1 - {fx(cr.phat, 3)}) / {nr}) = {fx(cr.phat, 3)} ± {fx(cr.moe, 4)}, which is ({fx(cr.lo, 3)}, {fx(cr.hi, 3)})."),
           ("E", "The margin of error measures only the variability from sampling (how much the sample proportion typically varies from sample to sample). Bias is a systematic error from the sampling method, so a larger sample or a different margin of error would not remove it.")]
    prompt, sample = frq_text(setup, parts, ans)
    B.frq(3, "MULTI_FOCUS", prompt,
          L("A: Uses the sample size formula with p̂ = 0.5 and the correct values substituted.",
            f"A: Calculates {nreq:.2f}.",
            f"A: Rounds up to {nmin}.",
            "B: Describes numbering the voters and using a random number generator (or another random process).",
            f"B: States that {nmin} different numbers are selected (without replacement).",
            "C: Identifies nonresponse bias.",
            "C: Explains how it could affect the result (the voters who responded may differ from those who did not).",
            f"D: Gives the correct interval formula with the values substituted ($\\hat{{p}}$ = {fx(cr.phat, 3)}, n = {nr}).",
            f"D: Gives the interval ({fx(cr.lo, 3)}, {fx(cr.hi, 3)}).",
            "E: Explains that the margin of error accounts only for sampling variability and not for bias from the sampling method."),
          sample)
