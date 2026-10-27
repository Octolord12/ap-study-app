"""Unit 3, topics 3.5 to 3.8.

Required content (CED effective Fall 2026): 3.5 a hypothesis test decides about a parameter; the one-sample z-test for a proportion; the parameter in context; H0 (status quo, equality p = p0, tested at the boundary) and Ha (the claim: p < p0, p > p0
or p != p0); conditions: random sample, 10% condition, and the expected counts n p0 and n(1 - p0) at least 10. 3.6 the p-value is the probability, assuming H0 is true, of a test statistic as extreme or more extreme (in the direction of Ha) than the one
observed; one-sided and two-sided p-values; a simulated null distribution gives the proportion at least as extreme; interpret it assuming H0 is true; small p-values are evidence for Ha, large p-values are not evidence for H0. 3.7 z = (p-hat - p0) /
sqrt(p0(1 - p0)/n); the significance level alpha; reject H0 if p-value < alpha, otherwise fail to reject; a conclusion in context in terms of Ha with non-definitive language; a test never proves H0. 3.8 a Type I error (convincing evidence for Ha that is
false) has probability alpha; a Type II error (no convincing evidence for Ha that is true) has probability 1 - power; power increases with sample size, a smaller standard error, a true value farther from H0 and a larger alpha; consider the consequences
of each error. Skills 2.C, 2.D, 2.E, 3.C, 3.E, 4.D, 4.E, 4.F, 4.G.
"""
from scipy import stats as sps

from lib import *


def f3(v):
    return f"{float(v):.3f}"


def f4(v):
    return f"{float(v):.4f}"


