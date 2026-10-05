from lib import *

B = Bank(2, "unit-2-differentiation-definition-and-properties")
T_AVG, T_DD, T_PW, T_TR, T_PQ = (
    "average-vs-instantaneous-rate-of-change",
    "derivative-definition-and-differentiability",
    "power-rule-and-basic-derivatives",
    "derivatives-of-trig-exponential-log",
    "sum-difference-product-quotient-rules",
)

# 1. simplify first, then differentiate
f = (3 * x**3 + 4 * x - sqrt(x)) / x**2
simp = 3 * x + 4 / x - x ** Rational(-3, 2)
assert simplify(f - simp) == 0
fp = diff(simp, x)
right = fp.subs(x, 4)
assert right == Rational(179, 64)
e1 = (diff(3 * x**3 + 4 * x - sqrt(x), x) / diff(x**2, x)).subs(x, 4)
e2 = (3 - 4 / x**2 - Rational(3, 2) * x ** Rational(-5, 2)).subs(x, 4)
e3 = (3 - 4 / x + Rational(3, 2) * x ** Rational(-5, 2)).subs(x, 4)
B.mcq(T_PQ, "Let $f(x)=\\dfrac{3x^3+4x-\\sqrt{x}}{x^2}$. What is $f'(4)$?",
      ch(right, "Split the fraction first: $f(x)=3x+4x^{-1}-x^{-3/2}$. Then $f'(x)=3-4x^{-2}+\\frac32x^{-5/2}$, and $f'(4)=3-\\frac14+\\frac{3}{2\\cdot32}=\\frac{179}{64}$."),
      [ch(e1, "This divides the derivative of the numerator by the derivative of the denominator. The quotient rule is not 'derivative over derivative'."),
       ch(e2, "The last term has the wrong sign: $-x^{-3/2}$ differentiates to $-(-\\frac32)x^{-5/2}=+\\frac32x^{-5/2}$."),
       ch(e3, "The derivative of $4x^{-1}$ is $-4x^{-2}$, not $-4x^{-1}$. The exponent must drop by one and the old exponent comes down as a factor.")],
      "Dividing each term by $x^2$ turns the quotient into a sum of powers, so the power rule applies term by term. Evaluate only after differentiating.")

# 2. normal line equation
f = x**3 - 4 * x + 1
slope = diff(f, x).subs(x, 2)
assert slope == 8 and f.subs(x, 2) == 1
B.mcq(T_PW, "What is an equation of the line normal to the graph of $f(x)=x^3-4x+1$ at the point $(2,1)$?",
      ch("$y-1=-\\dfrac18(x-2)$", "$f'(2)=3(4)-4=8$, so the tangent slope is 8 and the normal (perpendicular) slope is $-\\frac18$."),
      [ch("$y-1=8(x-2)$", "This is the tangent line. The normal line is perpendicular to it."),
       ch("$y-1=\\dfrac18(x-2)$", "This takes the reciprocal of 8 but not the negative. Perpendicular slopes multiply to $-1$."),
       ch("$y-1=-8(x-2)$", "This negates the slope but does not take the reciprocal. $8\\cdot(-8)=-64$, not $-1$.")],
      "The normal line passes through the point with slope $-\\frac{1}{f'(2)}$.")

# 3. tangent lines through an external point
t0 = symbols("t0", real=True)
eq = Eq(5, 2 * t0 * 3 - t0**2)
roots = solve(eq, t0)
assert sorted(roots) == [1, 5]
B.mcq(T_PW, "Two lines through the point $(3,5)$ are tangent to the graph of $y=x^2$. What is the sum of the $x$-coordinates of the two points of tangency?",
      ch(6, "A tangent line at $x=t$ is $y=2tx-t^2$. It passes through $(3,5)$ when $5=6t-t^2$, i.e. $t^2-6t+5=0$, so $t=1$ or $t=5$. The sum is 6."),
      [ch(5, "5 is one of the points of tangency (it is also the product of the two roots), not the sum."),
       ch(3, "3 is the $x$-coordinate of the given point, which is not on the parabola ($3^2=9\\neq5$)."),
       ch(1, "1 is one of the two points of tangency. The question asks for the sum of both.")],
      "Write the tangent line at a general point $x=t$, force it through $(3,5)$, and solve for $t$.")

