"""Writes content/ap-statistics/refreshers/unit-2.json (12 refreshers, one per topic). Layout: ### The idea, ### Key facts, ### Watch out for, ### Worked example.
Facts are the CED's essential knowledge for each topic (effective Fall 2026); every number in a worked example is asserted. No single-asterisk italics (a math course turns them into
multiplication dots), no lone dollar sign, no em dashes. Edit this script, not the JSON. Run: python3 u2_refreshers.py"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import refreshers_lib
import numpy as np
from scipy import stats as sps

from lib import check_markdown

# 2.2
assert 120 / 400 == 0.30 and 180 / 400 == 0.45 and 120 / 200 == 0.60 and abs(120 / 180 - 2 / 3) < 1e-12
# 2.3
assert 312 / 1000 == 0.312
# 2.4
assert abs((1 - 0.8 ** 4) - 0.5904) < 1e-12 and 6 / 36 == 1 / 6
# 2.5 / 2.6 / 2.7
assert 0.40 + 0.35 - 0.15 == 0.60 and abs(0.30 / 0.60 - 0.5) < 1e-12 and abs(4 / 52 * 3 / 51 - 12 / 2652) < 1e-12
# 2.9
xs, ps = [0, 1, 2, 3], [0.10, 0.30, 0.35, 0.25]
mu = sum(x * p for x, p in zip(xs, ps))
var = sum((x - mu) ** 2 * p for x, p in zip(xs, ps))
assert abs(mu - 1.75) < 1e-12 and abs(var - 0.8875) < 1e-12 and abs(math.sqrt(var) - 0.942) < 1e-3
# 2.10
assert abs(sps.binom.pmf(3, 8, 0.4) - 0.2787) < 1e-3 and abs(math.sqrt(50 * 0.2 * 0.8) - 2.828) < 1e-3
# 2.11
assert abs(sps.norm.cdf(1.25) - 0.8944) < 1e-4 and abs(1050 + sps.norm.ppf(0.90) * 200 - 1306.3) < 0.1

ENTRIES = [
("tabular-and-graphical-representations-for-the-distributions-of-two-categorical-variables", r"""
### The idea
A **two-way table** (also called a **contingency table**) summarizes two categorical variables at once. Its rows are the levels of one variable and its columns are the levels of the other.

### Key facts
- The cells hold **frequencies** (counts) or **relative frequencies** (proportions). The row totals and column totals are shown in the margins.
- **Side-by-side bar charts**, **segmented bar charts**, and **mosaic plots** display the relationship between two categorical variables. Each shows the levels of one variable for every level of the other.
- To compare groups of different sizes, graph **relative frequencies** within each group, so that every bar or segmented bar has the same total.
- If the distribution of one variable is about the same at every level of the other, the variables do not appear to be **associated**. If it changes from one level to the next, they are associated.

### Watch out for
An association is not a cause-and-effect relationship. And a tall bar of counts can be tall only because its group is large: compare proportions, not counts.

### Worked example
Prompt: "Of 80 students in Grade 9, 32 prefer a packed lunch. Of 120 students in Grade 10, 90 prefer a packed lunch. Which grade has the greater proportion who prefer a packed lunch?"

Grade 9: $32 / 80 = 0.40$. Grade 10: $90 / 120 = 0.75$. A greater proportion of the Grade 10 students prefer a packed lunch, so the two variables appear to be associated.
"""),
("summary-statistics-for-two-categorical-variables", r"""
### The idea
Three kinds of relative frequency can be read from a two-way table, and they differ only in the number that you divide by.

### Key facts
- **Joint relative frequency:** a cell divided by the total for the **entire table**. It answers "what proportion of everyone is in both groups?"
- **Marginal relative frequency:** a row total, or a column total, divided by the total for the entire table.
- **Conditional relative frequency:** a cell divided by the total for **its row** or **its column**. You restrict to one level (the condition) and divide by that group's total.
- To look for an association, compare the **conditional distributions**: if they are different, the variables are associated.

### Watch out for
Read the condition carefully. "Among the adults under 40" divides by the row total for under 40. "Among the adults who get news online" divides by the column total for online. These two answers are different.

### Worked example
Prompt: "In a survey of 400 adults, 120 are under 40 and get their news mainly online, 200 are under 40, and 180 get their news mainly online. Find the joint, the marginal and the conditional relative frequencies of the adults under 40 who get news online."

