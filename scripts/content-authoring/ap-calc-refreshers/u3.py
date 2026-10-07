import sympy as sp
from common import write

x = sp.symbols("x")
y = sp.Function("y")

# --- checks -----------------------------------------------------------------------------------
assert sp.simplify(sp.diff(sp.sin(x**2), x) - 2 * x * sp.cos(x**2)) == 0
assert sp.simplify(sp.diff((3 * x + 1) ** 5, x) - 15 * (3 * x + 1) ** 4) == 0
assert sp.simplify(sp.diff(sp.exp(2 * x), x) - 2 * sp.exp(2 * x)) == 0
assert sp.simplify(sp.diff(sp.cos(x**3) ** 2, x) - (-6 * x**2 * sp.cos(x**3) * sp.sin(x**3))) == 0

# x^2 + y^2 = 25  ->  dy/dx = -x/y ; at (3, 4) slope -3/4
eq = sp.Eq(x**2 + y(x) ** 2, 25)
dydx = sp.solve(sp.diff(eq.lhs - eq.rhs, x), sp.diff(y(x), x))[0]
assert sp.simplify(dydx + x / y(x)) == 0
assert (-sp.Integer(3) / 4) == sp.Rational(-3, 4)
# d/dx(x y) = y + x y'
assert sp.simplify(sp.diff(x * y(x), x) - (y(x) + x * sp.diff(y(x), x))) == 0

# inverse functions: f(x) = x^3 + x, f(1) = 2, (f^-1)'(2) = 1/f'(1) = 1/4
f = x**3 + x
assert f.subs(x, 1) == 2 and 1 / sp.diff(f, x).subs(x, 1) == sp.Rational(1, 4)
assert sp.diff(sp.atan(x), x) == 1 / (1 + x**2)
assert sp.simplify(sp.diff(sp.asin(x), x) - 1 / sp.sqrt(1 - x**2)) == 0

g = x**4 - 3 * x**2
assert sp.expand(sp.diff(g, x) - (4 * x**3 - 6 * x)) == 0 and sp.expand(sp.diff(g, x, 2) - (12 * x**2 - 6)) == 0 and sp.expand(sp.diff(g, x, 3) - 24 * x) == 0
# ----------------------------------------------------------------------------------------------

