"""Unit 3, topics 3.9 to 3.13 (two proportions).

Required content (CED effective Fall 2026): 3.9 for independent samples the sampling distribution of p-hat1 - p-hat2 has mean p1 - p2 and standard deviation sqrt(p1(1 - p1)/n1 + p2(1 - p2)/n2); conditions: two independent random samples
(or an experiment with random assignment, where only randomization is needed), n <= 10% of each population, and n1p1, n1(1 - p1), n2p2, n2(1 - p2) all at least 10; interpret in context. 3.10 the two-sample z-interval for p1 - p2: parameters in context,
conditions (randomization, 10% unless an experiment, at least 10 observed successes and failures in both groups), (p-hat1 - p-hat2) +- z* sqrt(p-hat1(1 - p-hat1)/n1 + p-hat2(1 - p-hat2)/n2). 3.11 interpret the interval and the confidence level; if the
interval contains 0 there is not convincing evidence of a difference, if it does not there is. 3.12 the two-sample z-test: H0: p1 = p2 (or p1 - p2 = 0), the alternatives, conditions with the combined (pooled) proportion $\hat{p}_c$ in the expected counts.
3.13 z = (p-hat1 - p-hat2) / sqrt($\hat{p}_c$(1 - $\hat{p}_c$)(1/n1 + 1/n2)); the p-value, the decision against alpha, a conclusion in context about the two populations. Skills 2.C, 2.E, 3.D, 3.E, 4.D, 4.E, 4.F, 4.G.
"""
from scipy import stats as sps

from lib import *


def f3(v):
    return f"{float(v):.3f}"


def f4(v):
    return f"{float(v):.4f}"


