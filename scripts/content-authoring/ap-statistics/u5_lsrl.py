"""Unit 5, topic 5.5 Least-Squares Regression (12 questions).

Required content (CED effective Fall 2026): 5.5.A the simple linear regression model is fit by minimizing the SUM OF THE SQUARES OF THE RESIDUALS (the least-squares regression line, LSRL),
found with technology; the line passes through (x-bar, y-bar); slope b, y-intercept a and r come from technology; r squared (the coefficient of determination) is the proportion of
variation in the response explained by the linear relationship with the explanatory variable. 5.5.B interpret the coefficients: the slope is the PREDICTED increase or decrease in the
response for a one-unit increase in the explanatory variable, in context; the y-intercept is the PREDICTED response when the explanatory variable is 0, in context, and sometimes has no
reasonable interpretation (x = 0 is outside the data, or a negative value for a response that cannot be negative). Skills 3.B, 4.D. (The slope formula is not on the formula sheet.)
"""
from lib import *


def build(B):
    T = 5

    # 1. What least squares minimizes
    B.mcq(T, "The least-squares regression line for a set of data is the line that minimizes which of the following?",
          ch("The sum of the squares of the residuals", "The least-squares line is the line for which the sum of the squared residuals is as small as possible."),
          [ch("The sum of the residuals of the points", "The residuals of the least-squares line add to 0, so this is not what is minimized."),
           ch("The number of points that are not on the line", "The line is not chosen to pass through as many points as possible."),
           ch("The size of the largest residual of any of the points", "The line minimizes the sum of the squared residuals, not the single largest residual.")],
          "The least-squares regression line minimizes the sum of the squares of the residuals.", difficulty="easy")

    # 2. Interpret the slope
    B.mcq(T, "The equation of the least-squares regression line for predicting a violinist's performance rating, in points, from the number of hours that the violinist practices per week is $\\hat{y} = 12.4 + 2.1x$. Which of the following is the correct interpretation of the slope?",
          ch("For each additional hour of practice per week, the predicted performance rating increases by 2.1 points", "The slope is the predicted change in the response for a one-unit increase in the explanatory variable."),
          [ch("For each additional hour of practice per week, the predicted performance rating decreases by 2.1 points", "The slope is positive, so the predicted rating increases."),
           ch("For each additional point of performance rating, the predicted number of hours of practice per week increases by 2.1", "This reverses the roles of the variables. The model predicts the rating from the hours."),
           ch("A violinist who does not practice is predicted to have a performance rating of 2.1 points on the rating scale", "That would be the y-intercept, which is 12.4. The slope is the change for each additional hour.")],
          "The slope 2.1 is the predicted increase in the performance rating for each additional hour of practice per week.", difficulty="easy")

    # 3. Interpret an intercept that makes sense
    B.mcq(T, "The equation of the least-squares regression line for predicting the resting heart rate, in beats per minute, of adults from the number of minutes that they exercise per day is $\\hat{y} = 71.6 - 0.18x$. The data include adults who exercise from 0 to 60 minutes per day. Which of the following is the correct interpretation of the y-intercept?",
          ch("The predicted resting heart rate of an adult who does not exercise is 71.6 beats per minute", "The y-intercept is the predicted response when the explanatory variable is 0. Here 0 minutes of exercise is in the data, so the interpretation makes sense."),
          [ch("For each additional minute of exercise per day, the predicted resting heart rate decreases by 71.6 beats per minute", "That describes a slope. The slope is -0.18."),
           ch("The mean resting heart rate of all of the adults in the data set is 71.6 beats per minute", "The intercept is a prediction for x = 0. It is not the mean of the response for all adults."),
           ch("An adult with a resting heart rate of 0 beats per minute is predicted to exercise for 71.6 minutes per day", "This reverses the roles of the variables. The y-intercept is a predicted response, not a predicted explanatory value.")],
          "When x = 0, the predicted resting heart rate is 71.6 beats per minute.", difficulty="medium")

    # 4. An intercept that cannot be interpreted
    B.mcq(T, "The equation of the least-squares regression line for predicting the weight, in pounds, of adult women from their height, in inches, is $\\hat{y} = -119.4 + 4.0x$. The heights in the data are between 58 inches and 72 inches. Which of the following best explains why the y-intercept has no reasonable interpretation in this context?",
          ch("A height of 0 inches is far outside the heights in the data, and the predicted weight of -119.4 pounds is not possible", "The intercept is a prediction at x = 0, which is an extrapolation here, and a weight cannot be negative."),
          [ch("The y-intercept of a least-squares regression line never has a reasonable interpretation in any context", "In many contexts, such as when x = 0 is in the data, the y-intercept can be interpreted."),
           ch("The y-intercept has no interpretation because the slope of the regression line is positive and is greater than 1", "The sign and size of the slope do not decide whether the intercept can be interpreted."),
           ch("The y-intercept cannot be interpreted because the data set must be too small for any intercept to be calculated", "The intercept can be calculated from any data set. The problem is that x = 0 is outside the data and the value is negative.")],
          "x = 0 is outside the interval of heights used to find the line (an extrapolation), and the negative weight is not logical.", difficulty="medium")

    # 5. Interpret r squared
    B.mcq(T, "A least-squares regression line is used to predict a student's test score from the number of hours that the student studied. The coefficient of determination is $r^2 = 0.64$. Which of the following is a correct interpretation of $r^2$?",
          ch("About 64% of the variation in test scores is explained by the linear relationship with the number of hours studied", "r squared is the proportion of the variation in the response variable that is explained by the linear relationship with the explanatory variable."),
          [ch("About 64% of the students have test scores that are exactly the same as the scores that the regression line predicts", "r squared is not the percent of the points that are on the line."),
           ch("About 64% of the variation in the number of hours studied is explained by the linear relationship with the test scores", "This reverses the variables. The response is the test score."),
           ch("The correlation between the number of hours studied and the test score is 0.64, so the association is positive and moderate", "r squared is the square of the correlation. Here r would be about 0.80.")],
          "r squared = 0.64 means that about 64% of the variation in the response (test score) is explained by the linear relationship with the explanatory variable (hours studied).", difficulty="medium")

    # 6. The line passes through (x-bar, y-bar)
    xbar, ybar, b = 30, 82, 1.6
    a = ybar - b * xbar
    assert a == 34.0
    B.mcq(T, f"For a set of data, the mean of the explanatory variable is $\\bar{{x}} = {xbar}$ and the mean of the response variable is $\\bar{{y}} = {ybar}$. The slope of the least-squares regression line is {b}. What is the y-intercept of the line?",
          ch(f"{a:.1f}", f"The least-squares line passes through ({xbar}, {ybar}), so {ybar} = a + {b}({xbar}) and a = {ybar} - {b * xbar:.0f} = {a:.0f}.", a),
          [ch(f"{ybar + b * xbar:.1f}", "This adds b times x-bar to y-bar. The intercept is y-bar minus b times x-bar.", ybar + b * xbar),
           ch(f"{ybar - b:.1f}", "This subtracts the slope from y-bar without multiplying the slope by x-bar.", ybar - b),
           ch(f"{xbar - b * ybar:.1f}", "This reverses the roles of x-bar and y-bar.", xbar - b * ybar)],
          f"Because the line passes through (x-bar, y-bar): a = {ybar} - {b}({xbar}) = {a:.0f}.", difficulty="medium")

    # 7. LSRL has the smallest sum of squared residuals
    B.mcq(T, "A student draws a line by eye through a scatterplot. The sum of the squares of the residuals for the student's line is 150. The sum of the squares of the residuals for the least-squares regression line is 120. Which of the following statements is correct?",
          ch("This result is expected, because the least-squares line has the smallest possible sum of squared residuals of all of the lines", "By definition, the least-squares line minimizes the sum of the squared residuals."),
          [ch("This result is not possible, because a line that is drawn by eye through the middle of the points must have a smaller sum", "No line has a smaller sum of squared residuals than the least-squares line."),
           ch("This result shows that the least-squares line does not pass through the point of the means, unlike the line drawn by the student", "The least-squares line always passes through (x-bar, y-bar)."),
           ch("This result shows that the student's line is a better model, because a larger sum of squares means that the line fits better", "A larger sum of squared residuals means a worse fit.")],
          "The least-squares line minimizes the sum of the squared residuals, so no other line can have a smaller sum.", difficulty="medium")

    # 8. Compare r squared
    B.mcq(T, "Two different least-squares regression lines were found for predicting the same response variable. The line that uses the first explanatory variable has $r^2 = 0.81$. The line that uses the second explanatory variable has $r^2 = 0.45$. Which of the following statements is correct?",
          ch("The linear relationship with the first explanatory variable explains a greater proportion of the variation in the response variable", "r squared is the proportion of the variation in the response that is explained. 0.81 is greater than 0.45."),
          [ch("The linear relationship with the second explanatory variable explains a greater proportion of the variation in the response variable", "The smaller r squared explains a smaller proportion of the variation."),
           ch("The regression line for the first explanatory variable has a greater slope than the line for the second explanatory variable", "r squared does not tell the size of the slope."),
           ch("The first explanatory variable causes the response variable to change, but the second explanatory variable does not", "A larger r squared does not show that a variable is a cause.")],
          "The greater r squared means that more of the variation in the response is explained by the linear relationship.", difficulty="easy")

    # 9. Sign of the slope
    B.mcq(T, "For a set of data the correlation coefficient is r = -0.74. Which of the following must be true about the slope of the least-squares regression line?",
          ch("The slope is negative, because the slope of the least-squares line and the correlation coefficient always have the same sign", "A negative correlation means a negative association, so the least-squares line slopes downward."),
          [ch("The slope is equal to -0.74, because the slope of a regression line is the same as the correlation coefficient", "The slope has the same sign as r, but it is not equal to r. Its size depends on the units of the two variables."),
           ch("The slope is positive, because the value of r squared is 0.55, which is a positive number that is less than 1", "r squared is always positive. The sign of the slope is the sign of r."),
           ch("The sign of the slope cannot be determined, because the slope also depends on the units of the two variables", "The size of the slope depends on the units, but its sign does not. It is the same as the sign of r.")],
          "The slope and the correlation coefficient have the same sign.", difficulty="hard")

    # 10-12. Shared scenario: exercise and resting heart rate
    out = table(["Predictor", "Coefficient"], [("Constant", "78.40"), ("Hours of exercise per week", "-2.15")], caption="R-sq = 54.3%", row_headers=True)
    scenario = "Researchers used technology to find the least-squares regression line for predicting the resting heart rate, in beats per minute, of 40 adults from the number of hours per week that they exercise. The adults exercised between 0 and 8 hours per week. Part of the output is shown."
    B.mcq(T, scenario + " Which of the following is a correct interpretation of the slope?",
          ch("For each additional hour of exercise per week, the predicted resting heart rate decreases by about 2.15 beats per minute", "The slope is -2.15, so the predicted resting heart rate decreases by 2.15 beats per minute for each additional hour of exercise per week."),
          [ch("For each additional hour of exercise per week, the predicted resting heart rate increases by about 2.15 beats per minute", "The coefficient is negative, so the predicted heart rate decreases."),
           ch("For each additional beat per minute of resting heart rate, the predicted hours of exercise per week decrease by about 2.15", "This reverses the roles of the variables."),
           ch("For each additional hour of exercise per week, the resting heart rate of every adult decreases by exactly 2.15 beats per minute", "The slope describes the predicted change on average, not an exact change for every adult.")],
          "The slope -2.15 is the predicted change in resting heart rate for one more hour of exercise per week: a decrease of about 2.15 beats per minute.", diagram=out, difficulty="medium")

    B.mcq(T, scenario + " Which of the following statements about the y-intercept of the line is correct?",
          ch("It can be interpreted: the predicted resting heart rate of an adult who does not exercise is about 78.4 beats per minute, because 0 hours is within the data", "The y-intercept is the predicted response when x = 0, and 0 hours is within the interval 0 to 8 hours, so the interpretation is reasonable."),
          [ch("It cannot be interpreted in context, because 0 hours of exercise per week is outside the interval of hours of the 40 adults in the data", "0 hours is in the data (the adults exercised from 0 to 8 hours), so the intercept can be interpreted."),
           ch("It is the predicted decrease in the resting heart rate for each additional hour of exercise that an adult does every week, so it is a rate of change", "That describes the slope, not the y-intercept."),
           ch("It is the mean resting heart rate of the 40 adults who were in the study, which is about 78.4 beats per minute for all of them", "The intercept is a prediction for x = 0. It is not the mean resting heart rate of all of the adults.")],
          "The y-intercept is the predicted response for x = 0. Here x = 0 is in the data, so it is interpretable.", diagram=out, difficulty="medium")

    r2 = 0.543
    r = -math.sqrt(r2)
    assert round(r, 3) == -0.737
    B.mcq(T, scenario + " What is the value of the correlation coefficient?",
          ch(f"r = {r:.3f}", "r squared is 0.543, so |r| = sqrt(0.543) = 0.737. The slope is negative, so r is negative.", r),
          [ch(f"r = {-r:.3f}", "The square root of r squared is 0.737, but the slope is negative, so r must be negative.", -r),
           ch(f"r = {-r2:.3f}", "0.543 is r squared, not r. r is the square root of r squared.", -r2),
           ch(f"r = {-(r2 ** 2):.3f}", "This squares r squared instead of taking its square root.", -(r2 ** 2))],
          "r = -sqrt(0.543) = -0.737. The sign of r matches the sign of the slope.", diagram=out, difficulty="hard")
