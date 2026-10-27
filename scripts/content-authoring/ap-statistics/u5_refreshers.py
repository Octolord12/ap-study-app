"""Writes content/ap-statistics/refreshers/unit-5.json (five refreshers, one per topic). Layout: ### The idea, ### Key facts, ### Watch out for, ### Worked example.
Facts are the CED's essential knowledge for each topic (effective Fall 2026); every number in a worked example is asserted. Avoid a lone dollar sign, single-asterisk
italics and em dashes. Edit this script, not the JSON. Run: python3 u5_refreshers.py"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import refreshers_lib
import numpy as np

# 5.1 example: hours studied and quiz score
hrs, sc = [1, 2, 3, 4, 5, 6], [52, 60, 64, 75, 80, 88]
assert np.corrcoef(hrs, sc)[0, 1] > 0.98

# 5.2 example
xs, ys = [1, 2, 3, 4, 5], [9, 7, 6, 3, 2]
r = np.corrcoef(xs, ys)[0, 1]
assert round(r, 2) == -0.99

# 5.3 example
a, b = 3.2, 1.45
assert round(a + b * 12, 2) == 20.6

# 5.4 example
a4, b4 = 41, 6.5
assert a4 + b4 * 3 == 60.5 and 68 - 60.5 == 7.5

# 5.5 example
a5, b5, r2 = 78.4, -2.15, 0.543
assert round(a5 + b5 * 4, 1) == 69.8
assert round(-math.sqrt(r2), 3) == -0.737

ENTRIES = [
("graphical-representations-between-two-quantitative-variables", r"""
### The idea
A scatterplot shows the relationship between two quantitative variables measured on the same individuals. Each point is one individual: its position across is the value of one variable and its height is the value of the other.

### Key facts
- The **explanatory variable** is the one used to explain or predict, and it goes on the **horizontal** axis. The **response variable** goes on the **vertical** axis.
- Describe the association with four things: **form** (linear or non-linear), **direction** (positive or negative), **strength** (strong, moderate or weak) and **unusual features** (clusters, or points that do not fit the general pattern).
- In a **positive** association, the response tends to increase as the explanatory variable increases. In a **negative** association, it tends to decrease.
- **Strength** is how closely the points follow the general pattern.
- A scatterplot can support claims about the variables, always written in context.

### Watch out for
Strength is not steepness: a steep pattern with widely scattered points is not a strong association. Also say "tends to": an association describes a pattern, not what every individual does.

### Worked example
Prompt: "Six students recorded hours studied and quiz score: (1, 52), (2, 60), (3, 64), (4, 75), (5, 80), (6, 88). Describe the association."

The points rise from left to right along a straight pattern, with very little scatter. In context: there is a strong, positive, linear association between hours studied and quiz score; students who studied more hours tended to score higher. There are no clusters and no points that do not fit the pattern.
"""),
("correlation", r"""
### The idea
The correlation coefficient, $r$, is one number that summarizes the **direction and strength of a linear association** between two quantitative variables. Technology calculates it.

### Key facts
- $r$ is always between $-1$ and $1$, inclusive, and it has **no units**, so changing the units of measurement does not change it.
- The sign of $r$ is the direction of the association. The closer $r$ is to $-1$ or $1$, the stronger the linear association.
- $r = 0$ means no linear association. $r = 1$ or $r = -1$ means a perfect linear association: all the points lie on a line.
- An $r$ close to $-1$ or $1$ does not mean a linear model is appropriate. Look at the scatterplot.
- **Correlation does not imply causation.** A real relationship between two variables does not mean that changes in one cause changes in the other.

### Watch out for
$r$ is not the slope, not the percent of points on a line, and not the percent of variation explained (that is $r^2$). And $r$ near 0 means no *linear* association, but there can still be a strong curved pattern.

### Worked example
Prompt: "For the points (1, 9), (2, 7), (3, 6), (4, 3), (5, 2), technology gives $r = -0.99$. Interpret $r$."

The value is negative and very close to $-1$. There is a strong, negative, linear association: as $x$ increases, $y$ tends to decrease, and the points are very close to a line.
"""),
("linear-regression-models", r"""
### The idea
If the form of a relationship looks linear, a **linear regression model** uses the explanatory variable $x$ to predict the response variable $y$.

