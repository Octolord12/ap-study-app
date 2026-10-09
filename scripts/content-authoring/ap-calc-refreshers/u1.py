import sympy as sp
from common import write

x = sp.symbols("x")

# --- checks for the worked examples -----------------------------------------------------------
f = lambda t: (t**2 - 4) / (t - 2)
assert [round(f(v), 6) for v in (1.9, 1.99, 1.999)] == [3.9, 3.99, 3.999]
assert [round(f(v), 6) for v in (2.1, 2.01, 2.001)] == [4.1, 4.01, 4.001]
assert sp.limit((x**2 - 4) / (x - 2), x, 2) == 4

assert sp.limit((x**2 - 9) / (x - 3), x, 3) == 6
assert sp.limit((sp.sqrt(x + 4) - 2) / x, x, 0) == sp.Rational(1, 4)

k = sp.symbols("k")
assert sp.solve(sp.Eq(2**2 + 1, 2 * k - 1), k) == [3]

g = (3 * x**2 + 1) / (x**2 - 4)
assert sp.limit(g, x, sp.oo) == 3 and sp.limit(g, x, 2, "+") == sp.oo and sp.limit(g, x, 2, "-") == -sp.oo

h = x**3 - x - 1
assert h.subs(x, 1) == -1 and h.subs(x, 2) == 5
# -----------------------------------------------------------------------------------------------

