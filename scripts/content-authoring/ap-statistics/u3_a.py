"""Unit 3, topics 3.1 to 3.4.

Required content (CED effective Fall 2026): 3.1 an estimator is unbiased if on average it neither under- nor overestimates the parameter; a sample statistic is a point estimator (p-hat for p). 3.2 the sampling distribution of p-hat has mean p
and standard deviation sqrt(p(1 - p)/n) when the sampled values are independent; conditions: random sample, 10% condition (n <= N/10, without replacement), and np >= 10 and n(1 - p) >= 10 for an approximately normal shape; interpret in context.
3.3 one-sample z-interval for a proportion: parameter in context, conditions (random, 10%, at least 10 observed successes and failures), p-hat +- z* sqrt(p-hat(1 - p-hat)/n), standard error, margin of error, n = (z*/MOE)^2 p-hat(1 - p-hat)
(p-hat = 0.5 when unknown). 3.4 interpret an interval and the confidence level (C% of intervals from repeated random samples of the same size capture p), justify a claim with the interval, how the width changes with the confidence level and the
sample size (width roughly proportional to 1 / sqrt(n)). Skills 2.C, 2.D, 3.D, 3.E, 4.B, 4.D, 4.E, 4.F, 4.G.
"""
from scipy import stats as sps

from lib import *


def f3(v):
    return f"{float(v):.3f}"


def f4(v):
    return f"{float(v):.4f}"


