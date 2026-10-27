"""Unit 1 free response, part 2: four ANALYZE_DATA prompts (Question 2: practices 3 and 4) and two MULTI_FOCUS prompts (Question 4), 10 points each.

  A1 1.9 boxplots of two classes: compare, the 1.5 IQR rule, a z-score      A2 1.6 a right-skewed histogram: shape, which summary, a change of units
  A3 1.7 twelve delivery times: median, IQR, an outlier, the effect of removing it     A4 1.4 counts of two groups: relative frequencies and a claim
  M1 1.11 a simple random sample, a histogram, a z-score, the 2 SD rule        M2 1.13 an experiment with boxplots: design, comparison, the 1.5 IQR rule
Every number is computed here from the data that is shown or described.
"""
from lib import *


def L(*lines):
    return [(1, t) for t in lines]


def fx(v, p=1):
    return f"{v:.{p}f}"


def build(B):
    # ----------------------------------------------------------------------------------------------------------- A1: two boxplots
    rA = random.Random(3)
    class_a = sorted(int(round(rA.gauss(72, 7))) for _ in range(24))
    rB = random.Random(1)
    class_b = sorted([int(round(rB.gauss(80, 8))) for _ in range(23)] + [41])
    ga, gb = box_group(class_a, "Class A"), box_group(class_b, "Class B")
    fa, fb = quartiles(class_a), quartiles(class_b)
    assert gb.get("outliers") == [41] and "outliers" not in ga and fb.median > fa.median + 4
    mean_a, sd_a, mean_b, sd_b = mean(class_a), sd(class_a), mean(class_b), sd(class_b)
    zA = (class_a[-1] - mean_a) / sd_a
    fence_lo = fb.q1 - 1.5 * fb.iqr
    d = boxplot([ga, gb], "Score on the final exam (points)", alt="Boxplots of the final exam scores of Class A and Class B; Class B has one low outlier.")
    setup = (f"A teacher gave the same final exam to two classes of 24 students each. The boxplots show the distributions of the scores. The mean and the standard deviation of the scores are {fx(mean_a)} and {fx(sd_a)} for Class A, and {fx(mean_b)} and {fx(sd_b)} for Class B. The five-number summaries are Class A: {fa.min}, {fx(fa.q1)}, {fx(fa.median)}, {fx(fa.q3)}, {fa.max} and Class B: {fb.min}, {fx(fb.q1)}, {fx(fb.median)}, {fx(fb.q3)}, {fb.max}.")
    parts = [("A", "Compare the centers of the two distributions of scores, using the medians."),
             ("B", "Compare the variability of the two distributions of scores, using the interquartile ranges (IQR)."),
             ("C", "The lowest score in Class B is shown as a separate point. Use the rule that an outlier is a value more than 1.5 IQR below the first quartile or above the third quartile to show that the lowest score in Class B is an outlier."),
             (("D"), f"In Class A, the highest score is {class_a[-1]}. Calculate the z-score for this score, and interpret the z-score in context."),
             ("E", "A student in Class B says, \"Class B did better on the exam than Class A.\" Use the boxplots to justify a claim about the performance of the two classes, and say whether the outlier changes your claim.")]
    ans = [("A", f"The median of Class B ({fx(fb.median)}) is greater than the median of Class A ({fx(fa.median)}), so the center of the scores is higher for Class B, by {fx(fb.median - fa.median)} points."),
           ("B", f"The IQR for Class A is {fx(fa.q3)} - {fx(fa.q1)} = {fx(fa.iqr)} and the IQR for Class B is {fx(fb.q3)} - {fx(fb.q1)} = {fx(fb.iqr)}. The IQR is {'greater' if fb.iqr > fa.iqr else 'smaller'} for Class B, so the scores of Class B are {'more' if fb.iqr > fa.iqr else 'less'} variable in the middle 50%."),
           ("C", f"For Class B, IQR = {fx(fb.iqr)}, so the lower boundary is Q1 - 1.5(IQR) = {fx(fb.q1)} - 1.5({fx(fb.iqr)}) = {fx(fence_lo)}. The lowest score, 41, is less than {fx(fence_lo)}, so it is an outlier."),
           ("D", f"z = ({class_a[-1]} - {fx(mean_a)}) / {fx(sd_a)} = {fx(zA, 2)}. The highest score in Class A is about {fx(zA, 2)} standard deviations above the mean score of Class A."),
           ("E", f"The boxplot of Class B is shifted to the right of the boxplot of Class A (the median, the quartiles and the maximum are all higher), so the students in Class B generally scored higher. The one low outlier in Class B does not change this claim, because the median and the IQR are not much affected by an outlier.")]
    prompt, sample = frq_text(setup, parts, ans)
    B.frq(9, "ANALYZE_DATA", prompt,
          L(f"A: Compares the medians correctly ({fx(fb.median)} for Class B is greater than {fx(fa.median)} for Class A).",
            "A: States the conclusion in context: the center of the scores is higher for Class B.",
            f"B: Calculates the IQRs ({fx(fa.iqr)} for Class A and {fx(fb.iqr)} for Class B).",
            f"B: Compares the variability in context: the middle 50% of the scores of Class {'B' if fb.iqr > fa.iqr else 'A'} are more spread out.",
            f"C: Calculates the lower boundary: {fx(fb.q1)} - 1.5({fx(fb.iqr)}) = {fx(fence_lo)}.",
            "C: Concludes that 41 is less than the boundary, so it is an outlier.",
            f"D: Calculates the z-score = ({class_a[-1]} - {fx(mean_a)}) / {fx(sd_a)} = {fx(zA, 2)}.",
            f"D: Interprets the z-score in context: the highest score of Class A is about {fx(zA, 2)} standard deviations above the mean score of Class A.",
            "E: Justifies a claim using the boxplots: the distribution of Class B is shifted higher (a greater median and quartiles), so Class B generally did better.",
            "E: States that the outlier does not change the claim (the median and IQR are resistant)."),
          sample, diagram=d)

    # ----------------------------------------------------------------------------------------------------------- A2: right-skewed histogram
    commute = [max(3, int(v)) for v in draw("right", 60, 3, 0, 100)]
    assert skewness(commute) > 0.9
    edges = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    cts = bin_counts(commute, edges)
    m_, md_, s_ = mean(commute), float(np.median(commute)), sd(commute)
    f_ = quartiles(commute)
    assert m_ > md_
    d = histogram(commute, edges, "Commute time (minutes)", alt="Histogram of the commute times of 60 workers: skewed to the right.")
    ge40 = sum(cts[4:])
    mh, sh = m_ / 60, s_ / 60
    setup = (f"A company asked each of 60 workers for the time, in minutes, that it takes the worker to commute to work. The histogram shows the distribution of the times. The mean is {fx(m_)} minutes, the median is {fx(md_)} minutes, the standard deviation is {fx(s_)} minutes, and the interquartile range is {fx(f_.iqr)} minutes.")
    parts = [("A", "Describe the distribution of the commute times in context. Include the shape, the center, and the variability."),
             ("B", "Explain why the median and the IQR are better than the mean and the standard deviation for describing these data."),
             ("C", "Use the histogram to find the number of workers whose commute time is 40 minutes or more."),
             ("D", "Explain why the mean is greater than the median for these data."),
             ("E", "The company converts the commute times from minutes to hours. (i) Find the mean of the commute times in hours.\n\n(ii) Find the standard deviation of the commute times in hours.\n\n(iii) Explain how the shape of the distribution of the times is affected by the change of units.")]
    ans = [("A", f"The distribution is skewed to the right (a long tail toward the longer times), with a peak at the shorter times. A typical commute time is about {fx(md_)} minutes (the median). The commute times vary, with an IQR of {fx(f_.iqr)} minutes, and a few workers have a much longer commute than the others."),
           ("B", "The distribution is skewed to the right with some large values. The median and the IQR are resistant to outliers and skew, but the mean and the standard deviation are pulled toward the long right tail."),
           ("C", f"The bars from 40 minutes up have heights {', '.join(str(c) for c in cts[4:])}, so {ge40} workers had a commute of 40 minutes or more."),
           ("D", "The distribution is skewed right. The few very long commute times pull the mean toward the right tail, but they do not affect the median much, so the mean is greater than the median."),
           ("E", f"(i) {fx(m_)} / 60 = {fx(mh, 3)} hours. (ii) {fx(s_)} / 60 = {fx(sh, 3)} hours. (iii) The shape does not change: it is still skewed to the right, because every value is divided by the same number.")]
    prompt, sample = frq_text(setup, parts, ans)
    B.frq(6, "ANALYZE_DATA", prompt,
          L("A: Describes the shape in context: skewed to the right (long tail toward longer commute times).",
            f"A: Describes the center in context (a typical commute of about {fx(md_)} minutes, the median, or about {fx(m_)} minutes, the mean).",
            f"A: Describes the variability in context (an IQR of {fx(f_.iqr)} minutes or a standard deviation of {fx(s_)} minutes, or a range of the times).",
            "B: Explains that the median and the IQR are resistant measures that are not affected much by the skew and the large values, while the mean and the standard deviation are.",
            f"C: Reads the histogram correctly: {ge40} workers had commute times of 40 minutes or more.",
            "D: Explains that the right skew (a few very large values) pulls the mean up toward the tail.",
            "D: Explains that the median is resistant, so it is less affected by the large values and is smaller than the mean.",
            f"E(i): Calculates the mean in hours: {fx(m_)} / 60 = {fx(mh, 3)}.",
            f"E(ii): Calculates the standard deviation in hours: {fx(s_)} / 60 = {fx(sh, 3)}.",
            "E(iii): States that the shape does not change (the distribution is still skewed right), because all values are divided by the same positive number."),
          sample, diagram=d)

    # ----------------------------------------------------------------------------------------------------------- A3: delivery times, median, IQR, outlier
    times = [22, 25, 27, 28, 30, 31, 33, 34, 36, 38, 41, 85]
    f = quartiles(times)
    assert (f.q1, f.median, f.q3, f.iqr) == (27.5, 32.0, 37.0, 9.5) and outliers_iqr(times) == [85]
    m_all = mean(times)
    without = [t for t in times if t != 85]
    m_wo, md_wo = mean(without), float(np.median(without))
    hi_fence = f.q3 + 1.5 * f.iqr
    d = dotplot(times, "Delivery time (minutes)", axis=(20, 90, 10), alt="Dotplot of 12 delivery times; one value, 85, is far from the others.")
    setup = ("A restaurant recorded the time, in minutes, that it took to deliver each of 12 orders. The times, in order from least to greatest, are 22, 25, 27, 28, 30, 31, 33, 34, 36, 38, 41, and 85. The dotplot shows the data.")
    parts = [("A", "Calculate the median and the interquartile range (IQR) of the delivery times."),
             ("B", "Use the rule that an outlier is a value more than 1.5 IQR above the third quartile or below the first quartile to determine whether the longest delivery time is an outlier."),
             ("C", f"The mean of all 12 delivery times is {fx(m_all, 2)} minutes. (i) Calculate the mean of the 11 times that remain when the time of 85 minutes is removed.\n\n(ii) Explain which summary statistic of center, the mean or the median, is affected more by removing the time of 85 minutes."),
             ("D", "The restaurant wants to report a typical delivery time and the variability of the delivery times. Which measures should it use? Justify your answer."),
             ("E", "Each delivery time is increased by 5 minutes because of a change in the route. Describe the effect of this change on the median and on the IQR.")]
    ans = [("A", f"The median is (31 + 33) / 2 = {fx(f.median)} minutes. Q1 is the median of the lower six values (27 and 28), which is {fx(f.q1)}, and Q3 is the median of the upper six values (36 and 38), which is {fx(f.q3)}. IQR = {fx(f.q3)} - {fx(f.q1)} = {fx(f.iqr)} minutes."),
           ("B", f"The upper boundary is Q3 + 1.5(IQR) = {fx(f.q3)} + 1.5({fx(f.iqr)}) = {fx(hi_fence, 2)}. The longest time, 85, is greater than {fx(hi_fence, 2)}, so it is an outlier."),
           ("C", f"(i) The mean of the 11 times is {sum(without)} / 11 = {fx(m_wo, 2)} minutes. (ii) The mean changes from {fx(m_all, 2)} to {fx(m_wo, 2)}, a change of {fx(m_all - m_wo, 2)} minutes, and the median changes from {fx(f.median)} to {fx(md_wo)}, a change of {fx(f.median - md_wo)} minute. The mean is affected more, because it is not resistant to outliers."),
           ("D", "The restaurant should use the median and the IQR, because the data have an outlier, and these measures are resistant, so they describe a typical delivery and the variability of most of the deliveries."),
           ("E", "Adding 5 minutes to each time adds 5 to the median (it becomes 37 minutes), but the IQR does not change (it is still 9.5 minutes), since adding a constant does not change the spread.")]
    prompt, sample = frq_text(setup, parts, ans)
    B.frq(7, "ANALYZE_DATA", prompt,
          L(f"A: Calculates the median correctly ({fx(f.median)} minutes).",
            f"A: Calculates the quartiles and the IQR correctly (Q1 = {fx(f.q1)}, Q3 = {fx(f.q3)}, IQR = {fx(f.iqr)}).",
            f"B: Calculates the upper boundary {fx(f.q3)} + 1.5({fx(f.iqr)}) = {fx(hi_fence, 2)}.",
            "B: Concludes that 85 is greater than the boundary, so it is an outlier.",
            f"C(i): Calculates the mean without the 85: {sum(without)} / 11 = {fx(m_wo, 2)} minutes.",
            f"C(ii): Identifies the mean as affected more, supported by the change in the mean ({fx(m_all, 2)} to {fx(m_wo, 2)}) and the small change in the median ({fx(f.median)} to {fx(md_wo)}).",
            "D: Chooses the median and the IQR.",
            "D: Justifies the choice: the data have an outlier, and the median and the IQR are resistant to outliers.",
            "E: States that the median increases by 5 minutes.",
            "E: States that the IQR does not change (adding a constant does not change the variability)."),
          sample, diagram=d)

    # ----------------------------------------------------------------------------------------------------------- A4: categorical, two groups
    students = {"Earlier": 45, "Same": 75, "Later": 180}
    teachers = {"Earlier": 66, "Same": 30, "Later": 24}
    ns, nt = sum(students.values()), sum(teachers.values())
    assert (ns, nt) == (300, 120)
    rows = [(k, str(students[k]), str(teachers[k])) for k in students] + [("Total", str(ns), str(nt))]
    tab = table(["Preferred start time", "Students", "Teachers"], rows, caption="Responses to the question: Should the school day start earlier, at the same time, or later?", row_headers=True)
    rs = {k: v / ns for k, v in students.items()}
    rt = {k: v / nt for k, v in teachers.items()}
    setup = ("A school asked 300 randomly selected students and 120 randomly selected teachers whether the school day should start earlier, at the same time, or later. The table shows the numbers of responses.")
    parts = [("A", "(i) Calculate the relative frequency of the students who prefer a later start.\n\n(ii) Calculate the relative frequency of the teachers who prefer a later start."),
             ("B", "Compare the distributions of the preferences of the students and of the teachers. Use the relative frequencies, in context."),
             ("C", "A student says, \"More students than teachers prefer a later start, so students are more in favor of a later start than teachers.\" Explain why using the counts to compare the two groups is not appropriate."),
             ("D", "Identify a graphical display that could be used to compare the preferences of the students and of the teachers, and explain why it is appropriate."),
             ("E", "The principal says that most of the students prefer a later start. Is the claim supported by the data? Justify your answer.")]
    ans = [("A", f"(i) {students['Later']} / {ns} = {fx(rs['Later'], 2)}. (ii) {teachers['Later']} / {nt} = {fx(rt['Later'], 2)}."),
           ("B", f"The students prefer a later start ({fx(rs['Later'] * 100, 0)}% of the students, with only {fx(rs['Earlier'] * 100, 0)}% preferring an earlier start), but most of the teachers prefer an earlier start ({fx(rt['Earlier'] * 100, 0)}% of the teachers, with only {fx(rt['Later'] * 100, 0)}% preferring a later start). The preferences of the two groups are very different."),
           ("C", "The groups are different sizes (300 students and 120 teachers), so a larger count for the students does not mean a larger proportion. The relative frequencies should be compared instead: 0.60 is much greater than 0.20, so the student's conclusion is correct, but it has to be justified with the proportions and not with the counts."),
           ("D", "A side-by-side (or segmented) bar chart of the relative frequencies of the three responses for each group. The preferred start time is a categorical variable, and relative frequencies allow groups of different sizes to be compared."),
           ("E", f"Yes. {students['Later']} of the {ns} students ({fx(rs['Later'] * 100, 0)}%) prefer a later start, which is more than half. This applies to the students in the school because the students were selected at random.")]
    prompt, sample = frq_text(setup, parts, ans)
    B.frq(4, "ANALYZE_DATA", prompt,
          L(f"A(i): Calculates the relative frequency for the students: {students['Later']} / {ns} = {fx(rs['Later'], 2)}.",
            f"A(ii): Calculates the relative frequency for the teachers: {teachers['Later']} / {nt} = {fx(rt['Later'], 2)}.",
            f"B: Compares the groups using the relative frequencies: a much greater proportion of the students than of the teachers prefer a later start ({fx(rs['Later'], 2)} compared with {fx(rt['Later'], 2)}).",
            f"B: Describes the other part of the distributions in context: most of the teachers ({fx(rt['Earlier'], 2)}) prefer an earlier start, but few of the students ({fx(rs['Earlier'], 2)}) do.",
            "C: Explains that the groups have different sizes (300 and 120), so the counts cannot be compared directly.",
            "C: Explains that the relative frequencies (proportions) should be used to compare the two groups.",
            "D: Identifies a side-by-side (or segmented) bar chart of the relative frequencies, for the two groups.",
            "D: Explains that the variable is categorical and the relative frequencies let groups of different sizes be compared.",
            f"E: States that the claim is supported, using the relative frequency ({fx(rs['Later'], 2)}, which is greater than 0.5).",
            "E: Notes that the conclusion applies to the students of the school, since the students were randomly selected."),
          sample, diagram=tab)

    # ----------------------------------------------------------------------------------------------------------- M1: SRS, histogram, z-score, 2 SD rule
    sleep = sorted(round(v, 1) for v in [random.Random(70 + i).gauss(7.2, 1.0) for i in range(40)])
    sleep[0] = 3.6
    mu_s, sg_s = mean(sleep), sd(sleep)
    sedges = [3, 4, 5, 6, 7, 8, 9, 10, 11]
    h = histogram(sleep, sedges, "Hours of sleep on a school night", alt="Histogram of the hours of sleep of 40 students: roughly symmetric with a low value.")
    z_low = (sleep[0] - mu_s) / sg_s
    assert z_low < -2 and len(sleep) == 40
    hi_v = sleep[-1]
    setup = (f"A school has 800 students. A counselor selected a simple random sample of 40 students and asked each student how many hours the student slept on the previous school night. The histogram shows the data. The mean of the sample is {fx(mu_s, 2)} hours and the standard deviation is {fx(sg_s, 2)} hours.")
    parts = [("A", "Describe a method that the counselor could have used to select the simple random sample of 40 students from the 800 students. Include how the random numbers are used."),
             ("B", "Describe the distribution of the hours of sleep shown in the histogram. Include the shape, the center, and any unusual features."),
             ("C", f"One student in the sample slept {sleep[0]} hours. (i) Calculate the z-score for this student.\n\n(ii) Interpret the z-score in context."),
             ("D", "An outlier can be defined as a value that is more than 2 standard deviations from the mean. Does this definition identify the student who slept the least as an outlier? Show your work."),
             ("E", "To which group of students can the counselor generalize the results of the sample? Explain why.")]
    ans = [("A", "Make a list of the 800 students and number them from 1 to 800. Use a random number generator to select 40 different numbers from 1 to 800 (ignoring any repeats). The students with those numbers are the sample."),
           ("B", f"The distribution is approximately symmetric and unimodal, with a center near {fx(mu_s, 1)} hours of sleep (the mean). There is one unusually low value, a student who slept about 3.6 hours, which is separated from the others."),
           ("C", f"(i) z = ({sleep[0]} - {fx(mu_s, 2)}) / {fx(sg_s, 2)} = {fx(z_low, 2)}. (ii) This student slept {fx(abs(z_low), 2)} standard deviations less than the mean number of hours of sleep of the 40 students."),
           ("D", f"Yes. The student's value is {fx(mu_s - sleep[0], 2)} hours below the mean, and 2 standard deviations is 2({fx(sg_s, 2)}) = {fx(2 * sg_s, 2)} hours. Since {fx(mu_s - sleep[0], 2)} > {fx(2 * sg_s, 2)}, the value is an outlier by this rule."),
           ("E", "All 800 students at the school, because the sample was selected at random from the students at the school, so it is representative of them. The counselor cannot generalize to students at other schools.")]
    prompt, sample = frq_text(setup, parts, ans)
    B.frq(11, "MULTI_FOCUS", prompt,
          L("A: Describes numbering the 800 students (from 1 to 800).",
            "A: Describes using a random number generator to select 40 different numbers, and using the students with those numbers.",
            "B: Describes the shape in context: approximately symmetric and unimodal.",
            f"B: Describes the center (about {fx(mu_s, 1)} hours) and identifies the unusual low value (a student who slept about 3.6 hours).",
            f"C(i): Calculates the z-score: ({sleep[0]} - {fx(mu_s, 2)}) / {fx(sg_s, 2)} = {fx(z_low, 2)}.",
            "C(ii): Interprets the z-score in context: this student slept more than 2 standard deviations less than the mean amount of sleep of the sample.",
            f"D: Calculates 2 standard deviations ({fx(2 * sg_s, 2)} hours) and the distance of the value from the mean ({fx(mu_s - sleep[0], 2)} hours).",
            "D: Concludes that the value is an outlier by the 2 standard deviation rule, since the distance is greater than 2 standard deviations.",
            "E: States that the results can be generalized to all 800 students at the school.",
            "E: Explains that this is because the sample was selected at random (a simple random sample) from the students at the school."),
          sample, diagram=h)

    # ----------------------------------------------------------------------------------------------------------- M2: an experiment and boxplots
    r1, r2 = random.Random(3), random.Random(1)
    fert_a = sorted(round(r1.gauss(52, 5), 1) for _ in range(20))
    fert_b = sorted([round(r2.gauss(60, 5), 1) for _ in range(19)] + [78.0])
    ba, bb = box_group(fert_a, "Fertilizer A"), box_group(fert_b, "Fertilizer B")
    qa, qb = quartiles(fert_a), quartiles(fert_b)
    assert bb.get("outliers") == [78.0] and "outliers" not in ba and qb.median > qa.median + 4
    hi_fb = qb.q3 + 1.5 * qb.iqr
    d = boxplot([ba, bb], "Yield of a plant (grams)", alt="Boxplots of the yields of plants that received fertilizer A and fertilizer B; B has one high outlier.")
    setup = ("A gardener has 40 tomato plants. The gardener uses a random number generator to assign 20 of the plants to receive fertilizer A and the other 20 plants to receive fertilizer B. After the growing season, the yield of each plant, in grams, is measured. The boxplots show the distributions of the yields.\n\n"
             f"The five-number summaries are fertilizer A: {fx(qa.min)}, {fx(qa.q1)}, {fx(qa.median)}, {fx(qa.q3)}, {fx(qa.max)} and fertilizer B: {fx(qb.min)}, {fx(qb.q1)}, {fx(qb.median)}, {fx(qb.q3)}, {fx(qb.max)}.")
    parts = [("A", "(i) Identify the type of study (experiment or observational study) that the gardener conducted.\n\n(ii) Identify the response variable."),
             ("B", "Compare the distributions of the yields of the two fertilizers. Include the center and the variability."),
             ("C", f"The largest yield for fertilizer B, {fx(qb.max)} grams, is shown as a separate point. Use the 1.5 IQR rule to show that it is an outlier."),
             ("D", "Suppose that the difference in the yields is too large to be explained by chance alone. Explain why the gardener could then conclude that fertilizer B caused the greater yields."),
             ("E", "A neighbor says that the result applies to all kinds of plants in all gardens. Explain why the neighbor's statement is not justified.")]
    ans = [("A", "(i) An experiment, because the gardener assigned the treatments (the fertilizers) to the plants. (ii) The response variable is the yield of a plant, in grams."),
           ("B", f"The median yield is greater for fertilizer B ({fx(qb.median)} grams) than for fertilizer A ({fx(qa.median)} grams), so the center is higher for B. The IQR is {fx(qa.iqr)} for A and {fx(qb.iqr)} for B, so the variability of the middle 50% is similar for the two fertilizers."),
           ("C", f"For fertilizer B, the upper boundary is Q3 + 1.5(IQR) = {fx(qb.q3)} + 1.5({fx(qb.iqr)}) = {fx(hi_fb, 2)}. Since {fx(qb.max)} is greater than {fx(hi_fb, 2)}, it is an outlier."),
           ("D", "The plants were randomly assigned to the fertilizers, which creates groups that are as similar as possible in the other variables that could affect the yield. So the difference in the yields is likely caused by the fertilizers."),
           ("E", "The plants in the experiment were 40 tomato plants in one garden, and they were not randomly selected from all plants. The results apply to plants that are similar to these tomato plants, not to all kinds of plants.")]
    prompt, sample = frq_text(setup, parts, ans)
    B.frq(13, "MULTI_FOCUS", prompt,
          L("A(i): Identifies the study as an experiment (the gardener assigned the treatments).",
            "A(ii): Identifies the response variable as the yield of a plant.",
            f"B: Compares the centers using the medians ({fx(qb.median)} for fertilizer B and {fx(qa.median)} for fertilizer A): the center is higher for fertilizer B.",
            f"B: Compares the variability using the IQRs or the ranges ({fx(qa.iqr)} and {fx(qb.iqr)}): similar variability.",
            f"C: Calculates the upper boundary: {fx(qb.q3)} + 1.5({fx(qb.iqr)}) = {fx(hi_fb, 2)}.",
            f"C: Concludes that {fx(qb.max)} is greater than the boundary, so it is an outlier.",
            "D: Explains that the plants were randomly assigned to the treatments.",
            "D: Explains that random assignment makes the groups similar in other variables, so a difference in the yields can be attributed to the fertilizers (a cause-and-effect conclusion).",
            "E: Explains that the plants were not randomly selected from a larger population (all plants).",
            "E: States that the conclusion applies only to plants that are similar to those that were in the experiment."),
          sample, diagram=d)
