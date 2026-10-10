import sympy as sp
from common import write

x = sp.symbols("x", positive=True)

# --- checks -----------------------------------------------------------------------------------
assert sp.simplify(sp.apart((x**2) / (x**2 + 1), x) - (1 - 1 / (x**2 + 1))) == 0 and sp.simplify(sp.integrate(x**2 / (x**2 + 1), (x, 0, 1)) - (1 - sp.pi / 4)) == 0
assert sp.simplify(sp.diff(sp.atan((x + 1) / 2) / 2, x) - 1 / (x**2 + 2 * x + 5)) == 0
assert sp.simplify(sp.diff(x**2 / 2 * sp.log(x) - x**2 / 4, x) - x * sp.log(x)) == 0
assert sp.simplify(sp.diff(x * sp.sin(x) + sp.cos(x), x) - x * sp.cos(x)) == 0
assert sp.simplify(sp.diff(2 * sp.log(x - 1) - sp.log(x + 3), x) - (x + 7) / ((x - 1) * (x + 3))) == 0
assert sp.apart((x + 7) / ((x - 1) * (x + 3)), x) == 2 / (x - 1) - 1 / (x + 3)
assert sp.integrate(x ** sp.Rational(-3, 2), (x, 1, sp.oo)) == 2 and sp.integrate(sp.exp(-3 * x), (x, 0, sp.oo)) == sp.Rational(1, 3)
# ----------------------------------------------------------------------------------------------

