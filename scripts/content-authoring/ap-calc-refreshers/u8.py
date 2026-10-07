import sympy as sp
from common import write

x = sp.symbols("x")

# --- checks -----------------------------------------------------------------------------------
avg = sp.integrate(x**2, (x, 0, 3)) / 3
assert avg == 3 and sp.solve(sp.Eq(x**2, 3), x) == [-sp.sqrt(3), sp.sqrt(3)]

assert sp.solve(sp.Eq(x + 2, x**2), x) == [-1, 2]
assert sp.integrate((x + 2) - x**2, (x, -1, 2)) == sp.Rational(9, 2)
assert sp.integrate(x - x**2, (x, 0, 1)) == sp.Rational(1, 6)

assert sp.integrate(sp.sqrt(x), (x, 0, 4)) == sp.Rational(16, 3)  # not used in text, sanity check
assert sp.integrate(sp.sqrt(x) ** 2, (x, 0, 4)) == 8              # squares with side sqrt(x): A = x
assert sp.integrate(sp.pi * sp.sqrt(x) ** 2, (x, 0, 4)) == 8 * sp.pi
assert sp.integrate(sp.pi * (x**2 - x**4), (x, 0, 1)) == 2 * sp.pi / 15
assert sp.integrate(sp.pi * sp.Rational(1, 8) * (sp.sqrt(x)) ** 2, (x, 0, 4)) == sp.pi  # semicircle: pi*d^2/8, d = sqrt(x)
# ----------------------------------------------------------------------------------------------

write(8, [
("average-value-of-a-function", r"""
### The idea
The average value of a function over an interval is the constant height that would give the same area. It is the total accumulated amount divided by the length of the interval.

### Key facts
- $f_{\text{avg}} = \dfrac{1}{b - a}\displaystyle\int_a^b f(x)\,dx$.
- This is different from the **average rate of change** $\dfrac{f(b) - f(a)}{b - a}$. One averages the values of $f$. The other averages its derivative.
- **Mean Value Theorem for integrals:** if $f$ is continuous on $[a, b]$, there is a $c$ in $[a, b]$ with $f(c) = f_{\text{avg}}$.
- For a velocity function, the average value is the average velocity. Multiply by the length of time to get the displacement.
- The units of the average are the units of $f$.

### Watch out for
Forgetting to divide by $b - a$. Without it you have the integral, which is a total, not an average. Also, do not confuse the two kinds of average above.

### Worked example
Find the average value of $f(x) = x^2$ on $[0, 3]$.

$$f_{\text{avg}} = \frac{1}{3 - 0}\int_0^3 x^2\,dx = \frac{1}{3}\cdot 9 = 3.$$

By the theorem, some $c$ satisfies $c^2 = 3$. Taking the value in $[0, 3]$, $c = \sqrt{3} \approx 1.73$.
"""),
("area-between-curves", r"""
### The idea
The area between two curves is the area under the upper curve minus the area under the lower one. Integrate the vertical gap between them.

### Key facts
- If $f(x) \ge g(x)$ on $[a, b]$, the area is $\displaystyle\int_a^b \big[f(x) - g(x)\big]\,dx$: top minus bottom.
- Find the limits by solving $f(x) = g(x)$ for the points where the curves meet.
- If the curves **cross** inside the interval, split the integral at each crossing, so that top minus bottom is correct in every piece.
- When it is easier, integrate with respect to $y$: area $= \displaystyle\int_c^d \big[\text{right} - \text{left}\big]\,dy$.
- Area is never negative. If your answer is negative, the order of subtraction is wrong.

### Watch out for
Using the same top-minus-bottom for the whole interval when the curves cross. That gives the signed area, where the pieces cancel each other.

### Worked example
Find the area between $y = x + 2$ and $y = x^2$.

Set them equal: $x + 2 = x^2$ gives $x = -1$ and $x = 2$. On $(-1, 2)$ the line is above the parabola, so

$$\int_{-1}^{2}\big[(x + 2) - x^2\big]\,dx = \left[\frac{x^2}{2} + 2x - \frac{x^3}{3}\right]_{-1}^{2} = \frac{9}{2}.$$
"""),
("volume-by-cross-sections", r"""
### The idea
If you know the area $A(x)$ of the slice of a solid at each position $x$, you can add up the slices to get the volume. Each slice has a tiny thickness $dx$, so its volume is $A(x)\,dx$.

### Key facts
- $V = \displaystyle\int_a^b A(x)\,dx$ for slices perpendicular to the $x$-axis. For slices perpendicular to the $y$-axis, integrate $A(y)\,dy$.
- The **base** is a region in the plane, and the length of a cross-section's base edge comes from the region: top minus bottom.
- The area formula depends on the shape of the slice, in terms of that length $s$:
  - square: $s^2$
  - semicircle with diameter $s$: $\dfrac{\pi}{8}s^2$
  - equilateral triangle with side $s$: $\dfrac{\sqrt{3}}{4}s^2$
  - rectangle of height $h$: $s \cdot h$
- Identify the shape first, then express its dimension in terms of $x$.

### Watch out for
Using the wrong formula for the slice, or using the radius where the diameter is given (or the reverse). For a semicircle, the base edge is the **diameter**.

### Worked example
The base of a solid is the region under $y = \sqrt{x}$ from $x = 0$ to $x = 4$. Cross-sections perpendicular to the $x$-axis are squares.

The side of the square at $x$ is $s = \sqrt{x}$, so $A(x) = (\sqrt{x})^2 = x$. Then

$$V = \int_0^4 x\,dx = \left[\frac{x^2}{2}\right]_0^4 = 8.$$

With semicircles instead, $A(x) = \dfrac{\pi}{8}x$ and $V = \pi$.
"""),
("volume-by-disc-washer", r"""
### The idea
Spin a region around a line and it sweeps out a solid. Slicing that solid perpendicular to the axis gives circular discs, or discs with a hole (washers), whose areas you can add.

### Key facts
- **Disc method** (the region touches the axis): $V = \pi\displaystyle\int_a^b \big[R(x)\big]^2\,dx$, where $R$ is the distance from the axis to the curve.
- **Washer method** (there is a gap between region and axis): $V = \pi\displaystyle\int_a^b \Big(\big[R(x)\big]^2 - \big[r(x)\big]^2\Big)\,dx$, with $R$ the outer radius and $r$ the inner radius.
- The radius is a **distance from the axis of rotation**. If the axis is not the $x$-axis (for example $y = -1$), the radii change: $R = f(x) + 1$.
- If you rotate about a vertical line and slice horizontally, integrate with respect to $y$.
- Square the **radius**, then subtract. Do not square the difference $R - r$.

### Watch out for
Writing $\pi\int (R - r)^2\,dx$ for a washer. The correct form subtracts the squares: $R^2 - r^2$. The two are not equal.

### Worked example
Rotate the region under $y = \sqrt{x}$ on $[0, 4]$ about the $x$-axis. Discs of radius $\sqrt{x}$:

$$V = \pi\int_0^4 x\,dx = 8\pi.$$

Now rotate the region between $y = x$ (outer) and $y = x^2$ (inner) on $[0, 1]$ about the $x$-axis. Washers:

$$V = \pi\int_0^1 \big(x^2 - x^4\big)\,dx = \pi\left(\frac{1}{3} - \frac{1}{5}\right) = \frac{2\pi}{15}.$$
"""),
])
