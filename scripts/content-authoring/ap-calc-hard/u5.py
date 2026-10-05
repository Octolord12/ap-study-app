from lib import *

B = Bank(5, "unit-5-analytical-applications-of-differentiation")
T_MVT, T_EXT, T_CON, T_OPT, T_CS = (
    "mean-value-theorem",
    "extrema-and-first-derivative-test",
    "concavity-and-second-derivative-test",
    "optimization",
    "curve-sketching",
)

# 1. MVT value of c for ln x
cc = symbols("cc", positive=True)
sol = solve(Eq(1 / cc, (log(exp(2)) - log(1)) / (exp(2) - 1)), cc)[0]
assert simplify(sol - (exp(2) - 1) / 2) == 0
B.mcq(T_MVT, "For $f(x)=\\ln x$ on the interval $[1,e^2]$, what value of $c$ does the Mean Value Theorem guarantee?",
      ch("$\\dfrac{e^2-1}{2}$", "The average rate of change is $\\frac{\\ln e^2-\\ln 1}{e^2-1}=\\frac{2}{e^2-1}$. Setting $f'(c)=\\frac1c=\\frac{2}{e^2-1}$ gives $c=\\frac{e^2-1}{2}\\approx3.19$, which is in the interval."),
      [ch("$\\dfrac{e^2+1}{2}$", "This is the midpoint of the interval. The MVT point is where $f'(c)$ equals the average rate, and that is generally not the midpoint."),
       ch("$\\dfrac{2}{e^2-1}$", "This is the average rate of change, which equals $f'(c)=\\frac1c$. It is not $c$ itself; $c$ is the reciprocal."),
       ch(E, "$f'(e)=\\frac1e$ is not the average rate $\\frac{2}{e^2-1}$, so $x=e$ is not the guaranteed point.")],
      "Set $f'(c)$ equal to $\\frac{f(b)-f(a)}{b-a}$ and solve for $c$. Check that $c$ is in the open interval.")

# 2. MVT hypotheses
B.mcq(T_MVT, "On which of the following functions does the Mean Value Theorem apply on the interval $[0,3]$?",
      ch("$f(x)=\\sqrt{3x-x^2}$", "$f$ is continuous on $[0,3]$ (the radicand is $\\ge0$ there) and differentiable on $(0,3)$: $f'(x)=\\frac{3-2x}{2\\sqrt{3x-x^2}}$ exists for $0<x<3$. The derivative is not required to exist at the endpoints."),
      [ch("$g(x)=|x-1|$", "$g$ is continuous but has a corner at $x=1$, which is inside $(0,3)$, so it is not differentiable on the whole open interval."),
       ch("$h(x)=(x-1)^{2/3}$", "$h$ is continuous, but $h'(x)=\\frac23(x-1)^{-1/3}$ is undefined at $x=1$, inside the interval (a cusp)."),
       ch("$k(x)=\\dfrac{1}{x-2}$", "$k$ has a vertical asymptote at $x=2$, so it is not continuous on $[0,3]$.")],
      "Check both hypotheses: continuous on the closed interval and differentiable on the open interval. A function can fail to be differentiable at an endpoint and still satisfy the MVT.")

# 3. bounding f(4) using derivative bounds
B.mcq(T_MVT, "The function $f$ is differentiable for all $x$, with $f(1)=2$ and $-1\\le f'(x)\\le4$ for all $x$. Which statement must be true about $f(4)$?",
      ch("$-1\\le f(4)\\le14$", "By the MVT, $f(4)-f(1)=3f'(c)$ for some $c$ in $(1,4)$, so $-3\\le f(4)-f(1)\\le12$. Adding $f(1)=2$ gives $-1\\le f(4)\\le14$."),
      [ch("$-3\\le f(4)\\le12$", "This bounds the change $f(4)-f(1)$, not the value $f(4)$. Add the starting value $f(1)=2$."),
       ch("$-1\\le f(4)\\le4$", "The bounds on the derivative are bounds on the slope, not on the function value. The interval has length 3, which multiplies those bounds."),
       ch("$2\\le f(4)\\le14$", "The lower bound is wrong: $f'$ can be negative, so $f$ can decrease. The lowest value is $2+3(-1)=-1$.")],
      "Apply the MVT on $[1,4]$: $\\frac{f(4)-f(1)}{4-1}=f'(c)$, then use the bounds on $f'(c)$.")