def build(B):
    # ------------------------------------------------------------------------------------------------------------ 3.1
    T = 1
    B.mcq(T, "A random sample of 200 adults in a city is selected, and 84 of them say that they ride the bus at least once a week. Which of the following is the point estimate of the proportion of all adults in the city who ride the bus at least once a week?",
          ch("0.42", "The sample proportion is a point estimator of the population proportion: 84 / 200 = 0.42."),
          [ch("84", "This is the number of adults in the sample who ride the bus, not a proportion."),
           ch("0.58", "This is the sample proportion of the adults who do not ride the bus at least once a week."),
           ch("0.50", "Nothing in the sample points to 0.50. The point estimate is the sample proportion.")],
          "The point estimate is p̂ = 84 / 200 = 0.42.", difficulty="easy")

    B.mcq(T, "Which of the following is the best description of an unbiased estimator of a population parameter?",
          ch("An estimator whose values, on average over repeated random samples, neither underestimate nor overestimate the parameter",
             "An estimator is unbiased if on average the value of the estimator does not underestimate or overestimate the parameter."),
          [ch("An estimator that gives exactly the value of the population parameter whenever it is calculated from any random sample of the population",
              "An unbiased estimator varies from sample to sample. Only its average is right."),
           ch("An estimator that is calculated from a sample that is larger than 10% of the population from which the sample was selected",
              "The size of the sample compared with the population is not what makes an estimator unbiased."),
           ch("An estimator whose values are always less than the value of the population parameter that it is used to estimate from the sample",
              "That describes an estimator that underestimates, which is biased.")],
          "An unbiased estimator is correct on average over many random samples.", difficulty="easy")

    B.mcq(T, "A statistician takes many random samples of size 50 from a population in which the proportion is 0.30. The mean of all of the sample proportions is 0.301. Which of the following is the best conclusion?",
          ch("The sample proportion appears to be an unbiased estimator of the population proportion, because its mean is very close to 0.30",
             "The center of the distribution of the sample proportions is the population proportion, so the estimator does not under- or overestimate on average."),
          [ch("The sample proportion is a biased estimator, because the mean of the sample proportions in the simulation is not exactly equal to 0.30",
              "A simulation gives a mean that is close to, but not exactly, the center, because of chance."),
           ch("The sample proportion is a biased estimator that overestimates the population proportion, because the mean of 0.301 is greater than 0.30",
              "The difference of 0.001 is small enough to be explained by chance in a simulation."),
           ch("The sample proportion is an unbiased estimator, because every sample proportion in the simulation of random samples is exactly equal to 0.30",
              "The sample proportions vary from sample to sample. It is their mean that is close to 0.30.")],
          "The mean of the sampling distribution is about the parameter, so p-hat is unbiased.", difficulty="medium")

    B.mcq(T, "The values of a statistic from many random samples have a distribution that is centered at 0.35, but the value of the population parameter that it is used to estimate is 0.30. Which of the following is correct?",
          ch("The statistic is a biased estimator that, on average, overestimates the parameter", "The center of its distribution is greater than the parameter, so it overestimates on average."),
          [ch("The statistic is an unbiased estimator, because the values of the statistic from different samples are different",
              "Variation from sample to sample does not make an estimator biased. The center matters."),
           ch("The statistic is a biased estimator that, on average, underestimates the parameter", "The center, 0.35, is greater than the parameter, 0.30, so it overestimates."),
           ch("The statistic is an unbiased estimator, because its center is close to the parameter", "A difference of 0.05 in the center means that the estimator is biased.")],
          "A statistic with a center above the parameter overestimates on average: it is biased.", difficulty="medium")

    B.mcq(T, "Which symbol is used for the point estimator of the population proportion p?",
          ch("The sample proportion, p̂", "The sample proportion p-hat is the point estimator for the population proportion p."),
          [ch("The sample mean, x̄", "The sample mean is the point estimator for a population mean."),
           ch("The population proportion, p", "The parameter p is what is estimated, not the estimator."),
           ch("The sample standard deviation, s", "The sample standard deviation estimates a population standard deviation.")],
          "p-hat is the point estimator of p.", difficulty="easy")

    B.mcq(T, "A researcher says, \"My estimator is unbiased, so the value that I calculated from my random sample must be equal to the population parameter.\" Which of the following is the best response?",
          ch("The statement is incorrect: an unbiased estimator is right on average, but the value from a single sample usually differs from the parameter",
             "Unbiased describes the center of the sampling distribution, not each value."),
          [ch("The statement is correct, because an unbiased estimator never differs from the parameter for a random sample",
              "Values of an unbiased estimator vary from sample to sample."),
           ch("The statement is correct, because the sample was random, so the value of the estimator is guaranteed to be right and equal to the value of the parameter",
              "Random selection removes bias but does not make a single estimate exact."),
           ch("The statement is incorrect, because an estimator that is unbiased cannot be calculated from a random sample",
              "Unbiased estimators are calculated from random samples.")],
          "Unbiased: correct on average. One sample's estimate has sampling variability.", difficulty="hard")

    # ------------------------------------------------------------------------------------------------------------ 3.2
    T = 2
    p, n = 0.30, 100
    sd_ = math.sqrt(p * (1 - p) / n)
    B.mcq(T, "In a large population, the proportion of adults who have a pet is p = 0.30. Random samples of size 100 are selected. What are the mean and the standard deviation of the sampling distribution of the sample proportion p̂?",
          ch(f"The mean is 0.30 and the standard deviation is {f4(sd_)}", "μ = p = 0.30 and σ = √(p(1 - p) / n) = √(0.30(0.70) / 100)."),
          [ch(f"The mean is 0.30 and the standard deviation is {f4(p * (1 - p) / n)}", "The value 0.0021 is the variance, p(1 - p) / n. The standard deviation is its square root."),
           ch(f"The mean is 30 and the standard deviation is {f4(math.sqrt(100 * p * (1 - p)))}", "These are the mean and standard deviation of the count of adults with a pet, np and the square root of np(1 - p), not of the proportion."),
           ch(f"The mean is 0.30 and the standard deviation is {f4(math.sqrt(p * (1 - p)))}", "This is √(p(1 - p)), which leaves out the division by the sample size.")],
          f"μ = 0.30 and σ = √(0.30(0.70) / 100) = {f4(sd_)}.", difficulty="easy")

    B.mcq(T, "A school has 1,500 students. A researcher plans to select a random sample of 200 students without replacement, to estimate the proportion of the students who walk to school. Which of the following is correct about the 10% condition?",
          ch("The condition is not met, because the sample size of 200 is more than 10% of the population size of 1,500", "The 10% condition requires n ≤ N / 10 = 150."),
          [ch("The condition is met, because the sample was selected at random from the students at the school, and a random sample always meets it", "Random selection is the randomization condition. The 10% condition is about the size of the sample."),
           ch("The condition is met, because the sample size of 200 is greater than 30", "A sample size above 30 does not satisfy the 10% condition."),
           ch("The condition is not met, because a sample of students must be selected with replacement", "The 10% condition is for samples taken without replacement. Replacement is not required.")],
          "n = 200 is greater than 10% of 1,500, which is 150.", difficulty="medium")

    B.mcq(T, "Random samples of size 40 are selected from a very large population in which the proportion of successes is p = 0.10. Is the sampling distribution of the sample proportion p̂ approximately normal?",
          ch("No, because np = 40(0.10) = 4 is less than 10", "The expected number of successes should be at least 10 (and the expected number of failures should be at least 10)."),
          [ch("Yes, because the sample size 40 is greater than 30", "For a sample proportion, the condition uses np and n(1 - p), not just the sample size."),
           ch("Yes, because n(1 - p) = 40(0.90) = 36 is greater than 10", "Both np and n(1 - p) must be at least 10, and np = 4."),
           ch("No, because the population is very large, which is not allowed in the conditions", "A large population is not a problem. The problem is the expected number of successes.")],
          "np = 4 < 10, so the normal approximation is not appropriate.", difficulty="medium")

    p2, n2 = 0.60, 150
    sd2 = math.sqrt(p2 * (1 - p2) / n2)
    z2 = (0.65 - p2) / sd2
    pr = float(sps.norm.sf(z2))
    B.mcq(T, "In a large population, the proportion of voters who support a measure is 0.60. A random sample of 150 voters is selected. What is the approximate probability that the sample proportion who support the measure is greater than 0.65?",
          ch(f3(pr), f"The sampling distribution is approximately normal with mean 0.60 and standard deviation {f4(sd2)}. z = (0.65 - 0.60) / {f4(sd2)} = {z2:.2f}."),
          [ch(f3(sps.norm.cdf(z2)), "This is the probability that the sample proportion is less than 0.65, the complement."),
           ch(f3(sps.norm.sf((0.65 - p2) / math.sqrt(p2 * (1 - p2)))), "This divides by √(p(1 - p)) and leaves out the sample size, which gives a standard deviation that is too large."),
           ch("0.500", "This is the probability that the sample proportion is greater than the mean, 0.60.")],
          f"P(p̂ > 0.65) = P(z > {z2:.2f}), about {f3(pr)}.", difficulty="hard")

    B.mcq(T, "The standard deviation of the sampling distribution of the sample proportion of adults with a pet, for random samples of size 100, is 0.0458. Which of the following is the correct interpretation of this value?",
          ch("In random samples of 100 adults, the sample proportion typically varies from the population proportion by about 0.0458",
             "The standard deviation of a sampling distribution quantifies the typical amount that the statistic varies from the parameter."),
          [ch("In every random sample of 100 adults, the sample proportion is within 0.0458 of the population proportion of adults who have a pet",
              "Some sample proportions are farther away. The standard deviation is a typical distance."),
           ch("The population proportion of adults with a pet is 0.0458",
              "The standard deviation of the sampling distribution is not the population proportion."),
           ch("About 4.58% of the adults in each random sample of 100 have a pet",
              "That would be a sample proportion. The standard deviation describes how the sample proportions vary.")],
          "The standard deviation of p-hat is the typical distance of p-hat from p in repeated samples.", difficulty="medium")

    s100 = math.sqrt(0.3 * 0.7 / 100)
    s400 = math.sqrt(0.3 * 0.7 / 400)
    assert abs(s400 * 2 - s100) < 1e-12
    B.mcq(T, "Random samples are selected from a large population with proportion p. The sample size is increased from 100 to 400. What happens to the standard deviation of the sampling distribution of the sample proportion?",
          ch("It is divided by 2, because the standard deviation includes √n and √400 is 2 times √100", "The sample size is multiplied by 4, so the standard deviation is multiplied by 1/2."),
          [ch("It is divided by 4, because the sample size is multiplied by 4", "The standard deviation involves the square root of n, so it is divided by 2 and not by 4."),
           ch("It is multiplied by 2, because a larger sample varies more from sample to sample", "A larger sample varies less from sample to sample."),
           ch("It does not change, because the population proportion p stays the same when the sample size changes", "The sample size is in the formula, so the standard deviation changes.")],
          "σ is proportional to 1 / √n: quadrupling n halves σ.", difficulty="medium")

    B.mcq(T, "A researcher wants to use the sampling distribution of a sample proportion. The researcher selects the first 60 people who walk into a store. Which condition for the sampling distribution is most clearly violated?",
          ch("The randomization condition, because the people who walk in first were not selected by a random method", "The data should be collected using a random sample."),
          [ch("The 10% condition, because 60 people is more than 10% of the population of all of the customers who might walk in", "Nothing says the sample is more than 10% of the population. The problem is how it was selected."),
           ch("The condition that the sample size must be greater than 30, because 60 is too small a sample", "60 is not less than 30. The issue is the method of selection."),
           ch("The condition that p must be 0.5, because the people who walk in are of two types", "There is no condition that p = 0.5.")],
          "A convenience sample is not random: the randomization condition is violated.", difficulty="medium")

    B.mcq(T, "The sampling distribution of the sample proportion p̂ for random samples of size 80 has mean 0.40. What is the probability that p̂ is less than 0.40, assuming that the distribution is approximately normal?",
          ch("0.50", "The distribution is approximately normal and symmetric about its mean, 0.40, so half of the values are less than 0.40."),
          [ch("0.40", "This is the mean of the distribution, not a probability."),
           ch("0.68", "This is the probability that p-hat is within 1 standard deviation of the mean."),
           ch("0.05", "A probability of 0.05 would be for a value 1.645 standard deviations below the mean, not for the mean itself.")],
          "By symmetry about the mean, P(p-hat < 0.40) = 0.50.", difficulty="medium")

    q1 = sps.norm.cdf((0.34 - 0.30) / math.sqrt(0.3 * 0.7 / 200)) - sps.norm.cdf((0.26 - 0.30) / math.sqrt(0.3 * 0.7 / 200))
    B.mcq(T, "In a large population, p = 0.30. A random sample of 200 is selected. Which of the following is the approximate probability that the sample proportion is between 0.26 and 0.34?",
          ch(f3(q1), "σ = √(0.30(0.70) / 200) = 0.0324, so the boundaries are z = ±1.23, and the area between them is about 0.78."),
          [ch("0.680", "This is the area within 1 standard deviation. The boundaries here are about 1.23 standard deviations from the mean."),
           ch("0.950", "This is the area within 2 standard deviations. The boundaries here are about 1.23 standard deviations from the mean."),
           ch(f3(sps.norm.cdf(1.23)), "This is the area to the left of z = 1.23. It includes the area below 0.26.")],
          f"P(0.26 < p-hat < 0.34) is about {f3(q1)}.", difficulty="hard")

    # ------------------------------------------------------------------------------------------------------------ 3.3
    T = 3
    B.mcq(T, "A researcher selects a random sample of 400 students from a large school and finds the proportion of the students in the sample who own a bicycle. The researcher wants to estimate the proportion of all students at the school who own a bicycle. Which procedure is appropriate?",
          ch("A one-sample z-interval for a population proportion", "The parameter is a single population proportion, estimated from one random sample."),
          [ch("A two-sample z-interval for a difference between population proportions", "There is only one sample and one population, so there is no difference between two proportions."),
           ch("A chi-square test for independence", "A chi-square test is for categorical variables in a two-way table, not for an interval estimate of one proportion."),
           ch("A one-sample z-test for a population proportion", "A test answers a question about whether the proportion differs from a specified value. The goal here is to estimate it.")],
          "The goal is to estimate one population proportion: a one-sample z-interval.", difficulty="easy")

    B.mcq(T, "A random sample of 400 students from a large school is selected, and the proportion who own a bicycle is used to construct a confidence interval. Which of the following correctly states the parameter?",
          ch("p = the proportion of all students at the school who own a bicycle", "The parameter references the proportion, the response variable and the population in context."),
          [ch("p̂ = the proportion of the 400 students in the sample who own a bicycle", "This is the sample proportion, a statistic, and not the parameter."),
           ch("p = the number of students in the sample at the school who own a bicycle", "A proportion is not a count."),
           ch("p = the proportion of the 400 students in the sample who do not own a bicycle", "The parameter is about the population, and about owning a bicycle.")],
          "The parameter is the proportion of all students at the school who own a bicycle.", difficulty="easy")

    B.mcq(T, "Which of the following lists the conditions that must be verified for a one-sample z-interval for a population proportion?",
          ch("The sample is random; the sample size is at most 10% of the population; and the observed numbers of successes and failures are each at least 10",
             "These are the randomization, 10% and normality conditions."),
          [ch("The sample is random; the sample size is at least 10% of the population; and the number of successes and failures in the sample are each at least 5",
              "The sample size should be at most 10% of the population, and the counts should be at least 10."),
           ch("The sample is random; the population is approximately normal in shape; and the sample size is greater than 30, so the counts do not matter",
              "For a proportion, the condition is on the counts of successes and failures, not on a normal population."),
           ch("The two samples are independent; the sample sizes are at most 10% of the populations; and the expected counts are each greater than 5",
              "Those are for other procedures. A one-sample interval has a single sample.")],
          "Randomization, 10% condition, and at least 10 observed successes and failures.", difficulty="medium")

    x, nn = 180, 400
    ci = prop_ci(x, nn, 0.95)
    B.mcq(T, "In a random sample of 400 students from a large school, 180 own a bicycle. Which of the following is a 95% confidence interval for the proportion of all students at the school who own a bicycle?",
          ch(f"({f3(ci.lo)}, {f3(ci.hi)})", f"p̂ = 0.45 and the margin of error is 1.96√(0.45(0.55) / 400) = {f3(ci.moe)}."),
          [ch(f"({f3(ci.phat - 1.645 * ci.se)}, {f3(ci.phat + 1.645 * ci.se)})", "This uses $z^*$ = 1.645, which is for a 90% confidence level."),
           ch(f"({f3(ci.phat - 1.96 * math.sqrt(0.45 * 0.55))}, {f3(ci.phat + 1.96 * math.sqrt(0.45 * 0.55))})", "This leaves out the division by the sample size in the standard error."),
           ch(f"({f3(ci.phat - 1.96 * ci.se ** 2)}, {f3(ci.phat + 1.96 * ci.se ** 2)})", "This uses the variance of the sample proportion instead of the standard error.")],
          f"p-hat ± $z^*$√(p-hat(1 - p-hat) / n) = 0.45 ± {f3(ci.moe)}, which is ({f3(ci.lo)}, {f3(ci.hi)}).", difficulty="medium")

    B.mcq(T, "Which of the following is the critical value $z^*$ for a 99% confidence interval for a population proportion?",
          ch("2.576", "The middle 99% of the standard normal distribution lies between -2.576 and 2.576."),
          [ch("1.960", "This is the critical value for a 95% confidence level."),
           ch("1.645", "This is the critical value for a 90% confidence level."),
           ch("2.326", "This is the z-score with 1% of the area above it, which is for a 98% confidence level.")],
          "$z^*$ = 2.576 for 99% confidence.", difficulty="easy")

    se1 = math.sqrt(0.45 * 0.55 / 400)
    B.mcq(T, "In a random sample of 400 students, the sample proportion who own a bicycle is 0.45. What is the standard error of the sample proportion?",
          ch(f4(se1), "SE = √(p-hat(1 - p-hat) / n) = √(0.45(0.55) / 400)."),
          [ch(f4(0.45 * 0.55 / 400), "This is p-hat(1 - p-hat) / n, the variance, before taking the square root."),
           ch(f4(math.sqrt(0.45 * 0.55)), "This leaves out the division by the sample size."),
           ch(f4(1.96 * se1), "This is the margin of error for a 95% confidence level, not the standard error.")],
          f"SE = {f4(se1)}.", difficulty="medium")

    zc = 1.96
    moe_t = 0.03
    nmin = zc ** 2 * 0.5 * 0.5 / moe_t ** 2
    ntrue = math.ceil(nmin)
    B.mcq(T, "A researcher wants to estimate a population proportion with a 95% confidence level and a margin of error of no more than 0.03. There is no prior estimate of the proportion. What is the minimum sample size needed?",
          ch(f"{ntrue:,}", f"Use p-hat = 0.5 for the upper bound: n = (1.96 / 0.03)²(0.5)(0.5) = {nmin:.1f}, so the sample size is {ntrue:,}."),
          [ch(f"{math.ceil(zc ** 2 * 0.25 / 0.03):,}", "This divides by the margin of error instead of by its square."),
           ch(f"{math.ceil(nmin / 4):,}", "This is one-fourth of the correct sample size, which comes from leaving out the factor of 4 in 1 / 0.5²."),
           ch(f"{math.floor(nmin):,}", "The sample size must be rounded up to the next whole number, so that the margin of error is no more than 0.03.")],
          f"n ≥ ($z^*$ / MOE)² p-hat(1 - p-hat) = {nmin:.1f}, so use {ntrue:,}.", difficulty="hard")

    B.mcq(T, "In a random sample of 80 adults from a large city, 6 say that they own a motorcycle. A student wants to construct a one-sample z-interval for the proportion of all adults in the city who own a motorcycle. Which of the following is correct?",
          ch("The normality condition is not met, because the observed number of successes, 6, is less than 10", "The number of observed successes and the number of observed failures must each be at least 10."),
          [ch("All conditions are met, because the sample is random and the sample size is greater than 30", "The normality condition uses the counts of successes and failures, and 6 is less than 10."),
           ch("The randomization condition is not met, because only 6 of the 80 adults in the sample own a motorcycle", "The number of adults who own a motorcycle does not decide whether the sample was selected at random."),
           ch("The 10% condition is not met, because 80 is greater than 6", "The 10% condition compares the sample size with the population size.")],
          "n p-hat = 6 < 10, so the normality condition fails.", difficulty="medium")

    B.mcq(T, "Which of the following is a correct statement of the margin of error for a one-sample z-interval for a population proportion?",
          ch("It is half the width of the interval, and equals the critical value $z^*$ times the standard error of the sample proportion",
             "The margin of error is $z^*$√(p-hat(1 - p-hat) / n)."),
          [ch("It is the width of the interval, and equals the critical value $z^*$ divided by the standard error of the sample proportion",
              "The margin of error is half the width, and it is a product with the standard error."),
           ch("It is the standard error of the sample proportion, and equals the sample proportion divided by the square root of n",
              "The standard error is not the margin of error. The margin of error is $z^*$ times the standard error."),
           ch("It is half the width of the interval, and equals the sample proportion times the critical value $z^*$",
              "The margin of error multiplies $z^*$ by the standard error, not by the sample proportion.")],
          "MOE = $z^*$ × SE, half the width of the interval.", difficulty="medium")

    # ------------------------------------------------------------------------------------------------------------ 3.4
    T = 4
    B.mcq(T, f"A 95% confidence interval for the proportion of all students at a school who own a bicycle is ({f3(ci.lo)}, {f3(ci.hi)}). Which of the following is a correct interpretation?",
          ch(f"We are 95% confident that the interval from {f3(ci.lo)} to {f3(ci.hi)} contains the proportion of all students at the school who own a bicycle", "An interpretation references the parameter, the population and the context."),
          [ch(f"There is a 95% probability that the proportion of the students in the sample who own a bicycle is between {f3(ci.lo)} and {f3(ci.hi)}", "The sample proportion, 0.45, is known. The interval is about the population proportion."),
           ch(f"About 95% of the students at the school own a bicycle, because the interval is between {f3(ci.lo)} and {f3(ci.hi)}", "The interval estimates a proportion. It does not say that 95% of the students own a bicycle."),
           ch(f"95% of all of the sample proportions from random samples of 400 students are between {f3(ci.lo)} and {f3(ci.hi)}", "The interval is not a range for the sample proportions of other samples.")],
          "Interpret the interval as a statement of confidence about the population proportion.", difficulty="medium")

    B.mcq(T, "Which of the following is the correct interpretation of a 95% confidence level for a population proportion?",
          ch("In repeated random sampling with the same sample size, about 95% of the intervals calculated will capture the population proportion",
             "The confidence level describes the long-run success rate of the method."),
          [ch("There is a 95% probability that the population proportion is in the one interval that was calculated from the sample that was selected",
              "The population proportion is a fixed value. The interval from one sample either contains it or does not."),
           ch("In any one random sample, 95% of the values are within the interval that was calculated from the sample",
              "The interval is for the population proportion, not for the individual values."),
           ch("In repeated random sampling, approximately 95% of the sample proportions are equal to the population proportion",
              "Most sample proportions differ from the population proportion.")],
          "A 95% confidence level means that about 95% of the intervals from repeated random samples capture the parameter.", difficulty="medium")

    B.mcq(T, "A random sample of 500 adults is used to construct a 95% confidence interval for the proportion of all adults in a city who support a tax. The interval is (0.36, 0.44). A mayor claims that the proportion of all adults in the city who support the tax is 0.50. Which of the following is the best conclusion?",
          ch("The interval provides convincing evidence that the proportion is not 0.50, because 0.50 is not in the interval of plausible values", "Values outside the interval are not plausible values for the proportion."),
          [ch("The interval provides convincing evidence that the proportion is 0.50, because 0.50 is close to the interval", "A value outside the interval is not plausible, however close it is."),
           ch("The interval does not provide any evidence about the claim, because a confidence interval cannot be used to evaluate a claim", "An interval gives plausible values and can support a claim."),
           ch("The interval provides convincing evidence that the proportion is 0.40, because 0.40 is the center of the interval that was calculated", "The interval gives a range of plausible values. It does not prove a single value.")],
          "0.50 is not in (0.36, 0.44), so it is not a plausible value for the proportion.", difficulty="medium")

    B.mcq(T, "A 95% confidence interval for the proportion of all registered voters in a state who support a measure is (0.46, 0.54). Which of the following claims is supported by the interval?",
          ch("There is not convincing evidence that a majority of the voters support the measure, because 0.50 is in the interval", "Plausible values include proportions below 0.50, so the interval does not support a claim of a majority."),
          [ch("There is convincing evidence that a majority of the voters support the measure, because the center of the interval is 0.50", "The center is 0.50, but the interval includes values less than 0.50."),
           ch("There is convincing evidence that fewer than half of the voters support the measure, because the interval has values below 0.50", "The interval also has values above 0.50, so neither claim is supported."),
           ch("There is convincing evidence that exactly 50% of the voters support the measure, because 0.50 is in the interval of plausible values", "An interval gives a range of plausible values, not a proof of one value.")],
          "0.50 is a plausible value, so the interval does not show a majority.", difficulty="medium")

    B.mcq(T, "A student constructs a 90% confidence interval and a 99% confidence interval for a population proportion, using the same random sample. Which of the following is true?",
          ch("The 99% interval is wider, because a greater confidence level has a greater critical value and a greater margin of error", "$z^*$ is 2.576 for 99% and 1.645 for 90%."),
          [ch("The 90% interval is wider, because it is less likely to contain the parameter", "A lower confidence level gives a narrower interval."),
           ch("The two intervals have the same width, because they are calculated from the same sample and the same sample size", "The critical values differ, so the margins of error differ."),
           ch("The 99% interval is narrower, because it is more likely to contain the parameter", "To be more confident, the interval must be wider.")],
          "For the same sample, a higher confidence level gives a larger critical value and a wider interval.", difficulty="easy")

    w100 = 2 * 1.96 * math.sqrt(0.5 * 0.5 / 100)
    w400 = 2 * 1.96 * math.sqrt(0.5 * 0.5 / 400)
    assert abs(w100 - 2 * w400) < 1e-12
    B.mcq(T, "A 95% confidence interval for a population proportion, based on a random sample of 100, has a width of about 0.196. About what would the width be for a random sample of 400, with the same sample proportion and the same confidence level?",
          ch("0.098, because the width is approximately proportional to 1 / √n, and √400 is 2 times √100", "Quadrupling the sample size halves the width."),
          [ch("0.049, because the width is divided by 4 when the sample size is multiplied by 4", "The width is proportional to 1 / √n, so it is divided by 2, not by 4."),
           ch("0.196, because the confidence level and the sample proportion did not change when the sample size changed", "The sample size is in the standard error, so the width changes."),
           ch("0.392, because a larger sample gives a larger margin of error", "A larger sample gives a smaller margin of error.")],
          "Width is about proportional to 1 / √n: 0.196 / 2 = 0.098.", difficulty="medium")

    B.mcq(T, "Two intervals are calculated from the same random sample: one for a 95% confidence level and one for a 90% confidence level. The sample proportion is 0.40 and the sample size is 300. A student says that the 90% interval gives a more precise estimate and is therefore better. Which of the following is the best response?",
          ch("The 90% interval is narrower, but the method that produced it captures the parameter less often (about 90% of the time)", "There is a trade-off between the width of the interval and the confidence level."),
          [ch("The 90% interval is narrower and captures the parameter more often, so it is better in every way for estimating the proportion", "A lower confidence level captures the parameter less often."),
           ch("The 90% interval is wider but more precise, because it uses a smaller critical value", "A smaller critical value gives a narrower interval, not a wider one."),
           ch("The two intervals are equally good, because they are calculated from the same random sample", "The two have different widths and different confidence levels.")],
          "A narrower interval comes with a lower confidence level.", difficulty="hard")

    B.mcq(T, "A 95% confidence interval for the proportion of all households in a city that recycle is (0.58, 0.66). A city official claims that more than half of the households recycle. Does the interval provide convincing evidence for the claim?",
          ch("Yes, because all of the plausible values in the interval are greater than 0.50", "The interval (0.58, 0.66) does not contain 0.50 or any value less than 0.50."),
          [ch("No, because the interval contains values that are less than its upper limit of 0.66", "Values within the interval being less than its upper limit is always true and does not argue against the claim."),
           ch("No, because a confidence interval can only be used for a claim about a difference between two proportions", "An interval for a single proportion can support a claim about that proportion."),
           ch("Yes, because the sample proportion, 0.62, is more than 0.50 in the sample of households", "The sample proportion is above 0.50, but it is the interval that shows convincing evidence about the population.")],
          "Every plausible value is above 0.50, so the interval supports the claim.", difficulty="medium")
