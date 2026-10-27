"""Unit 1, topics 1.1 to 1.4 (33 questions).

Required content (CED effective Fall 2026): 1.1 a statistical study collects data from a SAMPLE to answer an investigative question about a larger POPULATION; N and n; a study is needed when the population is too large
or hard to measure; datum and data set; "in context"; an investigative question has a defined purpose, is not changed after seeing the results, and can be answered with data that can be collected. 1.2 observational unit,
variable, parameter (population) and statistic (sample; need not equal the parameter), categorical and quantitative, discrete and continuous. 1.3 frequency and relative frequency tables; percentages, relative frequencies and
ratios give the same information as proportions; counts and relative frequencies justify claims. 1.4 bar charts and pie charts (slices' areas add to 100%); compare data sets on a categorical variable; justify claims.
"""
from lib import *


def build(B):
    # ------------------------------------------------------------------------------------------------------------ 1.1
    T = 1
    B.mcq(T, "A city has 400,000 residents. The transportation department wants to know the mean time that its residents spend commuting each day. Which of the following is the best reason for the department to use a statistical study instead of collecting data from every resident?",
          ch("It would be too difficult and costly to collect data from all of the residents, so data from a sample are used to answer the question about the population", "Statistical studies are necessary when the population is too large or too difficult to collect data from every individual."),
          [ch("A statistical study always gives the exact value of the mean commuting time for the population, which a count of every resident would not", "A sample gives an estimate, not the exact value for the population."),
           ch("Data collected from a sample are always more accurate than data that are collected from every one of the residents in the population", "Collecting data from every individual is not less accurate. It is just usually impractical."),
           ch("A statistical study is required by law whenever the question of an investigation involves more than one thousand people in a city", "No such requirement applies. The reason is that a study of the whole population is not practical.")],
          "A statistical study is used when the population is too large, or collecting data from everyone is too difficult.", difficulty="easy")

    B.mcq(T, "The principal of a school with 1,800 students wants to estimate the mean number of hours that students at the school sleep on school nights. The principal surveys 120 students who were randomly chosen. Which of the following correctly identifies the population and the sample?",
          ch("The population is all 1,800 students at the school, and the sample is the 120 students who were surveyed", "The population is the whole group of interest. The sample is the subset from which data were obtained."),
          [ch("The population is the 120 students who were surveyed, and the sample is all 1,800 students at the school", "These are reversed. The sample is the smaller group that is studied."),
           ch("The population is the hours of sleep of the students, and the sample is the 120 students who were randomly chosen", "The population consists of the individuals of interest, not the values that are measured."),
           ch("The population is the principal of the school, and the sample is the 120 students who were surveyed", "The principal collects the data. The population is the students.")],
          "The population is all of the items or individuals of interest (the 1,800 students). The sample is the subset that was studied (the 120).", difficulty="easy")

    B.mcq(T, "A town has 6,500 registered voters. A polling firm contacts 400 of the registered voters. Which of the following gives the population size N and the sample size n?",
          ch("N = 6,500 and n = 400", "N is the population size and n is the sample size."),
          [ch("N = 400 and n = 6,500", "These are reversed."),
           ch("N = 6,900 and n = 400", "The sample is part of the population. The sizes are not added."),
           ch("N = 6,500 and n = 6,100", "n is the number contacted, which is 400. 6,100 is the number who were not contacted.")],
          "N is the number in the population (6,500). n is the number in the sample (400).", difficulty="easy")

    B.mcq(T, "A researcher planned to investigate whether a tutoring program improves students' scores on a math test. After seeing that the scores had not improved, the researcher decided to ask a different question: whether the program improves students' reading scores. Which of the following statements is correct?",
          ch("The researcher should keep the original question, because an investigative question should have a defined purpose and not be changed based on the results of the analysis", "Changing the question after seeing the data makes the results hard to interpret."),
          [ch("The researcher may change the question at any time, because a better question is always the one with a result that is significant", "A question should be chosen before the analysis and not by which result looks better."),
           ch("The researcher must change the question, because a study with a result that shows no improvement does not answer any question", "A result of no improvement answers the original question."),
           ch("The researcher should collect new data on the reading scores, because the data on math scores can answer only the reading question", "The data on math scores answer the original question about math scores.")],
          "An investigative question should have a defined purpose and should not be changed based on the results of the analysis.", difficulty="medium")

    B.mcq(T, "Which of the following is an investigative question that can be answered by collecting and analyzing data?",
          ch("Do students at a school who eat breakfast have a higher mean score on a morning quiz than students who do not eat breakfast?", "The variables can be measured and the data can be collected and analyzed."),
          [ch("Is it fair for a school to give a quiz to its students at the beginning of the morning on every day of the week, or is it too much?", "This asks about an opinion about fairness. It does not define data to collect."),
           ch("Why do some people enjoy listening to music more than other people enjoy listening to music when they study?", "This does not define variables or data that could be collected."),
           ch("Is mathematics the best subject for a student to study at a high school, college, or university in the future?", "This is an opinion. There is no variable that can be measured.")],
          "A question should be posed so that the required data can be collected and analyzed.", difficulty="medium")

    B.mcq(T, "A study of 100 students reports that the mean amount of sleep on a school night was 7.2 hours. Which of the following is a statement of this result in context?",
          ch("The mean amount of sleep on a school night for the 100 students in the study was 7.2 hours", "It names the variable (sleep on a school night), the group (the 100 students) and the units."),
          [ch("The mean was 7.2, which is the value that was found when the data from the students were added and divided by the sample size", "This describes the calculation, but it does not say what the 7.2 is about."),
           ch("Each of the 100 students in the study slept for exactly 7.2 hours on a school night, which is the mean of the sleep data", "A mean does not mean that every student slept for that long."),
           ch("The mean amount of sleep for all of the students in the world on a school night is 7.2 hours, according to the study", "The study included 100 students. It does not give the mean for all students in the world.")],
          "Interpreting in context means relating the number to the variable, the group and the units from the situation.", difficulty="medium")

    B.mcq(T, "In a statistical study, what is a collection of data called?",
          ch("A data set", "A datum is a piece of information about an item or individual. A collection of data is called a data set."),
          [ch("A parameter", "A parameter is a numerical summary of a population."),
           ch("A population", "A population is all of the items or individuals of interest."),
           ch("A datum", "A datum is a single piece of information. A collection of data is a data set.")],
          "A collection of data is called a data set.", difficulty="easy")

    # ------------------------------------------------------------------------------------------------------------ 1.2
    T = 2
    rows = [("Maya", "10", "3.4", "Chess"), ("Jon", "11", "2.9", "Band"), ("Priya", "9", "3.8", "None"), ("Luis", "12", "3.1", "Chess"), ("Ava", "10", "3.6", "Drama")]
    tab = table(["Student", "Grade level", "GPA", "Club"], rows, caption="Data on 5 students")
    B.mcq(T, "The table shows some data from a study of students at a school. What is the observational unit in this data set?",
          ch("A student at the school, because each row of the table gives the data collected from one student", "An observational unit is the item or individual from which a datum is collected."),
          [ch("A grade level, because it is the first variable listed in the table after the names of the students", "Grade level is a variable. It changes from one student to another."),
           ch("The GPA of a student, because it is the numerical variable in the data set and it is measured for every student", "GPA is a variable that is measured on each observational unit. It is not the unit."),
           ch("The school, because all five students in the table were selected from the one school that is in the study", "The data are collected from each student, so the student is the unit.")],
          "Each row describes one student, so the observational unit is a student.", diagram=tab, difficulty="easy")

    B.mcq(T, "A polling firm surveys 400 randomly selected voters in a state and finds that 54% of them support a ballot measure. Which of the following describes the value 54%?",
          ch("A statistic, because it is a numerical summary of a variable for a sample of voters, not for the whole population of the state", "A statistic is a numerical summary for a sample. Here it summarizes the 400 voters."),
          [ch("A parameter, because it is the percent of voters that was found by the polling firm in the study of the state", "A parameter summarizes a population. The 54% describes only the 400 voters."),
           ch("A parameter, because it is a percent and all percents describe the whole population from which a sample is taken", "A percent from a sample is a statistic."),
           ch("A variable, because it is a characteristic that changes from one voter in the sample to another voter in the sample", "A variable is a characteristic that changes from one unit to another. 54% is a single summary.")],
          "A numerical summary of a sample is a statistic.", difficulty="easy")

    B.mcq(T, "The school district has 3,200 students. The district reports that the proportion of all of its students who walk to school is 0.18. Which of the following describes the value 0.18?",
          ch("A parameter, because it is a numerical summary of a variable for the whole population of students in the district", "The 0.18 summarizes all 3,200 students (the population), so it is a parameter."),
          [ch("A statistic, because a proportion is always calculated from a sample of the students in the population", "A proportion can describe a population. Here all of the students are included."),
           ch("A statistic, because it is a number that is between 0 and 1 and is calculated from the data that the district has collected", "Being between 0 and 1 does not make it a statistic. The group is the population."),
           ch("A categorical variable, because the students either walk to school or they do not walk to school each day", "The variable (how a student gets to school) is categorical, but 0.18 is a summary of it for the population.")],
          "A numerical summary of a variable for a whole population is a parameter.", difficulty="medium")

    B.mcq(T, "A random sample of 150 adults in a city is used to find the proportion of adults who own a bicycle. Which of the following statements about the sample proportion and the population proportion is correct?",
          ch("The sample proportion is a statistic. Its value is often not equal to the population proportion, but it can be used to make inferences about it", "The value of a statistic is often not equal to the parameter, but it may provide the basis for inferences about the parameter."),
          [ch("The sample proportion is a parameter, because it was found by using a random sample of the adults who live in the city", "A value from a sample is a statistic, even if the sample is random."),
           ch("The sample proportion is a statistic, and it is always exactly equal to the proportion of the population that is estimated", "A statistic is usually not exactly equal to the parameter."),
           ch("The sample proportion is a statistic, and it cannot be used to learn anything at all about the proportion of the population of adults in the city", "Statistics can be used to make inferences about parameters.")],
          "A statistic is a summary of a sample. It is often not equal to the unknown parameter but can be used to make inferences about it.", difficulty="medium")

    B.mcq(T, "Which of the following variables is categorical?",
          ch("The postal code of a student's home address", "A postal code is a label for a group, so it is categorical even though it is written with digits."),
          [ch("The number of siblings that a student has", "This is a count, so it is quantitative."),
           ch("The height of a student, in inches", "This is a measured quantity with units, so it is quantitative."),
           ch("The time that a student takes to run a mile", "This is a measured quantity with units, so it is quantitative.")],
          "A categorical variable takes values that are category names or group labels, such as postal codes.", difficulty="medium")

    B.mcq(T, "Which of the following variables is continuous?",
          ch("The time, in seconds, that a runner takes to finish a 100-meter race", "A continuous variable can take any value in an interval. Time can be any value between two times."),
          [ch("The number of goals that a soccer team scores in one game of the season", "This can only be a whole number, so it is discrete."),
           ch("The number of pets that a family in a neighborhood owns at this time", "This can only be a whole number, so it is discrete."),
           ch("The number of students in a class who are absent today", "This can only be a whole number, so it is discrete.")],
          "A continuous quantitative variable can take any value in an interval. Counts are discrete.", difficulty="easy")

    B.mcq(T, "Which of the following variables is quantitative?",
          ch("The weight, in ounces, of a package that a company ships", "It is a measured amount with units."),
          [ch("The identification number that a school gives to each student", "An ID number is a label for a student. It is a categorical variable."),
           ch("The number on the back of the jersey of a basketball player", "A jersey number is a label, so it is a categorical variable."),
           ch("The area code of the telephone number of a customer", "An area code is a label for a region, so it is a categorical variable.")],
          "A quantitative variable takes numerical values for a measured or counted quantity. Labels written with digits are categorical.", difficulty="medium")

    tab = table(["Dog", "Breed", "Weight (lb)", "Age (years)", "Owner has a fence"], [("Rex", "Beagle", "24", "3", "Yes"), ("Mia", "Poodle", "18", "7", "No"), ("Bo", "Boxer", "62", "5", "Yes"), ("Zed", "Beagle", "27", "2", "No")], caption="Data on 4 dogs", row_headers=True)
    B.mcq(T, "The table shows data on four dogs. How many of the variables in the table are quantitative?",
          ch("Two, because weight and age are measured quantities with units, and the other variables are labels or categories", "Weight (pounds) and age (years) are quantitative."),
          [ch("Three, because the age, the weight, and the name of each dog are all values that can be put in order", "The names are labels, so they are categorical."),
           ch("Four, because the breed and the fence information are values that are recorded for every one of the dogs", "Breed and whether the owner has a fence are categorical."),
           ch("One, because only the weight of a dog is measured with units while the age is a count of the years", "Age in years is also a quantitative variable with units.")],
          "Weight and age are quantitative. Breed and fence are categorical (and the dog's name is a label).", diagram=tab, difficulty="easy")

    B.mcq(T, "A biologist records the species and the height, in meters, of each of 60 trees in a forest. Which of the following correctly describes the variables?",
          ch("Species is a categorical variable, and height is a continuous quantitative variable that can take any value", "Species names are categories. Height is a measurement that can take any value in an interval."),
          [ch("Species is a quantitative variable, and height is a categorical variable that can be grouped into short and tall", "Species is a category name, and height is a measurement."),
           ch("Species is a categorical variable, and height is a discrete quantitative variable because it is recorded in meters", "Height can take any value in an interval, so it is continuous."),
           ch("Both species and height are categorical variables, because the observational units are trees and not people", "Height is a measured quantity, so it is quantitative.")],
          "Species is categorical. Height is a measured quantity that can take any value in an interval: continuous.", difficulty="medium")

    # ------------------------------------------------------------------------------------------------------------ 1.3
    T = 3
    B.mcq(T, "In a survey of 200 students, 80 students said that pizza is their favorite lunch. What is the relative frequency of students who chose pizza?",
          ch("0.40", "The relative frequency is the count divided by the total: 80 / 200 = 0.40."),
          [ch("0.60", "This is the relative frequency of the students who did not choose pizza: 120 / 200."),
           ch("2.50", "This divides the total by the count. The relative frequency is the count divided by the total."),
           ch("80", "This is the frequency (the count), not the relative frequency.")],
          "Relative frequency = 80 / 200 = 0.40.", difficulty="easy")

    B.mcq(T, "A relative frequency table for the favorite season of a group of students has the entries 0.35, 0.25, and 0.15 for three of the seasons. The remaining season has no entry. What is the relative frequency for the remaining season?",
          ch("0.25", "The relative frequencies add to 1, so the remaining one is 1 - 0.35 - 0.25 - 0.15 = 0.25."),
          [ch("0.75", "This is the sum of the three entries, not the remaining relative frequency."),
           ch("0.15", "This repeats one of the entries. The missing one is 1 minus the sum of the entries."),
           ch("0.35", "This repeats one of the entries. The missing one is 1 minus the sum of the entries.")],
          "The relative frequencies add to 1: 1 - (0.35 + 0.25 + 0.15) = 0.25.", difficulty="easy")

    cats = ["Walk", "Bike", "Bus", "Car", "Other"]
    counts = [24, 18, 66, 36, 6]
    tab = table(["Way of getting to school", "Number of students"], list(zip(cats, counts)), caption="Survey of 150 students", row_headers=True)
    assert sum(counts) == 150
    B.mcq(T, "The table shows how 150 students get to school. What percent of the students chose the category Other?",
          ch("4%", "6 / 150 = 0.04, which is 4%."),
          [ch("6%", "This uses the count 6 as a percent. The percent is the count divided by the total, 150."),
           ch("25%", "This is 6 / 24, which divides by the count for Walk instead of by the total of 150."),
           ch("44%", "This is the percent of the students who chose the bus: 66 / 150. The question asks about the category Other.")],
          "Percent = 6 / 150 = 0.04 = 4%.", diagram=tab, difficulty="medium")

    B.mcq(T, "Among the students in a club who prefer either cats or dogs, the ratio of the number who prefer cats to the number who prefer dogs is 3 to 2. What proportion of these students prefer cats?",
          ch("0.60", "3 of every 5 students prefer cats: 3 / (3 + 2) = 0.60."),
          [ch("0.67", "This is 2 / 3, the ratio of dogs to cats. The proportion divides by the total of 5."),
           ch("1.50", "This is the ratio 3 / 2, which is not a proportion because it is greater than 1."),
           ch("0.40", "This is the proportion of the students who prefer dogs.")],
          "A ratio of 3 to 2 means 3 of every 5: a proportion of 3/5 = 0.60.", difficulty="medium")

    B.mcq(T, "In Group A, 60 of 200 students prefer online homework. In Group B, 32 of 80 students prefer online homework. Which of the following is a correct statement?",
          ch("A larger proportion of the students in Group B prefer online homework, because 32 / 80 = 0.40 is greater than 60 / 200 = 0.30", "Groups of different sizes should be compared using relative frequencies."),
          [ch("A larger proportion of the students in Group A prefer online homework, because the count of 60 students is greater than the count of 32 students", "The counts cannot be compared directly because the groups have different sizes."),
           ch("The two groups have the same proportion of students who prefer online homework, because both groups have more than 30 of them", "The proportions are different: 0.30 and 0.40."),
           ch("A larger proportion of the students in Group A prefer online homework, because Group A has more students in it", "The size of a group does not decide the proportion.")],
          "Compare 60/200 = 0.30 with 32/80 = 0.40: Group B has the greater proportion.", difficulty="medium")

    cats = ["Walk", "Bike", "Bus", "Car"]
    counts = [24, 18, 66, 42]
    tab = table(["Way of getting to school", "Number of students"], list(zip(cats, counts)), caption="Survey of 150 students", row_headers=True)
    assert sum(counts) == 150
    B.mcq(T, "The table shows how 150 students get to school. Which of the following claims is supported by the table?",
          ch("More students in the survey took the bus than took any of the other ways of getting to school, because the bus has the largest count", "66 is greater than each of the other counts."),
          [ch("More than half of the students in the survey took the bus to school, because the bus has the largest count", "Half of 150 is 75, and 66 is less than 75."),
           ch("More students in the survey walked to school than rode in a car, because the walking category comes first in the table", "42 students rode in a car and 24 walked, so more students rode in a car."),
           ch("The same number of students walk to school as ride in a car, because both categories have more than 20 students", "24 students walk and 42 students ride in a car.")],
          "Counts and relative frequencies can justify claims in context: 66 is the greatest count, but it is only 44% of the students.", diagram=tab, difficulty="medium")

    B.mcq(T, "A relative frequency of 0.28 for a category is equivalent to which of the following?",
          ch("28 out of every 100 observations are in the category", "Proportions, percentages and relative frequencies give the same information: 0.28 = 28%."),
          [ch("0.28 observations are in the category", "Observations are counted in whole numbers. The relative frequency is a proportion."),
           ch("28 observations are in the category", "That would be a frequency. The relative frequency is a proportion of the total."),
           ch("2.8 out of every 100 observations are in the category", "0.28 is 28%, not 2.8%.")],
          "A relative frequency of 0.28 is a proportion of 28%.", difficulty="easy")

    B.mcq(T, "A frequency table for the favorite color of 80 children shows 20 for blue. A relative frequency table for the favorite color of 50 adults shows 0.30 for blue. Which of the following is a correct statement?",
          ch("A greater proportion of the adults than of the children chose blue, because 0.30 is greater than 20 / 80 = 0.25", "Both are proportions after the count 20 is divided by 80."),
          [ch("A greater proportion of the children than of the adults chose blue, because the children are more than the adults", "The group sizes do not decide the proportions."),
           ch("The same proportion of the children and of the adults chose blue, because both groups gave a number near 20", "0.30 is a proportion, and 20 is a count of the children."),
           ch("A greater proportion of the children than of the adults chose blue, because a count of 20 is greater than 0.30", "A count cannot be compared with a proportion.")],
          "20 / 80 = 0.25 for the children, which is less than the 0.30 for the adults.", difficulty="medium")

    # ------------------------------------------------------------------------------------------------------------ 1.4
    T = 4
    cats = ["Pizza", "Tacos", "Salad", "Pasta", "Sushi"]
    counts = [32, 26, 12, 20, 10]
    d = bars(cats, counts, "Favorite lunch", "Number of students", alt="Bar chart of the favorite lunch of 100 students.")
    assert sum(counts) == 100
    B.mcq(T, "The bar chart shows the favorite lunch of 100 students. How many more students chose pizza than chose salad?",
          ch("20", "Pizza has a count of 32 and salad has a count of 12, so the difference is 20."),
          [ch("12", "This is the number of students who chose salad."),
           ch("32", "This is the number of students who chose pizza."),
           ch("44", "This adds the counts of the two categories instead of finding their difference.")],
          "32 - 12 = 20 students.", diagram=d, difficulty="easy")

    B.mcq(T, "A pie chart displays the favorite pet of the students in a class. One slice has a central angle of 90 degrees. What relative frequency does this slice represent?",
          ch("0.25", "The whole circle is 360 degrees, and 90 / 360 = 0.25."),
          [ch("0.90", "The angle is not the percentage. The slice is 90 out of 360 degrees."),
           ch("0.50", "A half would be 180 degrees."),
           ch("4.00", "This divides 360 by 90. The relative frequency is 90 / 360, which is less than 1.")],
          "The area of a slice, as a fraction of the whole, is the relative frequency: 90/360 = 0.25.", difficulty="easy")

    B.mcq(T, "A pie chart shows four categories of a categorical variable. Three of the slices represent 15%, 25% and 30% of the observations. What percent of the observations does the fourth slice represent?",
          ch("30%", "The slices of a pie chart add to 100%: 100 - (15 + 25 + 30) = 30."),
          [ch("70%", "This is the sum of the three slices."),
           ch("20%", "The sum of all four slices must be 100%, so the fourth slice is 100 minus the other three."),
           ch("40%", "The three slices add to 70%, so the remaining slice is 30%.")],
          "The areas of the slices add to 100%.", difficulty="easy")

    B.mcq(T, "Which of the following graphs is appropriate for displaying the distribution of a categorical variable such as the favorite sport of the students in a school?",
          ch("A bar chart, with a bar for each sport and the height of the bar showing the count or the relative frequency", "Bar charts display the frequencies or relative frequencies of the categories of one categorical variable."),
          [ch("A histogram, with the intervals of the sports along the horizontal axis and the height of each bar showing the count", "A histogram groups the values of a quantitative variable into intervals."),
           ch("A boxplot, with a box that shows the median and the quartiles of the sports on the horizontal axis of the display", "A boxplot summarizes a quantitative variable, using a five-number summary."),
           ch("A scatterplot, with each student as a point and the sports placed along the vertical axis of the graph of the study", "A scatterplot shows two quantitative variables.")],
          "A bar chart (or a pie chart) displays a categorical variable.", difficulty="easy")

    cats = ["Pizza", "Tacos", "Salad", "Pasta"]
    r1 = [0.40, 0.30, 0.10, 0.20]
    r2 = [0.25, 0.35, 0.25, 0.15]
    d = bars(cats, r1, "Favorite lunch", "Relative frequency", y_max=0.5, series_label="Grade 6", extra=(r2, "Grade 8"), alt="Bar charts of the relative frequency of favorite lunch for Grade 6 and Grade 8 students.")
    B.mcq(T, "The bar chart shows the relative frequencies of the favorite lunch for the students in Grade 6 and for the students in Grade 8. Which of the following is a correct comparison?",
          ch("A greater proportion of the Grade 6 students than of the Grade 8 students chose pizza", "The Grade 6 relative frequency for pizza is 0.40, which is greater than 0.25."),
          [ch("A greater proportion of the Grade 8 students than of the Grade 6 students chose pizza", "The Grade 8 bar for pizza is shorter than the Grade 6 bar."),
           ch("The same proportion of the Grade 6 students and of the Grade 8 students chose tacos", "The bars for tacos are not the same height (0.30 and 0.35)."),
           ch("A greater proportion of the Grade 6 students than of the Grade 8 students chose salad, because the Grade 6 bar is taller", "The Grade 8 bar for salad is taller (0.25 compared with 0.10), so a greater proportion of Grade 8 students chose it.")],
          "Relative frequency bar charts can be used to compare two groups on the same categorical variable.", diagram=d, difficulty="medium")

    cats = ["Soccer", "Basketball", "Baseball", "Tennis"]
    counts = [40, 55, 30, 15]
    d = bars(cats, counts, "Favorite sport", "Number of students", alt="Bar chart of the favorite sport of 140 students.")
    B.mcq(T, "The bar chart shows the favorite sport of 140 students. Which of the following claims is supported by the bar chart?",
          ch("Basketball was the favorite sport of more of the students than any of the other sports, because it has the tallest bar", "The bar for basketball (55) is the tallest."),
          [ch("Basketball was the favorite sport of more than half of the students, because it has the tallest bar", "Half of 140 is 70, and 55 is less than 70."),
           ch("Baseball was the favorite sport of three times as many students as tennis, because the bar for baseball is the taller one", "Baseball has 30 and tennis has 15, so baseball has twice as many, not three times as many."),
           ch("Soccer and basketball together were the favorite sports of fewer than half of the students in the study", "40 + 55 = 95, which is more than half of 140.")],
          "A bar chart can justify claims about a categorical variable in context.", diagram=d, difficulty="medium")

    B.mcq(T, "Which of the following is a difference between a bar chart and a histogram?",
          ch("A bar chart displays the categories of a categorical variable, which can be put in any order, and a histogram displays intervals of a quantitative variable in their natural order", "Bars of a histogram stay in the natural order of the numbers. The categories on a bar chart can be rearranged."),
          [ch("A bar chart displays a quantitative variable in intervals, and a histogram displays a categorical variable with one bar for each category", "These are reversed."),
           ch("A bar chart shows only counts, and a histogram shows only relative frequencies, because the histogram bars cannot show counts", "Both can show either frequencies or relative frequencies."),
           ch("A bar chart has bars that touch each other, and a histogram has bars that do not touch because the data are numbers", "On a histogram the bars touch. On a bar chart there are usually gaps between the bars.")],
          "Bar charts show categories (in any order). Histograms show intervals of a quantitative variable in order.", difficulty="medium")

    B.mcq(T, "In a bar chart of the number of students in each of three clubs, the bar for the Chess club is exactly twice as tall as the bar for the Art club. Which of the following must be true?",
          ch("The Chess club has twice as many students as the Art club, because bar height shows the number of students", "The height of each bar corresponds to the frequency, so a bar that is twice as tall has twice the count."),
          [ch("The Chess club has 2 more students than the Art club, because the bar is taller by one unit of the vertical axis", "A bar twice as tall means twice the count, not 2 more."),
           ch("The Art club has twice as many students as the Chess club, because the shorter bar always shows the larger club", "The taller bar is the larger count."),
           ch("The Chess club has half of the students of the three clubs, because its bar is the tallest bar of the chart", "Twice as tall as the Art club does not mean one half of the total.")],
          "The height of each bar corresponds to the frequency (or relative frequency).", difficulty="medium")
