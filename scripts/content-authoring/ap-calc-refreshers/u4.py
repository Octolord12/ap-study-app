import sympy as sp
from common import write

t, x, y = sp.symbols("t x y")

# --- checks -----------------------------------------------------------------------------------
s = t**3 - 6 * t**2 + 9 * t
v, a = sp.diff(s, t), sp.diff(s, t, 2)
assert sp.expand(v - 3 * (t - 1) * (t - 3)) == 0 and sp.expand(a - (6 * t - 12)) == 0
assert sp.solve(v, t) == [1, 3]
assert (v.subs(t, sp.Rational(3, 2)), a.subs(t, sp.Rational(3, 2))) == (sp.Rational(-9, 4), -3)  # both negative: speeding up
assert (v.subs(t, sp.Rational(5, 2)), a.subs(t, sp.Rational(5, 2))) == (sp.Rational(-9, 4), 3)    # opposite signs: slowing down
assert (v.subs(t, 4), a.subs(t, 4)) == (9, 12)
assert [s.subs(t, k) for k in (0, 1, 3, 4)] == [0, 4, 0, 4]
assert sp.integrate(abs(v), (t, 0, 4)) == 12 and s.subs(t, 4) - s.subs(t, 0) == 4

# ladder: x^2 + y^2 = 100, dx/dt = 2 at x = 6 (so y = 8): dy/dt = -(x/y) dx/dt
assert 6**2 + 8**2 == 100 and sp.Rational(-6, 8) * 2 == sp.Rational(-3, 2)

f = sp.sqrt(x)
L = lambda u: f.subs(x, 4) + sp.diff(f, x).subs(x, 4) * (u - 4)
assert L(sp.Rational(41, 10)) == sp.Rational(81, 40) and float(f.subs(x, sp.Rational(41, 10))) < float(L(sp.Rational(41, 10)))
assert sp.diff(f, x, 2).subs(x, 4) < 0  # concave down: tangent line lies above, so an overestimate

assert sp.limit((sp.exp(x) - 1) / x, x, 0) == 1
assert sp.limit(sp.log(x) / x, x, sp.oo) == 0
assert sp.limit((x + 3) / (x - 1), x, 2) == 5
# ----------------------------------------------------------------------------------------------