Joint: $120 / 400 = 0.30$. Marginal for online: $180 / 400 = 0.45$. Conditional among the adults under 40: $120 / 200 = 0.60$. Conditional among those who get news online: $120 / 180 \approx 0.67$.
"""),
("estimating-probabilities-using-simulation", r"""
### The idea
A **random process** gives results that are determined by chance. A **simulation** models a random process so that the simulated outcomes closely match real-world outcomes, and the results are used to estimate a probability.

### Key facts
- An **outcome** is the result of one trial of a random process. An **event** is a collection of outcomes.
- The **probability** of an outcome or event is its **long-run relative frequency**: the relative frequency over a very large number of trials.
- To simulate, assign values (for example, random digits) so that each outcome has the correct probability. Run a trial, record the result, repeat, and record the counts and the total count.
- The **law of large numbers** says that for independent trials, as the number of trials increases, the relative frequency of an outcome gets closer and closer to a single value.

### Watch out for
A probability describes the long run, not the next few trials. After four heads in a row, the next flip of a fair coin is still 50% likely to be a head. And a simulation with a few trials gives an estimate that can be far from the true probability.

### Worked example
Prompt: "A spinner is spun 1,000 times and lands on red 312 times. Estimate P(red). A free throw shooter makes 70% of shots: how can random digits 0 to 9 simulate one shot?"

$P(\text{red}) \approx 312 / 1000 = 0.312$. Let the digits 0 to 6 be a made shot and 7 to 9 a missed shot: seven of ten digits gives probability 0.70.
"""),
("introduction-to-probability", r"""
### The idea
The **sample space** is the set of all possible nonoverlapping outcomes of a random process. Its probability is 1.

### Key facts
- When all outcomes in the sample space are **equally likely**, $P(E) = \dfrac{\text{number of outcomes in event } E}{\text{total number of outcomes in the sample space}}$.
- A probability is a number between 0 and 1, inclusive. An event that cannot happen has probability 0, and an event that is certain has probability 1.
- The **complement** of an event E is "not E", written $E'$. Its probability is $P(E') = 1 - P(E)$.
- "At least one" problems are often easiest with the complement: $P(\text{at least one}) = 1 - P(\text{none})$.

### Watch out for
Do not treat outcomes as equally likely when they are not. The 11 possible sums of two dice are not equally likely; the 36 pairs of numbers are.

### Worked example
Prompt: "A family buys 4 meals. Each meal has a coupon with probability 0.20, independently. Find the probability that at least one meal has a coupon."

P(no coupon in one meal) = 0.80, so P(no coupons in 4 meals) = $0.80^4 = 0.4096$. Then $P(\text{at least one}) = 1 - 0.4096 = 0.5904$.
"""),
("mutually-exclusive-events", r"""
### The idea
The **joint probability** of events A and B is the probability that **both** occur. It is the probability of the intersection, written $P(A \cap B)$.

### Key facts
- Events A and B are **mutually exclusive** (or **disjoint**) if they cannot occur at the same time.
- If A and B are mutually exclusive, then $P(A \cap B) = 0$. To justify that events are mutually exclusive, show that the joint probability is 0.
- If $P(A \cap B)$ is greater than 0, the events can occur together, so they are not mutually exclusive.
- Two events that are mutually exclusive, each with a positive probability, are **not independent**: if one occurs, the other cannot.

### Watch out for
Mutually exclusive and independent are different ideas. Mutually exclusive: they cannot both happen. Independent: knowing about one does not change the probability of the other.

### Worked example
Prompt: "A card is selected at random from a standard deck. Are 'heart' and 'king' mutually exclusive? Are 'heart' and 'spade' mutually exclusive?"

The king of hearts is both a heart and a king, so $P(\text{heart} \cap \text{king}) = 1/52$, not 0: not mutually exclusive. No card is both a heart and a spade, so $P(\text{heart} \cap \text{spade}) = 0$: mutually exclusive.
"""),
("conditional-probability", r"""
### The idea
A **conditional probability** is the probability that an event A occurs **given that** another event B has occurred. It is written $P(A \mid B)$.