# 4. first derivative test with a cusp
f = x ** Rational(2, 3) * (x - 5)
fp = simplify(diff(f, x))
assert simplify(fp - Rational(5, 3) * x ** Rational(-1, 3) * (x - 2)) == 0
B.mcq(T_EXT, "Let $f(x)=x^{2/3}(x-5)$. What does the First Derivative Test show about the critical numbers of $f$?",
      ch("$f$ has a local maximum at $x=0$ and a local minimum at $x=2$", "$f'(x)=\\frac53x^{-1/3}(x-2)$ is undefined at $x=0$ and zero at $x=2$. The sign of $f'$: positive for $x<0$ (both factors negative), negative on $(0,2)$, positive for $x>2$. So $f$ rises then falls at 0 (local max) and falls then rises at 2 (local min)."),
      [ch("$f$ has a local minimum at $x=0$ and a local maximum at $x=2$", "The two are swapped. $f'$ changes from $+$ to $-$ at 0 (maximum) and from $-$ to $+$ at 2 (minimum)."),
       ch("$f$ has a local minimum at $x=2$ only", "$x=0$ is a critical number because $f'$ is undefined there while $f$ is defined. $f'$ changes sign at 0, so it is also a local extremum."),
       ch("$f$ has a local maximum at $x=0$ only", "$f'$ also changes sign at $x=2$, from negative to positive, which gives a local minimum.")],
      "Critical numbers include points where $f'$ is undefined but $f$ is defined. Test the sign of $f'$ on each side of every critical number.")

# 5. sign analysis with a squared factor
fpx = (x - 1) ** 2 * (x + 2) * (x - 3)
B.mcq(T_EXT, "The derivative of $f$ is $f'(x)=(x-1)^2(x+2)(x-3)$. At which value of $x$ does $f$ have a local maximum?",
      ch("$x=-2$", "$f'>0$ for $x<-2$ and $f'<0$ on $(-2,1)$, so $f'$ changes from positive to negative at $-2$: a local maximum."),
      [ch("$x=1$", "At $x=1$ the factor $(x-1)^2$ is zero but never changes sign, so $f'$ is negative on both sides. There is no extremum at 1."),
       ch("$x=3$", "$f'$ changes from negative to positive at $x=3$, which is a local minimum."),
       ch("$x=-2$ and $x=3$", "$f'$ changes from $+$ to $-$ only at $-2$. At $3$ it changes from $-$ to $+$, which is a local minimum, not a maximum.")],
      "Make a sign chart of $f'$. A local maximum is a sign change from positive to negative; squared factors do not change the sign.")

# 6. graph of f' (diagram): increasing and concave down
d6 = graph("x", "f'(x)", 0, 8, -4, 4,
           [{"points": [{"x": 0, "y": -3}, {"x": 2, "y": 3}, {"x": 6, "y": -3}, {"x": 8, "y": -1}], "color": "blue", "label": "f'"}],
           "Graph of f prime made of line segments through (0,-3), (2,3), (6,-3) and (8,-1). It crosses the x-axis at x=1 and x=4.")
B.mcq(T_CS, "The graph of $f'$, the derivative of $f$, is shown for $0\\le x\\le8$. It consists of line segments. On which interval is the graph of $f$ both increasing and concave down?",
      ch("$2<x<4$", "$f$ is increasing where $f'>0$, which is $1<x<4$ (the graph crosses the axis at $x=1$ and $x=4$). $f$ is concave down where $f'$ is decreasing, which is $2<x<6$. Both hold on $(2,4)$."),
      [ch("$1<x<2$", "Here $f'>0$ so $f$ is increasing, but $f'$ is also increasing, so $f$ is concave up."),
       ch("$4<x<6$", "Here $f'$ is decreasing so $f$ is concave down, but $f'<0$, so $f$ is decreasing, not increasing."),
       ch("$1<x<4$", "$f$ is increasing on all of $(1,4)$, but concavity changes at $x=2$: $f'$ is increasing on $(1,2)$ and decreasing on $(2,4)$.")],
      "Read increasing/decreasing from the sign of $f'$ and concavity from whether $f'$ is rising or falling.", diagram=d6)

