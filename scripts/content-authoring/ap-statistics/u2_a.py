"""Unit 2, topics 2.1 to 2.3.

Required content (CED effective Fall 2026): 2.1 a two-way (contingency) table summarizes two categorical variables, with frequencies or relative frequencies in the cells; side-by-side bar charts, segmented bar charts and mosaic plots show the
relationship by displaying each level of one variable for every level of the other; they can show whether the variables are associated. 2.2 joint relative frequency (cell / table total), marginal (row or column total / table total),
conditional (a cell / its row total or column total); compare conditional distributions for evidence of association. 2.3 random process, outcome, event, simulation (assign values by chance, record counts and the count total), probability as
long-run relative frequency, empirical estimates of probability, the law of large numbers. Skills 3.B, 3.C, 4.A, 4.B.
"""
from lib import *


def build(B):
    # ------------------------------------------------------------------------------------------------------------ 2.1
    T = 1
    cnt = [[48, 32], [30, 90]]
    tb = twoway("Grade", ["Cafeteria lunch", "Packed lunch"], ["Grade 9", "Grade 10"], cnt, caption="Preferred lunch of 200 students, by grade level")
    n9, n10 = sum(cnt[0]), sum(cnt[1])
    pk_total = cnt[0][1] + cnt[1][1]
    assert (n9, n10, pk_total) == (80, 120, 122)
    B.mcq(T, "The table shows the preferred lunch of 200 students, by grade level. How many of the students are in Grade 10 and prefer a packed lunch?",
          ch("90", "The cell in the row for Grade 10 and the column for packed lunch is 90."),
          [ch("120", "This is the row total, the number of students in Grade 10 who prefer either type of lunch."),
           ch("122", "This is the column total, the number of students in either grade who prefer a packed lunch."),
           ch("32", "This is the number of students in Grade 9 who prefer a packed lunch.")],
          "Read the cell where the row for Grade 10 meets the column for packed lunch: 90 students.", diagram=tb, difficulty="easy")

    B.mcq(T, "Which of the following displays can be used to show the relationship between two categorical variables?",
          ch("A segmented bar chart, with one bar for each level of the first variable divided into segments for the levels of the second variable",
             "A segmented bar chart shows the distribution of one categorical variable within each level of the other."),
          [ch("A histogram, with each bar showing the frequency of the values of the first variable that fall in an interval of the number line",
              "A histogram displays the distribution of a single quantitative variable."),
           ch("A boxplot, with a box showing the middle 50% of the values of the first variable for each of the categories",
              "A boxplot summarizes a quantitative variable using its five-number summary."),
           ch("A dotplot, with one dot for each of the individuals above the values of the first variable on a number line",
              "A dotplot shows the values of one quantitative variable.")],
          "Side-by-side bar charts, segmented bar charts and mosaic plots display two categorical variables.", difficulty="easy")

    rel = [[c / n9 for c in cnt[0]], [c / n10 for c in cnt[1]]]
    assert [round(v, 2) for v in rel[0]] == [0.60, 0.40] and [round(v, 2) for v in rel[1]] == [0.25, 0.75]
    bg = bars(["Grade 9", "Grade 10"], [rel[0][0], rel[1][0]], "Grade level", "Relative frequency", y_max=1.0, series_label="Cafeteria lunch",
              extra=([rel[0][1], rel[1][1]], "Packed lunch"), alt="Side-by-side bar chart of the relative frequencies of the preferred lunch, for each grade level: Grade 9 cafeteria 0.60, packed 0.40; Grade 10 cafeteria 0.25, packed 0.75.")
    B.mcq(T, "The side-by-side bar chart shows, for the students in each grade level, the proportion who prefer a cafeteria lunch and the proportion who prefer a packed lunch. Which of the following statements is supported by the graph?",
          ch("A greater proportion of the students in Grade 10 than of the students in Grade 9 prefer a packed lunch",
             "The bar for packed lunch is 0.75 for Grade 10 and 0.40 for Grade 9."),
          [ch("A greater proportion of the students in Grade 9 than of the students in Grade 10 prefer a packed lunch",
              "The Grade 9 bar for packed lunch (0.40) is shorter than the Grade 10 bar (0.75)."),
           ch("The same proportion of the students in each grade prefer a packed lunch, because the bars for each grade add to 1",
              "The bars add to 1 within each grade, but the packed lunch bars are not the same height."),
           ch("There are more students in Grade 10 than in Grade 9, because the Grade 10 bar for packed lunch is taller",
              "The graph shows relative frequencies within each grade, so it does not show the number of students in a grade.")],
          "The graph compares the distribution of lunch preference across the levels of grade: 0.75 compared with 0.40 prefer a packed lunch.", diagram=bg, difficulty="medium")

    B.mcq(T, "In a segmented bar chart, there is one bar for each grade level, and each bar is divided into segments for the preferred lunch. The segments are in about the same proportions in every bar. Which of the following is the best conclusion?",
          ch("There is little or no evidence of an association between the grade level and the preferred lunch",
             "If the distribution of one variable is about the same at every level of the other variable, the variables do not appear to be associated."),
          [ch("There is strong evidence of an association between the grade level and the preferred lunch",
              "An association would show as segments with different proportions from one bar to another."),
           ch("The grade level causes the students to have the preferred lunch that they have",
              "A graph of two categorical variables cannot show that one variable causes the other."),
           ch("The bars have the same number of students in each of the grade levels in the chart",
              "The proportions can be the same even when the bars are for groups of different sizes.")],
          "The variables are associated when the distribution of one changes across the levels of the other; here it does not change.", difficulty="medium")

    tb2 = twoway("Grade", ["Cafeteria lunch", "Packed lunch"], ["Grade 9", "Grade 10"], cnt, caption="Preferred lunch of 200 students, by grade level")
    B.mcq(T, "A student looks at the table and says, \"More students in Grade 10 prefer a packed lunch than in Grade 9, since 90 is greater than 32, so Grade 10 students are more likely to prefer a packed lunch.\" Which of the following is the best response?",
          ch("The groups are different sizes, so the student should compare the proportions: 90 / 120 = 0.75 for Grade 10 and 32 / 80 = 0.40 for Grade 9",
             "Counts from groups of different sizes should be compared using relative frequencies. Here the conclusion is correct but the reason is not."),
          [ch("The student is correct, because a greater count always shows a greater proportion in two groups of any sizes that the student compares",
              "A greater count does not show a greater proportion when the groups have different sizes."),
           ch("The student is incorrect, because the proportions are 0.75 for Grade 9 and 0.40 for Grade 10 in this table",
              "The proportion who prefer a packed lunch is 0.75 for Grade 10 and 0.40 for Grade 9."),
           ch("The student cannot compare the grades, because a two-way table cannot be used to compare two groups of students",
              "A two-way table is used to compare the distributions of one variable across the levels of another.")],
          "To justify a claim about two groups of different sizes, compare relative frequencies: 0.75 and 0.40.", diagram=tb2, difficulty="medium")

    B.mcq(T, "What do the entries in the cells of a two-way table show?",
          ch("The frequency (count) or the relative frequency of the individuals that have a particular level of each of the two categorical variables",
             "Each cell is for one combination of a level of one variable and a level of the other."),
          [ch("The mean of a quantitative variable for the individuals in each of the groups that are formed by the two categorical variables in the table",
              "Cells of a two-way table are counts or proportions, not means of a quantitative variable."),
           ch("The correlation between the two variables for the individuals that have each of the levels of the first variable",
              "A correlation is for two quantitative variables."),
           ch("The five-number summary of the values of one of the variables for each of the levels of the other variable",
              "A five-number summary is for a quantitative variable.")],
          "The entries in the cells are frequencies or relative frequencies.", difficulty="easy")

    B.mcq(T, "A researcher records, for 300 adults, whether each lives in a city or in the country, and whether each prefers to read books on paper or on a screen. The numbers of adults in the two living groups are not equal. Which of the following displays is best for comparing the reading preference of the two living groups?",
          ch("A segmented bar chart of relative frequencies, with one bar for each living group and the segments showing the proportions that prefer paper and screen",
             "Relative frequencies adjust for groups of different sizes, so the segments can be compared directly."),
          [ch("A segmented bar chart of counts, because the heights of the segments for the two groups can be compared directly",
              "When the groups have different sizes, counts are hard to compare."),
           ch("A histogram of the number of adults in each of the living groups, with the bars placed next to each other",
              "A histogram is for a quantitative variable."),
           ch("A boxplot of the reading preferences, with one box for each of the living groups that the researcher studied",
              "A boxplot is for a quantitative variable.")],
          "To compare the distribution of one variable across groups of different sizes, use relative frequencies.", difficulty="hard")

    # ------------------------------------------------------------------------------------------------------------ 2.2
    T = 2
    news = [[120, 50, 30], [60, 80, 60]]
    nt = twoway("Age group", ["Online", "Television", "Print"], ["Under 40", "40 or over"], news, caption="Main way of getting news, for 400 adults")
    tot = sum(map(sum, news))
    assert tot == 400 and [sum(r) for r in news] == [200, 200] and [news[0][c] + news[1][c] for c in range(3)] == [180, 130, 90]
    B.mcq(T, "The table shows the main way of getting news of 400 adults, by age group. What is the joint relative frequency of adults who are under 40 and get their news mainly online?",
          ch("0.30", "A joint relative frequency is a cell divided by the table total: 120 / 400 = 0.30."),
          [ch("0.60", "This is the conditional relative frequency among the adults under 40: 120 / 200."),
           ch("0.45", "This is the marginal relative frequency of getting news online: 180 / 400."),
           ch("0.67", "This is the conditional relative frequency among the adults who get news online: 120 / 180.")],
          "Joint relative frequency = 120 / 400 = 0.30.", diagram=nt, difficulty="easy")

    B.mcq(T, "The table shows the main way of getting news of 400 adults, by age group. What is the marginal relative frequency of adults who get their news mainly online?",
          ch("0.45", "A marginal relative frequency is a column total divided by the table total: 180 / 400 = 0.45."),
          [ch("0.30", "This is the joint relative frequency of adults who are under 40 and get news online: 120 / 400."),
           ch("0.60", "This is the proportion of the adults under 40 who get news online, a conditional relative frequency."),
           ch("0.90", "This is 180 / 200, which divides the column total by the size of only one of the age groups.")],
          "Marginal relative frequency = 180 / 400 = 0.45.", diagram=nt, difficulty="easy")

    B.mcq(T, "The table shows the main way of getting news of 400 adults, by age group. Among the adults who are under 40, what proportion get their news mainly online?",
          ch("0.60", "Restrict to the row for adults under 40 and divide the cell by the row total: 120 / 200 = 0.60."),
          [ch("0.30", "This divides by the table total (400), which is the joint relative frequency."),
           ch("0.67", "This restricts to the adults who get news online instead of to the adults under 40: 120 / 180."),
           ch("0.45", "This is the proportion of all of the adults who get news online, which ignores age.")],
          "Conditional relative frequency = 120 / 200 = 0.60.", diagram=nt, difficulty="medium")

    B.mcq(T, "The table shows the main way of getting news of 400 adults, by age group. Among the adults who get their news mainly online, what proportion are under 40?",
          ch("0.67", "Restrict to the column for online and divide the cell by the column total: 120 / 180 = 0.67."),
          [ch("0.60", "This restricts to the adults under 40 instead of to the adults who get news online: 120 / 200."),
           ch("0.30", "This divides by the table total (400), which is the joint relative frequency."),
           ch("0.33", "This is the proportion of the adults who get news online who are 40 or over: 60 / 180.")],
          "Conditional relative frequency = 120 / 180, which is about 0.67.", diagram=nt, difficulty="medium")

    rows3 = [("Under 40", news[0]), ("40 or over", news[1])]
    cond = [[v / sum(r) for v in r] for _, r in rows3]
    assert [round(v, 2) for v in cond[0]] == [0.60, 0.25, 0.15] and [round(v, 2) for v in cond[1]] == [0.30, 0.40, 0.30]
    B.mcq(T, "The table shows the main way of getting news of 400 adults, by age group. Which of the following is a correct comparison of the two age groups?",
          ch("The adults under 40 are more likely to get their news mainly online, because 60% of them do, compared with 30% of the adults who are 40 or over",
             "The conditional relative frequencies, 120 / 200 and 60 / 200, show that the distributions differ, which is evidence of an association."),
          [ch("The adults who are 40 or over are more likely to get their news mainly online, because 80 is the greatest count in their row",
              "The 80 is the count for television. Online is 60 of the 200 adults who are 40 or over, which is 30%."),
           ch("The adults under 40 are more likely to get their news mainly from print, because 30% of them do, compared with 15% of the adults who are 40 or over",
              "This is reversed. Print is 30 of 200 (15%) for the adults under 40 and 60 of 200 (30%) for the adults who are 40 or over."),
           ch("The two age groups have the same distribution of the main way of getting news, because each age group has 200 adults",
              "The group sizes are equal, but the distributions of the main way are different.")],
          "Compare the conditional distributions: online 0.60 and 0.30, television 0.25 and 0.40, print 0.15 and 0.30.", diagram=nt, difficulty="medium")

    same = [[60, 40], [90, 60]]
    ts = twoway("Class", ["Passed", "Did not pass"], ["Class 1", "Class 2"], same, caption="Results of an exam in two classes")
    assert same[0][0] / sum(same[0]) == same[1][0] / sum(same[1]) == 0.6
    B.mcq(T, "The table shows the results of an exam in two classes. Which of the following is the best conclusion about the relationship between the class and passing the exam?",
          ch("There is no evidence of an association, because the proportion who passed is 0.60 in each class",
             "The conditional relative frequencies are 60 / 100 = 0.60 and 90 / 150 = 0.60, the same for both classes."),
          [ch("There is evidence of an association, because more students in Class 2 passed the exam than in Class 1",
              "The counts are different because the classes have different sizes. The proportions that passed are equal."),
           ch("There is evidence of an association, because the number who did not pass is different in the two classes",
              "The counts differ only because the classes have different sizes. The proportions that did not pass are both 0.40."),
           ch("The evidence of an association cannot be found, because a two-way table has no relative frequencies in it",
              "Relative frequencies can be calculated from the counts of a two-way table.")],
          "Equal conditional distributions (0.60 passed in each class) show no association between class and passing.", diagram=ts, difficulty="medium")

    miss = twoway("Age group", ["Online", "Television", "Print"], ["Under 40", "40 or over"], news, caption="Main way of getting news, for 400 adults", hide={(1, 1)})
    B.mcq(T, "A table of the main way of getting news of 400 adults shows the row and column totals, but one entry is missing. What is the missing entry?",
          ch("80", "The row total for the adults who are 40 or over is 200, and 60 + 60 = 120 are the other entries, so the missing entry is 200 - 120 = 80. The column total, 130, gives 130 - 50 = 80 as well."),
          [ch("70", "This does not agree with the totals. The row must add to 200: 60 + 70 + 60 = 190."),
           ch("130", "This is the column total for television, not the entry for one age group."),
           ch("50", "This is the number of adults under 40 who get news from television, in the same column.")],
          "Use the totals: 200 - 60 - 60 = 80, and 130 - 50 = 80.", diagram=miss, difficulty="medium")

    B.mcq(T, "In a two-way table of 400 adults, 120 are under 40 and get their news mainly online, 200 are under 40, and 180 get their news mainly online. Which of the following expressions is a conditional relative frequency?",
          ch("120 / 180, the proportion of the adults who get news online who are under 40", "A conditional relative frequency divides a cell by the total for the row or the column of interest."),
          [ch("120 / 400, the proportion of all of the adults who are under 40 and get news online", "This divides by the table total, so it is a joint relative frequency."),
           ch("180 / 400, the proportion of all of the adults who get news online", "This is a column total divided by the table total, a marginal relative frequency."),
           ch("200 / 400, the proportion of all of the adults who are under 40", "This is a row total divided by the table total, a marginal relative frequency.")],
          "Conditional: restrict to a level (the 180 who get news online) and divide by that total: 120 / 180.", difficulty="easy")

    ut = [[40, 20], [30, 60]]
    t2 = twoway("Plan", ["Renewed", "Did not renew"], ["Basic plan", "Premium plan"], ut, caption="Membership renewals at a gym")
    r_b, r_p = ut[0][0] / sum(ut[0]), ut[1][0] / sum(ut[1])
    assert (round(r_b, 3), round(r_p, 3)) == (0.667, 0.333)
    B.mcq(T, "The table shows whether the members of a gym renewed their membership, by type of plan. Which of the following statements is supported by the summary statistics?",
          ch("The members of the basic plan were more likely to renew, because 2/3 of the basic plan members renewed and 1/3 of the premium plan members renewed",
             "The conditional relative frequencies of renewing are 40 / 60 and 30 / 90, about 0.67 and 0.33."),
          [ch("The members of the premium plan were more likely to renew than the members of the basic plan, because the premium plan has more members in it, and 90 is greater than 60",
              "The number of members in a plan does not decide the proportion who renewed."),
           ch("The two plans had the same proportion of the members who renewed, because 40 and 30 are close in the table",
              "The proportions are 0.67 and 0.33, which are not the same."),
           ch("The members of the basic plan were less likely to renew than the members of the premium plan, because 40 members renewed and 60 members did not renew, and 60 is greater than 40",
              "The 60 is the number of members in the basic plan, 40 + 20, and not the number who did not renew.")],
          "Compare the conditional relative frequencies of renewing: 40 / 60 for basic and 30 / 90 for premium.", diagram=t2, difficulty="medium")

    B.mcq(T, "In a survey, 0.15 of all of the 400 adults are 40 or over and get their news mainly from print. A student says, \"This means that 15% of the adults who are 40 or over get their news mainly from print.\" What is the error in the statement?",
          ch("The 0.15 is a joint relative frequency, based on all 400 adults. The proportion of the adults who are 40 or over who get news from print is 60 / 200 = 0.30, a conditional relative frequency",
             "To describe a group, divide by the total for that group. The group of adults who are 40 or over has 200 adults."),
          [ch("The 0.15 is a marginal relative frequency, so it describes the adults who get news from print, whatever their age",
              "A marginal relative frequency divides a row total or a column total by the table total. The 0.15 uses a single cell."),
           ch("There is no error, because a relative frequency always describes the group that it is about, whatever the total used",
              "The total used to divide matters: a joint relative frequency describes all of the individuals in the table."),
           ch("The 0.15 should be a percent of the adults under 40, because print is a way of getting news that is chosen only by younger adults",
              "Nothing in the statement or the table limits print to younger adults.")],
          "A joint relative frequency is out of the whole table; the proportion within the 40-or-over group is 60 / 200 = 0.30.", difficulty="hard")

    # ------------------------------------------------------------------------------------------------------------ 2.3
    T = 3
    B.mcq(T, "A spinner is spun 1,000 times and lands on red 312 times. Which of the following is the best estimate of the probability that the spinner lands on red on a single spin?",
          ch("0.312", "The probability of an outcome is estimated by its relative frequency over a large number of trials: 312 / 1,000."),
          [ch("312", "This is the number of times that the spinner landed on red, not a probability."),
           ch("0.50", "A probability of 0.50 would be right only if red and not red were equally likely, and nothing says that."),
           ch("0.688", "This is the relative frequency of the spins that did not land on red.")],
          "Estimated probability = 312 / 1,000 = 0.312.", difficulty="easy")

    B.mcq(T, "Which of the following statements best describes the law of large numbers?",
          ch("For independent trials, as the number of trials increases, the relative frequency of an outcome gets closer and closer to a single value",
             "The single value is the probability of the outcome."),
          [ch("After a long run of one outcome, the other outcomes become more likely, so the results balance out over the next few trials",
              "Independent trials do not remember earlier results, so the next trial is not affected."),
           ch("In any set of independent trials, the number of times that an outcome occurs is equal to the probability times the number of trials",
              "The count only tends to be close to this value, and it need not be equal to it."),
           ch("In a small number of trials the relative frequency of an outcome is always equal to the probability of the outcome",
              "A relative frequency from a small number of trials can be far from the probability.")],
          "The law of large numbers is about relative frequencies of independent trials getting closer to a single value.", difficulty="medium")

    B.mcq(T, "A basketball player makes 70% of free throws. A student plans to use a random digit table, in which each of the digits 0 to 9 is equally likely, to simulate one free throw by this player. Which of the following assignments is appropriate?",
          ch("Let the digits 0 through 6 represent a made free throw and the digits 7 through 9 represent a missed free throw",
             "Seven of the ten digits have probability 0.70, and three of the ten have probability 0.30."),
          [ch("Let the digits 0 through 7 represent a made free throw and the digits 8 and 9 represent a missed free throw",
              "Eight of the ten digits have probability 0.80, not 0.70."),
           ch("Let the digits 0 through 2 represent a made free throw and the digits 3 through 9 represent a missed free throw",
              "Three of the ten digits have probability 0.30, which would be the probability of a miss."),
           ch("Let the digits 0 through 4 represent a made free throw and the digits 5 through 9 represent a missed free throw",
              "Five of the ten digits have probability 0.50, so a made free throw would be as likely as a miss.")],
          "The digits assigned to a made free throw must have probability 0.70: seven of the ten digits.", difficulty="medium")

    B.mcq(T, "To estimate the probability that a family with 3 children has exactly 2 girls, a student lets each odd digit in a random digit table represent a girl and each even digit represent a boy. Which of the following describes one trial of the simulation?",
          ch("Read 3 digits and count how many of them are odd. Record whether the count is exactly 2",
             "A trial simulates one family: three children, each with a probability of 0.5 of being a girl."),
          [ch("Read 1 digit and record whether it is odd, and repeat this until the student has found exactly 2 odd digits in a row",
              "A trial must model one family with 3 children, not a run of digits."),
           ch("Read 3 digits and add them. Record whether the sum is exactly 2",
              "The sum of the digits does not count the children who are girls."),
           ch("Read 2 digits and record whether both of them are odd, as an estimate for 2 girls in a family of 3",
              "A family has 3 children, so 3 digits should be read in a trial.")],
          "Each trial reads three digits (one for each child), counts the odd ones, and records whether the count is 2.", difficulty="medium")

    rng = np.random.default_rng(11)
    made = sorted(int(v) for v in rng.binomial(10, 0.7, 40))
    ge8 = sum(1 for v in made if v >= 8)
    assert 10 <= ge8 <= 20 and len(set(made)) >= 5, (ge8, made)
    dp = dotplot(made, "Free throws made in 10 attempts", axis=(0, 10, 1), alt="Dotplot of the number of free throws made out of 10, in each of 40 simulated trials.")
    B.mcq(T, f"A player makes 70% of free throws. The dotplot shows the number of free throws made out of 10 attempts in each of 40 simulated trials. Based on the simulation, what is the estimated probability that the player makes at least 8 of 10 free throws?",
          ch(f"{ge8 / 40:.3f}", f"{ge8} of the 40 trials had 8 or more made free throws: {ge8} / 40."),
          [ch(f"{made.count(8) / 40:.3f}", f"This counts only the trials with exactly 8 made free throws: {made.count(8)} / 40."),
           ch(f"{ge8}", f"This is the number of trials with at least 8 made free throws, not a probability."),
           ch(f"{(40 - ge8) / 40:.3f}", f"This is the relative frequency of the trials with fewer than 8 made free throws: {40 - ge8} / 40.")],
          f"Estimated probability = {ge8} / 40 = {ge8 / 40:.3f}.", diagram=dp, difficulty="medium")

    B.mcq(T, "The probability that a certain bus arrives late is 0.20. Which of the following is a correct interpretation of this probability?",
          ch("Over a very large number of days, the bus arrives late on about 20% of the days", "A probability is the long-run relative frequency of an outcome."),
          [ch("The bus arrives late on exactly 1 day out of every 5 days, so after 4 days on time the next day it will be late",
              "Probability describes the long run. It does not guarantee a pattern in a short run."),
           ch("The bus arrives late on 20 days out of every 100 days, with the same number of late days in every set of 100 days",
              "The number of late days varies from one set of days to another. Only the long-run proportion is about 20%."),
           ch("The bus arrives on time on 20% of the days, because 0.20 is the probability that the bus arrives at the stop",
              "The 0.20 is the probability that the bus is late.")],
          "A probability of 0.20 means that, in the long run, about 20% of the days the bus arrives late.", difficulty="easy")

    B.mcq(T, "Which of the following is an event, but is not a single outcome, when a fair six-sided die is rolled once?",
          ch("Rolling an odd number", "An event is a collection of outcomes. Rolling an odd number is made up of the outcomes 1, 3 and 5."),
          [ch("Rolling a 3", "This is a single outcome, the result of one trial."),
           ch("Rolling a 6", "This is a single outcome, the result of one trial."),
           ch("Rolling the die one time", "This is the random process, not a result of it.")],
          "An event is a collection of outcomes; rolling an odd number is {1, 3, 5}.", difficulty="easy")

    boys = [12, 48, 74, 50, 16]
    assert sum(boys) == 200
    ge3 = sum(boys[3:])
    tb = table(["Number of boys", "0", "1", "2", "3", "4"], [["Number of trials"] + [str(v) for v in boys]], caption="Results of 200 simulated families with 4 children", row_headers=True)
    B.mcq(T, "The table shows the number of boys in each of 200 simulated families with 4 children. Based on the simulation, what is the estimated probability that a family with 4 children has at least 3 boys?",
          ch(f"{ge3 / 200:.2f}", f"The trials with 3 or 4 boys number {boys[3]} + {boys[4]} = {ge3}, and {ge3} / 200 = {ge3 / 200:.2f}."),
          [ch(f"{boys[3] / 200:.2f}", f"This counts only the families with exactly 3 boys: {boys[3]} / 200."),
           ch(f"{boys[4] / 200:.2f}", f"This counts only the families with 4 boys: {boys[4]} / 200."),
           ch(f"{sum(boys[:3]) / 200:.2f}", f"This is the relative frequency of the families with at most 2 boys: {sum(boys[:3])} / 200.")],
          f"Estimated probability = ({boys[3]} + {boys[4]}) / 200 = {ge3 / 200:.2f}.", diagram=tb, difficulty="medium")