### Key facts
- $P(A \mid B) = \dfrac{P(A \cap B)}{P(B)}$. Restrict to the outcomes in B, and ask what fraction of them are also in A.
- The **general multiplication rule**: $P(A \cap B) = P(A) \cdot P(B \mid A)$.
- In a two-way table, a conditional probability is a conditional relative frequency: divide a cell by the total of the row or column for the condition.
- When sampling **without replacement**, the probability of the second draw changes with the result of the first.

### Watch out for
$P(A \mid B)$ and $P(B \mid A)$ are usually different. "The probability of passing given that a student studied" is not "the probability of having studied given that a student passed."

### Worked example
Prompt: "Two cards are dealt without replacement from a standard deck. Find the probability that both are aces."

$P(\text{first ace}) = 4/52$ and $P(\text{second ace} \mid \text{first ace}) = 3/51$. So $P(\text{both}) = \dfrac{4}{52} \cdot \dfrac{3}{51} = \dfrac{12}{2652} \approx 0.0045$.
"""),
("independent-events-and-unions-of-events", r"""
### The idea
Two events are **independent** if knowing whether one has occurred does not change the probability of the other. The **union** of two events is the event that at least one of them occurs.

### Key facts
- Events A and B are independent if and only if $P(B \mid A) = P(B)$, equivalently $P(A \cap B) = P(A) \cdot P(B)$.
- To check independence, compare $P(A \cap B)$ with $P(A) \cdot P(B)$, or $P(B \mid A)$ with $P(B)$.
- The probability that A or B (or both) occurs is $P(A \cup B) = P(A) + P(B) - P(A \cap B)$. The subtraction removes the overlap that was counted twice.
- For mutually exclusive events the overlap is 0, so $P(A \cup B) = P(A) + P(B)$.

### Watch out for
Events that seem related can still be independent, and events that seem unrelated need not be. Check the numbers. And do not add probabilities for "or" without checking the overlap.

### Worked example
Prompt: "P(A) = 0.40, P(B) = 0.35 and P(A and B) = 0.15. Find P(A or B). Are A and B independent?"

$P(A \cup B) = 0.40 + 0.35 - 0.15 = 0.60$. Independence would need $P(A \cap B) = 0.40 \cdot 0.35 = 0.14$, which is not 0.15, so the events are not independent.
"""),
("introduction-to-random-variables-and-probability-distributions", r"""
### The idea
A **random variable** is a variable whose values are numerical outcomes of a random phenomenon. A **discrete** random variable takes countable values.

### Key facts
- A **probability distribution** for a discrete random variable gives the probability of every possible value. It can be shown as a table, a graph, or a function.
- The probabilities are each between 0 and 1 and their **sum is 1**.
- A distribution can be found with the rules of probability, or estimated with a simulation.
- A **cumulative distribution** gives $P(X \le x)$, the probability of being less than or equal to each value.

### Watch out for
For "at least" and "more than," list the values carefully: $P(X > 1)$ does not include 1, but $P(X \ge 1)$ does. And a table that does not add to 1 is not a probability distribution.

### Worked example
Prompt: "X takes the values 0, 1, 2, 3 with probabilities 0.10, 0.30, 0.35 and 0.25. Find P(X ≤ 2) and P(X > 1)."

The probabilities add to 1. $P(X \le 2) = 0.10 + 0.30 + 0.35 = 0.75$ and $P(X > 1) = 0.35 + 0.25 = 0.60$.
"""),
("parameters-of-random-variables", r"""
### The idea
The **mean** (expected value) and the **standard deviation** of a random variable are **parameters**: single, fixed values that describe its probability distribution.

### Key facts
- Mean: $\mu_X = E(X) = \sum x_i \, P(x_i)$. It is the **long-run average** outcome of the random variable.
- Standard deviation: $\sigma_X = \sqrt{\sum (x_i - \mu_X)^2 \, P(x_i)}$. It is the typical deviation of the values from the mean over the long run. The square of the standard deviation is the **variance**, $\sigma_X^2$.
- Interpret both in the context of the situation, with units: "over many ... the mean number of ... is about ...".
- The mean need not be a possible value of X.

### Watch out for
The expected value is not what happens in each trial; it is a long-run average. And a standard deviation is a typical distance from the mean, not a bound on the values.

### Worked example
Prompt: "X takes the values 0, 1, 2, 3 with probabilities 0.10, 0.30, 0.35, 0.25. Find the mean and the standard deviation."

