"""Writes content/ap-statistics/refreshers/unit-3.json (15 refreshers, one per topic). Layout: ### The idea, ### Key facts, ### Watch out for, ### Worked example.
Facts are the CED's essential knowledge for each topic (effective Fall 2026); every number in a worked example is asserted. No single-asterisk italics (write the critical value as $z^*$), no lone dollar sign, no em dashes.
Edit this script, not the JSON. Run: python3 u3_refreshers.py"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import refreshers_lib
import numpy as np
from scipy import stats as sps

from lib import check_markdown, prop_ci, prop_z, two_prop_ci, two_prop_z, chi_square

# 3.2
assert abs(math.sqrt(0.30 * 0.70 / 100) - 0.0458) < 1e-4
# 3.3
c = prop_ci(172, 400, 0.95)
assert (round(c.lo, 3), round(c.hi, 3)) == (0.381, 0.479)
assert math.ceil(1.96 ** 2 * 0.25 / 0.04 ** 2) == 601
# 3.7
t = prop_z(71, 150, 0.40, "gt")
assert abs(t.z - 1.83) < 0.01 and abs(t.p - 0.0336) < 1e-3
# 3.9 / 3.10
assert abs(math.sqrt(0.6 * 0.4 / 200 + 0.5 * 0.5 / 250) - 0.0469) < 1e-3
d = two_prop_ci(132, 220, 105, 240, 0.95)
assert (round(d.lo, 3), round(d.hi, 3)) == (0.072, 0.253)
# 3.13
tz = two_prop_z(52, 80, 38, 80, "gt")
assert abs(tz.pc - 0.5625) < 1e-9 and abs(tz.z - 2.23) < 0.01
# 3.15
k = chi_square([[60, 25, 15], [45, 35, 20], [25, 35, 40]])
assert k.df == 4 and abs(k.expected[0][0] - 43.333) < 1e-2 and k.p < 0.01

ENTRIES = [
("estimators", r"""
### The idea
A sample statistic is used to estimate the value of a population parameter. A **point estimator** is a statistic that gives one number as the estimate.

### Key facts
- The sample proportion $\hat{p}$ is a point estimator for the population proportion $p$. The sample mean $\bar{x}$ is a point estimator for the population mean $\mu$.
- An estimator is **unbiased** if, on average over repeated random samples, it does not underestimate or overestimate the parameter. The center of its sampling distribution is the parameter.
- An unbiased estimator still varies from sample to sample: one value from one sample usually differs from the parameter.
- A **biased** estimator is consistently too large or too small on average.

### Watch out for
"Unbiased" does not mean "equal to the parameter in my sample." It describes the estimator's long-run behavior. And a bigger sample does not fix bias that comes from the way the sample was chosen.

### Worked example
Prompt: "Many random samples of size 50 are taken from a population with $p = 0.30$. The mean of all of the sample proportions is 0.301. Is $\hat{p}$ a biased estimator?"

The center of the sampling distribution is very close to $p = 0.30$ (the small difference is chance in the simulation), so $\hat{p}$ appears to be unbiased.
"""),
("sampling-distributions-for-sample-proportions", r"""
### The idea
The **sampling distribution of $\hat{p}$** describes how the sample proportion varies from one random sample of size $n$ to another.

### Key facts
- When the sampled values are independent, the mean is $\mu_{\hat{p}} = p$ and the standard deviation is $\sigma_{\hat{p}} = \sqrt{\dfrac{p(1 - p)}{n}}$.
- Conditions: the data are a **random sample**; the **10% condition**, $n \le N/10$ when sampling without replacement; and the **large counts condition**, $np \ge 10$ and $n(1 - p) \ge 10$, so that the shape is approximately normal.
- Quadrupling the sample size cuts the standard deviation in half, because $\sigma_{\hat{p}}$ is proportional to $1/\sqrt{n}$.
- Interpret the standard deviation in context: the typical distance between the sample proportion and $p$ in random samples of that size.

### Watch out for
The standard deviation uses the population proportion $p$, not $\hat{p}$ (that comes in for intervals). And check the counts with $p$, not with the sample.

### Worked example
Prompt: "A population has $p = 0.30$. Find the mean and the standard deviation of $\hat{p}$ for samples of size 100."

$\mu_{\hat{p}} = 0.30$ and $\sigma_{\hat{p}} = \sqrt{0.30(0.70)/100} \approx 0.0458$. The counts $100(0.30) = 30$ and $100(0.70) = 70$ are both at least 10, so the shape is approximately normal.
"""),
("constructing-a-confidence-interval-for-a-population-proportion", r"""
### The idea
A **confidence interval** is an interval estimate for a parameter. For a proportion, the procedure is a **one-sample z-interval for a population proportion**.