### Key facts
- The predicted response is $\hat{y} = a + bx$, where $a$ is the **y-intercept** and $b$ is the **slope**. The symbol $\hat{y}$ ("y-hat") is a *predicted* value, not an observed one.
- **Interpolation** is predicting for an $x$ inside the interval of $x$-values used to find the line.
- **Extrapolation** is predicting for an $x$ outside that interval. The prediction is less reliable the farther out it is.
- Only fit a linear model when the data show a linear trend.

### Watch out for
Plugging into the equation is easy to get wrong in order: multiply the slope by $x$, then add the intercept. And a prediction can be impossible (a percentage over 100, a negative price) when you extrapolate. That is a sign to distrust it.

### Worked example
Prompt: "A line for predicting a plant's height in centimeters from the days since planting is $\hat{y} = 3.2 + 1.45x$, found from plants that were 1 to 20 days old. Predict the height at 12 days and at 40 days."

At 12 days: $\hat{y} = 3.2 + 1.45(12) = 20.6$ cm. This is interpolation, because 12 is between 1 and 20. At 40 days the model gives $3.2 + 1.45(40) = 61.2$ cm, but 40 is outside 1 to 20, so it is an extrapolation and should not be trusted.
"""),
("residuals", r"""
### The idea
A **residual** measures how far an observation is from the model's prediction: $\text{residual} = y - \hat{y}$, that is, observed minus predicted.

### Key facts
- **Positive** residual: the observed value is above the predicted value, so the model **underpredicts**.
- **Negative** residual: the observed value is below the predicted value, so the model **overpredicts**.
- A **residual plot** is a scatterplot of the residuals against the predicted values (or against the explanatory variable).
- **No pattern** (apparent randomness) in a residual plot supports a linear form: the linear model is appropriate.
- **Curvature** in a residual plot suggests that the linear model is not the most appropriate model.

### Watch out for
Subtract in the right order: observed minus predicted. The sign is the whole message, so say "underpredicts" or "overpredicts" in context. And a residual plot should be judged by its *pattern*, not by whether it has both positive and negative values.

### Worked example
Prompt: "The line $\hat{y} = 41 + 6.5x$ predicts a quiz score from hours studied. A student who studied 3 hours scored 68. Find and interpret the residual."

Predicted: $41 + 6.5(3) = 60.5$. Residual: $68 - 60.5 = 7.5$. The student scored 7.5 points higher than the model predicted, so the model underpredicts for this student.
"""),
("least-squares-regression", r"""
### The idea
The **least-squares regression line** is the line that makes the sum of the squares of the residuals as small as possible. Technology finds its slope $b$, its y-intercept $a$ and the correlation $r$.

### Key facts
- The line always passes through the point $(\bar{x}, \bar{y})$.
- **Slope:** the *predicted* change in the response for a one-unit increase in the explanatory variable, in context.
- **Y-intercept:** the *predicted* response when the explanatory variable is 0, in context. Sometimes it has no reasonable interpretation: $x = 0$ may be outside the data (extrapolation), or the value may be impossible, such as a negative height.
- $r^2$, the **coefficient of determination**, is the proportion of the variation in the response that is explained by the linear relationship with the explanatory variable.
- The slope and $r$ always have the same sign.

### Watch out for
Always say "predicted" when interpreting the slope and intercept, name the units, and use the context. And $r^2$ is a proportion of *variation*, not a percent of points on the line. To get $r$ from $r^2$, take the square root and give it the sign of the slope.

### Worked example
Prompt: "Output for predicting resting heart rate (beats per minute) from hours of exercise per week: Constant 78.4, Hours $-2.15$, R-sq = 54.3%. Interpret each part."

Slope: for each additional hour of exercise per week, the predicted resting heart rate decreases by about 2.15 beats per minute. Intercept: the predicted resting heart rate with no exercise is 78.4 beats per minute. $r^2 = 0.543$: about 54.3% of the variation in resting heart rate is explained by the linear relationship with hours of exercise. The slope is negative, so $r = -\sqrt{0.543} = -0.737$. At 4 hours the prediction is $78.4 - 2.15(4) = 69.8$.
"""),
]

if __name__ == "__main__":
    refreshers_lib.write("ap-statistics", 5, ENTRIES)
