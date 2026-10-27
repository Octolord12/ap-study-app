"""Unit 4, topics 4.9 and 4.10 (the two-sample t-test).

Required content (CED effective Fall 2026): 4.9 the two-sample t-test for the difference between two population means; the parameters in context; H0: mu1 = mu2 (or mu1 - mu2 = 0) with Ha: mu1 - mu2 <, > or != 0; conditions: two independent random samples or a randomized
experiment, 10% (unnecessary for an experiment), and both samples n >= 30 or both populations approximately normal (if either n < 30, both samples free of strong skewness and outliers). 4.10 t = (x-bar1 - x-bar2) / sqrt(s1^2/n1 + s2^2/n2), p-value from the
t-distribution with the degrees of freedom technology gives; interpret it assuming H0 is true; reject if the p-value <= alpha; a conclusion in context about the populations in terms of Ha (cause and effect only from random assignment). Skills 2.C, 2.E, 3.E, 4.E, 4.F, 4.G.
"""
from scipy import stats as sps

from lib import *


def f2(v):
    return f"{float(v):.2f}"


def f3(v):
    return f"{float(v):.3f}"


def f4(v):
    return f"{float(v):.4f}"


def build(B):
    # ------------------------------------------------------------------------------------------------------------ 4.9
    T = 9
    B.mcq(T, "In a randomized experiment, 40 volunteers are randomly assigned to a new study method and 40 volunteers to the usual method. A researcher wants to test whether the mean test score is greater with the new method. The population standard deviations are unknown. Which procedure is appropriate?",
          ch("A two-sample t-test for the difference between two population means", "The parameter is μ₁ - μ₂ for two independent treatment groups, with σ unknown."),
          [ch("A one-sample t-test for a population mean difference, using matched pairs", "The volunteers in the two groups are different people, not matched pairs."),
           ch("A two-sample z-test for the difference between two population proportions", "The scores are quantitative, so the parameter is a difference in means, not proportions."),
           ch("A one-sample t-test for a population mean of one group of students at the school", "There are two treatment groups, so the parameter is a difference between two means.")],
          "Two independent treatment groups with a quantitative response: a two-sample t-test.", difficulty="easy")

    B.mcq(T, "In a randomized experiment, volunteers are randomly assigned to a new study method (population 1) or the usual method (population 2). The researcher believes that the mean test score is greater with the new method. Which of the following are the correct hypotheses?",
          ch("H₀: μ₁ - μ₂ = 0 and Hₐ: μ₁ - μ₂ > 0, where μ₁ and μ₂ are the mean test scores of all students like these", "The null hypothesis states no difference, and the alternative states the belief."),
          [ch("H₀: μ₁ - μ₂ = 0 and Hₐ: μ₁ - μ₂ < 0, where μ₁ and μ₂ are the mean test scores of all students like these with each method", "The researcher believes that μ₁ is greater, so the alternative is μ₁ - μ₂ > 0."),
           ch("H₀: μ₁ - μ₂ > 0 and Hₐ: μ₁ - μ₂ = 0, where μ₁ and μ₂ are the mean test scores of all students like these with each method", "The null hypothesis contains the equality (no difference)."),
           ch("H₀: x̄₁ - x̄₂ = 0 and Hₐ: x̄₁ - x̄₂ > 0, where x̄₁ and x̄₂ are the mean scores of the volunteers in the groups", "Hypotheses are about the population means, not the sample means.")],
          "H0: μ1 - μ2 = 0; Ha: μ1 - μ2 > 0.", difficulty="medium")

    B.mcq(T, "A principal wants to know whether the mean time that students spend on homework each night differs between Grade 9 and Grade 12 at a school. Which of the following are the correct hypotheses?",
          ch("H₀: μ₁ = μ₂ and Hₐ: μ₁ ≠ μ₂, where μ₁ and μ₂ are the mean times that all Grade 9 and all Grade 12 students at the school spend on homework", "A difference in either direction is a two-sided alternative."),
          [ch("H₀: μ₁ ≠ μ₂ and Hₐ: μ₁ = μ₂, where μ₁ and μ₂ are the mean times that all Grade 9 students and all Grade 12 students spend on homework each night", "The null hypothesis contains the equality."),
           ch("H₀: μ₁ = μ₂ and Hₐ: μ₁ > μ₂, where μ₁ and μ₂ are the mean times that all Grade 9 students and all Grade 12 students spend on homework each night", "The question does not say that Grade 9 is greater, so the alternative is two-sided."),
           ch("H₀: μ = 60 and Hₐ: μ ≠ 60, where μ is the mean time that all students at the school spend on homework each night of the whole school year, in minutes", "The question compares two groups. It is not a test about one mean and a stated value.")],
          "A difference in either direction: Ha: μ1 ≠ μ2.", difficulty="easy")

    B.mcq(T, "A researcher will test a claim about the mean daily screen time of the students in two cities. Which of the following correctly defines the parameters?",
          ch("μ₁ = the mean daily screen time, in hours, of all students in City A, and μ₂ = the same mean for all students in City B", "The parameters reference the means, the response variable and the populations in context."),
          [ch("μ₁ = the mean daily screen time of the students in the sample from City A, and μ₂ = the same for the students in the sample from City B", "These are sample means, statistics, and not the population parameters."),
           ch("μ = the mean daily screen time, in hours, of all students in both cities", "This is one combined mean. A test of a difference needs two parameters."),
           ch("μ₁ = the number of students in City A who use screens, and μ₂ = the number in City B", "The parameters are mean times, not counts.")],
          "The parameters are the two population means, in context.", difficulty="easy")

    B.mcq(T, "Which conditions must be verified for a two-sample t-test for the difference between two population means when the data come from a randomized experiment with 25 units in each treatment group?",
          ch("The treatments are randomly assigned, and both samples of responses are free from strong skewness and outliers (or both populations are approximately normal); the 10% condition is not needed", "For an experiment, the randomization condition is the random assignment, and the sample data condition applies because n < 30."),
          [ch("The treatments are randomly assigned, and each group is at most 10% of a population", "The 10% condition is unnecessary for a randomized experiment."),
           ch("The volunteers are randomly selected from a population, and the group sizes are equal", "For an experiment, random assignment is what is needed, and the group sizes need not be equal."),
           ch("The two groups are paired, and the differences are free from outliers", "The groups are independent treatment groups, not paired.")],
          "Random assignment, and the sample data condition for n < 30; no 10% condition.", difficulty="medium")

    B.mcq(T, "Independent random samples of 45 students from School A and 52 students from School B, from large schools, are used in a two-sample t-test for the difference between the population mean scores. Which of the following is correct about the conditions?",
          ch("All conditions are met: the samples are independent and random, each is less than 10% of its school, and both sample sizes are at least 30", "These are the randomization, 10% and sample data conditions."),
          [ch("The sample data condition is not met, because the sample sizes are not equal", "The sample sizes do not need to be equal."),
           ch("The 10% condition is not met, because both samples are larger than 30", "The 10% condition compares each sample with its population, which is large."),
           ch("The randomization condition is not met, because the samples are of different schools", "Independent random samples from different populations meet the condition.")],
          "Independent random samples, each under 10% of its population, both n ≥ 30.", difficulty="medium")

    B.mcq(T, "Which of the following situations calls for a two-sample t-test (independent samples), and not for a matched pairs analysis?",
          ch("A researcher compares the resting heart rates of a random sample of 40 runners and a separate random sample of 40 swimmers", "The two groups are made of different people, with no pairing."),
          [ch("A researcher measures the resting heart rate of each of 40 people before and after a month of training", "Each person is measured twice, so the data are paired."),
           ch("A researcher measures the resting heart rates of 40 pairs of twins, one twin trained and one did not", "The twins in a pair are related, so the data are matched pairs."),
           ch("A researcher measures the resting heart rate of each of 40 people sitting and then standing, in a random order, with a rest in between", "Each person is measured under both conditions, so the data are paired.")],
          "Two separate groups, no pairing: a two-sample t-test.", difficulty="medium")

    sk1 = [3, 4, 4, 5, 5, 6, 6, 7, 9, 12, 34]
    sk2 = [5, 6, 6, 7, 8, 9, 9, 10, 11, 14, 15, 16]
    b1 = box_group(sk1, "Group 1")
    assert b1.get("outliers")
    bxs = boxplot([b1, box_group(sk2, "Group 2")], "Time (minutes)", axis=(0, 40, 5), alt="Boxplots of two groups: Group 1 has an outlier at 34 minutes and a long upper whisker.")
    B.mcq(T, f"In a randomized experiment, {len(sk1)} volunteers in Group 1 and {len(sk2)} volunteers in Group 2 receive two treatments, and their times are recorded. The boxplots show the times. A two-sample t-test is planned. Which of the following is correct about the conditions?",
          ch("The sample data condition is not met, because a sample size is less than 30 and Group 1 has an outlier", "If either sample size is less than 30, both samples should be free from strong skewness and outliers."),
          [ch("All conditions are met, because the treatments were randomly assigned", "Random assignment gives the randomization condition, but the sample data condition is also needed."),
           ch("The randomization condition is not met, because the sample sizes are not equal to each other in the two groups", "The sample sizes need not be equal, and random assignment meets the randomization condition."),
           ch("The 10% condition is not met, because the group sizes are small", "The 10% condition is unnecessary for a randomized experiment.")],
          "n < 30 and an outlier in Group 1: the sample data condition is not met.", diagram=bxs, difficulty="medium")

    B.mcq(T, "A student writes the hypotheses H₀: x̄₁ = x̄₂ and Hₐ: x̄₁ > x̄₂ for a test about the mean times of all students in two schools, where x̄₁ and x̄₂ are the mean times of the students in two samples. What is the error?",
          ch("The hypotheses are about sample means, but they should be about the population means μ₁ and μ₂", "Hypotheses are statements about population parameters."),
          [ch("The null hypothesis should have the inequality x̄₁ > x̄₂, and the alternative should have the equality", "The null hypothesis has the equality."),
           ch("The alternative hypothesis must always be two-sided", "An alternative hypothesis can be one-sided."),
           ch("There is no error, because the sample means are used to carry out the test", "The sample means are used in the test statistic, but the hypotheses are about the parameters.")],
          "Hypotheses use the parameters μ1 and μ2, not the statistics.", difficulty="medium")

    # ------------------------------------------------------------------------------------------------------------ 4.10
    T = 10
    t1 = t2_test(24.1, 5.2, 30, 21.0, 4.8, 32, "ne")
    B.mcq(T, "Independent random samples of students from two schools have times, in minutes, to finish a test. School A: n = 30, mean 24.1, standard deviation 5.2. School B: n = 32, mean 21.0, standard deviation 4.8. A test has H₀: μ₁ - μ₂ = 0 and Hₐ: μ₁ - μ₂ ≠ 0. What is the value of the test statistic?",
          ch(f"t = {f2(t1.t)}", f"t = (24.1 - 21.0) / √(5.2²/30 + 4.8²/32) = 3.1 / {f3(t1.se)}."),
          [ch(f"t = {f2(3.1 / math.sqrt(5.2 ** 2 + 4.8 ** 2))}", "This leaves out the division by the sample sizes inside the standard error."),
           ch(f"t = {f2(3.1 / (math.sqrt(5.2 ** 2 / 30) + math.sqrt(4.8 ** 2 / 32)))}", "This adds the two standard errors instead of adding the variances and taking the square root."),
           ch(f"t = {f2((21.0 - 24.1) / t1.se)}", "The difference is taken in the wrong order for Hₐ as written: μ₁ - μ₂ uses 24.1 - 21.0.")],
          f"t = 3.1 / {f3(t1.se)} = {f2(t1.t)}.", difficulty="medium")

    pone = 2 * float(sps.t.sf(2.43, 58.8))
    B.mcq(T, f"A two-sample t-test of H₀: μ₁ - μ₂ = 0 versus Hₐ: μ₁ - μ₂ ≠ 0 gives t = {f2(t1.t)}, and technology reports {t1.df:.1f} degrees of freedom. Which of the following is the p-value?",
          ch(f3(t1.p), "The two-sided p-value is 2P(t ≥ 2.43) with about 59 degrees of freedom."),
          [ch(f3(t1.p / 2), "This is the one-sided p-value, for Hₐ: μ₁ - μ₂ > 0 only."),
           ch(f3(2 * float(sps.norm.sf(t1.t))), "This uses the standard normal distribution. The p-value should come from the t-distribution."),
           ch(f3(1 - t1.p), "This is 1 minus the two-sided p-value, which is not a tail probability.")],
          f"p-value = 2P(t ≥ {f2(t1.t)}) = {f3(t1.p)}.", difficulty="medium")

    B.mcq(T, f"Independent random samples of students from School A and School B are used in a two-sample t-test of H₀: μ₁ - μ₂ = 0 versus Hₐ: μ₁ - μ₂ ≠ 0, where μ₁ and μ₂ are the mean times, in minutes, to finish a test for all students at the schools. The p-value is {f3(t1.p)}. Which of the following is the best conclusion at the 0.05 significance level?",
          ch("There is convincing statistical evidence that the mean times to finish the test are different for all students at the two schools", f"The p-value, {f3(t1.p)}, is less than 0.05: reject H0."),
          [ch("There is convincing statistical evidence that the mean times to finish the test are equal for all students at the two schools, as H₀ states", "A small p-value is evidence for a difference, not for sameness."),
           ch("There is not convincing statistical evidence of a difference, because the sample means differ by only 3.1 minutes", "The decision depends on the p-value. A difference in the sample means can still be significant."),
           ch("There is convincing statistical evidence that the mean times are different for the students in the two samples", "The conclusion should be about the population means, not the samples.")],
          f"p-value {f3(t1.p)} < 0.05: reject H0.", difficulty="medium")

    B.mcq(T, "In a randomized experiment, 40 volunteers are randomly assigned to a new study method and 40 volunteers to the usual method. A two-sample t-test of H₀: μ₁ - μ₂ = 0 versus Hₐ: μ₁ - μ₂ > 0 has a p-value of 0.006. Which of the following is the best conclusion at the 0.05 significance level?",
          ch("There is convincing statistical evidence that the new method causes a greater mean score than the usual method for students like these volunteers", "The p-value is small and the treatments were randomly assigned."),
          [ch("There is convincing statistical evidence that the new method would cause a greater mean score for all students in the country, since the treatments were randomly assigned", "The volunteers were not a random sample of all students, so the conclusion applies only to similar students."),
           ch("There is only evidence of an association between the method and the score, because the volunteers chose to take part", "Random assignment of the treatments allows a cause-and-effect conclusion."),
           ch("There is not convincing statistical evidence of a difference, because the p-value is not 0", "The p-value is less than 0.05, so the evidence is convincing.")],
          "Small p-value and random assignment: convincing evidence of a causal effect for similar volunteers.", difficulty="medium")

    t3 = t2_test(78.4, 12.0, 35, 75.1, 11.0, 38, "gt")
    B.mcq(T, f"Independent random samples of 35 students at School A and 38 students at School B are used to test H₀: μ₁ - μ₂ = 0 versus Hₐ: μ₁ - μ₂ > 0, where μ₁ and μ₂ are the mean test scores of all students at the schools. The sample means are 78.4 and 75.1. The test gives t = {f2(t3.t)} and a p-value of {f3(t3.p)}. Which of the following is the best conclusion at the 0.05 significance level?",
          ch("There is not convincing statistical evidence that the mean test score of all students at School A is greater than that at School B", f"The p-value, {f3(t3.p)}, is greater than 0.05: fail to reject H0."),
          [ch("There is convincing statistical evidence that the mean test scores of all students at the two schools are equal", "A test cannot show that the null hypothesis is true."),
           ch("There is convincing statistical evidence that the mean test score of all students at School A is greater than that at School B, because 78.4 is greater than 75.1", f"The p-value, {f3(t3.p)}, is greater than 0.05, so the evidence is not convincing."),
           ch("It has been proved that the two schools have the same mean test score", "Failing to reject H0 does not prove anything about equality.")],
          f"p-value {f3(t3.p)} > 0.05: fail to reject H0.", difficulty="medium")

    B.mcq(T, "A two-sample t-test for the difference between two population means has a p-value of 0.02. Which of the following is the correct interpretation of the p-value?",
          ch("Assuming that the two population means are equal, the probability of getting a difference in the sample means at least as extreme as the one observed is 0.02", "The p-value is computed assuming that the null hypothesis is true: the means are equal."),
          [ch("The probability that the two population means are equal is 0.02", "The p-value is not the probability that the null hypothesis is true."),
           ch("Assuming that the two population means are different, the probability of a difference in the sample means at least as extreme as the one observed is 0.02 in the study", "The p-value is computed assuming the null hypothesis, of no difference, is true."),
           ch("The difference between the two sample means is 0.02", "The p-value is a probability, not a difference in means.")],
          "The p-value is computed assuming H0 (equal means) is true.", difficulty="medium")

    B.mcq(T, "A student calculates a test statistic for a difference in two sample means as ($\\bar{x}_1 - \\bar{x}_2$) / $\\sqrt{(s_1^2 + s_2^2) / (n_1 + n_2)}$. What is wrong with this standard error?",
          ch("The standard error of the difference is √(s₁²/n₁ + s₂²/n₂): each variance is divided by its own sample size, then added", "The variance of each sample mean is s² / n for that sample."),
          [ch("Nothing is wrong, because the variances and the sample sizes can be added separately", "The variances must be divided by their own sample sizes."),
           ch("The standard error should add the standard deviations s₁ + s₂ and divide by n₁ + n₂", "The variances are added, not the standard deviations."),
           ch("The standard error should use the product of the sample sizes", "The sample sizes are used in the denominators of each term.")],
          "SE = √(s1²/n1 + s2²/n2).", difficulty="hard")

    ts = t2_test(3.1 + 21.0, 5.2, 30, 21.0, 4.8, 32, "ne")
    tl = t2_test(3.1 + 21.0, 5.2, 120, 21.0, 4.8, 128, "ne")
    assert tl.p < 0.0001, tl.p
    B.mcq(T, f"Two studies find the same sample mean difference (3.1 minutes) and the same standard deviations (5.2 and 4.8). Study X has samples of about 30 per group and Study Y has about 120 per group. The two-sided p-values are {f3(ts.p)} for Study X and less than 0.0001 for Study Y. Which of the following is the best explanation for the difference between the p-values?",
          ch("The larger samples in Study Y give a smaller standard error, so the same difference is farther from 0 in standard errors and the p-value is smaller", "The test statistic is the difference divided by the standard error, which decreases with the sample size."),
          [ch("The larger samples in Study Y give a larger difference in the sample means", "The sample mean difference is the same, 3.1, in both studies."),
           ch("The p-value does not depend on the sample sizes, so the difference is due to chance", "The standard error depends on the sample sizes, so the p-value does too."),
           ch("The larger samples in Study Y give a larger standard error, so the p-value is smaller", "A larger sample gives a smaller standard error, not a larger one.")],
          "Same difference, smaller SE with larger n: a larger t and a smaller p-value.", difficulty="hard")

    B.mcq(T, "A two-sample t-test comparing the mean scores of two groups gives a p-value of 0.30. Which of the following is the best interpretation?",
          ch("Assuming that the two population means are equal, a difference in the sample means this large would not be unusual; there is not convincing evidence of a difference", "A p-value that is not small does not provide convincing evidence for the alternative."),
          [ch("There is a 30% chance that the two population means are equal", "The p-value is not the probability that the null hypothesis is true."),
           ch("There is convincing evidence that the two population means are equal", "A test cannot show that the null hypothesis is true."),
           ch("The two sample means are 30% different", "The p-value is not a percent difference of the sample means.")],
          "A p-value of 0.30 would not be unusual under H0.", difficulty="medium")