### Key facts
- The parameter names the proportion, the response variable and the population in context.
- Conditions: a **random sample**; the **10% condition**; and at least 10 **observed** successes and 10 observed failures, $n\hat{p} \ge 10$ and $n(1 - \hat{p}) \ge 10$.
- The interval is $\hat{p} \pm z^* \sqrt{\dfrac{\hat{p}(1 - \hat{p})}{n}}$. The critical value $z^*$ encloses the middle C% of the standard normal distribution: 1.645 for 90%, 1.960 for 95%, 2.576 for 99%.
- The **standard error** $\sqrt{\hat{p}(1 - \hat{p})/n}$ estimates the standard deviation of $\hat{p}$. The **margin of error** is $z^*$ times the standard error, half the width of the interval.
- To get a margin of error of at most MOE: $n \ge \left(\dfrac{z^*}{\text{MOE}}\right)^2 \hat{p}(1 - \hat{p})$. If $\hat{p}$ is unknown, use $\hat{p} = 0.5$ and round up.

### Watch out for
Round the sample size **up**. And for an interval, use the observed counts; for a test, use the null value.

### Worked example
Prompt: "In a random sample of 400 adults, 172 ride a bus weekly. Find a 95% interval."

$\hat{p} = 0.43$, SE $= \sqrt{0.43(0.57)/400} \approx 0.0248$, margin of error $= 1.96(0.0248) \approx 0.0485$. The interval is $(0.381, 0.479)$.
"""),
("justifying-a-claim-based-on-a-confidence-interval-for-a-population-proportion", r"""
### The idea
A confidence interval is a range of **plausible values** for the parameter. We interpret it, and the confidence level, in context, and we use it to judge a claim.

### Key facts
- **Interpretation of the interval:** "We are C% confident that the interval from $a$ to $b$ contains the proportion of all (population) who (context)."
- **Interpretation of the confidence level:** in repeated random sampling with the same sample size, approximately C% of the intervals will capture the population proportion. The method succeeds C% of the time; any one interval either contains the parameter or does not.
- A value **inside** the interval is plausible; a value **outside** is not plausible, which can be convincing evidence against a claim about that value.
- Higher confidence level: larger $z^*$, larger margin of error, **wider** interval. Larger sample size: smaller standard error, **narrower** interval (the width is roughly proportional to $1/\sqrt{n}$).

### Watch out for
Do not say "there is a 95% probability that the parameter is in the interval," and do not say that 95% of the data are in the interval. The interval estimates the parameter.

### Worked example
Prompt: "A 95% interval for the proportion of voters who support a measure is $(0.46, 0.54)$. Is there convincing evidence that a majority support it?"

No. The interval includes values below 0.50 (and 0.50 itself), so a majority has not been shown.
"""),
("setting-up-a-test-for-a-population-proportion", r"""
### The idea
A **hypothesis test** uses a sample to decide about a claim for a population parameter. For one proportion, the procedure is a **one-sample z-test**.

### Key facts
- The **null hypothesis** $H_0$ is the status quo, assumed correct unless the evidence is convincing. It contains an equality: $H_0\!: p = p_0$.
- The **alternative hypothesis** $H_a$ is the claim for which evidence is collected: $p < p_0$, $p > p_0$ (one-sided) or $p \ne p_0$ (two-sided).
- Define the parameter in context: the proportion of all (population) who (context). Hypotheses are about the **parameter**, never about $\hat{p}$.
- Conditions: a random sample; the 10% condition; and the **expected** counts $np_0 \ge 10$ and $n(1 - p_0) \ge 10$ (use the null value, since the test assumes $H_0$ is true).

### Watch out for
The direction of $H_a$ comes from the researcher's claim, written before looking at the data. And the large counts condition for a test uses $p_0$; for an interval it uses $\hat{p}$.

### Worked example
Prompt: "A manufacturer says that at most 5% of its bulbs are defective. An inspector thinks the proportion is higher. A sample of 150 bulbs is planned. State the hypotheses and check the counts."

$H_0\!: p = 0.05$, $H_a\!: p > 0.05$. But $np_0 = 150(0.05) = 7.5 < 10$, so the large counts condition is not met.
"""),
("p-values", r"""
### The idea
The **p-value** measures how surprising the sample result would be if the null hypothesis were true.

