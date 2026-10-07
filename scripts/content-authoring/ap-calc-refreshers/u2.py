import sympy as sp
from common import write

x, t, h = sp.symbols("x t h")

# --- checks -----------------------------------------------------------------------------------
s = t**3
assert (s.subs(t, 3) - s.subs(t, 1)) / 2 == 13 and sp.diff(s, t).subs(t, 2) == 12

assert sp.limit(((3 + h) ** 2 - 9) / h, h, 0) == 6
assert sp.limit((abs(h) - 0) / h, h, 0, "+") == 1 and sp.limit((abs(h) - 0) / h, h, 0, "-") == -1

f3 = 4 * x**3 - 2 / x**2 + sp.sqrt(x)
assert sp.simplify(sp.diff(f3, x) - (12 * x**2 + 4 * x**-3 + 1 / (2 * sp.sqrt(x)))) == 0

f4 = 3 * sp.exp(x) - 2 * sp.sin(x) + sp.log(x)
assert sp.simplify(sp.diff(f4, x) - (3 * sp.exp(x) - 2 * sp.cos(x) + 1 / x)) == 0
assert sp.diff(5**x, x) == 5**x * sp.log(5)

assert sp.simplify(sp.diff(x**2 * sp.sin(x), x) - (2 * x * sp.sin(x) + x**2 * sp.cos(x))) == 0
assert sp.simplify(sp.diff(x / (x + 1), x) - 1 / (x + 1) ** 2) == 0
# ----------------------------------------------------------------------------------------------