write(6, [
("long-division-and-completing-the-square", r"""
### The idea
Some fractions have no antiderivative you can read off until you rewrite them. If the top is at least as high a degree as the bottom, divide first. If the bottom is a quadratic that does not factor, complete the square to reach an arctangent or a logarithm.

### Key facts
- **Long division:** when $\deg P \ge \deg Q$, write $\dfrac{P(x)}{Q(x)}$ as a polynomial plus $\dfrac{\text{remainder}}{Q(x)}$, where the remainder has lower degree than $Q$. Integrate each piece.
- **Completing the square:** $x^2 + bx + c = \left(x + \dfrac b2\right)^2 + \left(c - \dfrac{b^2}{4}\right)$.
- When the bottom becomes $u^2 + a^2$, use $\displaystyle\int \frac{du}{u^2 + a^2} = \frac1a \arctan\frac ua + C$.
- When the top is the derivative of the bottom, the integral is a logarithm: $\displaystyle\int \frac{u'}{u}\,dx = \ln|u| + C$. For a top like $2x + 3$ over $x^2 + 4x + 8$, split it as $(2x + 4) - 1$ and use both ideas.

### Watch out for
Forgetting the $\frac1a$ in the arctangent formula, and "integrating top and bottom separately." An integral of a quotient is not a quotient of integrals.

### Worked example
Find $\displaystyle\int \frac{dx}{x^2 + 2x + 5}$.

Complete the square: $x^2 + 2x + 5 = (x + 1)^2 + 4$. With $u = x + 1$ and $a = 2$:

$$\int \frac{dx}{(x+1)^2 + 4} = \frac12 \arctan\frac{x + 1}{2} + C$$

For a division example, $\dfrac{x^2}{x^2 + 1} = 1 - \dfrac{1}{x^2 + 1}$, so $\displaystyle\int_0^1 \frac{x^2}{x^2+1}\,dx = \left[x - \arctan x\right]_0^1 = 1 - \frac\pi4$.
"""),
("integration-by-parts", r"""
### The idea
Integration by parts is the product rule run backward. It trades an integral you cannot do for one you can.

### Key facts
- **Formula:** $\displaystyle\int u\,dv = uv - \int v\,du$. For a definite integral, $\displaystyle\int_a^b u\,dv = \Big[uv\Big]_a^b - \int_a^b v\,du$.
- **Choosing $u$:** pick the factor that gets simpler when you differentiate it (a polynomial, a logarithm or an inverse trigonometric function), and let $dv$ be the rest, something you can integrate (like $e^x$, $\sin x$ or $\cos x$).
- **Repeat** when the polynomial has degree 2 or more, as with $\int x^2 e^x\,dx$: each round lowers the degree by one.
- **Cycles:** for $\int e^x \sin x\,dx$, two rounds bring the original integral back. Call it $I$, get an equation like $I = \ldots - I$, and solve for $I$.
- **$dv = dx$ trick:** for $\int \ln x\,dx$ and $\int \arctan x\,dx$, take $u$ to be the function and $dv = dx$.

### Watch out for
The minus sign in the formula, and evaluating $uv$ at both limits of a definite integral.

### Worked example
Find $\displaystyle\int x\ln x\,dx$.

Let $u = \ln x$ and $dv = x\,dx$, so $du = \dfrac{dx}{x}$ and $v = \dfrac{x^2}{2}$:

$$
\begin{aligned}
\int x\ln x\,dx &= \frac{x^2}{2}\ln x - \int \frac{x}{2}\,dx \\
&= \frac{x^2}{2}\ln x - \frac{x^2}{4} + C
\end{aligned}
$$

Check by differentiating: the derivative of the right side is $x\ln x + \frac x2 - \frac x2 = x\ln x$.
"""),
("partial-fractions", r"""
### The idea
A fraction whose bottom factors into different linear factors can be split into simpler fractions, and each simple fraction integrates to a logarithm.

### Key facts
- For distinct linear factors, $\dfrac{P(x)}{(x - a)(x - b)} = \dfrac{A}{x - a} + \dfrac{B}{x - b}$, provided $\deg P < 2$. If the top has degree 2 or more, divide first.
- **Find $A$ and $B$:** clear denominators, then substitute the roots. Putting $x = a$ kills the $B$ term and leaves $A$. Putting $x = b$ leaves $B$.
- **Integrate:** $\displaystyle\int \frac{A}{x - a}\,dx = A\ln|x - a| + C$. Two logarithms with opposite signs combine into one quotient.
- A factor like $K - P$ integrates to $-\ln|K - P|$ because of the inner function. This is what happens in the logistic equation, where $\dfrac{1}{P(K - P)} = \dfrac1K\left(\dfrac1P + \dfrac{1}{K - P}\right)$.

### Watch out for
Swapping $A$ and $B$, and losing the minus sign that comes with $\frac{1}{K - P}$.

### Worked example
Find $\displaystyle\int \frac{x + 7}{(x - 1)(x + 3)}\,dx$.

Write $x + 7 = A(x + 3) + B(x - 1)$. At $x = 1$: $8 = 4A$, so $A = 2$. At $x = -3$: $4 = -4B$, so $B = -1$. Then

$$
\begin{aligned}
&\int \left(\frac{2}{x - 1} - \frac{1}{x + 3}\right)dx \\
&= 2\ln|x - 1| - \ln|x + 3| + C
\end{aligned}
$$
"""),
("improper-integrals", r"""
### The idea
An integral is improper when an endpoint is infinite or the function blows up. You define it as a limit, and the integral either settles on a number (it converges) or it does not (it diverges).

### Key facts
- **Infinite interval:** $\displaystyle\int_a^\infty f(x)\,dx = \lim_{b\to\infty}\int_a^b f(x)\,dx$.
- **$p$-integrals:** $\displaystyle\int_1^\infty \frac{dx}{x^p}$ converges exactly when $p > 1$ (to $\frac{1}{p - 1}$). $\displaystyle\int_0^1 \frac{dx}{x^p}$ converges exactly when $p < 1$. The borderline $p = 1$ diverges both ways.
- **Exponentials decay fast:** $\displaystyle\int_0^\infty e^{-kx}\,dx = \dfrac1k$ for $k > 0$.
- **Blow-up at an endpoint:** replace that endpoint by $c$ and take $c \to 0^+$ (or the matching limit).
- **Blow-up inside the interval:** split the integral at the bad point; both halves must converge.

### Watch out for
Applying the Fundamental Theorem straight across a point where the function is undefined, as in $\int_0^2 \frac{dx}{(x-1)^2}$. It gives $-2$ for a positive function, which is a sign that something is wrong. The integral diverges. Also, limits like $\lim_{b\to\infty} be^{-b} = 0$ need care.

### Worked example
Find $\displaystyle\int_1^\infty \frac{dx}{x^{3/2}}$.

$$
\begin{aligned}
\int_1^b x^{-3/2}\,dx &= \Big[-2x^{-1/2}\Big]_1^b \\
&= 2 - \frac{2}{\sqrt b} \longrightarrow 2 \quad (b \to \infty)
\end{aligned}
$$

It converges to 2, as the rule for $p = \frac32 > 1$ predicts: $\frac{1}{p-1} = 2$.
"""),
])
