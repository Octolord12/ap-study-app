"""Unit 5: six free-response prompts, 10 points each.

  ANALYZE_DATA (Q2: practices 3 and 4)         5.2  sleep and reaction time        correlation, slope, prediction, residual, r squared, causation
  ANALYZE_DATA                                  5.4  laptop age and resale value    a CURVED residual plot, interpolation and extrapolation, what r squared does not show
  ANALYZE_DATA                                  5.5  tutoring hours and improvement computer output, the intercept, r from R-sq, extrapolation
  MULTI_FOCUS  (Q4: practices 2, 3 and 4)       5.1  trees and block temperature    sampling, an observational study, regression
  MULTI_FOCUS                                   5.5  height and arm span            simple random sample, a z-score, regression, r squared and units
  MULTI_FOCUS                                   5.3  exit velocity and distance      a normal probability, regression, a random residual plot, extrapolation

Layout follows the CED's sample questions: a stimulus, then parts A to E with labelled sub-parts; one rubric line per point, in the order of the parts.
Every number is computed here from the data that is plotted, and the coefficients the prompt gives are the ones the sample response uses.
"""
import random

from scipy import stats as sps

from lib import *

YH = r"$\hat{y}$"
INSTR = "Use the given information to respond to parts A, B, C, D, and E. Label any subparts (e.g., i and ii) that may be present."


def gen(n, lo, hi, a, b, noise, seed, xp=1, yp=0):
    rnd = random.Random(seed)
    step = (hi - lo) / (n - 1)
    xs = sorted(round(lo + step * i + rnd.uniform(-0.3, 0.3) * step * 2, xp) for i in range(n))
    ys = [round(a + b * x + rnd.uniform(-noise, noise), yp) for x in xs]
    return xs, ys


