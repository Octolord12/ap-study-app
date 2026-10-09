import sympy as sp
from common import write

x, t = sp.symbols("x t")

# --- checks -----------------------------------------------------------------------------------
f = lambda v: sp.Rational(v) ** 2
dx = sp.Rational(1, 2)
left = sum(f(k * dx) for k in range(0, 4)) * dx
right = sum(f(k * dx) for k in range(1, 5)) * dx
assert (left, right) == (sp.Rational(7, 4), sp.Rational(15, 4)) and sp.integrate(x**2, (x, 0, 2)) == sp.Rational(8, 3)
assert left < sp.Rational(8, 3) < right

G = sp.integrate(sp.sin(t), (t, 1, x**2))
assert sp.simplify(sp.diff(G, x) - 2 * x * sp.sin(x**2)) == 0
assert sp.integrate(2 * x, (x, 1, 3)) == 8

F = sp.integrate(6 * x**2 - 4, x) + sp.symbols("C")
C = sp.solve(F.subs(x, 1) - 3, sp.symbols("C"))[0]
assert C == 5 and sp.expand(F.subs(sp.symbols("C"), 5) - (2 * x**3 - 4 * x + 5)) == 0

assert sp.integrate(2 * x * (x**2 + 1) ** 5, (x, 0, 2)) == 2604 and (5**6 - 1) // 6 == 2604
assert sp.simplify(sp.diff((x**2 + 1) ** 6 / 6, x) - 2 * x * (x**2 + 1) ** 5) == 0
# ----------------------------------------------------------------------------------------------