write(4, [
("straight-line-motion", r"""
### The idea
For an object moving along a line, position, velocity and acceleration are linked by derivatives. Reading their signs together tells you what the object is doing.

### Key facts
- Position $s(t)$, velocity $v(t) = s'(t)$, acceleration $a(t) = v'(t) = s''(t)$.
- The sign of $v$ is the direction of motion. The object **changes direction** when $v$ changes sign (a zero of $v$ is not enough by itself).
- **Speed** is $|v|$. It is **increasing** when $v$ and $a$ have the same sign, and **decreasing** when they have opposite signs.
- **Displacement** is the net change in position, $s(b) - s(a)$. **Total distance** adds up all the movement, so it counts back-and-forth motion as positive.
- Units: velocity is position units per time, acceleration is velocity units per time.

### Watch out for
Saying the object slows down because acceleration is negative. Negative acceleration speeds the object up if it is already moving in the negative direction. Compare the signs of $v$ and $a$.

### Worked example
A particle has $s(t) = t^3 - 6t^2 + 9t$ for $t \ge 0$. Then $v(t) = 3t^2 - 12t + 9 = 3(t - 1)(t - 3)$ and $a(t) = 6t - 12$.

The velocity is positive before $t = 1$, negative from $1$ to $3$, and positive after $3$, so the particle turns around at $t = 1$ and $t = 3$.

At $t = 1.5$: $v = -2.25$ and $a = -3$, the same sign, so it is speeding up. At $t = 2.5$: $v = -2.25$ and $a = 3$, opposite signs, so it is slowing down.

On $[0, 4]$: $s(0) = 0$, $s(1) = 4$, $s(3) = 0$, $s(4) = 4$. The displacement is $4$, but the total distance is $4 + 4 + 4 = 12$.
"""),
("related-rates", r"""
### The idea
When two quantities are linked by an equation, and both change with time, their rates of change are linked too. Differentiate the equation with respect to time to find the link.

### Key facts
1. Draw a picture and name every changing quantity with a variable. Write down which rates are given and which one you want.
2. Write an equation connecting the variables that holds at **every** moment.
3. Differentiate both sides with respect to $t$. Every variable that changes gets a factor like $\dfrac{dx}{dt}$ from the chain rule.
4. Only now substitute the values for the specific moment, then solve.
5. Answer with units, and say what the sign means (a negative rate means the quantity is decreasing).

### Watch out for
Substituting numbers before differentiating. A quantity that is changing must stay a variable until after the derivative is taken. Plugging in $x = 6$ too early turns it into a constant whose derivative is $0$.

### Worked example
A 10-foot ladder leans against a wall. The bottom slides away at $2$ ft/s. How fast is the top sliding down when the bottom is $6$ ft from the wall?

Let $x$ be the bottom's distance and $y$ the top's height. Then $x^2 + y^2 = 100$. Differentiate with respect to $t$:

$$
\begin{aligned}
2x\frac{dx}{dt} + 2y\frac{dy}{dt} &= 0 \\
\frac{dy}{dt} &= -\frac{x}{y}\frac{dx}{dt}
\end{aligned}
$$

When $x = 6$, $y = 8$. So $\dfrac{dy}{dt} = -\dfrac{6}{8}(2) = -1.5$ ft/s. The top is sliding down at $1.5$ ft/s.
"""),
("local-linearization", r"""
### The idea
Near a point, a smooth curve is almost a straight line: its tangent line. So you can use the tangent line to estimate function values close to the point, which is useful when the function itself is hard to evaluate.

### Key facts
- The linearization of $f$ at $x = a$ is $L(x) = f(a) + f'(a)(x - a)$. It is just the tangent line equation.
- Use it for $x$ close to $a$. The farther you move away, the worse the estimate.
- If $f$ is **concave up** near $a$, the tangent line lies below the curve, so $L(x)$ is an **underestimate**.
- If $f$ is **concave down**, the tangent line lies above the curve, so $L(x)$ is an **overestimate**.
- Pick $a$ to be a nearby input where $f(a)$ and $f'(a)$ are easy to compute.

### Watch out for
Getting the over/underestimate backward. Think of the picture: a curve that bends away from its tangent line on the upper side makes the tangent line lie below it.

### Worked example
Estimate $\sqrt{4.1}$. Take $f(x) = \sqrt{x}$ and $a = 4$, where $f(4) = 2$ and $f'(x) = \dfrac{1}{2\sqrt{x}}$ gives $f'(4) = \dfrac{1}{4}$.

$$
\begin{aligned}
L(x) &= 2 + \tfrac{1}{4}(x - 4) \\
L(4.1) &= 2 + 0.025 = 2.025
\end{aligned}
$$

Since $f''(x) < 0$, the curve is concave down, so $2.025$ is an overestimate. The true value is about $2.02485$.
"""),
("lhopitals-rule", r"""
### The idea
Some limits look like $\frac{0}{0}$ or $\frac{\infty}{\infty}$ and cannot be settled by substitution. L'Hôpital's Rule replaces the top and the bottom by their derivatives, which often makes the problem simple.

### Key facts
- **The rule:** if $\lim \dfrac{f(x)}{g(x)}$ has the form $\dfrac{0}{0}$ or $\dfrac{\pm\infty}{\pm\infty}$, then $\lim \dfrac{f(x)}{g(x)} = \lim \dfrac{f'(x)}{g'(x)}$, provided the second limit exists (or is infinite).
- Check the form **first**. The rule only applies to those two indeterminate forms.
- You can apply it again if the new limit is still indeterminate.
- Differentiate the top and the bottom **separately**. This is not the quotient rule.
- Other indeterminate forms, such as $0 \cdot \infty$, must be rewritten as a quotient before you can use it.

### Watch out for
Using the rule when substitution already gives an answer. For $\lim_{x \to 2} \dfrac{x + 3}{x - 1}$ substitution gives $5$, which is the limit. Applying the rule here would give a wrong answer.

### Worked example
Find $\lim_{x \to 0} \dfrac{e^x - 1}{x}$. Substitution gives $\dfrac{0}{0}$, so apply the rule:

$$\lim_{x \to 0} \frac{e^x}{1} = 1.$$

Find $\lim_{x \to \infty} \dfrac{\ln x}{x}$. This has the form $\dfrac{\infty}{\infty}$, so

$$\lim_{x \to \infty} \frac{1/x}{1} = 0.$$
"""),
])
