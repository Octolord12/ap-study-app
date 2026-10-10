import sympy as sp
from common import write

x = sp.symbols("x", real=True)
n = sp.symbols("n", integer=True, positive=True)
R = sp.Rational

# --- checks -----------------------------------------------------------------------------------
assert sp.summation(2 ** (n + 1) / sp.Integer(5) ** n, (n, 0, sp.oo)) == R(10, 3) and R(36, 100) / (1 - R(1, 100)) == R(4, 11)
assert sp.integrate(1 / (x**2 + 1), (x, 1, sp.oo)) == sp.pi / 4 and sp.diff(1 / (x**2 + 1), x).subs(x, 2) < 0
assert sp.limit(((3 * n + 2) / (n**3 + n)) / (1 / n**2), n, sp.oo) == 3
S4 = 1 - R(1, 2) + R(1, 6) - R(1, 24)
assert S4 == R(5, 8) and 0 < float(1 - 1 / sp.E) - float(S4) < float(R(1, 120))
assert sp.limit((sp.factorial(n + 1) / (n + 1) ** (n + 1)) / (sp.factorial(n) / n**n), n, sp.oo) == 1 / sp.E
f = sp.sqrt(x)
T2 = f.subs(x, 4) + sp.diff(f, x).subs(x, 4) * (x - 4) + sp.diff(f, x, 2).subs(x, 4) / 2 * (x - 4) ** 2
assert sp.expand(T2 - (2 + (x - 4) / 4 - (x - 4) ** 2 / 64)) == 0 and T2.subs(x, R(22, 5)) == R(839, 400)
m3 = max(abs(sp.diff(f, x, 3).subs(x, c)) for c in (4, R(22, 5)))
assert m3 == R(3, 256)
bound = m3 / 6 * R(2, 5) ** 3
assert bound == R(1, 8000) and abs(float(sp.sqrt(R(22, 5))) - float(T2.subs(x, R(22, 5)))) < float(bound)
a_ = lambda xv: (xv - 3) ** n / (n**2 * sp.Integer(4) ** n)
assert [sp.limit(sp.Abs(a_(v_).subs(n, n + 1) / a_(v_)), n, sp.oo) for v_ in (4, 5, 7, -1)] == [R(1, 4), R(1, 2), 1, 1]  # the ratio limit is |x - 3| / 4
assert sp.summation(sp.Abs(a_(7)), (n, 1, sp.oo)) == sp.pi**2 / 6 and sp.summation(sp.Abs(a_(-1)), (n, 1, sp.oo)) == sp.pi**2 / 6  # both endpoints give p-series with p = 2
ser = sp.series(x * sp.exp(x**2), x, 0, 8).removeO()
assert [ser.coeff(x, k) for k in (1, 3, 5)] == [1, 1, R(1, 2)] and sp.diff(x * sp.exp(x**2), x, 5).subs(x, 0) == 60
assert sp.series(1 / (2 + x), x, 0, 5).removeO() == R(1, 2) - x / 4 + x**2 / 8 - x**3 / 16 + x**4 / 32
# ----------------------------------------------------------------------------------------------