# 7. inflection points with a squared factor
B.mcq(T_CON, "The second derivative of $f$ is $f''(x)=x(x-2)^2(x+1)$. What are the $x$-coordinates of the inflection points of the graph of $f$?",
      ch("$x=-1$ and $x=0$", "$f''$ changes sign at $-1$ (from $+$ to $-$) and at $0$ (from $-$ to $+$). At $x=2$ the factor $(x-2)^2$ keeps the sign, so concavity does not change."),
      [ch("$x=-1$, $x=0$ and $x=2$", "$f''(2)=0$, but $f''$ does not change sign at 2 because of the squared factor, so there is no inflection point there."),
       ch("$x=0$ and $x=2$", "$x=-1$ is missed: $f''$ changes sign there. And $x=2$ is not an inflection point."),
       ch("$x=2$ only", "$f''=0$ at 2, but a zero of the second derivative is an inflection point only if the sign changes.")],
      "An inflection point needs $f''$ to change sign. Zeros from even-power factors do not change the sign.")

# 8. parameters from an inflection point, then a minimum value
aa, bb = symbols("aa bb", real=True)
sol = solve([Eq(6 * aa * 1 + 2 * bb, 0), Eq(aa + bb, -4)], [aa, bb])
assert sol == {aa: 2, bb: -6}
f = 2 * x**3 - 6 * x**2
assert solve(diff(f, x), x) == [0, 2] and f.subs(x, 2) == -8 and diff(f, x, 2).subs(x, 2) > 0
B.mcq(T_CON, "The graph of $f(x)=ax^3+bx^2$ has an inflection point at $(1,-4)$. What is the local minimum value of $f$?",
      ch(-8, "$f''(x)=6ax+2b=0$ at $x=1$ gives $b=-3a$. $f(1)=a+b=-4$ then gives $-2a=-4$, so $a=2$ and $b=-6$. Then $f'(x)=6x^2-12x=6x(x-2)$ and $f''(2)=12>0$, a local minimum with $f(2)=16-24=-8$."),
      [ch(-4, "$-4$ is the value of $f$ at the inflection point $x=1$, not at the local minimum $x=2$."),
       ch(0, "$f(0)=0$ is the local maximum value ($f''(0)=-12<0$), not the local minimum."),
       ch(-6, "$-6$ is the coefficient $b$, not a value of the function. The local minimum value is $f(2)=16-24=-8$.")],
      "Use $f''(1)=0$ and $f(1)=-4$ to find $a$ and $b$, then find and classify the critical points of the resulting function.")

# 9. absolute extrema on a closed interval
f = x**3 - 6 * x**2 + 9 * x + 1
vals = {q_: f.subs(x, q_) for q_ in (-1, 1, 3, 4)}
assert vals == {-1: -15, 1: 5, 3: 1, 4: 5}
B.mcq(T_EXT, "Let $f(x)=x^3-6x^2+9x+1$. What is the difference between the absolute maximum value and the absolute minimum value of $f$ on the interval $[-1,4]$?",
      ch(20, "$f'(x)=3(x-1)(x-3)$, so compare $f$ at the critical points and endpoints: $f(-1)=-15$, $f(1)=5$, $f(3)=1$, $f(4)=5$. Maximum 5, minimum $-15$, difference 20."),
      [ch(4, "This is the local maximum minus the local minimum, $f(1)-f(3)=5-1$. Absolute extrema on a closed interval must also be checked at the endpoints."),
       ch(15, "$-15$ is the absolute minimum (at the endpoint $x=-1$); the question asks for the difference between the maximum and the minimum."),
       ch(6, "This miscomputes $f(-1)$ as $-1$. $f(-1)=-1-6-9+1=-15$.")],
      "Apply the Extreme Value Theorem: evaluate $f$ at each critical point in the interval and at both endpoints.")

# 10. open-top box
x_ = symbols("x_", positive=True)
S = x_**2 + 128 / x_
xmin = solve(diff(S, x_), x_)[0]
assert xmin == 4 and S.subs(x_, 4) == 48
B.mcq(T_OPT, "An open-top box with a square base is to have volume 32 cubic feet. What is the least possible surface area of the box (the base and four sides), in square feet?",
      ch(48, "With base side $x$ and height $h=\\frac{32}{x^2}$, $S=x^2+4xh=x^2+\\frac{128}{x}$. $S'=2x-\\frac{128}{x^2}=0$ gives $x=4$, $h=2$, and $S=16+32=48$. $S''>0$, so this is a minimum."),
      [ch(64, "This counts a top ($S=2x^2+\\frac{128}x$ at $x=4$, which is $32+32=64$). The box is open-topped, so there is no top."),
       ch(32, "32 is the volume, not the surface area."),
       ch(68, "This uses $x=2$ and $h=8$, which is not the minimizing dimension ($S'(2)\\neq0$). The minimum is at $x=4$.")],
      "Write the surface area as a function of the base side, set the derivative equal to 0, and confirm a minimum.")

