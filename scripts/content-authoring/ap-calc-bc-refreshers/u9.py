import sympy as sp
from common import write

t, x = sp.symbols("t x", real=True)
R = sp.Rational

# --- checks -----------------------------------------------------------------------------------
# parametric derivatives: x = t^2, y = t^3 - 3t at t = 2
xt, yt = t**2, t**3 - 3 * t
first = sp.diff(yt, t) / sp.diff(xt, t)
second = sp.simplify(sp.diff(first, t) / sp.diff(xt, t))
assert first.subs(t, 2) == R(9, 4) and second.subs(t, 2) == R(15, 32)
# arc length of the astroid arc x = cos^3 t, y = sin^3 t, 0 <= t <= pi/2
xa, ya = sp.cos(t) ** 3, sp.sin(t) ** 3
sp_ = sp.simplify(sp.diff(xa, t) ** 2 + sp.diff(ya, t) ** 2 - 9 * sp.sin(t) ** 2 * sp.cos(t) ** 2)
assert sp_ == 0 and sp.integrate(3 * sp.sin(t) * sp.cos(t), (t, 0, sp.pi / 2)) == R(3, 2)
# vectors: v = <cos t, 2t>, r(0) = <0, 3>
v = sp.Matrix([sp.cos(t), 2 * t])
r = sp.Matrix([0, 3]) + v.applyfunc(lambda e: sp.integrate(e, (t, 0, t)))
assert list(r) == [sp.sin(t), t**2 + 3]
# motion: v = <4 - t^2, t>, a = <-2t, 1>; at t = 1
vv, aa = sp.Matrix([4 - t**2, t]), sp.Matrix([4 - t**2, t]).diff(t)
assert list(vv.subs(t, 1)) == [3, 1] and list(aa.subs(t, 1)) == [-2, 1] and (vv.T * aa)[0].subs(t, 1) == -5
# polar: r = 1 + sin(theta) at pi/6 has a vertical tangent
rf = 1 + sp.sin(t)
dy = sp.diff(rf, t) * sp.sin(t) + rf * sp.cos(t)
dx = sp.diff(rf, t) * sp.cos(t) - rf * sp.sin(t)
assert sp.simplify(dx.subs(t, sp.pi / 6)) == 0 and sp.simplify(dy.subs(t, sp.pi / 6) - sp.sqrt(3)) == 0
# polar area: inside r = 4 sin(theta) and outside r = 2
A = sp.integrate((16 * sp.sin(t) ** 2 - 4) / 2, (t, sp.pi / 6, 5 * sp.pi / 6))
assert sp.simplify(A - (4 * sp.pi / 3 + 2 * sp.sqrt(3))) == 0
n = 1200
cnt = sum(1 for i in range(n) for j in range(n) if (lambda px, py: px * px + py * py < 4 * py and px * px + py * py > 4)(-2.2 + (i + .5) * 4.4 / n, (j + .5) * 4.4 / n))
assert abs(cnt * (4.4 / n) ** 2 - float(A)) < 0.02
# ----------------------------------------------------------------------------------------------

