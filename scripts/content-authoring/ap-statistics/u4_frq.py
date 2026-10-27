"""Unit 4 free response: two COLLECT_DATA prompts, six INFERENCE prompts (the exam's Question 3) and two MULTI_FOCUS prompts, 10 points each (one point per rubric line, in the order of the parts).

  C1 4.9/1.13 a matched pairs experiment: design and scope                       C2 4.2/1.11 a stratified random sample and bias, to estimate a mean
  I1 4.2/4.3 a one-sample t-interval and a claim (dotplot)                       I2 4.5 a one-sample t-test (dotplot)
  I3 4.2/4.3 a matched pairs t-interval (dotplot of the differences)             I4 4.5 a matched pairs t-test (dotplot of the differences)
  I5 4.7/4.8 a two-sample t-interval (both samples at least 30)                  I6 4.10 a two-sample t-test in an experiment (two boxplots)
  M1 4.1 the sampling distribution of a mean, a probability, one value or a mean  M2 4.6 the sampling distribution of a difference in means, a probability, a random sample
Every number is computed here from the data that is shown or described.
"""
from scipy import stats as sps

from lib import *


def L(*lines):
    return [(1, t) for t in lines]


def fx(v, p=2):
    return f"{v:.{p}f}"


def draw_ints(mu, s, n, seed):
    r = np.random.default_rng(seed)
    d = sorted(int(round(v)) for v in r.normal(mu, s, n))
    assert not outliers_iqr(d) and abs(skewness(d)) < 0.4, (seed, d)
    return d


