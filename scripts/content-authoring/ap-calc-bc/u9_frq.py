"""Unit 9 free-response prompts (9 points each, in the style of the AP exam)."""
from lib import *

R = Rational
T_PD, T_AL, T_VV, T_MP, T_PC, T_PA = (
    "parametric-derivatives", "parametric-arc-length", "vector-valued-functions",
    "motion-in-the-plane", "polar-coordinates-and-derivatives", "area-in-polar-coordinates",
)


def add(B):
    # 1. parametric curve: slope, vertical tangent, concavity
    xt, yt = t**2 - 2 * t, t**3 - 12 * t
    first = diff(yt, t) / diff(xt, t)
    assert first.subs(t, 3) == R(15, 4)
    second = simplify(diff(first, t) / diff(xt, t))
    assert simplify(second - (6 * t**2 - 12 * t + 24) / (2 * t - 2) ** 3) == 0 and second.subs(t, 3) == R(21, 32)
    assert (xt.subs(t, 1), yt.subs(t, 1)) == (-1, -11) and diff(yt, t).subs(t, 1) == -9
    B.frq(T_PD,
          "A curve $C$ is defined by the parametric equations $x(t)=t^2-2t$ and $y(t)=t^3-12t$.\n\n**(a)** Find $\\dfrac{dy}{dx}$ in terms of $t$, and find its value at $t=3$.\n\n**(b)** The curve has a vertical tangent line at one point. Find the point, and write an equation of that tangent line.\n\n**(c)** Find $\\dfrac{d^2y}{dx^2}$ at $t=3$. Is the curve concave up or concave down there? Give a reason.",
          [(1, "(a) $\\frac{dy}{dx}=\\frac{dy/dt}{dx/dt}=\\frac{3t^2-12}{2t-2}$"),
           (1, "(a) At $t=3$: $\\frac{15}{4}$"),
           (1, "(b) Sets $\\frac{dx}{dt}=2t-2=0$ and gets $t=1$"),
           (1, "(b) Checks $\\frac{dy}{dt}=-9\\ne0$ at $t=1$ and finds the point $(-1,-11)$"),
           (1, "(b) Equation of the vertical line: $x=-1$"),
           (1, "(c) Differentiates $\\frac{dy}{dx}$ with respect to $t$ (quotient rule)"),
           (1, "(c) Divides by $\\frac{dx}{dt}$: $\\frac{d^2y}{dx^2}=\\frac{6t^2-12t+24}{(2t-2)^3}$"),
           (1, "(c) Value $\\frac{21}{32}$ at $t=3$"),
           (1, "(c) Concave up, because $\\frac{d^2y}{dx^2}>0$")],
          "(a) $\\frac{dy}{dx}=\\frac{3t^2-12}{2t-2}$; at $t=3$ this is $\\frac{15}{4}$.\n(b) $\\frac{dx}{dt}=0$ when $t=1$, and $\\frac{dy}{dt}=3-12=-9\\ne0$. The point is $(x(1),y(1))=(-1,-11)$ and the vertical tangent line is $x=-1$.\n(c) $\\frac{d}{dt}\\left(\\frac{dy}{dx}\\right)=\\frac{6t(2t-2)-2(3t^2-12)}{(2t-2)^2}=\\frac{6t^2-12t+24}{(2t-2)^2}$. Dividing by $\\frac{dx}{dt}=2t-2$: $\\frac{d^2y}{dx^2}=\\frac{6t^2-12t+24}{(2t-2)^3}$. At $t=3$: $\\frac{42}{64}=\\frac{21}{32}>0$, so the curve is concave up.")

    # 2. vector motion
    v = Matrix([t**2 - 4, 2 * t])
    a = v.diff(t)
    assert list(a.subs(t, 1)) == [2, 2] and v.subs(t, 1).norm() == sqrt(13) and (v.T * a)[0].subs(t, 1) == -2
    pos3 = Matrix([0, 3]) + v.applyfunc(lambda e: integrate(e, (t, 0, 3)))
    assert list(pos3) == [-3, 12]
    assert solve(v[0], t) == [-2, 2]
    B.frq(T_MP,
          "A particle moves in the $xy$-plane with velocity vector $\\vec v(t)=\\langle t^2-4,\\,2t\\rangle$ for $t\\ge0$. At time $t=0$ the particle is at the point $(0,3)$.\n\n**(a)** Find the acceleration vector and the speed of the particle at $t=1$.\n\n**(b)** Is the speed of the particle increasing or decreasing at $t=1$? Give a reason for your answer.\n\n**(c)** Find the position of the particle at $t=3$.\n\n**(d)** At what time $t>0$ is the particle moving straight up or straight down?",
          [(1, "(a) Acceleration $\\vec a(t)=\\langle2t,2\\rangle$, so $\\vec a(1)=\\langle2,2\\rangle$"),
           (1, "(a) Speed $=\\sqrt{(-3)^2+2^2}=\\sqrt{13}$"),
           (1, "(b) Computes $\\vec v(1)\\cdot\\vec a(1)=(-3)(2)+(2)(2)=-2$"),
           (1, "(b) Decreasing, because the dot product is negative"),
           (1, "(c) Integrates each component of the velocity with a constant of integration (or uses the limits 0 to 3)"),
           (1, "(c) Uses the initial position $(0,3)$"),
           (1, "(c) Position $(-3,12)$"),
           (1, "(d) $x'(t)=t^2-4=0$ gives $t=2$"),
           (1, "(d) Checks $y'(2)=4\\ne0$ and answers $t=2$")],
          "(a) $\\vec a(t)=\\vec v\\,'(t)=\\langle2t,2\\rangle$, so $\\vec a(1)=\\langle2,2\\rangle$. $\\vec v(1)=\\langle-3,2\\rangle$, so the speed is $\\sqrt{9+4}=\\sqrt{13}$.\n(b) $\\vec v(1)\\cdot\\vec a(1)=-6+4=-2<0$, so the speed is decreasing.\n(c) $x(3)=0+\\int_0^3\\left(t^2-4\\right)dt=9-12=-3$ and $y(3)=3+\\int_0^32t\\,dt=3+9=12$. The position is $(-3,12)$.\n(d) The particle moves vertically when $x'(t)=0$ and $y'(t)\\ne0$: $t^2-4=0$ gives $t=2$ (for $t>0$), and $y'(2)=4\\ne0$.")

    # 3. polar area and slope
    area = integrate((4 * cos(t) ** 2 - 1) / 2, (t, -pi / 3, pi / 3))
    assert simplify(area - (pi / 3 + sqrt(3) / 2)) == 0
    sl = simplify((diff(2 * cos(t), t) * sin(t) + 2 * cos(t) * cos(t)) / (diff(2 * cos(t), t) * cos(t) - 2 * cos(t) * sin(t))).subs(t, pi / 3)
    assert simplify(sl - sqrt(3) / 3) == 0
    B.frq(T_PA,
          "The graphs of the polar curves $r=2\\cos\\theta$ and $r=1$ are both circles. Let $R$ be the region that lies inside the graph of $r=2\\cos\\theta$ and outside the graph of $r=1$.\n\n**(a)** Find the two values of $\\theta$, with $-\\frac\\pi2<\\theta<\\frac\\pi2$, at which the graphs intersect.\n\n**(b)** Write an integral expression for the area of $R$, and find the area.\n\n**(c)** Find $\\dfrac{dy}{dx}$ for the curve $r=2\\cos\\theta$ at $\\theta=\\dfrac\\pi3$.",
          [(1, "(a) Sets $2\\cos\\theta=1$"),
           (1, "(a) $\\theta=\\pm\\frac\\pi3$"),
           (1, "(b) Integrand $\\frac12\\left(4\\cos^2\\theta-1\\right)$ (outer radius squared minus inner radius squared)"),
           (1, "(b) Limits $-\\frac\\pi3$ to $\\frac\\pi3$ (or twice the integral from 0 to $\\frac\\pi3$)"),
           (1, "(b) Antiderivative using $\\cos^2\\theta=\\frac{1+\\cos2\\theta}{2}$"),
           (1, "(b) Area $=\\frac\\pi3+\\frac{\\sqrt3}{2}$"),
           (1, "(c) $\\frac{dy}{d\\theta}=r'\\sin\\theta+r\\cos\\theta$ and $\\frac{dx}{d\\theta}=r'\\cos\\theta-r\\sin\\theta$ with $r=2\\cos\\theta$, $r'=-2\\sin\\theta$"),
           (1, "(c) At $\\theta=\\frac\\pi3$: $\\frac{dy}{d\\theta}=2\\cos\\frac{2\\pi}{3}=-1$ and $\\frac{dx}{d\\theta}=-2\\sin\\frac{2\\pi}{3}=-\\sqrt3$ (or the slope $-\\cot2\\theta$)"),
           (1, "(c) $\\frac{dy}{dx}=\\frac{\\sqrt3}{3}$")],
          "(a) $2\\cos\\theta=1$ gives $\\cos\\theta=\\frac12$, so $\\theta=\\pm\\frac\\pi3$.\n(b) $A=\\frac12\\int_{-\\pi/3}^{\\pi/3}\\left(4\\cos^2\\theta-1\\right)d\\theta=\\frac12\\int_{-\\pi/3}^{\\pi/3}\\left(1+2\\cos2\\theta\\right)d\\theta=\\frac12\\left[\\theta+\\sin2\\theta\\right]_{-\\pi/3}^{\\pi/3}=\\frac12\\left(\\frac{2\\pi}{3}+\\sqrt3\\right)=\\frac\\pi3+\\frac{\\sqrt3}{2}$.\n(c) With $r=2\\cos\\theta$ and $r'=-2\\sin\\theta$: $\\frac{dy}{d\\theta}=-2\\sin^2\\theta+2\\cos^2\\theta=2\\cos2\\theta$ and $\\frac{dx}{d\\theta}=-2\\sin\\theta\\cos\\theta-2\\cos\\theta\\sin\\theta=-2\\sin2\\theta$. At $\\theta=\\frac\\pi3$: $\\frac{dy}{dx}=\\frac{2\\cos\\frac{2\\pi}3}{-2\\sin\\frac{2\\pi}3}=\\frac{-1}{-\\sqrt3}=\\frac{\\sqrt3}{3}$.")

    # 4. limacon
    rf = 3 - 2 * cos(t)
    sl = simplify((diff(rf, t) * sin(t) + rf * cos(t)) / (diff(rf, t) * cos(t) - rf * sin(t))).subs(t, pi / 2)
    assert sl == -R(2, 3)
    assert integrate(rf, (t, 0, pi)) / pi == 3 and simplify(integrate(rf**2 / 2, (t, 0, 2 * pi)) - 11 * pi) == 0
    B.frq(T_PC,
          "Consider the polar curve $r=3-2\\cos\\theta$ for $0\\le\\theta\\le2\\pi$.\n\n**(a)** Find $\\dfrac{dy}{dx}$ at $\\theta=\\dfrac\\pi2$.\n\n**(b)** For what values of $\\theta$ in $(0,2\\pi)$ is the distance from the curve to the origin increasing? Justify your answer.\n\n**(c)** Find the average value of $r$ for $0\\le\\theta\\le\\pi$.\n\n**(d)** Find the area enclosed by the curve.",
          [(1, "(a) $r=3$ and $r'=2\\sin\\theta=2$ at $\\theta=\\frac\\pi2$"),
           (1, "(a) $\\frac{dy}{d\\theta}=r'\\sin\\theta+r\\cos\\theta=2$ and $\\frac{dx}{d\\theta}=r'\\cos\\theta-r\\sin\\theta=-3$"),
           (1, "(a) $\\frac{dy}{dx}=-\\frac23$"),
           (1, "(b) $\\frac{dr}{d\\theta}=2\\sin\\theta$"),
           (1, "(b) Increasing on $(0,\\pi)$, because $\\frac{dr}{d\\theta}>0$ there"),
           (1, "(c) $\\frac1\\pi\\int_0^\\pi(3-2\\cos\\theta)\\,d\\theta$"),
           (1, "(c) Value 3"),
           (1, "(d) $\\frac12\\int_0^{2\\pi}(3-2\\cos\\theta)^2d\\theta$"),
           (1, "(d) Area $=11\\pi$")],
          "(a) At $\\theta=\\frac\\pi2$: $r=3$, $r'=2\\sin\\theta=2$. $\\frac{dy}{d\\theta}=2\\cdot1+3\\cdot0=2$ and $\\frac{dx}{d\\theta}=2\\cdot0-3\\cdot1=-3$, so $\\frac{dy}{dx}=-\\frac23$.\n(b) The distance from the origin is $|r|=r$ (since $r\\ge1>0$), and $\\frac{dr}{d\\theta}=2\\sin\\theta>0$ for $0<\\theta<\\pi$. So the distance is increasing on $(0,\\pi)$.\n(c) $\\frac1\\pi\\int_0^\\pi(3-2\\cos\\theta)\\,d\\theta=\\frac1\\pi\\left[3\\theta-2\\sin\\theta\\right]_0^\\pi=3$.\n(d) $A=\\frac12\\int_0^{2\\pi}\\left(9-12\\cos\\theta+4\\cos^2\\theta\\right)d\\theta=\\frac12\\left(18\\pi-0+4\\pi\\right)=11\\pi$.")

    # 5. parametric: slope, vertical tangents, length by calculator
    x_, y_ = t + 2 * sin(t), 2 * cos(t)
    assert simplify((diff(y_, t) / diff(x_, t)).subs(t, pi / 3) + sqrt(3) / 2) == 0
    assert solve(Eq(diff(x_, t), 0), t) and abs(float(diff(x_, t).subs(t, 2 * pi / 3))) < 1e-12
    ln = N(Integral(sqrt(diff(x_, t) ** 2 + diff(y_, t) ** 2), (t, 0, 2 * pi)), 12)
    ln_txt = num(ln)
    assert simplify(diff(x_, t) ** 2 + diff(y_, t) ** 2 - (5 + 4 * cos(t))) == 0
    B.frq(T_AL,
          "A particle moves along a curve in the plane with position $\\left(x(t),y(t)\\right)=\\left(t+2\\sin t,\;2\\cos t\\right)$ for $0\\le t\\le2\\pi$.\n\n**(a)** Find $\\dfrac{dy}{dx}$ at $t=\\dfrac\\pi3$.\n\n**(b)** Find all values of $t$ in $(0,2\\pi)$ at which the particle's path has a vertical tangent line.\n\n**(c)** A graphing calculator may be used. Write an integral expression for the total distance the particle travels from $t=0$ to $t=2\\pi$, and find its value.",
          [(1, "(a) $\\frac{dx}{dt}=1+2\\cos t$ and $\\frac{dy}{dt}=-2\\sin t$"),
           (1, "(a) $\\frac{dy}{dx}=\\frac{-2\\sin t}{1+2\\cos t}=-\\frac{\\sqrt3}{2}$ at $t=\\frac\\pi3$"),
           (1, "(b) Sets $1+2\\cos t=0$, so $\\cos t=-\\frac12$"),
           (1, "(b) $t=\\frac{2\\pi}{3}$ and $t=\\frac{4\\pi}{3}$"),
           (1, "(b) Checks $\\frac{dy}{dt}\\ne0$ at both values"),
           (1, "(c) Integrand $\\sqrt{(1+2\\cos t)^2+(-2\\sin t)^2}$ (equivalently $\\sqrt{5+4\\cos t}$)"),
           (1, "(c) Limits 0 to $2\\pi$"),
           (1, "(c) Evaluates the integral with the calculator"),
           (1, f"(c) Distance $\\approx{ln_txt}$")],
          f"(a) At $t=\\frac\\pi3$: $\\frac{{dy}}{{dx}}=\\frac{{-2\\sin\\frac\\pi3}}{{1+2\\cos\\frac\\pi3}}=\\frac{{-\\sqrt3}}{{2}}$.\n(b) $\\frac{{dx}}{{dt}}=1+2\\cos t=0$ when $\\cos t=-\\frac12$, so $t=\\frac{{2\\pi}}{{3}}$ or $t=\\frac{{4\\pi}}{{3}}$. At both, $\\frac{{dy}}{{dt}}=-2\\sin t=\\mp\\sqrt3\\ne0$.\n(c) Distance $=\\int_0^{{2\\pi}}\\sqrt{{(1+2\\cos t)^2+4\\sin^2t}}\\,dt=\\int_0^{{2\\pi}}\\sqrt{{5+4\\cos t}}\\,dt\\approx{ln_txt}$.")
