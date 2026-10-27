"""Writes content/ap-statistics/refreshers/unit-1.json (13 refreshers, one per topic). Layout: ### The idea, ### Key facts, ### Watch out for, ### Worked example.
Facts are the CED's essential knowledge for each topic (effective Fall 2026); every number in a worked example is asserted. No single-asterisk italics (a math course turns them into
multiplication dots), no lone dollar sign, no em dashes. Edit this script, not the JSON. Run: python3 u1_refreshers.py"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import refreshers_lib
import numpy as np

from lib import quartiles, outliers_iqr, check_markdown

# 1.3
assert 80 / 200 == 0.4 and 3 / (3 + 2) == 0.6
# 1.7
data = [8, 12, 9, 25, 14, 10, 11, 15]
assert sum(data) / 8 == 13.0 and float(np.median(data)) == 11.5
f = quartiles([4, 7, 8, 10, 12, 13, 15, 17, 18, 21, 24, 30])
assert (f.q1, f.q3, f.iqr) == (9.0, 19.5, 10.5) and 19.5 + 1.5 * 10.5 == 35.25
# 1.8
assert quartiles([14, 22, 9, 31, 18, 26, 12, 40, 20, 24]).median == 21.0
# 1.9
assert (78 - 70) / 4 == 2.0
sat, act = (1250 - 1050) / 200, (27 - 21) / 5
assert (sat, act) == (1.0, 1.2)
# 1.11
assert 400 * 0.15 == 60

ENTRIES = [
("introducing-statistics-what-can-we-learn-from-data", r"""
### The idea
A statistical study collects data from a **sample** to answer an investigative question about a larger **population**. We use a sample when it is too difficult or costly to collect data from every individual.

### Key facts
- The **population** is all of the items or individuals of interest, and its size is $N$. The **sample** is the part of the population from which data are obtained, and its size is $n$.
- A **datum** is one piece of information about an item or individual. A collection of data is a **data set**.
- An **investigative question** has a defined purpose, is posed so the data can be collected and analyzed, and is **not changed after seeing the results**.
- "In context" means that every number or statement is tied to the variable, the group, and the units of the situation.

### Watch out for
A statement such as "the mean is 7.2" is not in context. Say what was measured and for whom: "the mean amount of sleep on a school night for the 100 students in the study was 7.2 hours."

### Worked example
Prompt: "A school has 1,800 students. The principal surveys 120 randomly chosen students about sleep. Identify the population, the sample, $N$ and $n$."

The population is all 1,800 students at the school, so $N = 1800$. The sample is the 120 students who were surveyed, so $n = 120$.
"""),
("variables", r"""
### The idea
Each row of a data set describes an **observational unit**. Each column is a **variable**: a characteristic that can change from one unit to another.

### Key facts
- A **categorical** variable takes values that are category names or labels. A **quantitative** variable takes numerical values for a measured or counted quantity, usually with units.
- A **discrete** quantitative variable takes countable values (such as a count). A **continuous** one can take any value in an interval (such as a time or a weight).
- A **parameter** is a numerical summary of a variable for a **population**. A **statistic** is a numerical summary for a **sample**.
- The value of a statistic is often not equal to the unknown parameter, but it can be used to make inferences about it.

### Watch out for
Labels written with digits (postal codes, jersey numbers, ID numbers) are **categorical**. And a percent from a sample is a statistic, even when the sample is random.

### Worked example
Prompt: "A poll of 400 voters finds that 54% support a measure. The district has 3,200 students and 18% of all of them walk to school. Classify 54% and 18%."

The 54% summarizes a sample of 400 voters, so it is a **statistic**. The 18% summarizes all 3,200 students of the district, so it is a **parameter**.
"""),
("tabular-representation-and-summary-statistics-for-one-categorical-variable", r"""
### The idea
A table can show how the observational units are spread over the categories of a categorical variable.

### Key facts
- A **frequency table** gives the number of units in each category. A **relative frequency table** gives the proportion in each category: the count divided by the total.
- Relative frequencies add to 1 (or the percents add to 100%).
- Percentages, relative frequencies, and ratios all give the same information as proportions: 0.28, 28%, and 28 out of 100 mean the same thing.
- Counts and relative frequencies can be used to justify claims about the variable, in context.