def ax(data, step):
    lo = (min(data) - 1) // step * step
    hi = -(-(max(data) + 1) // step) * step
    return (lo, hi, step)


def pick_pair(mu1, s1, n1, mu2, s2, n2, alt, p_max, p_min=0.0):
    for seed in range(1, 400):
        try:
            a, b = draw_ints(mu1, s1, n1, seed), draw_ints(mu2, s2, n2, seed + 1000)
        except AssertionError:
            continue
        t = t2_test(mean(a), sd(a), n1, mean(b), sd(b), n2, alt)
        if p_min < t.p < p_max:
            return a, b, t
    raise AssertionError("no pair")


def build(B):
    # ----------------------------------------------------------------------------------------------------------- C1: matched pairs design
    setup = ("A sports store wants to know whether a new model of running shoe lets runners finish a 5-kilometer course faster than the old model. Twenty runners agree to take part. Each runner is willing to run the course twice, wearing a different model each time, on two different days.")
    parts = [("A", "Identify the experimental units, the treatments, and the response variable."),
             ("B", "Describe how the store should use a random process to decide the order in which each runner wears the models, and explain why the order should be randomized."),
             ("C", "Describe one other way to control the conditions so that the comparison of the two models is fair."),
             ("D", "Describe the statistic that the store should calculate for each runner, and the analysis that the store should use to decide whether the new model is faster."),
             ("E", "Suppose that the analysis gives convincing evidence that the new model is faster. What conclusion can the store make, and for which runners does it apply?")]
    ans = [("A", "The experimental units are the 20 runners. The treatments are wearing the new model and wearing the old model. The response variable is the time the runner takes to finish the 5-kilometer course."),
           ("B", "For each runner, flip a coin (or use a random number generator): heads means the runner wears the new model first, and tails means the old model first. Randomizing the order spreads any effect of the order (fatigue or practice) evenly, so it does not favor one model."),
           ("C", "Have every runner run the same course at about the same time of day and in similar weather, and with the same amount of rest between the two runs."),
           ("D", "Calculate, for each runner, the difference in the finishing times (old model minus new model). Use the 20 differences in a one-sample t-test (or t-interval) for the population mean difference, with the hypothesis that the mean difference is 0."),
           ("E", "Because the order was randomized, and each runner used both models, the store can conclude that the new model causes faster times, on average, for runners like those in the study. The conclusion applies to runners like the 20 volunteers, and not to all runners, because they were not a random sample of all runners.")]
    prompt, sample = frq_text(setup, parts, ans)
    B.frq(9, "COLLECT_DATA", prompt,
          L("A: Identifies the runners as the experimental units.",
            "A: Identifies the treatments (the two models) and the response variable (the finishing time).",
            "B: Describes a random process for the order (such as a coin flip for each runner).",
            "B: Explains that randomizing the order balances out the effect of the order (such as fatigue or practice).",
            "C: Describes a way to control other conditions (the same course, similar weather or time of day, the same rest).",
            "D: States that the difference between the two times is calculated for each runner (a matched pairs analysis).",
            "D: States a one-sample t-procedure on the differences (a test or an interval for the population mean difference).",
            "E: States a cause-and-effect conclusion, because of randomization of the order and the comparison within runners.",
            "E: States that the new model is faster on average, in context.",
            "E: States that the conclusion applies to runners like the volunteers, not to all runners."),
          sample)

    # ----------------------------------------------------------------------------------------------------------- C2: stratified sample, bias
    setup = ("A school has 1,200 students: 400 freshmen, 350 sophomores, 250 juniors and 200 seniors. The student council wants to estimate the mean number of hours that all of the students at the school sleep on a school night. A council member suggests asking the students who are in the cafeteria at lunch.")
    parts = [("A", "Explain why asking the students in the cafeteria at lunch is likely to give a biased estimate of the mean number of hours of sleep, and describe the direction of the bias if you can."),
             ("B", "Describe how the council could select a stratified random sample of 60 students, using the grade levels as the strata, so that each grade level is represented in proportion to its size."),
             ("C", "Explain why a stratified random sample may be a better choice here than a simple random sample."),
             ("D", "The council selects a sample, calculates the sample mean and the sample standard deviation of the hours of sleep, and wants to estimate the population mean. Name the procedure that the council should use, and state the conditions that must be checked."),
             ("E", "Another student says, \"If we use a larger sample, our result will be unbiased.\" Is this correct? Justify your answer.")]
    ans = [("A", "The students in the cafeteria at lunch are a convenience sample: students who are not in the cafeteria (for example those who sleep in, eat elsewhere, or have a different schedule) have no chance of being selected, so the sample may not represent all students. Students who are up early or who eat at school may sleep less, so the estimate may be too low (the direction is not certain)."),
           ("B", "The proportions of the 60 students are 400/1200, 350/1200, 250/1200 and 200/1200 of the sample: 20 freshmen, 17 or 18 sophomores, 12 or 13 juniors and 10 seniors (for example 20, 18, 12 and 10). For each grade, number the students and use a random number generator to select the needed number of different students from that grade. Combine the four groups."),
           ("C", "Students in different grades may sleep different amounts. A stratified sample guarantees that every grade is represented in proportion to its size, which reduces the variability of the sample mean compared with a simple random sample, where one grade could be over- or under-represented by chance."),
           ("D", "A one-sample t-interval for a population mean (the population standard deviation is unknown). Conditions: the sample is random; the 10% condition (the sample is less than 10% of the 1,200 students, so n ≤ 120); and the sample data condition (n ≥ 30, or the data are approximately normal, or there is no strong skewness or outliers)."),
           ("E", "No. Bias comes from the sampling method. A larger sample taken with a biased method, such as asking the students in the cafeteria, is still biased. A larger sample reduces variability, not bias; random selection is what removes the bias.")]
    prompt, sample = frq_text(setup, parts, ans)
    B.frq(2 - 0 + 0, "COLLECT_DATA", prompt,
          L("A: Identifies the cafeteria sample as a convenience sample (or voluntary or undercoverage bias): not every student has a chance to be selected.",
            "A: Explains how this could make the estimate too high or too low, in context.",
            "B: Gives the correct allocation of the 60 students to the grade levels (proportional to 400, 350, 250 and 200: about 20, 17 or 18, 12 or 13, and 10).",
            "B: Describes a random process to select students within each grade (a random number generator or similar).",
            "C: Explains that a stratified sample guarantees representation of every grade, in proportion to size.",
            "C: Explains that this can reduce variability if the grades differ in the amount of sleep.",
            "D: Identifies a one-sample t-interval for a population mean.",
            "D: States the randomization condition and the 10% condition (n ≤ 120).",
            "D: States the sample data condition (n ≥ 30, or no strong skewness or outliers).",
            "E: States that the statement is incorrect, because a larger sample does not remove bias from the sampling method."),
          sample)

    # ----------------------------------------------------------------------------------------------------------- I1: one-sample t-interval
    d1 = draw_ints(48, 6, 15, 4)
    n1_, xb, sx = len(d1), mean(d1), sd(d1)
    ci = t_ci(xb, sx, n1_, 0.95)
    assert ci.hi < 55
    dp = dotplot(d1, "Lifetime (hours)", axis=ax(d1, 2), alt="Dotplot of the lifetimes, in hours, of 15 batteries: roughly symmetric, with no outliers.")
    setup = (f"A manufacturer claims that the mean lifetime of its rechargeable batteries is 55 hours. A consumer group selected a random sample of {n1_} batteries from the very large number of batteries that the manufacturer made in one month, and recorded the lifetime, in hours, of each. "
             f"The dotplot shows the lifetimes. The mean of the sample is {fx(xb)} hours and the standard deviation is {fx(sx)} hours.")
    parts = [("A", "Identify the appropriate inference procedure for estimating the mean lifetime of all of the batteries that the manufacturer made in that month, and state the parameter in context."),
             ("B", "Verify that the conditions for the procedure are met."),
             ("C", "Construct and show the work for a 95% confidence interval for the mean lifetime."),
             ("D", "Interpret the interval from part C in context."),
             ("E", "Does the interval provide convincing evidence against the manufacturer's claim that the mean lifetime is 55 hours? Justify your answer.")]
    ans = [("A", "A one-sample t-interval for a population mean (the population standard deviation is unknown). The parameter is μ, the mean lifetime, in hours, of all of the batteries that the manufacturer made in that month."),
           ("B", f"Randomization: the batteries are a random sample. 10% condition: the sample of {n1_} is less than 10% of a very large number of batteries. Sample data condition: n = {n1_} < 30, but the dotplot is roughly symmetric with no strong skewness or outliers."),
           ("C", f"$\\bar{{x}}$ ± $t^*$ s / √n = {fx(xb)} ± {fx(ci.t, 3)}({fx(sx)} / √{n1_}) with df = {ci.df}, which is {fx(xb)} ± {fx(ci.moe)}, or ({fx(ci.lo)}, {fx(ci.hi)})."),
           ("D", f"We are 95% confident that the interval from {fx(ci.lo)} to {fx(ci.hi)} hours contains the mean lifetime of all of the batteries that the manufacturer made in that month."),
           ("E", f"Yes. The value 55 hours is not in the interval ({fx(ci.lo)}, {fx(ci.hi)}), so it is not a plausible value for the mean. All plausible values are less than 55, so the interval provides convincing evidence that the mean lifetime is less than 55 hours.")]
    prompt, sample = frq_text(setup, parts, ans)
    B.frq(2, "INFERENCE", prompt,
          L("A: Identifies a one-sample t-interval for a population mean.",
            "A: States the parameter in context: the mean lifetime of all of the batteries made in that month.",
            "B: Verifies the randomization condition and the 10% condition.",
            f"B: Verifies the sample data condition (n < 30 and the dotplot shows no strong skewness or outliers).",
            f"C: Gives the correct formula with the values substituted ($t^*$ = {fx(ci.t, 3)} with df = {ci.df}).",
            f"C: Gives the interval ({fx(ci.lo)}, {fx(ci.hi)}).",
            "D: Interprets the confidence level (95% confident).",
            "D: States that the interval is for the mean lifetime of all of the batteries, in context.",
            "E: States that 55 is not in the interval, so it is not a plausible value.",
            "E: Concludes that there is convincing evidence against the claim (the mean is less than 55 hours)."),
          sample, diagram=dp)

    # ----------------------------------------------------------------------------------------------------------- I2: one-sample t-test
    d2 = draw_ints(30, 5, 20, 4)
    n2_, x2, s2 = len(d2), mean(d2), sd(d2)
    tt = t_test(x2, s2, n2_, 35, "lt")
    assert tt.p < 0.01
    dp2 = dotplot(d2, "Wait time (minutes)", axis=ax(d2, 2), alt="Dotplot of the wait times, in minutes, of 20 patients: roughly symmetric, with no outliers.")
    setup = (f"A clinic says that the mean wait time for its patients is 35 minutes. The manager believes that the mean wait time is less than 35 minutes. The manager selected a random sample of {n2_} patients from the clinic's very large number of patients and recorded each patient's wait time. "
             f"The dotplot shows the wait times. The mean of the sample is {fx(x2)} minutes and the standard deviation is {fx(s2)} minutes.")
    parts = [("A", "State the appropriate null and alternative hypotheses for a test of the manager's belief. Define any parameter that you use."),
             ("B", "Verify that the conditions for the test are met."),
             ("C", "Calculate the test statistic and the p-value for the test."),
             ("D", "Using a significance level of α = 0.05, state a conclusion for the test in context, and justify your conclusion."),
             ("E", "Interpret the p-value from part C in context.")]
    ans = [("A", "Let μ be the mean wait time, in minutes, of all of the clinic's patients. H₀: μ = 35 and Hₐ: μ < 35."),
           ("B", f"Randomization: the patients are a random sample. 10% condition: {n2_} is less than 10% of a very large number of patients. Sample data condition: n = {n2_} < 30, but the dotplot is roughly symmetric with no strong skewness or outliers."),
           ("C", f"t = ({fx(x2)} - 35) / ({fx(s2)} / √{n2_}) = {fx(tt.t)}, with df = {tt.df}. The p-value is P(t ≤ {fx(tt.t)}) = {fx(tt.p, 4)}."),
           ("D", f"The p-value {fx(tt.p, 4)} is less than α = 0.05, so reject the null hypothesis. There is convincing statistical evidence that the mean wait time of all of the clinic's patients is less than 35 minutes."),
           ("E", f"Assuming that the mean wait time of all of the clinic's patients is 35 minutes, the probability of getting a sample mean as small as {fx(x2)} minutes or smaller, in a random sample of {n2_} patients, is {fx(tt.p, 4)}.")]
    prompt, sample = frq_text(setup, parts, ans)
    B.frq(5, "INFERENCE", prompt,
          L("A: States H₀: μ = 35 and Hₐ: μ < 35.",
            "A: Defines μ as the mean wait time of all of the clinic's patients.",
            "B: Verifies the randomization condition and the 10% condition.",
            "B: Verifies the sample data condition (n < 30 and the dotplot shows no strong skewness or outliers).",
            f"C: Calculates the test statistic t = {fx(tt.t)} (with df = {tt.df}).",
            f"C: Calculates the p-value {fx(tt.p, 4)}.",
            "D: Compares the p-value with α = 0.05 and rejects the null hypothesis.",
            "D: States a conclusion in context, in terms of the alternative (convincing evidence that the mean is less than 35 minutes).",
            "E: States that the p-value is computed assuming the null hypothesis (mean 35) is true.",
            f"E: Interprets it as the probability of a sample mean at least as small as {fx(x2)} in a random sample of {n2_}."),
          sample, diagram=dp2)

    # ----------------------------------------------------------------------------------------------------------- I3: matched pairs t-interval
    d3 = draw_ints(3, 4, 12, 4)
    n3_, x3, s3 = len(d3), mean(d3), sd(d3)
    c3 = t_ci(x3, s3, n3_, 0.95)
    assert c3.lo > 0
    dp3 = dotplot(d3, "Difference in score (after - before)", axis=ax(d3, 1), alt="Dotplot of the differences in the scores, after minus before, for 12 students: roughly symmetric, with no outliers.")
    setup = (f"A teacher randomly selected {n3_} students from a very large school district. Each student took a vocabulary quiz, completed a two-week tutoring program, and then took a similar quiz. The teacher recorded the difference in each student's scores, after minus before. "
             f"The dotplot shows the differences. The mean of the differences is {fx(x3)} points and the standard deviation is {fx(s3)} points.")
    parts = [("A", "Identify the appropriate inference procedure for estimating the mean change in the scores for all of the students in the district, and state the parameter in context."),
             ("B", "Verify that the conditions for the procedure are met."),
             ("C", "Construct and show the work for a 95% confidence interval for the parameter."),
             ("D", "Interpret the interval from part C in context."),
             ("E", "Does the interval provide convincing evidence that the mean score is different after the program? Justify your answer.")]
    ans = [("A", "A one-sample t-interval for a population mean difference (matched pairs). The parameter is μ_d, the mean difference (after - before) in the vocabulary scores of all of the students in the district who complete the program."),
           ("B", f"Randomization: the students are a random sample. 10% condition: {n3_} is less than 10% of the students in a very large district. Sample data condition: there are {n3_} differences, which is fewer than 30, and the dotplot of the differences is roughly symmetric with no strong skewness or outliers."),
           ("C", f"$\\bar{{x}}_d$ ± $t^*$ s_d / √n = {fx(x3)} ± {fx(c3.t, 3)}({fx(s3)} / √{n3_}) with df = {c3.df}, which is {fx(x3)} ± {fx(c3.moe)}, or ({fx(c3.lo)}, {fx(c3.hi)})."),
           ("D", f"We are 95% confident that the interval from {fx(c3.lo)} to {fx(c3.hi)} points contains the mean difference (after - before) in the vocabulary scores of all of the students in the district who complete the program."),
           ("E", f"Yes. The interval ({fx(c3.lo)}, {fx(c3.hi)}) does not contain 0 and all of its values are positive, so there is convincing evidence that the mean score after the program is greater than the mean score before it.")]
    ans[0] = (ans[0][0], ans[0][1].replace("μ_d", "$\\mu_d$"))
    ans[2] = (ans[2][0], ans[2][1].replace("s_d", "$s_d$"))
    prompt, sample = frq_text(setup, parts, ans)
    B.frq(2, "INFERENCE", prompt,
          L("A: Identifies a one-sample t-interval for a population mean difference (matched pairs).",
            "A: States the parameter in context, with the order of subtraction (after - before).",
            "B: Verifies the randomization condition and the 10% condition.",
            "B: Verifies the sample data condition using the differences (n < 30 and the dotplot shows no strong skewness or outliers).",
            f"C: Gives the correct formula with the values substituted ($t^*$ = {fx(c3.t, 3)} with df = {c3.df}).",
            f"C: Gives the interval ({fx(c3.lo)}, {fx(c3.hi)}).",
            "D: Interprets the confidence level (95% confident).",
            "D: States that the interval is for the mean difference (after - before), in context.",
            "E: States that the interval does not contain 0.",
            "E: Concludes that there is convincing evidence of a change (the mean score is greater after the program)."),
          sample, diagram=dp3)

    # ----------------------------------------------------------------------------------------------------------- I4: matched pairs t-test
    d4 = draw_ints(4, 3, 14, 4)
    n4_, x4, s4 = len(d4), mean(d4), sd(d4)
    t4 = t_test(x4, s4, n4_, 0, "gt")
    assert t4.p < 0.01
    dp4 = dotplot(d4, "Difference in time (old - new), seconds", axis=ax(d4, 1), alt="Dotplot of the differences in the times, old tool minus new tool, for 14 workers: roughly symmetric, with no outliers.")
    setup = (f"A company randomly selected {n4_} of its many workers to test a new tool. Each worker did the same task twice, once with the old tool and once with the new tool, and the order was randomized. The company recorded each worker's difference in times, in seconds, old tool minus new tool. "
             f"The dotplot shows the differences. The mean of the differences is {fx(x4)} seconds and the standard deviation is {fx(s4)} seconds. The company believes that the new tool is faster.")
    parts = [("A", "State the appropriate null and alternative hypotheses for a test of the company's belief. Define any parameter that you use."),
             ("B", "Verify that the conditions for the test are met."),
             ("C", "Calculate the test statistic and the p-value for the test."),
             ("D", "Using a significance level of α = 0.05, state a conclusion for the test in context, and justify your conclusion."),
             ("E", "Can the company conclude that the new tool causes the shorter times? Explain your answer.")]
    ans = [("A", "Let $\\mu_d$ be the mean difference (old tool - new tool) in the times, in seconds, of all of the company's workers. H₀: $\\mu_d$ = 0 and Hₐ: $\\mu_d$ > 0."),
           ("B", f"Randomization: the workers are a random sample, and the order of the tools was randomized. 10% condition: {n4_} is less than 10% of the company's many workers. Sample data condition: there are {n4_} differences, which is fewer than 30, and the dotplot of the differences is roughly symmetric with no strong skewness or outliers."),
           ("C", f"t = ({fx(x4)} - 0) / ({fx(s4)} / √{n4_}) = {fx(t4.t)}, with df = {t4.df}. The p-value is P(t ≥ {fx(t4.t)}) = {fx(t4.p, 4)}."),
           ("D", f"The p-value {fx(t4.p, 4)} is less than α = 0.05, so reject the null hypothesis. There is convincing statistical evidence that the mean time with the old tool is greater than the mean time with the new tool for all of the company's workers."),
           ("E", "Yes. Each worker used both tools in a randomized order, which controls the effect of the order and of differences among the workers, so a difference that is too large to be due to chance can be attributed to the tools. The conclusion applies to the company's workers, because they were randomly selected.")]
    prompt, sample = frq_text(setup, parts, ans)
    B.frq(5, "INFERENCE", prompt,
          L("A: States H₀: $\\mu_d$ = 0 and Hₐ: $\\mu_d$ > 0 (with the order of subtraction, old - new).",
            "A: Defines the parameter as the mean difference in the times of all of the company's workers.",
            "B: Verifies the randomization condition and the 10% condition.",
            "B: Verifies the sample data condition using the differences (n < 30 and the dotplot shows no strong skewness or outliers).",
            f"C: Calculates the test statistic t = {fx(t4.t)}.",
            f"C: Calculates the p-value {fx(t4.p, 4)}.",
            "D: Compares the p-value with α = 0.05 and rejects the null hypothesis.",
            "D: States a conclusion in context, in terms of the alternative (convincing evidence that the mean time with the new tool is shorter).",
            "E: States that a cause-and-effect conclusion is justified because the order was randomized.",
            "E: Gives a reason, in context (each worker used both tools in a random order, which controls other differences)."),
          sample, diagram=dp4)

    # ----------------------------------------------------------------------------------------------------------- I5: two-sample t-interval, both n >= 30
    xa, sa, na, xb2, sb, nb = 23.4, 6.6, 36, 20.5, 5.3, 40
    c5 = t2_ci(xa, sa, na, xb2, sb, nb, 0.95)
    assert c5.lo > 0
    setup = (f"A researcher compared the times that students at two large high schools take to get to school. She selected independent random samples of {na} students from School A and {nb} students from School B. "
             f"In the School A sample, the mean time was {xa} minutes with a standard deviation of {sa} minutes. In the School B sample, the mean time was {xb2} minutes with a standard deviation of {sb} minutes.")
    parts = [("A", "Identify the appropriate inference procedure for estimating the difference between the mean times of all students at the two schools, and state the parameter in context."),
             ("B", "Verify that the conditions for the procedure are met."),
             ("C", f"A technology output gives {c5.df:.1f} degrees of freedom. Construct and show the work for a 95% confidence interval for the difference in the mean times, School A minus School B."),
             ("D", "Interpret the interval from part C in context."),
             ("E", "Does the interval provide convincing evidence of a difference between the mean times of all students at the two schools? Justify your answer.")]
    ans = [("A", "A two-sample t-interval for a difference between population means. The parameter is μ₁ - μ₂, where μ₁ is the mean time, in minutes, that all students at School A take to get to school and μ₂ is the mean time that all students at School B take."),
           ("B", f"Randomization: the data come from two independent random samples. 10% condition: each sample is less than 10% of the students at its (large) school. Sample data condition: both sample sizes, {na} and {nb}, are at least 30."),
           ("C", f"({xa} - {xb2}) ± $t^*$√({sa}²/{na} + {sb}²/{nb}) = {fx(c5.diff, 1)} ± {fx(c5.t, 3)}({fx(c5.se, 3)}) = {fx(c5.diff, 1)} ± {fx(c5.moe)}, which is ({fx(c5.lo)}, {fx(c5.hi)})."),
           ("D", f"We are 95% confident that the interval from {fx(c5.lo)} to {fx(c5.hi)} minutes contains the difference between the mean time of all students at School A and the mean time of all students at School B to get to school."),
           ("E", f"Yes. The interval ({fx(c5.lo)}, {fx(c5.hi)}) does not contain 0, and all of its values are positive, so there is convincing evidence that the mean time is greater for the students at School A than for the students at School B.")]
    prompt, sample = frq_text(setup, parts, ans)
    B.frq(7, "INFERENCE", prompt,
          L("A: Identifies a two-sample t-interval for a difference between population means.",
            "A: States the parameter in context: the difference between the mean times of all students at School A and at School B.",
            "B: Verifies the randomization condition (two independent random samples) and the 10% condition for each sample.",
            f"B: Verifies the sample data condition (both sample sizes, {na} and {nb}, are at least 30).",
            f"C: Gives the correct formula with the values substituted (difference {fx(c5.diff, 1)}, standard error {fx(c5.se, 3)}, $t^*$ = {fx(c5.t, 3)}).",
            f"C: Gives the interval ({fx(c5.lo)}, {fx(c5.hi)}).",
            "D: Interprets the confidence level (95% confident).",
            "D: States that the interval is for the difference in the two population mean times, in context.",
            "E: States that the interval does not contain 0.",
            "E: Concludes that the mean time is greater at School A (convincing evidence of a difference)."),
          sample)

    # ----------------------------------------------------------------------------------------------------------- I6: two-sample t-test, experiment, boxplots
    g1, g2, t6 = pick_pair(80, 8, 16, 71, 8, 18, "gt", 0.02, 0.0005)
    n6a, n6b = len(g1), len(g2)
    x6a, s6a, x6b, s6b = mean(g1), sd(g1), mean(g2), sd(g2)
    bp6 = boxplot([box_group(g1, "New program"), box_group(g2, "Standard program")], "Score on the fitness test (points)", axis=(min(g1 + g2) - 5 - (min(g1 + g2) - 5) % 5, max(g1 + g2) + 5 - (max(g1 + g2) + 5) % 5 + 5, 5),
                  alt="Boxplots of the fitness test scores of the volunteers in the two programs: both roughly symmetric, with no outliers.")
    setup = (f"A trainer randomly assigned {n6a + n6b} volunteers to a new training program ({n6a} volunteers) or the standard training program ({n6b} volunteers). After 8 weeks, each volunteer took a fitness test. The boxplots show the scores. "
             f"The new program group had a mean of {fx(x6a)} points and a standard deviation of {fx(s6a)} points. The standard program group had a mean of {fx(x6b)} points and a standard deviation of {fx(s6b)} points. The trainer believes that the new program gives a greater mean score.")
    parts = [("A", "State the appropriate null and alternative hypotheses for a test of the trainer's belief. Define any parameters that you use."),
             ("B", "Verify that the conditions for the test are met."),
             ("C", f"Calculate the test statistic and the p-value for the test. (Technology gives {t6.df:.1f} degrees of freedom.)"),
             ("D", "Using a significance level of α = 0.05, state a conclusion for the test in context, and justify your conclusion."),
             ("E", "Can the trainer conclude that the new program causes the greater mean score? Can the conclusion be applied to all adults? Justify your answers.")]
    ans = [("A", "Let μ₁ be the mean fitness test score for volunteers like these after the new program, and μ₂ the mean score after the standard program. H₀: μ₁ - μ₂ = 0 and Hₐ: μ₁ - μ₂ > 0."),
           ("B", f"Randomization: the volunteers were randomly assigned to the programs (the 10% condition is not needed for an experiment). Sample data condition: both sample sizes ({n6a} and {n6b}) are less than 30, but the boxplots are roughly symmetric with no outliers."),
           ("C", f"t = ({fx(x6a)} - {fx(x6b)}) / √({fx(s6a)}²/{n6a} + {fx(s6b)}²/{n6b}) = {fx(t6.t)}. The p-value is P(t ≥ {fx(t6.t)}) = {fx(t6.p, 4)}."),
           ("D", f"The p-value {fx(t6.p, 4)} is less than α = 0.05, so reject the null hypothesis. There is convincing statistical evidence that the mean fitness test score is greater after the new program than after the standard program for volunteers like these."),
           ("E", "Yes, the trainer can conclude that the new program causes the greater mean score, because the volunteers were randomly assigned to the programs. No, the conclusion cannot be applied to all adults, because the participants were volunteers and not a random sample of all adults; it applies to people like the volunteers.")]
    prompt, sample = frq_text(setup, parts, ans)
    B.frq(10, "INFERENCE", prompt,
          L("A: States H₀: μ₁ - μ₂ = 0 and Hₐ: μ₁ - μ₂ > 0.",
            "A: Defines the parameters in context (the mean scores for volunteers like these after each program).",
            "B: Verifies the randomization condition (random assignment; the 10% condition is not needed).",
            "B: Verifies the sample data condition (both n < 30 and the boxplots show no strong skewness or outliers).",
            f"C: Calculates the test statistic t = {fx(t6.t)}.",
            f"C: Calculates the p-value {fx(t6.p, 4)}.",
            "D: Compares the p-value with α = 0.05 and rejects the null hypothesis.",
            "D: States a conclusion in context, in terms of the alternative (convincing evidence that the mean score is greater with the new program).",
            "E: States that a cause-and-effect conclusion is justified because of random assignment.",
            "E: States that the conclusion applies to volunteers like those in the study, not to all adults."),
          sample, diagram=bp6)

    # ----------------------------------------------------------------------------------------------------------- M1: sampling distribution of a mean
    muM, sgM, nM = 70, 10, 25
    seM = sgM / math.sqrt(nM)
    zM = (75 - muM) / seM
    pM = float(sps.norm.sf(zM))
    pI = float(sps.norm.sf((75 - muM) / sgM))
    setup = ("The heights of the plants in a large field are approximately normally distributed with a mean of 70 centimeters and a standard deviation of 10 centimeters. A botanist selects a random sample of 25 plants from the field.")
    parts = [("A", "Find the mean and the standard deviation of the sampling distribution of the sample mean height $\\bar{x}$ for random samples of 25 plants."),
             ("B", "Justify that it is appropriate to model the sampling distribution of $\\bar{x}$ with a normal distribution."),
             ("C", "Calculate the probability that the mean height of the 25 plants in the sample is greater than 75 centimeters."),
             ("D", "Calculate the probability that one plant selected at random from the field is taller than 75 centimeters, and explain why this probability is different from the probability in part C."),
             ("E", "The botanist wants the standard deviation of the sampling distribution to be half as large. By what factor should the sample size be multiplied? Justify your answer.")]
    ans = [("A", f"μ = 70 centimeters and σ = 10 / √25 = {fx(seM, 1)} centimeters."),
           ("B", "The plants are a random sample, 25 is less than 10% of the plants in a large field, and the population is approximately normal, so the sampling distribution of $\\bar{x}$ is normal for any sample size."),
           ("C", f"z = (75 - 70) / {fx(seM, 1)} = {fx(zM, 1)}, so P($\\bar{{x}}$ > 75) = P(z > {fx(zM, 1)}) = {fx(pM, 4)}."),
           ("D", f"For one plant, z = (75 - 70) / 10 = 0.5, so P(X > 75) = {fx(pI, 4)}. The probability is much greater than the probability in part C because individual plants vary more (standard deviation 10) than the mean of 25 plants (standard deviation 2), so a sample mean is much less likely to be far from 70."),
           ("E", "The standard deviation is 10 / √n, so to halve it the sample size must be multiplied by 4 (from 25 to 100), because √4 = 2.")]
    prompt, sample = frq_text(setup, parts, ans)
    B.frq(1, "MULTI_FOCUS", prompt,
          L("A: States the mean of the sampling distribution as 70 centimeters.",
            f"A: Calculates the standard deviation {fx(seM, 1)} centimeters.",
            "B: Verifies the randomization and 10% conditions.",
            "B: Cites the approximately normal population, so the sampling distribution of the mean is normal for any n.",
            f"C: Calculates the z-score {fx(zM, 1)}, using the standard deviation from part A.",
            f"C: Calculates the probability {fx(pM, 4)}.",
            f"D: Calculates the probability for one plant ({fx(pI, 4)}), using the standard deviation of 10.",
            "D: Explains that individual values vary more than the mean of a sample (the standard deviation of $\\bar{x}$ is smaller).",
            "E: States that the sample size should be multiplied by 4.",
            "E: Justifies the answer using σ / √n."),
          sample)

    # ----------------------------------------------------------------------------------------------------------- M2: difference of two means, random sample
    m1_, s1_, n1m, m2_, s2_, n2m = 60, 10, 40, 55, 12, 50
    sdM = math.sqrt(s1_ ** 2 / n1m + s2_ ** 2 / n2m)
    zM2 = (0 - (m1_ - m2_)) / sdM
    pM2 = float(sps.norm.sf(zM2))
    setup = ("A district has 3,000 students at Lincoln High School and 4,000 students at Roosevelt High School. The mean score on a district math test is 60 points with a standard deviation of 10 points at Lincoln, and 55 points with a standard deviation of 12 points at Roosevelt. "
             "A researcher plans to select independent random samples of 40 Lincoln students and 50 Roosevelt students.")
    parts = [("A", "Find the mean and the standard deviation of the sampling distribution of $\\bar{x}_1 - \\bar{x}_2$, the sample mean score at Lincoln minus the sample mean score at Roosevelt."),
             ("B", "Verify that the conditions for using a normal distribution to model this sampling distribution are met."),
             ("C", "Calculate the probability that the sample mean score at Lincoln is greater than the sample mean score at Roosevelt."),
             ("D", "Describe how the researcher could select the simple random sample of 40 Lincoln students from a list of the 3,000 students."),
             ("E", "Interpret the standard deviation from part A in context.")]
    ans = [("A", f"μ = 60 - 55 = 5 points and σ = √(10²/40 + 12²/50) = √(2.5 + 2.88) = {fx(sdM)} points."),
           ("B", "The samples are independent random samples. 10% condition: 40 is less than 10% of 3,000, and 50 is less than 10% of 4,000. Sample data condition: both sample sizes, 40 and 50, are at least 30, so the sampling distribution is approximately normal."),
           ("C", f"z = (0 - 5) / {fx(sdM)} = {fx(zM2)}, so P($\\bar{{x}}_1 - \\bar{{x}}_2$ > 0) = P(z > {fx(zM2)}) = {fx(pM2, 4)}."),
           ("D", "Number the Lincoln students from 1 to 3,000. Use a random number generator to select 40 different numbers between 1 and 3,000. The students with those numbers are the sample."),
           ("E", f"In pairs of random samples of these sizes, the difference between the sample mean scores (Lincoln minus Roosevelt) typically varies from the difference in the population mean scores, 5 points, by about {fx(sdM)} points.")]
    prompt, sample = frq_text(setup, parts, ans)
    B.frq(6, "MULTI_FOCUS", prompt,
          L("A: States the mean of the sampling distribution as 5 points.",
            f"A: Calculates the standard deviation {fx(sdM)} points.",
            "B: Verifies the independent random samples and the 10% condition for both samples.",
            "B: Verifies that both sample sizes are at least 30.",
            f"C: Calculates the z-score {fx(zM2)}, using the mean and the standard deviation from part A.",
            f"C: Calculates the probability {fx(pM2, 4)}.",
            "D: Describes numbering the 3,000 students and using a random number generator (or another random process).",
            "D: States that 40 different numbers are selected (without replacement).",
            "E: Interprets the standard deviation as the typical amount that the difference in the sample means varies from the difference in the population means.",
            "E: Gives the interpretation in context (the difference in the sample mean scores, Lincoln minus Roosevelt)."),
          sample)
