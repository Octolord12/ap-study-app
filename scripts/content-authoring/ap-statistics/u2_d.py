"""Unit 2, topics 2.11 and 2.12.

Required content (CED effective Fall 2026): 2.11 a continuous random variable takes any value in a domain and every interval has a probability; a normal distribution is continuous, unimodal, bell-shaped and symmetric, identified by mu and
sigma (a smaller sigma gives a taller, more concentrated curve); standard normal mu = 0, sigma = 1; the empirical rule 68-95-99.7; probability = area under the curve (total area 1), found with technology or z-scores and a table; intervals for
a given area (lowest p%, middle p%, highest p%, most extreme p% split in two); percentiles and proportions compare relative positions. 2.12 the sampling distribution of a statistic (all possible samples of a size), simulated by taking many random
samples, a randomization distribution (reallocating the responses to the treatment groups), and the central limit theorem (the sampling distribution of a mean is approximately normal, better as the sample gets larger). Skills 3.C, 3.D, 4.C.
"""
from scipy import stats as sps

from lib import *


def p3(v):
    return f"{float(v):.3f}"


def build(B):
    # ------------------------------------------------------------------------------------------------------------ 2.11
    T = 11
    B.mcq(T, "Which of the following describes a normal distribution?",
          ch("A continuous, unimodal, bell-shaped and symmetric distribution that is identified by its mean and its standard deviation",
             "A normal curve has these features, and the mean and standard deviation are its two parameters."),
          [ch("A discrete, bimodal, rectangular and skewed distribution that is identified by its median and its range",
              "A normal distribution is continuous, unimodal, bell-shaped and symmetric."),
           ch("A continuous, unimodal, bell-shaped distribution that is skewed to the right and identified by its minimum and maximum",
              "A normal distribution is symmetric and is identified by the mean and standard deviation, not by the extreme values."),
           ch("A discrete, unimodal, symmetric distribution that counts the successes in a fixed number of independent trials",
              "That describes a binomial distribution (which can be symmetric), not a normal distribution.")],
          "A normal distribution is continuous, unimodal, bell-shaped and symmetric, with parameters μ and σ.", difficulty="easy")

    B.mcq(T, "The heights of the adult women in a large city are approximately normally distributed with a mean of 65 inches and a standard deviation of 3 inches. According to the empirical rule, approximately what percent of the heights are between 62 inches and 68 inches?",
          ch("68%", "62 and 68 are 1 standard deviation below and above the mean, and about 68% of the values are within 1 standard deviation."),
          [ch("95%", "About 95% of the values are within 2 standard deviations, from 59 to 71 inches."),
           ch("99.7%", "About 99.7% of the values are within 3 standard deviations, from 56 to 74 inches."),
           ch("34%", "About 34% of the values are between the mean and 1 standard deviation above it. The interval here is on both sides of the mean.")],
          "The interval is μ ± 1σ, which contains about 68% of the values.", difficulty="easy")

    B.mcq(T, "The heights of the adult women in a large city are approximately normally distributed with a mean of 65 inches and a standard deviation of 3 inches. According to the empirical rule, approximately what percent of the women are taller than 71 inches?",
          ch("2.5%", "71 is 2 standard deviations above the mean. About 95% are within 2 standard deviations, so about 5% are outside, and half of the 5% is above 71."),
          [ch("5%", "This is the percent that is more than 2 standard deviations from the mean on both sides. Only the upper side is asked about."),
           ch("16%", "This is the percent above 1 standard deviation above the mean, 68 inches."),
           ch("0.15%", "This is the percent above 3 standard deviations above the mean, 74 inches.")],
          "(100% - 95%) / 2 = 2.5% are more than 2 standard deviations above the mean.", difficulty="medium")

    pr80 = sps.norm.cdf(80, 70, 8)
    d1 = density(70, 8, [(70, "70"), (80, "80")], shade=[(70 - 3.6 * 8, 80)], x_label="x", alt="Normal curve with mean 70 and standard deviation 8, with the area to the left of 80 shaded.")
    B.mcq(T, "A random variable X is approximately normally distributed with a mean of 70 and a standard deviation of 8. The graph shows the region under the curve to the left of 80. What is the probability that X is less than 80?",
          ch(p3(pr80), f"z = (80 - 70) / 8 = 1.25, and the area to the left of z = 1.25 is about {p3(pr80)}."),
          [ch(p3(1 - pr80), "This is the area to the right of 80, P(X > 80), the unshaded region."),
           ch("0.500", "This is the area to the left of the mean, 70, not of 80."),
           ch(p3(sps.norm.cdf(1)), "This is the area to the left of z = 1, which is 78, not 80.")],
          f"P(X < 80) = P(Z < 1.25), about {p3(pr80)}.", diagram=d1, difficulty="medium")

    pb = sps.norm.cdf(120, 100, 15) - sps.norm.cdf(90, 100, 15)
    B.mcq(T, "Scores on a test are approximately normally distributed with a mean of 100 and a standard deviation of 15. What is the probability that a randomly selected score is between 90 and 120?",
          ch(p3(pb), "z = (90 - 100) / 15 = -0.67 and z = (120 - 100) / 15 = 1.33. The area between them is P(Z < 1.33) - P(Z < -0.67)."),
          [ch(p3(sps.norm.cdf(120, 100, 15)), "This is P(X < 120), the area to the left of 120, which includes the scores below 90."),
           ch(p3(sps.norm.cdf(1.33) - sps.norm.cdf(0.67)), "This uses z = +0.67 instead of z = -0.67 for the lower boundary, 90, which is below the mean."),
           ch("0.680", "This is the area within 1 standard deviation of the mean. The interval from 90 to 120 is not symmetric about 100.")],
          f"P(90 < X < 120) = P(-0.67 < Z < 1.33), about {p3(pb)}.", difficulty="hard")

    p90 = 1050 + sps.norm.ppf(0.90) * 200
    B.mcq(T, "Scores on a college admission test are approximately normally distributed with a mean of 1050 and a standard deviation of 200. Which of the following is the score at the 90th percentile?",
          ch(f"{p90:.0f}", "The 90th percentile has z = 1.28, so the score is 1050 + 1.28(200)."),
          [ch(f"{1050 + sps.norm.ppf(0.95) * 200:.0f}", "This uses z = 1.645, which is for the 95th percentile."),
           ch("1250", "This is 1 standard deviation above the mean, z = 1, the 84th percentile."),
           ch(f"{1050 + sps.norm.ppf(0.10) * 200:.0f}", "This is the 10th percentile, z = -1.28, with the wrong sign.")],
          f"x = μ + zσ = 1050 + 1.28(200), about {p90:.0f}.", difficulty="medium")

    B.mcq(T, "A random variable Z has the standard normal distribution. Which of the following is true?",
          ch("Z has mean 0 and standard deviation 1", "The standard normal distribution is the normal distribution with μ = 0 and σ = 1."),
          [ch("Z has mean 1 and standard deviation 0", "A standard deviation of 0 would mean that all of the values are the same."),
           ch("Z has mean 0 and standard deviation 0.5", "The standard deviation of the standard normal distribution is 1."),
           ch("Z has median 0 and the distribution is skewed to the right", "The standard normal distribution is symmetric.")],
          "Standard normal: μ = 0 and σ = 1.", difficulty="easy")

    B.mcq(T, "Two normal curves have the same mean. Curve A has a standard deviation of 2 and Curve B has a standard deviation of 5. Which of the following is correct?",
          ch("Curve A is taller and more concentrated around the mean than Curve B", "The smaller the standard deviation, the taller and more concentrated the curve."),
          [ch("Curve B is taller and more concentrated around the mean than Curve A", "The curve with the larger standard deviation is shorter and more spread out."),
           ch("Curve A is shifted to the left of Curve B, because it has the smaller standard deviation", "The standard deviation does not change the center. The means are the same."),
           ch("The two curves have the same height, because the areas under the curves are both equal to 1", "The areas are equal, but the curve with the smaller standard deviation must be taller to keep the area at 1.")],
          "A smaller standard deviation gives a taller, more concentrated curve; the area under each curve is 1.", difficulty="medium")

    za, zb = (85 - 78) / 5, (640 - 600) / 50
    assert (za, zb) == (1.4, 0.8)
    B.mcq(T, "A student scores 85 on Test A, which has a mean of 78 and a standard deviation of 5. The same student scores 640 on Test B, which has a mean of 600 and a standard deviation of 50. Both distributions are approximately normal. On which test did the student do better relative to the other students?",
          ch("Test A, because z = 1.4 on Test A is greater than z = 0.8 on Test B", "z-scores compare relative positions: (85 - 78) / 5 = 1.4 and (640 - 600) / 50 = 0.8."),
          [ch("Test B, because 640 is greater than 85", "The scores are on different scales and cannot be compared directly."),
           ch("Test B, because the standard deviation of Test B is greater than the standard deviation of Test A", "A larger standard deviation does not mean a higher relative position."),
           ch("The same on both tests, because the student is above the mean on both tests", "The student is above the mean on both, but by different numbers of standard deviations.")],
          "Compare relative positions with z-scores: 1.4 on Test A and 0.8 on Test B.", difficulty="medium")

    lo, hi = 50 + sps.norm.ppf(0.05) * 10, 50 + sps.norm.ppf(0.95) * 10
    d2 = density(50, 10, [(lo, f"{lo:.1f}"), (50, "50"), (hi, f"{hi:.1f}")], shade=[(lo, hi)], x_label="x", alt="Normal curve with mean 50 and standard deviation 10, with the middle 90% shaded.")
    B.mcq(T, "A random variable X is approximately normally distributed with a mean of 50 and a standard deviation of 10. Which of the following is the interval that contains the middle 90% of the values of X?",
          ch(f"{lo:.1f} to {hi:.1f}", "The middle 90% leaves 5% in each tail. The z-scores are -1.645 and 1.645, so the boundaries are 50 ± 1.645(10)."),
          [ch(f"{50 - 2 * 10:.1f} to {50 + 2 * 10:.1f}", "This is μ ± 2σ, which contains about 95% of the values, not 90%."),
           ch(f"{50 - 1.28 * 10:.1f} to {50 + 1.28 * 10:.1f}", "This is μ ± 1.28σ, which uses the z-score for the 90th percentile and contains about 80% of the values."),
           ch(f"{50 - 1 * 10:.1f} to {50 + 1 * 10:.1f}", "This is μ ± 1σ, which contains about 68% of the values.")],
          f"P({lo:.1f} < X < {hi:.1f}) = 0.90.", diagram=d2, difficulty="hard")

    p75 = sps.norm.sf(75, 65, 3)
    B.mcq(T, "The heights of the adult women in a large city are approximately normally distributed with a mean of 65 inches and a standard deviation of 3 inches. The probability that a randomly selected woman is taller than 69 inches is 0.091. Which of the following is the correct interpretation of this probability?",
          ch("If a woman from the city is selected at random, there is a probability of 0.091 that she is taller than 69 inches", "The probability is interpreted in the context of the situation: the chance for a randomly selected woman."),
          [ch("In the city, exactly 9.1% of the women are 69 inches tall", "The probability is for women taller than 69 inches, not exactly 69 inches. A single height has probability 0."),
           ch("A woman who is 69 inches tall is 0.091 standard deviations above the mean", "That would be a z-score. The probability is an area under the curve."),
           ch("There is a probability of 0.091 that the mean height of the women in the city is greater than 69 inches", "The probability is about the height of one woman, not about the mean height of the women.")],
          "P(X > 69) = 0.091, about 9.1% of the women are taller than 69 inches.", difficulty="medium")

    ps = sps.norm.cdf(650, 500, 100) - sps.norm.cdf(400, 500, 100)
    d3 = density(500, 100, [(400, "400"), (500, "500"), (650, "650")], shade=[(400, 650)], x_label="x", alt="Normal curve with mean 500 and standard deviation 100, with the area between 400 and 650 shaded.")
    B.mcq(T, "The graph shows a normal curve with a mean of 500 and a standard deviation of 100. The area between 400 and 650 is shaded. Which of the following is the proportion of the values in the shaded region?",
          ch(p3(ps), "z = (400 - 500) / 100 = -1 and z = (650 - 500) / 100 = 1.5. The area is P(Z < 1.5) - P(Z < -1) = 0.9332 - 0.1587."),
          [ch(p3(sps.norm.cdf(1.5)), "This is the area to the left of 650, which includes the area to the left of 400."),
           ch(p3(sps.norm.cdf(1.5) - sps.norm.cdf(-1.5)), "This uses z = -1.5 for the lower boundary, which would be 350, not 400."),
           ch("0.950", "This is the area within 2 standard deviations of the mean. The shaded region is from 1 below to 1.5 above.")],
          f"P(400 < X < 650) = P(-1 < Z < 1.5), about {p3(ps)}.", diagram=d3, difficulty="hard")

    # ------------------------------------------------------------------------------------------------------------ 2.12
    T = 12
    B.mcq(T, "What is the sampling distribution of a statistic?",
          ch("The distribution of the values of the statistic for all possible samples of a given size from a given population", "A sampling distribution shows how the statistic varies from sample to sample."),
          [ch("The distribution of the values of the variable for the individuals in one sample that was selected from the population", "That is the distribution of the sample data, not of a statistic."),
           ch("The distribution of the values of the variable for all of the individuals in the population that is sampled", "That is the distribution of the population."),
           ch("The distribution of the values of the statistic for the same sample, calculated again after each of the individuals is removed", "A sampling distribution comes from different samples, not from changes to a single sample.")],
          "A sampling distribution is the distribution of a statistic over all possible samples of a given size.", difficulty="easy")

    B.mcq(T, "A student wants to simulate the sampling distribution of the sample proportion for samples of size 25 from a population in which the proportion is 0.40. Which of the following is the best description of the simulation?",
          ch("Repeatedly generate a large number of random samples of size 25 from a population with proportion 0.40, record the sample proportion of each sample, and display the distribution of the recorded values",
             "The distribution of the statistic over many random samples approximates the sampling distribution."),
          [ch("Generate one random sample of size 25 from a population with proportion 0.40, and display the distribution of the values in that sample",
              "One sample gives one value of the statistic, not a distribution of the statistic."),
           ch("Generate 25 random samples of size 1 from a population with proportion 0.40, and display the distribution of the 25 results",
              "The samples must have size 25, and a large number of samples should be generated."),
           ch("Generate a large number of random samples of size 25 from a population with proportion 0.40, and display the distribution of the values in the first sample",
              "The statistic must be recorded for each sample, and all of the recorded values should be displayed.")],
          "Simulate by taking many random samples, recording the statistic from each, and displaying its distribution.", difficulty="medium")

    B.mcq(T, "In an experiment, 20 participants are randomly assigned to two treatment groups of 10. A researcher repeatedly reassigns the 20 observed response values at random to the two groups, and records the difference between the group means each time. What is the distribution of these recorded differences called?",
          ch("A randomization distribution", "A randomization distribution is generated by repeatedly randomly reallocating the response values to the treatment groups."),
          [ch("A binomial distribution", "A binomial distribution counts successes in a fixed number of independent trials."),
           ch("A standard normal distribution", "A standard normal distribution has mean 0 and standard deviation 1, and these differences do not necessarily have those parameters."),
           ch("A population distribution", "A population distribution is the distribution of the values for all of the individuals in a population.")],
          "Repeatedly reassigning the responses to the groups and recording a statistic gives a randomization distribution.", difficulty="medium")

    B.mcq(T, "Which of the following is a statement of the central limit theorem?",
          ch("The sampling distribution of the mean of a random sample has a shape that can be approximated by a normal distribution, and the larger the sample, the better the approximation",
             "This is the central limit theorem."),
          [ch("The distribution of the values in a large random sample is approximately normal, whatever the shape of the population",
              "The data in a sample look like the population. It is the distribution of the sample means that becomes approximately normal."),
           ch("The mean of a large random sample is always exactly equal to the mean of the population from which it was selected",
              "A sample mean is an estimate that varies from sample to sample."),
           ch("The sampling distribution of the mean of a random sample is normal only when the population is itself normal",
              "The approximation holds for large samples from populations with other shapes as well.")],
          "The central limit theorem is about the shape of the sampling distribution of a mean.", difficulty="medium")

    rng = np.random.default_rng(3)
    means = [float(np.mean(rng.exponential(20, 40))) for _ in range(300)]
    edges = [10 + 2 * k for k in range(0, 14)]
    assert min(means) > 10 and max(means) < 36, (min(means), max(means))
    h = histogram(means, edges, "Sample mean (minutes)", alt="Histogram of the means of 300 simulated random samples of size 40 from a right-skewed population: approximately normal and centered near 20.")
    B.mcq(T, "A population of waiting times is strongly skewed to the right, with a mean of 20 minutes. The histogram shows the means of 300 simulated random samples of size 40 from this population. Which of the following best describes the shape of the distribution of the sample means?",
          ch("Approximately normal, even though the population is skewed", "By the central limit theorem, the sampling distribution of the mean of a sample of size 40 is approximately normal."),
          [ch("Skewed to the right, like the population, because the samples come from a skewed population", "The sampling distribution of a mean of a larger sample is more symmetric than the population."),
           ch("Bimodal, because the samples have two groups of waiting times", "Nothing indicates two groups. The sample means form one pile near 20."),
           ch("Approximately uniform, because every sample mean is about equally likely to occur", "The histogram has one main peak near the mean of 20, and fewer values far from it.")],
          "The sampling distribution of a mean from a sample of size 40 is approximately normal (central limit theorem).", diagram=h, difficulty="medium")

    B.mcq(T, "A population is skewed to the right. A statistician takes many random samples of size 5 and many random samples of size 100, and makes a histogram of the sample means for each sample size. Which of the following is the most reasonable conclusion?",
          ch("The histogram for the samples of size 100 is closer to a normal shape than the histogram for the samples of size 5", "The larger the sample size, the better the normal approximation to the sampling distribution of the mean."),
          [ch("The histogram for the samples of size 5 is closer to a normal shape than the histogram for the samples of size 100", "A larger sample size gives a better approximation."),
           ch("Both histograms have exactly the same shape, because the samples come from the same population", "The shape of the sampling distribution of the mean changes with the sample size."),
           ch("Neither histogram can be approximately normal, because the population is not normal", "A large enough sample size gives an approximately normal sampling distribution.")],
          "With a larger sample, the central limit theorem gives a better normal approximation.", difficulty="medium")

    rngp = np.random.default_rng(8)
    phats = [round(float(v) / 25, 2) for v in rngp.binomial(25, 0.4, 60)]
    ge = sum(1 for v in phats if v >= 0.52)
    ex = phats.count(0.52)
    assert 5 <= ge <= 14 and 0 < ex < ge and min(phats) >= 0.08 and max(phats) <= 0.72, (ge, ex, sorted(phats))
    dpp = dotplot(phats, "Sample proportion", axis=(0.08, 0.72, 0.08), alt="Dotplot of the sample proportions from 60 simulated random samples of size 25 from a population with proportion 0.40.")
    B.mcq(T, "The dotplot shows the sample proportions from 60 simulated random samples of size 25 from a population with proportion 0.40. Based on the simulation, what is the estimated probability of a sample proportion of 0.52 or greater?",
          ch(p3(ge / 60), f"{ge} of the 60 simulated sample proportions are 0.52 or greater: {ge} / 60."),
          [ch(p3(ex / 60), f"This counts only the {ex} samples with a sample proportion of exactly 0.52."),
           ch(f"{ge}", "This is the number of sample proportions that are 0.52 or greater, not a probability."),
           ch(p3(1 - ge / 60), f"This is the relative frequency of the sample proportions that are less than 0.52: {60 - ge} / 60.")],
          f"Estimated probability = {ge} / 60 = {p3(ge / 60)}.", diagram=dpp, difficulty="medium")

    B.mcq(T, "Two different random samples of 50 students are selected from the same school, and the mean number of hours of sleep is calculated for each sample. The two sample means are 7.1 and 7.4 hours. Which of the following is the best explanation for the difference?",
          ch("The sample mean varies from sample to sample, because each random sample contains different students", "A statistic varies from one random sample to another. This is described by its sampling distribution."),
          [ch("One of the two samples must have been selected incorrectly, because the sample means should be equal", "Samples from the same population have different means by chance."),
           ch("The population mean changed between the two samples, because the students were selected at different times", "The population mean is a fixed value. The statistics are what vary."),
           ch("The larger sample mean is the true mean of the population, because it is closer to 8 hours", "Neither sample mean is known to equal the population mean.")],
          "The values of a statistic vary from sample to sample; the sampling distribution describes that variation.", difficulty="medium")