write(10, [
("convergent-and-geometric-series", r"""
### The idea
An infinite series is a sum with no last term. It **converges** if the running totals (the partial sums) settle on a number, and **diverges** if they do not. Geometric series are the ones you can add up exactly.

### Key facts
- $\sum a_n$ converges to $S$ when the partial sums $S_N = a_1 + a_2 + \cdots + a_N$ approach $S$ as $N \to \infty$.
- **Geometric series:** $\displaystyle\sum_{n=0}^{\infty} ar^n = \frac{a}{1 - r}$ when $|r| < 1$, where $a$ is the **first term** and $r$ the common ratio. If $|r| \ge 1$ it diverges.
- If the sum starts at $n = 1$, the first term is the value at $n = 1$, not at $n = 0$.
- **Finite sum:** $S_N = a\,\dfrac{1 - r^N}{1 - r}$.
- A repeating decimal is a geometric series: $0.\overline{36} = \dfrac{36}{100} + \dfrac{36}{100^2} + \cdots = \dfrac{36/100}{1 - 1/100} = \dfrac{4}{11}$.
- Changing finitely many terms never changes whether a series converges (it may change the sum).

### Watch out for
Using the wrong first term, and forgetting to check $|r| < 1$. A series like $1 + 2 + 4 + 8 + \cdots$ has no sum.

### Worked example
Find $\displaystyle\sum_{n=0}^{\infty}\frac{2^{n+1}}{5^n}$.

Rewrite the terms as $2\cdot\left(\dfrac25\right)^n$. The first term is $a = 2$ and the ratio is $r = \dfrac25$, which has $|r| < 1$, so

$$\sum_{n=0}^{\infty}\frac{2^{n+1}}{5^n} = \frac{2}{1 - \frac25} = \frac{10}{3}$$
"""),
("divergence-integral-and-p-series", r"""
### The idea
Before using heavier tests, ask whether the terms even have a chance. Then compare the series with an integral or with a $p$-series, whose behavior you know.

### Key facts
- **$n$th-Term Test:** if $\lim_{n\to\infty} a_n \ne 0$ (or does not exist), then $\sum a_n$ **diverges**. If the limit is 0, the test tells you nothing.
- **Harmonic series** $\sum \dfrac1n$ diverges, even though its terms go to 0.
- **$p$-series:** $\sum \dfrac{1}{n^p}$ converges exactly when $p > 1$.
- **Integral Test:** if $f$ is positive, continuous and decreasing for $x \ge 1$ and $a_n = f(n)$, then $\sum a_n$ and $\int_1^\infty f(x)\,dx$ both converge or both diverge. It is enough that $f$ is eventually decreasing.
- A convergent integral does **not** give the sum of the series, only the fact that it converges.

### Watch out for
Concluding that a series converges because its terms go to 0. Also, check the hypotheses of the Integral Test before computing the integral.

### Worked example
Does $\displaystyle\sum_{n=1}^{\infty}\frac{1}{n^2 + 1}$ converge?

Let $f(x) = \dfrac{1}{x^2 + 1}$. It is positive, continuous and decreasing for $x \ge 1$. Then

$$
\begin{aligned}
\int_1^\infty \frac{dx}{x^2 + 1} &= \lim_{b\to\infty}\Big[\arctan x\Big]_1^b \\
&= \frac\pi2 - \frac\pi4 = \frac\pi4
\end{aligned}
$$

The integral is finite, so the series converges. (Its sum is not $\frac\pi4$.)
"""),
("comparison-tests", r"""
### The idea
If a series behaves like one you already understand, it has the same fate. The comparison tests make "behaves like" precise.

### Key facts
- **Direct Comparison:** if $0 \le a_n \le b_n$ and $\sum b_n$ converges, then $\sum a_n$ converges. If $a_n \ge b_n \ge 0$ and $\sum b_n$ diverges, then $\sum a_n$ diverges.
- **Limit Comparison:** for positive terms, if $\displaystyle\lim_{n\to\infty}\frac{a_n}{b_n} = L$ with $0 < L < \infty$, then $\sum a_n$ and $\sum b_n$ both converge or both diverge.
- **Pick $b_n$ from the dominant terms** of $a_n$: for a ratio of polynomials, compare with $\dfrac{1}{n^k}$, where $k$ is the difference of the degrees.
- Good benchmarks: geometric series, and $p$-series (including the harmonic series).

### Watch out for
The direction of the inequality. Being smaller than a divergent series, or larger than a convergent one, proves nothing.

### Worked example
Does $\displaystyle\sum_{n=1}^{\infty}\frac{3n + 2}{n^3 + n}$ converge?

The terms behave like $\dfrac{3n}{n^3} = \dfrac{3}{n^2}$. Compare with $b_n = \dfrac{1}{n^2}$:

$$
\begin{aligned}
\lim_{n\to\infty}\frac{(3n + 2)/(n^3 + n)}{1/n^2} &= \lim_{n\to\infty}\frac{3n^3 + 2n^2}{n^3 + n} \\
&= 3
\end{aligned}
$$

The limit is finite and positive, and $\sum \frac1{n^2}$ converges, so the series converges.
"""),
("alternating-series-and-error-bound", r"""
### The idea
When terms alternate in sign and shrink to zero, the partial sums zigzag around the true sum, and each zigzag is smaller than the last. That makes both convergence and error estimates easy.

### Key facts
- **Alternating Series Test:** if $a_n > 0$, the $a_n$ are decreasing (at least eventually) and $a_n \to 0$, then $\sum (-1)^n a_n$ converges.
- **Error bound:** for such a series, $|S - S_N| \le a_{N+1}$: the error is at most the **first term you left out**. The true sum lies between consecutive partial sums.
- **Absolute convergence:** $\sum |a_n|$ converges. It guarantees convergence of $\sum a_n$.
- **Conditional convergence:** $\sum a_n$ converges but $\sum |a_n|$ diverges, like $\sum \dfrac{(-1)^n}{n}$.
- If $a_n \not\to 0$, the series diverges by the $n$th-Term Test, and the alternating test does not apply.

### Watch out for
Using the last term used instead of the first term omitted as the bound, and applying the bound to series whose terms do not alternate.

### Worked example
Estimate $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n!}$ with its first four terms, and bound the error.

$$S_4 = 1 - \frac12 + \frac16 - \frac1{24} = \frac58 = 0.625$$

The terms $\frac{1}{n!}$ decrease to 0, so the error is at most the first omitted term, $\dfrac{1}{5!} = \dfrac{1}{120} \approx 0.0083$. (The series actually sums to $1 - \frac1e \approx 0.6321$, which is within that bound.)
"""),
("ratio-test-and-absolute-convergence", r"""
### The idea
The Ratio Test asks how fast terms shrink from one to the next. If each term is a fixed fraction (less than 1) of the one before, the series behaves like a geometric series and converges.

### Key facts
- **Ratio Test:** let $L = \displaystyle\lim_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|$. If $L < 1$, the series converges **absolutely**. If $L > 1$ (including $\infty$), it diverges. If $L = 1$, the test says nothing.
- It is best for terms with **factorials** or **exponentials** like $n!$, $2^n$, $n^n$. Factorials simplify: $\dfrac{(n+1)!}{n!} = n + 1$.
- For a $p$-series, $L = 1$ always, so use a different test.
- **Absolute convergence implies convergence.** To classify a series: check $\sum|a_n|$ first; if that diverges and the series alternates, try the Alternating Series Test for conditional convergence.

### Watch out for
Treating $L = 1$ as divergence, and forgetting the absolute value in the ratio.

### Worked example
Does $\displaystyle\sum_{n=1}^{\infty}\frac{n!}{n^n}$ converge?

$$
\begin{aligned}
\frac{a_{n+1}}{a_n} &= \frac{(n+1)!}{(n+1)^{n+1}}\cdot\frac{n^n}{n!} \\
&= \left(\frac{n}{n+1}\right)^n \\
&= \left(1 + \frac1n\right)^{-n} \longrightarrow \frac1e
\end{aligned}
$$

Since $\frac1e < 1$, the series converges absolutely.
"""),
("taylor-polynomials", r"""
### The idea
A Taylor polynomial approximates a function near a point by matching the function's value and its first several derivatives there. The more derivatives it matches, the better the fit.

### Key facts
- **Degree $n$ polynomial about $x = a$:**
  $$T_n(x) = \sum_{k=0}^{n}\frac{f^{(k)}(a)}{k!}(x - a)^k$$
- With $a = 0$ it is a **Maclaurin** polynomial. The first-degree one is the tangent line.
- Memorize the low-order ones for $e^x$, $\sin x$ and $\cos x$ about 0.
- $T_n$ is written in powers of $(x - a)$, and each coefficient is a derivative **divided by $k!$**.
- The approximation is best near $a$. How good is the subject of the Lagrange error bound.

### Watch out for
Leaving out the factorials, centering at the wrong point, and evaluating derivatives at $x$ instead of at $a$.

### Worked example
Find $T_2$ for $f(x) = \sqrt x$ about $x = 4$, and use it to approximate $\sqrt{4.4}$.

$f(4) = 2$, $f'(x) = \dfrac{1}{2\sqrt x}$ gives $f'(4) = \dfrac14$, and $f''(x) = -\dfrac{1}{4x^{3/2}}$ gives $f''(4) = -\dfrac{1}{32}$. So

$$T_2(x) = 2 + \frac{x - 4}{4} - \frac{(x - 4)^2}{64}$$

$$\sqrt{4.4} \approx 2 + 0.1 - 0.0025 = 2.0975$$
"""),
("lagrange-error-bound", r"""
### The idea
A Taylor polynomial is only useful if you know how far off it can be. The Lagrange error bound gives a guaranteed limit on the error, using the next derivative.

### Key facts
- **Bound:** if $\left|f^{(n+1)}(t)\right| \le M$ for all $t$ between $a$ and $x$, then
  $$\left|f(x) - T_n(x)\right| \le \frac{M}{(n+1)!}\,|x - a|^{n+1}$$
- It looks like the first omitted Taylor term, with the derivative replaced by its **largest** absolute value on the interval.
- To pick $M$, bound $|f^{(n+1)}|$ on the whole interval from $a$ to $x$: find where it is largest, or use a simple known bound (like $|\sin t| \le 1$ or $e^t \le 3$ for $t \le 1$).
- To find how many terms are needed, solve $\dfrac{M}{(n+1)!}|x - a|^{n+1} <$ the tolerance for the smallest $n$.

### Watch out for
Using the wrong derivative (it is the $(n+1)$th), taking $M$ at one endpoint without checking it is the maximum, and forgetting the factorial.

### Worked example
Bound the error in approximating $\sqrt{4.4}$ with $T_2$ about $x = 4$ from the previous topic.

$f'''(x) = \dfrac{3}{8x^{5/2}}$ is decreasing, so on $[4, 4.4]$ its largest value is $f'''(4) = \dfrac{3}{256}$. Then

$$\text{error} \le \frac{3/256}{3!}\,(0.4)^3 = \frac{1}{8000} = 0.000125$$

(The actual error is about $0.000118$.)
"""),
("radius-and-interval-of-convergence", r"""
### The idea
A power series $\sum c_n (x - a)^n$ is a function that only makes sense for those $x$ where the series converges. The set of such $x$ is always an interval centered at $a$.

### Key facts
- Use the **Ratio Test** on the terms, including the factor $|x - a|^n$. It gives a condition like $|x - a| < R$. $R$ is the **radius of convergence**.
- The radius can be $0$ (converges only at $x = a$), a positive number, or $\infty$ (converges for every $x$).
- The Ratio Test is silent at the endpoints $x = a \pm R$. **Test each endpoint separately** by substituting it into the series and using another test ($p$-series, alternating series, comparison).
- The **interval of convergence** includes whichever endpoints converge. It may be open, closed, or half-open.

### Watch out for
Forgetting the endpoints, and not centering the interval at $a$. For terms like $(3x - 2)^n$, solve $|3x - 2| < 1$ to get the interval in $x$.

### Worked example
Find the interval of convergence of $\displaystyle\sum_{n=1}^{\infty}\frac{(x - 3)^n}{n^2\,4^n}$.

The ratio of consecutive terms has absolute value $\dfrac{n^2}{(n+1)^2}\cdot\dfrac{|x - 3|}{4} \to \dfrac{|x - 3|}{4}$, which is less than 1 when $|x - 3| < 4$, so $-1 < x < 7$.

At $x = 7$ the series is $\sum \dfrac{1}{n^2}$, which converges. At $x = -1$ it is $\sum \dfrac{(-1)^n}{n^2}$, which converges absolutely. So the interval is $[-1, 7]$.
"""),
("taylor-and-maclaurin-series", r"""
### The idea
Let the degree of a Taylor polynomial grow without bound and you get a Taylor series, a power series built from all the derivatives of $f$ at one point. Within its interval of convergence it often equals the function.

### Key facts
- **Taylor series about $a$:** $\displaystyle\sum_{n=0}^{\infty}\frac{f^{(n)}(a)}{n!}(x - a)^n$. About $a = 0$ it is the **Maclaurin** series.
- **Coefficients and derivatives:** if $c_n$ is the coefficient of $x^n$, then $f^{(n)}(0) = n!\,c_n$.
- Memorize these Maclaurin series:
  - $e^x = 1 + x + \dfrac{x^2}{2!} + \dfrac{x^3}{3!} + \cdots$ (all $x$)
  - $\sin x = x - \dfrac{x^3}{3!} + \dfrac{x^5}{5!} - \cdots$ and $\cos x = 1 - \dfrac{x^2}{2!} + \dfrac{x^4}{4!} - \cdots$ (all $x$)
  - $\dfrac{1}{1 - x} = 1 + x + x^2 + \cdots$ for $|x| < 1$
- **New series from old:** substitute (for $e^{x^2}$ replace $x$ by $x^2$), multiply by a power of $x$, or differentiate and integrate term by term.

### Watch out for
Forgetting that the coefficient is the derivative divided by $n!$, and skipping the sign pattern of $\sin x$ and $\cos x$.

### Worked example
Find the first three nonzero terms of the Maclaurin series for $f(x) = xe^{x^2}$, and $f^{(5)}(0)$.

Substitute $x^2$ into the series for $e^x$ and multiply by $x$:

$$
\begin{aligned}
xe^{x^2} &= x\left(1 + x^2 + \frac{x^4}{2} + \cdots\right) \\
&= x + x^3 + \frac{x^5}{2} + \cdots
\end{aligned}
$$

The coefficient of $x^5$ is $\frac12$, so $f^{(5)}(0) = 5!\cdot\frac12 = 60$.
"""),
("power-series-representations", r"""
### The idea
Many functions can be written as power series, and the geometric series is the key to most of them. Substitute into it, then differentiate or integrate term by term to get more.

### Key facts
- **Geometric series:** $\dfrac{1}{1 - u} = 1 + u + u^2 + \cdots$ for $|u| < 1$. Replacing $u$ by $-x^2$, $3x$ or $\dfrac{x}{2}$ gives series for $\dfrac{1}{1 + x^2}$, $\dfrac{1}{1 - 3x}$ and $\dfrac{1}{2 - x}$.
- **Differentiate or integrate term by term** inside the interval of convergence. The radius stays the same, but endpoints may change.
- $\dfrac{1}{(1 - x)^2} = 1 + 2x + 3x^2 + \cdots$ (differentiate the geometric series).
- $\ln(1 + x) = x - \dfrac{x^2}{2} + \dfrac{x^3}{3} - \cdots$ and $\arctan x = x - \dfrac{x^3}{3} + \dfrac{x^5}{5} - \cdots$ (integrate $\frac{1}{1+x}$ and $\frac{1}{1+x^2}$).
- Series give exact values for sums such as $\sum \dfrac{n}{2^n}$ (use $\sum nx^n = \dfrac{x}{(1 - x)^2}$ at $x = \frac12$).

### Watch out for
Forgetting the constant of integration (find it from a known value, such as $\ln 1 = 0$), and not matching the first term: $\frac{1}{2 + x}$ must be rewritten as $\frac{1/2}{1 + x/2}$ first.

### Worked example
Write $\dfrac{1}{2 + x}$ as a power series about $x = 0$ and find where it is valid.

$$
\begin{aligned}
\frac{1}{2 + x} &= \frac12\cdot\frac{1}{1 + \frac x2} \\
&= \frac12\sum_{n=0}^{\infty}\left(-\frac x2\right)^n \\
&= \sum_{n=0}^{\infty}\frac{(-1)^n x^n}{2^{n+1}}
\end{aligned}
$$

This is the geometric series with ratio $-\frac x2$, so it converges for $\left|\frac x2\right| < 1$, that is, $|x| < 2$.
"""),
])
