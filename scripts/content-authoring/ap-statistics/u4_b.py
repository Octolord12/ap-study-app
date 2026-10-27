"""Unit 4, topics 4.4 and 4.5 (one-sample t-test and matched pairs).

Required content (CED effective Fall 2026): 4.4 the one-sample t-test for a mean when sigma is unknown; for a matched pairs design the one-sample t-test for a mean difference (one sample of differences); the parameter in context (and the order of
subtraction for a difference); H0: mu = mu0 (or mu_d = 0) with Ha: <, > or !=; conditions: random sample or randomized experiment, 10%, and the sample data condition (approximately normal population, or n >= 30, or n < 30 with data free of strong skewness
and outliers; for matched pairs, the differences). 4.5 t = (x-bar - mu0) / (s / sqrt(n)) with df = n - 1; the p-value from the t-distribution; interpret it assuming H0 is true; reject H0 if the p-value <= alpha, else fail to reject; a conclusion in context in terms of Ha,
non-definitive. Skills 2.C, 2.E, 3.E, 4.E, 4.F, 4.G.
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
    # ------------------------------------------------------------------------------------------------------------ 4.4
    T = 4
    B.mcq(T, "A cereal company claims that the mean weight of its boxes is 340 grams. An inspector believes that the mean weight is less than 340 grams and plans to weigh a random sample of 20 boxes. The population standard deviation is unknown. Which procedure is appropriate?",
          ch("A one-sample t-test for a population mean", "The parameter is one population mean, compared with a claimed value, and σ is unknown."),
          [ch("A one-sample z-test for a population proportion", "The weights are quantitative, so the parameter is a mean, not a proportion."),
           ch("A two-sample t-test for a difference between two population means", "There is one sample and one population."),
           ch("A one-sample z-test for a population mean, using the sample standard deviation as σ", "When σ is unknown, the sample standard deviation is used with the t-distribution.")],
          "One mean, claimed value, σ unknown: a one-sample t-test.", difficulty="easy")

    B.mcq(T, "A cereal company claims that the mean weight of its boxes is 340 grams. An inspector believes that the mean weight is less than 340 grams. Which of the following are the correct hypotheses?",
          ch("H₀: μ = 340 and Hₐ: μ < 340, where μ is the mean weight, in grams, of all of the company's boxes", "The null hypothesis is the claim with an equality, and the alternative is the inspector's belief."),
          [ch("H₀: μ < 340 and Hₐ: μ = 340, where μ is the mean weight, in grams, of all of the company's boxes", "The null hypothesis contains the equality."),
           ch("H₀: μ = 340 and Hₐ: μ > 340, where μ is the mean weight, in grams, of all of the company's boxes", "The inspector believes that the mean is less than 340, not greater."),
           ch("H₀: x̄ = 340 and Hₐ: x̄ < 340, where x̄ is the mean weight, in grams, of the boxes in the sample", "Hypotheses are about the population mean μ, not the sample mean.")],
          "H0: μ = 340 and Ha: μ < 340.", difficulty="medium")

    B.mcq(T, "Twelve people each have their reaction time measured before and after drinking an energy drink. The researcher wants to test whether the mean reaction time is different after the drink. Which procedure is appropriate?",
          ch("A one-sample t-test for a population mean difference, using the 12 differences", "The measurements are paired, so the analysis is a one-sample test of the differences."),
          [ch("A two-sample t-test for a difference between two population means, using independent samples", "The before and after times are for the same people, so they are not independent."),
           ch("A one-sample t-test for the mean of the before times", "The question is about the change, which needs both times."),
           ch("A chi-square test for homogeneity of the before and after times", "The response is quantitative, and a chi-square test is for categorical data.")],
          "Matched pairs: use the differences in a one-sample t-test.", difficulty="medium")

    B.mcq(T, "Twelve people each have their reaction time, in milliseconds, measured before and after drinking an energy drink. Let the difference for a person be the time before minus the time after. The researcher believes that the drink shortens the mean reaction time. Which of the following are the correct hypotheses?",
          ch("H₀: $\mu_d$ = 0 and Hₐ: $\mu_d$ > 0, where $\mu_d$ is the population mean difference (before - after) in the reaction times of people like these", "A shorter time after the drink gives a positive difference (before - after)."),
          [ch("H₀: $\mu_d$ = 0 and Hₐ: $\mu_d$ < 0, where $\mu_d$ is the population mean difference (before - after) in the reaction times of people like these", "A positive mean difference (before - after) means that the drink shortens the time, so the alternative is $\mu_d$ > 0."),
           ch("H₀: $\mu_d$ > 0 and Hₐ: $\mu_d$ = 0, where $\mu_d$ is the population mean difference (before - after) in the reaction times of people like these", "The null hypothesis has the equality."),
           ch("H₀: μ₁ = μ₂ and Hₐ: μ₁ > μ₂, where μ₁ and μ₂ are the mean reaction times of two separate groups", "The data are paired, so the parameter is one mean difference.")],
          "With d = before - after, the researcher's belief is $\mu_d$ > 0.", difficulty="hard")

    B.mcq(T, "A teacher says that the mean time that students spend on homework each night is 40 minutes. A parent thinks the mean is different from 40 minutes. Which of the following are the correct hypotheses?",
          ch("H₀: μ = 40 and Hₐ: μ ≠ 40, where μ is the mean time, in minutes, that all students spend on homework each night", "A difference in either direction is a two-sided alternative."),
          [ch("H₀: μ = 40 and Hₐ: μ > 40, where μ is the mean time, in minutes, that all students spend on homework each night", "The parent does not say the mean is greater, only that it is different."),
           ch("H₀: μ ≠ 40 and Hₐ: μ = 40, where μ is the mean time, in minutes, that all students spend on homework each night", "The null hypothesis contains the equality."),
           ch("H₀: μ = 40 and Hₐ: μ < 40, where μ is the mean time, in minutes, that all students spend on homework each night", "The parent does not say the mean is less, only that it is different.")],
          "A mean that is different: Ha: μ ≠ 40.", difficulty="easy")

    sym = [31, 33, 34, 35, 36, 36, 37, 38, 38, 39, 40, 41, 43, 45]
    dpl = dotplot(sym, "Time (minutes)", axis=(30, 46, 2), alt="Dotplot of 14 times: roughly symmetric around 37 minutes, with no outliers.")
    B.mcq(T, "A random sample of 14 students from a very large school is selected, and each student's time to finish an assignment is recorded. The dotplot shows the times. A one-sample t-test is planned for the mean time of all students at the school. Which of the following is the best statement about the conditions?",
          ch("The sample data condition is met, because n < 30 and the dotplot has no strong skewness or outliers", "For n < 30, the sample data should be free from strong skewness and outliers."),
          [ch("The sample data condition is not met, because the sample size is less than 30", "A sample size under 30 is acceptable when the data show no strong skewness or outliers."),
           ch("The sample data condition is not met, because the data are not exactly normal in shape", "The data need not be exactly normal."),
           ch("The 10% condition is not met, because the sample size of 14 is greater than 10", "The 10% condition compares the sample size with the number of students at the school, which is very large.")],
          "n = 14 < 30 and the data are roughly symmetric with no outliers: the condition is met.", diagram=dpl, difficulty="medium")

    grp = box_group([7, 8, 9, 9, 10, 10, 11, 12, 13, 14, 45], None)
    assert grp.get("outliers") == [45]
    bx = boxplot([grp], "Time (minutes)", axis=(0, 50, 5), alt="Boxplot of 11 times: the box is between about 9 and 13 minutes, and one value, 45, is plotted as an outlier.")
    B.mcq(T, "A random sample of 11 customers from a very large number of customers is selected, and each customer's wait time is recorded. The boxplot shows the times. A one-sample t-test is planned for the mean wait time of all customers. Which of the following is correct?",
          ch("The sample data condition is not met, because the sample size is less than 30 and the data have an outlier", "For n < 30, the sample data should be free from strong skewness and outliers."),
          [ch("The sample data condition is met, because the sample size is greater than 10", "A sample size above 10 does not meet the condition if there is an outlier."),
           ch("The sample data condition is met, because the outlier is only one of the 11 values in the sample of customers", "One strong outlier in a small sample violates the condition."),
           ch("The randomization condition is not met, because the data have an outlier", "An outlier does not mean the sample was selected without a random method.")],
          "n = 11 < 30 and there is an outlier (45): the sample data condition is not met.", diagram=bx, difficulty="medium")

    B.mcq(T, "A researcher will test a claim about the mean daily screen time of all students at a school. Which of the following is the best way to define the parameter in context?",
          ch("μ = the mean daily screen time, in hours, of all students at the school", "The parameter references the population mean, the response variable and the population."),
          [ch("μ = the mean daily screen time, in hours, of the students in the sample who answered", "This is a sample mean, a statistic."),
           ch("μ = the mean daily screen time of the students who answered the survey at school", "This does not state the population."),
           ch("μ = the median daily screen time, in hours, of all students at the school", "The test is about the mean, not the median.")],
          "The parameter is the population mean, in context.", difficulty="easy")

    B.mcq(T, "Why is a t-test, rather than a z-test, used for a population mean in most situations?",
          ch("Because the population standard deviation σ is usually unknown, so s is used, and the t-distribution accounts for the added variability", "t-distributions are used when σ is unknown and s must be used."),
          [ch("Because a t-test can be used only when the sample size is less than 30", "A t-test can be used for any sample size when the conditions are met."),
           ch("Because a t-test does not require a random sample", "A random sample or a randomized experiment is still required."),
           ch("Because the population standard deviation σ is always known and equal to the sample standard deviation, so t is a more exact choice in every situation", "σ is usually not known.")],
          "t is used when σ is unknown and s replaces it.", difficulty="medium")

    # ------------------------------------------------------------------------------------------------------------ 4.5
    T = 5
    tt = t_test(52.1, 8.0, 25, 50, "gt")
    B.mcq(T, "A random sample of 25 students has a mean score of 52.1 and a standard deviation of 8.0. A test has H₀: μ = 50 and Hₐ: μ > 50. What is the value of the test statistic?",
          ch(f"t = {f2(tt.t)}", "t = ($\\bar{x}$ - μ₀) / (s / √n) = (52.1 - 50) / (8.0 / √25) = 2.1 / 1.6."),
          [ch(f"t = {f2((52.1 - 50) / 8.0)}", "This leaves out the division by √n: the standard error is s / √n."),
           ch(f"t = {f2((52.1 - 50) / (8.0 / 25))}", "This divides s by n instead of by √n."),
           ch(f"t = {f2((50 - 52.1) / 1.6)}", "The difference is taken in the wrong order: a sample mean above μ₀ gives a positive t.")],
          f"t = 2.1 / 1.6 = {f2(tt.t)}.", difficulty="medium")

    B.mcq(T, "A one-sample t-test is based on a random sample of 25 values. How many degrees of freedom does the t-distribution have?",
          ch("24", "df = n - 1 = 24."),
          [ch("25", "This is the sample size. The degrees of freedom are n - 1."),
           ch("23", "This is n - 2, which is the degrees of freedom for a different procedure."),
           ch("26", "This is n + 1, which has no use here.")],
          "df = 25 - 1 = 24.", difficulty="easy")

    p_up = float(sps.t.sf(2.30, 24))
    p_two = 2 * p_up
    B.mcq(T, "A one-sample t-test of H₀: μ = 50 versus Hₐ: μ ≠ 50 is based on a random sample of 25 values and gives t = 2.30. What is the p-value?",
          ch(f3(p_two), "The two-sided p-value is 2P(t ≥ 2.30) with df = 24."),
          [ch(f3(p_up), "This is the one-sided p-value, for Hₐ: μ > 50 only."),
           ch(f3(2 * float(sps.norm.sf(2.30))), "This uses the standard normal distribution. The p-value should come from the t-distribution with 24 degrees of freedom."),
           ch(f3(1 - p_up), "This is the area to the left of t = 2.30, not a tail probability.")],
          f"p-value = 2P(t ≥ 2.30) with df = 24, about {f3(p_two)}.", difficulty="medium")

    B.mcq(T, f"A test of H₀: μ = 50 versus Hₐ: μ ≠ 50 gives t = 2.30 with 24 degrees of freedom and a p-value of {f3(p_two)}. The significance level is 0.05. Which of the following is the correct decision and its meaning?",
          ch("Reject the null hypothesis, because the p-value is less than 0.05; there is convincing evidence that the mean differs from 50", "A p-value less than α means reject H0."),
          [ch("Fail to reject the null hypothesis, because the p-value is less than 0.05; there is no convincing evidence that the mean is different", "A p-value less than α leads to rejecting the null hypothesis."),
           ch("Reject the null hypothesis, because t = 2.30 is greater than the degrees of freedom, 24", "The decision compares the p-value with α."),
           ch("Fail to reject the null hypothesis, because the mean is not equal to 50 in the sample", "The sample mean always differs somewhat from μ₀. The p-value decides.")],
          f"p-value {f3(p_two)} < 0.05: reject H0.", difficulty="easy")

    B.mcq(T, "A test of H₀: μ = 340 versus Hₐ: μ < 340, where μ is the mean weight, in grams, of all of a company's cereal boxes, has a p-value of 0.18. The significance level is 0.05. Which of the following is the best conclusion?",
          ch("There is not convincing statistical evidence that the mean weight of all of the company's cereal boxes is less than 340 grams", "The p-value is greater than α: fail to reject H0."),
          [ch("There is convincing statistical evidence that the mean weight of all of the company's cereal boxes is 340 grams", "A test cannot show that the null hypothesis is true."),
           ch("There is convincing statistical evidence that the mean weight of all of the company's cereal boxes is less than 340 grams, as the inspector believes", "The p-value is greater than 0.05, so the evidence is not convincing."),
           ch("It has been proved that the company's boxes weigh exactly 340 grams", "Failing to reject H0 is not proof, and the language should be non-definitive.")],
          "p-value 0.18 > 0.05: fail to reject H0.", difficulty="medium")

    B.mcq(T, "A test of H₀: μ = 40 versus Hₐ: μ ≠ 40, where μ is the mean time, in minutes, that all students at a school spend on homework each night, has a p-value of 0.03. Which of the following is the correct interpretation of the p-value?",
          ch("Assuming that the mean time of all students is 40 minutes, the probability of a sample mean at least as far from 40 as the one observed is 0.03", "The p-value is computed assuming that the null hypothesis is true."),
          [ch("The probability that the mean time of all students at the school is 40 minutes is 0.03", "The p-value is not the probability that the null hypothesis is true."),
           ch("Assuming that the mean time is different from 40 minutes, the probability of the observed sample mean from the random sample that was selected is 0.03", "The p-value is computed assuming the null value, not the alternative."),
           ch("3% of the students at the school spend 40 minutes on homework", "The p-value is not a percent of the students.")],
          "The p-value is computed assuming H0 is true.", difficulty="medium")

    mp = t_test(2.5, 4.0, 16, 0, "ne")
    B.mcq(T, f"Each of 16 workers has a task timed with an old tool and with a new tool. The difference for each worker is the time with the old tool minus the time with the new tool. The mean of the differences is 2.5 minutes with a standard deviation of 4.0 minutes. The differences have no strong skewness or outliers. A test of H₀: $\\mu_d$ = 0 versus Hₐ: $\\mu_d$ ≠ 0 gives t = {f2(mp.t)} with df = {mp.df} and a p-value of {f3(mp.p)}. Which of the following is the best conclusion at the 0.05 significance level?",
          ch("There is convincing statistical evidence that the population mean difference in the times (old - new) is not 0 for workers like these", f"The p-value, {f3(mp.p)}, is less than 0.05: reject H0."),
          [ch("There is not convincing statistical evidence of a difference in the mean times, because the sample mean difference is only 2.5 minutes", "The decision depends on the p-value, not on the size of the sample mean difference alone."),
           ch("There is convincing statistical evidence that the mean difference in the 16 sampled workers is not 0", "The conclusion should be about the population of workers, not about the sample."),
           ch("There is convincing statistical evidence that the two tools take the same mean time", "A small p-value is evidence for a difference, not for sameness.")],
          f"t = 2.5 / (4.0 / √16) = {f2(mp.t)}; p-value = {f3(mp.p)} < 0.05: reject H0.", difficulty="medium")

    pz = 2 * float(sps.norm.sf(2.1))
    pt = 2 * float(sps.t.sf(2.1, 14))
    B.mcq(T, f"A student has a t-statistic of 2.1 from a random sample of 15 values and finds the two-sided p-value {f3(pz)} by using a standard normal distribution. The correct p-value, from the t-distribution with 14 degrees of freedom, is {f3(pt)}. What is wrong with the student's approach?",
          ch("The student used a standard normal distribution, which has thinner tails, so the p-value is too small and the evidence looks stronger", "A t-statistic from a small sample follows a t-distribution, which has wider tails."),
          [ch("The student used a t-distribution, which has thinner tails than the standard normal distribution", "The student used the standard normal distribution, and the t-distribution has wider tails."),
           ch("The student should have doubled the p-value a second time, because the test is two-sided", "The p-value already includes both tails."),
           ch("Nothing is wrong, because the standard normal distribution and the t-distribution are always the same for every sample size and every sample", "They are close only for large samples.")],
          "For small samples, using the standard normal distribution gives a p-value that is too small.", difficulty="hard")

    B.mcq(T, "A random sample of 40 students is used to test H₀: μ = 70 versus Hₐ: μ > 70. The result is not statistically significant at the 0.05 level. Which of the following is the best conclusion?",
          ch("There is not convincing evidence that the mean is greater than 70, and this does not show that it is 70", "Failing to reject H0 is not evidence for H0."),
          [ch("The mean is exactly 70, because the test did not reject the null hypothesis, so H₀ is true", "A test cannot show that the null hypothesis is true."),
           ch("The mean is less than 70, because the p-value is large", "A large p-value does not point to the other direction."),
           ch("The test was invalid, because a valid test always rejects the null hypothesis when the sample is large enough", "A valid test may or may not reject the null hypothesis.")],
          "Failing to reject H0 means no convincing evidence for Ha, not evidence for H0.", difficulty="medium")