### Watch out for
When two groups have different sizes, compare **relative frequencies**, not counts. A larger count in a larger group does not mean a larger proportion.

### Worked example
Prompt: "In Group A, 60 of 200 students prefer online homework. In Group B, 32 of 80 students prefer it. Which group has the greater proportion?"

Group A: $60 / 200 = 0.30$. Group B: $32 / 80 = 0.40$. Group B has the greater proportion, even though Group A has the greater count.
"""),
("graphical-representations-for-one-categorical-variable", r"""
### The idea
A **bar chart** or a **pie chart** displays the distribution of one categorical variable.

### Key facts
- In a **bar chart**, each bar is a category, and the height of the bar is the frequency (count) or the relative frequency. The categories can be put in any order.
- In a **pie chart**, each slice is a category, and its area as a fraction of the whole is the relative frequency. The slices add up to 100% of the circle.
- Tables, bar charts, and pie charts can be used to compare two or more groups on the same categorical variable.
- A graph of a categorical variable can justify a claim about the variable in context.

### Watch out for
A bar chart is not a histogram. A histogram is for a quantitative variable, and its bars touch and stay in numerical order. To compare groups of different sizes, graph the relative frequencies.

### Worked example
Prompt: "In a pie chart, one slice has a central angle of 90 degrees. What relative frequency does it show?"

The whole circle is 360 degrees, so the relative frequency is $90 / 360 = 0.25$, which is 25%.
"""),
("graphical-representations-for-one-quantitative-variable", r"""
### The idea
A histogram, a stem-and-leaf plot, and a dotplot show how the values of a quantitative variable are distributed, in their natural order from smallest to largest.

### Key facts
- A **histogram** puts the values into ordered intervals (**bins**). The height of a bar is the frequency or relative frequency of the values in that bin. The bars touch.
- Changing the **bin width** can change the appearance of a histogram.
- A **stem-and-leaf plot** splits each value into a stem (the first digits) and a leaf (usually the last digit). Stems and leaves are both ordered, and a key explains them.
- A **dotplot** puts one dot for each value above a number line, stacking dots at nearly identical values.

### Watch out for
A histogram does not show the individual values, but a stem-and-leaf plot and a dotplot do. And add the bars carefully: "20 or more" means every bar from 20 up.

### Worked example
Prompt: "A histogram has bars of heights 3, 8, 12, 9, 5, 2, 1 for the intervals 0 to 10, 10 to 20, and so on up to 70. How many values are 40 or more, and how many values are there in all?"

The bars for 40 to 50, 50 to 60, and 60 to 70 give $5 + 2 + 1 = 8$ values. All of the bars give $3 + 8 + 12 + 9 + 5 + 2 + 1 = 40$ values.
"""),
("descriptions-for-one-quantitative-variable-distributions", r"""
### The idea
To describe the distribution of a quantitative variable, give its **shape**, **center**, and **variability**, and any **unusual features**, always in context.

### Key facts
- **Skewed right** (positively skewed): the right tail, toward larger values, is longer. **Skewed left**: the left tail is longer. **Approximately symmetric**: the left half is about a mirror image of the right half.
- **Unimodal**: one main peak. **Bimodal**: two prominent peaks. **Approximately uniform**: about the same frequency everywhere, with no prominent peaks.
- An **outlier** is a value unusually small or large compared with the rest. A **gap** is a region with no data. **Clusters** are concentrations of values, usually separated by gaps.
- A graph can justify a claim about the variable in context.

### Watch out for
The direction of the skew is the direction of the **tail**, not of the peak. Income, which has a few very large values, is skewed right.

### Worked example
Prompt: "Most of the waiting times at a clinic are short, and a few are very long. Describe the shape."

The histogram has its peak at the short times and a long tail toward the long times, so the distribution is **skewed right**.
"""),
("summary-statistics-for-one-quantitative-variable", r"""
### The idea
Summary statistics describe the center, the variability, and the position of values in a quantitative data set.

