"""Unit 1, topics 1.5 to 1.7.

Required content (CED effective Fall 2026): 1.5 histograms (bins; changing the bin width changes the appearance), stem-and-leaf plots (stems and leaves ordered) and dotplots show the distribution of a quantitative variable;
1.6 describe a distribution by shape (skewed right = longer right tail; skewed left; approximately symmetric; unimodal, bimodal, approximately uniform), center, variability and unusual features (outliers, gaps, clusters), in context;
1.7 mean, median, quartiles (medians of the lower and upper halves), percentiles, range, IQR, sample standard deviation (technology), changing units changes the statistics, outliers by the 1.5 IQR rule or more than 2 standard
deviations from the mean, resistant (median, IQR) and non-resistant (mean, range, standard deviation) measures, choosing a summary statistic. Skills 3.A, 3.B, 4.A, 4.B.
"""
from lib import *


def build(B):
    # ------------------------------------------------------------------------------------------------------------ 1.5
    T = 5
    counts = [3, 8, 12, 9, 5, 2, 1]
    edges = [0, 10, 20, 30, 40, 50, 60, 70]
    d = hist_from_counts(counts, edges, "Time spent on homework (minutes)", alt="Histogram of the time that 40 students spent on homework.")
    assert sum(counts) == 40
    B.mcq(T, "The histogram shows the time that each of the students in a class spent on homework one evening. How many of the students spent at least 20 minutes but less than 30 minutes on homework?",
          ch("12", "The bar for the interval from 20 to 30 minutes has a height of 12."),
          [ch("9", "This is the height of the bar for the interval from 30 to 40 minutes."),
           ch("8", "This is the height of the bar for the interval from 10 to 20 minutes."),
           ch("29", "This is the number of students who spent 20 minutes or more, not just the interval from 20 to 30 minutes.")],
          "Read the height of the bar for the interval 20 to 30: 12 students.", diagram=d, difficulty="easy")

    B.mcq(T, "The histogram shows the time that each of the students in a class spent on homework one evening. How many students are in the data set?",
          ch("40", "The total number of students is the sum of the heights of the bars: 3 + 8 + 12 + 9 + 5 + 2 + 1 = 40."),
          [ch("12", "This is the height of the tallest bar, not the number of students in all of the bars."),
           ch("7", "This is the number of bars (intervals), not the number of students."),
           ch("70", "This is the largest value on the horizontal axis, not the number of students.")],
          "Add the heights of the bars: 40 students.", diagram=d, difficulty="easy")

    B.mcq(T, "The histogram shows the time that each of the students in a class spent on homework one evening. How many of the students spent 40 minutes or more on homework?",
          ch("8", "Add the bars for 40 to 50, 50 to 60 and 60 to 70: 5 + 2 + 1 = 8."),
          [ch("5", "This is only the bar for the interval from 40 to 50 minutes."),
           ch("3", "This is the number of bars that lie to the right of 40 minutes."),
           ch("32", "This is the number of students who spent less than 40 minutes.")],
          "5 + 2 + 1 = 8 students.", diagram=d, difficulty="medium")

    B.mcq(T, "A histogram of the scores of 100 students on an exam, drawn with bins that are 20 points wide, has one peak. The same data are drawn with bins that are 2 points wide, and the second histogram has several small peaks. Which of the following best explains the difference?",
          ch("Changing the bin width can change the appearance of a histogram, even though the data are the same", "Altering the bin widths can change the shape that a histogram appears to have."),
          [ch("The data were changed when the second histogram was drawn, because a histogram with narrower bins uses more values", "Both histograms use the same data. Only the bins are different."),
           ch("One of the two histograms must have been drawn with an error, because the same data cannot give two different shapes", "Both can be correct. The bin width affects how the data are grouped."),
           ch("The mean of the data is different for the two histograms, because the bin width decides the mean", "The bin width does not change the values or the mean of the data.")],
          "The choice of bin width changes the appearance of a histogram.", difficulty="medium")

    data = [0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 5]
    d = dotplot(data, "Number of pets", axis=(0, 6, 1), alt="Dotplot of the number of pets for 17 students.")
    B.mcq(T, "The dotplot shows the number of pets owned by each of 17 students. How many of the students own more than 2 pets?",
          ch("4", "The values greater than 2 are 3, 3, 4 and 5, which are 4 students."),
          [ch("6", "This is the number of students who own exactly 1 pet."),
           ch("8", "This is the number of students who own 2 pets or more."),
           ch("13", "This is the number of students who own 2 pets or fewer.")],
          "Count the dots to the right of 2: 2 + 1 + 1 = 4.", diagram=d, difficulty="medium")

    stem = [12, 15, 18, 21, 23, 23, 27, 31, 34, 38, 40, 45]
    sp = stemplot(stem, "Key: 2 | 3 means 23 minutes")
    B.mcq(T, "The stem-and-leaf plot shows the time, in minutes, that each of 12 students took to finish a quiz. How many of the students took more than 30 minutes?",
          ch("5", "The values greater than 30 are 31, 34, 38, 40 and 45."),
          [ch("4", "This misses one of the values greater than 30. Count every leaf in rows 3 and 4."),
           ch("3", "This is the number of leaves in the row with the stem 3 only."),
           ch("7", "This is the number of students who took 30 minutes or less.")],
          "Rows 3 and 4 have 3 + 2 = 5 leaves.", diagram=sp, difficulty="medium")

    B.mcq(T, "In a stem-and-leaf plot with the key 2 | 3 means 23 minutes, a row reads 3 | 4 8. Which values does this row represent?",
          ch("34 minutes and 38 minutes", "The stem is the first digit (3) and each leaf is the next digit: 34 and 38."),
          [ch("3.4 minutes and 3.8 minutes", "The key shows that the stem is the tens digit, so 3 | 4 is 34, not 3.4."),
           ch("3 minutes, 4 minutes and 8 minutes", "The row has one stem and two leaves, which give two values."),
           ch("7 minutes and 11 minutes", "The leaves are not added to the stem. They are the next digit.")],
          "Each value is the stem followed by its leaf: 34 and 38.", difficulty="easy")

    B.mcq(T, "A researcher wants a display of a quantitative data set that shows every individual data value and keeps the values in order from smallest to largest. Which of the following displays does that?",
          ch("A stem-and-leaf plot, because each value is split into a stem and a leaf and all of the values are shown in order", "Stem-and-leaf plots (and dotplots) show each observation, in order."),
          [ch("A histogram, because it shows the height of a bar for the number of values that are in each interval of the data", "A histogram shows the counts in intervals. The individual values cannot be read."),
           ch("A bar chart, because it shows the height of a bar for each of the categories into which the data are placed", "Bar charts are for categorical variables."),
           ch("A pie chart, because it shows the share of the data in each slice of a circle whose total area is 100 percent", "Pie charts are for categorical variables.")],
          "Stem-and-leaf plots and dotplots show the actual values.", difficulty="medium")

    rel = [0.05, 0.20, 0.30, 0.25, 0.15, 0.05]
    edges = [0, 10, 20, 30, 40, 50, 60]
    d = hist_from_counts(rel, edges, "Age (years)", y_label="Relative frequency", y_axis=(0, 0.4, 0.1), alt="Relative frequency histogram of ages.")
    assert abs(sum(rel) - 1) < 1e-9
    B.mcq(T, "The relative frequency histogram shows the ages of the members of a club. What proportion of the members are at least 30 years old but younger than 50 years old?",
          ch("0.55", "Add the bars for 30 to 40 and 40 to 50: 0.30 + 0.25 = 0.55."),
          [ch("0.30", "This is only the bar for the interval from 30 to 40 years."),
           ch("0.45", "This is the proportion of the members who are younger than 30 years."),
           ch("0.70", "This is the proportion of the members who are 30 years old or older.")],
          "0.30 + 0.25 = 0.55.", diagram=d, difficulty="medium")

    # ------------------------------------------------------------------------------------------------------------ 1.6
    T = 6
    edges = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    right = draw("right", 80, 5, 0, 100)
    assert skewness(right) > 0.8
    d = histogram(right, edges, "Waiting time (minutes)", alt="Histogram of waiting times: most values are small, with a long tail to the right.")
    B.mcq(T, "A clinic recorded the waiting time of each of 80 patients. The histogram shows the data. Which of the following best describes the shape of the distribution?",
          ch("Skewed to the right, because the tail extends farther toward the larger values than toward the smaller values", "The right tail (toward larger values) is longer than the left tail."),
          [ch("Skewed to the left, because most of the patients waited for a short time and only a few waited for a long time", "A longer tail toward the larger values is skewed right, not left."),
           ch("Approximately symmetric, because both sides of the histogram have bars that are very tall and very short", "The left half is not a mirror image of the right half."),
           ch("Approximately uniform, because all of the bars of the histogram have about the same height as one another", "The bars are not all about the same height. The distribution has a peak at small values.")],
          "The long tail toward larger values means the distribution is skewed right.", diagram=d, difficulty="easy")

    left = draw("left", 80, 6, 0, 100)
    assert skewness(left) < -0.8
    d = histogram(left, edges, "Score on an easy quiz (points)", alt="Histogram of quiz scores: most values are large, with a long tail to the left.")
    B.mcq(T, "The histogram shows the scores of 80 students on a quiz. Which of the following best describes the shape of the distribution?",
          ch("Skewed to the left, because the tail extends farther toward the smaller scores than toward the larger scores", "The left tail (toward smaller values) is longer than the right tail."),
          [ch("Skewed to the right, because most of the scores are large and only a small number of the scores are small", "A longer tail toward smaller values is skewed left."),
           ch("Approximately symmetric, because the tallest bars of the histogram are close to the right end of the graph", "A symmetric distribution has halves that are mirror images. This one has a longer left tail."),
           ch("Bimodal, because the histogram has a tall peak near the large scores and then bars that decrease in height as the scores get smaller", "There is only one main peak, so the distribution is unimodal.")],
          "The longer tail toward smaller values means the distribution is skewed left.", diagram=d, difficulty="easy")

    sym = draw("symmetric", 80, 2, 0, 100)
    assert abs(skewness(sym)) < 0.15
    d = histogram(sym, edges, "Height of a plant (cm)", alt="Histogram of plant heights: a single peak in the middle with similar tails.")
    B.mcq(T, "The histogram shows the heights of 80 plants. Which of the following best describes the shape of the distribution?",
          ch("Approximately symmetric and unimodal, with one main peak near the middle and the bars falling evenly to each side", "The left half is approximately the mirror image of the right half, and there is one peak."),
          [ch("Skewed to the right, because there are a few plants that are much taller than the typical height of the plants", "The right tail is not longer than the left tail."),
           ch("Bimodal, because the tallest bar is at the center and there is a bar on each side of the center bar", "Bimodal means two prominent peaks. This histogram has one."),
           ch("Approximately uniform, because there are bars at every one of the heights that are shown on the horizontal axis", "The bars are not about the same height. They are tallest in the middle.")],
          "One peak in the middle and tails of similar length: approximately symmetric and unimodal.", diagram=d, difficulty="easy")

    bi = draw("bimodal", 80, 2, 0, 100)
    d = histogram(bi, edges, "Time of an eruption (minutes)", alt="Histogram with two prominent peaks, one at small values and one at large values.")
    cts = bin_counts(bi, edges)
    assert cts[1] + cts[2] > 12 and cts[7] + cts[8] > 12 and min(cts[4], cts[5]) < 5, cts
    B.mcq(T, "The histogram shows the lengths of the eruptions of a geyser. Which of the following best describes the shape of the distribution?",
          ch("Bimodal, because there are two prominent peaks, one at short times and one at long times, with a dip between", "A distribution with two prominent peaks is bimodal."),
          [ch("Unimodal, because the histogram has a single group of bars that are tall near the center of the graph", "There are two groups of tall bars with shorter bars between them."),
           ch("Skewed to the right, because there are bars at the large values that are as tall as those at the small values", "The two peaks have similar heights, so there is no longer tail on one side."),
           ch("Approximately uniform, because the heights of the bars are never zero for any of the intervals that are shown", "The heights of the bars are not about the same. There are two peaks.")],
          "Two prominent peaks: a bimodal distribution.", diagram=d, difficulty="medium")

    uni = draw("uniform", 90, 21, 0, 100)
    d = histogram(uni, edges, "Wait for a bus (minutes)", alt="Histogram with bars of roughly equal height.")
    cts = bin_counts(uni, edges)
    assert max(cts) - min(cts) <= 4, cts
    B.mcq(T, "The histogram shows the wait, in minutes, for a bus for each of 90 riders. Which of the following best describes the shape of the distribution?",
          ch("Approximately uniform, because the bars all have about the same height and there are no prominent peaks", "Each interval has about the same frequency, so the distribution is approximately uniform."),
          [ch("Skewed to the right, because the bars at the larger values of the wait are the same as those at the smaller values", "A skewed distribution has a longer tail on one side, with tapering bars."),
           ch("Bimodal, because the bars rise and fall several times as the values of the wait get larger across the graph", "There are no two prominent peaks. The differences in height are small."),
           ch("Unimodal and symmetric, because the bars at the left end are a mirror image of the bars at the right end", "A symmetric unimodal distribution has a peak in the middle. The bars here are about equal.")],
          "No prominent peaks and about equal frequencies: approximately uniform.", diagram=d, difficulty="medium")

    counts = [4, 10, 13, 9, 4, 0, 0, 0, 0, 1]
    d = hist_from_counts(counts, edges, "Daily rainfall (mm)", alt="Histogram of rainfall with most values below 50 and one value between 90 and 100.")
    B.mcq(T, "The histogram shows the amount of rain, in millimeters, on each of 41 days. Which of the following is an unusual feature of the distribution?",
          ch("There is a gap between 50 and 90 millimeters, and one day with a much larger value than the other days", "A region with no data is a gap, and a value that is far from the rest is an outlier."),
          [ch("There are two clusters of data, one cluster for the small values and another cluster for the large values", "There is a single main group and one isolated value, which is not two clusters."),
           ch("There are no unusual features, because the histogram has a peak and the heights of the bars decrease after the peak", "The gap and the single large value are unusual features."),
           ch("The distribution is bimodal, because there is a bar at the large values that is separate from the main group", "A single day does not form a prominent peak. It is a potential outlier.")],
          "A gap (no data between the main group and the large value) and an outlier.", diagram=d, difficulty="medium")

    B.mcq(T, "Which of the following describes a distribution that is skewed to the right?",
          ch("The tail on the right, toward the larger values, is longer than the tail on the left", "Skewed right (positively skewed) means the right tail is longer."),
          [ch("The left tail, toward the smaller values, is longer than the right tail", "That is skewed left."),
           ch("The left half of the distribution is approximately the mirror image of the right half", "That is approximately symmetric."),
           ch("The distribution has two prominent peaks that are separated by a region of smaller frequencies", "That is bimodal.")],
          "A distribution is skewed right if the right tail (toward larger values) is longer than the left.", difficulty="easy")

    B.mcq(T, "Which of the following variables is most likely to have a distribution that is skewed to the right?",
          ch("The annual income of the households in a large city, because a few households have incomes that are much larger than the others", "Income has a lower limit and a few very large values, which creates a long right tail."),
          [ch("The heights of the adult men in a large city, because most of the men have heights that are close to one typical value", "Heights are typically approximately symmetric."),
           ch("The scores of the students on a very easy test, because most of the students have scores that are close to the maximum", "Most scores near the maximum with a few low scores is skewed left."),
           ch("The result of rolling a fair die many times, because each of the six outcomes has the same chance of occurring", "Each outcome is equally likely, so it is approximately uniform.")],
          "A variable with a lower limit and a few very large values, such as income, is typically skewed right.", difficulty="medium")

    right2 = draw("right", 70, 7, 0, 100)
    d = histogram(right2, edges, "Commute time (minutes)", alt="Histogram of commute times, skewed right.")
    B.mcq(T, "The histogram shows the commute times of 70 workers. Which of the following claims is justified by the histogram?",
          ch("Most of the workers have fairly short commutes, and a few workers have commutes that are much longer than the others", "The tall bars are at the smaller values and there is a long tail to the right."),
          [ch("Most of the workers have long commutes, and a few workers have commutes that are much shorter than the others", "The tail extends to the larger values, not the smaller values."),
           ch("The commute times of the workers are spread evenly over all of the intervals that are shown on the horizontal axis, so there is no peak", "The frequencies are not about equal. They are largest at small values."),
           ch("The workers can be separated into two groups, one with short commutes and another with long commutes", "There is a single main peak, and not two groups.")],
          "A graph can justify claims in context: here, most commutes are short and a few are very long.", diagram=d, difficulty="medium")

    # ------------------------------------------------------------------------------------------------------------ 1.7
    T = 7
    data = [8, 12, 9, 25, 14, 10, 11, 15]
    m, md = mean(data), float(np.median(data))
    assert (m, md) == (13.0, 11.5)
    B.mcq(T, "The data set 8, 12, 9, 25, 14, 10, 11, 15 shows the number of text messages that each of 8 students sent yesterday. What is the mean of the data?",
          ch("13.0", "The sum is 104 and 104 / 8 = 13.0."),
          [ch("11.5", "This is the median, the average of the two middle values (11 and 12) of the ordered data."),
           ch("14.9", "This divides the sum by 7 instead of by the number of values, which is 8."),
           ch("25.0", "This is the maximum of the data, not the mean.")],
          "Mean = 104 / 8 = 13.0.", difficulty="easy")

    data = [23, 41, 18, 35, 29, 52, 27, 33, 38, 30]
    assert float(np.median(data)) == 31.5 and mean(data) == 32.6
    B.mcq(T, "The data set 23, 41, 18, 35, 29, 52, 27, 33, 38, 30 shows the ages of 10 members of a club. What is the median age?",
          ch("31.5", "The ordered data are 18, 23, 27, 29, 30, 33, 35, 38, 41, 52. With 10 values, the median is the mean of the two middle values, 30 and 33."),
          [ch("30.0", "This is only the lower of the two middle values. With an even number of values, average the two middle values."),
           ch("33.0", "This is only the upper of the two middle values. With an even number of values, average the two middle values."),
           ch("32.6", "This is the mean of the data, not the median.")],
          "Median = (30 + 33) / 2 = 31.5.", difficulty="easy")

    data = [4, 7, 8, 10, 12, 13, 15, 17, 18, 21, 24, 30]
    f = quartiles(data)
    assert (f.q1, f.median, f.q3, f.iqr) == (9.0, 14.0, 19.5, 10.5)
    B.mcq(T, "The ordered data set 4, 7, 8, 10, 12, 13, 15, 17, 18, 21, 24, 30 has 12 values. What is the interquartile range (IQR)?",
          ch("10.5", "Q1 is the median of the lower half (9) and Q3 is the median of the upper half (19.5), so IQR = 19.5 - 9 = 10.5."),
          [ch("26", "This is the range, the maximum minus the minimum (30 - 4)."),
           ch("5.5", "This is Q3 minus the median (19.5 - 14), which is only the upper part of the middle half of the data."),
           ch("19.5", "This is the third quartile, Q3, not the interquartile range.")],
          "IQR = Q3 - Q1 = 19.5 - 9 = 10.5.", difficulty="medium")

    data = [6, 8, 10, 12, 14]
    s_ = sd(data)
    assert round(s_, 2) == 3.16 and round(float(np.std(data)), 2) == 2.83
    B.mcq(T, "The data set 6, 8, 10, 12, 14 is a sample. A calculator gives several statistics for the data. Which of the following is the sample standard deviation, s?",
          ch("3.16", "The sample standard deviation divides the sum of the squared deviations (40) by n - 1 = 4 and takes the square root: sqrt(10) = 3.16."),
          [ch("2.83", "This divides by n instead of n - 1. That would be the standard deviation of a whole population."),
           ch("10.00", "This is the sample variance, s squared, not the standard deviation."),
           ch("8.00", "This is the range, the maximum minus the minimum, not the standard deviation.")],
          "s = sqrt(40 / 4) = sqrt(10) = 3.16.", difficulty="medium")

    B.mcq(T, "A student's score on an exam is at the 85th percentile of the scores of all of the students who took the exam. Which of the following is a correct interpretation?",
          ch("About 85% of the scores are less than or equal to this student's score, and about 15% are greater", "The pth percentile is the value with p% of the data less than or equal to it."),
          [ch("This student answered 85% of the questions on the exam correctly, which is a score of 85 out of 100", "A percentile is about the position of a score among the scores, not the percent correct."),
           ch("About 85% of the scores are greater than or equal to this student's score, and about 15% are less", "This is reversed. The 85th percentile has 85% of the scores at or below it."),
           ch("This student's score is 85 points higher than the mean of the scores of the students who took the exam", "A percentile does not give a difference in points.")],
          "The 85th percentile has about 85% of the data at or below it.", difficulty="medium")

    mu, sg = 20, 5
    new_mu, new_sg = 1.8 * mu + 32, 1.8 * sg
    assert (new_mu, new_sg) == (68.0, 9.0)
    B.mcq(T, "The daily high temperatures for a city, in degrees Celsius, have a mean of 20 and a standard deviation of 5. Each temperature is converted to degrees Fahrenheit using F = 1.8C + 32. What are the mean and the standard deviation of the temperatures in degrees Fahrenheit?",
          ch("The mean is 68 and the standard deviation is 9", "The mean is converted the same way as each value (1.8(20) + 32 = 68). The standard deviation is multiplied by 1.8, and adding 32 does not change it."),
          [ch("The mean is 68 and the standard deviation is 41", "The standard deviation is not changed by adding 32. It is only multiplied by 1.8."),
           ch("The mean is 36 and the standard deviation is 9", "The mean is also changed by adding 32, so it is 68."),
           ch("The mean is 20 and the standard deviation is 5", "Changing the units of measurement changes the values of the statistics.")],
          "Changing units affects the statistics: mean 1.8(20) + 32 = 68, standard deviation 1.8(5) = 9.", difficulty="hard")

    B.mcq(T, "A teacher adds 5 points to every student's score on a test. Which of the following correctly describes the effect on the measures of center and variability of the scores?",
          ch("The mean and the median each increase by 5, and the standard deviation and the IQR do not change", "Adding a constant shifts all of the values and so the measures of center. The spread does not change."),
          [ch("The mean and the median each increase by 5, and the standard deviation and the IQR each increase by 5", "Adding the same value to every score does not change how spread out the scores are."),
           ch("The mean increases by 5, but the median and the standard deviation and the IQR do not change", "The median also increases by 5."),
           ch("None of the measures changes, because adding the same value to each of the scores does not change their order", "The measures of center change. The order does not.")],
          "Adding a constant to every value adds it to the mean and median and leaves the standard deviation and IQR unchanged.", difficulty="medium")

    q1, q3, mx = 40, 52, 74
    fence = q3 + 1.5 * (q3 - q1)
    assert fence == 70
    B.mcq(T, "A data set has a first quartile of 40, a third quartile of 52, and a maximum value of 74. According to the rule that an outlier is more than 1.5 IQR above the third quartile or below the first quartile, is the maximum value an outlier?",
          ch("Yes, because the upper boundary is 52 + 1.5(12) = 70 and 74 is greater than 70", "IQR = 52 - 40 = 12. Values above Q3 + 1.5(IQR) = 70 are outliers."),
          [ch("No, because 74 is less than 52 + 3(12) = 88, which is the upper boundary for an outlier", "The rule uses 1.5 times the IQR, not 3 times."),
           ch("No, because the maximum value of a data set can never be an outlier of the values of the data set", "A maximum can be an outlier."),
           ch("Yes, because 74 is greater than the mean of the first quartile and the third quartile, which is 46", "The rule compares the value with the boundary Q3 + 1.5(IQR).")],
          "Upper boundary = Q3 + 1.5(IQR) = 52 + 18 = 70. Since 74 > 70, the maximum is an outlier.", difficulty="medium")

    mu, sg = 80, 6
    vals = [71, 93, 92, 68]
    outl = [v for v in vals if abs(v - mu) > 2 * sg]
    assert outl == [93]
    B.mcq(T, "A data set has a mean of 80 and a standard deviation of 6. A value is considered an outlier if it is more than 2 standard deviations above or below the mean. Which of the following values is an outlier?",
          ch("93", "93 is 13 above the mean, which is more than 2(6) = 12."),
          [ch("92", "92 is exactly 12 above the mean, which is exactly 2 standard deviations and not more than 2."),
           ch("71", "71 is 9 below the mean, which is less than 2 standard deviations."),
           ch("68", "68 is exactly 12 below the mean, which is exactly 2 standard deviations and not more than 2.")],
          "An outlier is more than 12 from the mean: only 93 qualifies.", difficulty="medium")

    B.mcq(T, "Which of the following pairs consists of a resistant measure of center and a resistant measure of variability?",
          ch("The median and the interquartile range", "Outliers do not greatly affect the median or the IQR."),
          [ch("The mean and the standard deviation", "Outliers can affect both of these values greatly, so they are not resistant."),
           ch("The median and the range", "The range uses the minimum and maximum, so it is not resistant."),
           ch("The mean and the interquartile range", "The mean is not resistant, because outliers can affect it greatly.")],
          "The median and IQR are resistant. The mean, range and standard deviation are not.", difficulty="medium")

    B.mcq(T, "The largest value in a data set of 15 values is changed from 40 to 400, and no other value is changed. Which of the following summary statistics must stay the same?",
          ch("The median", "The median is the middle value, which does not depend on how large the largest value is."),
          [ch("The mean", "The mean uses every value, so it increases."),
           ch("The standard deviation", "The standard deviation uses every value, so it increases."),
           ch("The range", "The range is the maximum minus the minimum, so it increases.")],
          "The median is resistant to the change in the largest value.", difficulty="medium")

    B.mcq(T, "The incomes of the households in a large city have a distribution that is strongly skewed to the right. Which of the following is the better choice of summary statistics to describe the typical income and the variability of the incomes?",
          ch("The median and the IQR, because they are not greatly affected by the very large incomes in the right tail", "For a skewed distribution with outliers, resistant measures describe the data better."),
          [ch("The mean and the standard deviation, because they use every one of the values of the incomes in the calculation", "The very large incomes would affect the mean and standard deviation greatly."),
           ch("The mean and the IQR, because the mean is a good measure of the center for a distribution of any shape", "The mean is not resistant, so it is pulled toward the long tail."),
           ch("The range and the standard deviation, because they show how far the largest income is from the smallest income", "Both are affected greatly by very large incomes.")],
          "Use the median and IQR when the distribution is skewed or has outliers.", difficulty="medium")

    B.mcq(T, "The sample standard deviation of a data set is 4. What is the sample variance?",
          ch("16", "The variance is the square of the standard deviation: 4 squared = 16."),
          [ch("2", "This is the square root of the standard deviation."),
           ch("8", "This doubles the standard deviation instead of squaring it."),
           ch("4", "This is the standard deviation. The variance is its square.")],
          "Variance = s squared = 16.", difficulty="easy")
