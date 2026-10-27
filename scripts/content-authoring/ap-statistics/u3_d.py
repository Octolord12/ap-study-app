"""Unit 3, topics 3.14 and 3.15 (chi-square tests for homogeneity and independence).

Required content (CED effective Fall 2026): 3.14 the chi-square statistic measures the distance between observed and expected counts relative to the expected counts; chi-square distributions have positive values and are skewed right, less skewed as the
degrees of freedom grow; the test for homogeneity compares the distribution of a categorical variable across two or more populations or treatments (H0: no difference in the distributions, Ha: a difference); the test for independence asks whether two
categorical variables in one population are associated (H0: no association / independent); conditions: random sample (independence) or independent random samples or a randomized experiment (homogeneity), the 10% condition (unnecessary for an
experiment), all expected counts greater than 5. 3.15 expected count = row total x column total / table total; chi-square = sum of (observed - expected)^2 / expected over all cells, with (rows - 1)(columns - 1) degrees of freedom; the p-value from the
chi-square distribution; interpret it assuming H0 is true; decide against alpha; a conclusion in context about the population(s). Skills 2.C, 2.E, 3.C, 3.E, 4.C, 4.E, 4.F, 4.G.
"""
from scipy import stats as sps

from lib import *


def f3(v):
    return f"{float(v):.3f}"


def f4(v):
    return f"{float(v):.4f}"


