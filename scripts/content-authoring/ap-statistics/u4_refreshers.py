"""Writes content/ap-statistics/refreshers/unit-4.json (10 refreshers, one per topic). Layout: ### The idea, ### Key facts, ### Watch out for, ### Worked example.
Facts are the CED's essential knowledge for each topic (effective Fall 2026); every number in a worked example is asserted. No single-asterisk italics (write the critical value as $t^*$), no lone dollar sign, no em dashes.
Edit this script, not the JSON. Run: python3 u4_refreshers.py"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import refreshers_lib
import numpy as np
from scipy import stats as sps

from lib import check_markdown, t_ci, t_test, t2_ci, t2_test, tstar

# 4.1
assert abs(12 / math.sqrt(36) - 2) < 1e-12 and abs(sps.norm.sf(105, 100, 20 / 8) - 0.0228) < 1e-4
# 4.2
c = t_ci(48.2, 6.4, 25)
assert (round(c.lo, 2), round(c.hi, 2)) == (45.56, 50.84) and abs(tstar(0.95, 14) - 2.145) < 1e-3
# 4.5
t = t_test(52.1, 8.0, 25, 50, "gt")
assert abs(t.t - 1.3125) < 1e-9 and abs(t.p - 0.1009) < 1e-3
assert abs(2 * sps.t.sf(2.30, 24) - 0.0304) < 1e-3
# 4.6
assert abs(math.sqrt(10 ** 2 / 40 + 12 ** 2 / 50) - 2.32) < 0.01
# 4.7
d = t2_ci(24.1, 5.2, 30, 21.0, 4.8, 32)
assert (round(d.lo, 2), round(d.hi, 2)) == (0.55, 5.65)
# 4.10
w = t2_test(24.1, 5.2, 30, 21.0, 4.8, 32, "ne")
assert abs(w.t - 2.43) < 0.01 and abs(w.p - 0.018) < 0.002

ENTRIES = [
("sampling-distributions-for-sample-means", r"""
### The idea
The **sampling distribution of $\bar{x}$** describes how the sample mean varies from one random sample of size $n$ to another.

### Key facts
- When the sampled values are independent, the mean is $\mu_{\bar{x}} = \mu$ and the standard deviation is $\sigma_{\bar{x}} = \dfrac{\sigma}{\sqrt{n}}$.
- Conditions: the data are a **random sample**, and the **10% condition**, $n \le N/10$, when sampling without replacement.
- **Shape:** if the population is normal, the sampling distribution of $\bar{x}$ is normal for **any** sample size. If it is not, the sampling distribution is approximately normal when $n \ge 30$ (central limit theorem); an extremely skewed population may need a much larger $n$.
- Quadrupling $n$ halves $\sigma_{\bar{x}}$. A sample mean varies much less than a single value, so probabilities for $\bar{x}$ are very different from probabilities for one individual.
- Interpret in context: the standard deviation is the typical distance between $\bar{x}$ and $\mu$ in random samples of that size.

### Watch out for
Divide by $\sqrt{n}$, not by $n$. And do not use $\sigma$ alone for a probability about a sample mean.

### Worked example
Prompt: "Scores are approximately normal with $\mu = 100$ and $\sigma = 20$. Find the probability that the mean of a random sample of 64 scores is greater than 105."

$\sigma_{\bar{x}} = 20/\sqrt{64} = 2.5$ and $z = (105 - 100)/2.5 = 2$, so the probability is about $0.0228$. (For one score, $z = 0.25$ and the probability is about $0.40$.)
"""),
("constructing-a-confidence-interval-for-a-population-mean-or-population-mean-difference", r"""
### The idea
When $\sigma$ is unknown, a confidence interval for a mean uses the sample standard deviation $s$ and a **t-distribution**. Paired data are analyzed through their **differences**.