write(9, [
("parametric-derivatives", r"""
### The idea
A parametric curve gives $x$ and $y$ separately as functions of a parameter $t$. You find the slope of the curve by comparing how fast $y$ changes with how fast $x$ changes.

### Key facts
- **Slope:** $\dfrac{dy}{dx} = \dfrac{dy/dt}{dx/dt}$, as long as $\dfrac{dx}{dt} \ne 0$.
- **Horizontal tangent:** $\dfrac{dy}{dt} = 0$ and $\dfrac{dx}{dt} \ne 0$. **Vertical tangent:** $\dfrac{dx}{dt} = 0$ and $\dfrac{dy}{dt} \ne 0$.
- **Second derivative:** $\dfrac{d^2y}{dx^2} = \dfrac{\dfrac{d}{dt}\left(\dfrac{dy}{dx}\right)}{dx/dt}$. Differentiate the slope with respect to $t$, then divide by $\dfrac{dx}{dt}$. Its sign gives concavity.
- **Tangent line:** find the point $(x(t_0), y(t_0))$, the slope at $t_0$, and use point-slope form.
- **Eliminating the parameter:** solve one equation for $t$ and substitute into the other.

### Watch out for
Dividing the derivatives the wrong way round, and forgetting that the second derivative needs a second division by $\frac{dx}{dt}$.

### Worked example
For $x = t^2$ and $y = t^3 - 3t$, find $\dfrac{dy}{dx}$ and $\dfrac{d^2y}{dx^2}$ at $t = 2$.

$$\frac{dy}{dx} = \frac{3t^2 - 3}{2t} = \frac{3t}{2} - \frac{3}{2t}$$

At $t = 2$ this is $3 - \frac34 = \frac94$. Next, $\dfrac{d}{dt}\left(\dfrac{3t}{2} - \dfrac{3}{2t}\right) = \dfrac32 + \dfrac{3}{2t^2}$, which is $\dfrac{15}{8}$ at $t = 2$. Dividing by $\dfrac{dx}{dt} = 4$:

$$\frac{d^2y}{dx^2}\Big|_{t=2} = \frac{15/8}{4} = \frac{15}{32} > 0$$

so the curve is concave up there.
"""),
("parametric-arc-length", r"""
### The idea
A particle moving along a parametric curve covers a tiny distance $\sqrt{dx^2 + dy^2}$ in each tiny time $dt$. The length of the curve is the total of those distances, which is the integral of the particle's speed.

### Key facts
- **Arc length:** $\displaystyle L = \int_a^b \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2}\,dt$.
- The integrand is the **speed**. For a straight line at constant speed, the length is speed times time.
- Designed problems make $(x')^2 + (y')^2$ a perfect square, or factor to something like $t\sqrt{1 + t^2}$ that a substitution handles. Otherwise use a calculator and show the integral.
- Distance traveled is not displacement. Displacement comes from the integrals of $x'$ and $y'$ separately, and its length is at most the distance traveled.

### Watch out for
Leaving out the square root, using $x$ and $y$ instead of $x'$ and $y'$, and adding the integrals of $|x'|$ and $|y'|$.

### Worked example
Find the length of the arc $x = \cos^3 t$, $y = \sin^3 t$ for $0 \le t \le \dfrac\pi2$.

$x' = -3\cos^2 t \sin t$ and $y' = 3\sin^2 t\cos t$, so

$$
\begin{aligned}
(x')^2 + (y')^2 &= 9\sin^2 t\cos^2 t(\cos^2 t + \sin^2 t) \\
&= 9\sin^2 t\cos^2 t
\end{aligned}
$$

The speed is $3\sin t\cos t$ on this interval (both factors are nonnegative), so

$$L = \int_0^{\pi/2} 3\sin t\cos t\,dt = \left[\frac32\sin^2 t\right]_0^{\pi/2} = \frac32$$
"""),
("vector-valued-functions", r"""
### The idea
A vector-valued function $\vec r(t) = \langle x(t), y(t)\rangle$ packages two coordinate functions into one object that describes the position of a particle at time $t$. Calculus on it works one component at a time.

### Key facts
- **Velocity** is $\vec v(t) = \vec r\,'(t) = \langle x'(t), y'(t)\rangle$, **speed** is its magnitude $\sqrt{(x')^2 + (y')^2}$, and **acceleration** is $\vec a(t) = \vec v\,'(t) = \vec r\,''(t)$.
- **Integrals** are taken component by component: $\displaystyle\int \langle f, g\rangle\,dt = \left\langle \int f\,dt, \int g\,dt\right\rangle$.
- **Position from velocity:** $\vec r(t) = \vec r(0) + \displaystyle\int_0^t \vec v(s)\,ds$. The initial position supplies the constants of integration.
- **Limits** are also taken component by component.
- The velocity vector points along the path; its slope $\dfrac{y'}{x'}$ is the slope of the tangent line.

### Watch out for
Forgetting the initial position (or initial velocity, when starting from acceleration), and giving a vector where the question asks for a number such as speed.

### Worked example
A particle has velocity $\vec v(t) = \langle \cos t, 2t\rangle$ and position $\langle 0, 3\rangle$ at $t = 0$. Find its position at $t = \dfrac\pi2$.

Integrate each component: $x(t) = \sin t + C_1$ with $x(0) = 0$ gives $x = \sin t$, and $y(t) = t^2 + C_2$ with $y(0) = 3$ gives $y = t^2 + 3$. So

$$
\begin{aligned}
\vec r(t) &= \langle \sin t,\ t^2 + 3\rangle \\
\vec r\left(\frac\pi2\right) &= \left\langle 1,\ \frac{\pi^2}{4} + 3\right\rangle
\end{aligned}
$$
"""),
("motion-in-the-plane", r"""
### The idea
When a particle moves in a plane, position, velocity and acceleration are vectors. The questions are about where it is, how fast it moves, which way it goes, and whether it is speeding up.

### Key facts
- **Direction:** the particle moves right when $x' > 0$ and left when $x' < 0$; up when $y' > 0$ and down when $y' < 0$.
- **Speed** is $|\vec v| = \sqrt{(x')^2 + (y')^2}$. It is **increasing** when $\vec v\cdot\vec a > 0$ and **decreasing** when $\vec v\cdot\vec a < 0$. A positive acceleration component alone does not tell you this.
- **Distance traveled** from $t = a$ to $t = b$ is $\displaystyle\int_a^b |\vec v(t)|\,dt$. **Displacement** is $\vec r(b) - \vec r(a)$.
- **Position:** $\vec r(t) = \vec r(a) + \displaystyle\int_a^t \vec v(s)\,ds$, and one more integration with an initial velocity if you start from acceleration.
- Speed can be minimal or maximal at times where $\vec v\cdot\vec a = 0$.

### Watch out for
Mixing up speed (a number) with velocity (a vector), and treating the length of the displacement as the distance traveled.

### Worked example
A particle has velocity $\vec v(t) = \langle 4 - t^2, t\rangle$. At $t = 1$, is it speeding up or slowing down?

$\vec v(1) = \langle 3, 1\rangle$ and $\vec a(t) = \langle -2t, 1\rangle$, so $\vec a(1) = \langle -2, 1\rangle$. Then

$$\vec v(1)\cdot\vec a(1) = (3)(-2) + (1)(1) = -5 < 0$$

so the speed, $\sqrt{10}$ at that moment, is decreasing.
"""),
("polar-coordinates-and-derivatives", r"""
### The idea
A point in polar coordinates $(r, \theta)$ is described by its distance from the origin and the angle from the positive $x$-axis. A polar curve $r = f(\theta)$ is a parametric curve with parameter $\theta$, so its slope is found like any parametric slope.

### Key facts
- **Conversions:** $x = r\cos\theta$, $y = r\sin\theta$, $r^2 = x^2 + y^2$, $\tan\theta = \dfrac yx$ (check the quadrant).
- **Slope:** from $x = f(\theta)\cos\theta$ and $y = f(\theta)\sin\theta$,
  $$\frac{dy}{dx} = \frac{f'(\theta)\sin\theta + f(\theta)\cos\theta}{f'(\theta)\cos\theta - f(\theta)\sin\theta}$$
- **Horizontal tangent:** numerator zero (and denominator not). **Vertical tangent:** denominator zero (and numerator not).
- At the **pole** ($r = 0$), if $f'(\theta_0) \ne 0$, the tangent line is the line $\theta = \theta_0$.
- $\frac{dr}{d\theta}$ measures how the distance from the origin changes as $\theta$ increases. It is not the slope of the curve.

### Watch out for
Using $\tan\theta$ as the slope of the curve, and sign slips in the product rule.

### Worked example
For $r = 1 + \sin\theta$, find the tangent direction at $\theta = \dfrac\pi6$.

Here $r = \frac32$ and $r' = \cos\theta = \frac{\sqrt3}{2}$. Then

$$
\begin{aligned}
\frac{dy}{d\theta} &= r'\sin\theta + r\cos\theta \\
&= \frac{\sqrt3}{4} + \frac{3\sqrt3}{4} = \sqrt3
\end{aligned}
$$

$$\frac{dx}{d\theta} = r'\cos\theta - r\sin\theta = \frac34 - \frac34 = 0$$

The numerator is nonzero and the denominator is zero, so the tangent line there is **vertical**.
"""),
("area-in-polar-coordinates", r"""
### The idea
In polar coordinates the natural slice is a thin pie wedge, not a rectangle. A wedge with radius $r$ and angle $d\theta$ has area $\frac12 r^2\,d\theta$.

### Key facts
- **One curve:** $\displaystyle A = \frac12\int_\alpha^\beta r^2\,d\theta$, over an interval where the curve is traced once.
- **Between two curves:** $\displaystyle A = \frac12\int_\alpha^\beta \left(r_{\text{out}}^2 - r_{\text{in}}^2\right)d\theta$. It is the squares that are subtracted, not the radii.
- **Limits:** the angles where $r = 0$ bound a petal. The angles where two curves meet, found by setting the radii equal, bound the region between them. A sketch shows which curve is outer.
- **Symmetry** can halve the work: integrate over half the region and double.
- Useful identities: $\cos^2\theta = \dfrac{1 + \cos2\theta}{2}$ and $\sin^2\theta = \dfrac{1 - \cos2\theta}{2}$.

### Watch out for
Leaving out the $\frac12$, integrating over an interval that traces the curve twice (for example $r = 2\cos\theta$ over $[0, 2\pi]$), and using the wrong curve as outer.

### Worked example
Find the area inside $r = 4\sin\theta$ and outside $r = 2$.

The curves meet where $4\sin\theta = 2$, so $\theta = \dfrac\pi6$ and $\dfrac{5\pi}6$. Between these angles $r = 4\sin\theta$ is farther out:

$$\begin{aligned}A &= \frac12\int_{\pi/6}^{5\pi/6}\left(16\sin^2\theta - 4\right)d\theta \\ &= \frac12\Big[4\theta - 4\sin2\theta\Big]_{\pi/6}^{5\pi/6} \\ &= \frac12\left(\frac{8\pi}{3} + 4\sqrt3\right) = \frac{4\pi}{3} + 2\sqrt3\end{aligned}$$
"""),
])
