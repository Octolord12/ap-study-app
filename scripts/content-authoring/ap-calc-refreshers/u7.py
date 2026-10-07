import sympy as sp
from common import write

x, t, C, k = sp.symbols("x t C k")
y = sp.Function("y")

# --- checks -----------------------------------------------------------------------------------
assert sp.simplify(sp.diff(C * sp.exp(3 * x), x) - 3 * C * sp.exp(3 * x)) == 0
assert sp.simplify(sp.diff(x**2 / 2 + C, x) - x) == 0

slope = lambda a, b: a - b  # dy/dx = x - y
assert [slope(0, 0), slope(1, 0), slope(0, 1), slope(2, 2)] == [0, 1, -1, 0]

sol = sp.dsolve(sp.Eq(y(x).diff(x), 2 * x * y(x)), y(x), ics={y(0): 3})
assert sp.simplify(sol.rhs - 3 * sp.exp(x**2)) == 0

kk = sp.log(2) / 3
assert sp.simplify(500 * sp.exp(kk * 9) - 4000) == 0 and sp.simplify(500 * sp.exp(kk * 3) - 1000) == 0

T, Ta, T0 = sp.symbols("T Ta T0")
Tsol = Ta + (T0 - Ta) * sp.exp(-k * t)
assert sp.simplify(sp.diff(Tsol, t) - (-k * (Tsol - Ta))) == 0 and Tsol.subs(t, 0) == T0
# ----------------------------------------------------------------------------------------------

write(7, [
("modeling-with-differential-equations", r"""
### The idea
A differential equation is an equation that involves a function and its derivatives. It describes how something changes, and its solutions are the functions that behave that way.

### Key facts
- Statements about rates translate directly. "The rate of change of $y$ is proportional to $y$" becomes $\dfrac{dy}{dx} = ky$. "The rate is proportional to the difference between $T$ and room temperature $T_a$" becomes $\dfrac{dT}{dt} = -k(T - T_a)$.
- A **solution** is a function that makes the equation true when substituted in. To check one, differentiate it and substitute.
- A **general solution** has an arbitrary constant and describes a whole family. A **particular solution** uses an **initial condition** to fix the constant.
- Always say what the variables mean, and keep the units.

### Watch out for
Forgetting to check the derivative as well as the function. A function can look right but only satisfies the equation if its derivative matches too.

### Worked example
Show that $y = Ce^{3x}$ solves $\dfrac{dy}{dx} = 3y$ for every constant $C$.

Differentiate: $\dfrac{dy}{dx} = 3Ce^{3x}$. The right side is $3y = 3Ce^{3x}$. They match, so it is a solution, and since $C$ is free, it is a general solution.

Likewise $y = \dfrac{x^2}{2} + C$ solves $\dfrac{dy}{dx} = x$.
"""),
("slope-fields", r"""
### The idea
A slope field is a picture of a differential equation. At many points $(x, y)$ you draw a short segment whose slope is the value of $\dfrac{dy}{dx}$ there. A solution curve is any curve that follows the segments.

### Key facts
- To build one for $\dfrac{dy}{dx} = f(x, y)$, evaluate $f$ at each point and draw a segment with that slope.
- Where $f(x, y) = 0$ the segments are **horizontal**. Where $f$ is undefined the segments are vertical or missing.
- If the equation depends only on $x$, the segments are identical along every vertical line. If it depends only on $y$, they are identical along every horizontal line.
- To sketch a solution through a point, start there and follow the segments, keeping the curve tangent to them.
- To match an equation to a slope field, test a few points: check where the slopes are zero, and where they are positive or negative.

### Watch out for
Mixing up the slope with the value of $y$. The segment's slope is $\dfrac{dy}{dx}$ at that point, not the height of the solution there.

### Worked example
For $\dfrac{dy}{dx} = x - y$, the slopes at a few points are:

- at $(0, 0)$: $0 - 0 = 0$, a horizontal segment
- at $(1, 0)$: $1 - 0 = 1$, rising at slope $1$
- at $(0, 1)$: $0 - 1 = -1$, falling at slope $-1$
- at $(2, 2)$: $2 - 2 = 0$, horizontal again

Every point on the line $y = x$ has a horizontal segment, because $x - y = 0$ there.
"""),
("separation-of-variables", r"""
### The idea
If a differential equation can be rearranged so that every $y$ (with $dy$) is on one side and every $x$ (with $dx$) on the other, you can integrate each side separately to solve it.

### Key facts
1. Rewrite $\dfrac{dy}{dx} = g(x)\,h(y)$ as $\dfrac{1}{h(y)}\,dy = g(x)\,dx$.
2. Integrate both sides, with a $+C$ on **one** side.
3. Use the initial condition to find $C$.
4. Solve for $y$ if you can, and state the answer as a function of $x$.
- It only works when the equation really can be separated into a function of $x$ times a function of $y$.

### Watch out for
Losing the $+C$, or adding it too late. Put it in as soon as you integrate, before you use the initial condition or solve for $y$. If you drop it, the answer is wrong, even if the algebra after that is perfect.

### Worked example
Solve $\dfrac{dy}{dx} = 2xy$ with $y(0) = 3$.

Separate: $\dfrac{1}{y}\,dy = 2x\,dx$. Integrate: $\ln|y| = x^2 + C$. Then $|y| = e^C e^{x^2}$, so $y = Ae^{x^2}$ for a constant $A$.

Use $y(0) = 3$: $A = 3$. The solution is $y = 3e^{x^2}$.
"""),
("exponential-growth-and-decay", r"""
### The idea
When a quantity changes at a rate proportional to its current size, it grows or decays exponentially. Populations, compound interest, radioactive decay and cooling all follow this pattern.

### Key facts
- $\dfrac{dy}{dt} = ky$ has the general solution $y = y_0 e^{kt}$, where $y_0$ is the value at $t = 0$.
- $k > 0$ is growth and $k < 0$ is decay. The size of $k$ tells you how fast.
- To find $k$, use a known data point, such as a doubling or half-life.
- **Doubling time** is $\dfrac{\ln 2}{k}$. **Half-life** is $\dfrac{\ln 2}{|k|}$.
- **Newton's Law of Cooling:** $\dfrac{dT}{dt} = -k(T - T_a)$ has solution $T = T_a + (T_0 - T_a)e^{-kt}$. The temperature moves toward the surrounding temperature $T_a$, not toward zero.

### Watch out for
Using $T = T_0 e^{-kt}$ for cooling. The decaying part is the **difference** from the surroundings, so $T$ levels off at $T_a$.

### Worked example
A population of $500$ doubles every $3$ hours. Find its size after $9$ hours.

$y = 500e^{kt}$ and doubling in $3$ hours means $e^{3k} = 2$, so $k = \dfrac{\ln 2}{3}$.

At $t = 9$: $y = 500e^{3\ln 2} = 500 \cdot 2^3 = 4000$.
"""),
])