### Key facts
- **Center:** the mean $\bar{x}$ (the sum divided by $n$) and the median (the middle value, or the mean of the two middle values when $n$ is even).
- **Quartiles:** Q1 is the median of the lower half, Q3 the median of the upper half. The **pth percentile** has p% of the data at or below it.
- **Variability:** the range (maximum minus minimum), the IQR ($Q3 - Q1$), and the sample standard deviation $s$ (technology finds it). The variance is $s^2$.
- **Outliers:** a value more than $1.5 \times IQR$ below Q1 or above Q3, or (a second rule) more than 2 standard deviations from the mean.
- The **median and IQR** are resistant to outliers. The **mean, range, and standard deviation** are not.
- Changing the units changes the statistics. Adding a constant shifts the center but not the spread. Multiplying by a constant multiplies both.

### Watch out for
Use the median and the IQR for a skewed distribution or one with outliers. Do not forget to say which outlier rule you use.

### Worked example
Prompt: "For the ordered data 4, 7, 8, 10, 12, 13, 15, 17, 18, 21, 24, 30, find the IQR and the upper outlier boundary."

Q1 is the median of 4, 7, 8, 10, 12, 13, which is $(8 + 10) / 2 = 9$. Q3 is the median of 15, 17, 18, 21, 24, 30, which is $(18 + 21) / 2 = 19.5$. So $IQR = 10.5$. The upper boundary is $19.5 + 1.5(10.5) = 35.25$, and 30 is not an outlier.
"""),
("graphical-representations-of-summary-statistics-for-one-quantitative-variable", r"""
### The idea
A **boxplot** is a picture of the **five-number summary**: the minimum, Q1, the median, Q3, and the maximum.

### Key facts
- The **box** runs from Q1 to Q3 and holds the middle 50% of the data. A line marks the median.
- The **whiskers** each represent about 25% of the data. With outliers, a whisker goes to the most extreme value that is **not** an outlier, and each outlier is shown separately with a symbol.
- If a distribution is roughly symmetric, the mean and the median are close. If it is skewed right, the mean is usually larger than the median. If it is skewed left, the mean is usually smaller.

### Watch out for
A boxplot does not show the number of peaks, so it cannot show whether a distribution is bimodal or uniform. And a long whisker does not mean more data: each whisker holds about 25% of the values.

### Worked example
Prompt: "A boxplot has a median close to Q1 and a much longer upper whisker. How do the mean and the median compare?"

The picture shows a distribution skewed right, so the mean is usually greater than the median.
"""),
("comparisons-of-the-distributions-for-one-quantitative-variable", r"""
### The idea
Graphs and summary statistics can be used to compare two or more distributions of the same quantitative variable.

### Key facts
- Histograms, dotplots, and back-to-back stem-and-leaf plots compare center, variability, shape, outliers, clusters, and gaps. Boxplots compare center, variability, outliers, and skewness.
- A **z-score** is $z = \dfrac{x - \mu}{\sigma}$. It measures how many standard deviations a value is above (positive) or below (negative) the mean. When the population values are unknown, use $\bar{x}$ and $s$.
- z-scores compare relative position within a distribution or between different distributions.

### Watch out for
Compare the distributions in context, and say both the center and the variability. To compare values on different scales, use z-scores, not the original values.

### Worked example
Prompt: "SAT scores have a mean of 1050 and a standard deviation of 200. ACT scores have a mean of 21 and a standard deviation of 5. Who did better relative to the other test takers: a student with a 1250 SAT or a student with a 27 ACT?"

SAT: $z = (1250 - 1050) / 200 = 1.0$. ACT: $z = (27 - 21) / 5 = 1.2$. The ACT student did better relative to the others.
"""),
("the-investigative-question-revisited-and-data-collection", r"""
### The idea
The investigative question guides the whole study: what data to collect, how to analyze them, and what conclusion is possible.

### Key facts
- A valid investigative question has three components: the **variable(s)** of interest; the **parameter and the direction** (for a test) or the **goal of estimation** (for an interval); and the **population** (and a cause-and-effect conclusion, if the study is an experiment with random assignment).
- A **census** records information from every member of a population.
- In an **experiment**, the researcher assigns **treatments** (the levels of the explanatory variable) to **experimental units**, and then measures a **response variable**. In an **observational study**, treatments are not imposed. Observational studies can be prospective (data now and into the future) or retrospective (data from the past), and a **survey** is one.
- A **confounding variable** in an observational study is associated with **both** the explanatory and the response variable.
- A random sample allows generalizing to the whole population. Volunteers or non-random samples only allow generalizing to similar individuals.

