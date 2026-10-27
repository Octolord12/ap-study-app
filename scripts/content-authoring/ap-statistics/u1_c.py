"""Unit 1, topics 1.8 and 1.9.

Required content (CED effective Fall 2026): 1.8 the five-number summary (minimum, Q1, median, Q3, maximum) and the boxplot (the box is the middle 50% of the data, whiskers each represent 25% of the data and go to the most extreme
values that are not outliers, outliers are marked); if a distribution is roughly symmetric the mean and median are close, skewed right: mean usually larger than the median, skewed left: mean usually smaller. 1.9 compare
distributions with graphs (histograms, back-to-back stem-and-leaf plots, dotplots: center, variability, shape, outliers, clusters, gaps; boxplots: center, variability, outliers, skewness) and with summary statistics; z-scores
(x - mu) / sigma, the number of standard deviations above or below the mean; compare relative positions across distributions. Skills 3.A, 3.B, 4.A, 4.B, 4.C.
"""
from lib import *


def build(B):
    # ------------------------------------------------------------------------------------------------------------ 1.8
    T = 8
    lower = [20, 24, 26, 28, 29, 31, 32, 34, 35, 36]
    upper = [44, 46, 49, 52, 54, 56, 58, 62, 66, 78]
    data = lower + upper
    f = quartiles(data)
    assert (f.min, f.q1, f.median, f.q3, f.max, f.iqr) == (20, 30.0, 40.0, 55.0, 78, 25.0) and not outliers_iqr(data)
    d = boxplot([box_group(data)], "Score on a test (points)", axis=(0, 100, 10), alt="Boxplot of test scores: minimum 20, Q1 30, median 40, Q3 55, maximum 78.")
    B.mcq(T, "The boxplot shows the scores of 20 students on a test. What is the interquartile range (IQR) of the scores?",
          ch("25", "Q1 is 30 and Q3 is 55, the ends of the box, so IQR = 55 - 30 = 25."),
          [ch("58", "This is the range, the maximum minus the minimum (78 - 20)."),
           ch("40", "This is the median, the line inside the box."),
           ch("15", "This is the median minus the first quartile (40 - 30), which is only part of the box.")],
          "IQR = Q3 - Q1 = 55 - 30 = 25.", diagram=d, difficulty="easy")

    B.mcq(T, "The boxplot shows the scores of 20 students on a test. About what percent of the students had scores between 30 and 55?",
          ch("50%", "The box, from Q1 to Q3, represents the middle 50% of the data."),
          [ch("25%", "Each whisker represents about 25% of the data. The box represents 50%."),
           ch("75%", "The first quartile is the 25th percentile and the third quartile is the 75th percentile, so the box contains 50%, not 75%."),
           ch("100%", "The whiskers extend beyond the box to the minimum and maximum. The box has the middle 50% of the data.")],
          "Q1 and Q3 form the boundaries of the middle 50% of the values.", diagram=d, difficulty="easy")

    B.mcq(T, "In a boxplot with no outliers, about what percent of the data values are between the third quartile and the maximum?",
          ch("25%", "Each whisker represents about 25% of the data."),
          [ch("50%", "That is the percent of the data in the box, between Q1 and Q3."),
           ch("75%", "About 75% of the data are less than or equal to Q3. The whisker above Q3 has 25%."),
           ch("10%", "The whisker above Q3 represents about 25%, not 10%.")],
          "The lines (whiskers) each represent 25% of the data.", difficulty="medium")

    base = [31, 33, 34, 35, 36, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46]
    out_data = base + [75]
    g = box_group(out_data)
    assert g.get("outliers") == [75]
    d = boxplot([g], "Time (minutes)", axis=(30, 80, 5), alt="Boxplot with one point, 75, plotted beyond the upper whisker.")
    B.mcq(T, "The boxplot shows the times, in minutes, that 16 people took to complete a puzzle. The point at 75 is plotted separately from the whisker. Which of the following is the best description of the point?",
          ch("It is an outlier, because it is more than 1.5 IQR above the third quartile, so the whisker extends only to the largest value that is not an outlier", "When there are outliers, the whiskers extend to the most extreme values that are not outliers, and the outliers are shown with a symbol."),
          [ch("It is the third quartile, because it is the value that is farthest to the right of the median in the boxplot", "The third quartile is the right end of the box."),
           ch("It is the mean of the data, because it is plotted separately from the box and the whiskers on the number line", "The mean is not shown on a boxplot."),
           ch("It is a typical value, because every value of a data set must be inside the whiskers of a boxplot of the data", "Values beyond the whiskers are outliers.")],
          "A value more than 1.5 IQR beyond a quartile is an outlier and is plotted separately.", diagram=d, difficulty="medium")

    rs = draw("right", 61, 12, 0, 100)
    g = box_group(rs)
    assert g["median"] - g["q1"] < g["q3"] - g["median"] and mean(rs) > float(np.median(rs))
    d = boxplot([g], "Value", axis=(0, 100, 10), alt="Boxplot of a right-skewed variable: the median is near the left of the box and the upper whisker is long.")
    B.mcq(T, "The boxplot shows a data set. The median is closer to the first quartile than to the third quartile, and the upper whisker is much longer than the lower whisker. Which of the following is most likely true about the relationship between the mean and the median?",
          ch("The mean is greater than the median, because the distribution is skewed to the right", "If a distribution is skewed right, the mean is usually larger than the median."),
          [ch("The mean is less than the median, because the distribution is skewed to the right", "A right skew pulls the mean up, above the median."),
           ch("The mean is approximately equal to the median, because the box of the boxplot contains the middle 50% of the data", "The mean and median are close only when the distribution is approximately symmetric."),
           ch("The mean is less than the median, because the upper whisker is longer than the lower whisker of the boxplot", "A longer upper whisker indicates a right skew, which makes the mean larger.")],
          "A long right whisker and a median near Q1 indicate skewed right, so the mean is usually greater than the median.", diagram=d, difficulty="medium")

    B.mcq(T, "Which of the following sets of values is the five-number summary that is used to construct a boxplot?",
          ch("The minimum, the first quartile, the median, the third quartile, and the maximum of the data set", "A five-number summary is made up of these five values."),
          [ch("The mean, the standard deviation, the minimum, the maximum, and the sample size of the data", "A boxplot is not based on the mean or standard deviation."),
           ch("The minimum, the mean, the median, the mode, and the maximum of the values of the data set", "The mean and mode are not part of the five-number summary."),
           ch("The first quartile, the second quartile, the third quartile, the fourth quartile, and the range", "The five-number summary includes the minimum and the maximum, not the range.")],
          "Minimum, Q1, median, Q3, maximum.", difficulty="easy")

    data = [14, 22, 9, 31, 18, 26, 12, 40, 20, 24]
    f = quartiles(data)
    assert sorted(data) == [9, 12, 14, 18, 20, 22, 24, 26, 31, 40] and (f.q1, f.median, f.q3) == (14, 21.0, 26)
    B.mcq(T, "The data set 14, 22, 9, 31, 18, 26, 12, 40, 20, 24 has 10 values. Which of the following is its five-number summary?",
          ch("9, 14, 21, 26, 40", "Ordered: 9, 12, 14, 18, 20, 22, 24, 26, 31, 40. The median is (20 + 22) / 2 = 21, Q1 is the median of the lower five values (14), and Q3 is the median of the upper five values (26)."),
          [ch("9, 14, 22, 26, 40", "22 is not the median. With 10 values, the median is the mean of the fifth and sixth values (20 and 22), which is 21."),
           ch("9, 13, 21, 28, 40", "These quartiles are not the medians of the lower and upper halves of the ordered data."),
           ch("9, 18, 21.6, 24, 40", "21.6 is the mean, not the median, and 18 and 24 are not the quartiles.")],
          "The five-number summary is 9, 14, 21, 26, 40.", difficulty="medium")

    B.mcq(T, "In a boxplot of a data set, the median is in the middle of the box, and the two whiskers have about the same length. Which of the following is the most reasonable conclusion about the distribution?",
          ch("The distribution is approximately symmetric, so the mean and the median are close to each other", "A median in the middle of the box and equal whiskers indicate symmetry."),
          [ch("The distribution is skewed to the right, so the mean is much greater than the median of the distribution", "There is no sign of a longer upper whisker or a median near Q1."),
           ch("The distribution is bimodal, because a boxplot with a median in the middle always has two peaks in the data", "A boxplot does not show the number of peaks."),
           ch("The distribution is uniform, because the two whiskers are the same length and the box is in the middle", "A boxplot cannot show whether a distribution is uniform.")],
          "A median in the middle of the box and whiskers of similar length suggest an approximately symmetric distribution.", difficulty="medium")

    # ------------------------------------------------------------------------------------------------------------ 1.9
    T = 9
    a = [round(v) for v in draw("symmetric", 40, 31, 40, 100)]
    b = [min(100, round(v)) for v in [x + 8 + (i % 7 - 3) * 1.6 for i, x in enumerate(a)]]
    ga, gb = box_group(a, "Class A"), box_group(b, "Class B")
    fa, fb = quartiles(a), quartiles(b)
    assert gb["median"] > ga["median"] and abs(fb.iqr - fa.iqr) < 8
    d = boxplot([ga, gb], "Score on a test (points)", axis=(30, 100, 10), alt="Boxplots of the test scores of two classes.")
    assert gb["median"] - ga["median"] > 5
    B.mcq(T, "The boxplots show the test scores of the students in Class A and in Class B. Which of the following is a correct comparison of the two distributions?",
          ch("The median score is higher for Class B than for Class A, and the variability, as measured by the IQR, is similar for the two classes", "Compare the centers (the medians are the lines in the boxes) and the lengths of the boxes (IQR)."),
          [ch("The median score is higher for Class A than for Class B, and the variability, as measured by the IQR, is similar for the two classes", "The median line of Class B is farther to the right than the median line of Class A."),
           ch("The median score is higher for Class B than for Class A, and the IQR is much greater for Class A than for Class B", "The boxes have similar lengths, so the IQRs are similar."),
           ch("The median scores of the two classes are the same, and the range is greater for Class B than for Class A", "The medians are not the same. Class B has the higher median.")],
          f"Class B's median ({gb['median']}) is greater than Class A's ({ga['median']}); the boxes have similar lengths.", diagram=d, difficulty="medium")

    tab = table(["Group", "Mean", "Standard deviation", "Median", "IQR"], [("Plan 1", "52", "8", "51", "10"), ("Plan 2", "52", "15", "50", "21")], caption="Weight loss, in pounds, for two groups of people after 3 months", row_headers=True)
    B.mcq(T, "The table gives summary statistics for the amounts of weight lost, in pounds, by two groups of people who followed two different plans. Which of the following is a correct comparison of the two distributions?",
          ch("The centers are about the same, but the weight losses for Plan 2 are more variable than the weight losses for Plan 1", "The means and medians are close, while the standard deviation and IQR are larger for Plan 2."),
          [ch("The centers are about the same, but the weight losses for Plan 1 are more variable than the weight losses for Plan 2", "Plan 1 has the smaller standard deviation and IQR, so it is less variable."),
           ch("The weight losses for Plan 2 are greater than those for Plan 1, because the standard deviation is greater for Plan 2", "A greater standard deviation means more variability, not a greater center."),
           ch("The weight losses for the two plans are the same, because the means of the two groups are exactly equal to each other", "The variability is different, so the distributions are not the same.")],
          "Same center (means about 52), but Plan 2 has the greater standard deviation and IQR.", diagram=tab, difficulty="medium")

    B.mcq(T, "A student's score on a test is 78. The mean score of the class is 70 and the standard deviation of the scores is 4. What is the z-score of the student's score?",
          ch("2.0", "z = (78 - 70) / 4 = 2.0."),
          [ch("8.0", "This is the difference from the mean. The z-score divides it by the standard deviation."),
           ch("0.5", "This divides the standard deviation by the difference (4 / 8). The z-score is the difference divided by the standard deviation."),
           ch("19.5", "This divides the score by the standard deviation instead of using the difference from the mean.")],
          "z = (x - mu) / sigma = (78 - 70) / 4 = 2.0.", difficulty="easy")

    B.mcq(T, "A runner's time in a race has a z-score of -1.5 among the times of all of the runners in the race. Which of the following is a correct interpretation?",
          ch("The runner's time was 1.5 standard deviations below the mean time of the runners", "A negative z-score means the value is below the mean. The size is the number of standard deviations."),
          [ch("The runner's time was 1.5 standard deviations above the mean time of the runners", "A negative z-score means below the mean."),
           ch("The runner's time was 1.5 minutes below the mean time of the runners in the race", "A z-score is a number of standard deviations, not minutes."),
           ch("The runner's time was 1.5 times the mean time of the runners who took part in the race", "A z-score is not a ratio to the mean.")],
          "A z-score measures how many standard deviations a value is above (positive) or below (negative) the mean.", difficulty="easy")

    sat = z(1250, 1050, 200)
    act = z(27, 21, 5)
    assert (sat, act) == (1.0, 1.2)
    B.mcq(T, "On the SAT, the scores have a mean of 1050 and a standard deviation of 200. On the ACT, the scores have a mean of 21 and a standard deviation of 5. A student has an SAT score of 1250 and a different student has an ACT score of 27. Which of the following is a correct statement?",
          ch("The student with the ACT score had the better performance relative to the other test takers, because a z-score of 1.2 is greater than a z-score of 1.0", "z-scores compare relative position: ACT z = (27 - 21) / 5 = 1.2, SAT z = (1250 - 1050) / 200 = 1.0."),
          [ch("The student with the SAT score had the better performance relative to the other test takers, because 1250 is greater than 27", "The scores are on different scales and cannot be compared directly."),
           ch("The two students had the same performance relative to the others, because each score is above the mean of its own test", "Both are above the mean, but by different numbers of standard deviations."),
           ch("The student with the SAT score had the better performance relative to the others, because the SAT has the greater standard deviation", "A greater standard deviation does not mean a better relative performance. Compare the z-scores.")],
          "Compare z-scores: ACT 1.2 is greater than SAT 1.0.", difficulty="hard")

    mu, sg, zz = 60, 8, 1.25
    xv = mu + zz * sg
    assert xv == 70
    B.mcq(T, "The scores on a test have a mean of 60 and a standard deviation of 8. A student's score has a z-score of 1.25. What was the student's score?",
          ch("70", "x = mu + z(sigma) = 60 + 1.25(8) = 70."),
          [ch("61.25", "This adds the z-score to the mean. The z-score must be multiplied by the standard deviation first."),
           ch("10", "This is the number of points above the mean. The score is the mean plus 10."),
           ch("52", "This subtracts 1.25(8) from the mean. A positive z-score is above the mean.")],
          "x = 60 + 1.25(8) = 70.", difficulty="medium")

    B.mcq(T, "A sample of 50 values has a mean of 50 and a standard deviation of 5. The population mean and standard deviation are not known. Which of the following is the z-score of a value of 60 that is based on the sample statistics?",
          ch("2", "When the population mean and standard deviation are unknown, the sample mean and standard deviation may be used: z = (60 - 50) / 5 = 2."),
          [ch("12", "This divides the value by the standard deviation instead of using the difference from the mean."),
           ch("0.5", "This divides the standard deviation by the difference. The z-score is the difference divided by the standard deviation."),
           ch("It cannot be calculated", "The sample mean and standard deviation can be used when the parameters are unknown.")],
          "z = (60 - 50) / 5 = 2.", difficulty="medium")

    B.mcq(T, "A value in a data set is equal to the mean of the data set. What is the z-score of the value?",
          ch("0", "z = (x - mean) / s = 0, because the value is exactly at the mean."),
          [ch("1", "A z-score of 1 would be one standard deviation above the mean."),
           ch("-1", "A z-score of -1 would be one standard deviation below the mean."),
           ch("It depends on the standard deviation", "The numerator is 0, so the z-score is 0 for any standard deviation.")],
          "The value is 0 standard deviations from the mean.", difficulty="easy")

    ga_ = [round(v) for v in draw("right", 40, 58, 0, 100)]
    gb_ = [round(v) for v in draw("symmetric", 40, 41, 0, 100)]
    ba, bb = box_group(ga_, "Store A"), box_group(gb_, "Store B")
    # Store A: median nearer Q1 and a much longer upper whisker; Store B: roughly symmetric (so the claim below is true of the pictures)
    assert (ba["median"] - ba["q1"]) < (ba["q3"] - ba["median"]) and (ba["max"] - ba["q3"]) > 1.8 * (ba["q1"] - ba["min"]), ba
    assert abs((bb["median"] - bb["q1"]) - (bb["q3"] - bb["median"])) <= 0.25 * (bb["q3"] - bb["q1"]), bb
    assert "outliers" not in ba and "outliers" not in bb
    d = boxplot([ba, bb], "Time to check out (minutes)", axis=None, alt="Boxplots of the checkout times at two stores.")
    B.mcq(T, "The boxplots show the time, in minutes, that customers took to check out at two stores. Which of the following claims is justified by the boxplots?",
          ch("Store A has the longer upper whisker and the median closer to the first quartile, so its times are more skewed to the right than the times at Store B", "Boxplots can be used to compare center, variability, outliers and skewness."),
          [ch("Store B has the longer upper whisker and the median closer to the first quartile, so its times are more skewed to the right than the times at Store A", "This describes the pattern of Store A, not Store B."),
           ch("Both stores have the same median checkout time, because the boxplots are drawn on the same number line of times", "The medians are different. Compare the median lines."),
           ch("The checkout times at Store A are the shorter times, because its boxplot has a longer upper whisker than that of Store B", "A longer upper whisker does not mean shorter times.")],
          "Compare the shapes of the boxplots: Store A's is skewed right.", diagram=d, difficulty="hard")