write(6, [
("riemann-sums-and-definite-integrals", r"""
### The idea
To find the area under a curve, slice it into thin rectangles, add up their areas, and let the slices get thinner and thinner. The definite integral is what that sum approaches.

### Key facts
- **Riemann sum:** split $[a, b]$ into $n$ pieces of width $\Delta x = \dfrac{b - a}{n}$ and add $f(x_i^*) \, \Delta x$ over the pieces. The height can come from the left end, the right end, or the midpoint of each piece. The trapezoid rule averages the left and right sums.
- **Definite integral:** $\displaystyle\int_a^b f(x)\,dx$ is the limit of those sums as $n \to \infty$.
- It measures **signed** area: area above the $x$-axis counts positive, area below counts negative.
- For an **increasing** function, a left sum underestimates and a right sum overestimates. For a decreasing function it is the other way around.
- Useful properties: $\int_a^a f = 0$, reversing the limits flips the sign, and $\int_a^c f = \int_a^b f + \int_b^c f$.

### Watch out for
Treating the integral as ordinary area when the function goes negative. It gives net area. Also, units: if $f$ is in meters per second and $x$ in seconds, the integral is in meters.

### Worked example
Estimate $\displaystyle\int_0^2 x^2\,dx$ with $4$ equal pieces, so $\Delta x = 0.5$.

Left sum: $(0 + 0.25 + 1 + 2.25)(0.5) = 1.75$. Right sum: $(0.25 + 1 + 2.25 + 4)(0.5) = 3.75$.

The function is increasing, so the true value is between them. It is $\dfrac{8}{3} \approx 2.67$.
"""),
("fundamental-theorem-of-calculus", r"""
### The idea
Differentiation and integration undo each other. The Fundamental Theorem says this in two parts: one tells you the derivative of an accumulated amount, and the other tells you how to compute a definite integral from an antiderivative.

### Key facts
- **Part 1:** if $G(x) = \displaystyle\int_a^x f(t)\,dt$ and $f$ is continuous, then $G'(x) = f(x)$.
- **With the chain rule:** $\dfrac{d}{dx}\displaystyle\int_a^{g(x)} f(t)\,dt = f(g(x)) \cdot g'(x)$.
- **Part 2:** if $F' = f$, then $\displaystyle\int_a^b f(x)\,dx = F(b) - F(a)$.
- An accumulation function $G$ increases where $f > 0$ and decreases where $f < 0$. Its graph is concave up where $f$ is increasing.
- $\displaystyle\int_a^b f'(x)\,dx = f(b) - f(a)$: the total change is the integral of the rate of change.

### Watch out for
Putting the variable in two places. The inside variable $t$ is only a dummy, and the answer to a Part 1 question depends on $x$ only through the upper limit. Also, with a function of $x$ as the upper limit, do not forget to multiply by its derivative.

### Worked example
Find $\dfrac{d}{dx}\displaystyle\int_1^{x^2} \sin t\,dt$. By Part 1 with the chain rule, substitute the upper limit into $\sin t$ and multiply by its derivative:

$$\sin(x^2) \cdot 2x = 2x\sin(x^2).$$

Part 2: $\displaystyle\int_1^3 2x\,dx = \big[x^2\big]_1^3 = 9 - 1 = 8$.
"""),
("antiderivatives-and-indefinite-integrals", r"""
### The idea
An antiderivative of $f$ is a function whose derivative is $f$. Because constants disappear when you differentiate, every function has a whole family of antiderivatives that differ by a constant, and the indefinite integral stands for all of them.

### Key facts
- $\displaystyle\int f(x)\,dx = F(x) + C$ where $F' = f$. The $+C$ is part of the answer.
- $\displaystyle\int x^n\,dx = \dfrac{x^{n+1}}{n+1} + C$ for $n \ne -1$, and $\displaystyle\int \dfrac{1}{x}\,dx = \ln|x| + C$.
- $\displaystyle\int e^x\,dx = e^x + C$, $\displaystyle\int \sin x\,dx = -\cos x + C$, $\displaystyle\int \cos x\,dx = \sin x + C$, $\displaystyle\int \sec^2 x\,dx = \tan x + C$.
- $\displaystyle\int \dfrac{1}{1 + x^2}\,dx = \arctan x + C$.
- Constants come out, and sums split: integrate term by term.
- An **initial condition** such as $f(1) = 3$ pins down the value of $C$.
- You can always check an antiderivative by differentiating it.

### Watch out for
Leaving off $+C$, and the sign of $\int \sin x\,dx$, which is $-\cos x$. Also, the power rule backwards divides by the new exponent, so it fails for $n = -1$.

### Worked example
Find $f$ if $f'(x) = 6x^2 - 4$ and $f(1) = 3$.

$$f(x) = \int (6x^2 - 4)\,dx = 2x^3 - 4x + C.$$

Use $f(1) = 3$: $2 - 4 + C = 3$, so $C = 5$. Therefore $f(x) = 2x^3 - 4x + 5$.
"""),
("u-substitution", r"""
### The idea
$u$-substitution undoes the chain rule. When an integral contains a function and (a constant multiple of) its inner derivative, replacing the inner part with a new variable $u$ turns the integral into a simple one.

### Key facts
1. Choose $u$ to be an inner function whose derivative also appears in the integrand (up to a constant factor).
2. Compute $du = u'\,dx$ and rewrite the **whole** integral in terms of $u$. No $x$ may remain.
3. Integrate with respect to $u$.
4. Substitute back to $x$ for an indefinite integral.
5. For a **definite** integral, either change the limits to $u$-values, or go back to $x$ and keep the original limits. Do not mix them.

### Watch out for
Changing the integrand to $u$ but keeping the $x$ limits. If you convert to $u$, the limits must be the $u$-values too. Also, a missing constant factor is fine (divide by it), but a missing variable factor means this $u$ will not work.

### Worked example
Evaluate $\displaystyle\int_0^2 2x(x^2 + 1)^5\,dx$.

Let $u = x^2 + 1$, so $du = 2x\,dx$. The limits change: when $x = 0$, $u = 1$, and when $x = 2$, $u = 5$.

$$
\begin{aligned}
\int_1^5 u^5\,du &= \left[\frac{u^6}{6}\right]_1^5 \\
&= \frac{5^6 - 1}{6} = \frac{15624}{6} = 2604
\end{aligned}
$$
"""),
])