def build(B):
    # ------------------------------------------------------------------------------------------------------------ 3.5
    T = 5
    B.mcq(T, "A company claims that 90% of its customers are satisfied. A consumer group selects a random sample of 300 customers and wants to test whether the proportion of all of the company's customers who are satisfied is different from 0.90. Which procedure is appropriate?",
          ch("A one-sample z-test for a population proportion", "The parameter is one population proportion and it is compared with a specified value, 0.90."),
          [ch("A two-sample z-test for the difference between two population proportions", "There is one sample and one population, not two."),
           ch("A one-sample z-interval for a population proportion", "An interval estimates a proportion. This question asks about a specific claimed value, so a test is used."),
           ch("A chi-square test for homogeneity", "A chi-square test compares distributions of a categorical variable across populations in a two-way table.")],
          "A test about one proportion compared with a stated value: a one-sample z-test.", difficulty="easy")

    B.mcq(T, "A manufacturer claims that at most 5% of its light bulbs are defective. An inspector believes that the proportion of all of the bulbs that are defective is greater than 5%, and plans to test the claim. Which of the following are the correct hypotheses?",
          ch("H₀: p = 0.05 and Hₐ: p > 0.05, where p is the proportion of all of the manufacturer's bulbs that are defective", "The null hypothesis is the status quo with an equality, and the alternative is the inspector's belief."),
          [ch("H₀: p > 0.05 and Hₐ: p = 0.05, where p is the proportion of all of the manufacturer's bulbs that are defective", "The null hypothesis contains the equality, and the alternative is the belief."),
           ch("H₀: p = 0.05 and Hₐ: p < 0.05, where p is the proportion of all of the manufacturer's bulbs that are defective", "The inspector believes that the proportion is greater than 0.05, not less than 0.05."),
           ch("H₀: p̂ = 0.05 and Hₐ: p̂ > 0.05, where p̂ is the proportion of the bulbs in the sample that are defective", "Hypotheses are about a population parameter, p, not about a sample statistic.")],
          "H0: p = 0.05 and Ha: p > 0.05.", difficulty="medium")

    B.mcq(T, "A school board wants to know whether the proportion of all students at a large school who take the bus has changed from last year's value of 0.40. Which of the following are the correct hypotheses?",
          ch("H₀: p = 0.40 and Hₐ: p ≠ 0.40, where p is the proportion of all students at the school who take the bus now", "The question asks whether the proportion has changed, in either direction, so the alternative is two-sided."),
          [ch("H₀: p = 0.40 and Hₐ: p > 0.40, where p is the proportion of all students at the school who take the bus now", "Nothing says that the proportion increased. The question is whether it changed."),
           ch("H₀: p ≠ 0.40 and Hₐ: p = 0.40, where p is the proportion of all students at the school who take the bus now", "The null hypothesis has the equality, and the alternative says that there is a change."),
           ch("H₀: p = 0.40 and Hₐ: p < 0.40, where p is the proportion of all students at the school who take the bus now", "Nothing says that the proportion decreased. The question is whether it changed.")],
          "A change in either direction is a two-sided alternative: p ≠ 0.40.", difficulty="easy")

    B.mcq(T, "A researcher will test a claim about the proportion of all adults in a city who exercise regularly. Which of the following is the best way to define the parameter in context?",
          ch("p = the proportion of all adults in the city who exercise regularly", "The parameter references the proportion, the response variable and the population."),
          [ch("p = the proportion of the adults in the sample who exercise regularly", "That is the sample proportion, a statistic."),
           ch("p = the number of adults in the city who exercise regularly", "A parameter for this test is a proportion, not a count."),
           ch("p = the proportion of adults who exercise", "This does not state the population, the adults in the city.")],
          "The parameter is the proportion of all adults in the city who exercise regularly.", difficulty="easy")

    B.mcq(T, "For a one-sample z-test for a population proportion with the null hypothesis H₀: p = p₀, how is the normality condition checked?",
          ch("The expected numbers of successes and failures, n p₀ and n(1 - p₀), should each be at least 10", "The test is done assuming the null hypothesis is true, so the null value p₀ is used."),
          [ch("The observed numbers of successes and failures in the sample should each be at least 10, whatever p₀ is", "That is the condition for a confidence interval. For a test, use the null value."),
           ch("The sample size should be greater than 30, whatever the value of p₀", "The condition uses the expected counts, not only the sample size."),
           ch("The expected numbers of successes and failures should each be greater than 5", "Greater than 5 is the expected counts condition for a chi-square test, not for a z-test for a proportion.")],
          "For the z-test, check n p0 ≥ 10 and n(1 - p0) ≥ 10.", difficulty="medium")

    B.mcq(T, "A random sample of 150 bulbs is selected from a very large shipment, to test H₀: p = 0.05 where p is the proportion of all bulbs in the shipment that are defective. Is the normality condition for the one-sample z-test met?",
          ch("No, because the expected number of defective bulbs, 150(0.05) = 7.5, is less than 10", "The expected number of successes under H0 must be at least 10."),
          [ch("Yes, because the expected number of non-defective bulbs, 150(0.95) = 142.5, is greater than 10", "Both expected counts must be at least 10, and the expected number of defective bulbs is 7.5."),
           ch("Yes, because the sample size of 150 is greater than 30", "The condition is about the expected counts."),
           ch("No, because the sample size, 150, is more than 10% of a very large shipment", "A sample of 150 from a very large shipment is less than 10% of it.")],
          "n p0 = 7.5 < 10: the normality condition is not met.", difficulty="medium")

    B.mcq(T, "A student writes the hypotheses H₀: p̂ = 0.60 and Hₐ: p̂ < 0.60 for a test about the proportion of all voters who support a measure, where p̂ is the proportion who support it in a sample of 400 voters. What is the error?",
          ch("The hypotheses are about the sample proportion, but they should be about the population proportion p", "Hypotheses are statements about a population parameter."),
          [ch("The null hypothesis should have the inequality p̂ > 0.60, and the alternative should have the equality", "The null hypothesis has the equality."),
           ch("The alternative hypothesis must always be two-sided, with p̂ ≠ 0.60", "An alternative hypothesis can be one-sided."),
           ch("There is no error, because a sample statistic is used to carry out the test of the claim", "The statistic is used in the test statistic, but the hypotheses are about the parameter.")],
          "Hypotheses use the parameter p, not the statistic p-hat.", difficulty="medium")

    B.mcq(T, "Which of the following is the best description of the null hypothesis in a hypothesis test for a population proportion?",
          ch("The statement about the parameter that is assumed to be correct unless there is convincing statistical evidence otherwise", "It is the status quo, and it contains an equality."),
          [ch("The claim or belief about the parameter for which the researcher is collecting evidence in the study and hopes to support with the data", "That describes the alternative hypothesis."),
           ch("The statement that the sample proportion is equal to the population proportion", "Both hypotheses are about the population parameter, not the sample statistic."),
           ch("The statement that the researcher can prove to be true by using the sample data", "A test can never prove that the null hypothesis is true.")],
          "H0 is the status quo that is assumed unless the evidence is convincing.", difficulty="easy")

    # ------------------------------------------------------------------------------------------------------------ 3.6
    T = 6
    B.mcq(T, "In a test of H₀: p = 0.50 versus Hₐ: p > 0.50, where p is the proportion of all voters in a state who support a measure, the p-value is 0.008. Which of the following is the correct interpretation of the p-value?",
          ch("Assuming that the proportion of all voters in the state who support the measure is 0.50, the probability of getting a sample proportion as large as the one observed, or larger, is 0.008", "The p-value is computed assuming that the null hypothesis is true."),
          [ch("The probability that the proportion of all voters in the state who support the measure is 0.50 is 0.008", "The p-value is not the probability that the null hypothesis is true."),
           ch("The probability that the proportion of all voters who support the measure is greater than 0.50 is 0.992", "The p-value does not give the probability of the alternative hypothesis."),
           ch("Assuming that the proportion of all voters in the state who support the measure is greater than 0.50, the probability of getting the sample proportion that was observed in the random sample is 0.008", "The p-value is computed assuming the null value, not assuming the alternative.")],
          "A p-value is a probability about the data, computed assuming H0 is true.", difficulty="medium")

    B.mcq(T, "A test of a population proportion gives a small p-value. Which of the following is the best interpretation?",
          ch("The observed value of the test statistic would be unusual if the null hypothesis were true, which is evidence for the alternative", "The smaller the p-value, the more convincing the evidence for the alternative."),
          [ch("The null hypothesis is certain to be false, and the alternative hypothesis is certain to be true in this test", "A p-value gives evidence, not certainty."),
           ch("The observed value of the test statistic would be likely if the null hypothesis were true", "A small p-value means that the result would be unlikely if H0 were true."),
           ch("The sample was selected incorrectly, because a sample should not give a small p-value", "A small p-value is not a sign of an incorrect sample.")],
          "A small p-value: the result would be unusual under H0, which supports Ha.", difficulty="medium")

    B.mcq(T, "A test of H₀: p = 0.40 versus Hₐ: p > 0.40 gives a p-value of 0.31. Which of the following is the best conclusion?",
          ch("The p-value is not small, so there is not convincing evidence for the alternative hypothesis, and this is not evidence that the null hypothesis is true", "A large p-value fails to support Ha, but it does not show that H0 is true."),
          [ch("The p-value is large, so there is convincing evidence that the null hypothesis is true for the population in the study", "A large p-value is not evidence for the null hypothesis."),
           ch("The p-value is large, so there is convincing evidence for the alternative hypothesis about the population", "A large p-value does not support the alternative."),
           ch("The p-value is 0.31, so the probability that the null hypothesis is true is 0.31", "The p-value is not the probability that the null hypothesis is true.")],
          "A large p-value: no convincing evidence for Ha, and no evidence that H0 is true.", difficulty="medium")

    z = 2.10
    p_up = float(sps.norm.sf(z))
    p_two = 2 * p_up
    B.mcq(T, "The test statistic for a one-sample z-test is z = 2.10. What is the p-value if the alternative hypothesis is Hₐ: p ≠ p₀ (a two-sided test)?",
          ch(f4(p_two), f"The two-sided p-value is P(z ≤ -2.10) + P(z ≥ 2.10) = 2({f4(p_up)})."),
          [ch(f4(p_up), "This is the one-sided p-value, for the alternative Hₐ: p > p₀ only."),
           ch(f4(1 - p_up), "This is the probability of a z-score less than 2.10. A p-value is a tail probability."),
           ch(f4(p_up / 2), "This halves the one-sided p-value instead of doubling it.")],
          f"p-value = 2P(z ≥ 2.10) = {f4(p_two)}.", difficulty="medium")

    z2 = -1.65
    B.mcq(T, "The test statistic for a one-sample z-test is z = -1.65. What is the p-value if the alternative hypothesis is Hₐ: p < p₀?",
          ch(f4(sps.norm.cdf(z2)), "For a lower-tail alternative, the p-value is P(z ≤ -1.65)."),
          [ch(f4(sps.norm.sf(z2)), "This is P(z ≥ -1.65), the upper tail, which is the wrong direction for this alternative."),
           ch(f4(2 * sps.norm.cdf(z2)), "This is the two-sided p-value. The alternative here is one-sided."),
           ch(f4(1 - 2 * sps.norm.cdf(z2)), "This is 1 minus the two-sided p-value, which is not a tail probability.")],
          f"p-value = P(z ≤ -1.65) = {f4(sps.norm.cdf(z2))}.", difficulty="medium")

    rng = np.random.default_rng(31)
    null_sim = sorted(round(float(v) / 100, 2) for v in rng.binomial(100, 0.50, 100))
    obs = 0.60
    cnt = sum(1 for v in null_sim if v >= obs)
    assert 1 <= cnt <= 10 and null_sim.count(obs) >= 1, (cnt, null_sim.count(obs))
    dp = dotplot(null_sim, "Simulated sample proportion", axis=(0.36, 0.64, 0.04), alt="Dotplot of the sample proportions from 100 simulated random samples of size 100 from a population in which p = 0.50.")
    B.mcq(T, "A test has H₀: p = 0.50 and Hₐ: p > 0.50. The observed sample proportion, from a random sample of size 100, is 0.60. The dotplot shows 100 sample proportions from simulated random samples of size 100 when p = 0.50. Based on the simulation, what is the estimated p-value?",
          ch(f3(cnt / 100), f"{cnt} of the 100 simulated sample proportions are 0.60 or greater, as extreme or more extreme in the direction of the alternative."),
          [ch(f3(null_sim.count(obs) / 100), f"This counts only the simulated proportions that are exactly 0.60: {null_sim.count(obs)} / 100."),
           ch(f3(1 - cnt / 100), f"This is the proportion of the simulated sample proportions that are less than 0.60: {100 - cnt} / 100."),
           ch(f3(2 * cnt / 100), "This doubles the proportion, which is for a two-sided alternative. The alternative here is p > 0.50.")],
          f"Estimated p-value = {cnt} / 100 = {f3(cnt / 100)}.", diagram=dp, difficulty="hard")

    B.mcq(T, "Two different tests of two different claims about population proportions have p-values of 0.003 and 0.04. Which of the following is the best comparison of the evidence?",
          ch("The test with the p-value of 0.003 provides more convincing evidence for its alternative than the test with the p-value of 0.04", "The lower the p-value, the more convincing the evidence for the alternative."),
          [ch("The test with the p-value of 0.04 provides more convincing evidence, because 0.04 is closer to the significance level of 0.05", "A p-value closer to 0.05 is weaker evidence."),
           ch("The two tests provide the same evidence, because both p-values are less than 0.05", "Both are small, but the smaller one is more convincing."),
           ch("The test with the p-value of 0.003 shows that its null hypothesis is certainly false, and the other test shows that its null hypothesis is true", "A p-value gives strength of evidence, not certainty.")],
          "A smaller p-value is more convincing evidence for the alternative.", difficulty="medium")

    # ------------------------------------------------------------------------------------------------------------ 3.7
    T = 7
    t1 = prop_z(62, 100, 0.50, "gt")
    assert abs(t1.z - 2.4) < 1e-9
    B.mcq(T, "A random sample of 100 voters is selected, and 62 of them support a measure. A test has H₀: p = 0.50 and Hₐ: p > 0.50, where p is the proportion of all voters who support the measure. What is the value of the test statistic?",
          ch(f"z = {t1.z:.2f}", f"z = (p̂ - p₀) / √(p₀(1 - p₀) / n) = (0.62 - 0.50) / √(0.50(0.50) / 100) = 0.12 / 0.05."),
          [ch(f"z = {(0.62 - 0.50) / math.sqrt(0.62 * 0.38 / 100):.2f}", "This uses the sample proportion in the standard error. For a test, use the null value p₀."),
           ch(f"z = {(0.62 - 0.50) / math.sqrt(0.5 * 0.5):.2f}", "This leaves out the division by the sample size in the standard error."),
           ch(f"z = {(0.50 - 0.62) / 0.05:.2f}", "The difference is taken in the wrong order. A sample proportion above p₀ gives a positive z.")],
          f"z = {t1.z:.2f}.", difficulty="medium")

    B.mcq(T, "A one-sample z-test of H₀: p = 0.50 versus Hₐ: p > 0.50 gives z = 2.40. Which of the following is the p-value?",
          ch(f4(t1.p), "The p-value is the area to the right of z = 2.40 under the standard normal curve."),
          [ch(f4(2 * t1.p), "This is the two-sided p-value. The alternative is one-sided."),
           ch(f4(1 - t1.p), "This is the area to the left of z = 2.40, not the tail probability."),
           ch(f4(float(sps.norm.pdf(2.4))), "This is the height of the normal curve at z = 2.40, not an area.")],
          f"p-value = P(z ≥ 2.40) = {f4(t1.p)}.", difficulty="medium")

    B.mcq(T, "A test has a p-value of 0.0082. The significance level is α = 0.05. Which of the following is the correct decision and its meaning?",
          ch("Reject the null hypothesis, because the p-value is less than α; the result is statistically significant", "A p-value less than α means reject H0."),
          [ch("Fail to reject the null hypothesis, because the p-value is less than 1", "The decision compares the p-value with α, not with 1."),
           ch("Fail to reject the null hypothesis, because the p-value is very small", "A small p-value less than α leads to rejecting the null hypothesis."),
           ch("Reject the null hypothesis, because the p-value is greater than α; the result is not statistically significant", "The p-value is less than α, not greater.")],
          "p-value 0.0082 < α = 0.05: reject H0.", difficulty="easy")

    B.mcq(T, "A test of H₀: p = 0.50 versus Hₐ: p > 0.50, where p is the proportion of all voters in a state who support a measure, has a p-value of 0.0082. Which of the following is the best conclusion at the 0.05 significance level?",
          ch("There is convincing statistical evidence that the proportion of all voters in the state who support the measure is greater than 0.50", "The conclusion is in context, in terms of the alternative hypothesis, and uses non-definitive language."),
          [ch("There is convincing statistical evidence that the proportion of the voters in the sample who support the measure is greater than 0.50", "The conclusion is about the population proportion, not about the sample."),
           ch("It has been proved that more than 50% of all voters in the state support the measure", "A test does not prove a claim. The language should be non-definitive."),
           ch("There is not convincing statistical evidence that the proportion of all voters in the state who support the measure is greater than 0.50", "With a p-value below α, there is convincing evidence for the alternative.")],
          "Reject H0: convincing evidence that p > 0.50, in context.", difficulty="medium")

    B.mcq(T, "A test of H₀: p = 0.30 versus Hₐ: p ≠ 0.30, where p is the proportion of all students at a school who walk to school, has a p-value of 0.12. The significance level is 0.05. Which of the following is the correct conclusion?",
          ch("There is not convincing statistical evidence that the proportion of all students at the school who walk to school is different from 0.30", "Fail to reject H0: no convincing evidence for Ha."),
          [ch("There is convincing statistical evidence that the proportion of all students at the school who walk to school is exactly 0.30, as the null hypothesis states", "A test cannot show that the null hypothesis is true."),
           ch("There is convincing statistical evidence that the proportion of all students at the school who walk to school is different from 0.30", "The p-value is greater than α, so there is no convincing evidence of a difference."),
           ch("The proportion of all students at the school who walk to school has been shown to be equal to 0.30 by the test", "Failing to reject H0 is not proof that H0 is true.")],
          "p-value 0.12 > 0.05: fail to reject H0. We do not conclude that p = 0.30.", difficulty="medium")

    B.mcq(T, "A test of H₀: p = 0.50 versus Hₐ: p ≠ 0.50 gives z = -1.80. Which of the following is the p-value?",
          ch(f4(2 * sps.norm.cdf(-1.8)), "The two-sided p-value is P(z ≤ -1.80) + P(z ≥ 1.80)."),
          [ch(f4(sps.norm.cdf(-1.8)), "This is the lower-tail p-value, for Hₐ: p < 0.50 only."),
           ch(f4(1 - sps.norm.cdf(-1.8)), "This is P(z ≥ -1.80), which is not a tail probability for this test."),
           ch(f4(4 * sps.norm.cdf(-1.8)), "This doubles the two-sided p-value, which is already the sum of both tails.")],
          f"p-value = 2P(z ≤ -1.80) = {f4(2 * sps.norm.cdf(-1.8))}.", difficulty="medium")

    B.mcq(T, "In a hypothesis test, what is the meaning of the significance level α?",
          ch("The predetermined probability of rejecting the null hypothesis given that it is true", "The significance level is set before the data are collected."),
          [ch("The probability that the null hypothesis is true", "The null hypothesis is either true or not. α is a probability about the decision rule."),
           ch("The probability of failing to reject the null hypothesis given that it is false", "That is the probability of a Type II error, not α."),
           ch("The probability of getting the observed test statistic when the null hypothesis is true", "That is related to the p-value, which is computed from the data.")],
          "α = P(reject H0 | H0 is true).", difficulty="medium")

    B.mcq(T, "A test has a p-value of 0.04. The researcher first planned to use α = 0.01, but then changed to α = 0.05 after seeing the p-value, so that the result would be significant. Which of the following is the best response?",
          ch("The significance level should be chosen in advance, and with α = 0.01 the decision is to fail to reject the null hypothesis", "Choosing α after seeing the result changes the meaning of the test."),
          [ch("The change is appropriate, because the researcher may select any significance level after seeing the p-value of the test", "The significance level is predetermined."),
           ch("The change is appropriate, because a p-value of 0.04 is always significant", "Whether a result is significant depends on the α that was chosen in advance."),
           ch("The change is not needed, because with α = 0.01 the decision is to reject the null hypothesis", "0.04 is greater than 0.01, so the decision is to fail to reject.")],
          "With the planned α = 0.01 and p-value 0.04, fail to reject H0.", difficulty="hard")

    t9 = prop_z(45, 80, 0.60, "lt")
    B.mcq(T, f"A company claims that 60% of its customers renew their membership. A random sample of 80 customers from a very large number of customers is selected, and 45 of them renew. A test of H₀: p = 0.60 versus Hₐ: p < 0.60 gives a test statistic z = {t9.z:.2f} and a p-value of {t9.p:.3f}. At the 0.05 significance level, which of the following is the correct conclusion?",
          ch("There is not convincing statistical evidence that the proportion of all of the company's customers who renew is less than 0.60", f"The p-value, {f3(t9.p)}, is greater than 0.05, so fail to reject H0."),
          [ch("There is convincing statistical evidence that the proportion of all of the company's customers who renew is less than 0.60", f"The p-value, {f3(t9.p)}, is greater than 0.05, so the evidence is not convincing."),
           ch("There is convincing statistical evidence that the proportion of all of the company's customers who renew is equal to 0.60", "A test cannot show that the null hypothesis is true."),
           ch("There is not convincing statistical evidence for anything at all, because the sample proportion is not equal to 0.60 exactly", "The sample proportion is 0.5625. The question is whether that is enough evidence for Ha.")],
          f"z = (0.5625 - 0.60) / √(0.60(0.40) / 80) = {t9.z:.2f}; p-value = {f3(t9.p)} > 0.05: fail to reject H0.", difficulty="hard")

    # ------------------------------------------------------------------------------------------------------------ 3.8
    T = 8
    B.mcq(T, "A test of H₀: p = 0.10 versus Hₐ: p > 0.10 is conducted, where p is the proportion of all patients who have a side effect from a medicine. Which of the following describes a Type I error?",
          ch("Concluding that there is convincing evidence that the proportion of all patients with the side effect is greater than 0.10, when it is actually 0.10", "A Type I error is convincing evidence for the alternative when it is false."),
          [ch("Concluding that there is not convincing evidence that the proportion is greater than 0.10, when it is actually greater than 0.10", "That is a Type II error."),
           ch("Concluding that there is convincing evidence that the proportion is greater than 0.10, when it is actually greater than 0.10", "That is a correct conclusion, not an error."),
           ch("Concluding that there is not convincing evidence that the proportion is greater than 0.10, when it is actually 0.10", "That is a correct conclusion, not an error.")],
          "Type I: evidence for Ha that is not true.", difficulty="medium")

    B.mcq(T, "A test of H₀: p = 0.10 versus Hₐ: p > 0.10 is conducted, where p is the proportion of all patients who have a side effect from a medicine. Which of the following describes a Type II error?",
          ch("Concluding that there is not convincing evidence that the proportion of all patients with the side effect is greater than 0.10, when it is actually greater than 0.10", "A Type II error is no convincing evidence for the alternative when the alternative is true."),
          [ch("Concluding that there is convincing evidence that the proportion of all patients who have the side effect is greater than 0.10, when it is actually 0.10", "That is a Type I error."),
           ch("Concluding that there is convincing evidence that the proportion of all patients who have the side effect is 0.10, when it is actually greater than 0.10", "A test does not provide evidence for the null hypothesis."),
           ch("Concluding that there is not convincing evidence that the proportion is greater than 0.10, when it is actually 0.10", "That is a correct conclusion, not an error.")],
          "Type II: no convincing evidence for Ha although Ha is true.", difficulty="medium")

    B.mcq(T, "A hypothesis test is conducted at the significance level α = 0.01. Which of the following is the probability of a Type I error?",
          ch("0.01", "The probability of a Type I error is the significance level."),
          [ch("0.99", "This is 1 - α, the probability of not rejecting a true null hypothesis."),
           ch("0.05", "The probability of a Type I error is the chosen α, 0.01."),
           ch("It cannot be determined without the sample size", "The probability of a Type I error is α, whatever the sample size.")],
          "P(Type I error) = α = 0.01.", difficulty="easy")

    B.mcq(T, "Which of the following is the best description of the power of a hypothesis test?",
          ch("The probability that the test correctly rejects the null hypothesis when the null hypothesis is false", "Power is the probability of correctly rejecting a false null hypothesis."),
          [ch("The probability that the test rejects the null hypothesis when the null hypothesis is true", "That is the probability of a Type I error, α."),
           ch("The probability that the test fails to reject the null hypothesis when the null hypothesis is actually false", "That is the probability of a Type II error."),
           ch("The probability that the null hypothesis is false", "Power is a probability about the test, given the true value of the parameter.")],
          "Power = P(reject H0 | H0 is false) = 1 - P(Type II error).", difficulty="easy")

    B.mcq(T, "The power of a test against a specific alternative value is 0.85. What is the probability of a Type II error for that alternative value?",
          ch("0.15", "P(Type II error) = 1 - power = 1 - 0.85."),
          [ch("0.85", "This is the power, not the probability of a Type II error."),
           ch("0.05", "The probability of a Type I error is α, which is not given, and it is not 1 - power."),
           ch("0.95", "This would be 1 - α for α = 0.05, which does not apply here.")],
          "P(Type II) = 1 - 0.85 = 0.15.", difficulty="medium")

    B.mcq(T, "A researcher wants to increase the power of a test of a population proportion, and nothing else about the study changes. Which of the following would increase the power?",
          ch("Increasing the sample size", "A larger sample reduces the standard error, which increases the power."),
          [ch("Decreasing the sample size of the study", "A smaller sample increases the standard error and decreases the power."),
           ch("Decreasing the significance level α", "A smaller α makes it harder to reject the null hypothesis, which decreases the power."),
           ch("Choosing a null value that is closer to the true proportion", "When the true value is closer to the null value, the power is smaller.")],
          "Power increases when the sample size increases.", difficulty="medium")

    B.mcq(T, "A test of a medicine's safety has the null hypothesis that the proportion of patients who have a dangerous side effect is at most 0.01. A Type II error would mean not detecting a medicine that is dangerous. Which of the following is the best recommendation?",
          ch("Use a large sample size, since a Type II error has serious consequences and the sample size influences the probability of a Type II error", "The consequences of a Type II error influence the sample size."),
          [ch("Use a very small significance level, since a Type II error has serious consequences and α is the probability of a Type II error in the test", "α is the probability of a Type I error, not of a Type II error."),
           ch("Use a small sample size, since a small sample reduces the probability of a Type II error", "A small sample increases the probability of a Type II error."),
           ch("Ignore the consequences of the errors, since the significance level should be chosen only as 0.05", "The consequences of each error should be considered before the study.")],
          "Consequences of a Type II error should influence the choice of the sample size (a larger n gives more power).", difficulty="hard")

    B.mcq(T, "A researcher increases the significance level of a test from 0.01 to 0.05, with everything else unchanged. Which of the following is correct?",
          ch("The probability of a Type I error increases and the probability of a Type II error decreases", "A larger α makes it easier to reject the null hypothesis, which raises the power."),
          [ch("The probability of a Type I error decreases and the probability of a Type II error increases", "The probability of a Type I error equals α, which increased."),
           ch("The probabilities of both errors increase", "A larger α decreases the probability of a Type II error."),
           ch("The probabilities of both errors stay the same", "The probability of a Type I error is α, which changed.")],
          "Larger α: higher P(Type I), lower P(Type II) (higher power).", difficulty="hard")
