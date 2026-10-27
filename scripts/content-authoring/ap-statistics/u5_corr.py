"""Unit 5, topic 5.2 Correlation (12 questions).

Required content (CED effective Fall 2026): 5.2.A interpret the correlation for a linear relationship. The correlation coefficient r summarizes the strength and direction of the
LINEAR association between two QUANTITATIVE variables; r is unit-free and always between -1 and 1, inclusive; a negative r means a negative association, a positive r a positive one;
strength is how close r is to -1 or 1; r = 0 means no linear association; r = -1 or 1 means a perfect linear association; an r close to -1 or 1 does not mean a linear model is
appropriate; correlation does not imply causation. Skill 4.D. (r is found by technology; the formula is not on the formula sheet and is not asked for.)
"""
from lib import *


def build(B):
    T = 2

    # 1. An impossible value
    B.mcq(T, "A student calculated the correlation coefficient for four different data sets. Which of the following values must contain an error?",
          ch("r = 1.3", "A correlation coefficient is always between -1 and 1, inclusive, so 1.3 is not possible."),
          [ch("r = -1", "r = -1 is possible. It means a perfect negative linear association."),
           ch("r = 0", "r = 0 is possible. It means that there is no linear association."),
           ch("r = 0.62", "r = 0.62 is possible. It means a moderate positive linear association.")],
          "r must be between -1 and 1, inclusive.", difficulty="easy")

    # 2. Interpret r = -0.82
    B.mcq(T, "A researcher studied the relationship between the number of hours that adults spent watching television per day and their scores on a fitness test. The correlation coefficient was r = -0.82. Which of the following is the best interpretation of the correlation coefficient?",
          ch("There is a strong, negative linear association between the hours of television and the fitness score", "The value is negative, so the association is negative. It is close to -1, so the linear association is strong."),
          [ch("There is a strong, positive linear association between the hours of television and the fitness score", "The correlation coefficient is negative, so the direction is negative."),
           ch("There is a weak, negative linear association between the hours of television and the fitness score", "A value close to -1 indicates a strong association, not a weak one. A weak association is close to 0."),
           ch("There is a strong, negative association, and 82 percent of the fitness scores are lower for adults who watch more television", "r is not a percent of the observations, and it does not say that 82 percent of the scores follow the pattern.")],
          "r = -0.82 is negative (the fitness score tends to decrease as television time increases) and close to -1 (strong).", difficulty="easy")

    # 3. Compare strength
    B.mcq(T, "Relationship 1 has a correlation coefficient of r = -0.91. Relationship 2 has a correlation coefficient of r = 0.78. Which of the following statements is correct?",
          ch("Relationship 1 has the stronger linear association, because -0.91 is closer to -1 than 0.78 is to 1", "Strength depends on how close r is to -1 or 1, not on its sign. |-0.91| is greater than |0.78|."),
          [ch("Relationship 2 has the stronger linear association, because positive correlations are always stronger than negative correlations", "The sign gives the direction, not the strength."),
           ch("Relationship 2 has the stronger linear association, because 0.78 is a greater number than -0.91", "A greater value of r does not mean a stronger association. Strength is how close r is to -1 or 1."),
           ch("The two relationships have equally strong linear associations, because the signs of the two correlation coefficients are different", "Opposite signs mean opposite directions. The strengths are determined by how close each value is to -1 or 1, and they differ.")],
          "The relationship with the correlation coefficient that is farther from 0 (closer to -1 or 1) is stronger.", difficulty="medium")

    # 4. Units
    B.mcq(T, "A data set contains the heights, in inches, and the weights, in pounds, of 40 students. The correlation coefficient is r = 0.62. Each height is converted to centimeters and each weight is converted to kilograms. What is the correlation coefficient for the converted data?",
          ch("The correlation coefficient is still 0.62, because r has no units and does not change when the units of measurement are changed", "r is unit-free. Converting to different units does not change it."),
          [ch("The correlation coefficient is 0.62 multiplied by 2.54, because each height in centimeters is 2.54 times the height in inches", "r has no units, so it is not multiplied by a conversion factor."),
           ch("The correlation coefficient is less than 0.62, because weights in kilograms are smaller numbers than weights in pounds", "The size of the numbers does not change r."),
           ch("The correlation coefficient cannot be determined without calculating it again from the converted heights and the converted weights of all 40 students", "It does not need to be recalculated. r is not affected by a change of units.")],
          "The correlation coefficient is unit-free, so it does not change when the units are changed.", difficulty="medium")

    # 5. Estimate r from a scatterplot
    xs = list(range(1, 21))
    ys = [int(v) for v in noisy_line(xs, 78, -1.9, 28, seed=10, places=0)]
    m = lsrl(xs, ys)
    assert -0.66 < m.r < -0.56 and 0 <= min(ys) and max(ys) <= 100, m.r
    B.mcq(T, "The scatterplot shows the number of absences and the percent of homework completed for 20 students. Which of the following is the best estimate of the correlation coefficient?",
          ch("r = -0.6, because the association is negative and the points follow the pattern moderately closely", "The points decrease from left to right (negative) with a fair amount of scatter, so r is moderately far from 0."),
          [ch("r = 0.6, because the association is positive and the points follow the pattern moderately closely from left to right", "The points decrease from left to right, so r must be negative."),
           ch("r = -0.1, because the association is negative and the points follow the pattern only very loosely", "The points follow a clear downward pattern, so the association is stronger than r = -0.1."),
           ch("r = -0.95, because the association is negative and the points follow the pattern very closely", "There is too much scatter around the pattern for r to be this close to -1.")],
          f"The pattern slopes downward with moderate scatter. The correlation coefficient of these points is about {m.r:.2f}.",
          diagram=scatter(list(zip(xs, ys)), "Number of absences", "Homework completed (%)", x_axis=(0, 22, 2), y_axis=(0, 100, 20), alt="Scatterplot of percent of homework completed against absences for 20 students: a moderate negative pattern."), difficulty="medium")

    # 6. r near 1 but curved
    xs = list(range(1, 13))
    ys = [round(3 * 1.28 ** x + random.Random(70 + x).uniform(-1.5, 1.5), 1) for x in xs]
    m = lsrl(xs, ys)
    assert m.r > 0.93, m.r
    B.mcq(T, f"The scatterplot shows the number of students in a school who have a tablet computer for each of 12 years. The correlation coefficient is r = {m.r:.2f}. A student says, \"Because r is close to 1, the relationship is linear, and a linear model is appropriate for these data.\" Which of the following is the best response to the student?",
          ch("The student is incorrect, because the scatterplot shows a curved pattern and an r close to 1 does not mean that a linear model is appropriate", "The scatterplot shows a pattern that curves upward. An r close to 1 or -1 does not guarantee that the form is linear."),
          [ch("The student is correct, because a correlation coefficient that is close to 1 shows that the form of the association is linear", "r measures the strength of a linear association. A high r does not show that the form is linear. The scatterplot must be examined."),
           ch("The student is incorrect, because the correlation coefficient cannot be as large as this when the pattern of the points is curved", "A curved pattern can still have a correlation coefficient close to 1."),
           ch("The student is correct, because the correlation coefficient describes the strength of any association, whether it is linear or curved", "r describes the strength of a linear association only.")],
          "A value of r close to 1 or -1 does not mean that a linear model is appropriate. The curved pattern in the scatterplot shows it is not.",
          diagram=scatter(list(zip(xs, ys)), "Year", "Students with a tablet", alt="Scatterplot of the number of students with a tablet against year: a curve that rises faster and faster."), difficulty="hard")

    # 7. Correlation and causation
    B.mcq(T, "A study of 40 cities found a strong positive correlation, r = 0.85, between the number of ice cream shops in a city and the number of drowning incidents in the city each year. Which of the following is the most appropriate conclusion?",
          ch("There is a strong positive linear association, but this does not show that ice cream shops cause drownings, because warm weather could be related to both", "Correlation does not imply causation. A related factor could explain the association."),
          [ch("Ice cream shops cause drownings, so a city could reduce the number of drowning incidents by closing some of its ice cream shops", "A strong correlation does not show that one variable causes changes in the other."),
           ch("About 85 percent of the drowning incidents in a city are caused by the ice cream shops that are located within the boundaries of that city", "r is not the percent of incidents, and it does not give a cause."),
           ch("There is no association between the variables, because there is no reasonable way that an ice cream shop could ever cause a drowning in a city", "The data do show a strong association. Whether one variable causes the other is a separate question.")],
          "A correlation shows association, not causation.", difficulty="medium")

    # 8. r = 1
    B.mcq(T, "A set of points has a correlation coefficient of r = 1. Which of the following must be true?",
          ch("All of the points lie on a single straight line that slopes upward", "r = 1 is a perfect positive linear association. All points lie on a line with a positive slope."),
          [ch("All of the points lie on a single straight line that has a slope of exactly 1", "A perfect association can have any positive slope. The slope is not r."),
           ch("A change in the first variable is the cause of the change in the second", "Correlation does not imply causation, even for r = 1."),
           ch("There is no pattern in the points, because a value of 1 means that the data are as random as possible", "r = 1 is the strongest possible linear pattern.")],
          "r = 1 means a perfect positive linear association: the points lie exactly on an upward-sloping line (of any slope).", difficulty="easy")

    # 9. Interpreting r = 0.60
    B.mcq(T, "A scatterplot of the number of hours that students spend on homework and their grade point averages has a correlation coefficient of r = 0.60. Which of the following is an appropriate interpretation?",
          ch("The linear association is positive and moderate, so students who spend more hours on homework tend to have higher grade point averages", "r = 0.60 is positive and moderate: the response tends to increase as the explanatory variable increases."),
          [ch("Exactly 60 percent of the students in the data set are on the line that best fits the points in the scatterplot", "r is not the percent of points on a line."),
           ch("For each additional hour spent on homework, the grade point average increases by 0.60 points", "That would be an interpretation of a slope. r is not a slope."),
           ch("Sixty percent of the variation in the grade point averages is explained by the number of hours spent on homework", "That describes r squared, not r. About 36 percent would be explained here.")],
          "r = 0.60 describes the direction (positive) and strength (moderate) of the linear association. It is not a percent of the points, a slope, or the percent of variation explained.", difficulty="hard")

    # 10. r near 0, a curved pattern
    xs = [round(-5 + 0.5 * i, 1) for i in range(21)]
    ys = [round(25 - xx * xx + random.Random(80 + i).uniform(-2.5, 2.5), 1) for i, xx in enumerate(xs)]
    m = lsrl(xs, ys)
    assert abs(m.r) < 0.12, m.r
    rtxt = f"{abs(m.r):.2f}" if abs(m.r) < 0.005 else f"{m.r:.2f}"  # never print "-0.00"
    B.mcq(T, f"The scatterplot shows the relationship between two variables. The correlation coefficient is r = {rtxt}. Which of the following conclusions is best supported by the scatterplot and the correlation coefficient?",
          ch("There is almost no linear association, but there is a strong non-linear association, because the points follow a curve", "r measures only linear association. A value near 0 means almost no linear association. The points follow a clear curve."),
          [ch("There is no association of any kind between the variables, because the correlation coefficient is so close to 0", "r near 0 means no linear association. A strong curved association can still exist."),
           ch("There is a weak positive linear association, because the correlation coefficient is slightly greater than 0", "A value this close to 0 means essentially no linear association, and the pattern is strongly curved."),
           ch("There is a strong linear association, because the points are closely grouped around a single curve that is clearly visible", "The pattern is curved, not linear, and r is near 0, so the linear association is essentially zero.")],
          "r near 0 means no linear association, but this scatterplot shows a strong curved pattern.",
          diagram=scatter(list(zip(xs, ys)), "x", "y", alt="Scatterplot of y against x: a symmetric arch shape that rises and then falls."), difficulty="medium")

    # 11. Weakest linear association
    B.mcq(T, "Four different pairs of variables have the correlation coefficients shown. Which pair has the weakest linear association?",
          ch("The pair with r = -0.15", "|-0.15| is the closest to 0 of the four values, so this is the weakest linear association."),
          [ch("The pair with r = -0.82", "-0.82 is close to -1, so this is a strong association."),
           ch("The pair with r = 0.48", "0.48 is farther from 0 than -0.15 is, so it is a stronger association."),
           ch("The pair with r = 0.31", "0.31 is farther from 0 than -0.15 is, so it is a stronger association.")],
          "The weakest linear association is the one with a correlation coefficient closest to 0.", difficulty="easy")

    # 12. Which pair of variables can have an r
    B.mcq(T, "A researcher wants to calculate a correlation coefficient. For which of the following pairs of variables is it appropriate to calculate a correlation coefficient?",
          ch("The height, in inches, and the arm span, in inches, of each student in a class", "A correlation coefficient describes the linear association between two quantitative variables, and both of these are quantitative."),
          [ch("The eye color and the hair color of each student in a class", "Both variables are categorical. A correlation coefficient needs two quantitative variables."),
           ch("The postal code and the sale price of each house that was sold in a city last year", "A postal code is a label, so it is a categorical variable even though it is written with numbers."),
           ch("The favorite sport of each student and the number of siblings of the student", "Favorite sport is a categorical variable. A correlation coefficient needs two quantitative variables.")],
          "Correlation applies to two quantitative variables.", difficulty="easy")
