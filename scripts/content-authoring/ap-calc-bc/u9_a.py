"""Unit 9, parametric derivatives and parametric arc length."""
from lib import *

R = Rational
T_PD, T_AL = "parametric-derivatives", "parametric-arc-length"


def add(B):
    # ------------------------------------------------------------ derivatives of parametric equations
    xt, yt = t**2, t**3
    dydx = simplify(diff(yt, t) / diff(xt, t))
    assert dydx.subs(t, 2) == 3
    B.mcq(T_PD, "A curve is given by $x(t)=t^2$ and $y(t)=t^3$. What is $\\dfrac{dy}{dx}$ at $t=2$?",
          ch(3, "$\\frac{dy}{dx}=\\frac{dy/dt}{dx/dt}=\\frac{3t^2}{2t}=\\frac{3t}{2}$, which is 3 at $t=2$."),
          [ch(12, "This is $\\frac{dy}{dt}=3t^2$ at $t=2$. The slope divides by $\\frac{dx}{dt}$."),
           ch(R(1, 3), "This is $\\frac{dx/dt}{dy/dt}=\\frac{4}{12}$, the reciprocal of the slope."),
           ch(8, "This subtracts the derivatives ($12-4$). The slope is their quotient.")],
          "For parametric equations, $\\frac{dy}{dx}=\\frac{dy/dt}{dx/dt}$ provided $\\frac{dx}{dt}\\ne0$.", difficulty="easy")

    dydx = simplify(diff(2 * sin(t), t) / diff(3 * cos(t), t))
    assert simplify(dydx.subs(t, pi / 4) + R(2, 3)) == 0
    B.mcq(T_PD, "A curve is given by $x(t)=3\\cos t$ and $y(t)=2\\sin t$. What is $\\dfrac{dy}{dx}$ at $t=\\dfrac\\pi4$?",
          ch(-R(2, 3), "$\\frac{dy}{dx}=\\frac{2\\cos t}{-3\\sin t}=-\\frac23\\cot t$. At $t=\\frac\\pi4$, $\\cot t=1$, so the slope is $-\\frac23$."),
          [ch(R(2, 3), "$\\frac{dx}{dt}=-3\\sin t$ is negative. Leaving out the minus sign gives the wrong sign."),
           ch(-R(3, 2), "This is the reciprocal: $\\frac{dx/dt}{dy/dt}$ rather than $\\frac{dy/dt}{dx/dt}$."),
           ch(-1, "At $t=\\frac\\pi4$, $\\sin t=\\cos t$, so the ratio $\\frac{\\cos t}{\\sin t}$ is 1, but the coefficients 2 and 3 still matter.")],
          "Differentiate each coordinate with respect to $t$ and divide: the coefficients 2 and 3 stay in the quotient.", difficulty="easy")

    # horizontal tangent: dy/dt = 0 and dx/dt != 0
    xt, yt = t**3 - 3 * t, t**2 - 4 * t
    assert solve(diff(yt, t), t) == [2] and diff(xt, t).subs(t, 2) == 9
    B.mcq(T_PD, "A curve is given by $x(t)=t^3-3t$ and $y(t)=t^2-4t$. At what value of $t$ does the curve have a horizontal tangent line?",
          ch(2, "A horizontal tangent needs $\\frac{dy}{dt}=2t-4=0$, so $t=2$, and $\\frac{dx}{dt}=3t^2-3=9\\ne0$ there."),
          [ch("$t=-1$ and $t=1$", "At $t=\\pm1$, $\\frac{dx}{dt}=3t^2-3=0$ while $\\frac{dy}{dt}\\ne0$. Those are vertical tangents."),
           ch(0, "At $t=0$ the curve passes through the origin, but $\\frac{dy}{dt}=-4\\ne0$, so the tangent is not horizontal."),
           ch(4, "$t=4$ is where $y=0$. A horizontal tangent comes from $\\frac{dy}{dt}=0$, not from $y=0$.")],
          "The tangent is horizontal where $\\frac{dy}{dt}=0$ and $\\frac{dx}{dt}\\ne0$, and vertical where $\\frac{dx}{dt}=0$ and $\\frac{dy}{dt}\\ne0$.", difficulty="medium")

    xt, yt = t**2 - 4 * t + 1, t**3 - 3 * t
    assert solve(diff(xt, t), t) == [2] and diff(yt, t).subs(t, 2) == 9
    B.mcq(T_PD, "A curve is given by $x(t)=t^2-4t+1$ and $y(t)=t^3-3t$. At what value of $t$ does the curve have a vertical tangent line?",
          ch(2, "A vertical tangent needs $\\frac{dx}{dt}=2t-4=0$, so $t=2$, and $\\frac{dy}{dt}=3t^2-3=9\\ne0$ there."),
          [ch("$t=-1$ and $t=1$", "At $t=\\pm1$, $\\frac{dy}{dt}=0$ while $\\frac{dx}{dt}\\ne0$. Those are horizontal tangents."),
           ch(0, "$\\frac{dx}{dt}=-4$ at $t=0$, not 0."),
           ch(4, "$t=4$ gives $x=1$, but $\\frac{dx}{dt}=4\\ne0$ there.")],
          "The tangent is vertical where $\\frac{dx}{dt}=0$ and $\\frac{dy}{dt}\\ne0$.", difficulty="medium")

    # tangent line equation
    xt, yt = t**2 + 1, t**3 - t
    px, py, m = xt.subs(t, 2), yt.subs(t, 2), (diff(yt, t) / diff(xt, t)).subs(t, 2)
    assert (px, py, m) == (5, 6, R(11, 4))
    B.mcq(T_PD, "A curve is given by $x(t)=t^2+1$ and $y(t)=t^3-t$. Which is an equation of the line tangent to the curve at $t=2$?",
          ch("$y-6=\\frac{11}{4}(x-5)$", "At $t=2$ the point is $(5,6)$ and the slope is $\\frac{3t^2-1}{2t}=\\frac{11}{4}$."),
          [ch("$y-6=11(x-5)$", "11 is $\\frac{dy}{dt}$ at $t=2$. The slope divides by $\\frac{dx}{dt}=4$."),
           ch("$y-6=\\frac{4}{11}(x-5)$", "This uses the reciprocal slope, $\\frac{dx/dt}{dy/dt}$."),
           ch("$y-5=\\frac{11}{4}(x-6)$", "The point is $(x,y)=(5,6)$. This swaps the coordinates.")],
          "Find the point from $x(t_0),y(t_0)$, the slope from $\\frac{dy/dt}{dx/dt}$ at $t_0$, then use point-slope form.", difficulty="medium")

    # second derivative
    xt, yt = t**2, t**3
    first = diff(yt, t) / diff(xt, t)
    second = simplify(diff(first, t) / diff(xt, t))
    assert second == 3 / (4 * t) and second.subs(t, 2) == R(3, 8)
    wrong1 = diff(first, t).subs(t, 2)
    wrong2 = (diff(yt, t, 2) / diff(xt, t, 2)).subs(t, 2)
    wrong3 = (diff(first, t) / diff(xt, t) ** 2).subs(t, 2)
    assert (wrong1, wrong2, wrong3) == (R(3, 2), 6, R(3, 32))
    B.mcq(T_PD, "A curve is given by $x(t)=t^2$ and $y(t)=t^3$ for $t>0$. What is $\\dfrac{d^2y}{dx^2}$ at $t=2$?",
          ch(R(3, 8), "$\\frac{dy}{dx}=\\frac{3t}{2}$. Then $\\frac{d^2y}{dx^2}=\\frac{\\frac{d}{dt}\\left(\\frac{dy}{dx}\\right)}{dx/dt}=\\frac{3/2}{2t}=\\frac{3}{4t}$, which is $\\frac38$ at $t=2$."),
          [ch(R(3, 2), "This is $\\frac{d}{dt}\\left(\\frac{dy}{dx}\\right)$. The second derivative with respect to $x$ divides it by $\\frac{dx}{dt}$."),
           ch(6, "This is $\\frac{d^2y/dt^2}{d^2x/dt^2}$, which is not a valid formula for $\\frac{d^2y}{dx^2}$."),
           ch(R(3, 32), "This divides by $\\left(\\frac{dx}{dt}\\right)^2$ instead of $\\frac{dx}{dt}$.")],
          "For $\\frac{d^2y}{dx^2}$: differentiate $\\frac{dy}{dx}$ with respect to $t$, then divide by $\\frac{dx}{dt}$.", difficulty="medium")

    xt, yt = t**3, t**2
    first = diff(yt, t) / diff(xt, t)
    second = simplify(diff(first, t) / diff(xt, t))
    assert second.subs(t, 1) == -R(2, 9)
    B.mcq(T_PD, "A curve is given by $x(t)=t^3$ and $y(t)=t^2$ for $t>0$. What is $\\dfrac{d^2y}{dx^2}$ at $t=1$, and what does its sign tell you?",
          ch("$-\\frac29$, so the curve is concave down", "$\\frac{dy}{dx}=\\frac{2t}{3t^2}=\\frac{2}{3t}$. Then $\\frac{d^2y}{dx^2}=\\frac{-\\frac{2}{3t^2}}{3t^2}=-\\frac{2}{9t^4}$, which is $-\\frac29$ at $t=1$. Negative means concave down."),
          [ch("$-\\frac23$, so the curve is concave down", "$-\\frac23$ is $\\frac{d}{dt}\\left(\\frac{dy}{dx}\\right)$ at $t=1$. It must be divided by $\\frac{dx}{dt}=3t^2=3$."),
           ch("$\\frac29$, so the curve is concave up", "The sign was lost: $\\frac{d}{dt}\\left(\\frac{2}{3t}\\right)=-\\frac{2}{3t^2}<0$."),
           ch("$-\\frac{2}{27}$, so the curve is concave down", "This divides by $\\left(\\frac{dx}{dt}\\right)^2$ instead of $\\frac{dx}{dt}$.")],
          "Concavity of a parametric curve is the sign of $\\frac{d^2y}{dx^2}=\\frac{d(dy/dx)/dt}{dx/dt}$.", difficulty="medium")

    # eliminate the parameter
    B.mcq(T_PD, "Which Cartesian equation describes the curve $x=2t-1$, $y=t^2+1$?",
          ch("$y=\\frac{(x+1)^2}{4}+1$", "Solve $x=2t-1$ for $t$: $t=\\frac{x+1}{2}$. Then $y=\\left(\\frac{x+1}{2}\\right)^2+1$."),
          [ch("$y=\\frac{(x-1)^2}{4}+1$", "$x=2t-1$ gives $t=\\frac{x+1}{2}$, not $\\frac{x-1}{2}$."),
           ch("$y=(x+1)^2+1$", "$t=\\frac{x+1}{2}$, and squaring it gives $\\frac{(x+1)^2}{4}$. The 2 in the denominator is squared too."),
           ch("$y=\\frac{x^2+1}{4}+1$", "Substituting into $t^2$ needs the whole expression $(x+1)$ squared, not $x^2+1$.")],
          "Solve one equation for $t$ and substitute into the other.", difficulty="easy")

    xt, yt = sin(t), cos(2 * t)
    sl = simplify((diff(yt, t) / diff(xt, t)).subs(t, pi / 6))
    assert sl == -2
    B.mcq(T_PD, "A curve is given by $x(t)=\\sin t$ and $y(t)=\\cos2t$. What is $\\dfrac{dy}{dx}$ at $t=\\dfrac\\pi6$?",
          ch(-2, "$\\frac{dy}{dx}=\\frac{-2\\sin2t}{\\cos t}$. At $t=\\frac\\pi6$: $\\frac{-2\\sin\\frac\\pi3}{\\cos\\frac\\pi6}=\\frac{-2\\cdot\\frac{\\sqrt3}{2}}{\\frac{\\sqrt3}{2}}=-2$."),
          [ch(-sqrt(3), "This is $\\frac{dy}{dt}=-2\\sin2t$ at $t=\\frac\\pi6$. The slope divides by $\\frac{dx}{dt}=\\cos t=\\frac{\\sqrt3}2$."),
           ch(2, "The sign was lost: $\\frac{dy}{dt}=-2\\sin2t$ is negative at $t=\\frac\\pi6$, and $\\frac{dx}{dt}=\\cos t$ is positive."),
           ch(-R(1, 2), "This is the reciprocal of the slope.")],
          "Chain rule for $\\cos2t$: $\\frac{d}{dt}\\cos2t=-2\\sin2t$.", difficulty="medium")

    xt, yt = t**3 - 3 * t, t**4 - 4 * t**2
    horiz = [r_ for r_ in solve(diff(yt, t), t) if diff(xt, t).subs(t, r_) != 0]
    assert len(horiz) == 3
    B.mcq(T_PD, "A curve is given by $x(t)=t^3-3t$ and $y(t)=t^4-4t^2$. For how many values of $t$ does the curve have a horizontal tangent line?",
          ch(3, "$\\frac{dy}{dt}=4t^3-8t=4t\\left(t^2-2\\right)=0$ at $t=0,\\pm\\sqrt2$. At each of these $\\frac{dx}{dt}=3t^2-3\\ne0$ (it is $-3$ and $3$), so all three give horizontal tangents."),
          [ch(2, "This counts only $t=\\pm\\sqrt2$ and misses $t=0$, where $\\frac{dy}{dt}=0$ too."),
           ch(5, "This adds the two values of $t$ where $\\frac{dx}{dt}=0$ ($t=\\pm1$). Those are vertical tangents, not horizontal."),
           ch(4, "$\\frac{dy}{dt}=4t\\left(t^2-2\\right)$ has three zeros, not four.")],
          "Solve $\\frac{dy}{dt}=0$ and then check that $\\frac{dx}{dt}\\ne0$ at each solution.", difficulty="hard")

    xt, yt = 2 * t, t**3 - 3 * t
    assert [r_ for r_ in solve(Eq((diff(yt, t) / diff(xt, t)), 12), t) if r_ > 0] == [3]
    B.mcq(T_PD, "A curve is given by $x(t)=2t$ and $y(t)=t^3-3t$. For $t>0$, at what value of $t$ is the slope of the tangent line equal to 12?",
          ch(3, "$\\frac{dy}{dx}=\\frac{3t^2-3}{2}=12$ gives $3t^2=27$, so $t^2=9$ and $t=3$ for $t>0$."),
          [ch(sqrt(5), "This sets $3t^2-3=12$, leaving out the division by $\\frac{dx}{dt}=2$."),
           ch(9, "$t^2=9$, so $t=3$. The square root has to be taken."),
           ch(5, "This leaves out the division by $\\frac{dx}{dt}=2$ and also stops at $t^2=5$ without taking the square root.")],
          "Write $\\frac{dy}{dx}$ as a function of $t$, set it equal to 12 and solve.", difficulty="hard")

    # ------------------------------------------------------------ arc length of parametric curves
    B.mcq(T_AL, "Which integral gives the length of the curve $x=t^2$, $y=t^3$ for $0\\le t\\le1$?",
          ch("$\\displaystyle\\int_0^1\\sqrt{4t^2+9t^4}\\,dt$", "The length is $\\int\\sqrt{\\left(\\frac{dx}{dt}\\right)^2+\\left(\\frac{dy}{dt}\\right)^2}dt$ with $\\frac{dx}{dt}=2t$ and $\\frac{dy}{dt}=3t^2$."),
          [ch("$\\displaystyle\\int_0^1\\sqrt{2t+3t^2}\\,dt$", "The derivatives $2t$ and $3t^2$ must be squared under the root."),
           ch("$\\displaystyle\\int_0^1\\left(4t^2+9t^4\\right)dt$", "The sum of the squares needs a square root."),
           ch("$\\displaystyle\\int_0^1\\sqrt{t^4+t^6}\\,dt$", "This uses the coordinates $x$ and $y$ instead of their derivatives.")],
          "Arc length of a parametric curve is the integral of the speed, $\\sqrt{(x')^2+(y')^2}$.", difficulty="easy")

    B.mcq(T_AL, "What is the length of the curve $x=3t$, $y=4t$ for $0\\le t\\le2$?",
          ch(10, "$\\sqrt{3^2+4^2}=5$ is constant, so the length is $5\\cdot2=10$. (It is the segment from $(0,0)$ to $(6,8)$.)"),
          [ch(14, "This adds the changes in the coordinates, $6+8$, instead of using the Pythagorean theorem."),
           ch(5, "5 is the speed. Multiply by the length of the $t$-interval, 2."),
           ch(50, "This multiplies the sum of squares by the interval: $25\\cdot2$. The square root is missing.")],
          "A straight line traversed at constant speed has length speed times time.", difficulty="easy")

    B.mcq(T_AL, "What is the length of the curve $x=2\\cos t$, $y=2\\sin t$ for $0\\le t\\le\\pi$?",
          ch(2 * pi, "$\\frac{dx}{dt}=-2\\sin t$ and $\\frac{dy}{dt}=2\\cos t$, so the speed is $\\sqrt{4\\sin^2t+4\\cos^2t}=2$. The length is $2\\cdot\\pi=2\\pi$ (half of a circle of radius 2)."),
          [ch(4 * pi, "That is the full circle, the length for $0\\le t\\le2\\pi$."),
           ch(pi, "The speed is 2, not 1. The length is the speed times the interval length."),
           ch(4, "4 is the diameter, the straight-line distance between the endpoints $(2,0)$ and $(-2,0)$, not the length along the arc.")],
          "The speed on a circle of radius $r$ with parameter $t$ is $r$, so the length is $r\\cdot(\\text{change in }t)$.", difficulty="medium")

    xt, yt = 3 * t**2, 2 * t**3
    ln = integrate(sqrt(diff(xt, t) ** 2 + diff(yt, t) ** 2), (t, 0, 1))
    assert simplify(ln - (4 * sqrt(2) - 2)) == 0
    B.mcq(T_AL, "What is the length of the curve $x=3t^2$, $y=2t^3$ for $0\\le t\\le1$?",
          ch(4 * sqrt(2) - 2, "$\\frac{dx}{dt}=6t$, $\\frac{dy}{dt}=6t^2$. The integrand is $\\sqrt{36t^2+36t^4}=6t\\sqrt{1+t^2}$. With $u=1+t^2$: $\\int_0^16t\\sqrt{1+t^2}\\,dt=2(1+t^2)^{3/2}\\Big|_0^1=2\\left(2\\sqrt2-1\\right)$."),
          [ch(4 * sqrt(2), "This is the antiderivative at $t=1$ only. At $t=0$ it equals 2, which must be subtracted."),
           ch(12 * sqrt(2) - 6, "$\\int6t\\sqrt{1+t^2}\\,dt=6\\cdot\\frac13(1+t^2)^{3/2}$, where $\\frac13=\\frac23\\cdot\\frac12$ comes from integrating $u^{1/2}$ and from $du=2t\\,dt$. This leaves out the $\\frac13$."),
           ch((2 * sqrt(2) - 1) / 3, "The factor 6 from $6t$ was dropped.")],
          "Factor the integrand: $\\sqrt{36t^2+36t^4}=6t\\sqrt{1+t^2}$, then use $u=1+t^2$.", difficulty="medium")

    xt, yt = exp(t), t
    parts = {
        "ok": N(Integral(sqrt(diff(xt, t) ** 2 + diff(yt, t) ** 2), (t, 0, 1))),
        "sum": N(Integral(Abs(diff(xt, t)) + Abs(diff(yt, t)), (t, 0, 1))),
        "coords": N(Integral(sqrt(xt**2 + yt**2), (t, 0, 1))),
        "no_one": N(Integral(sqrt(diff(xt, t) ** 2), (t, 0, 1))),
    }
    tx = {k_: num(v_) for k_, v_ in parts.items()}
    assert len(set(tx.values())) == 4, tx
    B.mcq(T_AL, "A graphing calculator is allowed. What is the length of the curve $x=e^t$, $y=t$ for $0\\le t\\le1$, to three decimal places?",
          ch(f"${tx['ok']}$", f"The length is $\\int_0^1\\sqrt{{e^{{2t}}+1}}\\,dt\\approx{tx['ok']}$."),
          [ch(f"${tx['sum']}$", f"This integrates $|x'|+|y'|=e^t+1$ and gets $e\\approx{tx['sum']}$. Speed is $\\sqrt{{(x')^2+(y')^2}}$, not the sum."),
           ch(f"${tx['coords']}$", f"This integrates $\\sqrt{{x^2+y^2}}$ ($\\approx{tx['coords']}$), the distance from the origin, not the speed."),
           ch(f"${tx['no_one']}$", f"This leaves out the $y'=1$ term under the root, integrating $e^t$ ($\\approx{tx['no_one']}$).")],
          "Set up $\\int_0^1\\sqrt{\\left(\\frac{dx}{dt}\\right)^2+\\left(\\frac{dy}{dt}\\right)^2}\\,dt$ and evaluate it with the calculator. Write the setup as well as the result.", difficulty="medium")

    xt, yt = t - sin(t), 1 - cos(t)
    sp = simplify(sqrt(diff(xt, t) ** 2 + diff(yt, t) ** 2))
    ln = integrate(2 * sin(t / 2), (t, 0, 2 * pi))
    assert ln == 8 and simplify(diff(xt, t) ** 2 + diff(yt, t) ** 2 - 4 * sin(t / 2) ** 2) == 0
    B.mcq(T_AL, "One arch of a cycloid is given by $x=t-\\sin t$, $y=1-\\cos t$ for $0\\le t\\le2\\pi$. What is its length?",
          ch(8, "$\\left(\\frac{dx}{dt}\\right)^2+\\left(\\frac{dy}{dt}\\right)^2=(1-\\cos t)^2+\\sin^2t=2-2\\cos t=4\\sin^2\\frac t2$, so the speed is $2\\sin\\frac t2$ (positive on $[0,2\\pi]$). The length is $\\left[-4\\cos\\frac t2\\right]_0^{2\\pi}=4-(-4)=8$."),
          [ch(4, "This is the antiderivative at $t=2\\pi$ only. At $t=0$ it equals $-4$."),
           ch(16, "The antiderivative of $2\\sin\\frac t2$ is $-4\\cos\\frac t2$. Using $-8\\cos\\frac t2$ would double the result."),
           ch(2 * pi, "$2\\pi$ is the width of the arch, $x(2\\pi)-x(0)$. The arch is longer than its base.")],
          "Use the identity $1-\\cos t=2\\sin^2\\frac t2$ to turn $2-2\\cos t$ into a perfect square.", difficulty="hard")

    xt, yt = t**3, R(3, 2) * t**2
    ln = integrate(sqrt(diff(xt, t) ** 2 + diff(yt, t) ** 2), (t, 0, sqrt(3)))
    assert simplify(ln - 7) == 0
    B.mcq(T_AL, "What is the length of the curve $x=t^3$, $y=\\frac32t^2$ for $0\\le t\\le\\sqrt3$?",
          ch(7, "$\\frac{dx}{dt}=3t^2$, $\\frac{dy}{dt}=3t$. The integrand is $\\sqrt{9t^4+9t^2}=3t\\sqrt{t^2+1}$. With $u=t^2+1$, $\\int3t\\sqrt{t^2+1}\\,dt=\\left(t^2+1\\right)^{3/2}$. From $0$ to $\\sqrt3$: $8-1=7$."),
          [ch(8, "This is the antiderivative at the upper limit only; at $t=0$ it is 1."),
           ch(14, "$\\int3t\\sqrt{t^2+1}\\,dt$ with $du=2t\\,dt$ gives $\\frac32\\int u^{1/2}du=\\left(t^2+1\\right)^{3/2}$. Omitting the $\\frac12$ from $du=2t\\,dt$ doubles it."),
           ch(R(7, 3), "The factor 3 from $3t$ was dropped.")],
          "Factor $3t$ out of the root, then substitute $u=t^2+1$.", difficulty="hard")

    xt, yt = t**2 / 2, t**3 / 3
    ln = integrate(sqrt(diff(xt, t) ** 2 + diff(yt, t) ** 2), (t, 0, sqrt(3)))
    assert simplify(ln - R(7, 3)) == 0
    B.mcq(T_AL, "What is the length of the curve $x=\\frac{t^2}{2}$, $y=\\frac{t^3}{3}$ for $0\\le t\\le\\sqrt3$?",
          ch(R(7, 3), "$\\frac{dx}{dt}=t$, $\\frac{dy}{dt}=t^2$, so the speed is $\\sqrt{t^2+t^4}=t\\sqrt{1+t^2}$. Then $\\int_0^{\\sqrt3}t\\sqrt{1+t^2}\\,dt=\\frac13\\left(1+t^2\\right)^{3/2}\\Big|_0^{\\sqrt3}=\\frac13(8-1)=\\frac73$."),
          [ch(R(8, 3), "This is the value of the antiderivative at the upper limit only."),
           ch(7, "The antiderivative is $\\frac13(1+t^2)^{3/2}$. Without the $\\frac13$ the value is 7."),
           ch(R(14, 9), "$\\int t\\sqrt{1+t^2}\\,dt=\\frac12\\cdot\\frac23(1+t^2)^{3/2}=\\frac13(1+t^2)^{3/2}$. Using $\\frac23\\cdot\\frac13$ gives $\\frac29(\\ldots)$.")],
          "The speed simplifies: $\\sqrt{t^2+t^4}=t\\sqrt{1+t^2}$ for $t\\ge0$.", difficulty="medium")