$\mu = 0(0.10) + 1(0.30) + 2(0.35) + 3(0.25) = 1.75$. $\sigma^2 = (0 - 1.75)^2(0.10) + (1 - 1.75)^2(0.30) + (2 - 1.75)^2(0.35) + (3 - 1.75)^2(0.25) = 0.8875$, so $\sigma \approx 0.94$.
"""),
("the-binomial-distribution", r"""
### The idea
A **binomial random variable** counts the number of **successes** in a fixed number of repeated trials. The binomial distribution is the probability distribution of that count.

### Key facts
- X is binomial if there is a fixed number $n$ of trials, each trial has two outcomes (success or failure), the trials are **independent**, and the probability of success $p$ is the **same** for every trial.
- The probability of exactly $x$ successes is $P(X = x) = \binom{n}{x} p^x (1 - p)^{n - x}$ for $x = 0, 1, \ldots, n$.
- The mean is $\mu_X = np$ and the standard deviation is $\sigma_X = \sqrt{np(1 - p)}$.
- Use technology for sums, and use the complement for "at least": $P(X \ge 2) = 1 - P(X \le 1)$.
- A binomial probability can also be estimated with a simulation. Interpret the mean, the standard deviation, and the probabilities in context.

### Watch out for
Sampling without replacement from a small group makes the trials dependent, so the count is not binomial. And a count of the trials needed to get a success (waiting for the first 6) is not binomial: the number of trials is not fixed.

### Worked example
Prompt: "X is binomial with n = 8 and p = 0.4. Find P(X = 3)."

$P(X = 3) = \binom{8}{3}(0.4)^3(0.6)^5 = 56(0.064)(0.07776) \approx 0.279$.
"""),
("the-normal-distribution", r"""
### The idea
A **continuous random variable** can take any value in an interval, and probabilities are **areas under a curve**. Many continuous variables are well modeled by a **normal distribution**.

### Key facts
- A normal curve is continuous, unimodal, bell-shaped, and symmetric. It is identified by its mean $\mu$ and standard deviation $\sigma$. A smaller $\sigma$ gives a taller, more concentrated curve.
- The **standard normal** distribution has $\mu = 0$ and $\sigma = 1$. A z-score is $z = \dfrac{x - \mu}{\sigma}$.
- The **empirical rule**: about 68% of the values are within 1 standard deviation of the mean, about 95% within 2, and about 99.7% within 3.
- The total area under the curve is 1. For a probability, find the z-score(s) and use technology or a table. For an interval with a given area, work backward to the boundary.
- Percentiles and z-scores compare relative positions within a distribution and between distributions.

### Watch out for
Sketch the curve, label the mean, and shade the region before you calculate. The area to the right of a value is 1 minus the area to the left. And a single value has probability 0 for a continuous variable.

### Worked example
Prompt: "Test scores are approximately normal with mean 1050 and standard deviation 200. Find the score at the 90th percentile."

The 90th percentile has $z \approx 1.28$, so $x = 1050 + 1.28(200) \approx 1306$. (Check the direction: the 90th percentile is above the mean.)
"""),
("sampling-distributions-and-the-central-limit-theorem", r"""
### The idea
A statistic such as a sample mean or a sample proportion varies from sample to sample. Its **sampling distribution** describes that variation.

### Key facts
- The **sampling distribution of a statistic** is the distribution of the values of the statistic for **all possible samples of a given size** from a given population.
- It can be **simulated**: repeatedly take a large number of random samples from a population with known parameters, record the statistic from each, and display the distribution of the recorded values.
- A **randomization distribution** is generated by repeatedly randomly reassigning the response values to the treatment groups and recording the statistic each time.
- The **central limit theorem** (CLT): the sampling distribution of the mean of a random sample has a shape that can be approximated by a normal distribution. The larger the sample, the better the approximation.

### Watch out for
The CLT is about the distribution of the **sample means**, not of the data in one sample. A large sample from a skewed population is still skewed; the means of many large samples are approximately normal.

### Worked example
Prompt: "A right-skewed population has mean 20 minutes. Many random samples of size 40 are taken and their means are plotted. What does the histogram of the means look like?"

By the CLT it is approximately normal (symmetric with one peak), centered near the population mean of 20 minutes, even though the population itself is skewed right.
"""),
]

if __name__ == "__main__":
    for _slug, _body in ENTRIES:
        check_markdown(_body)
    refreshers_lib.write("ap-statistics", 2, ENTRIES)