# 4. horizontal tangents, points not x-values
f = x**4 - 4 * x**3 + 2
crit = solve(diff(f, x), x)
assert sorted(crit) == [0, 3] and f.subs(x, 0) == 2 and f.subs(x, 3) == -25
B.mcq(T_PW, "At which points does the graph of $f(x)=x^4-4x^3+2$ have a horizontal tangent line?",
      ch("$(0,2)$ and $(3,-25)$", "$f'(x)=4x^3-12x^2=4x^2(x-3)=0$ gives $x=0$ and $x=3$. The points on the graph are $(0,f(0))=(0,2)$ and $(3,f(3))=(3,-25)$."),
      [ch("$(3,-25)$ only", "Dividing $4x^3-12x^2=0$ by $x^2$ loses the solution $x=0$. Factor instead of dividing."),
       ch("$x=0$ and $x=3$", "These are the right $x$-values, but the question asks for points on the graph, which need $y$-coordinates too."),
       ch("$(0,0)$ and $(3,0)$", "The $y$-coordinates are $f(0)$ and $f(3)$, not 0. A horizontal tangent has slope 0; the function value there need not be 0.")],
      "Set $f'(x)=0$ by factoring, then substitute each solution into $f$ (not $f'$) to get the point.")

# 5. differentiability determines both constants
aa, bb = symbols("aa bb", real=True)
sol = solve([Eq(aa + bb, 2 - 3), Eq(2 * aa + bb, 6)], [aa, bb])
assert sol == {aa: 7, bb: -8}
B.mcq(T_DD,
      "Let $f(x)=\\begin{cases}ax^2+bx & x<1\\\\ 2x^3-3 & x\\ge1\\end{cases}$. For which values of $a$ and $b$ is $f$ differentiable at $x=1$?",
      ch("$a=7,\\ b=-8$", "Continuity at 1: $a+b=2-3=-1$. Matching slopes: $2a+b=6$ (the right-hand derivative $6x^2$ at 1). Subtracting gives $a=7$, then $b=-8$."),
      [ch("$a=5,\\ b=-6$", "These satisfy continuity ($5-6=-1$) but the slopes do not match: $2(5)-6=4\\neq6$. Differentiability needs both conditions."),
       ch("$a=6,\\ b=-6$", "These match the slopes ($12-6=6$) but not the values: $6-6=0\\neq-1$. A function must be continuous before it can be differentiable."),
       ch("$a=-7,\\ b=8$", "This has the signs reversed. Check: $a+b=1$, not $-1$.")],
      "Differentiable at 1 requires two equations: the pieces meet ($a+b=-1$) and the one-sided derivatives agree ($2a+b=6$).")

# 6. derivative as a limit (log)
B.mcq(T_DD, "What is $\\displaystyle\\lim_{h\\to0}\\frac{\\ln(e^2+h)-2}{h}$?",
      ch("$\\dfrac{1}{e^2}$", "Since $\\ln(e^2)=2$, this is $\\lim_{h\\to0}\\frac{f(e^2+h)-f(e^2)}{h}$ for $f(x)=\\ln x$, which is $f'(e^2)=\\frac1{e^2}$."),
      [ch("$\\dfrac1e$", "$f'(x)=\\frac1x$ is evaluated at $x=e^2$, not at $x=e$."),
       ch(2, "2 is the value $f(e^2)$, not the derivative."),
       ch("$e^2$", "This is the reciprocal of $f'(e^2)$. The derivative of $\\ln x$ is $\\frac1x$, so at $e^2$ it is $\\frac{1}{e^2}$.")],
      "Recognize the limit definition of the derivative of $f(x)=\\ln x$ at $a=e^2$.")

# 7. derivative as a limit (trig)
B.mcq(T_DD, "What is $\\displaystyle\\lim_{h\\to0}\\frac{\\tan\\left(\\frac{\\pi}{4}+h\\right)-1}{h}$?",
      ch(2, "This is $f'(\\frac\\pi4)$ for $f(x)=\\tan x$ (note $\\tan\\frac\\pi4=1$). $f'(x)=\\sec^2x$, and $\\sec^2\\frac\\pi4=(\\sqrt2)^2=2$."),
      [ch(1, "1 is the value of $\\tan\\frac\\pi4$. The limit is the derivative, $\\sec^2\\frac\\pi4$."),
       ch(Rational(1, 2), "$\\frac12$ is $\\cos^2\\frac\\pi4$, the reciprocal of the correct $\\sec^2\\frac\\pi4$."),
       ch(sqrt(2), "$\\sqrt2$ is $\\sec\\frac\\pi4$. The derivative of $\\tan x$ is $\\sec^2 x$, so the value is squared.")],
      "Recognize the difference quotient for $f(x)=\\tan x$ at $x=\\frac\\pi4$.")