def build(B):
    # ------------------------------------------------------------------------------------------------------------ 3.14
    T = 14
    B.mcq(T, "Which of the following best describes what the chi-square statistic measures?",
          ch("The distance between the observed counts and the expected counts, relative to the expected counts", "$\\chi^2$ is the sum of (observed - expected)² / expected over all of the cells."),
          [ch("The difference between the sample proportions of two groups, relative to the standard error of the difference", "That describes the z-statistic of a two-sample z-test."),
           ch("The distance between a sample mean and the null value, relative to the standard error of the mean", "That describes a t-statistic for a mean, which is not part of this unit."),
           ch("The total of the observed counts in the table, relative to the number of rows and columns", "The statistic is not a ratio of the total count to the size of the table.")],
          "Chi-square measures the distance between the observed and expected counts relative to the expected counts.", difficulty="medium")

    d3 = chi2_density(3, 14, [(2, "2"), (4, "4"), (6, "6"), (8, "8"), (10, "10"), (12, "12")], x_label="Chi-square value", alt="Chi-square curve with 3 degrees of freedom: it starts high near 0, skewed to the right.")
    B.mcq(T, "The graph shows a chi-square distribution with 3 degrees of freedom. Which of the following is true of chi-square distributions?",
          ch("They take only positive values and are skewed to the right; the skew is less pronounced as the degrees of freedom increase", "A chi-square distribution has positive values and is skewed right."),
          [ch("They take positive and negative values and are symmetric about 0, like the standard normal distribution", "Chi-square values are sums of squares, so they cannot be negative, and the curve is skewed."),
           ch("They take only positive values and are skewed to the left; the skew is more pronounced as the degrees of freedom of the test increase", "The distribution is skewed right, and the skew lessens with more degrees of freedom."),
           ch("They take only positive values and are symmetric, with a mean that equals the number of observations in the table", "The distribution is skewed right, and its mean is the degrees of freedom, not the number of observations.")],
          "Chi-square curves are skewed right with positive values; the skew lessens as the degrees of freedom increase.", diagram=d3, difficulty="medium")

    B.mcq(T, "A researcher randomly selects one group of 400 adults from a city, and records for each adult both the age group (18 to 34, 35 to 54, 55 or over) and the preferred way of getting news (online, television, print). The researcher wants to know whether age group and preferred way of getting news are associated in the city. Which test is appropriate?",
          ch("A chi-square test for independence, since there is one random sample and two categorical variables measured on each adult", "The test for independence is used to determine whether two categorical variables are associated in a single population."),
          [ch("A chi-square test for homogeneity, since the adults are divided into three age groups", "The test for homogeneity is for independent samples from different populations or treatment groups. Here there is one sample."),
           ch("A two-sample z-test for the difference between two proportions, since there are two categorical variables measured on each adult", "There are more than two categories, so a chi-square test is needed."),
           ch("A one-sample z-test for a population proportion, since each adult has one preferred way", "There are two variables and several categories, not one proportion.")],
          "One random sample with two categorical variables: a test for independence.", difficulty="medium")

    B.mcq(T, "A teacher randomly selects 100 students from each of three grade levels in a large school district, and asks each student to choose a favorite subject (math, science, or English). The teacher wants to know whether the distribution of favorite subject is the same in the three grade levels. Which test is appropriate?",
          ch("A chi-square test for homogeneity, since there are independent random samples from three populations and one categorical variable", "The test for homogeneity compares the distribution of a categorical variable across populations."),
          [ch("A chi-square test for independence, since the students are divided into three grade levels", "The samples were selected separately from each grade level, which is the design for a test of homogeneity."),
           ch("A two-sample z-test for the difference between two proportions, since there are three groups of students to compare in the district", "There are three groups and three categories, so a chi-square test is needed."),
           ch("A two-sample z-interval, since the teacher wants to compare the three grade levels", "An interval for a difference in proportions is for two groups and one category.")],
          "Independent random samples from several populations: a test for homogeneity.", difficulty="medium")

    B.mcq(T, "A chi-square test for homogeneity is used to compare the distribution of a categorical variable across three populations. Which of the following are the correct hypotheses?",
          ch("H₀: there is no difference in the distribution of the categorical variable across the three populations; Hₐ: there is a difference in the distribution across the populations", "These are the hypotheses for homogeneity."),
          [ch("H₀: the categorical variable is associated with the three populations; Hₐ: the categorical variable is not associated with the three populations", "The null hypothesis states no difference (no association)."),
           ch("H₀: the three population proportions of every category are different; Hₐ: the three population proportions are equal", "The null hypothesis states that the distributions are the same."),
           ch("H₀: μ₁ = μ₂ = μ₃; Hₐ: at least one mean is different", "The variable is categorical, so the hypotheses are about distributions, not means.")],
          "Homogeneity: H0 no difference in the distributions; Ha a difference.", difficulty="medium")

    B.mcq(T, "A chi-square test for independence is used with one random sample of adults to study age group and preferred way of getting news. Which of the following are the correct hypotheses?",
          ch("H₀: there is no association between age group and preferred way of getting news in the population; Hₐ: there is an association between them", "These are the hypotheses for independence."),
          [ch("H₀: there is an association between age group and preferred way of getting news in the population; Hₐ: there is no association between them", "The null hypothesis states no association."),
           ch("H₀: age group and preferred way of getting news are the same variable; Hₐ: they are different variables", "The hypotheses are about whether the variables are associated, not about whether they are the same."),
           ch("H₀: the sample proportions of every cell of the table are equal; Hₐ: some sample proportions are different", "Hypotheses are about the population, not about sample proportions.")],
          "Independence: H0 no association in the population; Ha an association.", difficulty="medium")

    B.mcq(T, "Which condition is required for a chi-square test for homogeneity or independence, and is checked using the expected counts?",
          ch("All expected counts should be greater than 5", "The expected counts condition uses the expected counts, from the row and column totals."),
          [ch("All observed counts should be greater than 5 in the table", "The condition is on the expected counts, not on the observed counts."),
           ch("All expected counts should be exactly equal to each other", "Expected counts need not be equal."),
           ch("At least 10 expected successes and 10 expected failures should be in the first row", "That is the style of the condition for a z-test for a proportion, not for a chi-square test.")],
          "Chi-square tests need all expected counts greater than 5.", difficulty="easy")

    ex_small = [[4, 9], [12, 25]]
    kx = chi_square(ex_small)
    B.mcq(T, "A student plans a chi-square test using the observed counts 4 and 9 in the first row, and 12 and 25 in the second row of a 2 by 2 table. Which of the following is correct about the expected counts condition?",
          ch(f"The condition is not met, because the expected count in the first row and first column is about {kx.expected[0][0]:.2f}, which is not greater than 5", "Expected = (row total)(column total) / table total = 13(16) / 50."),
          [ch("The condition is met, because the total of all of the counts, 50, is large", "The condition applies to each expected count, not only to the total."),
           ch("The condition is met, because all of the observed counts except one are greater than 5", "The condition is about the expected counts, and one of them is less than 5."),
           ch(f"The condition is not met, because the expected counts are different from the observed counts", "Expected counts are always different from the observed counts. The condition is that each is greater than 5.")],
          f"The smallest expected count is {kx.expected.min():.2f}, which is not greater than 5.", difficulty="hard")

    B.mcq(T, "In a randomized experiment, 90 volunteers are randomly assigned to one of three diets, 30 per diet. The proportions who reach a weight goal are compared with a chi-square test for homogeneity. Which condition is not needed?",
          ch("The 10% condition, since the data come from a randomized experiment", "For an experiment, the 10% condition is unnecessary."),
          [ch("The randomization condition, since the treatments must be randomly assigned", "The treatments must be randomly assigned."),
           ch("The expected counts condition, since all expected counts should be greater than 5", "The expected counts condition is required."),
           ch("The condition that the variable is categorical, since a chi-square test is for categorical data", "A chi-square test is for categorical variables.")],
          "The 10% condition is unnecessary when the data are from a randomized experiment.", difficulty="medium")

    B.mcq(T, "A researcher randomly assigns 150 patients to one of three treatments, 50 per treatment, and records whether each patient improved, stayed the same, or got worse. Which of the following is the best choice of test for the question \"Is the distribution of the outcome the same for the three treatments?\"",
          ch("A chi-square test for homogeneity", "The treatments are randomly assigned, and the distribution of one categorical variable is compared across treatments."),
          [ch("A chi-square test for independence", "The groups were formed by random assignment to treatments, which is the setting of a test for homogeneity."),
           ch("A two-sample z-test for a difference in proportions", "There are three treatments and three outcomes."),
           ch("A one-sample z-interval for a population proportion", "The question compares distributions across treatments, not one proportion.")],
          "A randomized experiment comparing a distribution across treatments: homogeneity.", difficulty="medium")

    # ------------------------------------------------------------------------------------------------------------ 3.15
    T = 15
    obs = [[30, 50, 20], [20, 50, 30]]
    kk = chi_square(obs)
    tb = twoway("Group", ["Online", "Television", "Print"], ["Group 1", "Group 2"], obs, caption="Observed counts of the main way of getting news")
    B.mcq(T, "The table shows the observed counts of the main way of getting news for two groups of adults. For a chi-square test, what is the expected count for Group 1 and Online, assuming the null hypothesis is true?",
          ch("25", "Expected count = (row total)(column total) / table total = (100)(50) / 200."),
          [ch("30", "This is the observed count for that cell, not the expected count."),
           ch("50", "This is the column total for Online, not the expected count of one cell."),
           ch("100", "This is the row total for Group 1, not the expected count of one cell.")],
          "Expected = 100 × 50 / 200 = 25.", diagram=tb, difficulty="medium")

    B.mcq(T, f"The table shows the observed counts of the main way of getting news for two groups of adults. A chi-square test of homogeneity has expected counts of 25, 50 and 25 in each row. What is the value of the chi-square statistic?",
          ch(f"{kk.chi2:.2f}", "χ² = Σ (observed - expected)² / expected = 2[(30 - 25)²/25 + (50 - 50)²/50 + (20 - 25)²/25]."),
          [ch(f"{kk.chi2 / 2:.2f}", "This adds the terms for one row only. All six cells are included."),
           ch(f"{sum(abs(o - e) / e for o, e in zip(np.array(obs).ravel(), kk.expected.ravel())):.2f}", "This uses |observed - expected| / expected, without squaring the differences."),
           ch(f"{sum((o - e) ** 2 for o, e in zip(np.array(obs).ravel(), kk.expected.ravel())):.2f}", "This adds the squared differences and does not divide by the expected counts.")],
          f"χ² = {kk.chi2:.2f}.", diagram=tb, difficulty="medium")

    B.mcq(T, "A chi-square test for independence is carried out with a two-way table that has 3 rows and 4 columns. How many degrees of freedom does the test have?",
          ch("6", "df = (number of rows - 1)(number of columns - 1) = (3 - 1)(4 - 1)."),
          [ch("12", "This is the number of cells, 3 × 4."),
           ch("7", "This is 3 + 4, the number of rows plus the number of columns, and not (rows - 1)(columns - 1)."),
           ch("11", "This is the number of cells minus 1, which is the number of degrees of freedom for a different test.")],
          "df = (3 - 1)(4 - 1) = 6.", difficulty="easy")

    chi, dff = 9.0, 3
    pchi = float(sps.chi2.sf(chi, dff))
    d9 = chi2_density(dff, 16, [(chi, "9.0")], shade=[(chi, 16)], x_label="Chi-square value", alt="Chi-square curve with 3 degrees of freedom with the area to the right of 9.0 shaded.")
    B.mcq(T, "A chi-square test has a test statistic of 9.0 and 3 degrees of freedom. The graph shows the area to the right of 9.0 under the chi-square curve. Which of the following is the p-value?",
          ch(f3(pchi), "The p-value is the area to the right of the test statistic under the chi-square curve with 3 degrees of freedom."),
          [ch(f3(1 - pchi), "This is the area to the left of 9.0, not the tail probability."),
           ch(f3(2 * pchi), "This doubles the area. A chi-square test uses only the right tail."),
           ch(f3(float(sps.chi2.sf(chi, 8))), "This uses 8 degrees of freedom, but the test has 3.")],
          f"p-value = P(χ² ≥ 9.0) with df = 3, about {f3(pchi)}.", diagram=d9, difficulty="medium")

    B.mcq(T, "A chi-square test for homogeneity of the distribution of a favorite subject across three grade levels has a p-value of 0.021. Which of the following is the correct interpretation of the p-value?",
          ch("Assuming that the distribution of favorite subject is the same in the three grade levels, the probability of getting a chi-square statistic at least as large as the one observed is 0.021", "The p-value is computed assuming that the null hypothesis is true."),
          [ch("The probability that the distribution of favorite subject is the same in the three grade levels is 0.021", "The p-value is not the probability that the null hypothesis is true."),
           ch("Assuming that the distributions of favorite subject are different in the three grade levels, the probability of getting the observed chi-square statistic is 0.021", "The p-value is computed assuming that the null hypothesis, of no difference, is true."),
           ch("About 2.1% of the students have a favorite subject that is different from the other students in their grade level", "The p-value is not a percent of the students.")],
          "p-value: computed assuming H0 is true.", difficulty="medium")

    B.mcq(T, "A chi-square test for homogeneity of the distribution of a favorite subject across three grade levels, using independent random samples from each grade level, has a p-value of 0.021. At the 0.05 significance level, which of the following is the best conclusion?",
          ch("There is convincing statistical evidence that the distribution of favorite subject is different for at least one of the three grade levels", "The p-value is less than 0.05, so reject H0: the distributions are not all the same."),
          [ch("There is convincing statistical evidence that the distribution of favorite subject is different for every pair of the three grade levels of students", "The test does not say which grade levels differ, only that the distributions are not all the same."),
           ch("There is not convincing statistical evidence that the distribution of favorite subject is different in the grade levels", "The p-value is less than 0.05, so the evidence is convincing."),
           ch("It has been proved that grade level causes the favorite subject of a student", "The data are from random samples, not an experiment, and a test does not prove a claim.")],
          "Reject H0: the distributions of favorite subject are not all the same.", difficulty="medium")

    B.mcq(T, "A chi-square test for independence, using one random sample of 300 adults from a city, tests whether age group and the preferred way of getting news are associated. The p-value is 0.34. At the 0.05 significance level, which of the following is the best conclusion?",
          ch("There is not convincing statistical evidence of an association between age group and preferred way of getting news for the adults in the city", "The p-value is greater than 0.05: fail to reject H0."),
          [ch("There is convincing statistical evidence that age group and preferred way of getting news are independent for the adults in the city", "A test cannot show that the null hypothesis is true."),
           ch("There is convincing statistical evidence of an association between age group and preferred way of getting news for all of the adults in the city", "The p-value is greater than 0.05, so the evidence is not convincing."),
           ch("There is convincing statistical evidence that the adults in the sample have no association between the two variables", "The conclusion should be about the population, and failing to reject does not show that there is no association.")],
          "p-value 0.34 > 0.05: fail to reject H0; no convincing evidence of an association.", difficulty="medium")

    rows = [[45, 15], [20, 30]]
    kr = chi_square(rows)
    contrib = kr.contrib
    flat = sorted(contrib.ravel())
    assert int(contrib.argmax()) == 3 and flat[-1] - flat[-2] > 0.5, contrib
    tb2 = twoway("Group", ["Improved", "Did not improve"], ["Treatment 1", "Treatment 2"], rows, caption="Results of a randomized experiment")
    E = kr.expected
    B.mcq(T, f"The table shows the results of a randomized experiment with two treatments. A chi-square test has expected counts of {E[0][0]:.1f}, {E[0][1]:.1f}, {E[1][0]:.1f} and {E[1][1]:.1f}, in the order of the cells of the table. Which cell contributes the most to the chi-square statistic?",
          ch("Treatment 2 and Did not improve", f"({rows[1][1]} - {E[1][1]:.1f})\u00b2 / {E[1][1]:.1f} = {contrib[1][1]:.2f} is the largest contribution."),
          [ch("Treatment 1 and Improved", f"Its contribution is ({rows[0][0]} - {E[0][0]:.1f})\u00b2 / {E[0][0]:.1f} = {contrib[0][0]:.2f}, which is smaller."),
           ch("Treatment 1 and Did not improve", f"Its contribution is ({rows[0][1]} - {E[0][1]:.1f})\u00b2 / {E[0][1]:.1f} = {contrib[0][1]:.2f}, which is smaller."),
           ch("Treatment 2 and Improved", f"Its contribution is ({rows[1][0]} - {E[1][0]:.1f})\u00b2 / {E[1][0]:.1f} = {contrib[1][0]:.2f}, which is smaller.")],
          "Compare (observed - expected)\u00b2 / expected for each cell: the largest is for Treatment 2 and Did not improve.", diagram=tb2, difficulty="hard")

    B.mcq(T, "In a randomized experiment, a chi-square test for homogeneity is used to compare the distribution of the outcome (improved, same, worse) for two treatments. The test has a p-value of 0.003. Which of the following is the best conclusion?",
          ch("There is convincing statistical evidence that the distribution of the outcome is different for the two treatments, and random assignment supports a cause-and-effect conclusion for individuals like those in the experiment", "The p-value is small and the treatments were randomly assigned."),
          [ch("There is only evidence of an association between the treatment and the outcome, because the volunteers chose to take part in the experiment", "Random assignment of the treatments allows a cause-and-effect conclusion."),
           ch("There is convincing statistical evidence that the distribution of the outcome is the same for the two treatments", "A small p-value is evidence for a difference, not for sameness."),
           ch("There is not convincing statistical evidence, because the p-value is not exactly 0", "The p-value is less than any usual significance level, so the evidence is convincing.")],
          "Small p-value and random assignment: convincing evidence of a difference caused by the treatment.", difficulty="medium")

    big = [[18, 12, 20], [22, 28, 20]]
    kb = chi_square(big)
    B.mcq(T, f"A chi-square test for independence of two categorical variables in one random sample gives a test statistic of {kb.chi2:.2f} with {kb.df} degrees of freedom, and a p-value of {f3(kb.p)}. At the 0.05 significance level, which of the following is the correct decision and its meaning?",
          ch(f"Fail to reject the null hypothesis, because the p-value {f3(kb.p)} is greater than 0.05; there is not convincing evidence of an association", "A p-value greater than α means fail to reject H0."),
          [ch(f"Reject the null hypothesis, because the test statistic {kb.chi2:.2f} is greater than the degrees of freedom {kb.df}; there is convincing evidence of an association", "The decision compares the p-value with α, not the statistic with the degrees of freedom."),
           ch(f"Reject the null hypothesis, because the p-value {f3(kb.p)} is less than 1; there is convincing evidence of an association", "The decision compares the p-value with α, which is 0.05."),
           ch(f"Fail to reject the null hypothesis, because the p-value {f3(kb.p)} is greater than 0.05; this proves that the variables are independent", "Failing to reject does not prove the null hypothesis.")],
          f"p-value {f3(kb.p)} > 0.05: fail to reject H0.", difficulty="medium")