# 11. closest point on a curve
D2 = (x - 4) ** 2 + x
xs = solve(diff(D2, x), x)
assert xs == [Rational(7, 2)]
B.mcq(T_OPT, "Which point on the graph of $y=\\sqrt{x}$ is closest to the point $(4,0)$?",
      ch("$\\left(\\dfrac72,\\sqrt{\\dfrac72}\\right)$", "Minimize the squared distance $D=(x-4)^2+(\\sqrt x)^2=(x-4)^2+x$. $D'=2(x-4)+1=0$ gives $x=\\frac72$, and $D''=2>0$ confirms a minimum."),
      [ch("$(4,2)$", "This is the point directly above $(4,0)$ (same $x$), not the nearest point. Moving left along the curve gets closer."),
       ch("$(2,\\sqrt2)$", "$x=2$ does not satisfy $D'=2(x-4)+1=0$. At $x=2$, $D'=-3<0$, so $D$ is still decreasing and a point further right is closer."),
       ch("$(0,0)$", "$(0,0)$ is at distance 4, whereas $x=\\frac72$ gives $D=\\frac14+\\frac72=\\frac{15}4$, a distance of about 1.94.")],
      "Minimize the square of the distance, which has the same minimizer as the distance and avoids a square root.")

# 12. inflection points of x^2 e^{-x}
f = x**2 * exp(-x)
d2 = simplify(diff(f, x, 2) * exp(x))
assert expand(d2 - (x**2 - 4 * x + 2)) == 0
B.mcq(T_CS, "What are the $x$-coordinates of the inflection points of the graph of $f(x)=x^2e^{-x}$?",
      ch("$x=2-\\sqrt2$ and $x=2+\\sqrt2$", "$f'(x)=(2x-x^2)e^{-x}$ and $f''(x)=(x^2-4x+2)e^{-x}$. $f''=0$ when $x^2-4x+2=0$, i.e. $x=2\\pm\\sqrt2$, and $f''$ changes sign at each."),
      [ch("$x=0$ and $x=2$", "These are the zeros of $f'$ (critical points), not of $f''$."),
       ch("$x=\\sqrt2$ and $x=-\\sqrt2$", "This solves $x^2-2=0$. The second derivative's quadratic is $x^2-4x+2$."),
       ch("$x=2$ only", "$x=2$ is a critical point (local maximum), not an inflection point.")],
      "Differentiate twice with the product rule and chain rule, factor out $e^{-x}$ and solve the quadratic.")

# 13. Rolle: how many c
f = x**3 - 3 * x
assert f.subs(x, sqrt(3)) == 0 and f.subs(x, -sqrt(3)) == 0
B.mcq(T_MVT, "For $f(x)=x^3-3x$ on the interval $\\left[-\\sqrt3,\\sqrt3\\right]$, how many values of $c$ in the open interval satisfy $f'(c)=0$?",
      ch(2, "$f(-\\sqrt3)=f(\\sqrt3)=0$, so Rolle's Theorem applies. $f'(c)=3c^2-3=0$ gives $c=1$ and $c=-1$, both inside the interval: two values."),
      [ch(1, "Rolle's Theorem guarantees at least one such $c$, but here the equation $3c^2-3=0$ has two solutions, both in the interval."),
       ch(0, "$f$ is continuous and differentiable and $f(-\\sqrt3)=f(\\sqrt3)$, so Rolle's Theorem guarantees at least one value."),
       ch(3, "$f'(c)=3c^2-3$ is a quadratic, so it has at most two zeros.")],
      "Rolle's Theorem guarantees at least one value; solving $f'(c)=0$ shows exactly how many there are.")