# 8. interpreting a limit expression, two shifted inputs
B.mcq(T_DD, "The function $f$ is differentiable at $x=3$ and $\\displaystyle\\lim_{h\\to0}\\frac{f(3+2h)-f(3-h)}{h}=12$. What is $f'(3)$?",
      ch(4, "Insert $f(3)$: $\\frac{f(3+2h)-f(3)}{h}+\\frac{f(3)-f(3-h)}{h}$. The first piece tends to $2f'(3)$ and the second to $f'(3)$, so the limit is $3f'(3)=12$ and $f'(3)=4$."),
      [ch(12, "12 is the value of the limit, not of $f'(3)$. The step sizes $2h$ and $-h$ change the multiple of $f'(3)$ that the limit equals."),
       ch(6, "This divides by 2, accounting only for the $2h$ and ignoring that the $-h$ side contributes a second copy of $f'(3)$."),
       ch(-4, "A negative answer comes from subtracting the second piece. Write $f(3+2h)-f(3-h)=[f(3+2h)-f(3)]+[f(3)-f(3-h)]$: both pieces are positive multiples of $f'(3)$, so the limit is $+3f'(3)$.")],
      "Split the numerator at $f(3)$. Each half is a difference quotient with a step that is a multiple of $h$.")

# 9. product of three factors, evaluated where one factor is zero
f = x**2 * exp(x) * log(x)
assert diff(f, x).subs(x, 1) == E
B.mcq(T_PQ, "If $y=x^2e^x\\ln x$, what is $\\dfrac{dy}{dx}$ at $x=1$?",
      ch("$e$", "Product rule on three factors: $y'=2xe^x\\ln x+x^2e^x\\ln x+x^2e^x\\cdot\\frac1x$. At $x=1$, $\\ln1=0$ kills the first two terms and the last is $1\\cdot e\\cdot1=e$."),
      [ch(0, "Only the terms that keep $\\ln x$ vanish at $x=1$. The term where $\\ln x$ is differentiated to $\\frac1x$ survives."),
       ch("$2e$", "This multiplies the three derivatives, $(2x)(e^x)(\\frac1x)$, which is not the product rule."),
       ch("$3e$", "This counts each of the three product-rule terms as $e$. Two of the three terms contain $\\ln 1=0$.")],
      "Differentiate one factor at a time, keep the other two, and add. Substitute at the end.")

# 10. quotient rule with trig, simplified
f = (1 + cos(x)) / sin(x)
val = diff(f, x).subs(x, pi / 3)
assert simplify(val) == -2
bad1 = (((-sin(x)) * sin(x) + (1 + cos(x)) * cos(x)) / sin(x) ** 2).subs(x, pi / 3)
bad2 = (-sin(x) / cos(x)).subs(x, pi / 3)
bad3 = (-sin(x) / sin(x) ** 2).subs(x, pi / 3)
B.mcq(T_PQ, "If $f(x)=\\dfrac{1+\\cos x}{\\sin x}$, what is $f'\\left(\\dfrac{\\pi}{3}\\right)$?",
      ch(-2, "$f'(x)=\\frac{(-\\sin x)(\\sin x)-(1+\\cos x)(\\cos x)}{\\sin^2x}=-\\frac{1+\\cos x}{\\sin^2x}=-\\frac{1}{1-\\cos x}$. At $x=\\frac\\pi3$, $\\cos x=\\frac12$, so $f'=-\\frac{1}{1/2}=-2$."),
      [ch(simplify(bad1), "The quotient rule subtracts: low times d(high) minus high times d(low). Adding the second product gives a different (and wrong) numerator."),
       ch(simplify(bad2), "This is $\\frac{(1+\\cos x)'}{(\\sin x)'}$. The quotient rule is not derivative over derivative."),
       ch(simplify(bad3), "This differentiates only the numerator and divides by $\\sin^2 x$, leaving out the term from differentiating the denominator.")],
      "Use $\\sin^2x+\\cos^2x=1$ to simplify $-\\sin^2x-\\cos x-\\cos^2x=-(1+\\cos x)$ before substituting.")

