"""Unit 5, topic 5.3 Linear Regression Models (12 questions).

Required content (CED effective Fall 2026): 5.3.A calculate a predicted response value using a linear regression model. If the form of the relationship looks linear, a linear
regression model (a linear equation using the explanatory variable x to predict the response y) approximates it; the predicted response is y-hat = a + bx where a is the y-intercept
and b the slope; EXTRAPOLATION is predicting for an x outside the interval of x-values used to find the line, and the prediction is less reliable the further out it is;
INTERPOLATION is predicting for an x inside that interval. Skill 3.B.
"""
from lib import *


def build(B):
    T = 3

    # 1. Plug in
    a, b, x = 3.2, 1.45, 12
    pred = a + b * x
    assert round(pred, 2) == 20.6
    B.mcq(T, f"The equation of a regression line for predicting the height of a plant, in centimeters, from the number of days since it was planted is {yhat_eq(a, b)}. What is the predicted height of a plant 12 days after it was planted?",
          ch(f"{pred:.2f} centimeters", f"Substitute x = 12: {a} + {b}(12) = {pred:.1f}.", pred),
          [ch(f"{b * x:.2f} centimeters", "This leaves out the y-intercept. The predicted value is a + bx.", b * x),
           ch(f"{a * x + b:.2f} centimeters", "This multiplies the y-intercept by 12 instead of the slope. The slope is multiplied by x.", a * x + b),
           ch(f"{a + b:.2f} centimeters", "This adds the intercept and the slope without using x = 12.", a + b)],
          f"Predicted height = {a} + {b}(12) = {pred:.1f} cm.", difficulty="easy")

    # 2. Which prediction is extrapolation
    B.mcq(T, "A forester measured the trunk diameters of trees that were between 10 and 40 years old and found a linear regression model for predicting trunk diameter from age. For which of the following ages would a prediction from the model involve extrapolation?",
          ch("52 years, because 52 is outside the interval of ages from 10 to 40 that was used to find the model", "Extrapolation is predicting for an x-value outside the interval of x-values used to find the model."),
          [ch("25 years, because 25 is near the middle of the interval of ages that was used to find the model", "25 is inside the interval from 10 to 40, so this would be interpolation."),
           ch("18 years, because 18 is not one of the ages of the trees that were measured in the study of the forester", "18 is inside the interval from 10 to 40. A value inside the interval is interpolation even if no tree had exactly that age."),
           ch("33 years, because 33 is close to the oldest of the trees that were measured in the study of the forester", "33 is inside the interval from 10 to 40, so this would be interpolation.")],
          "A prediction for an age outside 10 to 40 years is extrapolation.", difficulty="easy")

    # 3. Least reliable
    B.mcq(T, "A pediatrician used a linear regression model to predict the weight of an infant from its age. The model was found using infants who were between 6 and 12 months old. Which of the following predictions is likely to be the LEAST reliable?",
          ch("The prediction for an infant who is 30 months old, because it is the farthest beyond the interval of ages that was used to find the model", "A prediction is less reliable the further the x-value is beyond the interval used to find the line. 30 is farthest from the interval."),
          [ch("The prediction for an infant who is 14 months old, because it is beyond the interval of ages that was used to find the model", "14 months is extrapolation, but it is only 2 months beyond the interval, so it is more reliable than the prediction for 30 months."),
           ch("The prediction for an infant who is 5 months old, because it is below the interval of ages that was used to find the model", "5 months is extrapolation, but it is only 1 month below the interval. 30 months is much farther away."),
           ch("The prediction for an infant who is 9 months old, because it is in the middle of the interval of ages that was used to find the model", "9 months is inside the interval, so this is interpolation and it is the most reliable.")],
          "The further an x-value is from the interval used to find the model, the less reliable the prediction.", difficulty="medium")

    # 4. Equation from output
    B.mcq(T, "A company used technology to find a regression line for predicting the annual salary of an employee, in thousands of dollars, from the number of years of experience. Part of the output is shown. Which of the following is the equation of the regression line?",
          ch("$\\hat{y} = 18.62 + 2.37x$, where x is years of experience and y-hat is the predicted salary", "The constant is the y-intercept and the coefficient of years of experience is the slope: y-hat = a + bx."),
          [ch("$\\hat{y} = 2.37 + 18.62x$, where x is years of experience and y-hat is the predicted salary", "This reverses the roles of the two coefficients. The constant is the intercept."),
           ch("$\\hat{y} = 18.62 - 2.37x$, where x is years of experience and y-hat is the predicted salary", "Both coefficients are positive in the output, so the slope is +2.37."),
           ch("$\\hat{x} = 18.62 + 2.37y$, where y is the salary and x-hat is the predicted number of years", "The model predicts the salary from the years of experience. The variables are not reversed.")],
          "The Constant is the y-intercept (18.62) and the coefficient of the explanatory variable is the slope (2.37).",
          diagram=table(["Predictor", "Coefficient"], [("Constant", "18.62"), ("Years of experience", "2.37")], caption="Regression of salary (thousands of dollars) on years of experience", row_headers=True), difficulty="medium")

    # 5. Solve for x
    a, b = 52.1, 3.4
    x = (80 - a) / b
    assert round(x, 1) == 8.2
    B.mcq(T, f"The equation of a regression line for predicting a student's test score from the number of hours the student studied is {yhat_eq(a, b, 1)}. According to the model, about how many hours of studying are needed for a predicted score of 80?",
          ch(f"{x:.1f} hours", f"Solve 80 = {a} + {b}x: x = (80 - {a}) / {b} = {x:.1f}.", x),
          [ch(f"{80 / b:.1f} hours", "This divides 80 by the slope without subtracting the intercept first.", 80 / b),
           ch(f"{(80 - a) * b:.1f} hours", "This multiplies by the slope instead of dividing by it.", (80 - a) * b),
           ch(f"{(80 + a) / b:.1f} hours", "This adds the intercept instead of subtracting it.", (80 + a) / b)],
          f"80 = {a} + {b}x, so x = {x:.1f} hours.", difficulty="medium")

    # 6. Compare two predictions
    a, b = 38.4, -0.72
    diff = abs(b) * 4
    B.mcq(T, f"The equation of a regression line for predicting the time, in minutes, that a runner takes to finish a 5-kilometer race from the number of weeks of training is {yhat_eq(a, b)}. How does the predicted time for a runner who trained for 10 weeks compare with the predicted time for a runner who trained for 6 weeks?",
          ch(f"The predicted time is {diff:.2f} minutes less for the runner who trained for 10 weeks", "The x-values differ by 4 weeks, and the predicted time changes by 4 times the slope: 4(-0.72) = -2.88 minutes.", diff),
          [ch(f"The predicted time is {diff:.2f} minutes more for the runner who trained for 10 weeks", "The slope is negative, so more weeks of training means a smaller predicted time.", diff + 0.001),
           ch(f"The predicted time is {abs(b):.2f} minutes less for the runner who trained for 10 weeks", "The slope is the change in the predicted time for 1 week. The runners differ by 4 weeks.", abs(b)),
           ch(f"The predicted time is {abs(b) * 10:.1f} minutes less for the runner who trained for 10 weeks", "This multiplies the slope by 10 weeks instead of by the difference of 4 weeks between the two runners.", abs(b) * 10)],
          "The predicted response changes by b times the change in x: -0.72 x 4 = -2.88 minutes.", difficulty="medium")

    # 7. Is a line appropriate: a curved, levelling-off pattern
    xs = list(range(1, 13))
    ys = [round(30 * (1 - math.exp(-0.32 * x)) + random.Random(90 + x).uniform(-1.2, 1.2), 1) for x in xs]
    B.mcq(T, "A psychologist recorded the number of words that a person could recall from a list after each of 12 practice sessions. The scatterplot shows the number of words recalled against the number of practice sessions. A student wants to use a linear regression model to predict the number of words recalled. Which of the following is the best statement about the student's plan?",
          ch("A linear regression model is not appropriate, because the form of the association is curved: the number of words increases quickly at first and then levels off", "A linear model should be used only if the form of the association looks linear. These points curve."),
          [ch("A linear regression model is appropriate, because the direction of the association is positive and the number of words increases with practice", "A positive direction does not make a linear model appropriate. The form of the association must also be linear."),
           ch("A linear regression model is appropriate, because the number of words recalled never decreases as the number of practice sessions increases", "The points do not follow a line. The increases get smaller, so the form is curved."),
           ch("A linear regression model is not appropriate, because the association between the number of sessions and the words recalled is weak", "The association is not weak. The points closely follow a curve, and the problem is the curved form.")],
          "A linear regression model should be fit only if the data show a linear trend. This pattern is curved.",
          diagram=scatter(list(zip(xs, ys)), "Practice sessions", "Words recalled", alt="Scatterplot of words recalled against practice sessions: a curve that rises quickly and then levels off."), difficulty="medium")

    # 8. Extrapolation caution
    a, b = 25.3, 0.62
    pred = a + b * 150
    B.mcq(T, f"A company found the regression line {yhat_eq(a, b)} for predicting the monthly sales of a salesperson, in thousands of units, from the number of hours of training. The line was found using salespeople who had between 20 and 60 hours of training. A manager uses the line to predict the monthly sales of a salesperson who had 150 hours of training and gets {pred:.1f}. Which of the following is the best statement about the manager's prediction?",
          ch("The prediction is an extrapolation, because 150 hours is far beyond the 20 to 60 hours in the data, so it is not likely to be reliable", "A prediction for an x-value far outside the interval used to find the line is an extrapolation and is not reliable."),
          [ch("The prediction is reliable, because the regression line was found by a method that fits all of the data as closely as possible", "Fitting the data closely does not make predictions outside the interval of x-values reliable."),
           ch("The prediction is an interpolation, because 150 hours is a number that is greater than all of the numbers of hours in the data set of the company", "Interpolation is prediction inside the interval of the data. 150 is outside it."),
           ch("The prediction is reliable, because sales should keep increasing at the same rate for each additional hour of training that is given", "There is no evidence in the data that the pattern continues beyond 60 hours.")],
          "150 hours is well outside the 20 to 60 hours used to find the line, so the prediction is an extrapolation.", difficulty="hard")

    # 9. What y-hat means
    B.mcq(T, "In a linear regression model written as $\\hat{y} = a + bx$, what does $\\hat{y}$ represent?",
          ch("The predicted value of the response variable for a given value of the explanatory variable", "y-hat is the value of the response that the model predicts for the given x."),
          [ch("The observed value of the response variable for a given value of the explanatory variable", "The observed value is y. y-hat is the value predicted by the model."),
           ch("The mean of all of the observed values of the response variable in the data set that was used to find the model", "The mean of the response is written y-bar. y-hat is a prediction for a particular x."),
           ch("The value of the explanatory variable that is used to make a prediction with the model", "The explanatory variable is x. y-hat is the predicted response.")],
          "y-hat is the predicted response for a given x.", difficulty="easy")

    # 10-12: a shared scenario about practice and free-throw percentage
    a, b = 41.5, 3.9
    scenario = f"A basketball coach used data from players who practiced between 2 and 10 hours per week to find the regression line {yhat_eq(a, b, 1)}, where x is the number of hours of practice per week and y-hat is the predicted free-throw percentage."
    p6 = a + b * 6
    assert round(p6, 1) == 64.9
    B.mcq(T, scenario + " What is the predicted free-throw percentage for a player who practices 6 hours per week?",
          ch(f"{p6:.1f}%", f"Substitute x = 6: {a} + {b}(6) = {p6:.1f}.", p6),
          [ch(f"{b * 6:.1f}%", "This leaves out the y-intercept.", b * 6),
           ch(f"{a * 6 + b:.1f}%", "This multiplies the intercept by 6 instead of the slope.", a * 6 + b),
           ch(f"{a + b:.1f}%", "This adds the intercept and the slope and does not use x = 6.", a + b)],
          f"Predicted percentage = {a} + {b}(6) = {p6:.1f}.", difficulty="easy")

    p16 = a + b * 16
    assert round(p16, 1) == 103.9
    B.mcq(T, scenario + f" The coach uses the line to predict the free-throw percentage of a player who practices 16 hours per week and gets {p16:.1f}%. Which of the following is the best statement about this prediction?",
          ch("It is an extrapolation, and a free-throw percentage cannot be greater than 100%, which shows that the line should not be used for this many hours", "16 hours is far outside the 2 to 10 hours in the data, and a predicted percentage above 100 is impossible."),
          [ch("It is an interpolation, and it is reliable because the regression line was found from data on the free-throw percentage of players", "16 hours is outside the interval from 2 to 10 hours, so this is not interpolation."),
           ch("It is an extrapolation, but it is reliable because a larger number of hours of practice always leads to a larger free-throw percentage", "An extrapolation is not reliable, and a percentage above 100 shows that the pattern cannot continue."),
           ch("It is an interpolation, but it is not reliable because a player cannot practice for this many hours in a single week", "The problem is not that the number of hours is large. 16 hours is outside the interval of the data.")],
          "x = 16 is outside the interval from 2 to 10 hours, so the prediction is an extrapolation. A predicted percentage over 100% is impossible.", difficulty="hard")

    d = b * 4
    B.mcq(T, scenario + " How does the predicted free-throw percentage for a player who practices 8 hours per week compare with the predicted percentage for a player who practices 4 hours per week?",
          ch(f"It is {d:.1f} percentage points greater", "The players differ by 4 hours, and the predicted percentage changes by 4 times the slope: 4(3.9) = 15.6.", d),
          [ch(f"It is {b:.1f} percentage points greater", "The slope is the change in the predicted percentage for 1 hour. The players differ by 4 hours.", b),
           ch(f"It is {d:.1f} percentage points less", "The slope is positive, so more practice means a greater predicted percentage.", d + 0.001),
           ch(f"It is {2 * (a + 4 * b) - (a + 4 * b):.1f} percentage points greater", f"This is the predicted percentage for 4 hours, not the difference between the two predictions.", a + 4 * b)],
          "The difference in the predicted values is the slope times the difference in x: 3.9 x 4 = 15.6.", difficulty="medium")
