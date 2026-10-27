"""Unit 4, topics 4.1 to 4.3.

Required content (CED effective Fall 2026): 4.1 for independent values the sampling distribution of x-bar has mean mu and standard deviation sigma / sqrt(n); conditions: random sample, 10% condition; the shape is normal for any n when the population is
normal, approximately normal when n >= 30 otherwise (a much larger n if the population is extremely skewed); interpret in context. 4.2 t-distributions: symmetric, bell-shaped, wider tails than the standard normal, identified by the degrees of freedom, closer to
normal as df grows; used when sigma is unknown; the one-sample t-interval for a mean, and for a mean difference in a matched pairs design (one sample of differences, state the order of subtraction); conditions: random sample or randomized experiment, 10%, the
sample data condition (population approximately normal, or n >= 30, or n < 30 with data free of strong skewness and outliers); x-bar +- t* s / sqrt(n) with df = n - 1; SE = s / sqrt(n); margin of error = t* SE. 4.3 interpret the interval and confidence level, justify a
claim with the interval, how the width changes with the confidence level and n (about 1 / sqrt(n)). Skills 2.C, 2.D, 3.D, 3.E, 4.C, 4.D, 4.E, 4.F, 4.G.
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
    # ------------------------------------------------------------------------------------------------------------ 4.1
    T = 1
    mu, sg, n = 50, 12, 36
    se = sg / math.sqrt(n)
    B.mcq(T, "A population of delivery times has a mean of 50 minutes and a standard deviation of 12 minutes. Random samples of size 36 are selected. What are the mean and the standard deviation of the sampling distribution of the sample mean $\\bar{x}$?",
          ch(f"The mean is 50 minutes and the standard deviation is {f2(se)} minutes", "μ̄ = μ = 50 and σ = σ / √n = 12 / √36 = 2."),
          [ch("The mean is 50 minutes and the standard deviation is 12 minutes", "The standard deviation of 12 is for the individual delivery times. The sample mean varies less."),
           ch(f"The mean is 50 minutes and the standard deviation is {f2(sg / n)} minutes", "This divides σ by n instead of by √n."),
           ch(f"The mean is 50 minutes and the standard deviation is {f2(sg ** 2 / n)} minutes", "This is σ² / n, which is the variance of $\\bar{x}$, not its standard deviation.")],
          "μ = 50 and σ = 12 / √36 = 2 minutes.", difficulty="easy")

    B.mcq(T, "The weights of the apples from an orchard are approximately normally distributed. A random sample of only 8 apples is selected from the very large number of apples in the orchard. Is it appropriate to use a normal distribution to model the sampling distribution of the sample mean weight?",
          ch("Yes, because the population is approximately normal, so the sampling distribution of the sample mean is normal for any n", "When the population is normal, the sample mean is normally distributed regardless of n."),
          [ch("No, because the sample size, 8, is less than 30", "The sample size of 30 is needed only when the population is not normal."),
           ch("No, because the sampling distribution of a sample mean is never normal, whatever the shape of the population or the sample size is", "It is normal when the population is normal, and approximately normal for large samples from other populations."),
           ch("Yes, because the sample size is less than 10% of the population", "The 10% condition is a separate condition. The shape comes from the normal population.")],
          "A normal population gives a normal sampling distribution of $\\bar{x}$ for any n.", difficulty="medium")

    B.mcq(T, "The amounts of time, in minutes, that customers wait at a clinic have a distribution that is strongly skewed to the right. A random sample of 15 customers is selected from a very large number of customers. Is it appropriate to use a normal distribution to model the sampling distribution of the sample mean?",
          ch("No, because the population is not normal and the sample size, 15, is less than 30", "For a population that is not normal, the sample size should be at least 30."),
          [ch("Yes, because the sample is random and 15 is less than 10% of the customers", "The randomization and 10% conditions do not decide the shape."),
           ch("Yes, because every sampling distribution is approximately normal", "A sampling distribution is approximately normal only under conditions on the population or the sample size."),
           ch("No, because a random sample of customers cannot be used to find a sample mean of the times", "A random sample is what makes a sample mean usable. The problem is the shape.")],
          "A skewed population and n < 30: the normal model is not appropriate.", difficulty="medium")

    pm = sps.norm.sf(105, 100, 20 / math.sqrt(64))
    pi_ = sps.norm.sf(105, 100, 20)
    B.mcq(T, "The scores on a test are approximately normally distributed with a mean of 100 and a standard deviation of 20. A random sample of 64 scores is selected. What is the probability that the sample mean is greater than 105?",
          ch(f3(pm), "The sampling distribution of $\\bar{x}$ has mean 100 and standard deviation 20 / √64 = 2.5. z = (105 - 100) / 2.5 = 2.0."),
          [ch(f3(pi_), "This uses the standard deviation of individual scores, 20, which is the probability that one score is greater than 105."),
           ch(f3(1 - pm), "This is the probability that the sample mean is less than 105."),
           ch(f3(sps.norm.sf(105, 100, 20 / 64)), "This divides the standard deviation by n instead of by √n.")],
          f"P($\\bar{{x}}$ > 105) = P(z > 2.0), about {f3(pm)}.", difficulty="medium")

    B.mcq(T, "The standard deviation of the sampling distribution of the sample mean time, for random samples of 64 customers, is 2.5 minutes. Which of the following is the correct interpretation of this value?",
          ch("In random samples of 64 customers, the sample mean time typically varies from the population mean by about 2.5 minutes", "The standard deviation of a sampling distribution is the typical amount that the statistic varies from the parameter."),
          [ch("The time of a typical customer varies from the mean time of all customers by about 2.5 minutes in a random sample of 64", "That would describe the standard deviation of individual times, not of the sample mean."),
           ch("The mean time of the 64 customers in each sample is exactly 2.5 minutes", "The sample mean varies from sample to sample. 2.5 is a measure of how much."),
           ch("Every sample mean time is within 2.5 minutes of the population mean time", "Some sample means are farther away. The standard deviation is a typical distance.")],
          "The standard deviation of $\\bar{x}$ is the typical distance of $\\bar{x}$ from μ in repeated samples.", difficulty="medium")

    B.mcq(T, "Random samples are selected from a large population. The sample size is increased from 50 to 200. What happens to the standard deviation of the sampling distribution of the sample mean?",
          ch("It is divided by 2", "σ / √n: √200 is 2 times √50, so the standard deviation is divided by 2."),
          [ch("It is divided by 4", "The standard deviation involves √n, so quadrupling n divides it by 2, not by 4."),
           ch("It is multiplied by 2", "A larger sample gives less variability in the sample mean."),
           ch("It does not change", "The sample size is in the formula, so the standard deviation changes.")],
          "Quadrupling n divides σ / √n by 2.", difficulty="easy")

    B.mcq(T, "A district has 900 teachers. A researcher plans to select a simple random sample of 120 teachers without replacement, and to use the sampling distribution of the sample mean salary. Which of the following is correct?",
          ch("The 10% condition is not met, because the sample size of 120 is more than 10% of the 900 teachers", "n ≤ N / 10 = 90 is needed."),
          [ch("The randomization condition is not met, because the teachers were selected without replacement from the list", "Selecting without replacement is allowed. The 10% condition handles it."),
           ch("The 10% condition is met, because the sample size of 120 is greater than 30", "The 10% condition compares the sample size with the population size."),
           ch("Both conditions are met, because the sample was selected at random", "The sample is random, but 120 is more than 10% of 900.")],
          "120 > 90 = 10% of 900: the 10% condition fails.", difficulty="medium")

    B.mcq(T, "The populations of household incomes in a city is extremely skewed to the right. A random sample of 35 households is selected from the very large number of households. Which of the following is the best statement about the sampling distribution of the sample mean income?",
          ch("It may still be noticeably skewed, because an extremely skewed population may need a sample size much larger than 30", "The rule n ≥ 30 is a guide, and extreme skewness needs a larger n."),
          [ch("It is exactly normal, because the sample size is at least 30", "It is approximately normal at best, and only for large enough n."),
           ch("It is skewed in the same way as the population, whatever the sample size", "The sampling distribution becomes more normal as n increases."),
           ch("It has the same standard deviation as the population, because the sample is random and large enough to represent the population", "The standard deviation of $\\bar{x}$ is σ / √n.")],
          "Extreme skewness: a sample size much larger than 30 may be needed.", difficulty="hard")

    p_ind = sps.norm.sf(75, 70, 10)
    p_mean = sps.norm.sf(75, 70, 10 / 5)
    B.mcq(T, f"The heights of the plants in a large field are approximately normally distributed with a mean of 70 cm and a standard deviation of 10 cm. The probability that one randomly selected plant is taller than 75 cm is {f3(p_ind)}. What is the probability that the mean height of a random sample of 25 plants is greater than 75 cm?",
          ch(f3(p_mean), "The sample mean has standard deviation 10 / √25 = 2, so z = (75 - 70) / 2 = 2.5, which is far in the tail."),
          [ch(f3(p_ind), "This is the probability for one plant. A sample mean varies less than one value."),
           ch(f3(p_ind / 5), "This divides the probability for one plant by 5, which is not how the standard deviation changes."),
           ch(f3(sps.norm.sf(75, 70, 10 / 25)), "This divides the standard deviation by n = 25 instead of by √25 = 5.")],
          f"P($\\bar{{x}}$ > 75) = P(z > 2.5), about {f3(p_mean)}, much less than P(X > 75).", difficulty="hard")

    # ------------------------------------------------------------------------------------------------------------ 4.2
    T = 2
    B.mcq(T, "Which of the following is true of a t-distribution, compared with the standard normal distribution?",
          ch("It is symmetric and bell-shaped, but with wider tails; it has a lower peak when its degrees of freedom are small", "t-distributions have fatter tails, especially for small degrees of freedom."),
          [ch("It is skewed to the right, with narrower tails than the standard normal distribution, for any degrees of freedom", "A t-distribution is symmetric."),
           ch("It is symmetric and bell-shaped, but with narrower tails and a higher peak", "The tails of a t-distribution are wider, not narrower."),
           ch("It is identical to the standard normal distribution for every sample size", "A t-distribution is close to the standard normal distribution only when the degrees of freedom are large.")],
          "A t-distribution has wider tails than the standard normal; it approaches the standard normal as df increases.", difficulty="medium")

    B.mcq(T, "A researcher selects a random sample of 22 batteries of one brand and records the lifetime of each, in hours. The researcher wants to estimate the mean lifetime of all batteries of this brand. The population standard deviation is unknown. Which procedure is appropriate?",
          ch("A one-sample t-interval for a population mean", "The parameter is one population mean and σ is unknown, so t is used."),
          [ch("A one-sample z-interval for a population proportion", "The variable is quantitative (hours), so the parameter is a mean, not a proportion."),
           ch("A two-sample t-interval for a difference between population means", "There is one sample and one population."),
           ch("A one-sample z-interval for a population mean, using the sample standard deviation as σ", "When σ is unknown, the sample standard deviation is used with the t-distribution.")],
          "One quantitative variable, one sample, σ unknown: a one-sample t-interval.", difficulty="easy")

    B.mcq(T, "A teacher gives the same 15 students a reading test before a tutoring program and another reading test after the program. The teacher wants to estimate the mean change in the scores, for students like these. Which procedure is appropriate?",
          ch("A one-sample t-interval for a population mean difference, using the differences (after - before) for the 15 students", "The scores are paired, so the analysis uses one sample of differences."),
          [ch("A two-sample t-interval for a difference between two population means, treating the before and after scores as independent samples", "The before and after scores are for the same students, so they are not independent."),
           ch("A two-sample z-interval for a difference between population proportions", "The scores are quantitative, not categories."),
           ch("A one-sample t-interval for the mean of the before scores only", "The question is about the change, which needs both scores.")],
          "A matched pairs design: take the differences and use a one-sample t-interval.", difficulty="medium")

    B.mcq(T, "Each of 15 students takes a reading test before a tutoring program and again after it. Let the difference for a student be the after score minus the before score. Which of the following correctly states the parameter for a confidence interval for the mean change?",
          ch("$\mu_d$ = the mean difference (after - before) in the reading test scores of all students like these", "The parameter references the population mean difference, the response variable, and the order of subtraction."),
          [ch("$\mu_d$ = the mean of the 15 differences in the reading test scores of the students in the sample who were tested", "That describes the sample mean difference, a statistic."),
           ch("$\mu_d$ = the mean reading test score of the students after the program", "This is the mean of the after scores, not the mean difference."),
           ch("$\mu_d$ = the mean difference in the reading test scores", "This does not state the order of subtraction or the population.")],
          "State the population mean difference with the order of subtraction.", difficulty="medium")

    data = [12, 14, 15, 15, 16, 17, 17, 18, 19, 20, 21, 52]
    dpl = dotplot(data, "Time to finish a puzzle (minutes)", axis=(10, 55, 5), alt="Dotplot of the times of 12 people to finish a puzzle: most are between 12 and 21 minutes, and one is 52 minutes.")
    B.mcq(T, "A random sample of 12 people from a very large group finishes a puzzle. The dotplot shows the times. A student wants to construct a one-sample t-interval for the mean time of all people in the group. Which of the following is correct about the sample data condition?",
          ch("The condition is not met, because the sample size is less than 30 and the data have a strong outlier", "For n < 30, the sample data should be free from strong skewness and outliers."),
          [ch("The condition is met, because the sample was selected at random", "Random selection is the randomization condition. The sample data condition is about the shape of the data."),
           ch("The condition is met, because the sample size is greater than 10", "A sample size of 10 or more is not the condition. For n < 30 the data must have no strong skewness or outliers."),
           ch("The condition is not met, because the data are not exactly normal", "The data need not be exactly normal, but they should be free from strong skewness and outliers.")],
          "n = 12 < 30 and there is a strong outlier: the sample data condition is not met.", diagram=dpl, difficulty="medium")

    ci = t_ci(48.2, 6.4, 25, 0.95)
    z195 = (48.2 - 1.96 * 6.4 / 5, 48.2 + 1.96 * 6.4 / 5)
    t_99 = t_ci(48.2, 6.4, 25, 0.99)
    B.mcq(T, "A random sample of 25 batteries has a mean lifetime of 48.2 hours and a standard deviation of 6.4 hours. The lifetimes are approximately normally distributed. Which of the following is a 95% confidence interval for the mean lifetime of all batteries of this brand?",
          ch(f"({f2(ci.lo)}, {f2(ci.hi)})", f"$\\bar{{x}}$ ± $t^*$ s / √n = 48.2 ± {f3(ci.t)}(6.4 / √25), with df = 24."),
          [ch(f"({f2(z195[0])}, {f2(z195[1])})", "This uses the critical value 1.96 from the standard normal distribution. With an unknown σ, use the t critical value."),
           ch(f"({f2(48.2 - ci.t * 6.4)}, {f2(48.2 + ci.t * 6.4)})", "This uses s in place of the standard error, s / √n."),
           ch(f"({f2(t_99.lo)}, {f2(t_99.hi)})", "This uses the critical value for a 99% confidence level, 2.797.")],
          f"48.2 ± {f3(ci.t)}(1.28) = ({f2(ci.lo)}, {f2(ci.hi)}).", difficulty="medium")

    B.mcq(T, "What is the critical value $t^*$ for a 95% confidence interval for a population mean, based on a random sample of size 15?",
          ch("2.145", "The degrees of freedom are n - 1 = 14, and the central 95% of the t-distribution with 14 degrees of freedom lies between -2.145 and 2.145."),
          [ch("1.960", "This is the critical value for a 95% confidence level from the standard normal distribution."),
           ch("2.131", "This is the critical value for 15 degrees of freedom. The degrees of freedom are n - 1 = 14."),
           ch("1.761", "This is the critical value for a 90% confidence level with 14 degrees of freedom.")],
          f"df = 14 and $t^*$ = {f3(tstar(0.95, 14))}.", difficulty="medium")

    ci2 = t_ci(33.4, 10.2, 36, 0.95)
    B.mcq(T, "A random sample of 36 students has a mean commute of 33.4 minutes and a standard deviation of 10.2 minutes. What are the standard error of the sample mean and the margin of error for a 95% confidence interval?",
          ch(f"The standard error is {f2(ci2.se)} minutes and the margin of error is {f2(ci2.moe)} minutes", f"SE = s / √n = 10.2 / 6 = 1.7, and the margin of error is $t^*$ × SE = {f3(ci2.t)}(1.7) with df = 35."),
          [ch(f"The standard error is 10.2 minutes and the margin of error is {f2(ci2.t * 10.2)} minutes", "The standard deviation is not the standard error. The standard error divides by √n."),
           ch(f"The standard error is {f2(10.2 / 36)} minutes and the margin of error is {f2(ci2.t * 10.2 / 36)} minutes", "This divides s by n instead of by √n."),
           ch(f"The standard error is {f2(ci2.se)} minutes and the margin of error is {f2(ci2.se)} minutes", "The margin of error is the critical value times the standard error, not the standard error.")],
          f"SE = 1.70 and the margin of error = {f3(ci2.t)}(1.7) = {f2(ci2.moe)} minutes.", difficulty="medium")

    cd = t_ci(2.5, 4.0, 16, 0.95)
    B.mcq(T, "Each of 16 students solves a set of problems with and without music. The difference for each student is the time without music minus the time with music. The mean of the 16 differences is 2.5 minutes and the standard deviation is 4.0 minutes. The differences have no strong skewness or outliers. Which of the following is a 95% confidence interval for the population mean difference?",
          ch(f"({f2(cd.lo)}, {f2(cd.hi)})", f"2.5 ± {f3(cd.t)}(4.0 / √16), with df = 15."),
          [ch(f"({f2(2.5 - 1.96)}, {f2(2.5 + 1.96)})", "This uses 1.96 and the standard deviation divided by 2, with the wrong critical value for df = 15."),
           ch(f"({f2(2.5 - cd.t * 4.0)}, {f2(2.5 + cd.t * 4.0)})", "This uses the standard deviation of the differences in place of the standard error."),
           ch(f"({f2(2.5 - tstar(0.95, 16) * 1.0)}, {f2(2.5 + tstar(0.95, 16) * 1.0)})", "This uses 16 degrees of freedom instead of 15.")],
          f"2.5 ± {f3(cd.t)}(1.0) = ({f2(cd.lo)}, {f2(cd.hi)}).", difficulty="hard")

    B.mcq(T, "A researcher records the mass of each of 10 pairs of identical twins, one twin raised in a city and the other in the country. The researcher wants to estimate the mean difference in the masses. Which of the following is the best analysis?",
          ch("A one-sample t-interval for a mean difference, using the 10 differences between the twins", "Each pair is dependent, so use the differences."),
          [ch("A two-sample t-interval, treating the 10 city twins and the 10 country twins as independent samples", "The twins in a pair are related, so the samples are not independent."),
           ch("A one-sample z-interval for a proportion, comparing the number of heavier twins", "The data are masses, a quantitative variable. The pairs allow a mean difference."),
           ch("A chi-square test for homogeneity, comparing city and country", "The response is quantitative, not categories in a two-way table.")],
          "Matched pairs: the analysis is based on the differences.", difficulty="medium")

    # ------------------------------------------------------------------------------------------------------------ 4.3
    T = 3
    B.mcq(T, f"A 95% confidence interval for the mean lifetime of all batteries of a brand is ({f2(ci.lo)}, {f2(ci.hi)}) hours. Which of the following is a correct interpretation?",
          ch(f"We are 95% confident that the interval from {f2(ci.lo)} to {f2(ci.hi)} hours contains the mean lifetime of all batteries of this brand", "An interpretation references the parameter, the population, and the context."),
          [ch(f"95% of all batteries of this brand have lifetimes between {f2(ci.lo)} and {f2(ci.hi)} hours", "The interval estimates the mean. It does not describe where 95% of the individual lifetimes are."),
           ch(f"There is a 95% probability that the mean lifetime of the 25 batteries in the sample is between {f2(ci.lo)} and {f2(ci.hi)} hours", "The sample mean, 48.2, is known. The interval is about the population mean."),
           ch(f"The mean lifetime of every battery of this brand is between {f2(ci.lo)} and {f2(ci.hi)} hours", "Individual lifetimes vary around the mean. The interval is for the population mean.")],
          "Interpret the interval as a statement of confidence about the population mean.", difficulty="medium")

    B.mcq(T, "Which of the following is the correct interpretation of a 95% confidence level for a population mean?",
          ch("In repeated random sampling with the same sample size, about 95% of the intervals created will capture the population mean", "The confidence level describes the long-run success rate of the method."),
          [ch("There is a 95% probability that the population mean is in the one interval that was created from the random sample that was selected", "The population mean is a fixed value. A particular interval either contains it or does not."),
           ch("In repeated random sampling, 95% of the sample means will be equal to the population mean", "Sample means vary, and most are not equal to the population mean."),
           ch("95% of the individual values in the population are within the interval", "The interval is for the mean, not for the individual values.")],
          "A 95% confidence level: about 95% of intervals from repeated random samples capture the mean.", difficulty="medium")

    B.mcq(T, f"A company claims that the mean lifetime of its batteries is 52 hours. A 95% confidence interval for the mean lifetime, from a random sample of batteries, is ({f2(ci.lo)}, {f2(ci.hi)}) hours. Which of the following is the best conclusion?",
          ch("The interval provides convincing evidence that the mean lifetime is not 52 hours, because 52 is not a plausible value", "Values outside the interval are not plausible values for the mean."),
          [ch("The interval provides convincing evidence that the mean lifetime is 52 hours, because 52 is close to the interval of plausible values", "A value outside the interval is not plausible, however close it is."),
           ch("The interval provides no information about the claim, because an interval cannot be used to evaluate a claim", "An interval gives plausible values and can support or contradict a claim."),
           ch("The interval provides convincing evidence that the mean lifetime is 48.2 hours, the center of the interval", "An interval gives a range of plausible values and does not prove a single value.")],
          "52 is not in (45.56, 50.84): not a plausible value for the mean.", difficulty="medium")

    ci3 = t_ci(51.0, 6.4, 25, 0.95)
    B.mcq(T, f"A 95% confidence interval for the mean lifetime of a brand of batteries is ({f2(ci3.lo)}, {f2(ci3.hi)}) hours. A manager claims that the mean lifetime is at least 50 hours. Which of the following is the best conclusion?",
          ch("The interval does not provide convincing evidence against the claim, because values of 50 hours or more are plausible and 50 is in the interval", "The interval includes 50 and values above it."),
          [ch("The interval provides convincing evidence against the claim, because part of the interval is below 50 hours", "A part of the interval being below 50 does not make the claim implausible, since 50 and higher values are also plausible."),
           ch("The interval proves that the mean lifetime is at least 50 hours", "An interval gives plausible values and cannot prove a claim."),
           ch("The interval provides convincing evidence for the claim, because the center of the interval is 51", "The center is 51, but the interval also includes values less than 50, so it is not convincing evidence that the mean is at least 50.")],
          "50 is in the interval, so a mean of at least 50 is plausible.", difficulty="hard")

    B.mcq(T, "Each of 20 workers has the time for a task recorded with an old tool and with a new tool. The difference for each worker is the time with the old tool minus the time with the new tool. A 95% confidence interval for the population mean difference is (-0.4, 3.2) minutes. Which of the following is the best conclusion?",
          ch("There is not convincing evidence of a difference in the mean times, because 0 is in the interval", "If the interval contains 0, there is not sufficient evidence of a difference."),
          [ch("There is convincing evidence that the new tool is faster, because most of the interval is positive", "The interval includes 0 and negative values, so a difference has not been shown."),
           ch("There is convincing evidence that the mean times are equal, because 0 is in the interval", "An interval that contains 0 does not prove that the means are equal."),
           ch("There is convincing evidence of a difference, because the interval is not centered at 0", "The question is whether 0 is a plausible value. It is in the interval.")],
          "0 is a plausible value for the mean difference.", difficulty="medium")

    B.mcq(T, "Each of 20 students takes a test before and after a review class. The difference for each student is the after score minus the before score. A 95% confidence interval for the population mean difference is (1.2, 4.8) points. Which of the following is the best conclusion?",
          ch("There is convincing evidence that the mean score after the review class is greater than the mean score before it, for students like these", "All plausible values of the mean difference (after - before) are positive."),
          [ch("There is convincing evidence that the mean score before the review class is greater than the mean score after it", "Positive values of (after - before) mean that the after scores are greater."),
           ch("There is not convincing evidence of a change, because the interval has a width of 3.6 points", "The width does not decide this. The interval does not contain 0."),
           ch("There is convincing evidence that every student scored between 1.2 and 4.8 points higher after the review class", "The interval is for the mean difference, not for each student.")],
          "The interval has only positive values: the mean difference (after - before) is positive.", difficulty="medium")

    B.mcq(T, "A student constructs a 90% confidence interval and a 99% confidence interval for a population mean, using the same random sample. Which of the following is true?",
          ch("The 99% interval is wider, because a greater confidence level has a greater critical value", "$t^*$ is greater for a greater confidence level."),
          [ch("The 90% interval is wider, because it is less likely to contain the mean", "A lower confidence level gives a narrower interval."),
           ch("The two intervals have the same width, because they use the same sample", "The critical values differ, so the margins of error differ."),
           ch("The 99% interval is narrower, because it is more likely to contain the mean of the population", "To be more confident, the interval must be wider.")],
          "For the same sample, higher confidence means a larger critical value and a wider interval.", difficulty="easy")

    w36 = 2 * tstar(0.95, 35) * 10.2 / 6
    w144 = 2 * tstar(0.95, 143) * 10.2 / 12
    B.mcq(T, f"A 95% confidence interval for a population mean, based on a random sample of 36 with a standard deviation of 10.2, has a width of about {f2(w36)}. About what would the width be for a random sample of 144, with the same standard deviation and confidence level?",
          ch(f"About {f2(w144)}, because the width is approximately proportional to 1 / √n and √144 is 2 times √36", "Quadrupling the sample size roughly halves the width."),
          [ch(f"About {f2(w36 / 4)}, because the width is divided by 4 when the sample size is multiplied by 4", "The width is proportional to 1 / √n, so it is divided by about 2."),
           ch(f"About {f2(w36)}, because the confidence level and the standard deviation did not change", "The sample size is in the standard error, so the width changes."),
           ch(f"About {f2(w36 * 2)}, because a larger sample gives a larger margin of error", "A larger sample gives a smaller margin of error.")],
          f"Width is about proportional to 1 / √n: {f2(w36)} / 2 is about {f2(w144)}.", difficulty="medium")

    B.mcq(T, "Two researchers each take a random sample from the same population and construct a 95% confidence interval for the population mean. Researcher 1 uses n = 25 with s = 8. Researcher 2 uses n = 100 with s = 8. Which of the following is correct?",
          ch("Researcher 2's interval is narrower, because the larger sample size gives a smaller standard error", "SE = s / √n is 1.6 for Researcher 1 and 0.8 for Researcher 2."),
          [ch("Researcher 1's interval is narrower, because a smaller sample has less variability in the data", "The standard error is greater for the smaller sample."),
           ch("The two intervals have the same width, because the standard deviations and the confidence levels are equal", "The sample sizes differ, so the standard errors differ."),
           ch("Researcher 2's interval is wider, because a larger sample gives a greater critical value", "A larger sample gives a smaller critical value and a smaller standard error.")],
          "A larger n gives a smaller SE and a narrower interval.", difficulty="medium")
