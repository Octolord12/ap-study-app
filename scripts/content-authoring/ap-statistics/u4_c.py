"""Unit 4, topics 4.6 to 4.8 (the difference between two means).

Required content (CED effective Fall 2026): 4.6 for independent populations the sampling distribution of x-bar1 - x-bar2 has mean mu1 - mu2 and standard deviation sqrt(sigma1^2/n1 + sigma2^2/n2); conditions: two independent random samples (or an experiment with random
assignment, which needs only randomization), each sample at most 10% of its population; normal if both populations are normal, approximately normal if n1 >= 30 and n2 >= 30; interpret in context. 4.7 the two-sample t-interval for mu1 - mu2: parameter in context,
conditions (randomization, 10% unless an experiment, both n >= 30 or both populations approximately normal, otherwise both samples free of strong skewness and outliers), (x-bar1 - x-bar2) +- t* sqrt(s1^2/n1 + s2^2/n2) with t* and df from technology (df between the
smaller of n1 - 1 and n2 - 1 and n1 + n2 - 2); SE and margin of error. 4.8 interpret the interval and confidence level; an interval containing 0 gives insufficient evidence of a difference, one without 0 gives sufficient evidence. Skills 2.C, 3.D, 3.E, 4.D, 4.E, 4.F, 4.G.
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
    # ------------------------------------------------------------------------------------------------------------ 4.6
    T = 6
    m1, s1, n1, m2, s2, n2 = 60, 10, 40, 55, 12, 50
    sd = math.sqrt(s1 ** 2 / n1 + s2 ** 2 / n2)
    B.mcq(T, "Independent random samples of 40 students from School A and 50 students from School B are selected. The mean test score is 60 with a standard deviation of 10 at School A, and 55 with a standard deviation of 12 at School B. What are the mean and the standard deviation of the sampling distribution of $\\bar{x}_1 - \\bar{x}_2$?",
          ch(f"The mean is 5 and the standard deviation is {f2(sd)}", "μ = 60 - 55 = 5 and σ = √(10²/40 + 12²/50) = √(2.5 + 2.88)."),
          [ch(f"The mean is 5 and the standard deviation is {f2(s1 / math.sqrt(n1) + s2 / math.sqrt(n2))}", "This adds the two standard deviations. The variances are added, and then the square root is taken."),
           ch(f"The mean is 5 and the standard deviation is {f2(sd ** 2)}", "This is the variance, before the square root."),
           ch(f"The mean is 115 and the standard deviation is {f2(sd)}", "The mean of the difference is the difference of the means, 60 - 55, not the sum.")],
          f"μ = 5 and σ = √(2.5 + 2.88) = {f2(sd)}.", difficulty="medium")

    B.mcq(T, "Which of the following conditions must be met for the sampling distribution of $\\bar{x}_1 - \\bar{x}_2$ to be used when the data come from two samples taken without replacement?",
          ch("The two samples are independent random samples, and each sample is at most 10% of its population", "These are the randomization and 10% conditions for two samples."),
          [ch("The two samples are random, and the sample sizes are equal", "The sample sizes do not need to be equal."),
           ch("The two samples are matched pairs, and each sample is at least 10% of its population of values in the study", "The samples must be independent, and at most 10% of the populations."),
           ch("One sample is random, and the other is a convenience sample of the same size", "Both samples must be random.")],
          "Two independent random samples, each at most 10% of its population.", difficulty="medium")

    B.mcq(T, "A researcher randomly assigns 60 volunteers to one of two diets, 30 to each, and compares the mean weight loss of the two groups. Which condition is needed to use the sampling distribution of $\\bar{x}_1 - \\bar{x}_2$?",
          ch("The diets must be randomly assigned to the volunteers; the 10% condition is not needed", "For an experiment, the data need only meet the randomization condition."),
          [ch("The volunteers must be a random sample from a population, and the 10% condition must be met", "For an experiment, random assignment is what is needed."),
           ch("Each volunteer must choose their diet, so that the two groups are of equal size", "Choosing a diet is not random assignment."),
           ch("Each group must be at most 10% of a population of all volunteers", "The 10% condition is unnecessary for a randomized experiment.")],
          "For an experiment, random assignment provides randomization; no 10% condition.", difficulty="medium")

    B.mcq(T, "The heights of the plants of two varieties are each approximately normally distributed. Independent random samples of 8 plants of Variety 1 and 10 plants of Variety 2 are selected from very large fields. Is it appropriate to model the sampling distribution of $\\bar{x}_1 - \\bar{x}_2$ with a normal distribution?",
          ch("Yes, because each population is approximately normal, so the sampling distribution of the difference is normal for any sample sizes", "A difference of sample means from two normal populations is normal."),
          [ch("No, because both sample sizes are less than 30", "The sample sizes matter only when the populations are not normal."),
           ch("No, because the sample sizes are not equal", "The sample sizes do not need to be equal."),
           ch("Yes, because the sample sizes add to more than 10", "The sizes do not decide this. The normal populations do.")],
          "Normal populations give a normal sampling distribution of $\\bar{x}_1 - \\bar{x}_2$.", difficulty="medium")

    B.mcq(T, "The incomes in two cities are each strongly skewed to the right. Independent random samples of 20 households from City A and 45 households from City B are selected from very large numbers of households. Is it appropriate to model the sampling distribution of $\\bar{x}_1 - \\bar{x}_2$ with a normal distribution?",
          ch("No, because the populations are not normal and one of the sample sizes, 20, is less than 30", "When the populations are not normal, both sample sizes should be at least 30."),
          [ch("Yes, because one of the sample sizes, 45, is greater than 30, which is large enough for the difference", "Both sample sizes should be at least 30."),
           ch("Yes, because the samples are random and independent", "These are the randomization conditions. The shape needs both n ≥ 30."),
           ch("No, because the populations are in different cities", "Different populations are expected. The sample size of 20 is the issue.")],
          "n1 = 20 < 30 and skewed populations: not appropriate.", difficulty="medium")

    zz = (0 - 5) / sd
    pg = float(sps.norm.sf(zz))
    B.mcq(T, f"Independent random samples of 40 students from School A (μ₁ = 60, σ₁ = 10) and 50 students from School B (μ₂ = 55, σ₂ = 12) are selected. The sampling distribution of $\\bar{{x}}_1 - \\bar{{x}}_2$ is approximately normal with mean 5 and standard deviation {f2(sd)}. What is the approximate probability that the sample mean at School A is greater than the sample mean at School B?",
          ch(f3(pg), f"P($\\bar{{x}}_1 - \\bar{{x}}_2$ > 0) = P(z > (0 - 5) / {f2(sd)}) = P(z > {zz:.2f})."),
          [ch(f3(1 - pg), f"This is P(z < {zz:.2f}), the probability that the sample mean at School A is less than the sample mean at School B."),
           ch("0.500", "This would be the probability if the mean of the difference were 0. The mean is 5."),
           ch(f3(float(sps.norm.sf((0 - 5) / (sd * 2)))), "This doubles the standard deviation, which is not the standard deviation of the difference.")],
          f"P($\\bar{{x}}_1 - \\bar{{x}}_2$ > 0) = P(z > {zz:.2f}), about {f3(pg)}.", difficulty="hard")

    B.mcq(T, "The sampling distribution of $\\bar{x}_1 - \\bar{x}_2$ for independent random samples from School A and School B has a mean of 5 points. Which of the following is the correct interpretation of the mean?",
          ch("Over many pairs of random samples, the mean of the differences in the sample means, School A minus School B, is 5 points, which is μ₁ - μ₂", "The mean of the sampling distribution is the difference in the population means."),
          [ch("In every pair of random samples, the mean at School A is exactly 5 points greater than the mean at School B in that pair, so the sample means never vary", "The differences vary from one pair of samples to another."),
           ch("The mean score at each of the two schools is 5 points", "The mean describes the difference, 5, not each population mean."),
           ch("The scores of 5 points are the most common scores at the two schools", "The mean of the difference does not describe the common scores.")],
          "Interpret the mean as the average difference over many pairs of samples.", difficulty="medium")

    B.mcq(T, f"The standard deviation of the sampling distribution of $\\bar{{x}}_1 - \\bar{{x}}_2$ for independent random samples of test scores from School A and School B is {f2(sd)} points. Which of the following is the correct interpretation?",
          ch(f"In pairs of random samples, the difference in the sample mean scores typically varies from the difference in the population mean scores by about {f2(sd)} points", "The standard deviation is the typical amount that the statistic varies from the parameter."),
          [ch(f"The scores of the students at the two schools typically differ by {f2(sd)} points", "That would be about the scores of individual students, not about the difference in the means."),
           ch(f"Every difference in the sample mean scores is within {f2(sd)} points of the difference in the population mean scores", "Some differences are farther away. The standard deviation is a typical distance."),
           ch(f"The mean score at School A is {f2(sd)} points greater than the mean score at School B", "That would be the mean of the sampling distribution, not its standard deviation.")],
          "The standard deviation is the typical distance of the statistic from the parameter.", difficulty="medium")

    sd_dbl = math.sqrt(s1 ** 2 / (2 * n1) + s2 ** 2 / (2 * n2))
    B.mcq(T, "Both sample sizes are doubled, from 40 and 50 to 80 and 100, and the population means and standard deviations stay the same. What happens to the standard deviation of the sampling distribution of $\\bar{x}_1 - \\bar{x}_2$?",
          ch("It is divided by √2, so it is about 71% of its original value", "Each variance is divided by 2, so the variance of the difference is divided by 2 and the standard deviation by √2."),
          [ch("It is divided by 2", "The variance is divided by 2, so the standard deviation is divided by √2, not by 2."),
           ch("It is multiplied by 2", "Larger samples have less variability, so the standard deviation decreases."),
           ch("It does not change", "The sample sizes are in the formula, so the standard deviation changes.")],
          f"σ changes from {f2(sd)} to {f2(sd_dbl)}: divided by √2.", difficulty="hard")

    # ------------------------------------------------------------------------------------------------------------ 4.7
    T = 7
    B.mcq(T, "A researcher takes independent random samples of 30 students from School A and 32 students from School B, and records the time each student spends on homework. The researcher wants to estimate the difference between the mean times of all students at the two schools. Which procedure is appropriate?",
          ch("A two-sample t-interval for a difference between population means", "The parameter is μ₁ - μ₂, estimated from two independent samples, with σ unknown."),
          [ch("A one-sample t-interval for a population mean difference, using matched pairs", "The students in the two samples are not paired."),
           ch("A two-sample z-interval for a difference between population proportions", "The time is quantitative, so the parameter is a difference in means, not proportions."),
           ch("A one-sample t-interval for a population mean of the times at one school", "There are two populations, so the parameter is a difference between two means.")],
          "Two independent samples, quantitative response: a two-sample t-interval.", difficulty="easy")

    B.mcq(T, "Independent random samples from School A and School B are used to construct an interval for the difference in the mean times that students spend on homework each night. Which of the following correctly states the parameter?",
          ch("μ₁ - μ₂ = the difference between the mean time, in minutes, that all students at School A and all students at School B spend on homework each night", "The parameter references the difference in the means, the response variable and the populations."),
          [ch("$\\bar{x}_1 - \\bar{x}_2$ = the difference between the mean times of the students in the two samples", "This is a statistic. The parameter is about the populations."),
           ch("μ = the mean time that all students at both schools spend on homework each night", "This is a single combined mean, not a difference."),
           ch("μ₁ - μ₂ = the difference between the numbers of students at the two schools who do homework each night, in the sample of students that was selected from the schools", "The parameter is a difference in mean times, not in counts.")],
          "The parameter is the difference between the two population means, in context.", difficulty="easy")

    ga = [34, 38, 41, 43, 44, 46, 47, 49, 50, 52, 53, 55, 58, 60, 63]
    gb = [29, 33, 36, 38, 39, 41, 42, 44, 45, 46, 48, 51, 52, 54, 57, 59, 61, 62]
    bx2 = boxplot([box_group(ga, "Group 1"), box_group(gb, "Group 2")], "Time to complete the task (seconds)", axis=(25, 65, 5),
                  alt="Boxplots of the times of two groups: both are roughly symmetric, with no outliers.")
    assert "outliers" not in bx2["groups"][0] and "outliers" not in bx2["groups"][1]
    B.mcq(T, f"Independent random samples of {len(ga)} people (Group 1) and {len(gb)} people (Group 2) from very large populations complete a task. The boxplots show the times. A two-sample t-interval is planned for the difference in the mean times. Which of the following is correct about the sample data condition?",
          ch("The condition is met, because both samples are small but both boxplots are roughly symmetric with no outliers", "When a sample size is less than 30, the data should be free from strong skewness and outliers."),
          [ch("The condition is not met, because both sample sizes are less than 30, and 30 is always required for a t-interval", "Samples under 30 are acceptable when the data show no strong skewness or outliers."),
           ch("The condition is not met, because the two boxplots overlap", "Overlapping boxplots do not violate the condition."),
           ch("The condition is met, because the sample sizes are different", "The sample sizes do not decide this. The shapes of the data do.")],
          "Both n < 30 and both data sets look symmetric with no outliers: the condition is met.", diagram=bx2, difficulty="medium")

    gc = [8, 9, 10, 10, 11, 12, 12, 13, 14, 15, 41]
    gd = [9, 10, 11, 12, 12, 13, 14, 14, 15, 16, 17, 18]
    gcb = box_group(gc, "Group 1")
    assert gcb.get("outliers") == [41]
    bx3 = boxplot([gcb, box_group(gd, "Group 2")], "Time to complete the task (seconds)", axis=(0, 45, 5), alt="Boxplots of the times of two groups: Group 1 has one outlier at 41 seconds.")
    B.mcq(T, f"Independent random samples of {len(gc)} people (Group 1) and {len(gd)} people (Group 2) from very large populations complete a task. The boxplots show the times. A two-sample t-interval is planned for the difference in the mean times. Which of the following is correct?",
          ch("The sample data condition is not met, because a sample size is less than 30 and Group 1 has an outlier", "If either sample size is less than 30, both samples should be free from strong skewness and outliers."),
          [ch("The sample data condition is met, because the data for Group 2 have no outlier", "Both samples need to be free from strong skewness and outliers when a sample size is less than 30."),
           ch("The sample data condition is met, because the sample sizes are greater than 10", "A sample size above 10 does not meet the condition if there is an outlier."),
           ch("The randomization condition is not met, because there is an outlier in the data for Group 1 of the samples", "An outlier does not mean the samples were not selected at random.")],
          "n < 30 and an outlier in Group 1: the sample data condition is not met.", diagram=bx3, difficulty="medium")

    x1, sd1, nn1, x2, sd2, nn2 = 24.1, 5.2, 30, 21.0, 4.8, 32
    c2 = t2_ci(x1, sd1, nn1, x2, sd2, nn2, 0.95)
    zc = (x1 - x2) - 1.96 * c2.se, (x1 - x2) + 1.96 * c2.se
    sepl = math.sqrt(sd1 ** 2 / nn1) + math.sqrt(sd2 ** 2 / nn2)
    B.mcq(T, "Independent random samples of students from two schools have times, in minutes, to finish a test. School A: n = 30, mean 24.1, standard deviation 5.2. School B: n = 32, mean 21.0, standard deviation 4.8. Both data sets have no strong skewness or outliers. Which of the following is a 95% confidence interval for the difference in the mean times, School A minus School B, as given by technology?",
          ch(f"({f2(c2.lo)}, {f2(c2.hi)})", f"(24.1 - 21.0) ± $t^*$√(5.2²/30 + 4.8²/32) = 3.1 ± {f3(c2.t)}({f3(c2.se)})."),
          [ch(f"({f2(zc[0])}, {f2(zc[1])})", "This uses 1.96 from the standard normal distribution. For a difference in means with unknown σ, use the t critical value."),
           ch(f"({f2(3.1 - c2.t * sepl)}, {f2(3.1 + c2.t * sepl)})", "This adds the two standard errors instead of adding the variances and taking the square root."),
           ch(f"({f2(-3.1 - c2.moe)}, {f2(-3.1 + c2.moe)})", "This is the interval for School B minus School A, with the opposite sign.")],
          f"3.1 ± {f3(c2.moe)} = ({f2(c2.lo)}, {f2(c2.hi)}).", difficulty="hard")

    B.mcq(T, "Independent random samples of students from two schools have times, in minutes, to finish a test. School A: n = 30, standard deviation 5.2. School B: n = 32, standard deviation 4.8. What is the standard error of the difference in the sample mean times?",
          ch(f3(c2.se), "SE = √(s₁²/n₁ + s₂²/n₂) = √(5.2²/30 + 4.8²/32)."),
          [ch(f3(sepl), "This adds the two standard errors. The variances are added first."),
           ch(f3(c2.se ** 2), "This is the variance of the difference, before the square root."),
           ch(f3(math.sqrt(sd1 ** 2 / nn1) - math.sqrt(sd2 ** 2 / nn2)), "This subtracts the standard errors. For independent samples, the variances are added.")],
          f"SE = {f3(c2.se)}.", difficulty="medium")

    B.mcq(T, "For a two-sample t-interval, which of the following is the margin of error?",
          ch("The critical value $t^*$ times the standard error of the difference of the two sample means, √(s₁²/n₁ + s₂²/n₂)", "MOE = $t^*$ × SE."),
          [ch("The critical value $t^*$ times the standard deviation of the pooled samples", "The margin of error uses the standard error of the difference."),
           ch("The difference of the two sample means, $\\bar{x}_1 - \\bar{x}_2$, divided by $t^*$", "The difference of the sample means is the point estimate, the center of the interval."),
           ch("The sum of the two sample standard deviations divided by the total of the two sample sizes in the two groups studied", "This is not a standard error or a margin of error.")],
          "Margin of error = $t^*$ × SE of the difference.", difficulty="medium")

    B.mcq(T, "A two-sample t-interval is constructed from independent samples of sizes 12 and 15. Technology reports the degrees of freedom. Between which two values must the degrees of freedom fall?",
          ch("11 and 25", "The degrees of freedom fall between the smaller of n₁ - 1 and n₂ - 1 (11) and n₁ + n₂ - 2 (25)."),
          [ch("12 and 15", "These are the sample sizes. The degrees of freedom are based on n - 1 and n₁ + n₂ - 2."),
           ch("14 and 27", "These are the larger of n - 1 (14) and n₁ + n₂ (27)."),
           ch("0 and 27", "The degrees of freedom are bounded more tightly.")],
          "min(n1 - 1, n2 - 1) = 11 and n1 + n2 - 2 = 25.", difficulty="hard")

    B.mcq(T, "A confidence interval is calculated for the difference in two population means, μ₁ - μ₂. The sample means are $\\bar{x}_1$ = 24.1 and $\\bar{x}_2$ = 21.0. Which of the following is the point estimate for the difference?",
          ch("3.1", "The point estimate is $\\bar{x}_1 - \\bar{x}_2$ = 24.1 - 21.0."),
          [ch("45.1", "This is the sum of the sample means. The point estimate of the difference is found by subtracting."),
           ch("22.55", "This is the mean of the two sample means, not their difference."),
           ch("-3.1", "This is $\\bar{x}_2 - \\bar{x}_1$. The difference is written in the order the parameter is defined: μ₁ - μ₂.")],
          "Point estimate = 24.1 - 21.0 = 3.1.", difficulty="easy")

    # ------------------------------------------------------------------------------------------------------------ 4.8
    T = 8
    B.mcq(T, f"A 95% confidence interval for the difference between the mean times, in minutes, that students at School A and School B take to finish a test, School A minus School B, is ({f2(c2.lo)}, {f2(c2.hi)}). Which of the following is a correct interpretation?",
          ch(f"We are 95% confident that the interval from {f2(c2.lo)} to {f2(c2.hi)} minutes contains the difference between the mean time of all students at School A and the mean time of all students at School B", "The interpretation references the difference in the means and both populations."),
          [ch(f"There is a 95% probability that the difference between the sample mean times of the two schools is between {f2(c2.lo)} and {f2(c2.hi)} minutes", "The sample means are known. The interval is about the difference in the population means."),
           ch(f"95% of the students at School A take {f2(c2.lo)} to {f2(c2.hi)} minutes longer than the students at School B", "The interval is about the difference in the means, not about individual students."),
           ch(f"The mean time at School A is between {f2(c2.lo)} and {f2(c2.hi)} minutes for 95% of the days on which the test is given", "The interval does not describe days.")],
          "Interpret the interval for the difference in the population means.", difficulty="medium")

    B.mcq(T, "A 95% confidence interval for μ₁ - μ₂, the difference between the mean scores of students at two schools, is (-1.3, 5.2) points. Which of the following is the best conclusion?",
          ch("There is not convincing evidence of a difference between the two population mean scores, because 0 is in the interval", "If the interval contains 0, there is insufficient evidence of a difference."),
          [ch("There is convincing evidence that the two population mean scores are equal, because 0 is in the interval", "An interval that contains 0 does not prove that the means are equal."),
           ch("There is convincing evidence that the mean score is greater at the first school, because most of the interval is positive", "The interval includes 0 and negative values, so a difference has not been shown."),
           ch("There is convincing evidence of a difference, because the interval is not centered at 0", "The question is whether 0 is a plausible value. It is in the interval.")],
          "0 is a plausible value for the difference.", difficulty="medium")

    B.mcq(T, "A 95% confidence interval for μ₁ - μ₂, the difference between the mean cholesterol levels of adults who take Drug 1 and Drug 2, is (-18.5, -4.2) points. Which of the following is the best conclusion?",
          ch("There is convincing evidence that the mean cholesterol level is lower with Drug 1 than with Drug 2, because the interval has only negative values", "A negative difference μ₁ - μ₂ means that μ₁ is less than μ₂."),
          [ch("There is convincing evidence that the mean cholesterol level is higher with Drug 1 than with Drug 2, because the interval has only negative values", "Negative values of μ₁ - μ₂ mean that μ₁ is less than μ₂."),
           ch("There is not convincing evidence of a difference, because the lower limit is negative", "Both limits are negative, so 0 is not in the interval."),
           ch("Every adult who takes Drug 1 has a cholesterol level between 4.2 and 18.5 points lower than with Drug 2", "The interval is for the difference in the mean levels, not for each adult.")],
          "Both limits are negative: μ1 < μ2.", difficulty="medium")

    B.mcq(T, "Which of the following is the correct interpretation of the confidence level in a 95% confidence interval for the difference between two population means?",
          ch("In repeated random sampling with the same sample sizes, approximately 95% of the intervals created will capture the difference between the two population means", "The confidence level describes the long-run success rate of the method."),
          [ch("There is a 95% chance that the one interval that was created contains the difference in the sample means", "The difference in the sample means is known and is the center of the interval."),
           ch("In repeated random sampling, 95% of the differences in the sample means will be equal to the difference in the population means of the two schools being compared", "Most differences in sample means are not equal to the population difference."),
           ch("The difference between the population means is between the limits of the interval 95% of the time", "The difference in the population means is a fixed value. It does not move.")],
          "Long-run capture rate of the method: about 95% of intervals.", difficulty="medium")

    B.mcq(T, "In a randomized experiment, 40 volunteers are randomly assigned to a new study method and 40 volunteers to the usual method. A 95% confidence interval for μ₁ - μ₂, the difference between the mean test scores with the new method and the usual method, is (1.4, 8.9) points. Which of the following is the best conclusion?",
          ch("There is convincing evidence that the new method causes a greater mean score for volunteers like these, because the treatments were randomly assigned", "Random assignment allows a cause-and-effect conclusion, for individuals similar to the volunteers."),
          [ch("There is convincing evidence that the new method would cause a greater mean score for all students in the country, because the interval has only positive values", "The volunteers were not randomly selected from all students, so the conclusion cannot be generalized so widely."),
           ch("There is only evidence of an association between the study method and the score, because the volunteers chose to take part", "Random assignment of the treatments allows a cause-and-effect conclusion."),
           ch("There is not convincing evidence of a difference, because the lower limit, 1.4, is close to 0", "The interval does not contain 0, so there is convincing evidence of a difference.")],
          "Random assignment gives cause and effect; volunteers limit the generalization.", difficulty="hard")

    ca = t2_ci(24.1, 5.2, 30, 21.0, 4.8, 32, 0.90)
    cb = t2_ci(24.1, 5.2, 30, 21.0, 4.8, 32, 0.99)
    B.mcq(T, "From the same two independent random samples, a student constructs a 90% confidence interval and a 99% confidence interval for the difference between two population means. Which of the following is true?",
          ch(f"The 99% interval is wider ({f2(cb.hi - cb.lo)} compared with {f2(ca.hi - ca.lo)}), because a greater confidence level has a greater critical value", "$t^*$ increases with the confidence level."),
          [ch("The 90% interval is wider, because it is less likely to contain the difference", "A lower confidence level gives a narrower interval."),
           ch("The two intervals have the same width, because they use the same samples", "The critical values differ, so the margins of error differ."),
           ch("The 99% interval is narrower, because it is more likely to contain the difference", "To be more confident, the interval must be wider.")],
          "Higher confidence: larger critical value and a wider interval.", difficulty="easy")

    big = t2_ci(24.1, 5.2, 120, 21.0, 4.8, 128, 0.95)
    B.mcq(T, f"Two studies find the same sample means (24.1 and 21.0) and standard deviations (5.2 and 4.8). Study X has samples of about 30 per group and Study Y has samples of about 120 per group. The 95% intervals for μ₁ - μ₂ are ({f2(c2.lo)}, {f2(c2.hi)}) for Study X and ({f2(big.lo)}, {f2(big.hi)}) for Study Y. Which of the following is the best statement?",
          ch("Both intervals provide convincing evidence of a difference, and the interval for Study Y is narrower because its larger samples give a smaller standard error", "Neither interval contains 0, and the width is about proportional to 1 / √n."),
          [ch("Only Study X provides convincing evidence of a difference, because its interval is wider", "A wider interval is less precise, and both intervals exclude 0."),
           ch("The two intervals have the same width, because the sample means and standard deviations are the same", "The sample sizes differ, and the standard error depends on them."),
           ch("Neither interval provides convincing evidence of a difference, because the sample means differ by only 3.1 minutes in the samples", "Both intervals exclude 0, so they show convincing evidence of a difference.")],
          "Neither interval contains 0. Larger samples give a narrower interval.", difficulty="medium")

    B.mcq(T, "A 95% confidence interval for the difference between the mean heights of plants grown with and without a fertilizer, with minus without, is (-0.6, 1.4) cm. A gardener says, \"The fertilizer does not change the mean height.\" Which of the following is the best response?",
          ch("The interval does not provide convincing evidence of a difference, but it does not show that the means are equal; 0 is plausible", "An interval that contains 0 fails to show a difference, but it does not prove no difference."),
          [ch("The gardener is correct, because 0 is in the interval, which proves that the means are equal", "An interval cannot prove that the means are equal."),
           ch("The gardener is incorrect, because an interval that contains negative values shows that the fertilizer lowers the mean height of plants", "The interval also contains positive values and 0."),
           ch("The gardener is incorrect, because the interval has a width of 2.0 cm", "A width of 2.0 does not show a difference.")],
          "0 is plausible, but so are other values: not convincing evidence of a difference, and not proof of none.", difficulty="hard")