write(3, [
("chain-rule", r"""
### The idea
When one function is plugged into another, such as $\sin(x^2)$, the rate of change of the whole thing depends on two rates: how fast the outer function changes, and how fast the inner function feeds it. The chain rule multiplies them.

### Key facts
- $\dfrac{d}{dx} f(g(x)) = f'(g(x)) \cdot g'(x)$.
- In words: differentiate the outside function, leaving the inside alone, then multiply by the derivative of the inside.
- With several layers, keep working inward and multiply every factor.
- Spot a composition by asking "what is the last operation I would do to evaluate this?" That last operation is the outside function.
- Every basic derivative has a chain-rule version: $\dfrac{d}{dx} \sin(u) = \cos(u) \cdot u'$, $\dfrac{d}{dx} e^u = e^u \cdot u'$, and so on.

### Watch out for
Forgetting the inner derivative. The derivative of $\sin(x^2)$ is not $\cos(x^2)$. Also keep the inside unchanged when you differentiate the outside: it stays $x^2$ inside the cosine.

### Worked example
Differentiate $\sin(x^2)$. The outside is $\sin$ and the inside is $x^2$.

$$\frac{d}{dx} \sin(x^2) = \cos(x^2) \cdot 2x = 2x\cos(x^2)$$

Differentiate $(3x + 1)^5$: the outside is the fifth power, the inside is $3x + 1$, so the derivative is $5(3x + 1)^4 \cdot 3 = 15(3x + 1)^4$.

Two layers: $\cos^2(x^3)$ is $[\cos(x^3)]^2$, so its derivative is $2\cos(x^3) \cdot (-\sin(x^3)) \cdot 3x^2 = -6x^2 \cos(x^3)\sin(x^3)$.
"""),
("implicit-differentiation", r"""
### The idea
Some curves are not written as $y = f(x)$, for example the circle $x^2 + y^2 = 25$. Implicit differentiation finds the slope anyway by differentiating both sides with respect to $x$ and treating $y$ as an unknown function of $x$.

### Key facts
- Differentiate every term with respect to $x$. Each time you differentiate a term with $y$, the chain rule adds a factor $\dfrac{dy}{dx}$.
- So $\dfrac{d}{dx} y^2 = 2y \dfrac{dy}{dx}$, and $\dfrac{d}{dx}(xy) = y + x\dfrac{dy}{dx}$ by the product rule.
- After differentiating, collect the $\dfrac{dy}{dx}$ terms on one side and solve for it.
- The answer usually has both $x$ and $y$ in it. To get a slope at a point, substitute both coordinates.
- The tangent line at a point uses that slope in the usual point-slope form.

### Watch out for
Forgetting the factor $\dfrac{dy}{dx}$ on $y$ terms, which makes $y$ behave like a constant. Also, substitute the point only after you have solved for $\dfrac{dy}{dx}$.

### Worked example
Find the slope of $x^2 + y^2 = 25$ at the point $(3, 4)$.

Differentiate: $2x + 2y\dfrac{dy}{dx} = 0$. Solve: $\dfrac{dy}{dx} = -\dfrac{x}{y}$.

At $(3, 4)$ the slope is $-\dfrac{3}{4}$, so the tangent line is $y - 4 = -\dfrac{3}{4}(x - 3)$.
"""),
("derivatives-of-inverse-functions", r"""
### The idea
If $g$ is the inverse of $f$, their graphs are mirror images across the line $y = x$, so their slopes at matching points are reciprocals. That lets you find the derivative of an inverse without ever finding a formula for it.

### Key facts
- If $f$ has an inverse $g = f^{-1}$, then $g'(b) = \dfrac{1}{f'(g(b))}$.
- Reading it as a recipe: to find $g'(b)$, first find the $a$ with $f(a) = b$, then take $\dfrac{1}{f'(a)}$.
- This works only where $f'(a) \ne 0$.
- It is how the derivatives of inverse trig functions are found. Two to know: $\dfrac{d}{dx} \arcsin x = \dfrac{1}{\sqrt{1 - x^2}}$ and $\dfrac{d}{dx} \arctan x = \dfrac{1}{1 + x^2}$.
- The same idea gives $\dfrac{d}{dx}\ln x = \dfrac{1}{x}$, since $\ln$ is the inverse of $e^x$.

### Watch out for
Using $f'(b)$ instead of $f'(a)$. The derivative of $f$ is evaluated at the input of $f$, which is the output of the inverse. Mixing these up is the most common error.

### Worked example
Let $f(x) = x^3 + x$ and let $g$ be its inverse. Find $g'(2)$.

We need $a$ with $f(a) = 2$. Since $f(1) = 1 + 1 = 2$, we have $a = 1$. Then $f'(x) = 3x^2 + 1$, so $f'(1) = 4$, and

$$g'(2) = \frac{1}{f'(1)} = \frac{1}{4}.$$
"""),
("higher-order-derivatives", r"""
### The idea
A derivative is itself a function, so it can be differentiated again. Each new derivative describes the rate of change of the previous one.

### Key facts
- Notation for the second derivative: $f''(x)$ or $\dfrac{d^2y}{dx^2}$. For the third: $f'''(x)$. In general $f^{(n)}(x)$.
- $f'$ is the rate of change of $f$ (its slope). $f''$ is the rate of change of the slope, which describes how the curve bends. This is the idea of concavity, used later.
- In motion, if $s(t)$ is position, then $v = s'$ is velocity and $a = s'' = v'$ is acceleration.
- Differentiate one step at a time, simplifying as you go, rather than all at once.

### Watch out for
Mixing up $f''(x)$ with $\left[f'(x)\right]^2$ or $f(x)^2$. The second derivative means differentiating twice, not squaring.

### Worked example
Find the first three derivatives of $f(x) = x^4 - 3x^2$.

$$f'(x) = 4x^3 - 6x$$
$$f''(x) = 12x^2 - 6$$
$$f'''(x) = 24x$$

If this were a position function, $f'(x)$ would be the velocity and $f''(x)$ the acceleration.
"""),
])