### Key facts
- A t-distribution is symmetric and bell-shaped with **wider tails** than the standard normal; it is identified by its **degrees of freedom**. With small df it has a lower peak and fatter tails; as df grows it approaches the standard normal.
- **One-sample t-interval for a mean:** $\bar{x} \pm t^* \dfrac{s}{\sqrt{n}}$ with $\text{df} = n - 1$. The standard error is $\text{SE} = s/\sqrt{n}$ and the margin of error is $t^* \cdot \text{SE}$.
- **Matched pairs** (two measurements on the same unit, or paired units): take the difference for each pair and use a one-sample t-interval for the **mean difference** $\mu_d$. State the order of subtraction.
- Conditions: a random sample (or randomized experiment); the 10% condition; the **sample data condition**: the population is approximately normal, or $n \ge 30$, or (if $n < 30$) the data are free of strong skewness and outliers. For matched pairs, check the differences.

### Watch out for
Do not use $1.96$ when $\sigma$ is unknown. And do not treat before-and-after data on the same people as two independent samples.

### Worked example
Prompt: "A random sample of 25 batteries has $\bar{x} = 48.2$ hours and $s = 6.4$ hours, with no strong skewness or outliers. Find a 95% interval."

$\text{SE} = 6.4/\sqrt{25} = 1.28$, $t^* = 2.064$ (df = 24), so the interval is $48.2 \pm 2.064(1.28) = (45.56, 50.84)$.
"""),
("justifying-a-claim-based-on-a-confidence-interval-for-a-population-mean-or-population-mean-difference", r"""
### The idea
An interval for a mean (or a mean difference) is a range of **plausible values**. We interpret it, and the confidence level, in context, and we use it to judge a claim.

### Key facts
- **Interpretation:** "We are C% confident that the interval from $a$ to $b$ contains the mean (population, response variable, context)." For matched pairs, it is the mean **difference**, with the order of subtraction.
- **Confidence level:** in repeated random sampling with the same sample size, about C% of the intervals capture the parameter.
- A claimed value **outside** the interval is not plausible. For a mean difference, an interval that **contains 0** gives no convincing evidence of a change; one that does **not** contain 0 does.
- Higher confidence: larger $t^*$ and a **wider** interval. Larger $n$: smaller standard error and a **narrower** interval, roughly proportional to $1/\sqrt{n}$.

### Watch out for
The interval is for the **mean**, not for individual values: it does not say that 95% of the individuals are inside. And an interval that contains the claimed value does not prove the claim.

### Worked example
Prompt: "A 95% interval for the mean difference (after minus before) in test scores is $(1.2, 4.8)$ points. What do you conclude?"

0 is not in the interval and every value is positive, so there is convincing evidence that the mean score is greater after than before.
"""),
("setting-up-a-test-for-a-population-mean-or-population-mean-difference", r"""
### The idea
To test a claim about a mean when $\sigma$ is unknown, use a **one-sample t-test**. For paired data, use a one-sample t-test on the **differences**.

### Key facts
- $H_0\!: \mu = \mu_0$ (or $H_0\!: \mu_d = 0$). $H_a$ is $\mu < \mu_0$, $\mu > \mu_0$ or $\mu \ne \mu_0$, matching the claim in the question.
- Define the parameter in context: the mean (response variable) of all (population). For a mean difference, state the order of subtraction.
- Conditions: a random sample (or randomized experiment); the 10% condition; and the sample data condition (approximately normal population, or $n \ge 30$, or, if $n < 30$, data with no strong skewness or outliers; for pairs, the differences).
- A t-test is used rather than a z-test because $\sigma$ is almost never known.

### Watch out for
Hypotheses use $\mu$, never $\bar{x}$. And with $n < 30$, look at a plot of the data: one strong outlier is enough to make the condition fail.

### Worked example
Prompt: "A cereal company claims a mean weight of 340 g. An inspector thinks it is less. State the hypotheses."

$H_0\!: \mu = 340$ and $H_a\!: \mu < 340$, where $\mu$ is the mean weight, in grams, of all of the company's boxes.
"""),
("carrying-out-a-test-for-a-population-mean-or-population-mean-difference", r"""
### The idea
Calculate the t-statistic, find the p-value from the t-distribution, compare it with $\alpha$, and write a conclusion in context.