def build(B):
    # ------------------------------------------------------------------------------------------------------------ 3.9
    T = 9
    p1, n1, p2, n2 = 0.60, 200, 0.50, 250
    mu_d = p1 - p2
    sd_d = math.sqrt(p1 * (1 - p1) / n1 + p2 * (1 - p2) / n2)
    B.mcq(T, "Independent random samples of 200 adults from City A and 250 adults from City B are selected. In City A, the proportion of all adults who own a bicycle is 0.60, and in City B it is 0.50. What are the mean and the standard deviation of the sampling distribution of p̂₁ - p̂₂?",
          ch(f"The mean is 0.10 and the standard deviation is {f4(sd_d)}", "μ = p₁ - p₂ = 0.10 and σ = √(p₁(1 - p₁) / n₁ + p₂(1 - p₂) / n₂) = √(0.0012 + 0.0010)."),
          [ch(f"The mean is 0.10 and the standard deviation is {f4(math.sqrt(0.6 * 0.4 / 200) + math.sqrt(0.5 * 0.5 / 250))}", "This adds the two standard deviations. The variances are added, and then the square root is taken."),
           ch(f"The mean is 0.10 and the standard deviation is {f4(sd_d ** 2)}", "This is the variance, before the square root is taken."),
           ch(f"The mean is 1.10 and the standard deviation is {f4(sd_d)}", "The mean of the difference is the difference of the means, 0.60 - 0.50, not the sum.")],
          f"μ = 0.10 and σ = √(0.0012 + 0.0010) = {f4(sd_d)}.", difficulty="medium")

    B.mcq(T, "Which of the following conditions must be met for the sampling distribution of p̂₁ - p̂₂ to be approximately normal when the data come from two independent random samples taken without replacement?",
          ch("Each sample is at most 10% of its population, and n₁p₁, n₁(1 - p₁), n₂p₂ and n₂(1 - p₂) are all at least 10",
             "These are the 10% condition for each sample and the expected counts of successes and failures in both samples."),
          [ch("Each sample is at least 10% of its population, and the sample sizes are both greater than 30, so the counts do not matter",
              "Each sample should be at most 10% of its population, and the conditions use the counts of successes and failures."),
           ch("The two sample sizes are equal, and the two population proportions are equal",
              "Neither is required. The sample sizes and the proportions can be different."),
           ch("The two samples are dependent, and each sample has at least 5 successes and 5 failures",
              "The samples should be independent, and at least 10 successes and failures are needed.")],
          "Independent random samples, the 10% condition for each, and expected counts of at least 10 in all four cells.", difficulty="medium")

    B.mcq(T, "A researcher randomly assigns 120 volunteers to one of two treatments, 60 to each, and compares the proportions that improve. Which condition is needed for the sampling distribution of p̂₁ - p̂₂ to be used?",
          ch("The treatments must be randomly assigned to the volunteers; the 10% condition is not needed", "For an experiment, the data need to meet the randomization condition, and random assignment provides it."),
          [ch("The volunteers must be a random sample from a population, and the 10% condition must be met", "In an experiment, the condition is on the random assignment, and the 10% condition is unnecessary."),
           ch("The two groups must be selected without replacement from populations that are at least 10 times larger", "The 10% condition is not needed for a randomized experiment."),
           ch("The volunteers must choose their treatment, so that each person is in the group that they prefer", "Choosing a treatment is not randomization. The treatments must be randomly assigned.")],
          "For an experiment, randomization means random assignment of treatments; the 10% condition is unnecessary.", difficulty="medium")

    B.mcq(T, "The sampling distribution of p̂₁ - p̂₂ has a mean of 0.10 for independent random samples from City A and City B. Which of the following is the correct interpretation of the mean?",
          ch("Over many pairs of random samples, the mean of the differences in the sample proportions, City A minus City B, is 0.10, which is p₁ - p₂", "The mean of the sampling distribution is the difference in the population proportions."),
          [ch("In every pair of random samples, the sample proportion for City A is exactly 0.10 greater than the sample proportion for City B in that pair", "The differences vary from one pair of samples to another."),
           ch("The proportion of adults in City A is 0.10 and the proportion of adults in City B is 0.10", "The mean describes the difference, 0.10, not each proportion."),
           ch("The sample proportions for the two cities are each equal to 0.10 on average", "It is the difference between the sample proportions whose average is 0.10.")],
          "Interpret the mean in context: the average difference over many pairs of samples.", difficulty="medium")

    zz = (0 - mu_d) / sd_d
    pp = float(sps.norm.sf(zz))
    B.mcq(T, "Independent random samples of 200 adults from City A (p₁ = 0.60) and 250 adults from City B (p₂ = 0.50) are selected. The sampling distribution of p̂₁ - p̂₂ is approximately normal with mean 0.10 and standard deviation 0.0469. What is the approximate probability that the sample proportion for City A is greater than the sample proportion for City B?",
          ch(f3(pp), f"P(p̂₁ - p̂₂ > 0) = P(z > (0 - 0.10) / 0.0469) = P(z > {zz:.2f})."),
          [ch(f3(sps.norm.cdf(zz)), f"This is P(z < {zz:.2f}), the probability that the sample proportion for City A is less than the sample proportion for City B."),
           ch("0.500", "This would be the probability if the mean of the difference were 0. The mean is 0.10."),
           ch(f3(sps.norm.sf((0 - 0.10) / (0.0469 * 2))), "This doubles the standard deviation, which is not the standard deviation of the difference.")],
          f"P(p-hat1 - p-hat2 > 0) = P(z > {zz:.2f}), about {f3(pp)}.", difficulty="hard")

    s_small = math.sqrt(0.6 * 0.4 / 200 + 0.5 * 0.5 / 250)
    s_large = math.sqrt(0.6 * 0.4 / 800 + 0.5 * 0.5 / 1000)
    assert abs(s_small / s_large - 2) < 1e-9
    B.mcq(T, "Both sample sizes are multiplied by 4, from 200 and 250 to 800 and 1,000, and the population proportions stay the same. What happens to the standard deviation of the sampling distribution of p̂₁ - p̂₂?",
          ch("It is divided by 2", "Each variance is divided by 4, so the variance of the difference is divided by 4 and the standard deviation is divided by 2."),
          [ch("It is divided by 4", "The standard deviation involves a square root, so it is divided by 2, not by 4."),
           ch("It is multiplied by 4", "Larger samples have less variability, so the standard deviation decreases."),
           ch("It does not change", "The sample sizes are in the formula, so the standard deviation changes.")],
          "σ is proportional to 1 / √n for both samples: it is divided by 2.", difficulty="medium")

    B.mcq(T, "Independent random samples of 40 adults from Town A and 60 adults from Town B are selected. The population proportions are p₁ = 0.15 and p₂ = 0.40. Is the sampling distribution of p̂₁ - p̂₂ approximately normal?",
          ch("No, because n₁p₁ = 40(0.15) = 6 is less than 10", "All four expected counts must be at least 10, and n₁p₁ = 6."),
          [ch("Yes, because n₁ and n₂ are both greater than 30", "The conditions use the expected counts of successes and failures."),
           ch("Yes, because n₂p₂ = 60(0.40) = 24 is greater than 10", "All four expected counts must be at least 10, and the first is 6."),
           ch("No, because the two sample sizes are not equal", "The sample sizes do not need to be equal.")],
          "n1 p1 = 6 < 10, so the normal approximation is not appropriate.", difficulty="medium")

    # ------------------------------------------------------------------------------------------------------------ 3.10
    T = 10
    x1, m1, x2, m2 = 120, 200, 90, 220
    ci2 = two_prop_ci(x1, m1, x2, m2, 0.95)
    B.mcq(T, "Independent random samples of students from two large schools are used to estimate the difference between the proportions of all students at the two schools who favor a later start time. Which procedure is appropriate?",
          ch("A two-sample z-interval for a difference between population proportions", "The goal is to estimate p₁ - p₂ from two independent samples."),
          [ch("A one-sample z-interval for a population proportion", "There are two populations, so the parameter is a difference between two proportions."),
           ch("A chi-square test for independence", "A chi-square test is for categorical variables in a two-way table, and the goal here is an interval estimate."),
           ch("A two-sample z-test for a difference between population proportions", "A test is for evaluating a claim about the difference. The goal here is to estimate it.")],
          "Estimating p1 - p2 from two independent samples: a two-sample z-interval.", difficulty="easy")

    B.mcq(T, "Independent random samples from two large schools, School A and School B, are used to construct an interval for the difference in the proportions of all students at the schools who favor a later start time. Which of the following correctly states the parameter?",
          ch("p₁ - p₂ = the difference between the proportion of all students at School A who favor a later start time and the proportion of all students at School B who favor a later start time", "The parameter refers to the difference, the response variable and both populations."),
          [ch("p̂₁ - p̂₂ = the difference between the proportions of the students in the two samples who favor a later start time", "This is a statistic. The parameter is about the populations."),
           ch("p = the proportion of all students at both schools who favor a later start time", "This is a single combined proportion, not a difference."),
           ch("p₁ - p₂ = the difference between the number of students at the two schools who favor a later start time", "The parameter is a difference in proportions, not in counts.")],
          "The parameter is the difference between the two population proportions, in context.", difficulty="easy")

    B.mcq(T, "Which of the following lists the conditions for a two-sample z-interval for a difference between two population proportions when the data come from two independent random samples taken without replacement?",
          ch("Both samples are random and independent; each sample is at most 10% of its population; and the observed numbers of successes and failures in both samples are at least 10",
             "These are the randomization, 10% and normality conditions for two samples."),
          [ch("Both samples are random; each sample is at least 10% of its population; and the numbers of observed successes and failures are at least 5 in each of the two samples",
              "The samples should be at most 10% of the populations, and the counts should be at least 10."),
           ch("The two samples are paired; the population is approximately normal; and the sample sizes are each greater than 30",
              "The samples are independent, and the condition is on the counts of successes and failures."),
           ch("One sample is random; the other is a convenience sample; and the counts of successes and failures are each at least 10",
              "Both samples must be random.")],
          "Randomization, the 10% condition for each sample, and at least 10 observed successes and failures in each.", difficulty="medium")

    B.mcq(T, "In a random sample of 200 students from School A, 120 favor a later start time. In an independent random sample of 220 students from School B, 90 favor a later start time. Which of the following is a 95% confidence interval for the difference between the proportions of all students at the two schools who favor a later start time, School A minus School B?",
          ch(f"({f3(ci2.lo)}, {f3(ci2.hi)})", f"p̂₁ - p̂₂ = 0.600 - 0.409 = {f3(ci2.diff)}, and the margin of error is 1.96 × {f4(ci2.se)} = {f3(ci2.moe)}."),
          [ch(f"({f3(ci2.diff - 1.645 * ci2.se)}, {f3(ci2.diff + 1.645 * ci2.se)})", "This uses z* = 1.645, which is for a 90% confidence level."),
           ch(f"({f3(ci2.diff - 1.96 * (math.sqrt(ci2.p1 * (1 - ci2.p1) / m1) + math.sqrt(ci2.p2 * (1 - ci2.p2) / m2)))}, {f3(ci2.diff + 1.96 * (math.sqrt(ci2.p1 * (1 - ci2.p1) / m1) + math.sqrt(ci2.p2 * (1 - ci2.p2) / m2)))})", "This adds the two standard errors instead of adding the variances and taking the square root."),
           ch(f"({f3(ci2.p1 - 1.96 * ci2.se)}, {f3(ci2.p1 + 1.96 * ci2.se)})", "This is centered at the sample proportion for School A instead of at the difference in the proportions.")],
          f"{f3(ci2.diff)} ± {f3(ci2.moe)} = ({f3(ci2.lo)}, {f3(ci2.hi)}).", difficulty="medium")

    B.mcq(T, "In a random sample of 200 students from School A, 120 favor a later start time. In an independent random sample of 220 students from School B, 90 favor a later start time. What is the standard error of p̂₁ - p̂₂?",
          ch(f4(ci2.se), "SE = √(p̂₁(1 - p̂₁) / n₁ + p̂₂(1 - p̂₂) / n₂) = √(0.6(0.4) / 200 + 0.409(0.591) / 220)."),
          [ch(f4(ci2.se ** 2), "This is the variance of the difference, before the square root."),
           ch(f4(math.sqrt(ci2.p1 * (1 - ci2.p1) / m1) + math.sqrt(ci2.p2 * (1 - ci2.p2) / m2)), "This adds the two standard errors. The variances are added first."),
           ch(f4(math.sqrt(ci2.p1 * (1 - ci2.p1) / m1) - math.sqrt(ci2.p2 * (1 - ci2.p2) / m2)), "This subtracts the standard errors. The variances of independent samples are added.")],
          f"SE = {f4(ci2.se)}.", difficulty="medium")

    B.mcq(T, "A researcher randomly assigns 100 volunteers to a new exercise program and 100 volunteers to a control group. After 8 weeks, 45 of the volunteers in the program group and 30 of the volunteers in the control group have lowered their blood pressure. Which of the following is correct about the conditions for a two-sample z-interval for the difference in proportions?",
          ch("The randomization condition is met by the random assignment, the 10% condition is not needed, and all four counts (45, 55, 30 and 70) are at least 10",
             "For a randomized experiment, the 10% condition is unnecessary, and the observed successes and failures are all at least 10."),
          [ch("The randomization condition is not met, because the volunteers were not randomly selected from a population of all people",
              "For an experiment, random assignment of the treatments is what is needed."),
           ch("The 10% condition is not met, because 100 is more than 10% of the 8 weeks of the study",
              "The 10% condition does not apply to a randomized experiment, and it is not about weeks."),
           ch("The normality condition is not met, because 30 is less than 45", "The counts do not need to be equal. They need to be at least 10.")],
          "Random assignment gives randomization; the counts 45, 55, 30 and 70 are all at least 10.", difficulty="medium")

    B.mcq(T, "A confidence interval is calculated for the difference in two population proportions, p₁ - p₂. The sample proportions are p̂₁ = 0.45 and p̂₂ = 0.30. Which of the following is the point estimate for the difference?",
          ch("0.15", "The point estimate is p-hat1 - p-hat2 = 0.45 - 0.30."),
          [ch("0.75", "This is the sum p̂₁ + p̂₂. The point estimate for the difference is found by subtracting."),
           ch("0.375", "This is the mean of the two sample proportions, not their difference."),
           ch("-0.15", "This is p̂₂ - p̂₁. The difference is written in the order that the parameter is defined: p₁ - p₂.")],
          "Point estimate = 0.45 - 0.30 = 0.15.", difficulty="easy")

    B.mcq(T, "A student wants to construct a 90% confidence interval for p₁ - p₂. Which critical value z* should be used?",
          ch("1.645", "The middle 90% of the standard normal distribution lies between -1.645 and 1.645."),
          [ch("1.960", "This is the critical value for a 95% confidence level."),
           ch("2.576", "This is the critical value for a 99% confidence level."),
           ch("1.282", "This is the z-score with 10% of the area above it, which is for an 80% confidence level.")],
          "z* = 1.645 for a 90% confidence level.", difficulty="easy")

    # ------------------------------------------------------------------------------------------------------------ 3.11
    T = 11
    B.mcq(T, f"A 95% confidence interval for the difference between the proportions of all students at School A and School B who favor a later start time, School A minus School B, is ({f3(ci2.lo)}, {f3(ci2.hi)}). Which of the following is a correct interpretation?",
          ch(f"We are 95% confident that the interval from {f3(ci2.lo)} to {f3(ci2.hi)} contains the difference between the proportion of all students at School A and the proportion of all students at School B who favor a later start time",
             "The interpretation references the parameter and both populations in context."),
          [ch(f"There is a 95% probability that the difference between the sample proportions of the two schools is between {f3(ci2.lo)} and {f3(ci2.hi)}",
              "The sample proportions are known. The interval is about the difference in the population proportions."),
           ch(f"95% of the students at School A favor a later start time, compared with between {f3(ci2.lo)} and {f3(ci2.hi)} of the students at School B",
              "The interval is for a difference between two proportions, not for each proportion."),
           ch(f"About 95% of the pairs of students, one from each school, differ by an amount between {f3(ci2.lo)} and {f3(ci2.hi)}",
              "The interval does not describe pairs of students.")],
          "The interval is interpreted for the difference in the population proportions.", difficulty="medium")

    B.mcq(T, "A 95% confidence interval for p₁ - p₂, the difference between the proportions of adults in two cities who own a bicycle, is (-0.03, 0.11). Which of the following is the best conclusion?",
          ch("There is not convincing evidence of a difference between the two population proportions, because 0 is in the interval", "If the interval contains 0, there is insufficient evidence of a difference."),
          [ch("There is convincing evidence that the two population proportions are equal, because 0 is in the interval", "An interval that contains 0 does not prove that the proportions are equal."),
           ch("There is convincing evidence that the proportion in the first city is greater, because most of the interval is positive", "The interval includes negative values and 0, so a difference is not shown."),
           ch("There is convincing evidence of a difference, because the interval is not centered at 0", "The question is whether 0 is a plausible value. It is in the interval.")],
          "0 is a plausible value for p1 - p2, so a difference has not been shown.", difficulty="medium")

    B.mcq(T, "A 95% confidence interval for p₁ - p₂, the difference between the proportions of customers who are satisfied with Store 1 and Store 2, is (0.06, 0.18). Which of the following is the best conclusion?",
          ch("There is convincing evidence that the proportion of all customers who are satisfied is greater for Store 1, because all of the plausible values are positive", "The interval does not contain 0, and every value in it is greater than 0."),
          [ch("There is convincing evidence that the proportions are equal, because the interval is narrow", "The width of the interval does not show equal proportions."),
           ch("There is convincing evidence that the proportion is greater for Store 2 than for Store 1, because the interval of plausible values is positive", "A positive difference p₁ - p₂ means that Store 1 has the greater proportion."),
           ch("There is not convincing evidence of a difference, because the interval has a width of 0.12", "A width does not decide this. The interval does not contain 0.")],
          "The interval has only positive values: p1 > p2.", difficulty="medium")

    B.mcq(T, "A 99% confidence interval for p₁ - p₂ is (-0.22, -0.06), where p₁ is the proportion of all patients who recover with Drug 1 and p₂ is the proportion of all patients who recover with Drug 2. Which of the following is the best conclusion?",
          ch("There is convincing evidence that the proportion who recover is less with Drug 1 than with Drug 2, because the interval has only negative values", "A negative difference p₁ - p₂ means that p₁ is less than p₂."),
          [ch("There is convincing evidence that the proportion who recover is greater with Drug 1 than with Drug 2, because the interval has only negative values", "Negative values of p₁ - p₂ mean p₁ is less than p₂."),
           ch("There is not convincing evidence of a difference, because the lower limit of the interval is negative", "Both limits are negative, so 0 is not in the interval."),
           ch("The proportion who recover with Drug 2 is exactly 0.14 greater than with Drug 1, since 0.14 is the center of the interval", "The interval is a range of plausible values, not an exact value.")],
          "Both limits are negative, so p1 < p2.", difficulty="medium")

    B.mcq(T, "Which of the following is the correct interpretation of the confidence level in a 95% confidence interval for the difference between two population proportions?",
          ch("In repeated random sampling with the same sample sizes, approximately 95% of the intervals created will capture the difference between the two population proportions",
             "The confidence level describes the long-run rate at which the method captures the parameter."),
          [ch("There is a 95% chance that the one interval that was created contains the difference in the sample proportions",
              "The difference in the sample proportions is known and is the center of the interval."),
           ch("In repeated random sampling, 95% of the differences in the sample proportions will be equal to the difference in the population proportions",
              "Most differences in sample proportions are not equal to the population difference."),
           ch("The difference between the population proportions is 95% of the time between the limits of the interval",
              "The difference in the population proportions is a fixed value. It does not move.")],
          "Long-run capture rate of the method: about 95% of intervals.", difficulty="medium")

    B.mcq(T, "In a randomized experiment, 150 volunteers are randomly assigned to a new teaching method and 150 volunteers to the usual method. A 95% confidence interval for p₁ - p₂, the difference between the proportions of volunteers that would pass a test with the new method and with the usual method, is (0.05, 0.21). Which of the following is the best conclusion?",
          ch("There is convincing evidence that the new method causes a greater proportion of volunteers like these to pass, because the treatments were randomly assigned and the interval contains only positive values",
             "Random assignment allows a cause-and-effect conclusion, for individuals similar to the volunteers."),
          [ch("There is convincing evidence that the new method would cause a greater proportion of all students in the world to pass the test, because the interval contains only positive values",
              "The volunteers were not randomly selected from all students, so the conclusion cannot be generalized so widely."),
           ch("There is only evidence of an association between the method and passing, because the volunteers chose to take part",
              "Random assignment of the treatments allows a cause-and-effect conclusion."),
           ch("There is not convincing evidence of a difference, because the lower limit, 0.05, is close to 0",
              "The interval does not contain 0, so there is convincing evidence of a difference.")],
          "Random assignment gives cause and effect; volunteers limit the generalization.", difficulty="hard")

    ci_small = two_prop_ci(30, 100, 20, 100, 0.95)
    ci_large = two_prop_ci(300, 1000, 200, 1000, 0.95)
    B.mcq(T, f"Two studies each find a sample proportion of 0.30 in Group 1 and 0.20 in Group 2. Study X has 100 per group and Study Y has 1,000 per group. The 95% intervals for p₁ - p₂ are ({f3(ci_small.lo)}, {f3(ci_small.hi)}) for Study X and ({f3(ci_large.lo)}, {f3(ci_large.hi)}) for Study Y. Which of the following is the best conclusion?",
          ch("Only Study Y provides convincing evidence of a difference, because its interval does not contain 0; the larger samples give a narrower interval", "The interval for Study X contains 0, so a difference is not shown."),
          [ch("Both studies provide convincing evidence of a difference, because the sample proportions are the same in both studies", "The same sample proportions do not give the same evidence. The sample sizes matter."),
           ch("Only Study X provides convincing evidence of a difference, because its interval is wider", "A wider interval is less precise, and it contains 0."),
           ch("Neither study provides convincing evidence of a difference, because both differences in the sample proportions are the same, 0.10", "Study Y's interval does not contain 0.")],
          "The larger samples in Study Y give a smaller standard error and an interval that excludes 0.", diagram=None, difficulty="hard")

    # ------------------------------------------------------------------------------------------------------------ 3.12
    T = 12
    B.mcq(T, "In a randomized experiment, 100 patients are randomly assigned to a new medicine and 100 patients to a placebo. A researcher wants to test whether the proportion of all patients like these who would improve is greater with the new medicine. Which procedure is appropriate?",
          ch("A two-sample z-test for the difference between two population proportions", "The test compares the proportions that improve in two treatment groups."),
          [ch("A one-sample z-test for a population proportion", "There are two groups to compare, so the parameter is a difference between two proportions."),
           ch("A two-sample z-interval for a difference between population proportions", "An interval estimates the difference. This question asks for a test of a claim."),
           ch("A chi-square test for independence", "A chi-square test compares distributions of a categorical variable or tests for an association. It does not test a directional claim about two proportions.")],
          "Comparing two proportions in a test: a two-sample z-test.", difficulty="easy")

    B.mcq(T, "In a randomized experiment, patients are randomly assigned to a new medicine (population 1) or a placebo (population 2). The researcher believes that the proportion of patients who improve is greater with the new medicine. Which are the correct hypotheses?",
          ch("H₀: p₁ - p₂ = 0 and Hₐ: p₁ - p₂ > 0, where p₁ and p₂ are the proportions of all patients like these who would improve with each treatment", "The null hypothesis states no difference, and the alternative states the belief."),
          [ch("H₀: p₁ - p₂ > 0 and Hₐ: p₁ - p₂ = 0, where p₁ and p₂ are the proportions of all patients like these who would improve with each treatment", "The null hypothesis has the equality (no difference)."),
           ch("H₀: p₁ - p₂ = 0 and Hₐ: p₁ - p₂ < 0, where p₁ and p₂ are the proportions of all patients like these who would improve with each treatment", "The researcher believes that p₁ is greater than p₂, so the alternative is p₁ - p₂ > 0."),
           ch("H₀: p̂₁ - p̂₂ = 0 and Hₐ: p̂₁ - p̂₂ > 0, where p̂₁ and p̂₂ are the proportions of the patients in the groups who improved", "Hypotheses are about the population parameters, not about the sample proportions.")],
          "H0: p1 - p2 = 0; Ha: p1 - p2 > 0.", difficulty="medium")

    B.mcq(T, "A school board wants to know whether the proportion of all students at School A who take the bus differs from the proportion of all students at School B who take the bus. Which of the following are the correct hypotheses?",
          ch("H₀: p₁ = p₂ and Hₐ: p₁ ≠ p₂, where p₁ and p₂ are the proportions of all students at School A and at School B who take the bus", "The claim is that the proportions differ, in either direction, so the alternative is two-sided."),
          [ch("H₀: p₁ ≠ p₂ and Hₐ: p₁ = p₂, where p₁ and p₂ are the proportions of all students at School A and at School B who take the bus", "The null hypothesis states that there is no difference."),
           ch("H₀: p₁ = p₂ and Hₐ: p₁ > p₂, where p₁ and p₂ are the proportions of all students at School A and at School B who take the bus", "The question does not say that School A is greater, so the alternative is two-sided."),
           ch("H₀: p = 0.5 and Hₐ: p ≠ 0.5, where p is the proportion of all students at both schools who take the bus", "The question compares two proportions. It is not a test about one proportion and 0.5.")],
          "A difference in either direction: Ha: p1 ≠ p2.", difficulty="easy")

    B.mcq(T, "A researcher will test a claim about two populations of adults, those in City A and those in City B, and the proportions who own a bicycle. Which of the following correctly defines the parameters?",
          ch("p₁ = the proportion of all adults in City A who own a bicycle, and p₂ = the proportion of all adults in City B who own a bicycle", "The parameters reference the proportions, the response variable and the populations in context."),
          [ch("p₁ = the proportion of the adults in the sample from City A who own a bicycle, and p₂ = the proportion of the adults in the sample from City B", "These are sample proportions, statistics, and not the population parameters."),
           ch("p = the proportion of all adults in City A and City B who own a bicycle", "This is one combined proportion. A test of a difference needs two parameters."),
           ch("p₁ = the number of adults in City A who own a bicycle, and p₂ = the number in City B", "The parameters are proportions, not counts.")],
          "The parameters are the two population proportions, in context.", difficulty="easy")

    pc = (45 + 30) / 200
    B.mcq(T, "In a randomized experiment, 45 of 100 patients improve with a new medicine and 30 of 100 patients improve with a placebo. For a two-sample z-test of H₀: p₁ - p₂ = 0, what is the combined (pooled) sample proportion $\hat{p}_c$?",
          ch(f3(pc), "$\hat{p}_c$ = (45 + 30) / (100 + 100) = 75 / 200."),
          [ch("0.450", "This is the sample proportion for the first group only."),
           ch("0.150", "This is the difference p̂₁ - p̂₂ = 0.45 - 0.30, not the combined proportion."),
           ch(f3(0.45 * 0.30), "This is the product of the two sample proportions, which has no meaning here.")],
          "$\hat{p}_c$ = 75 / 200 = 0.375.", difficulty="medium")

    B.mcq(T, "A researcher plans a two-sample z-test using independent random samples of n₁ = 40 and n₂ = 50 from two populations. The combined sample proportion of successes is $\hat{p}_c$ = 0.06. Is the normality condition met?",
          ch("No, because n₁$\hat{p}_c$ = 2.4, which is less than 10", "All four of n₁$\hat{p}_c$, n₁(1 - $\hat{p}_c$), n₂$\hat{p}_c$ and n₂(1 - $\hat{p}_c$) must be at least 10."),
          [ch("Yes, because n₁(1 - $\hat{p}_c$) and n₂(1 - $\hat{p}_c$) are both greater than 10", "All four expected counts must be at least 10, and the expected numbers of successes are 2.4 and 3.0."),
           ch("Yes, because both sample sizes are greater than 30", "The condition uses the expected counts of successes and failures, not only the sample sizes."),
           ch("No, because the two sample sizes are not equal", "The sample sizes do not need to be equal.")],
          "The expected numbers of successes, 2.4 and 3.0, are less than 10: the condition fails.", difficulty="medium")

    B.mcq(T, "Which conditions must be verified for a two-sample z-test for a difference between two population proportions when the data come from a randomized experiment?",
          ch("The treatments are randomly assigned, and n₁$\hat{p}_c$, n₁(1 - $\hat{p}_c$), n₂$\hat{p}_c$ and n₂(1 - $\hat{p}_c$) are all at least 10; the 10% condition is not needed", "For an experiment, the data need to meet the randomization condition, and the 10% condition is unnecessary."),
          [ch("The treatments are randomly assigned, and each group is at most 10% of a population", "The 10% condition is unnecessary for a randomized experiment."),
           ch("The two groups are independent random samples, and the combined proportion is exactly 0.5", "There is no condition that the combined proportion is 0.5, and an experiment needs random assignment."),
           ch("The volunteers are randomly selected from a population, and the counts of successes and failures are at least 5", "For an experiment, random assignment is what is needed, and the counts should be at least 10.")],
          "Random assignment, and expected counts of at least 10 using the combined proportion.", difficulty="medium")

    # ------------------------------------------------------------------------------------------------------------ 3.13
    T = 13
    tz = two_prop_z(45, 100, 30, 100, "gt")
    B.mcq(T, "In a randomized experiment, 45 of 100 patients improve with a new medicine and 30 of 100 improve with a placebo. A test of H₀: p₁ - p₂ = 0 versus Hₐ: p₁ - p₂ > 0 uses the combined proportion $\hat{p}_c$ = 0.375. What is the test statistic?",
          ch(f"z = {tz.z:.2f}", f"z = (0.45 - 0.30) / √(0.375(0.625)(1/100 + 1/100)) = 0.15 / {tz.se0:.4f}."),
          [ch(f"z = {(0.45 - 0.30) / math.sqrt(0.45 * 0.55 / 100 + 0.30 * 0.70 / 100):.2f}", "This uses the separate sample proportions in the standard error, as for an interval. A test uses the combined proportion."),
           ch(f"z = {(0.45 - 0.30) / math.sqrt(0.375 * 0.625 / 200):.2f}", "This treats the two groups as a single sample of 200 instead of using 1/100 + 1/100 in the standard error."),
           ch(f"z = {0.15 / math.sqrt(0.375 * 0.625 / 100):.2f}", "This uses the sample size of only one group in the standard error. Both groups are needed.")],
          f"z = {tz.z:.2f}.", difficulty="medium")

    B.mcq(T, "A two-sample z-test of H₀: p₁ - p₂ = 0 versus Hₐ: p₁ - p₂ > 0 gives z = 2.19. What is the p-value?",
          ch(f3(tz.p), "The p-value is the area to the right of z = 2.19 under the standard normal curve."),
          [ch(f3(2 * tz.p), "This is the two-sided p-value. The alternative is one-sided."),
           ch(f3(1 - tz.p), "This is the area to the left of z = 2.19, not a tail probability."),
           ch(f3(tz.p / 2), "This halves the one-sided p-value instead of leaving it as it is.")],
          f"p-value = P(z ≥ 2.19) = {f3(tz.p)}.", difficulty="medium")

    B.mcq(T, "In a randomized experiment, 100 patients are randomly assigned to a new medicine and 100 to a placebo. A two-sample z-test of H₀: p₁ - p₂ = 0 versus Hₐ: p₁ - p₂ > 0 has a p-value of 0.014. Which of the following is the best conclusion at the 0.05 significance level?",
          ch("There is convincing statistical evidence that the new medicine causes a greater proportion of patients like these to improve", "The p-value is less than 0.05 and the treatments were randomly assigned, so a cause-and-effect conclusion is justified."),
          [ch("There is convincing statistical evidence that the proportion of the patients in the experiment who improved is greater with the new medicine", "The conclusion should be about the population proportions, not about the patients in the sample."),
           ch("There is not convincing statistical evidence that the new medicine is better, because the p-value is not 0", "A p-value does not need to be 0. It is less than 0.05, so the evidence is convincing."),
           ch("It has been proved that the new medicine cures patients, since the p-value is small", "A test does not prove a claim, and \"cures\" is not what was tested.")],
          "p-value 0.014 < 0.05 and random assignment: convincing evidence of a causal effect.", difficulty="medium")

    tz2 = two_prop_z(48, 100, 41, 100, "ne")
    B.mcq(T, f"In independent random samples, 48 of 100 students at School A and 41 of 100 students at School B favor a later start time. A two-sample z-test of H₀: p₁ = p₂ versus Hₐ: p₁ ≠ p₂ gives z = {tz2.z:.2f} and a p-value of {f3(tz2.p)}. Which of the following is the correct conclusion at the 0.05 significance level?",
          ch("There is not convincing statistical evidence that the proportions of all students at the two schools who favor a later start time are different", f"The p-value, {f3(tz2.p)}, is greater than 0.05, so fail to reject H0."),
          [ch("There is convincing statistical evidence that the proportions of all students at the two schools who favor a later start time are different from each other", f"The p-value, {f3(tz2.p)}, is greater than 0.05, so the evidence is not convincing."),
           ch("There is convincing statistical evidence that the proportions of all students at the two schools who favor a later start time are equal", "A test cannot show that the null hypothesis is true."),
           ch("There is convincing statistical evidence that the proportion is greater at School A, because 0.48 is greater than 0.41", "The test is two-sided, and the p-value shows that the difference could be due to chance.")],
          f"p-value = {f3(tz2.p)} > 0.05: fail to reject H0.", difficulty="medium")

    B.mcq(T, "A two-sample z-test for a difference between two population proportions has a p-value of 0.014. Which of the following is the correct interpretation of the p-value?",
          ch("Assuming that the two population proportions are equal, the probability of getting a difference in the sample proportions at least as large as the one observed is 0.014", "The p-value is computed assuming that the null hypothesis is true: the proportions are equal."),
          [ch("The probability that the two population proportions are equal is 0.014", "The p-value is not the probability that the null hypothesis is true."),
           ch("The probability that the difference in the sample proportions is 0.014", "The p-value is not the difference. It is a tail probability under H0."),
           ch("Assuming that the two population proportions are different, the probability of a difference in the sample proportions at least as large as the one observed is 0.014", "The p-value is computed assuming that the null hypothesis, of no difference, is true.")],
          "The p-value is computed assuming H0, equal proportions, is true.", difficulty="medium")

    B.mcq(T, "Independent random samples of 200 adults in City A and 200 adults in City B are taken, and the proportions who use public transportation are compared with a two-sample z-test. The p-value is 0.003. Which of the following is the best conclusion?",
          ch("There is convincing evidence that the proportions of all adults in the two cities who use public transportation are different; this is an association, not cause and effect", "The data come from observational random samples, so the conclusion is about the populations and does not claim cause and effect."),
          [ch("There is convincing evidence that living in City A causes adults to use public transportation more than living in City B, because the p-value is small", "The study is observational, so a cause-and-effect conclusion is not justified."),
           ch("There is not convincing evidence of a difference, because the sample sizes are equal", "Equal sample sizes do not decide anything. The p-value is small."),
           ch("There is convincing evidence that the proportion of the adults in the samples is different, but nothing about the cities", "The conclusion applies to the two populations from which the random samples were taken.")],
          "Small p-value: evidence of a difference in the population proportions; random samples, not an experiment: no cause and effect.", difficulty="medium")

    B.mcq(T, "A student carries out a two-sample z-test for p₁ - p₂ with p̂₁ = 0.45, n₁ = 100, p̂₂ = 0.30 and n₂ = 100, and uses the standard error from the two-sample z-interval, √(p̂₁(1 - p̂₁)/n₁ + p̂₂(1 - p̂₂)/n₂) in the test statistic. What is wrong?",
          ch("A test of H₀: p₁ - p₂ = 0 assumes that the proportions are equal, so the standard error should use the combined proportion $\hat{p}_c$", "Under the null hypothesis the two populations share one proportion, estimated by the combined proportion."),
          [ch("Nothing is wrong, because the standard error for a test is always the same as the standard error for an interval of the difference", "The test uses the combined proportion because H0 says that the proportions are equal."),
           ch("The student should have used the sample sizes in place of the proportions", "The standard error uses the proportions and the sample sizes."),
           ch("The student should have used only the larger of the two sample proportions", "The combined proportion uses both groups.")],
          "A test uses the pooled proportion because H0 says p1 = p2.", difficulty="hard")

    tz3 = two_prop_z(52, 80, 38, 80, "gt")
    B.mcq(T, f"In a randomized experiment, 52 of 80 volunteers who use a new study app (group 1) and 38 of 80 volunteers who use a notebook (group 2) pass a test. A two-sample z-test of H₀: p₁ - p₂ = 0 versus Hₐ: p₁ - p₂ > 0 gives z = {tz3.z:.2f} and a p-value of {f3(tz3.p)}. Which of the following is the best conclusion at the 0.05 significance level?",
          ch("There is convincing evidence that the new app causes a greater proportion of volunteers like these to pass the test than the notebook does", f"The p-value, {f3(tz3.p)}, is less than 0.05 and the treatments were randomly assigned."),
          [ch("There is convincing evidence that the new app would cause a greater proportion of all students in the country to pass the test, since the treatments were randomly assigned", "The volunteers were not randomly selected from all students, so the conclusion applies only to similar volunteers."),
           ch("There is only evidence of an association between the app and passing, because the volunteers chose to take part", "Random assignment of the treatments allows a cause-and-effect conclusion."),
           ch("There is not convincing evidence of a difference, because the p-value is greater than 0.01", "The significance level is 0.05, and the p-value is less than that.")],
          f"z = {tz3.z:.2f}, p-value = {f3(tz3.p)} < 0.05: convincing evidence of a causal effect for similar volunteers.", difficulty="hard")