def build(B):
    # ------------------------------------------------------------------------------------------------------ 1. sleep and reaction time
    xs, ys = gen(18, 5.0, 9.0, 420, -22, 28, 2, 1, 0)
    m = lsrl(xs, ys)
    ys = [int(v) for v in ys]
    m = lsrl(xs, ys)
    A, Bs = round(m.a, 2), round(m.b, 2)
    r, r2 = round(m.r, 2), round(m.r2, 2)
    i = xs.index(7.5)
    obs = ys[i]
    pred = A + Bs * 7.5
    res = obs - pred
    assert -0.9 < m.r < -0.8 and abs(res) > 5, (m.r, res)
    verdict = "lower" if res < 0 else "higher"
    over = "overpredicted" if res < 0 else "underpredicted"
    B.frq(2, "ANALYZE_DATA",
          f"A researcher studied whether the amount of sleep that college students get is related to their reaction times. The researcher selected a random sample of 18 students and recorded, for each student, the number of hours of sleep the student got the night before and the student's time to react to a visual signal, in milliseconds (ms). The scatterplot shows the data.\n\n"
          f"Technology was used to analyze the data. The least-squares regression line for predicting reaction time from hours of sleep has a y-intercept of {A} and a slope of {Bs}. The correlation coefficient is r = {r}, and the coefficient of determination is $r^2$ = {r2}.\n\n"
          f"{INSTR}\n\n"
          "**A.** Describe the association between the number of hours of sleep and reaction time that is shown in the scatterplot. Describe the form, the direction, and the strength of the association, in context.\n\n"
          "**B.** (i) Interpret the correlation coefficient in context.\n\n(ii) A classmate looks at the results and says, \"Getting more sleep makes a student react faster.\" Explain why the study does not justify the classmate's conclusion.\n\n"
          "**C.** (i) Write the equation of the least-squares regression line. Define any variables that you use in the equation.\n\n(ii) Interpret the slope of the line in context.\n\n"
          f"**D.** One of the 18 students slept 7.5 hours and had a reaction time of {obs} ms.\n\n(i) Calculate the predicted reaction time for a student who slept 7.5 hours.\n\n(ii) Calculate the residual for this student, and interpret the residual in context.\n\n"
          f"**E.** Interpret the coefficient of determination, $r^2$ = {r2}, in context.",
          [(1, "A: Describes the form and direction in context: the association is linear and negative (students who sleep more hours tend to have shorter reaction times)."),
           (1, "A: Describes the strength in context: the association is strong (the points are close to the line), consistent with the correlation coefficient."),
           (1, f"B(i): Interprets r in context: r = {r} indicates a strong, negative, linear association between hours of sleep and reaction time."),
           (1, "B(ii): Explains that an association does not show cause and effect. Students were not assigned amounts of sleep (this is an observational study), so other factors could explain the association. (A random sample allows generalizing to the population, not concluding causation.)"),
           (1, f"C(i): Writes the equation with variables defined: predicted reaction time = {A} {signed(Bs)}(hours of sleep), or {YH} = {A} {signed(Bs)}x with x = hours of sleep and {YH} = predicted reaction time in ms."),
           (1, f"C(ii): Interprets the slope in context: for each additional hour of sleep, the predicted reaction time decreases by about {abs(Bs)} ms."),
           (1, f"D(i): Calculates the predicted reaction time: {A} {signed(Bs)}(7.5) = {pred:.1f} ms."),
           (1, f"D(ii): Calculates the residual = observed - predicted = {obs} - {pred:.1f} = {res:.1f} ms."),
           (1, f"D(ii): Interprets the residual in context: the observed reaction time of this student was about {abs(res):.1f} ms {verdict} than the model predicted (the model {over})."),
           (1, f"E: Interprets $r^2$ in context: about {r2 * 100:.0f}% of the variation in reaction times is explained by the linear relationship with hours of sleep.")],
          f"A. The scatterplot shows a linear, negative association: students who slept more hours tended to have shorter reaction times. The points are close to a line, so the association is strong.\n\n"
          f"B. (i) r = {r} means that there is a strong, negative, linear association between hours of sleep and reaction time. (ii) Students were not assigned how much to sleep, so this is an observational study. It shows an association but not cause and effect, because other factors (for example, general health or how alert a student is) could be related to both sleep and reaction time.\n\n"
          f"C. (i) {YH} = {A} {signed(Bs)}x, where x is the number of hours of sleep and {YH} is the predicted reaction time in ms. (ii) For each additional hour of sleep, the predicted reaction time decreases by about {abs(Bs)} ms.\n\n"
          f"D. (i) {YH} = {A} {signed(Bs)}(7.5) = {pred:.1f} ms. (ii) The residual is {obs} - {pred:.1f} = {res:.1f} ms. This student's reaction time was about {abs(res):.1f} ms {verdict} than the model predicted.\n\n"
          f"E. About {r2 * 100:.0f}% of the variation in reaction times is explained by the linear relationship with hours of sleep.",
          diagram=scatter(list(zip(xs, ys)), "Hours of sleep", "Reaction time (ms)", alt="Scatterplot of reaction time against hours of sleep for 18 students: a strong negative linear pattern."))

    # ------------------------------------------------------------------------------------------------------ 2. laptop age and resale value (curved residuals)
    rnd = random.Random(7)
    xs = [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.0, 4.5, 5.0, 5.0, 5.5, 6.0, 6.0, 6.5, 7.0]
    ys = [round(9.6 * math.exp(-0.34 * x) * 100 / 100 + rnd.uniform(-0.25, 0.25), 2) for x in xs]
    m = lsrl(xs, ys)
    resid = [y - (m.a + m.b * x) for x, y in zip(xs, ys)]
    A, Bs = round(m.a, 2), round(m.b, 2)
    r2 = round(m.r2, 2)
    assert m.r2 > 0.88 and resid[0] > 0.2 and resid[-1] > -0.1 and min(resid) < -0.3, (m.r2, resid)
    k = xs.index(6.0)
    obs = ys[k]
    pred4 = A + Bs * 4
    pred10 = A + Bs * 10
    assert pred10 < 0
    pred6 = A + Bs * 6
    res = obs - pred6
    B.frq(4, "ANALYZE_DATA",
          f"A resale website recorded the age, in years, and the resale value, in hundreds of dollars, of 16 laptop computers of the same model that were sold on the site. A linear regression model was used to predict resale value from age. The ages in the data are between 1 year and 7 years. The residual plot for the model is shown.\n\n"
          f"The least-squares regression line is {YH} = {A} {signed(Bs)}x, where x is the age of the laptop in years and {YH} is the predicted resale value in hundreds of dollars. The coefficient of determination is $r^2$ = {r2}.\n\n"
          f"{INSTR}\n\n"
          "**A.** Based on the residual plot, is a linear model appropriate for these data? Justify your answer.\n\n"
          "**B.** (i) Use the regression line to calculate the predicted resale value of a laptop that is 4 years old.\n\n(ii) A student uses the regression line to predict the resale value of a laptop that is 10 years old. Identify the type of prediction this is, and explain why the prediction is less reliable than the prediction in part (i).\n\n"
          f"**C.** A laptop that is 6 years old sold for {obs} hundred dollars. Calculate the residual for this laptop, and interpret the residual in context.\n\n"
          f"**D.** A student says, \"Because $r^2$ = {r2}, {r2 * 100:.0f}% of the laptops lie on the regression line, so a linear model is appropriate.\" Identify two errors in the student's statement.\n\n"
          "**E.** Interpret the slope of the regression line in context.",
          [(1, "A: States that a linear model is not appropriate (not the most appropriate model) for these data."),
           (1, "A: Justifies using the residual plot: the residuals show a curved pattern (positive for the youngest and the oldest laptops and negative in the middle) instead of random scatter around zero."),
           (1, f"B(i): Calculates the predicted resale value for a 4-year-old laptop: {A} {signed(Bs)}(4) = {pred4:.2f} hundred dollars."),
           (1, "B(ii): Identifies the prediction for a 10-year-old laptop as an extrapolation (10 years is outside the ages from 1 to 7 years in the data)."),
           (1, f"B(ii): Explains that the prediction is less reliable because the pattern may not continue beyond the ages in the data (the farther from the data, the less reliable), and the linear model does not fit the curved pattern. (For example, the line gives {A} {signed(Bs)}(10) = {pred10:.2f} hundred dollars, a negative resale value, which is impossible.)"),
           (1, f"C: Calculates the residual = observed - predicted = {obs} - {pred6:.2f} = {res:.2f} hundred dollars."),
           (1, f"C: Interprets the residual in context: this laptop sold for about {abs(res):.2f} hundred dollars {'more' if res > 0 else 'less'} than the model predicted for a 6-year-old laptop."),
           (1, f"D: Identifies the first error: $r^2$ is the proportion of the variation in resale value that is explained by the linear relationship with age (about {r2 * 100:.0f}%), not the percent of laptops that lie on the line."),
           (1, f"D: Identifies the second error: a large $r^2$ does not mean that a linear model is appropriate. The residual plot shows curvature, so the linear model is not appropriate."),
           (1, f"E: Interprets the slope in context: for each additional year of age, the predicted resale value decreases by about {abs(Bs):.2f} hundred dollars.")],
          f"A. No. A linear model is not appropriate. The residual plot has a curved pattern: the residuals are positive for the newest and the oldest laptops and negative for the laptops in the middle. If a linear model were appropriate, the residuals would be scattered at random around zero.\n\n"
          f"B. (i) {YH} = {A} {signed(Bs)}(4) = {pred4:.2f}, so the predicted resale value is about {pred4:.2f} hundred dollars. (ii) A 10-year-old laptop is outside the ages from 1 to 7 years in the data, so the prediction is an extrapolation. It is less reliable because we do not know that the pattern continues beyond 7 years, and the relationship is curved, not linear. In fact, the line gives {A} {signed(Bs)}(10) = {pred10:.2f} hundred dollars, a negative resale value, which is impossible.\n\n"
          f"C. The predicted value for a 6-year-old laptop is {A} {signed(Bs)}(6) = {pred6:.2f}. The residual is {obs} - {pred6:.2f} = {res:.2f} hundred dollars. This laptop sold for about {abs(res):.2f} hundred dollars {'more' if res > 0 else 'less'} than the model predicted.\n\n"
          f"D. First, $r^2$ = {r2} means that about {r2 * 100:.0f}% of the variation in resale value is explained by the linear relationship with age. It does not mean that {r2 * 100:.0f}% of the laptops lie on the line. Second, a large $r^2$ does not show that a linear model is appropriate. The residual plot has a curved pattern, so the linear model is not appropriate.\n\n"
          f"E. For each additional year of age, the predicted resale value decreases by about {abs(Bs):.2f} hundred dollars.",
          diagram=scatter(list(zip(xs, resid)), "Age of the laptop (years)", "Residual (hundreds of dollars)", zero_line=True, alt="Residual plot: residuals against age, with a U-shaped (curved) pattern."))

    # ------------------------------------------------------------------------------------------------------ 3. tutoring hours and score improvement (output)
    xs = [0, 0.5, 1, 1.5, 2, 3, 3, 4, 5, 5.5, 6, 7, 7.5, 8, 9, 10]
    rnd = random.Random(5)
    ys = [int(round(3.0 + 4.5 * x + rnd.uniform(-11, 11))) for x in xs]
    m = lsrl(xs, ys)
    A, Bs = round(m.a, 2), round(m.b, 2)
    r2 = round(m.r2, 3)
    rr = math.sqrt(r2)
    assert 0 in xs and 0.75 < m.r < 0.95, (xs, m.r)
    obs5 = ys[min(range(len(xs)), key=lambda j: abs(xs[j] - 5.0))]
    x5 = xs[min(range(len(xs)), key=lambda j: abs(xs[j] - 5.0))]
    pred5 = A + Bs * x5
    res5 = obs5 - pred5
    pred40 = A + Bs * 40
    B.frq(5, "ANALYZE_DATA",
          f"A tutoring center wants to know how the number of hours that a student is tutored is related to the student's improvement on a placement test. The center selected a random sample of 16 students and recorded, for each student, the number of hours of tutoring received (between 0 and 10 hours) and the improvement in the student's test score, in points. The scatterplot shows the data.\n\n"
          f"Technology output for the least-squares regression line for predicting improvement from hours of tutoring is shown.\n\n"
          f"Constant: {A}\nHours of tutoring: {Bs}\nR-sq = {r2 * 100:.1f}%\n\n"
          f"{INSTR}\n\n"
          "**A.** (i) Identify the explanatory variable.\n\n(ii) Describe the form and the direction of the association shown in the scatterplot, in context.\n\n"
          "**B.** (i) Write the equation of the least-squares regression line. Define any variables that you use in the equation.\n\n(ii) Interpret the y-intercept of the line in context, or explain why it cannot be interpreted.\n\n"
          f"**C.** One student in the sample received {x5:g} hours of tutoring and improved by {obs5} points.\n\n(i) Calculate the predicted improvement for a student who received {x5:g} hours of tutoring.\n\n(ii) Calculate the residual for this student.\n\n"
          "**D.** (i) Determine the value of the correlation coefficient, r. Show how you found it.\n\n(ii) Interpret the coefficient of determination in context.\n\n"
          "**E.** A tutor uses the regression line to predict the improvement of a student who received 40 hours of tutoring.\n\n(i) Identify the type of prediction this is.\n\n(ii) Explain why this prediction is not reasonable.",
          [(1, "A(i): Identifies the explanatory variable as the number of hours of tutoring (it is the variable used to predict improvement)."),
           (1, "A(ii): Describes the form and direction in context: the association is linear and positive (students with more hours of tutoring tend to have greater improvement)."),
           (1, f"B(i): Writes the equation with variables defined: predicted improvement = {A} {signed(Bs)}(hours of tutoring), or {YH} = {A} {signed(Bs)}x with x = hours of tutoring and {YH} = predicted improvement in points."),
           (1, f"B(ii): Interprets the y-intercept in context: the predicted improvement for a student who received 0 hours of tutoring is {A} points. (0 hours is within the data, so the interpretation is reasonable.)"),
           (1, f"C(i): Calculates the predicted improvement: {A} {signed(Bs)}({x5:g}) = {pred5:.2f} points."),
           (1, f"C(ii): Calculates the residual = observed - predicted = {obs5} - {pred5:.2f} = {res5:.2f} points."),
           (1, f"D(i): Determines r = {rr:.3f} (the positive square root of {r2:.3f}, positive because the slope is positive)."),
           (1, f"D(ii): Interprets the coefficient of determination in context: about {r2 * 100:.1f}% of the variation in improvement is explained by the linear relationship with hours of tutoring."),
           (1, "E(i): Identifies the prediction as an extrapolation (40 hours is outside the 0 to 10 hours in the data)."),
           (1, f"E(ii): Explains that the prediction is not reasonable because it extrapolates far beyond the data (the line may not continue to hold) and the predicted improvement of {pred40:.0f} points is not realistic for a test score.")],
          f"A. (i) The explanatory variable is the number of hours of tutoring. (ii) The association is linear and positive: students who had more hours of tutoring tended to improve by more points.\n\n"
          f"B. (i) {YH} = {A} {signed(Bs)}x, where x is the number of hours of tutoring and {YH} is the predicted improvement in points. (ii) The predicted improvement for a student who received 0 hours of tutoring is {A} points. This makes sense because 0 hours is in the data.\n\n"
          f"C. (i) {YH} = {A} {signed(Bs)}({x5:g}) = {pred5:.2f} points. (ii) The residual is {obs5} - {pred5:.2f} = {res5:.2f} points.\n\n"
          f"D. (i) The slope is positive and R-sq = {r2 * 100:.1f}%, so r = +sqrt({r2:.3f}) = {rr:.3f}. (ii) About {r2 * 100:.1f}% of the variation in improvement is explained by the linear relationship with hours of tutoring.\n\n"
          f"E. (i) This is an extrapolation, because 40 hours is far outside the 0 to 10 hours in the data. (ii) The prediction is not reasonable: we do not know that the linear pattern continues so far beyond the data, and the line predicts an improvement of {A} {signed(Bs)}(40) = {pred40:.0f} points, which is not realistic for a test score.",
          diagram=scatter(list(zip(xs, ys)), "Hours of tutoring", "Improvement (points)", x_axis=(0, 10, 2), alt="Scatterplot of improvement against hours of tutoring for 16 students: a positive linear pattern."))

    # ------------------------------------------------------------------------------------------------------ 4. trees and block temperature (observational study)
    xs, ys = gen(25, 2, 40, 98.5, -0.28, 2.8, 8, 0, 1)
    xs = [int(v) for v in xs]
    m = lsrl(xs, ys)
    A, Bs = round(m.a, 2), round(m.b, 3)
    assert -0.95 < m.r < -0.75, m.r
    k = min(range(len(xs)), key=lambda j: abs(xs[j] - 12))
    x12, obs12 = xs[k], ys[k]
    pred30 = A + Bs * 30
    pred12 = A + Bs * x12
    res12 = obs12 - pred12
    B.frq(1, "MULTI_FOCUS",
          f"A city official wants to know whether blocks in the city that have more trees are cooler on hot days. The city has 800 blocks. The official used a random number generator to select a simple random sample of 25 of the blocks. On one hot afternoon, the official recorded for each selected block the number of trees on the block and the average temperature on the block, in degrees Fahrenheit. The scatterplot shows the data.\n\n"
          f"The least-squares regression line for predicting temperature from the number of trees is {YH} = {A} {signed(Bs, 3)}x, where x is the number of trees on a block and {YH} is the predicted temperature in degrees Fahrenheit.\n\n"
          f"{INSTR}\n\n"
          "**A.** (i) Identify the type of study (experiment or observational study) that the official conducted.\n\n(ii) Explain why the results of the study can be generalized to all 800 blocks in the city.\n\n"
          "**B.** Describe the form, the direction, and the strength of the association shown in the scatterplot, in context.\n\n"
          f"**C.** (i) Interpret the slope of the regression line in context.\n\n(ii) Calculate the predicted temperature for a block that has 30 trees.\n\n"
          "**D.** The official concludes, \"Planting more trees on a block will lower the temperature on the block.\"\n\n(i) Explain why the study does not justify this conclusion.\n\n(ii) Identify a variable, other than the number of trees, that could explain why blocks with more trees were cooler.\n\n"
          f"**E.** One block in the sample had {x12} trees and an average temperature of {obs12} degrees Fahrenheit. Calculate the residual for this block, and interpret the residual in context.",
          [(1, "A(i): Identifies the study as an observational study (the official did not assign the number of trees to blocks)."),
           (1, "A(ii): Explains that the blocks were selected at random (a simple random sample), so the sample should be representative of all 800 blocks and the results can be generalized to them."),
           (1, "B: Describes the form and direction in context: the association is linear and negative (blocks with more trees tend to have lower temperatures)."),
           (1, "B: Describes the strength in context: the association is strong (the points are close to a line)."),
           (1, f"C(i): Interprets the slope in context: for each additional tree on a block, the predicted temperature decreases by about {abs(Bs):.3f} degrees Fahrenheit."),
           (1, f"C(ii): Calculates the predicted temperature for 30 trees: {A} {signed(Bs, 3)}(30) = {pred30:.1f} degrees Fahrenheit."),
           (1, "D(i): Explains that an observational study can show an association but not cause and effect, because the number of trees was not randomly assigned to blocks."),
           (1, "D(ii): Identifies a plausible variable that could explain the association, such as the amount of pavement or buildings on the block, or the amount of shade or open space, which could be related to both the number of trees and the temperature."),
           (1, f"E: Calculates the residual = observed - predicted = {obs12} - {pred12:.1f} = {res12:.1f} degrees Fahrenheit."),
           (1, f"E: Interprets the residual in context: this block was {abs(res12):.1f} degrees Fahrenheit {'warmer' if res12 > 0 else 'cooler'} than the model predicted for a block with {x12} trees.")],
          f"A. (i) The official conducted an observational study, because the number of trees on each block was not assigned by the official. (ii) The blocks were selected with a simple random sample from all 800 blocks, so the sample is likely to be representative of the blocks in the city, and the results can be generalized to all 800 blocks.\n\n"
          f"B. The association is linear and negative: blocks with more trees tend to have lower average temperatures. The points are close to a line, so the association is strong.\n\n"
          f"C. (i) For each additional tree on a block, the predicted average temperature decreases by about {abs(Bs):.3f} degrees Fahrenheit. (ii) {YH} = {A} {signed(Bs, 3)}(30) = {pred30:.1f} degrees Fahrenheit.\n\n"
          f"D. (i) This is an observational study, so it shows an association between the number of trees and the temperature but cannot show that planting trees causes the temperature to go down. (ii) The amount of pavement and buildings on a block could be related to both the number of trees (fewer trees where there is more pavement) and the temperature (more pavement is hotter).\n\n"
          f"E. The predicted temperature for {x12} trees is {A} {signed(Bs, 3)}({x12}) = {pred12:.1f}. The residual is {obs12} - {pred12:.1f} = {res12:.1f}. This block was {abs(res12):.1f} degrees Fahrenheit {'warmer' if res12 > 0 else 'cooler'} than the model predicted.",
          diagram=scatter(list(zip(xs, ys)), "Number of trees on the block", "Average temperature (degrees F)", alt="Scatterplot of average temperature against number of trees for 25 blocks: a strong negative linear pattern."))

    # ------------------------------------------------------------------------------------------------------ 5. height and arm span (SRS, z-score, regression, units)
    xs, ys = gen(30, 60.0, 74.0, -2.1, 1.02, 1.5, 4, 1, 1)
    j = len(xs) // 2
    xs[j] = 70.3
    ys[j] = round(-2.1 + 1.02 * 70.3 + 1.4, 1)
    xs, ys = zip(*sorted(zip(xs, ys)))
    xs, ys = list(xs), list(ys)
    m = lsrl(xs, ys)
    A, Bs = round(m.a, 2), round(m.b, 3)
    r2 = round(m.r2, 3)
    mean_h, sd_h = round(mean(xs), 1), round(sd(xs), 1)
    z = (70.3 - mean_h) / sd_h
    assert 0.5 < z < 2.0, z
    k = xs.index(70.3)
    obs = ys[k]
    pred = A + Bs * 70.3
    res = obs - pred
    assert m.r2 > 0.85, m.r2
    B.frq(5, "MULTI_FOCUS",
          f"A school has 600 students. A teacher wants to select a simple random sample of 30 of the students and measure each selected student's height and arm span, both in inches, to see how well height can be used to predict arm span. The scatterplot shows the data for the 30 students who were selected, with the least-squares regression line.\n\n"
          f"The heights of the students in the sample have a mean of {mean_h} inches and a standard deviation of {sd_h} inches. The regression line for predicting arm span from height is {YH} = {A} {signed(Bs, 3)}x, where x is height in inches and {YH} is the predicted arm span in inches. The coefficient of determination is $r^2$ = {r2}.\n\n"
          f"{INSTR}\n\n"
          "**A.** Describe a method that the teacher could use to select a simple random sample of 30 students from the 600 students. Include a description of how the random numbers are used.\n\n"
          "**B.** One student in the sample is 70.3 inches tall. (i) Calculate the z-score for this student's height.\n\n(ii) Interpret the z-score in context.\n\n"
          f"**C.** (i) Interpret the slope of the regression line in context.\n\n(ii) Calculate the predicted arm span for the student who is 70.3 inches tall.\n\n(iii) The arm span of this student is {obs} inches. Calculate the residual.\n\n"
          f"**D.** Interpret the coefficient of determination, $r^2$ = {r2}, in context.\n\n"
          "**E.** The teacher says, \"If we had measured the heights and the arm spans in centimeters instead of inches, the value of $r^2$ would be different.\" Is the teacher correct? Explain.",
          [(1, "A: Assigns each of the 600 students a different number from 1 to 600 (a label, for example from an alphabetical list)."),
           (1, "A: Uses a random number generator (or a random number table) to select 30 different numbers from 1 to 600, ignoring repeats; the students with those numbers are the sample."),
           (1, f"B(i): Calculates the z-score = (70.3 - {mean_h}) / {sd_h} = {z:.2f}."),
           (1, f"B(ii): Interprets the z-score in context: this student's height is about {z:.2f} standard deviations above the mean height of the students in the sample."),
           (1, f"C(i): Interprets the slope in context: for each additional inch of height, the predicted arm span increases by about {Bs:.3f} inches."),
           (1, f"C(ii): Calculates the predicted arm span: {A} {signed(Bs, 3)}(70.3) = {pred:.2f} inches."),
           (1, f"C(iii): Calculates the residual = observed - predicted = {obs} - {pred:.2f} = {res:.2f} inches."),
           (1, f"D: Interprets $r^2$ in context: about {r2 * 100:.1f}% of the variation in arm span is explained by the linear relationship with height."),
           (1, "E: States that the teacher is not correct ($r^2$ would not change)."),
           (1, "E: Explains that the correlation coefficient r (and so $r^2$) has no units and is not changed by a change of units.")],
          f"A. Make a list of the 600 students and number them 1 to 600. Use a random number generator to pick 30 different integers from 1 to 600 (if a number repeats, ignore it and generate another). The students with those numbers are in the sample.\n\n"
          f"B. (i) z = (70.3 - {mean_h}) / {sd_h} = {z:.2f}. (ii) This student's height is about {z:.2f} standard deviations above the mean height of the sample.\n\n"
          f"C. (i) For each additional inch of height, the predicted arm span increases by about {Bs:.3f} inches. (ii) {YH} = {A} {signed(Bs, 3)}(70.3) = {pred:.2f} inches. (iii) The residual is {obs} - {pred:.2f} = {res:.2f} inches.\n\n"
          f"D. About {r2 * 100:.1f}% of the variation in arm span is explained by the linear relationship with height.\n\n"
          f"E. The teacher is not correct. The correlation coefficient r has no units, so changing from inches to centimeters does not change r, and so it does not change $r^2$.",
          diagram=scatter(list(zip(xs, ys)), "Height (inches)", "Arm span (inches)", line=(m.a, m.b), alt="Scatterplot of arm span against height for 30 students with the regression line: a strong positive linear pattern."))

    # ------------------------------------------------------------------------------------------------------ 6. exit velocity and distance (normal, regression, residual plot)
    xs, ys = gen(22, 72.0, 108.0, -118.0, 5.3, 14, 6, 0, 0)
    xs = [int(v) for v in xs]
    ys = [int(v) for v in ys]
    m = lsrl(xs, ys)
    resid = [y - (m.a + m.b * x) for x, y in zip(xs, ys)]
    quad = np.polyfit(xs, resid, 2)[0]
    A, Bs = round(m.a, 1), round(m.b, 2)
    mu, sigma = 88.5, 5.4
    zz = (95 - mu) / sigma
    prob = 1 - sps.norm.cdf(round(zz, 2))
    table_prob = 1 - 0.8856  # Table A: P(Z < 1.20) = .8849 ; checked below
    assert abs(quad) < 0.1 and max(abs(r_) for r_ in resid) < 30, (quad, max(resid), min(resid))
    obs95, pred95 = 350, A + Bs * 95
    res95 = obs95 - pred95
    pred130 = A + Bs * 130
    B.frq(3, "MULTI_FOCUS",
          f"A baseball analyst studied the exit velocity (the speed of the ball just after it is hit), in miles per hour (mph), and the distance traveled, in feet, of 22 batted balls. The exit velocities of the batted balls for the whole season are approximately normally distributed with a mean of {mu} mph and a standard deviation of {sigma} mph. The data for the 22 batted balls are between 72 mph and 108 mph. A linear regression model was used to predict distance from exit velocity, and the residual plot for the model is shown.\n\n"
          f"The least-squares regression line is {YH} = {A} {signed(Bs)}x, where x is the exit velocity in mph and {YH} is the predicted distance in feet.\n\n"
          f"{INSTR}\n\n"
          "**A.** (i) Calculate the z-score for a batted ball with an exit velocity of 95 mph.\n\n(ii) Use the standard normal table to find the probability that a randomly selected batted ball has an exit velocity greater than 95 mph.\n\n"
          "**B.** (i) Interpret the slope of the regression line in context.\n\n(ii) Use the regression line to calculate the predicted distance for a batted ball with an exit velocity of 95 mph.\n\n"
          f"**C.** A batted ball with an exit velocity of 95 mph traveled {obs95} feet. Calculate the residual for this batted ball, and interpret the residual in context.\n\n"
          "**D.** Based on the residual plot, is a linear model appropriate for the data? Justify your answer.\n\n"
          "**E.** The analyst uses the regression line to predict the distance of a ball with an exit velocity of 130 mph. Explain why this prediction should not be trusted.",
          [(1, f"A(i): Calculates the z-score = (95 - {mu}) / {sigma} = {zz:.2f}."),
           (1, f"A(ii): Uses the table to find the probability: P(Z > {zz:.2f}) = 1 - {sps.norm.cdf(round(zz, 2)):.4f} = {prob:.4f} (about {prob:.3f})."),
           (1, f"B(i): Interprets the slope in context: for each additional mph of exit velocity, the predicted distance increases by about {Bs} feet."),
           (1, f"B(ii): Calculates the predicted distance: {A} {signed(Bs)}(95) = {pred95:.1f} feet."),
           (1, f"C: Calculates the residual = observed - predicted = {obs95} - {pred95:.1f} = {res95:.1f} feet."),
           (1, f"C: Interprets the residual in context: this ball traveled about {abs(res95):.1f} feet {'farther' if res95 > 0 else 'less far'} than the model predicted for an exit velocity of 95 mph."),
           (1, "D: States that a linear model is appropriate."),
           (1, "D: Justifies using the residual plot: the residuals are scattered randomly above and below zero, with no pattern or curvature."),
           (1, "E: Identifies that 130 mph is outside the interval of exit velocities in the data (72 to 108 mph), so the prediction is an extrapolation."),
           (1, f"E: Explains that an extrapolation is not reliable because the linear pattern may not continue beyond the data (the line predicts {pred130:.0f} feet, which is not realistic).")],
          f"A. (i) z = (95 - {mu}) / {sigma} = {zz:.2f}. (ii) From the table, P(Z < {zz:.2f}) = {sps.norm.cdf(round(zz, 2)):.4f}, so P(Z > {zz:.2f}) = 1 - {sps.norm.cdf(round(zz, 2)):.4f} = {prob:.4f}.\n\n"
          f"B. (i) For each additional mph of exit velocity, the predicted distance increases by about {Bs} feet. (ii) {YH} = {A} {signed(Bs)}(95) = {pred95:.1f} feet.\n\n"
          f"C. The residual is {obs95} - {pred95:.1f} = {res95:.1f} feet. The ball traveled about {abs(res95):.1f} feet {'farther' if res95 > 0 else 'less far'} than the model predicted.\n\n"
          f"D. Yes, a linear model is appropriate. The residuals in the residual plot are scattered at random above and below zero, with no pattern or curve.\n\n"
          f"E. An exit velocity of 130 mph is far outside the 72 to 108 mph in the data, so the prediction is an extrapolation. We do not know that the linear pattern continues that far, and the line predicts {pred130:.0f} feet, which is not realistic.",
          diagram=scatter(list(zip(xs, resid)), "Exit velocity (mph)", "Residual (feet)", zero_line=True, alt="Residual plot: residuals against exit velocity, scattered at random above and below zero."))