# 11. tangent line x-intercept
f = x * exp(x) / (x + 1)
fp = simplify(diff(f, x))
assert simplify(fp - exp(x) * (x**2 + x + 1) / (x + 1) ** 2) == 0
xint = simplify(1 - f.subs(x, 1) / fp.subs(x, 1))
assert xint == Rational(1, 3)
B.mcq(T_PQ, "Let $f(x)=\\dfrac{xe^x}{x+1}$. The line tangent to the graph of $f$ at $x=1$ crosses the $x$-axis at $x=$",
      ch(Rational(1, 3), "$f'(x)=\\frac{e^x(x^2+x+1)}{(x+1)^2}$, so $f'(1)=\\frac{3e}{4}$ and $f(1)=\\frac e2$. The tangent is $y-\\frac e2=\\frac{3e}{4}(x-1)$. Setting $y=0$: $x-1=-\\frac{e/2}{3e/4}=-\\frac23$, so $x=\\frac13$."),
      [ch(Rational(2, 3), "$\\frac23$ is the horizontal distance from the point of tangency to the axis crossing, $\\frac{f(1)}{f'(1)}$. The crossing is that far to the left of $x=1$."),
       ch(Rational(5, 3), "This adds the distance $\\frac23$ to $x=1$. The tangent has positive slope and the point $(1,\\frac e2)$ is above the axis, so the line reaches the axis to the left."),
       ch("$\\dfrac{1}{e}$", "The factors of $e$ cancel in $\\frac{f(1)}{f'(1)}$; the answer is rational.")],
      "Find $f'(1)$ with the quotient and product rules, write the tangent line, and solve for $x$ when $y=0$: $x=1-\\frac{f(1)}{f'(1)}$.")

# 12. average vs instantaneous
f = x**3 - 6 * x
avg = (f.subs(x, 3) - f.subs(x, 0)) / 3
assert avg == 3
cs = [s for s in solve(Eq(diff(f, x), 3), x) if 0 < s < 3]
assert cs == [sqrt(3)]
B.mcq(T_AVG, "For $f(x)=x^3-6x$, at what value of $x$ in the interval $(0,3)$ is the instantaneous rate of change equal to the average rate of change over $[0,3]$?",
      ch(sqrt(3), "The average rate is $\\frac{f(3)-f(0)}{3}=\\frac{9-0}{3}=3$. Solve $f'(x)=3x^2-6=3$: $x^2=3$, so $x=\\sqrt3$ (the root $-\\sqrt3$ is outside the interval)."),
      [ch(Rational(3, 2), "$\\frac32$ is the midpoint of the interval. The point where the two rates agree is generally not the midpoint."),
       ch(3, "3 is the value of the average rate of change, not the $x$-value where $f'(x)$ equals it. Also, 3 is the endpoint of the interval."),
       ch(-sqrt(3), "$-\\sqrt3$ also satisfies $3x^2-6=3$, but it is not in $(0,3)$.")],
      "Compute the average rate of change, then solve $f'(x)=$ that value and keep only the solution in the interval.")

# 13. continuous but not differentiable
assert limit(x * Abs(x) / x, x, 0) == 0 and limit(x * sin(1 / x), x, 0) == 0
assert limit(Abs(x) ** Rational(1, 2), x, 0) == 0
assert limit(cbrt(x) ** -1 if False else 1 / cbrt(x), x, 0, "+") == oo
B.mcq(T_DD, "Which of the following functions is continuous at $x=0$ but NOT differentiable at $x=0$?",
      ch("$k(x)=x^{2/3}$", "$\\frac{k(h)-k(0)}{h}=h^{-1/3}$, which is unbounded as $h\\to0$ (it tends to $+\\infty$ from the right and $-\\infty$ from the left). $k$ is continuous with a cusp at 0, so no derivative exists."),
      [ch("$f(x)=x|x|$", "$\\frac{f(h)-f(0)}{h}=\\frac{h|h|}{h}=|h|\\to0$, so $f'(0)=0$. It is differentiable."),
       ch("$g(x)=x^2\\sin\\left(\\frac1x\\right)$ for $x\\neq0$, with $g(0)=0$", "$\\frac{g(h)-g(0)}{h}=h\\sin\\frac1h\\to0$ by the Squeeze Theorem, so $g'(0)=0$. It oscillates, but it is differentiable at 0."),
       ch("$p(x)=|x|^{3/2}$", "$\\frac{p(h)-p(0)}{h}=\\frac{|h|^{3/2}}{h}$, which has absolute value $|h|^{1/2}\\to0$. So $p'(0)=0$ and $p$ is differentiable.")],
      "Check the difference quotient at 0 for each. Only $x^{2/3}$ gives a quotient that does not settle to a number.")