### Key facts
- The p-value is the probability, **assuming $H_0$ is true**, of getting a test statistic as extreme or more extreme (in the direction of $H_a$) than the one observed.
- For $H_a\!: p > p_0$ it is the area to the right of $z$; for $p < p_0$, the area to the left; for $p \ne p_0$, **both tails** (twice the smaller tail).
- If the null distribution is simulated, the p-value is the **proportion** of simulated values at least as extreme as the observed one.
- A **small p-value** means the result would be unusual if $H_0$ were true, which is evidence for $H_a$. A **large p-value** is not convincing evidence for $H_a$, and it is **not** evidence that $H_0$ is true.

### Watch out for
The p-value is not the probability that $H_0$ is true, and it is not the probability that the result is due to chance. It is a probability about the data, computed assuming $H_0$.

### Worked example
Prompt: "A test has $z = 2.10$. Find the p-value for $H_a\!: p > p_0$ and for $H_a\!: p \ne p_0$."

$P(z \ge 2.10) \approx 0.0179$ for the one-sided test. For the two-sided test, $2(0.0179) \approx 0.0357$.
"""),
("carrying-out-a-test-for-a-population-proportion", r"""
### The idea
To carry out a test, calculate the test statistic and the p-value, compare the p-value with the significance level, and state a conclusion in context.

### Key facts
- Test statistic: $z = \dfrac{\hat{p} - p_0}{\sqrt{p_0(1 - p_0)/n}}$. It has a standard normal distribution when $H_0$ is true.
- The **significance level** $\alpha$ is chosen in advance (for example 0.05). If the p-value is less than $\alpha$, **reject** $H_0$; otherwise **fail to reject** $H_0$.
- Rejecting $H_0$ means convincing statistical evidence for $H_a$. Failing to reject means **not** convincing evidence for $H_a$; it never proves that $H_0$ is true.
- A conclusion is written in context, in terms of $H_a$, with non-definitive language, and names the parameter and the population.

### Watch out for
Do not choose $\alpha$ after seeing the p-value. And do not write "accept $H_0$" or "prove."

### Worked example
Prompt: "A random sample of 150 members shows 71 who renewed. Test $H_0\!: p = 0.40$ against $H_a\!: p > 0.40$ at $\alpha = 0.05$."

$\hat{p} = 0.473$ and $z = (0.473 - 0.40)/\sqrt{0.40(0.60)/150} \approx 1.83$, so the p-value is about $0.034 < 0.05$. Reject $H_0$: there is convincing evidence that the proportion of all members who renew is greater than 0.40.
"""),
("potential-errors-when-performing-tests", r"""
### The idea
A test can lead to a wrong decision. There are two ways to be wrong.

### Key facts
- A **Type I error**: convincing evidence for $H_a$, but $H_a$ is not true (rejecting a true $H_0$). Its probability is the significance level $\alpha$.
- A **Type II error**: no convincing evidence for $H_a$, but $H_a$ is true (failing to reject a false $H_0$). Its probability is $1 - \text{power}$.
- The **power** is the probability that the test correctly rejects a false null hypothesis.
- Power increases (and the probability of a Type II error decreases) when the **sample size** increases, the **standard error** decreases, the true parameter is **farther** from the null value, or $\alpha$ is **larger**.
- Consider the consequences of each error. The consequences of a Type I error guide the choice of $\alpha$; the consequences of a Type II error guide the sample size.

### Watch out for
Always describe an error **in context**, not just by name. And lowering $\alpha$ lowers the chance of a Type I error but raises the chance of a Type II error.

### Worked example
Prompt: "Test $H_0\!: p = 0.10$ against $H_a\!: p > 0.10$ for the proportion of patients with a side effect. Describe each error."

Type I: conclude that the proportion with the side effect is greater than 0.10 when it is actually 0.10. Type II: conclude that there is not convincing evidence that it is greater than 0.10 when it actually is.
"""),
("sampling-distributions-for-the-difference-between-sample-proportions", r"""
### The idea
When two populations (or two treatment groups) are compared, the statistic is the difference of the sample proportions, $\hat{p}_1 - \hat{p}_2$.

### Key facts
- For independent samples, the mean is $\mu = p_1 - p_2$ and the standard deviation is $\sigma = \sqrt{\dfrac{p_1(1 - p_1)}{n_1} + \dfrac{p_2(1 - p_2)}{n_2}}$. Variances add; standard deviations do not.
- Conditions: **two independent random samples**, each at most 10% of its population; or a **randomized experiment** (random assignment is the only randomization condition, and the 10% condition is not needed).
- The shape is approximately normal if $n_1p_1$, $n_1(1 - p_1)$, $n_2p_2$ and $n_2(1 - p_2)$ are all at least 10.
- Interpret in context, for two specific populations.