# 14. rectangle under a parabola
A = 2 * x * (12 - x**2)
xm = [s_ for s_ in solve(diff(A, x), x) if s_ > 0]
assert xm == [2] and A.subs(x, 2) == 32
B.mcq(T_OPT, "A rectangle has its base on the $x$-axis and its two upper vertices on the graph of $y=12-x^2$, symmetric about the $y$-axis. What is the largest possible area of such a rectangle?",
      ch(32, "With the right vertices at $(x,12-x^2)$, the width is $2x$, so $A=2x(12-x^2)=24x-2x^3$. $A'=24-6x^2=0$ gives $x=2$, and $A(2)=2\\cdot2\\cdot8=32$."),
      [ch(16, "This uses a width of $x$ instead of $2x$. The rectangle is symmetric, extending from $-x$ to $x$."),
       ch(48, "This uses a height of 12 (the maximum of the parabola) rather than $12-x^2=8$ at $x=2$."),
       ch(22, "This is $A(1)=2\\cdot1\\cdot11$, a value on the way but not the maximum. Set $A'(x)=0$ to find the optimal $x$.")],
      "Write the area as a function of $x$ (width $2x$, height $12-x^2$), find the critical number and confirm it gives a maximum.")

# 15. critical numbers versus local extrema
fp = 5 * x**2 * (x**2 - 3)
B.mcq(T_EXT, "The derivative of $f$ is $f'(x)=5x^2(x^2-3)$. How many critical numbers and how many local extrema does $f$ have?",
      ch("3 critical numbers and 2 local extrema", "$f'=0$ at $x=0$ and $x=\\pm\\sqrt3$: three critical numbers. $f'$ changes sign at $\\pm\\sqrt3$ (local maximum at $-\\sqrt3$, minimum at $\\sqrt3$) but not at 0, because $x^2$ keeps its sign."),
      [ch("3 critical numbers and 3 local extrema", "At $x=0$ the factor $x^2$ does not change sign and $x^2-3<0$ on both sides, so $f'<0$ on both sides and there is no extremum at 0."),
       ch("2 critical numbers and 2 local extrema", "$x=0$ is also a critical number, since $f'(0)=0$. It just is not an extremum."),
       ch("3 critical numbers and 1 local extremum", "$f'$ changes sign at both $-\\sqrt3$ and $\\sqrt3$, so there are two local extrema.")],
      "A critical number is any zero of $f'$ (or a point where $f'$ is undefined); an extremum also requires a sign change of $f'$.")

# ------------------------------------------------------------------ FRQs
dA = graph("x", "f'(x)", 0, 8, -4, 4,
           [{"points": [{"x": 0, "y": -3}, {"x": 2, "y": 3}, {"x": 6, "y": -3}, {"x": 8, "y": -1}], "color": "blue", "label": "f'"}],
           "Graph of f prime made of line segments through (0,-3), (2,3), (6,-3) and (8,-1).")
B.frq(T_CS,
      "The function $f$ is differentiable on $[0,8]$. The graph of $f'$, the derivative of $f$, is shown. It consists of line segments, with $f(3)=6$.\n\n**(a)** On what intervals is $f$ increasing? Justify your answer.\n\n**(b)** Find the $x$-coordinate of each local extremum of $f$ on $(0,8)$, and classify each as a local maximum or a local minimum. Justify your answer.\n\n**(c)** On what intervals is the graph of $f$ concave up? Find the $x$-coordinates of all points of inflection and justify your answer.\n\n**(d)** Find an equation of the line tangent to the graph of $f$ at $x=3$. Is the $y$-value of this line at $x=3.2$ greater than or less than $f(3.2)$? Justify your answer.",
      [(1, "(a) Finds where $f'>0$ using the graph: $f'$ crosses zero at $x=1$ and $x=4$, so $f$ is increasing on $(1,4)$"),
       (1, "(b) Identifies a local minimum at $x=1$ ($f'$ changes from negative to positive)"),
       (1, "(b) Identifies a local maximum at $x=4$ ($f'$ changes from positive to negative) and notes $f'$ has no other sign changes on $(0,8)$"),
       (1, "(c) States concave up where $f'$ is increasing: $(0,2)$ and $(6,8)$"),
       (1, "(c) Gives inflection points at $x=2$ and $x=6$ because $f'$ changes from increasing to decreasing and back"),
       (1, "(d) Finds $f'(3)=1.5$ and the tangent line $y-6=1.5(x-3)$"),
       (1, "(d) Concludes the tangent value is greater, since $f'$ is decreasing near $x=3$ so $f$ is concave down")],
      "(a) $f'>0$ when its graph is above the axis. The segment from $(0,-3)$ to $(2,3)$ crosses the axis at $x=1$, and the segment from $(2,3)$ to $(6,-3)$ crosses at $x=4$. So $f'>0$ on $(1,4)$ and $f$ is increasing on $[1,4]$.\n(b) $f'$ changes from negative to positive at $x=1$, so $f$ has a local minimum there. $f'$ changes from positive to negative at $x=4$, so $f$ has a local maximum there. $f'$ is negative on $(4,8)$, so there are no other sign changes.\n(c) $f$ is concave up where $f'$ is increasing: on $(0,2)$ and $(6,8)$. $f'$ changes from increasing to decreasing at $x=2$ and from decreasing to increasing at $x=6$, so the inflection points are at $x=2$ and $x=6$.\n(d) The slope of $f'$ between $x=2$ and $x=6$ is $\\frac{-3-3}{4}=-1.5$, so $f'(3)=3-1.5=1.5$. The tangent line is $y-6=1.5(x-3)$. At $x=3.2$ it gives $6.3$. Since $f'$ is decreasing near $x=3$, $f$ is concave down there, so the graph lies below its tangent line: the tangent line value is greater than $f(3.2)$.",
      diagram=dA)