write(2, [
("average-vs-instantaneous-rate-of-change", r"""
### The idea
The average rate of change of $f$ over $[a, b]$ tells you how fast the output changed per unit of input across a whole interval. The instantaneous rate of change tells you how fast it is changing at a single input. The second is what the derivative measures, and it is the limit of the first as the interval shrinks.

### Key facts
- **Average rate of change** on $[a, b]$ is $\dfrac{f(b) - f(a)}{b - a}$. Geometrically it is the slope of the secant line through $(a, f(a))$ and $(b, f(b))$.
- **Instantaneous rate of change** at $x = a$ is $\lim_{h \to 0} \dfrac{f(a + h) - f(a)}{h}$. Geometrically it is the slope of the tangent line at that point.
- The units are always output units per input unit, such as meters per second or dollars per item.
- To get from average to instantaneous, make the second point slide toward the first. That sliding is the limit.

### Watch out for
Treating a very short average rate as the instantaneous rate. It is only an estimate. The instantaneous rate needs the limit, because a single point has no width to average over.

### Worked example
A particle's position is $s(t) = t^3$ meters at time $t$ seconds.

Average velocity on $[1, 3]$: $\dfrac{s(3) - s(1)}{3 - 1} = \dfrac{27 - 1}{2} = 13$ m/s.

Instantaneous velocity at $t = 2$: $s'(t) = 3t^2$, so $s'(2) = 12$ m/s.

They are different numbers because the particle speeds up over the interval, so its speed at the middle moment is not the interval's average.
"""),
("derivative-definition-and-differentiability", r"""
### The idea
The derivative of $f$ at $x = a$ is the slope of the tangent line there, defined as a limit of secant slopes. A function is differentiable at a point when that limit exists.

### Key facts
- $f'(a) = \lim_{h \to 0} \dfrac{f(a + h) - f(a)}{h}$, or equivalently $f'(a) = \lim_{x \to a} \dfrac{f(x) - f(a)}{x - a}$.
- **Differentiable implies continuous.** If a derivative exists at a point, the function is continuous there.
- The converse is false. A function can be continuous at a point and still fail to have a derivative there.
- A function fails to be differentiable where its graph has a **corner**, a **cusp**, a **vertical tangent**, or a **discontinuity**.
- At a corner the left-hand and right-hand slopes both exist but disagree, so the limit does not exist.

### Watch out for
Concluding that "continuous" means "smooth". The graph of $f(x) = |x|$ has no breaks, yet it has no derivative at $x = 0$.

### Worked example
Use the definition to find $f'(3)$ for $f(x) = x^2$.

$$\frac{f(3 + h) - f(3)}{h} = \frac{(3 + h)^2 - 9}{h} = \frac{6h + h^2}{h} = 6 + h$$

As $h \to 0$ this approaches $6$, so $f'(3) = 6$.

For $f(x) = |x|$ at $x = 0$, the quotient is $\dfrac{|h|}{h}$, which is $1$ for $h > 0$ and $-1$ for $h < 0$. The two sides disagree, so $f'(0)$ does not exist.
"""),
("power-rule-and-basic-derivatives", r"""
### The idea
Most derivatives you will take are built from a few basic rules. The power rule handles any term of the form $x^n$, and the constant-multiple and sum rules let you take it term by term.

### Key facts
- **Power rule:** $\dfrac{d}{dx} x^n = n x^{n-1}$, for any real number $n$.
- **Constant:** $\dfrac{d}{dx} c = 0$.
- **Constant multiple:** $\dfrac{d}{dx}\big[c f(x)\big] = c f'(x)$.
- **Sum and difference:** differentiate each term separately.
- Rewrite roots and reciprocals as powers before differentiating: $\sqrt{x} = x^{1/2}$ and $\dfrac{1}{x^3} = x^{-3}$.

### Watch out for
Applying the power rule to a variable in the exponent. $x^3$ is a power function, but $3^x$ is not, and the power rule does not apply to it. Also remember the derivative of a constant is $0$, not the constant.

### Worked example
Differentiate $f(x) = 4x^3 - \dfrac{2}{x^2} + \sqrt{x}$.

First rewrite: $f(x) = 4x^3 - 2x^{-2} + x^{1/2}$. Then differentiate term by term:

$$f'(x) = 12x^2 + 4x^{-3} + \tfrac{1}{2}x^{-1/2} = 12x^2 + \frac{4}{x^3} + \frac{1}{2\sqrt{x}}$$
"""),
("derivatives-of-trig-exponential-log", r"""
### The idea
A short list of derivatives has to be memorized, because they cannot be built from the power rule. Once you know them, they combine with the other rules like any other function.

### Key facts
- $\dfrac{d}{dx} \sin x = \cos x$ and $\dfrac{d}{dx} \cos x = -\sin x$
- $\dfrac{d}{dx} \tan x = \sec^2 x$
- $\dfrac{d}{dx} \sec x = \sec x \tan x$
- $\dfrac{d}{dx} e^x = e^x$
- $\dfrac{d}{dx} a^x = a^x \ln a$, for a constant $a > 0$
- $\dfrac{d}{dx} \ln x = \dfrac{1}{x}$, for $x > 0$

The "co" functions pick up a minus sign: the derivative of $\cos x$, $\cot x$ and $\csc x$ is each negative.

### Watch out for
Dropping the minus sign on $\cos x$, and forgetting the factor $\ln a$ in $\dfrac{d}{dx} a^x$. The function $e^x$ is special because $\ln e = 1$, which is why it is its own derivative.

### Worked example
Differentiate $f(x) = 3e^x - 2\sin x + \ln x$.

Term by term: the derivative of $3e^x$ is $3e^x$, the derivative of $-2\sin x$ is $-2\cos x$, and the derivative of $\ln x$ is $\dfrac{1}{x}$.

$$f'(x) = 3e^x - 2\cos x + \frac{1}{x}$$

For an exponential with another base, $\dfrac{d}{dx} 5^x = 5^x \ln 5$.
"""),
("sum-difference-product-quotient-rules", r"""
### The idea
When two functions are multiplied or divided, you cannot just differentiate each piece and combine. The product and quotient rules say exactly how the pieces interact.

### Key facts
- **Sum and difference:** $(f \pm g)' = f' \pm g'$.
- **Product rule:** $(fg)' = f'g + fg'$.
- **Quotient rule:** $\left(\dfrac{f}{g}\right)' = \dfrac{f'g - fg'}{g^2}$.
- In the quotient rule the order matters: it is the derivative of the top times the bottom, minus the top times the derivative of the bottom.
- If an expression can be simplified first (for example by dividing term by term), that is often quicker than using the quotient rule.

### Watch out for
Writing $(fg)' = f'g'$. For $f = g = x$, the true derivative of $x^2$ is $2x$, but $f'g' = 1$. Another common slip is reversing the two terms in the quotient rule's numerator, which flips the sign.

### Worked example
Product: differentiate $x^2 \sin x$. With $f = x^2$ and $g = \sin x$,

$$(x^2 \sin x)' = 2x \sin x + x^2 \cos x.$$

Quotient: differentiate $\dfrac{x}{x + 1}$. With $f = x$ and $g = x + 1$,

$$\frac{1 \cdot (x + 1) - x \cdot 1}{(x + 1)^2} = \frac{1}{(x + 1)^2}.$$
"""),
])