### Watch out for
The mean of the difference is a difference, not a sum. And the standard deviation is the square root of the **sum of the variances**.

### Worked example
Prompt: "Independent samples: $p_1 = 0.60$, $n_1 = 200$ and $p_2 = 0.50$, $n_2 = 250$. Find the mean and standard deviation of $\hat{p}_1 - \hat{p}_2$."

$\mu = 0.10$ and $\sigma = \sqrt{0.60(0.40)/200 + 0.50(0.50)/250} = \sqrt{0.0012 + 0.0010} \approx 0.0469$.
"""),
("constructing-a-confidence-interval-for-the-difference-between-two-population-proportions", r"""
### The idea
To estimate the difference between two population proportions, use a **two-sample z-interval for a difference between proportions**.

### Key facts
- The parameter is $p_1 - p_2$: the difference between the proportion of (population 1) and the proportion of (population 2) who (context).
- Conditions: two independent random samples (or a randomized experiment); the 10% condition for each sample (not needed for an experiment); and at least 10 **observed** successes and failures in **both** samples.
- The point estimate is $\hat{p}_1 - \hat{p}_2$. The interval is $(\hat{p}_1 - \hat{p}_2) \pm z^* \sqrt{\dfrac{\hat{p}_1(1 - \hat{p}_1)}{n_1} + \dfrac{\hat{p}_2(1 - \hat{p}_2)}{n_2}}$.
- The standard error is the square root in that formula; the margin of error is $z^*$ times it.

### Watch out for
Write the difference in the same order as the parameter is defined. And use the separate sample proportions in the standard error, not a combined proportion (that is for tests).

### Worked example
Prompt: "School A: 132 of 220 favor a later start. School B: 105 of 240. Find a 95% interval for $p_1 - p_2$."

$\hat{p}_1 = 0.600$, $\hat{p}_2 = 0.4375$. SE $= \sqrt{0.6(0.4)/220 + 0.4375(0.5625)/240} \approx 0.046$, so the interval is $0.1625 \pm 1.96(0.046) = (0.072, 0.253)$.
"""),
("justifying-a-claim-based-on-a-confidence-interval-for-the-difference-between-two-population-proportions", r"""
### The idea
An interval for $p_1 - p_2$ is interpreted in context, and it can support a claim about whether the two proportions differ.

### Key facts
- **Interpretation:** "We are C% confident that the interval from $a$ to $b$ contains the difference between the proportion of (population 1) and the proportion of (population 2) who (context)."
- The **confidence level** means that in repeated random sampling with the same sample sizes, about C% of such intervals capture the difference.
- If the interval **contains 0**, there is not convincing evidence of a difference. If it does **not** contain 0, there is convincing evidence of a difference; all positive values mean $p_1 > p_2$, all negative values mean $p_1 < p_2$.
- From a **randomized experiment**, a difference that is convincing can be attributed to the treatments (cause and effect), for individuals like those in the study.

### Watch out for
An interval that contains 0 does not show that the proportions are equal; it only fails to show a difference. And observational data allow an association, not cause and effect.

### Worked example
Prompt: "A 95% interval for $p_1 - p_2$ is $(0.06, 0.18)$. What do you conclude?"

0 is not in the interval and every value is positive, so there is convincing evidence that $p_1 > p_2$.
"""),
("setting-up-a-test-for-the-difference-between-two-population-proportions", r"""
### The idea
To test whether two population proportions differ, use a **two-sample z-test for the difference between two proportions**.

### Key facts
- $H_0\!: p_1 = p_2$ (or $p_1 - p_2 = 0$), the status quo of no difference. $H_a$ is $p_1 - p_2 > 0$, $< 0$ or $\ne 0$, matching the claim. Define $p_1$ and $p_2$ in context, for the populations.
- Conditions: two independent random samples (or a randomized experiment); the 10% condition for each (not needed for an experiment); and the large counts condition with the **combined (pooled) proportion** $\hat{p}_c = \dfrac{x_1 + x_2}{n_1 + n_2}$: $n_1\hat{p}_c$, $n_1(1 - \hat{p}_c)$, $n_2\hat{p}_c$ and $n_2(1 - \hat{p}_c)$ all at least 10.
- Under $H_0$ the two populations share one proportion, which is why the combined proportion is used.

### Watch out for
Hypotheses are about the parameters $p_1$ and $p_2$, not $\hat{p}_1$ and $\hat{p}_2$. And a one-sided alternative must match the order in which the groups are defined.

### Worked example
Prompt: "In an experiment, 45 of 100 patients improve with a medicine and 30 of 100 improve with a placebo. Find $\hat{p}_c$."