# 14. table data with product and quotient
fv, fpv, gv, gpv = 2, -3, 4, 5
K = (x**2 * symbols("F") / symbols("G"))
Fv, Gv = symbols("F G")
kp = ((2 * 1 * fv + 1 * fpv) * gv - 1 * fv * gpv) / Rational(gv**2)
assert kp == Rational(-3, 8)
w1 = (1 * fpv * gv - 1 * fv * gpv) / Rational(gv**2)
w2 = ((2 * fv + fpv) * gv + fv * gpv) / Rational(gv**2)
w3 = ((2 * fv + fpv) * gv - fv * gpv) / Rational(gv)
B.mcq(T_PQ, "Let $k(x)=\\dfrac{x^2f(x)}{g(x)}$, where $f(1)=2$, $f'(1)=-3$, $g(1)=4$ and $g'(1)=5$. What is $k'(1)$?",
      ch(Rational(-3, 8), "Numerator $N=x^2f$: $N'=2xf+x^2f'$, so $N(1)=2$ and $N'(1)=4-3=1$. Then $k'(1)=\\frac{N'g-Ng'}{g^2}=\\frac{1\\cdot4-2\\cdot5}{16}=-\\frac38$."),
      [ch(w1, "This treats $x^2$ as a constant multiplier and drops the term $2xf$ that comes from differentiating $x^2$ in the product."),
       ch(w2, "The quotient rule subtracts the second product: $N'g-Ng'$. Adding $Ng'$ gives the wrong sign."),
       ch(w3, "The denominator of the quotient rule is $g^2=16$, not $g=4$.")],
      "Treat $x^2f(x)$ as one numerator function (product rule inside), then apply the quotient rule.")

# 15. normal line x-intercept
f = sqrt(x)
sl = diff(f, x).subs(x, 4)
assert sl == Rational(1, 4)
xi = 4 + Rational(2) / 4
assert xi == Rational(9, 2)
B.mcq(T_PW, "The line normal to the graph of $y=\\sqrt{x}$ at the point $(4,2)$ crosses the $x$-axis at $x=$",
      ch(Rational(9, 2), "$y'=\\frac1{2\\sqrt x}=\\frac14$ at $x=4$, so the normal slope is $-4$: $y-2=-4(x-4)$. At $y=0$: $x-4=\\frac12$, so $x=\\frac92$."),
      [ch(-4, "This is where the tangent line (slope $\\frac14$) crosses the axis: $0-2=\\frac14(x-4)$ gives $x=-4$."),
       ch(Rational(7, 2), "This has the sign wrong in $x-4=\\frac12$. The normal slope is negative, so the line falls from $(4,2)$ and reaches the axis to the right."),
       ch(Rational(1, 2), "This solves $x-4=\\frac12$ but forgets to add back the 4.")],
      "Find the slope of the tangent, take the negative reciprocal, write the normal line, and set $y=0$.")