write(1, [
("limit-definition-and-notation", r"""
### The idea
A limit describes what a function's output approaches as the input approaches a value. It is not the function's value at that point. We write $\lim_{x \to c} f(x) = L$ when $f(x)$ can be made as close to $L$ as we like by taking $x$ close enough to $c$, without ever using $x = c$ itself.

### Key facts
- $f(c)$ can be different from the limit, or not exist at all. The limit only looks at nearby values.
- A one-sided limit looks from one direction: $\lim_{x \to c^-}$ from the left, $\lim_{x \to c^+}$ from the right.
- The two-sided limit exists exactly when both one-sided limits exist and are equal. If they disagree, the limit does not exist.
- From a graph, follow the curve toward $x = c$ from each side and read the height it heads for. An open circle marks a point the curve approaches but does not include.
- From a table, choose $x$ values closer and closer to $c$ on both sides and watch where $f(x)$ settles.

### Watch out for
Reading the limit off $f(c)$. If a graph has a hole at $x = 2$ and a filled dot somewhere else above $x = 2$, the limit is the height of the hole, not the dot.

### Worked example
Estimate $\lim_{x \to 2} \dfrac{x^2 - 4}{x - 2}$. The function is undefined at $x = 2$, so try nearby values.

From the left, $x = 1.9, 1.99, 1.999$ give $f(x) = 3.9, 3.99, 3.999$. From the right, $x = 2.1, 2.01, 2.001$ give $f(x) = 4.1, 4.01, 4.001$.

Both sides head for 4, so the limit is 4, even though $f(2)$ does not exist.
"""),
("algebraic-limit-techniques", r"""
### The idea
To find a limit exactly, try direct substitution first. If it gives a number, that is the limit (for the continuous functions in this course). If it gives $\frac{0}{0}$, the expression is hiding a factor that is causing the trouble, and the job is to rewrite it so the trouble goes away.

### Key facts
- A result of $\frac{0}{0}$ is a signal to rewrite, not an answer. The limit may still exist.
- **Factor and cancel.** Common factors cancel for $x \ne c$, which is all a limit looks at.
- **Multiply by the conjugate** when a square root is involved.
- **Combine fractions** over a common denominator when the expression is a difference of fractions.
- Two trigonometric limits worth knowing: $\lim_{x \to 0} \dfrac{\sin x}{x} = 1$ and $\lim_{x \to 0} \dfrac{1 - \cos x}{x} = 0$.
- A nonzero number divided by $0$ is not $\frac{0}{0}$. It points to a vertical asymptote (see the infinite limits topic).

### Watch out for
Cancelling terms instead of factors. In $\dfrac{x^2 - 9}{x - 3}$ you cancel the factor $(x - 3)$ after factoring the top, not the $x$'s.

### Worked example
Find $\lim_{x \to 0} \dfrac{\sqrt{x + 4} - 2}{x}$. Substituting gives $\frac{0}{0}$, so multiply top and bottom by the conjugate $\sqrt{x + 4} + 2$:

$$
\begin{aligned}
&\frac{(\sqrt{x + 4} - 2)(\sqrt{x + 4} + 2)}{x(\sqrt{x + 4} + 2)} \\
&= \frac{(x + 4) - 4}{x(\sqrt{x + 4} + 2)} \\
&= \frac{1}{\sqrt{x + 4} + 2}
\end{aligned}
$$

Now substitute $x = 0$: the limit is $\dfrac{1}{4}$.
"""),
("continuity", r"""
### The idea
A function is continuous at $x = c$ if you can draw it through that point without lifting your pencil. Precisely, three things must all be true.

### Key facts
- $f(c)$ is defined.
- $\lim_{x \to c} f(x)$ exists.
- $\lim_{x \to c} f(x) = f(c)$.

A function that fails one of these has a discontinuity at $c$:
- **Removable:** the limit exists but $f(c)$ is missing or different (a hole or a misplaced dot).
- **Jump:** the one-sided limits exist but are different.
- **Infinite:** the function grows without bound near $c$ (a vertical asymptote).

Polynomials, $\sin x$, $\cos x$ and $e^x$ are continuous everywhere. Rational functions are continuous everywhere except where the denominator is $0$. A function is continuous on an interval if it is continuous at every point of it.

### Watch out for
Checking only that $f(c)$ exists, or only that the limit exists. You need all three conditions, and the third one connects the first two.

### Worked example
Find $k$ so that $f(x) = \begin{cases} x^2 + 1 & x < 2 \\ kx - 1 & x \ge 2 \end{cases}$ is continuous at $x = 2$.

From the left the limit is $2^2 + 1 = 5$. From the right it is $2k - 1$, and that is also $f(2)$. Continuity needs these to match: $2k - 1 = 5$, so $k = 3$.
"""),
("infinite-limits-and-asymptotes", r"""
### The idea
Two different questions get lumped together here. A **vertical asymptote** is about what happens as $x$ approaches a finite number and the output blows up. A **horizontal asymptote** is about what happens to the output as $x$ grows without bound.

### Key facts
- $\lim_{x \to c} f(x) = \pm\infty$ means the function grows without bound near $c$. The limit technically does not exist, but writing $\infty$ describes how it fails.
- For a rational function in lowest terms, a vertical asymptote sits at each zero of the denominator. A zero that cancels leaves a hole, not an asymptote.
- To decide between $+\infty$ and $-\infty$, check the sign on each side of $c$.
- For a rational function, compare degrees. If the numerator's degree is smaller, the horizontal asymptote is $y = 0$. If the degrees are equal, it is the ratio of leading coefficients. If the numerator's degree is larger, there is no horizontal asymptote.
- $\lim_{x \to \infty} f(x) = L$ means the graph settles toward the line $y = L$.

### Watch out for
Calling every zero of the denominator an asymptote. Factor first: in $\dfrac{x - 2}{x^2 - 4}$ the factor $(x - 2)$ cancels, leaving a hole at $x = 2$ and an asymptote only at $x = -2$.

### Worked example
For $f(x) = \dfrac{3x^2 + 1}{x^2 - 4}$, the denominator factors as $(x - 2)(x + 2)$, so the vertical asymptotes are $x = 2$ and $x = -2$. The degrees are equal and the leading coefficients are $3$ and $1$, so the horizontal asymptote is $y = 3$.

Near $x = 2$ from the right, the top is about $13$ (positive) and the bottom is small and positive, so $f(x) \to +\infty$. From the left the bottom is small and negative, so $f(x) \to -\infty$.
"""),
("intermediate-value-theorem", r"""
### The idea
If a function is continuous on a closed interval, it cannot skip over any value between its endpoint values. Walk from the height $f(a)$ to the height $f(b)$ without lifting your pencil and you must pass through every height in between.

### Key facts
- **Statement:** if $f$ is continuous on $[a, b]$ and $N$ is between $f(a)$ and $f(b)$, then there is at least one $c$ in $(a, b)$ with $f(c) = N$.
- It only promises that such a $c$ exists. It does not say how many there are or where.
- The standard use is to show a root exists: take $N = 0$ and find two inputs where $f$ has opposite signs.
- Continuity on the whole closed interval is required. A jump can hop over the target value.

### Watch out for
Applying it to a function that is not continuous. For $f(x) = \dfrac{1}{x}$ on $[-1, 1]$, we have $f(-1) = -1$ and $f(1) = 1$, but there is no root, because $f$ is not continuous at $0$.

### Worked example
Show that $x^3 - x - 1 = 0$ has a solution between $x = 1$ and $x = 2$.

Let $f(x) = x^3 - x - 1$, which is a polynomial and so continuous everywhere. Then $f(1) = -1$ and $f(2) = 5$. Since $0$ is between $-1$ and $5$, the Intermediate Value Theorem guarantees a $c$ in $(1, 2)$ with $f(c) = 0$.
"""),
])