$\hat{p}_c = (45 + 30)/(100 + 100) = 0.375$. Then $100(0.375) = 37.5$ and $100(0.625) = 62.5$ are both at least 10.
"""),
("carrying-out-a-test-for-the-difference-between-two-population-proportions", r"""
### The idea
Calculate the test statistic with the combined proportion, find the p-value, compare it with $\alpha$, and state a conclusion in context.

### Key facts
- Test statistic: $z = \dfrac{\hat{p}_1 - \hat{p}_2}{\sqrt{\hat{p}_c(1 - \hat{p}_c)\left(\dfrac{1}{n_1} + \dfrac{1}{n_2}\right)}}$, standard normal when $H_0$ is true.
- The p-value is the probability, assuming the two population proportions are equal, of a difference at least as extreme as the one observed, in the direction of $H_a$.
- If the p-value is less than $\alpha$, reject $H_0$: convincing evidence for $H_a$. Otherwise fail to reject.
- The conclusion names the parameters and the populations, in terms of $H_a$. For a randomized experiment, a convincing difference supports a **cause-and-effect** conclusion for individuals like those in the study; for random samples, only a conclusion about the populations.

### Watch out for
A test uses the combined proportion in the standard error, while an interval uses the separate proportions. And do not generalize beyond the volunteers or populations that were sampled.

### Worked example
Prompt: "52 of 80 students with an app pass, and 38 of 80 with a notebook pass (random assignment). Test $H_a\!: p_1 - p_2 > 0$."

$\hat{p}_c = 90/160 = 0.5625$, $z = 0.175/\sqrt{0.5625(0.4375)(2/80)} \approx 2.23$, so the p-value is about 0.013. Reject $H_0$: convincing evidence that the app causes a greater proportion of students like these to pass.
"""),
("setting-up-a-chi-square-test-for-homogeneity-or-independence", r"""
### The idea
A **chi-square test** compares observed counts in a two-way table with the counts expected if the null hypothesis were true.

### Key facts
- The **chi-square statistic** measures the distance between the observed and the expected counts, relative to the expected counts. Chi-square distributions take only positive values and are **skewed right**; the skew lessens as the degrees of freedom increase.
- **Homogeneity:** compares the distribution of one categorical variable across two or more populations or treatments (independent random samples, or a randomized experiment). $H_0$: no difference in the distributions. $H_a$: a difference.
- **Independence:** one random sample, two categorical variables. $H_0$: no association (independent) in the population. $H_a$: an association.
- Conditions: the randomization condition, the 10% condition (not needed for an experiment), and **all expected counts greater than 5**.

### Watch out for
Choose the test from how the data were collected, not from the table's shape. And the expected counts condition uses the **expected** counts, not the observed ones.

### Worked example
Prompt: "A teacher takes separate random samples of 100 students from each of three grade levels and records the favorite subject. Which test?"

Independent random samples from three populations and one categorical variable: a chi-square test for **homogeneity** ($H_0$: the distribution of favorite subject is the same in the three grade levels).
"""),
("carrying-out-a-chi-square-test-for-homogeneity-or-independence", r"""
### The idea
Find the expected counts, the chi-square statistic and the degrees of freedom, then the p-value, and decide.

### Key facts
- Expected count for a cell $= \dfrac{(\text{row total})(\text{column total})}{\text{table total}}$.
- $\chi^2 = \sum \dfrac{(\text{observed} - \text{expected})^2}{\text{expected}}$, summed over all cells. Degrees of freedom $= (\text{rows} - 1)(\text{columns} - 1)$.
- The p-value is the area to the **right** of $\chi^2$ under the chi-square curve with that many degrees of freedom. Interpret it assuming $H_0$ is true.
- If the p-value is less than $\alpha$, reject $H_0$; otherwise fail to reject. The conclusion is in context, about the population(s). The test says the distributions are **not all the same** (or that there is an association), not which cells differ; the cells with the largest contributions show where the data differ most.

### Watch out for
Do not use the table totals as the degrees of freedom. And a chi-square test from a randomized experiment supports cause and effect; from random samples it does not.

### Worked example
Prompt: "Age group (3 levels) by main way of getting news (3 ways), 300 adults, one random sample. Find the expected count for under 30 and online (row total 100, column total 130) and the degrees of freedom."

Expected $= 100(130)/300 \approx 43.3$ and $\text{df} = (3 - 1)(3 - 1) = 4$.
"""),
]

if __name__ == "__main__":
    for _slug, _body in ENTRIES:
        check_markdown(_body)
    refreshers_lib.write("ap-statistics", 3, ENTRIES)
