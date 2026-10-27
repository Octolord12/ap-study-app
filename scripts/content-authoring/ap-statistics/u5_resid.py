"""Unit 5, topic 5.4 Residuals (12 questions).

Required content (CED effective Fall 2026): 5.4.A a residual is the observed response minus the predicted response (residual = y - y-hat); 5.4.B a positive residual means the model
UNDERpredicts (underestimates) the response, a negative residual means it OVERpredicts (overestimates); 5.4.C a residual plot is a scatterplot of the residuals against the predicted
response values or the explanatory variable values; apparent randomness in a residual plot confirms a linear form and shows the linear model is appropriate; curvature suggests the
linear model is not the most appropriate model. Skills 3.B, 4.A, 4.D. (Not required here: patterns of changing spread, the standard deviation of the residuals, influential points.)
"""
from lib import *


def residuals(xs, ys):
    m = lsrl(xs, ys)
    return m, [y - (m.a + m.b * x) for x, y in zip(xs, ys)]


def build(B):
    T = 4

    # 1. Compute a residual
    a, b, x, y = 41, 6.5, 3, 68
    pred = a + b * x
    res = y - pred
    assert pred == 60.5 and res == 7.5
    B.mcq(T, f"The equation of a regression line for predicting a student's score on a vocabulary quiz from the number of hours that the student studied is {yhat_eq(a, b, 1)}. A student who studied for 3 hours scored 68 on the quiz. What is the residual for this student?",
          ch(f"{res:.1f}", f"The predicted score is {a} + {b}(3) = {pred}. The residual is observed minus predicted: 68 - {pred} = {res}.", res),
          [ch(f"{-res:.1f}", "This subtracts in the wrong order. A residual is observed minus predicted.", -res),
           ch(f"{pred}", "This is the predicted score, not the residual.", pred),
           ch(f"{y}", "This is the observed score, not the residual.", y)],
          f"Residual = observed - predicted = 68 - {pred} = {res}.", difficulty="easy")

    # 2. Interpret a negative residual
    B.mcq(T, "A regression line is used to predict a student's exam score from the number of hours studied. The residual for one student is -6.5. Which of the following is the best interpretation of this residual?",
          ch("The student's observed score was 6.5 points lower than the score that the model predicted, so the model overpredicted for this student", "A negative residual means the observed value is below the predicted value, so the model overpredicts."),
          [ch("The student's observed score was 6.5 points higher than the score that the model predicted, so the model underpredicted for this student", "A negative residual means the observed score is lower than the predicted score, not higher."),
           ch("The student's observed exam score was -6.5, so the student scored below zero on the exam and the data were recorded incorrectly", "A residual is a difference between the observed score and the predicted score. It is not the observed score."),
           ch("The student's predicted exam score was -6.5, so the regression line cannot be used to make a prediction for this student", "The residual is not the predicted score. It is the difference between the observed and predicted scores.")],
          "Residual = observed - predicted. A negative residual means the observed value is less than the predicted value, so the model overpredicts.", difficulty="medium")

    # 3. A point above the line
    B.mcq(T, "On a scatterplot that includes the regression line, one point is above the line. Which of the following is true about the residual for that point?",
          ch("The residual is positive, and the model underpredicts the response value for that point", "A point above the line has an observed value greater than the predicted value, so the residual is positive and the model underpredicts."),
          [ch("The residual is positive, and the model overpredicts the response value for that point", "A positive residual means the model underpredicts, not overpredicts."),
           ch("The residual is negative, and the model underpredicts the response value for that point", "A point above the line has a positive residual."),
           ch("The residual is zero, because the point is close to the regression line and so the observed and predicted values are equal", "A residual of zero means the point is exactly on the line. This point is above it.")],
          "A point above the line has an observed response greater than predicted: the residual is positive and the model underpredicts.", difficulty="easy")

    # 4. Residual plot: no pattern
    xs = list(range(1, 25))
    ys = noisy_line(xs, 8, 2.6, 9, seed=3, places=1)
    m, res = residuals(xs, ys)
    quad = np.polyfit(xs, res, 2)[0]
    assert abs(quad) < 0.05 and max(abs(r_) for r_ in res) < 10, (quad, max(res), min(res))
    B.mcq(T, "A linear regression model was fit to predict the weekly sales of a product, in hundreds of units, from the number of weeks since the product was introduced. The residual plot for the model is shown. Which of the following is the best conclusion from the residual plot?",
          ch("The residuals show no clear pattern, which confirms that the association is linear and the linear model is appropriate", "Apparent randomness in a residual plot confirms a linear form and shows that the linear model is appropriate."),
          [ch("The residuals show a clear curved pattern, which shows that the association is non-linear and the linear model is not appropriate", "The residuals are scattered at random above and below zero. There is no curvature."),
           ch("The linear model is not appropriate, because the residuals are not all equal to zero for the weeks that are shown", "Residuals are never all zero. A residual plot with no pattern supports the model."),
           ch("The linear model is appropriate, because the residual plot has a positive slope that is the same as the slope of the regression line", "A residual plot of a least-squares fit does not show the slope of the line. The important feature is the lack of a pattern.")],
          "Random scatter of the residuals around zero indicates that a linear model is appropriate.",
          diagram=scatter(list(zip(xs, res)), "Weeks since introduction", "Residual", zero_line=True, alt="Residual plot: residuals against weeks, scattered at random above and below zero with no pattern."), difficulty="medium")

    # 5. Residual plot: curved
    xs = list(range(1, 25))
    ys = [round(6 + 0.28 * (x - 12.5) ** 2 + random.Random(500 + x).uniform(-3, 3), 1) for x in xs]
    m, res = residuals(xs, ys)
    assert res[0] > 3 and res[-1] > 3 and res[11] < -3, (res[0], res[11], res[-1])
    B.mcq(T, "A linear regression model was fit to predict the stopping distance of a vehicle, in meters, from its speed. The residual plot for the model is shown. Which of the following is the best conclusion from the residual plot?",
          ch("The residuals show a clear curved pattern, which suggests that the linear model is not the most appropriate model for the data", "Curvature in a residual plot suggests that a linear model is not the most appropriate model."),
          [ch("The linear model is appropriate, because some of the residuals are positive and some of the residuals are negative", "Both signs always occur. What matters is whether there is a pattern, and this residual plot shows a curve."),
           ch("The linear model is appropriate, because the positive residuals and the negative residuals cancel each other out", "Residuals always balance out around the line. A curved pattern still shows that the linear form is not appropriate."),
           ch("The association between the variables is strong and linear, because the points in the residual plot follow a clear and easily visible pattern", "A clear pattern in a residual plot means the model does not describe the data well. It does not show a linear association.")],
          "The residuals are positive at both ends and negative in the middle, a curved pattern, so a linear model is not the most appropriate.",
          diagram=scatter(list(zip(xs, res)), "Speed (x)", "Residual", zero_line=True, alt="Residual plot: residuals against speed, forming a U shape: positive, then negative, then positive."), difficulty="medium")

    # 6. Observed from a residual
    a, b, x, resid = 4.1, 0.52, 30, -2.3
    pred = a + b * x
    obs = pred + resid
    assert round(pred, 1) == 19.7 and round(obs, 1) == 17.4
    B.mcq(T, f"The equation of a regression line is {yhat_eq(a, b)}. For an observation with x = 30, the residual is {resid}. What is the observed value of y for this observation?",
          ch(f"{obs:.1f}", f"The predicted value is {a} + {b}(30) = {pred:.1f}. Since residual = observed - predicted, observed = predicted + residual = {pred:.1f} + ({resid}) = {obs:.1f}.", obs),
          [ch(f"{pred - resid:.1f}", "This subtracts the residual from the predicted value. Observed = predicted + residual.", pred - resid),
           ch(f"{pred:.1f}", "This is the predicted value, not the observed value.", pred),
           ch(f"{x + resid:.1f}", "This adds the residual to x instead of to the predicted value.", x + resid)],
          f"Observed = predicted + residual = {pred:.1f} + ({resid}) = {obs:.1f}.", difficulty="medium")

    # 7. What a residual plot is
    B.mcq(T, "A residual plot for a linear regression model is a scatterplot of which of the following?",
          ch("The residuals versus the explanatory variable values, or the residuals versus the predicted response values", "A residual plot shows the residuals on the vertical axis, against either the explanatory variable or the predicted response."),
          [ch("The observed response values versus the predicted response values, with the regression line drawn through the points", "That plot compares observed and predicted values. A residual plot shows the differences between them."),
           ch("The predicted response values versus the explanatory variable values, with the residuals as the labels of the points", "The predicted values lie on a line when plotted against the explanatory variable. The residuals are plotted on the vertical axis."),
           ch("The explanatory variable values versus the observed response values, with the regression line drawn through the points", "That is the original scatterplot, not a residual plot.")],
          "A residual plot is a scatterplot of the residuals versus the predicted response values (or the explanatory variable values).", difficulty="easy")

    # 8. Largest overprediction from a table
    rows = [("A", 52, 48), ("B", 61, 69), ("C", 75, 74), ("D", 90, 95)]
    rs = {k: o - p for k, o, p in rows}
    assert rs == {"A": 4, "B": -8, "C": 1, "D": -5}
    B.mcq(T, "A regression line was used to predict the response for four observations. The observed and predicted values are shown in the table. For which observation did the model overpredict by the greatest amount?",
          ch("Observation B, which has a residual of -8", "Overprediction means the observed value is less than the predicted value. B has the most negative residual: 61 - 69 = -8."),
          [ch("Observation A, which has a residual of 4", "A has a positive residual, so the model underpredicted for A."),
           ch("Observation C, which has a residual of 1", "C has a positive residual, so the model underpredicted for C."),
           ch("Observation D, which has a residual of -5", "D was overpredicted, but by less than B. A residual of -5 is smaller in size than -8.")],
          "The greatest overprediction is the most negative residual, observed - predicted = 61 - 69 = -8, for observation B.",
          diagram=table(["Observation", "Observed value", "Predicted value"], rows, caption="Observed and predicted values", row_headers=True), difficulty="medium")

    # 9. A point above the line on a scatterplot with the line drawn
    xs = list(range(1, 13))
    ys = noisy_line(xs, 20, 3.1, 4, seed=15, places=0)
    ys = [int(v) for v in ys]
    ys[7] = ys[7] + 14
    m = lsrl(xs, ys)
    assert ys[7] - (m.a + m.b * xs[7]) > 8
    B.mcq(T, "The scatterplot shows the least-squares regression line for predicting the amount of money a store collects in a day, in hundreds of dollars, from the number of customers, in hundreds. The point labeled P is above the line. Which of the following is a correct statement about the residual for P?",
          ch("The residual is positive, because the observed value is greater than the value predicted by the line, so the model underpredicts for P", "P is above the line, so the observed value is greater than the predicted value. The residual is positive and the model underpredicts."),
          [ch("The residual is negative, because the point is above the line and so the observed value is less than the predicted value, so the model overpredicts for P", "A point above the line has a positive residual. The model underpredicts."),
           ch("The residual is positive, because the observed value is greater than the value predicted by the line, so the model overpredicts for P", "The residual is positive, but a positive residual means the model underpredicts."),
           ch("The residual is zero, because the point P is close to the line and so the observed and predicted values are the same", "A residual is zero only when the point is exactly on the line. P is above it.")],
          "Above the line means observed > predicted: a positive residual and an underprediction.",
          diagram=scatter(list(zip(xs, ys)), "Customers (hundreds)", "Money collected (hundreds of dollars)", line=(m.a, m.b), highlights=[(7, "P")], alt="Scatterplot with the regression line: a positive pattern; the point labeled P is well above the line."), difficulty="medium")

    # 10. A point far below zero in a residual plot
    xs = list(range(1, 21))
    ys = noisy_line(xs, 30, 2.0, 5, seed=41, places=1)
    ys[13] -= 15
    m, res = residuals(xs, ys)
    assert -19 < res[13] < -11 and all(abs(r_) < 8 for i, r_ in enumerate(res) if i != 13), res
    q = round(res[13])
    B.mcq(T, f"The residual plot is for a linear model that predicts the fuel efficiency of a car, in miles per gallon, from the age of the car, in years. The point labeled Q has a residual of about {q}. Which of the following is the best interpretation of the residual for Q?",
          ch(f"The observed fuel efficiency for the car at Q was about {abs(q)} miles per gallon lower than the model predicted, so the model overpredicted for this car", "A negative residual means observed minus predicted is negative: the observed value is lower than the predicted value."),
          [ch(f"The observed fuel efficiency for the car at Q was about {abs(q)} miles per gallon higher than the model predicted, so the model underpredicted for this car", "A negative residual means the model overpredicted, not underpredicted."),
           ch(f"The observed fuel efficiency for the car at Q was about {q} miles per gallon, which is not possible, so the data for this car must be wrong", "The residual is the difference between the observed and predicted values. It is not the observed value."),
           ch(f"The predicted fuel efficiency for the car at Q was about {q} miles per gallon, so the model should not be used for a car like this one", "The residual is not the predicted value. It is observed minus predicted.")],
          f"A residual of about {q} means the observed value was about {abs(q)} units below the predicted value.",
          diagram=scatter(list(zip(xs, res)), "Age of the car (years)", "Residual", zero_line=True, highlights=[(13, "Q")], alt="Residual plot: residuals against age; most are scattered near zero, and the point labeled Q is far below zero."), difficulty="hard")

    # 11-12. Shared scenario: hot chocolate sales
    a, b, x, y = 142, -3.6, 15, 91
    scenario = f"A cafe owner recorded the outside temperature, in degrees Celsius, and the number of cups of hot chocolate sold on each of many days. The regression line for predicting the number of cups sold from the temperature is {yhat_eq(a, b, 1)}. On one day the temperature was {x} degrees Celsius and {y} cups were sold."
    pred = a + b * x
    res = y - pred
    assert round(pred, 1) == 88.0 and round(res, 1) == 3.0
    B.mcq(T, scenario + " What is the residual for that day?",
          ch(f"{res:.0f} cups", f"The predicted number of cups is {a} + ({b})({x}) = {pred:.0f}. The residual is 91 - {pred:.0f} = {res:.0f}.", res),
          [ch(f"{-res:.0f} cups", "This subtracts in the wrong order. A residual is observed minus predicted.", -res),
           ch(f"{pred:.0f} cups", "This is the predicted number of cups, not the residual.", pred),
           ch(f"{y} cups", "This is the observed number of cups, not the residual.", y)],
          f"Predicted = {pred:.0f}; residual = 91 - {pred:.0f} = {res:.0f}.", difficulty="easy")

    B.mcq(T, scenario + " Which of the following is the best interpretation of the residual for that day?",
          ch("The cafe sold 3 more cups of hot chocolate than the number predicted by the model, so the model underpredicted for that day", "The residual is positive (observed - predicted = 3), so the observed value is 3 greater than predicted and the model underpredicts."),
          [ch("The cafe sold 3 fewer cups of hot chocolate than the number predicted by the model, so the model overpredicted for that day", "The residual is positive, so the cafe sold more cups than predicted."),
           ch("The cafe sold 3 more cups of hot chocolate than the number predicted by the model, so the model overpredicted for that day", "The cafe did sell more than predicted, but that means the model underpredicted."),
           ch("The cafe sold exactly 3 cups of hot chocolate on that day, which is the number that was predicted by the model", "The residual is the difference between the observed and the predicted number of cups, not the number sold.")],
          "A residual of +3 means that the observed number of cups was 3 more than predicted: the model underpredicted.", difficulty="medium")