rr = symbols("rr", positive=True)
hh = (24 - 2 * rr - pi * rr) / 2
Ar = 2 * rr * hh + pi * rr**2 / 2
rstar = solve(diff(Ar, rr), rr)[0]
assert simplify(rstar - 24 / (4 + pi)) == 0
assert simplify(Ar.subs(rr, rstar) - 288 / (4 + pi)) == 0
assert simplify(hh.subs(rr, rstar) - rstar) == 0
B.frq(T_OPT,
      "A window is made in the shape of a rectangle of width $2r$ and height $h$, topped by a semicircle of radius $r$ (the semicircle's diameter is the top side of the rectangle). The perimeter of the whole window, including the bottom side of the rectangle, is 24 feet.\n\n**(a)** Show that $h=\\dfrac{24-(2+\\pi)r}{2}$.\n\n**(b)** Write the area $A(r)$ of the window in terms of $r$ only.\n\n**(c)** Find the value of $r$ that maximizes the area. Justify that this value gives an absolute maximum.\n\n**(d)** Find the maximum area.\n\n**(e)** Show that, for the window of maximum area, $h=r$.",
      [(1, "(a) Writes the perimeter $2r+2h+\\pi r=24$ and solves for $h$"),
       (1, "(b) Writes $A=2rh+\\frac12\\pi r^2$ and substitutes to get $A(r)=24r-2r^2-\\frac{\\pi}{2}r^2$"),
       (1, "(c) Finds $A'(r)=24-(4+\\pi)r=0$, so $r=\\frac{24}{4+\\pi}$"),
       (1, "(c) Justifies a maximum, for example $A''(r)=-(4+\\pi)<0$, or that $A$ is a downward parabola, and checks $h>0$"),
       (1, "(d) Gives $A_{\\max}=\\frac{288}{4+\\pi}$"),
       (1, "(e) Substitutes $r=\\frac{24}{4+\\pi}$ into the formula for $h$ and simplifies to $h=r$")],
      "(a) The perimeter is the bottom ($2r$), two sides ($2h$) and the semicircular arc ($\\pi r$): $2r+2h+\\pi r=24$, so $h=\\frac{24-2r-\\pi r}{2}=\\frac{24-(2+\\pi)r}{2}$.\n(b) $A=2rh+\\frac12\\pi r^2=r\\left(24-(2+\\pi)r\\right)+\\frac\\pi2r^2=24r-2r^2-\\frac\\pi2r^2$.\n(c) $A'(r)=24-4r-\\pi r=24-(4+\\pi)r$, which is 0 at $r=\\frac{24}{4+\\pi}$. $A''(r)=-(4+\\pi)<0$ for all $r$, so $A$ is concave down everywhere and the critical number gives the absolute maximum on the domain. At this $r$, $h>0$ (see (e)), so it is a valid window.\n(d) $A=24r-\\frac{4+\\pi}{2}r^2$. With $(4+\\pi)r=24$: $A=24r-12r=12r=\\frac{288}{4+\\pi}$ square feet.\n(e) $h=\\frac{24-(2+\\pi)r}{2}$ with $r=\\frac{24}{4+\\pi}$: $24-(2+\\pi)\\frac{24}{4+\\pi}=\\frac{24(4+\\pi)-24(2+\\pi)}{4+\\pi}=\\frac{48}{4+\\pi}$, so $h=\\frac{24}{4+\\pi}=r$.")

B.save()
B.show()
