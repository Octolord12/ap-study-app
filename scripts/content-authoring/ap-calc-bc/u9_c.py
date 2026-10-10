"""Unit 9, polar coordinates and area in polar coordinates."""
from lib import *
import math

R = Rational
T_PC, T_PA = "polar-coordinates-and-derivatives", "area-in-polar-coordinates"


def grid_area(inside, x0, x1, y0, y1, n=1400):
    """Independent area check in Cartesian coordinates: count grid cells whose centre satisfies `inside`."""
    dx, dy = (x1 - x0) / n, (y1 - y0) / n
    cnt = 0
    for i in range(n):
        xx = x0 + (i + 0.5) * dx
        for j in range(n):
            if inside(xx, y0 + (j + 0.5) * dy):
                cnt += 1
    return cnt * dx * dy


def slope_polar(rf, th0):
    """dy/dx at theta = th0 for r = rf(theta), by the polar-to-Cartesian derivative formula."""
    r_ = rf
    dy = diff(r_, t) * sin(t) + r_ * cos(t)
    dx = diff(r_, t) * cos(t) - r_ * sin(t)
    return simplify((dy / dx).subs(t, th0))


def add(B):
    # ------------------------------------------------------------ polar coordinates and derivatives
    B.mcq(T_PC, "The polar point $\\left(4,\\frac\\pi3\\right)$ has which rectangular coordinates?",
          ch("$\\left(2,2\\sqrt3\\right)$", "$x=r\\cos\\theta=4\\cdot\\frac12=2$ and $y=r\\sin\\theta=4\\cdot\\frac{\\sqrt3}{2}=2\\sqrt3$."),
          [ch("$\\left(2\\sqrt3,2\\right)$", "The coordinates are swapped: $\\cos\\frac\\pi3=\\frac12$ goes with $x$ and $\\sin\\frac\\pi3=\\frac{\\sqrt3}2$ with $y$."),
           ch("$(2,2)$", "$\\sin\\frac\\pi3=\\frac{\\sqrt3}{2}$, not $\\frac12$."),
           ch("$\\left(\\frac12,\\frac{\\sqrt3}{2}\\right)$", "This is $(\\cos\\theta,\\sin\\theta)$ and leaves out the multiplication by $r=4$.")],
          "Use $x=r\\cos\\theta$ and $y=r\\sin\\theta$.", difficulty="easy")

    B.mcq(T_PC, "Which polar coordinates $(r,\\theta)$ with $r>0$ and $0\\le\\theta<2\\pi$ describe the point with rectangular coordinates $(-1,1)$?",
          ch("$\\left(\\sqrt2,\\frac{3\\pi}{4}\\right)$", "$r=\\sqrt{(-1)^2+1^2}=\\sqrt2$. The point is in the second quadrant, and $\\tan\\theta=-1$ there gives $\\theta=\\frac{3\\pi}4$."),
          [ch("$\\left(\\sqrt2,-\\frac\\pi4\\right)$", "$\\arctan(-1)=-\\frac\\pi4$ is in the fourth quadrant, which is the point $(1,-1)$. Add $\\pi$ to reach the second quadrant."),
           ch("$\\left(\\sqrt2,\\frac\\pi4\\right)$", "This is the point $(1,1)$ in the first quadrant."),
           ch("$\\left(2,\\frac{3\\pi}{4}\\right)$", "$r=\\sqrt{x^2+y^2}=\\sqrt2$, not 2.")],
          "Find $r$ from $x^2+y^2=r^2$, and choose $\\theta$ in the correct quadrant (a calculator's $\\arctan$ only returns angles in $(-\\frac\\pi2,\\frac\\pi2)$).", difficulty="easy")

    B.mcq(T_PC, "Which rectangular equation is equivalent to the polar equation $r=2\\cos\\theta$?",
          ch("$x^2+y^2=2x$", "Multiply both sides by $r$: $r^2=2r\\cos\\theta$, which is $x^2+y^2=2x$. This is a circle of radius 1 centered at $(1,0)$."),
          [ch("$x^2+y^2=2y$", "$r\\sin\\theta=y$ would give $r=2\\sin\\theta$. Here it is $r\\cos\\theta=x$."),
           ch("$x^2+y^2=4$", "This is the equation $r=2$, a circle centered at the origin."),
           ch("$y=2x$", "That is the line $\\tan\\theta=2$. The equation $r=2\\cos\\theta$ is a circle.")],
          "Multiply by $r$ to create the combinations $r^2=x^2+y^2$ and $r\\cos\\theta=x$.", difficulty="easy")

    rf = 1 + cos(t)
    assert slope_polar(rf, pi / 2) == 1
    B.mcq(T_PC, "For the polar curve $r=1+\\cos\\theta$, what is $\\dfrac{dy}{dx}$ at $\\theta=\\dfrac\\pi2$?",
          ch(1, "With $x=r\\cos\\theta$ and $y=r\\sin\\theta$: $\\frac{dy}{d\\theta}=-\\sin^2\\theta+(1+\\cos\\theta)\\cos\\theta=-1$ and $\\frac{dx}{d\\theta}=-\\sin\\theta\\cos\\theta-(1+\\cos\\theta)\\sin\\theta=-1$ at $\\theta=\\frac\\pi2$. The slope is $\\frac{-1}{-1}=1$."),
          [ch(-1, "This comes from a sign slip in $\\frac{dx}{d\\theta}$: using $r'\\cos\\theta+r\\sin\\theta$ instead of $r'\\cos\\theta-r\\sin\\theta$ gives $+1$ at this angle, and the slope would be $\\frac{-1}{1}=-1$."),
           ch(0, "This keeps only $r\\cos\\theta$ in $\\frac{dy}{d\\theta}$ and leaves out the $r'\\sin\\theta$ term."),
           ch("undefined", "This takes the slope to be $\\tan\\theta$, which is undefined at $\\frac\\pi2$. That is the slope of the radial line, not of the curve.")],
          "Treat $x=r(\\theta)\\cos\\theta$ and $y=r(\\theta)\\sin\\theta$ as parametric equations in $\\theta$ and use the product rule.", difficulty="medium")

    rf = 2 * cos(t)
    sl = slope_polar(rf, pi / 6)
    assert simplify(sl + sqrt(3) / 3) == 0
    B.mcq(T_PC, "For the polar curve $r=2\\cos\\theta$, what is $\\dfrac{dy}{dx}$ at $\\theta=\\dfrac\\pi6$?",
          ch(-sqrt(3) / 3, "$x=2\\cos^2\\theta$, $y=2\\sin\\theta\\cos\\theta=\\sin2\\theta$. So $\\frac{dy}{d\\theta}=2\\cos2\\theta$ and $\\frac{dx}{d\\theta}=-2\\sin2\\theta$, and the slope is $-\\cot2\\theta=-\\cot\\frac\\pi3=-\\frac{\\sqrt3}3$."),
          [ch(sqrt(3) / 3, "The slope is $\\frac{2\\cos2\\theta}{-2\\sin2\\theta}$. The minus sign from $\\frac{dx}{d\\theta}$ was lost."),
           ch(-sqrt(3), "This is $-\\tan2\\theta$, the reciprocal of the slope."),
           ch(0, "This is the slope at $\\theta=\\frac\\pi4$, where $\\cot2\\theta=\\cot\\frac\\pi2=0$.")],
          "Write $x$ and $y$ in terms of $\\theta$, simplify with double-angle identities, and divide the derivatives.", difficulty="medium")

    B.mcq(T_PC, "For a polar curve $r=f(\\theta)$, which expression gives $\\dfrac{dy}{dx}$?",
          ch("$\\dfrac{f'(\\theta)\\sin\\theta+f(\\theta)\\cos\\theta}{f'(\\theta)\\cos\\theta-f(\\theta)\\sin\\theta}$", "With $x=f(\\theta)\\cos\\theta$ and $y=f(\\theta)\\sin\\theta$, the product rule gives $\\frac{dy}{d\\theta}=f'\\sin\\theta+f\\cos\\theta$ and $\\frac{dx}{d\\theta}=f'\\cos\\theta-f\\sin\\theta$."),
          [ch("$\\dfrac{f'(\\theta)\\sin\\theta-f(\\theta)\\cos\\theta}{f'(\\theta)\\cos\\theta+f(\\theta)\\sin\\theta}$", "The signs of the second terms are reversed in both parts. The product rule adds in $\\frac{dy}{d\\theta}$ and subtracts in $\\frac{dx}{d\\theta}$."),
           ch("$f'(\\theta)$", "$f'(\\theta)=\\frac{dr}{d\\theta}$ is the rate at which the distance from the origin changes, not the slope of the curve."),
           ch("$\\tan\\theta$", "$\\tan\\theta$ is the slope of the line from the origin to the point, not the slope of the tangent to the curve.")],
          "A polar curve is a parametric curve in the parameter $\\theta$, so $\\frac{dy}{dx}=\\frac{dy/d\\theta}{dx/d\\theta}$.", difficulty="medium")

    B.mcq(T_PC, "How many petals does the polar graph of $r=2\\sin3\\theta$ have?",
          ch(3, "For $r=a\\sin n\\theta$ or $a\\cos n\\theta$ with $n$ odd, the graph has $n$ petals. Here $n=3$."),
          [ch(6, "6 petals would come from doubling when $n$ is odd. That rule applies to even $n$, which gives $2n$ petals."),
           ch(2, "The coefficient 2 is the length of the petals, not their number."),
           ch(1, "A single loop would be the graph of a circle such as $r=2\\sin\\theta$.")],
          "For $r=a\\sin n\\theta$ the number of petals is $n$ if $n$ is odd and $2n$ if $n$ is even.", difficulty="medium")

    B.mcq(T_PC, "Which rectangular equation is equivalent to the polar equation $r=4\\sin\\theta$?",
          ch("$x^2+(y-2)^2=4$", "Multiplying by $r$: $r^2=4r\\sin\\theta$, so $x^2+y^2=4y$. Completing the square gives $x^2+(y-2)^2=4$: a circle of radius 2 centered at $(0,2)$."),
          [ch("$(x-2)^2+y^2=4$", "This is the circle for $r=4\\cos\\theta$, centered at $(2,0)$."),
           ch("$x^2+y^2=4$", "This is the equation $r=2$."),
           ch("$x^2+(y-4)^2=16$", "Completing the square on $x^2+y^2-4y=0$ uses half of 4: $(y-2)^2$, with $4$ on the right.")],
          "Multiply both sides by $r$ and replace $r\\sin\\theta$ by $y$ and $r^2$ by $x^2+y^2$. Then complete the square.", difficulty="medium")

    rf = 1 + 2 * cos(t)
    assert slope_polar(rf, pi / 2) == 2
    B.mcq(T_PC, "For the polar curve $r=1+2\\cos\\theta$, what is $\\dfrac{dy}{dx}$ at $\\theta=\\dfrac\\pi2$?",
          ch(2, "At $\\theta=\\frac\\pi2$: $r=1$ and $r'=-2\\sin\\theta=-2$. Then $\\frac{dy}{d\\theta}=r'\\sin\\theta+r\\cos\\theta=-2$ and $\\frac{dx}{d\\theta}=r'\\cos\\theta-r\\sin\\theta=-1$. The slope is $\\frac{-2}{-1}=2$."),
          [ch(-2, "This is $\\frac{dy}{d\\theta}$ alone. The slope divides by $\\frac{dx}{d\\theta}=-1$."),
           ch(R(1, 2), "This is the reciprocal, $\\frac{dx}{d\\theta}\\big/\\frac{dy}{d\\theta}$."),
           ch(0, "This keeps only $r\\cos\\theta$ in $\\frac{dy}{d\\theta}$. The $r'\\sin\\theta$ term is $-2$ at this angle.")],
          "Compute $r$ and $r'$ at the angle first, then substitute into the two product-rule expressions.", difficulty="hard")

    B.mcq(T_PC, "A particle moves so that its polar coordinates at time $t$ are $r=2+\\sin t$ and $\\theta=t$, for $0\\le t\\le2\\pi$. During which times is the particle's distance from the origin increasing?",
          ch("$0<t<\\frac\\pi2$ and $\\frac{3\\pi}{2}<t<2\\pi$", "The distance is $r=2+\\sin t$, and $\\frac{dr}{dt}=\\cos t$. It is positive where $\\cos t>0$: on $\\left(0,\\frac\\pi2\\right)$ and $\\left(\\frac{3\\pi}2,2\\pi\\right)$."),
          [ch("$0<t<\\pi$", "On $\\left(0,\\pi\\right)$ the value $\\sin t$ is positive, so $r$ is greater than 2, but it is not increasing the whole time: $\\frac{dr}{dt}=\\cos t$ is negative on $\\left(\\frac\\pi2,\\pi\\right)$."),
           ch("$\\frac\\pi2<t<\\frac{3\\pi}2$", "This is where $\\cos t<0$: the distance is decreasing."),
           ch("$0<t<\\pi$ and $\\frac{3\\pi}{2}<t<2\\pi$", "Between $\\frac\\pi2$ and $\\pi$, $\\frac{dr}{dt}=\\cos t<0$, so the distance is decreasing there.")],
          "The distance from the origin is $r$. It increases where $\\frac{dr}{dt}>0$.", difficulty="medium")

    B.mcq(T_PC, "The polar curve $r=2\\cos3\\theta$ passes through the origin when $\\theta=\\dfrac\\pi6$. Which line is tangent to the curve at the origin there?",
          ch("$y=\\dfrac{1}{\\sqrt3}x$", "At the pole, $r=0$ and $\\frac{dr}{d\\theta}=-6\\sin3\\theta=-6\\ne0$, so the tangent line at the origin is the line $\\theta=\\frac\\pi6$, which has slope $\\tan\\frac\\pi6=\\frac1{\\sqrt3}$."),
          [ch("$y=\\sqrt3\\,x$", "That is the line $\\theta=\\frac\\pi3$. The curve reaches the origin at $\\theta=\\frac\\pi6$."),
           ch("$y=0$", "That is the line $\\theta=0$, where $r=2$: the curve is at its farthest point there, not at the origin."),
           ch("$x=0$", "That is the line $\\theta=\\frac\\pi2$.")],
          "When $r=0$ at $\\theta_0$ and $\\frac{dr}{d\\theta}\\ne0$, the tangent line to the curve at the origin is the line $\\theta=\\theta_0$.", difficulty="hard")

    # ------------------------------------------------------------ area in polar coordinates
    B.mcq(T_PA, "What is the area of the region enclosed by the polar curve $r=2$ for $0\\le\\theta\\le2\\pi$, found with $A=\\frac12\\int r^2\\,d\\theta$?",
          ch(4 * pi, "$A=\\frac12\\int_0^{2\\pi}2^2\\,d\\theta=\\frac12\\cdot4\\cdot2\\pi=4\\pi$, the area of a circle of radius 2."),
          [ch(8 * pi, "The factor $\\frac12$ is missing."),
           ch(2 * pi, "This integrates $\\frac12r$ instead of $\\frac12r^2$."),
           ch(16 * pi**2, "This squares the whole integral. $A=\\frac12\\int r^2\\,d\\theta$ squares only $r$.")],
          "In polar coordinates, area $=\\frac12\\int_\\alpha^\\beta r^2\\,d\\theta$.", difficulty="easy")

    B.mcq(T_PA, "Which integral gives the area of the region enclosed by the polar curve $r=3\\sin\\theta$?",
          ch("$\\displaystyle\\frac12\\int_0^{\\pi}\\left(3\\sin\\theta\\right)^2d\\theta$", "The graph of $r=3\\sin\\theta$ is a circle traced once as $\\theta$ goes from 0 to $\\pi$. The area is $\\frac12\\int r^2\\,d\\theta$ over that interval."),
          [ch("$\\displaystyle\\frac12\\int_0^{2\\pi}\\left(3\\sin\\theta\\right)^2d\\theta$", "Over $[0,2\\pi]$ the circle is traced twice (for $\\pi<\\theta<2\\pi$, $r<0$ and the points repeat), so the area would be counted twice."),
           ch("$\\displaystyle\\int_0^{\\pi}\\left(3\\sin\\theta\\right)^2d\\theta$", "The factor $\\frac12$ is missing."),
           ch("$\\displaystyle\\frac12\\int_0^{\\pi}3\\sin\\theta\\,d\\theta$", "The integrand must be $r^2$, not $r$.")],
          "Find the interval over which the curve is traced exactly once, then use $\\frac12\\int r^2\\,d\\theta$.", difficulty="medium")

    v = integrate((1 + cos(t)) ** 2 / 2, (t, 0, 2 * pi))
    assert simplify(v - 3 * pi / 2) == 0
    B.mcq(T_PA, "What is the area of the region enclosed by the polar curve $r=1+\\cos\\theta$?",
          ch(3 * pi / 2, "$A=\\frac12\\int_0^{2\\pi}(1+\\cos\\theta)^2d\\theta=\\frac12\\int_0^{2\\pi}\\left(1+2\\cos\\theta+\\cos^2\\theta\\right)d\\theta=\\frac12\\left(2\\pi+0+\\pi\\right)=\\frac{3\\pi}{2}$."),
          [ch(3 * pi, "The factor $\\frac12$ is missing."),
           ch(pi, "This integrates $\\frac12r=\\frac12(1+\\cos\\theta)$ instead of $\\frac12r^2$."),
           ch(3 * pi / 4, "This stops at $\\theta=\\pi$, which is only the top half of the curve. The cardioid needs $[0,2\\pi]$.")],
          "Expand $(1+\\cos\\theta)^2$ and integrate over a full turn; the cross term $2\\cos\\theta$ integrates to 0 and $\\cos^2\\theta$ to $\\pi$.", difficulty="medium")

    v = integrate(cos(2 * t) ** 2 / 2, (t, -pi / 4, pi / 4))
    assert simplify(v - pi / 8) == 0
    B.mcq(T_PA, "What is the area of one petal of the polar curve $r=\\cos2\\theta$, the petal centered on the positive $x$-axis?",
          ch(pi / 8, "That petal is traced for $-\\frac\\pi4\\le\\theta\\le\\frac\\pi4$, where $\\cos2\\theta\\ge0$. $A=\\frac12\\int_{-\\pi/4}^{\\pi/4}\\cos^22\\theta\\,d\\theta=\\frac12\\cdot\\frac\\pi4=\\frac\\pi8$."),
          [ch(pi / 4, "The factor $\\frac12$ is missing."),
           ch(pi / 2, "This is the area of all four petals, $4\\cdot\\frac\\pi8$."),
           ch(pi / 16, "$\\int_{-\\pi/4}^{\\pi/4}\\cos^22\\theta\\,d\\theta=\\frac\\pi4$. Halving it twice gives $\\frac\\pi{16}$.")],
          "Find the two angles where $r=0$ on each side of the petal; those are the limits of integration.", difficulty="medium")

    area5 = grid_area(lambda xx, yy: xx * xx + yy * yy < 4 * xx and xx * xx + yy * yy > 4, 0, 4.2, -2.2, 2.2)
    v5 = integrate((16 * cos(t) ** 2 - 4) / 2, (t, -pi / 3, pi / 3))
    assert abs(float(v5) - area5) < 0.02, (float(v5), area5)
    B.mcq(T_PA, "Which expression gives the area of the region that lies inside the circle $r=4\\cos\\theta$ and outside the circle $r=2$?",
          ch("$\\displaystyle\\frac12\\int_{-\\pi/3}^{\\pi/3}\\left(16\\cos^2\\theta-4\\right)d\\theta$", "The curves meet where $4\\cos\\theta=2$, so $\\theta=\\pm\\frac\\pi3$. Between these angles the outer curve is $r=4\\cos\\theta$ and the inner is $r=2$: $A=\\frac12\\int\\left(r_{\\text{out}}^2-r_{\\text{in}}^2\\right)d\\theta$."),
          [ch("$\\displaystyle\\frac12\\int_0^{\\pi/3}\\left(16\\cos^2\\theta-4\\right)d\\theta$", "This covers only the upper half of the region. The region extends from $-\\frac\\pi3$ to $\\frac\\pi3$."),
           ch("$\\displaystyle\\frac12\\int_{-\\pi/3}^{\\pi/3}\\left(4\\cos\\theta-2\\right)^2d\\theta$", "The difference of the areas is $r_{\\text{out}}^2-r_{\\text{in}}^2$, not $\\left(r_{\\text{out}}-r_{\\text{in}}\\right)^2$."),
           ch("$\\displaystyle\\frac12\\int_{-\\pi/2}^{\\pi/2}\\left(16\\cos^2\\theta-4\\right)d\\theta$", "Beyond $\\theta=\\pm\\frac\\pi3$ the circle $r=4\\cos\\theta$ is inside $r=2$, so the integrand would be negative there.")],
          "Find where the curves intersect, decide which is farther from the origin between those angles, and subtract the squares of the radii.", difficulty="hard")

    v = integrate(t**2 / 2, (t, 0, pi))
    assert simplify(v - pi**3 / 6) == 0
    B.mcq(T_PA, "What is the area swept out by the radius vector of the spiral $r=\\theta$ as $\\theta$ goes from 0 to $\\pi$?",
          ch(pi**3 / 6, "$A=\\frac12\\int_0^\\pi\\theta^2\\,d\\theta=\\frac12\\cdot\\frac{\\pi^3}{3}=\\frac{\\pi^3}{6}$."),
          [ch(pi**3 / 3, "The factor $\\frac12$ is missing."),
           ch(pi**2 / 2, "This integrates $\\frac12r=\\frac12\\theta$. The integrand is $\\frac12r^2$."),
           ch(pi**3 / 2, "$\\int_0^\\pi\\theta^2d\\theta=\\frac{\\pi^3}{3}$. Multiplying by 3 instead of $\\frac13$ gives $\\pi^3$, and half of that is $\\frac{\\pi^3}{2}$.")],
          "Use $A=\\frac12\\int_0^\\pi r^2\\,d\\theta$ with $r=\\theta$.", difficulty="medium")

    area7 = grid_area(lambda xx, yy: xx * xx + yy * yy < 3 * xx and (xx * xx + yy * yy) ** 0.5 > 1 + xx / max(1e-12, (xx * xx + yy * yy) ** 0.5), 0, 3.2, -2.2, 2.2)
    v7 = integrate((9 * cos(t) ** 2 - (1 + cos(t)) ** 2) / 2, (t, -pi / 3, pi / 3))
    assert abs(float(v7) - area7) < 0.02 and simplify(v7 - pi) == 0, (float(v7), area7)
    wrong_half = integrate((9 * cos(t) ** 2 - (1 + cos(t)) ** 2) / 2, (t, 0, pi / 3))
    wrong_diff = integrate((3 * cos(t) - (1 + cos(t))) ** 2 / 2, (t, -pi / 3, pi / 3))
    assert simplify(wrong_half - pi / 2) == 0 and simplify(wrong_diff - pi) != 0
    B.mcq(T_PA, "What is the area of the region that lies inside the circle $r=3\\cos\\theta$ and outside the cardioid $r=1+\\cos\\theta$?",
          ch(pi, "The curves meet where $3\\cos\\theta=1+\\cos\\theta$, so $\\cos\\theta=\\frac12$ and $\\theta=\\pm\\frac\\pi3$. $A=\\frac12\\int_{-\\pi/3}^{\\pi/3}\\left(9\\cos^2\\theta-(1+\\cos\\theta)^2\\right)d\\theta=\\frac12\\int\\left(8\\cos^2\\theta-2\\cos\\theta-1\\right)d\\theta=\\frac12(2\\pi)=\\pi$."),
          [ch(2 * pi, "The factor $\\frac12$ in $A=\\frac12\\int\\left(r_{\\text{out}}^2-r_{\\text{in}}^2\\right)d\\theta$ is missing."),
           ch(pi / 2, "This integrates only from 0 to $\\frac\\pi3$, the upper half of the region."),
           ch(nsimplify(simplify(wrong_diff)), "This squares the difference of the radii, $\\left(r_{\\text{out}}-r_{\\text{in}}\\right)^2$. The area between curves subtracts the squares: $r_{\\text{out}}^2-r_{\\text{in}}^2$.")],
          "Find the intersection angles, then integrate $\\frac12\\left(r_{\\text{out}}^2-r_{\\text{in}}^2\\right)$. Use $\\cos^2\\theta=\\frac{1+\\cos2\\theta}{2}$.", difficulty="hard")

    area8 = grid_area(lambda xx, yy: xx * xx + yy * yy < 2 * yy and xx * xx + yy * yy < 2 * xx, 0, 2.2, 0, 2.2)
    v8 = 2 * integrate((2 * sin(t)) ** 2 / 2, (t, 0, pi / 4))
    assert abs(float(v8) - area8) < 0.01 and simplify(v8 - (pi / 2 - 1)) == 0, (float(v8), area8)
    B.mcq(T_PA, "What is the area of the region inside both circles $r=2\\sin\\theta$ and $r=2\\cos\\theta$?",
          chv("\\frac\\pi2-1", "The circles meet at $\\theta=\\frac\\pi4$. For $0\\le\\theta\\le\\frac\\pi4$ the nearer boundary is $r=2\\sin\\theta$, and by symmetry the region is twice that piece: $2\\cdot\\frac12\\int_0^{\\pi/4}4\\sin^2\\theta\\,d\\theta=4\\left(\\frac\\pi8-\\frac14\\right)=\\frac\\pi2-1$.", pi / 2 - 1),
          [chv("\\frac\\pi2", "This is $\\frac12\\int_0^{\\pi/2}(2\\sin\\theta)^2d\\theta$, the area of half of one whole circle. The boundary switches to the other circle at $\\theta=\\frac\\pi4$.", pi / 2),
           chv("\\pi-2", "The factor $\\frac12$ in $\\frac12\\int r^2d\\theta$ is missing.", pi - 2),
           chv("\\frac\\pi4-\\frac12", "This is only one of the two symmetric pieces ($0\\le\\theta\\le\\frac\\pi4$). The region is twice as large.", pi / 4 - R(1, 2))],
          "Find where the circles intersect, use the circle that is closer to the origin on each side of that angle, and use symmetry about the line $\\theta=\\frac\\pi4$.", difficulty="hard")

    B.mcq(T_PA, "What is the area of the region enclosed by the polar curve $r=2\\cos\\theta$?",
          ch(pi, "The circle is traced once for $-\\frac\\pi2\\le\\theta\\le\\frac\\pi2$: $A=\\frac12\\int_{-\\pi/2}^{\\pi/2}4\\cos^2\\theta\\,d\\theta=2\\cdot\\frac\\pi2=\\pi$. It is a circle of radius 1."),
          [ch(2 * pi, "This integrates over $[0,2\\pi]$, which traces the circle twice."),
           ch(4 * pi, "This uses $[0,2\\pi]$ and also omits the $\\frac12$."),
           ch(pi / 2, "$\\int_{-\\pi/2}^{\\pi/2}\\cos^2\\theta\\,d\\theta=\\frac\\pi2$, and the integrand has the coefficient $4\\cdot\\frac12=2$. The result is $\\pi$, not $\\frac\\pi2$.")],
          "A circle $r=a\\cos\\theta$ is traced once as $\\theta$ goes through an interval of length $\\pi$.", difficulty="medium")

    v10 = integrate((2 * sin(3 * t)) ** 2 / 2, (t, 0, pi / 3))
    assert simplify(v10 - pi / 3) == 0
    B.mcq(T_PA, "What is the area of one petal of the polar curve $r=2\\sin3\\theta$?",
          ch(pi / 3, "One petal is traced for $0\\le\\theta\\le\\frac\\pi3$ (where $\\sin3\\theta\\ge0$): $A=\\frac12\\int_0^{\\pi/3}4\\sin^23\\theta\\,d\\theta=2\\cdot\\frac\\pi6=\\frac\\pi3$."),
          [ch(pi, "That is the area of all three petals."),
           ch(2 * pi / 3, "The factor $\\frac12$ is missing."),
           ch(pi / 6, "$\\int_0^{\\pi/3}\\sin^23\\theta\\,d\\theta=\\frac\\pi6$. The coefficient is $\\frac12\\cdot4=2$, so the area is $\\frac\\pi3$.")],
          "Find two consecutive angles where $r=0$ to bound a single petal, then use $\\sin^2u=\\frac{1-\\cos2u}{2}$.", difficulty="medium")

    v11 = integrate((3 * cos(2 * t)) ** 2 / 2, (t, 0, 2 * pi))
    assert simplify(v11 - 9 * pi / 2) == 0
    B.mcq(T_PA, "What is the total area enclosed by the four-petaled rose $r=3\\cos2\\theta$?",
          ch(9 * pi / 2, "$A=\\frac12\\int_0^{2\\pi}9\\cos^22\\theta\\,d\\theta=\\frac92\\cdot\\pi=\\frac{9\\pi}{2}$, since $\\int_0^{2\\pi}\\cos^22\\theta\\,d\\theta=\\pi$."),
          [ch(9 * pi, "The factor $\\frac12$ is missing."),
           ch(9 * pi / 8, "This is the area of one petal, $\\frac{9\\pi}{8}$."),
           ch(9 * pi / 4, "This integrates over $[0,\\pi]$ and so counts only two of the four petals.")],
          "The rose $r=3\\cos2\\theta$ closes after $\\theta$ goes from 0 to $2\\pi$. Integrate $\\frac12r^2$ over that interval.", difficulty="hard")