### Key facts
- $t = \dfrac{\bar{x} - \mu_0}{s/\sqrt{n}}$ with $\text{df} = n - 1$. For paired data, use $\bar{x}_d$ and $s_d$ in the same formula with $\mu_0 = 0$.
- The **p-value** is the probability, assuming $H_0$ is true, of a t-statistic as extreme or more extreme (in the direction of $H_a$). For $H_a\!: \mu \ne \mu_0$, double the tail.
- If the p-value is at most $\alpha$, **reject** $H_0$: convincing evidence for $H_a$. Otherwise fail to reject; that is never evidence that $H_0$ is true.
- The conclusion names the parameter and the population, in terms of $H_a$, with non-definitive language. Cause and effect needs random assignment.

### Watch out for
Using the standard normal distribution for a small sample gives a p-value that is too small, because a t-distribution has wider tails.

### Worked example
Prompt: "$n = 25$, $\bar{x} = 52.1$, $s = 8.0$. Test $H_0\!: \mu = 50$ against $H_a\!: \mu > 50$."

$t = (52.1 - 50)/(8.0/5) = 1.3125$ with df = 24, and the p-value is about $0.101$. This is greater than $0.05$, so we fail to reject $H_0$: there is not convincing evidence that the mean is greater than 50.
"""),
("sampling-distributions-for-the-difference-between-two-sample-means", r"""
### The idea
To compare two groups, the statistic is $\bar{x}_1 - \bar{x}_2$. Its sampling distribution tells how this difference varies from pair to pair of random samples.

### Key facts
- For independent samples: mean $\mu_1 - \mu_2$ and standard deviation $\sqrt{\dfrac{\sigma_1^2}{n_1} + \dfrac{\sigma_2^2}{n_2}}$. Variances add; the standard deviations do not.
- Conditions: **two independent random samples**, each at most 10% of its population; or a **randomized experiment** (only the random assignment is required).
- Shape: normal if both populations are normal, and approximately normal if both $n_1 \ge 30$ and $n_2 \ge 30$.
- Interpret in context, for two specific populations.

### Watch out for
The mean of the difference is a difference of the means. And one sample size of 30 or more is not enough when the populations are not normal: **both** must be.

### Worked example
Prompt: "Independent samples: $\mu_1 = 60$, $\sigma_1 = 10$, $n_1 = 40$; $\mu_2 = 55$, $\sigma_2 = 12$, $n_2 = 50$. Describe $\bar{x}_1 - \bar{x}_2$."

The mean is $5$ and the standard deviation is $\sqrt{100/40 + 144/50} = \sqrt{5.38} \approx 2.32$.
"""),
("constructing-a-confidence-interval-for-the-difference-between-two-population-means", r"""
### The idea
To estimate the difference between two population means, use a **two-sample t-interval**.

### Key facts
- The parameter is $\mu_1 - \mu_2$: the difference between the mean (response) of (population 1) and of (population 2).
- Conditions: two independent random samples (or a randomized experiment); the 10% condition for each (not needed for an experiment); and both sample sizes at least 30, or both populations approximately normal (if either $n < 30$, **both** samples free of strong skewness and outliers).
- Interval: $(\bar{x}_1 - \bar{x}_2) \pm t^* \sqrt{\dfrac{s_1^2}{n_1} + \dfrac{s_2^2}{n_2}}$. Technology gives $t^*$ and the degrees of freedom, which fall between the smaller of $n_1 - 1$ and $n_2 - 1$ and $n_1 + n_2 - 2$.
- The standard error is the square root; the margin of error is $t^*$ times it.

### Watch out for
Use the same order for the subtraction as in the parameter. And do not add the two standard errors; add the variances, then take the square root.

### Worked example
Prompt: "School A: $n = 30$, $\bar{x} = 24.1$, $s = 5.2$. School B: $n = 32$, $\bar{x} = 21.0$, $s = 4.8$. Find a 95% interval for $\mu_1 - \mu_2$."

$\text{SE} = \sqrt{5.2^2/30 + 4.8^2/32} \approx 1.273$ and technology gives $t^* \approx 2.00$, so the interval is $3.1 \pm 2.55 = (0.55, 5.65)$.
"""),
("justifying-a-claim-based-on-a-confidence-interval-for-the-difference-between-two-population-means", r"""
### The idea
An interval for $\mu_1 - \mu_2$ is interpreted in context, and it tells whether there is convincing evidence of a difference.

