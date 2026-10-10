import sympy as sp
from common import write

x = sp.symbols("x", positive=True)
R = sp.Rational

# --- checks -----------------------------------------------------------------------------------
y = x**2 / 4 - sp.log(x) / 2
yp = sp.diff(y, x)
assert sp.simplify(1 + yp**2 - (x / 2 + 1 / (2 * x)) ** 2) == 0
L = sp.integrate(x / 2 + 1 / (2 * x), (x, 1, sp.E))
assert sp.simplify(L - (sp.E**2 + 1) / 4) == 0
v = x**2 - 4
assert sp.integrate(4 - x**2, (x, 0, 2)) + sp.integrate(x**2 - 4, (x, 2, 3)) == R(23, 3)
# ----------------------------------------------------------------------------------------------

write(8, [
("arc-length-and-distance-traveled", r"""
### The idea
The length of a curve comes from the Pythagorean theorem applied to a tiny piece: a run of $dx$ and a rise of $dy$ make a hypotenuse of $\sqrt{dx^2 + dy^2}$. Adding up the pieces gives an integral.

### Key facts
- **Arc length of $y = f(x)$ on $[a, b]$:** $\displaystyle L = \int_a^b \sqrt{1 + \left(\frac{dy}{dx}\right)^2}\,dx$.
- The integrand needs the **derivative**, squared and added to 1, all under a square root.
- Problems built for hand work are designed so that $1 + \left(\frac{dy}{dx}\right)^2$ is a perfect square and the root disappears. Others call for a calculator: write the integral, then give the value.
- **Distance traveled along a line** with velocity $v(t)$ is $\displaystyle\int_a^b |v(t)|\,dt$. It differs from the displacement $\int_a^b v(t)\,dt$ whenever $v$ changes sign.
- The length of a curve is always at least the straight-line distance between its endpoints.

### Watch out for
Putting $y$ instead of $y'$ in the formula, leaving out the square root, or forgetting the 1.

### Worked example
Find the length of $y = \dfrac{x^2}{4} - \dfrac{\ln x}{2}$ from $x = 1$ to $x = e$.

$\dfrac{dy}{dx} = \dfrac x2 - \dfrac{1}{2x}$, and

$$1 + \left(\frac{dy}{dx}\right)^2 = \left(\frac x2 + \frac{1}{2x}\right)^2$$

so the root disappears and

$$
\begin{aligned}
L &= \int_1^e \left(\frac x2 + \frac{1}{2x}\right)dx \\
&= \left[\frac{x^2}{4} + \frac{\ln x}{2}\right]_1^e \\
&= \left(\frac{e^2}{4} + \frac12\right) - \frac14 = \frac{e^2 + 1}{4}
\end{aligned}
$$
"""),
])
