import sympy as sp
from common import write

x, t = sp.symbols("x t")
R = sp.Rational

# --- checks -----------------------------------------------------------------------------------
# Euler: dy/dx = x + y, y(0) = 1, step 0.5, estimate y(1)
pts = [(R(0), R(1))]
for _ in range(2):
    xx, yy = pts[-1]
    pts.append((xx + R(1, 2), yy + R(1, 2) * (xx + yy)))
assert pts == [(0, 1), (R(1, 2), R(3, 2)), (1, R(5, 2))]
y = sp.Function("y")
sol = sp.dsolve(sp.Eq(y(x).diff(x), x + y(x)), y(x), ics={y(0): 1}).rhs
assert sp.simplify(sol - (2 * sp.exp(x) - x - 1)) == 0 and sol.subs(x, 1) == 2 * sp.E - 2 and float(sol.subs(x, 1)) > 2.5
assert sp.simplify(sp.diff(sol, x, 2) - (1 + sp.diff(sol, x))) == 0  # y'' = 1 + y' > 0 for x >= 0

# logistic: dP/dt = 0.2 P (1 - P/500), P(0) = 100
P = 500 / (1 + 4 * sp.exp(-R(1, 5) * t))
assert sp.simplify(sp.diff(P, t) - R(1, 5) * P * (1 - P / 500)) == 0 and P.subs(t, 0) == 100
assert R(1, 5) * 250 * (1 - R(250, 500)) == 25
# ----------------------------------------------------------------------------------------------

write(7, [
("eulers-method", r"""
### The idea
When a differential equation cannot be solved exactly, you can still walk along the solution one small step at a time, following the tangent line at each stop. That is Euler's method.

### Key facts
- **The rule:** from a point $(x_n, y_n)$, with step size $\Delta x$, move to
  $$x_{n+1} = x_n + \Delta x, \qquad y_{n+1} = y_n + \Delta x\cdot\frac{dy}{dx}\Big|_{(x_n,\,y_n)}$$
- The slope always comes from the point you are **leaving**, using both coordinates in the formula for $\frac{dy}{dx}$.
- A table with columns $x$, $y$, $\frac{dy}{dx}$ keeps the steps straight.
- Smaller steps usually give better estimates. Each step is one line segment, so errors can add up.
- **Over or under?** If the solution is concave up, tangent lines lie below it and Euler underestimates. If it is concave down, Euler overestimates. Get concavity from $\frac{d^2y}{dx^2}$, computed from the differential equation.

### Watch out for
Using the wrong number of steps (from $x = 0$ to $x = 1$ with $\Delta x = 0.5$ takes two), and forgetting to multiply the slope by $\Delta x$.

### Worked example
For $\dfrac{dy}{dx} = x + y$ with $y(0) = 1$, use two steps of size $0.5$ to estimate $y(1)$.

At $(0, 1)$ the slope is $1$, so $y(0.5) \approx 1 + 0.5(1) = 1.5$. At $(0.5, 1.5)$ the slope is $2$, so $y(1) \approx 1.5 + 0.5(2) = 2.5$.

Since $y'' = 1 + y' > 0$ for $x \ge 0$, the solution is concave up and $2.5$ is an underestimate. (The exact solution is $y = 2e^x - x - 1$, so $y(1) = 2e - 2 \approx 3.44$.)
"""),
("logistic-models", r"""
### The idea
Populations do not grow forever. A logistic model grows almost exponentially at first, then slows as it approaches a limit set by the environment, the carrying capacity.

### Key facts
- **The equation:** $\dfrac{dP}{dt} = kP\left(1 - \dfrac PK\right)$, where $K$ is the carrying capacity. The form $kP(K - P)$ is the same model with a different constant.
- **Equilibria:** $P = 0$ (unstable) and $P = K$ (stable). For $0 < P < K$ the population increases toward $K$. If $P > K$ it decreases toward $K$.
- **Fastest growth** is at $P = \dfrac K2$, the vertex of the parabola $\frac{dP}{dt}$ as a function of $P$. That is where the graph of $P(t)$ has its inflection point.
- **Concavity:** concave up for $0 < P < \frac K2$ and concave down for $\frac K2 < P < K$. A solution above $K$ decreases and is concave up.
- **Solution:** $P(t) = \dfrac{K}{1 + Ae^{-kt}}$ with $A = \dfrac{K - P(0)}{P(0)}$.

### Watch out for
Reading $K$ as the constant out front in $kP(K - P)$, and forgetting that a starting value above $K$ gives a decreasing solution.

### Worked example
A population satisfies $\dfrac{dP}{dt} = 0.2P\left(1 - \dfrac{P}{500}\right)$ with $P(0) = 100$.

The carrying capacity is $K = 500$, so $\lim_{t\to\infty} P = 500$. Growth is fastest at $P = 250$, where $\dfrac{dP}{dt} = 0.2(250)(0.5) = 25$. With $A = \dfrac{500 - 100}{100} = 4$,

$$P(t) = \frac{500}{1 + 4e^{-0.2t}}$$
"""),
])