### Key facts
- **Interpretation:** "We are C% confident that the interval from $a$ to $b$ contains the difference between the mean (response) of (population 1) and the mean of (population 2)."
- **Confidence level:** in repeated random sampling with the same sample sizes, about C% of such intervals capture the difference.
- If the interval **contains 0**, there is not convincing evidence of a difference. If it **does not**, there is; all positive values mean $\mu_1 > \mu_2$ and all negative values mean $\mu_1 < \mu_2$.
- Random assignment in an experiment supports a **cause-and-effect** conclusion for individuals like the participants; random samples support a conclusion about the populations only.

### Watch out for
An interval with 0 in it does not prove that the means are equal. And the interval is for the difference in means, not for the difference between individuals.

### Worked example
Prompt: "A 95% interval for $\mu_1 - \mu_2$ is $(-18.5, -4.2)$ points. What do you conclude?"

Both limits are negative, so there is convincing evidence that $\mu_1 < \mu_2$.
"""),
("setting-up-a-test-for-the-difference-between-two-population-means", r"""
### The idea
To test whether two population means differ, use a **two-sample t-test for the difference between two means**.

### Key facts
- $H_0\!: \mu_1 = \mu_2$ (or $\mu_1 - \mu_2 = 0$). $H_a$ is $\mu_1 - \mu_2 > 0$, $< 0$ or $\ne 0$, matching the claim. Define $\mu_1$ and $\mu_2$ in context.
- Conditions: two independent random samples (or a randomized experiment); the 10% condition for each (not needed for an experiment); and both $n \ge 30$ or both populations approximately normal (if either $n < 30$, both samples free of strong skewness and outliers).
- Choose the test from the **design**: two separate groups need a two-sample test; the same units measured twice (or paired units) need a matched pairs test on the differences.

### Watch out for
Hypotheses are about the parameters $\mu_1$ and $\mu_2$, not $\bar{x}_1$ and $\bar{x}_2$. And look at the data when a sample is small: an outlier can break the sample data condition.

### Worked example
Prompt: "Volunteers are randomly assigned to a new study method or the usual method, and the researcher thinks the new method gives a greater mean score. State the hypotheses."

$H_0\!: \mu_1 - \mu_2 = 0$ and $H_a\!: \mu_1 - \mu_2 > 0$, where $\mu_1$ and $\mu_2$ are the mean scores of all students like these with the new and the usual method.
"""),
("carrying-out-a-test-for-the-difference-between-two-population-means", r"""
### The idea
Calculate the two-sample t-statistic, find the p-value, compare it with $\alpha$, and state a conclusion about the populations.

### Key facts
- $t = \dfrac{\bar{x}_1 - \bar{x}_2}{\sqrt{\dfrac{s_1^2}{n_1} + \dfrac{s_2^2}{n_2}}}$, with the degrees of freedom from technology.
- The p-value is the probability, assuming the two population means are equal, of a difference in sample means as extreme or more extreme (in the direction of $H_a$).
- If the p-value is at most $\alpha$, reject $H_0$: convincing evidence for $H_a$. Otherwise fail to reject.
- The conclusion names the parameters and the populations, in terms of $H_a$. A randomized experiment with a small p-value supports cause and effect for individuals like the participants; do not generalize beyond volunteers or the populations sampled.

### Watch out for
Do not use a pooled standard deviation or add standard deviations. The standard error adds the variances of the two sample means. And a larger sample makes the same difference more convincing.

### Worked example
Prompt: "School A: $n = 30$, $\bar{x} = 24.1$, $s = 5.2$. School B: $n = 32$, $\bar{x} = 21.0$, $s = 4.8$. Test $H_a\!: \mu_1 - \mu_2 \ne 0$."

$t = 3.1/1.273 \approx 2.43$ with about 59 degrees of freedom, so the p-value is about $0.018$. At $\alpha = 0.05$, reject $H_0$: there is convincing evidence that the mean times differ.
"""),
]

if __name__ == "__main__":
    for _slug, _body in ENTRIES:
        check_markdown(_body)
    refreshers_lib.write("ap-statistics", 4, ENTRIES)