# ------------------------------------------------------------------ FRQs
q = (4 * x**3 - 6 * x + sqrt(x)) / x**2
qp = diff(4 * x - 6 / x + x ** Rational(-3, 2), x)
assert simplify(diff(q, x) - qp) == 0
p = x**3 - 3 * x**2 - 9 * x + 4
assert solve(diff(p, x), x) == [-1, 3] or sorted(solve(diff(p, x), x)) == [-1, 3]
assert p.subs(x, 3) == -23 and p.subs(x, -1) == 9
g = 2 * x**2 - 8 * x + 5
assert diff(g, x).subs(x, 3) == 4 and g.subs(x, 3) == -1
B.frq(T_PQ,
      "**(a)** Let $q(x)=\\dfrac{4x^3-6x+\\sqrt{x}}{x^2}$. Rewrite $q$ as a sum of power functions, then find $q'(x)$. Do not use the quotient rule.\n\n**(b)** Find an equation of the tangent line, and an equation of the normal line, to the graph of $g(x)=2x^2-8x+5$ at the point $(3,-1)$.\n\n**(c)** Find all points on the graph of $p(x)=x^3-3x^2-9x+4$ at which the tangent line is horizontal.\n\n**(d)** Use the limit definition of the derivative to find $s'(t)$ for $s(t)=80t-5t^2$. Show each step of your work.",
      [(1, "(a) Rewrites $q(x)=4x-6x^{-1}+x^{-3/2}$"),
       (1, "(a) Differentiates correctly: $q'(x)=4+6x^{-2}-\\frac32x^{-5/2}$"),
       (1, "(b) Finds $g'(3)=4$ and the tangent line $y+1=4(x-3)$"),
       (1, "(b) Uses slope $-\\frac14$ for the normal line: $y+1=-\\frac14(x-3)$"),
       (1, "(c) Solves $p'(x)=3(x-3)(x+1)=0$ for $x=3$ and $x=-1$"),
       (1, "(c) Gives both points with $y$-values: $(3,-23)$ and $(-1,9)$"),
       (1, "(d) Sets up $\\lim_{h\\to0}\\frac{s(t+h)-s(t)}{h}$ and expands correctly"),
       (1, "(d) Simplifies to $80-10t-5h$ and takes the limit to get $80-10t$")],
      "(a) $q(x)=4x-6x^{-1}+x^{-3/2}$, so $q'(x)=4+6x^{-2}-\\frac32x^{-5/2}$.\n(b) $g'(x)=4x-8$, so $g'(3)=4$. Tangent: $y+1=4(x-3)$. Normal slope is $-\\frac14$: $y+1=-\\frac14(x-3)$.\n(c) $p'(x)=3x^2-6x-9=3(x-3)(x+1)$, which is 0 at $x=3$ and $x=-1$. $p(3)=27-27-27+4=-23$ and $p(-1)=-1-3+9+4=9$. The points are $(3,-23)$ and $(-1,9)$.\n(d) $s'(t)=\\lim_{h\\to0}\\frac{80(t+h)-5(t+h)^2-80t+5t^2}{h}=\\lim_{h\\to0}\\frac{80h-10th-5h^2}{h}=\\lim_{h\\to0}(80-10t-5h)=80-10t$.")

# FRQ: differentiability of a piecewise function
f_left = x**2 - 4 * x + 7
f_right = 2 * x - 2
assert f_left.subs(x, 3) == f_right.subs(x, 3) == 4
assert diff(f_left, x).subs(x, 3) == diff(f_right, x).subs(x, 3) == 2
mm, nn = symbols("mm nn", real=True)
sol = solve([Eq(f_left.subs(x, 3), mm * 3 + nn), Eq(diff(f_left, x).subs(x, 3), mm)], [mm, nn])
assert sol == {mm: 2, nn: -2}
B.frq(T_DD,
      "Let $f(x)=\\begin{cases}x^2-4x+7 & x<3\\\\ 2x-2 & x\\ge3\\end{cases}$.\n\n**(a)** Show that $f$ is continuous at $x=3$.\n\n**(b)** Find $\\lim_{x\\to3^-}f'(x)$ and $\\lim_{x\\to3^+}f'(x)$.\n\n**(c)** Is $f$ differentiable at $x=3$? Justify your answer using one-sided derivatives, and give an equation for the tangent line at $x=3$ if it exists.\n\n**(d)** Let $g(x)=\\begin{cases}x^2-4x+7 & x<3\\\\ mx+n & x\\ge3\\end{cases}$. Find the values of $m$ and $n$ for which $g$ is differentiable at $x=3$.",
      [(1, "(a) Shows the left limit, right limit and $f(3)$ all equal 4"),
       (1, "(b) Finds $f'(x)=2x-4$ for $x<3$ and $f'(x)=2$ for $x>3$, with both one-sided limits equal to 2"),
       (1, "(c) Concludes $f$ is differentiable at 3 because it is continuous and the one-sided derivatives agree ($f'(3)=2$)"),
       (1, "(c) Gives the tangent line $y-4=2(x-3)$, that is $y=2x-2$"),
       (1, "(d) Sets $m=g'(3^-)=2$"),
       (1, "(d) Uses continuity to find $n=-2$")],
      "(a) $\\lim_{x\\to3^-}f(x)=9-12+7=4$, $\\lim_{x\\to3^+}f(x)=6-2=4$ and $f(3)=2(3)-2=4$. All equal, so $f$ is continuous at 3.\n(b) For $x<3$, $f'(x)=2x-4\\to2$. For $x>3$, $f'(x)=2$. Both one-sided limits are 2.\n(c) $f$ is continuous at 3 and the left and right derivatives are both 2, so $f$ is differentiable at 3 with $f'(3)=2$. Tangent line: $y-4=2(x-3)$, i.e. $y=2x-2$.\n(d) The slope must match the left piece: $m=2(3)-4=2$. The pieces must meet: $3m+n=4$, so $n=4-6=-2$.")

B.save()
B.show()