### Watch out for
An observational study can show an association but not cause and effect. And a confounding variable must be related to both variables.

### Worked example
Prompt: "Researchers use records to compare disease rates of adults who drink coffee daily and adults who do not. Name the type of study and the kind of conclusion."

The researchers did not assign the treatments, and they used past records, so this is a **retrospective observational study**. It can show an association, but not that coffee causes the difference.
"""),
("random-sampling", r"""
### The idea
A random sample uses chance to select the individuals. There are several random sampling methods.

### Key facts
- **Without replacement:** a unit can be selected only once. **With replacement:** a unit can be selected more than once.
- **Simple random sample (SRS):** every sample of size $n$ has the same chance of being selected (for example, with a random number generator or numbered slips).
- **Stratified:** divide the population into non-overlapping groups of similar individuals (**strata**), take an SRS from each stratum, and combine them.
- **Cluster:** divide the population into groups (**clusters**) that each look like the whole population, take an SRS of the clusters, and observe **every** unit in the chosen clusters.
- **Systematic:** a random starting point and a fixed interval.

### Watch out for
Stratified and cluster samples are easy to mix up. Stratified takes a sample from **every** group. Cluster takes **every unit** from some groups. And an equal chance for each individual is not the same as an SRS.

### Worked example
Prompt: "A company has 30 trucks. The manager randomly selects 4 of the trucks and inspects every package in those 4 trucks. Name the method."

Groups (trucks) are randomly selected, and every unit in each selected group is observed, so this is a **cluster random sample**.
"""),
("potential-problems-with-sampling", r"""
### The idea
**Bias** is a systematic error in a sampling procedure that makes a statistic consistently larger, or consistently smaller, than the parameter it estimates.

### Key facts
- **Voluntary response bias:** the sample consists entirely of volunteers, who often have strong opinions.
- **Undercoverage bias:** part of the population is left out of the sampling method or is less likely to be selected.
- **Nonresponse bias:** some of the individuals who were chosen do not respond, and the respondents may differ from the nonrespondents.
- **Response bias:** responses tend to differ from the true value in one direction, for example from confusing or leading questions, or from self-reported answers.
- Non-random methods, such as convenience samples, introduce potential bias because they do not use random chance.

### Watch out for
A larger sample does not remove bias. A biased method with 50,000 responses is still biased. Say which direction the bias is likely to push the estimate.

### Worked example
Prompt: "A mailed survey goes to 1,000 randomly selected parents, and 120 surveys come back. Name the likely bias."

Most of the chosen parents did not respond, and those who did may differ from those who did not, so the likely bias is **nonresponse bias**.
"""),
("experimental-design", r"""
### The idea
A well-designed experiment lets us conclude that a treatment **caused** a difference in the response.

### Key facts
- A well-designed experiment has a **comparison** of at least two treatments (one may be a **control** or **placebo**), **random assignment**, **replication**, and **direct control** of extraneous variables.
- Random assignment makes the treatment groups as similar as possible, so a difference in the response can be attributed to the treatment (a cause-and-effect conclusion). Replication means more than one unit per treatment.
- In a **single-blind** experiment the participants do not know their treatment, but the research team does (or the reverse). In a **double-blind** experiment neither group knows.
- **Completely randomized design:** treatments are assigned to all of the units completely at random.
- **Randomized block design:** group similar units into **blocks** by a blocking variable, then randomly assign the treatments within each block. **Matched pairs:** a block design with two treatments (each pair, or each unit, gets both, in a random order).
- When the units are volunteers, the conclusion applies to similar individuals.

### Watch out for
Random assignment is different from random selection. Assignment allows cause and effect. Selection allows generalizing to the population.

### Worked example
Prompt: "A researcher believes the effect of a medicine differs for men and women. She randomly assigns half of the men and half of the women to the medicine. Name the design."

The units are grouped by a blocking variable (sex) and the treatments are randomly assigned within each block, so this is a **randomized block design**.
"""),
]

if __name__ == "__main__":
    for _slug, _body in ENTRIES:
        check_markdown(_body)
    refreshers_lib.write("ap-statistics", 1, ENTRIES)
