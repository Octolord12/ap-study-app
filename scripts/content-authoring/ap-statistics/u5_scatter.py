"""Unit 5, topic 5.1 Graphical Representations Between Two Quantitative Variables (12 questions).

Required content (CED effective Fall 2026): 5.1.A construct scatterplots; the explanatory variable is on the x-axis (the variable used to explain or predict) and the
response variable on the y-axis; 5.1.B describe an association by form (linear or non-linear), direction (positive or negative), strength (strong, moderate, weak: how
closely the points follow the general pattern) and unusual features (clusters, points that do not fit the general pattern); 5.1.C scatterplots can justify claims about
the variables in context. Skills 3.A, 4.A, 4.B.
"""
from lib import *


def build(B):
    T = 1

    # 1. Which variable goes where
    B.mcq(T, "A researcher wants to use the number of hours that students study per week to predict their scores on a statistics exam. The researcher will construct a scatterplot of the data. Which of the following correctly describes how the variables should be placed on the scatterplot?",
          ch("Hours studied per week should be on the horizontal axis, because it is the variable used to predict, and exam score on the vertical axis, because it is the variable being predicted", "The explanatory variable, the one used to explain or predict, goes on the horizontal axis. The response variable goes on the vertical axis."),
          [ch("Exam score should be on the horizontal axis, because it is the variable of main interest, and hours studied on the vertical axis, because it is easier to measure", "The variable of main interest here is the response, which belongs on the vertical axis."),
           ch("Either variable can be on either axis, because a scatterplot shows the association between the variables in the same way whichever axis each variable is on", "By convention the explanatory variable is on the horizontal axis. Reversing the axes changes which variable is being used to predict the other."),
           ch("Exam score should be on the horizontal axis, because the variable that is measured last in a study is always the explanatory variable of the study", "The explanatory variable is the one used to explain or predict, not the one measured first or last.")],
          "The explanatory variable (hours studied) is placed on the x-axis and the response variable (exam score) on the y-axis.", difficulty="easy")

    # 2. Describe a scatterplot: positive, linear, moderately strong, one point that does not fit
    xs = [62, 65, 68, 70, 72, 74, 76, 78, 80, 82, 85, 87, 90, 92]
    ys = [int(v) for v in noisy_line(xs, -20, 1.6, 11, seed=25, places=0)]
    ys[5] = 62  # the unusual day: much lower than the days next to it
    m = lsrl(xs, ys)
    assert 0.7 < m.r < 0.85, m.r
    B.mcq(T, "A café owner recorded the high temperature, in degrees Fahrenheit, and the number of iced coffees sold on each of 14 days. The scatterplot shows the data. Which of the following best describes the association shown in the scatterplot?",
          ch("The association is linear and positive, and it is moderately strong, with one day that does not fit the general pattern of the other days", "Form: the points follow a line. Direction: sales tend to increase as the temperature increases. Strength: the points are fairly close to the pattern. The point well below the others is an unusual feature."),
          [ch("The association is linear and negative, and it is moderately strong, with one day that does not fit the general pattern of the other days", "The points rise from left to right, so the direction is positive, not negative."),
           ch("The association is non-linear and positive, and it is moderately strong, with one day that does not fit the general pattern of the other days", "The points follow a roughly straight pattern, so the form is linear."),
           ch("The association is linear and positive, and it is moderately strong, with no unusual features because every day lies close to the line", "One day, with sales well below the others at a similar temperature, does not fit the general pattern.")],
          "The points rise from left to right along a roughly straight pattern (positive and linear), with a moderate amount of scatter. The one low point is an unusual feature.",
          diagram=scatter(list(zip(xs, ys)), "High temperature (degrees F)", "Iced coffees sold", alt="Scatterplot of iced coffees sold against high temperature for 14 days: a positive linear pattern with one low point."), difficulty="medium")

    # 3. Direction in words
    B.mcq(T, "A scatterplot of the age of a used car, in years, and its selling price, in thousands of dollars, shows a negative association. Which of the following statements describes what a negative association means in this context?",
          ch("As the age of a car increases, the selling price tends to decrease", "A negative association means that as the values of the explanatory variable increase, the values of the response variable tend to decrease."),
          [ch("As the age of a car increases, the selling price tends to increase", "That describes a positive association."),
           ch("As the age of a car increases, the selling price always decreases, with no exceptions", "A scatterplot shows a tendency. An association does not mean that every car follows the pattern."),
           ch("As the selling price of a car increases, the age of the car tends to increase", "That reverses the variables and describes a positive association. A negative association means the older cars tend to cost less.")],
          "In a negative association the response variable tends to decrease as the explanatory variable increases: older cars tend to sell for less.", difficulty="easy")

    # 4. Curved form: rises then falls
    xs = list(range(0, 13))
    ys = [round(4 + 2.2 * x - 0.17 * x * x + random.Random(4 + x).uniform(-0.5, 0.5), 1) for x in xs]
    m = lsrl(xs, ys)
    B.mcq(T, "After a patient takes a dose of a medicine, the concentration of the medicine in the blood is measured at several times. The scatterplot shows the concentration, in milligrams per liter, against the number of hours since the dose. Which of the following describes the form of the association?",
          ch("The form is non-linear, because the points follow a curve that rises and then falls instead of following a straight line", "The concentration increases for the first hours and then decreases, which a straight line cannot describe."),
          [ch("The form is linear and positive, because the concentration is higher after several hours than it was at the beginning of the study", "The concentration is not higher at every later time. The points rise and then fall, so the pattern is not linear."),
           ch("The form is linear and negative, because the concentration is lower at the end of the study than it was at the highest point", "The points do not follow a straight line that falls from left to right. They rise first."),
           ch("There is no form, because the points do not all lie exactly on a single curve or line and so no pattern can be described", "Points rarely lie exactly on a curve. The overall pattern is clearly curved.")],
          "The points rise to a maximum and then fall, so the form is a curve (non-linear).",
          diagram=scatter(list(zip(xs, ys)), "Hours since the dose", "Concentration (mg/L)", alt="Scatterplot of blood concentration against hours since the dose: the points rise to a peak and then fall."), difficulty="medium")

    # 5. Two clusters
    rnd = random.Random(33)
    c1 = [(round(rnd.uniform(3, 7), 1), round(rnd.uniform(8, 16), 1)) for _ in range(9)]
    c2 = [(round(rnd.uniform(18, 24), 1), round(rnd.uniform(44, 58), 1)) for _ in range(9)]
    B.mcq(T, "A veterinarian recorded the shoulder height, in inches, and the weight, in pounds, of dogs of many breeds that were brought to a clinic in one day. The scatterplot shows the data. Which of the following is an unusual feature of the scatterplot?",
          ch("The points form two separate clusters, one of small dogs and one of large dogs, with no points between them", "Clusters of individual points are an unusual feature. Here the points are in two groups with a large gap between them."),
          [ch("One point does not fit the general pattern, because it is much farther from the line than all of the other points are", "No single point stands apart from the others. Instead the points form two groups."),
           ch("There are no unusual features, because the points show a positive association that is strong and that rises from left to right", "The overall trend is positive, but the gap between two groups of points is an unusual feature to describe."),
           ch("The points follow a curve that rises and then falls, which is an unusual feature that a student should describe as the form", "The points do not rise and then fall. They are in two clusters.")],
          "The data fall into two clusters (small dogs and large dogs). Clusters are an unusual feature of a scatterplot.",
          diagram=scatter(c1 + c2, "Shoulder height (inches)", "Weight (pounds)", alt="Scatterplot of weight against shoulder height: two clusters of points, one at low values and one at high values."), difficulty="medium")

    # 6. Claim supported: U shape (curved)
    months = list(range(1, 13))
    temps = [35, 38, 47, 58, 68, 77, 84, 82, 74, 61, 48, 39]
    use = [round(600 + 0.55 * (t - 60) ** 2 + random.Random(m_).uniform(-40, 40)) for t, m_ in zip(temps, months)]
    assert min(use) < 700 and max(use) > 880 and use[0] > use[4] + 200 and use[6] > use[4] + 200, use  # a clear U
    B.mcq(T, "A utility company recorded the average outdoor temperature, in degrees Fahrenheit, and the average household electricity use, in kilowatt-hours per month, for each of 12 months. The scatterplot shows the data. Which of the following claims is supported by the scatterplot?",
          ch("Electricity use tends to be higher in months with very low or very high temperatures than in months with mild temperatures", "The points form a U shape: use is highest at the lowest and highest temperatures and lowest for mild temperatures."),
          [ch("Electricity use tends to increase as the average outdoor temperature increases, for all of the months in the data set", "Use is high in the coldest months too, so it does not increase for all of the temperatures."),
           ch("Electricity use tends to decrease as the average outdoor temperature increases, for all of the months in the data set", "Use increases again in the hottest months, so it does not decrease for all temperatures."),
           ch("There is no association between temperature and electricity use, because the points do not follow a straight line", "A pattern does not have to be linear to be an association. The points follow a clear curve.")],
          "A scatterplot can justify claims about the variables. The U-shaped pattern supports the claim that use is higher at the temperature extremes.",
          diagram=scatter(list(zip(temps, use)), "Average temperature (degrees F)", "Electricity use (kWh)", alt="Scatterplot of electricity use against temperature for 12 months: a U-shaped pattern."), difficulty="medium")

    # 7. What describing a scatterplot includes
    B.mcq(T, "Which of the following is NOT one of the characteristics that are used to describe the association shown in a scatterplot?",
          ch("The median of the values of the response variable", "A description of a scatterplot includes form, direction, strength, and unusual features. The median of one variable is not one of them."),
          [ch("The direction of the association between the variables", "Direction (positive or negative) is one of the characteristics used to describe a scatterplot."),
           ch("The strength of the association between the variables", "Strength (strong, moderate, or weak) is one of the characteristics used to describe a scatterplot."),
           ch("Unusual features such as clusters or points that do not fit", "Unusual features are one of the characteristics used to describe a scatterplot.")],
          "A scatterplot is described by form, direction, strength, and unusual features.", difficulty="easy")

    # 8. Table of pairs: absences and grade
    absences = [0, 1, 2, 3, 4, 6, 8, 10]
    grades = [96, 93, 91, 86, 84, 77, 70, 61]
    m = lsrl(absences, grades)
    assert m.r < -0.97
    B.mcq(T, "A teacher recorded the number of absences and the final grade, in points, for 8 students in a class. The data are shown in the table. Which of the following best describes the association between the number of absences and the final grade?",
          ch("The association is negative and linear: students with more absences tend to have lower final grades", "As the number of absences increases, the final grades decrease, and the pairs fall close to a line."),
          [ch("The association is positive and linear: students with more absences tend to have higher final grades", "The final grades decrease as the absences increase, so the direction is negative."),
           ch("The association is negative and non-linear: the final grades fall slowly for students with a few absences and then very quickly", "The grades decrease by roughly the same amount for each extra absence, so the pairs follow a line."),
           ch("There is no association, because students with 0 absences and students with 10 absences both took the same final exam", "Taking the same exam does not mean there is no association. The pairs show a clear pattern.")],
          "The grades go down as the number of absences goes up, in a roughly straight pattern: a negative linear association.",
          diagram=table(["Absences", "Final grade (points)"], list(zip(absences, grades)), caption="Absences and final grade for 8 students"), difficulty="medium")

    # 9. Strength is not steepness
    B.mcq(T, "A student looks at a scatterplot in which the points rise steeply from left to right and are widely spread out around the general pattern. The student says that the association is strong because the pattern is steep. Which of the following is the best response to the student?",
          ch("Strength depends on how closely the points follow the general pattern, so a steep pattern with widely spread points is not a strong association", "The strength of an association is how closely the points follow the pattern. Steepness is not strength."),
          [ch("The student is correct, because the steeper the general pattern is, the stronger the association between the two variables is", "Steepness describes the slope of the pattern, not how closely the points follow it."),
           ch("The student is correct, but only when the form of the association is linear and the direction of the association is positive", "Even for a positive linear form, strength depends on how closely the points follow the pattern."),
           ch("Strength depends only on the number of points that are plotted, so a scatterplot with many points always shows a strong association", "The number of points does not determine the strength of an association.")],
          "Strong means the points follow the pattern closely. A steep pattern with a lot of scatter is a weak or moderate association.", difficulty="hard")

    # 10. A point that does not fit
    xs = list(range(1, 15))
    ys = noisy_line(xs, 92, -4.1, 3.0, seed=9, places=0)
    ys = [int(v) for v in ys]
    ys[10] = 96  # the unusual point
    m = lsrl(xs, ys)
    B.mcq(T, "A scatterplot shows the age of a machine, in years, and the number of defective parts it made in one week. One point is labeled P. Which of the following statements about point P is correct?",
          ch("Point P is an unusual feature, because it does not fit the general negative linear pattern that the other points show", "Points that do not fit the general pattern are an unusual feature. P is far above where the other points suggest it should be."),
          [ch("Point P shows that the form of the association is non-linear, because a single point is far from the rest of the points", "One point away from the pattern does not make the form of the association curved. The other points follow a line."),
           ch("Point P shows that the direction of the association is positive, because it is higher than the points that are next to it", "The direction is determined by the overall pattern of all the points, which is negative."),
           ch("Point P is not an unusual feature, because every point in a scatterplot is part of the pattern of the association", "A point can be far from the general pattern. That is an unusual feature to be described.")],
          "Point P lies well away from the negative linear pattern formed by the other points, so it is an unusual feature.",
          diagram=scatter(list(zip(xs, ys)), "Age of the machine (years)", "Defective parts in a week", highlights=[(10, "P")], alt="Scatterplot of defective parts against machine age: a negative linear pattern with one point labeled P far above it."), difficulty="medium")

    # 11. Ordered pair for a student
    B.mcq(T, "A teacher wants to use the number of hours of sleep that students got last night to predict the number of questions that they answer correctly on a 25-question quiz. Student 3 slept 7 hours and answered 18 questions correctly. Which of the following is the ordered pair that represents Student 3 on a scatterplot?",
          ch("(7, 18), with the 7 on the horizontal axis, because hours of sleep is the explanatory variable", "The explanatory variable (hours of sleep) is the first coordinate, plotted on the horizontal axis. The response (questions correct) is the second."),
          [ch("(18, 7), with the 18 on the horizontal axis, because the number of questions is the larger of the two numbers", "The axis a variable goes on does not depend on the size of its values. The explanatory variable is on the horizontal axis."),
           ch("(7, 25), with the 7 on the horizontal axis, because the total number of questions on the quiz is the second coordinate", "The second coordinate is the number of questions this student answered correctly, which is 18."),
           ch("(18, 7), with the 18 on the horizontal axis, because the response variable is always on the horizontal axis of a scatterplot", "The response variable is on the vertical axis.")],
          "Each point is (explanatory value, response value) = (7, 18).", difficulty="easy")

    # 12. Curved, decreasing and levelling off
    xs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    ys = [round(2 + 38 * math.exp(-0.38 * x) + random.Random(60 + x).uniform(-1.2, 1.2), 1) for x in xs]
    B.mcq(T, "A scientist measured the amount of a chemical that remained in a sample, in grams, each day for 12 days. The scatterplot shows the amount remaining against the number of days. Which of the following best describes the form and the direction of the association?",
          ch("The association is non-linear and negative: the amount remaining decreases quickly at first and then levels off", "The points fall from left to right (negative) along a curve that flattens out, so the form is non-linear."),
          [ch("The association is linear and negative: the amount remaining decreases by about the same amount during each of the days", "The decreases get smaller over time, so a line does not describe the pattern."),
           ch("The association is non-linear and positive: the amount remaining increases quickly at first and then levels off over time", "The amount remaining decreases, so the direction is negative."),
           ch("The association is linear and positive: the amount remaining increases by about the same amount during each of the days", "The points fall from left to right, and they do not follow a line.")],
          "The points decrease from left to right (negative) along a curve that levels off (non-linear).",
          diagram=scatter(list(zip(xs, ys)), "Days", "Amount remaining (g)", alt="Scatterplot of the amount remaining against days: a curve that falls quickly and then levels off."), difficulty="hard")
