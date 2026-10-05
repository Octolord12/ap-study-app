from lib import *

B = Bank(3, "unit-3-differentiation-composite-implicit-inverse")
T_CH, T_IM, T_INV, T_HO = ("chain-rule", "implicit-differentiation", "derivatives-of-inverse-functions", "higher-order-derivatives")

# 1. nested chain rule evaluated where trig values matter
f = exp(sin(x**2))
d = diff(f, x)
v = simplify(d.subs(x, sqrt(pi)))
assert v == -2 * sqrt(pi)
e1 = simplify((exp(sin(x**2)) * cos(x**2)).subs(x, sqrt(pi)))
e3 = simplify((exp(sin(x**2)) * cos(x**2) * 2).subs(x, sqrt(pi)))
B.mcq(T_CH, "If $y=e^{\\sin(x^2)}$, what is $\\dfrac{dy}{dx}$ at $x=\\sqrt{\\pi}$?",
      ch(-2 * sqrt(pi), "$\\frac{dy}{dx}=e^{\\sin(x^2)}\\cdot\\cos(x^2)\\cdot2x$. At $x=\\sqrt\\pi$: $x^2=\\pi$, $\\sin\\pi=0$, $\\cos\\pi=-1$, so $1\\cdot(-1)\\cdot2\\sqrt\\pi=-2\\sqrt\\pi$."),
      [ch(e1, "This stops after two layers. There are three: the outer $e^{(\\ )}$, the middle $\\sin(\\ )$ and the inner $x^2$, whose derivative $2x$ is also a factor."),
       ch(2 * sqrt(pi), "The sign is wrong: $\\cos\\pi=-1$, so the factor $\\cos(x^2)$ is negative at this point."),
       ch(e3, "The derivative of the inner function $x^2$ is $2x$, which at $x=\\sqrt\\pi$ is $2\\sqrt\\pi$, not 2.")],
      "Differentiate layer by layer, outside in: $e^u\\to e^u$, then $\\sin w\\to\\cos w$, then $x^2\\to2x$. Multiply, then evaluate.")

# 2. composite inside a product, from a table
f1, fp1, g3, gp3 = 3, -2, 5, 4
Hp = fp1 * g3 + f1 * gp3 * fp1
assert Hp == -34
B.mcq(T_CH, "Let $H(x)=f(x)\\cdot g(f(x))$. Values: $f(1)=3$, $f'(1)=-2$, $g(3)=5$ and $g'(3)=4$. What is $H'(1)$?",
      ch(-34, "Product rule: $H'(x)=f'(x)\\,g(f(x))+f(x)\\,g'(f(x))\\,f'(x)$. At 1: $(-2)(5)+(3)(4)(-2)=-10-24=-34$."),
      [ch(f1 * gp3 + fp1 * g3, "The second term differentiates $g(f(x))$ but leaves out the factor $f'(1)=-2$ from the chain rule."),
       ch(fp1 * gp3, "This multiplies only the two derivative values. The product rule is $u'v+uv'$, not $u'v'$."),
       ch(fp1 * g3 - f1 * gp3 * fp1, "The product rule adds its two terms. Here the second term is $f(1)g'(3)f'(1)=-24$, so subtracting it gives the wrong sign.")],
      "Treat $f(x)$ and $g(f(x))$ as the two factors. Differentiating the second factor needs the chain rule.")

# 3. second derivative by implicit differentiation
F = x**2 + x * y + y**2 - 7
assert F.subs({x: 1, y: 2}) == 0
d1 = idiff(F, y, x)
d2 = idiff(F, y, x, 2)
val1 = d1.subs({x: 1, y: 2})
val2 = simplify(d2.subs({x: 1, y: 2}))
assert val1 == Rational(-4, 5) and val2 == Rational(-42, 125), (val1, val2)
w1 = (-3 * y / (x + 2 * y) ** 2).subs({x: 1, y: 2})
B.mcq(T_IM, "The curve $x^2+xy+y^2=7$ passes through the point $(1,2)$. What is the value of $\\dfrac{d^2y}{dx^2}$ at that point?",
      ch(val2, "First, $\\frac{dy}{dx}=-\\frac{2x+y}{x+2y}$, which is $-\\frac45$ at $(1,2)$. Differentiate again with the quotient rule, treating $y$ as a function of $x$: $\\frac{d^2y}{dx^2}=-\\frac{(2+y')(x+2y)-(2x+y)(1+2y')}{(x+2y)^2}$. At $(1,2)$ this is $-\\frac{42}{125}$."),
      [ch(w1, "This differentiates $-\\frac{2x+y}{x+2y}$ as if $y$ were a constant. Every $y$ in the expression is a function of $x$ and contributes a $\\frac{dy}{dx}$ term."),
       ch(-val2, "The sign is wrong. Carry the negative sign in $\\frac{dy}{dx}=-\\frac{2x+y}{x+2y}$ through the quotient rule."),
       ch(Rational(-42, 5), "$-\\frac{42}{5}$ is only the numerator of the quotient-rule expression. It still has to be divided by $(x+2y)^2=25$.")],
      "Find $y'=-\\frac{2x+y}{x+2y}$, substitute $y'=-\\frac45$ at $(1,2)$ after differentiating a second time (not before).")

# 4. horizontal tangents on a conic
F = x**2 - x * y + y**2 - 3
pts = solve([F, y - 2 * x], [x, y])
assert sorted(pts) == [(-1, -2), (1, 2)]
B.mcq(T_IM, "At which points on the curve $x^2-xy+y^2=3$ is the tangent line horizontal?",
      ch("$(1,2)$ and $(-1,-2)$", "Differentiating: $2x-y-xy'+2yy'=0$, so $y'=\\frac{y-2x}{2y-x}$. A horizontal tangent needs $y=2x$. Substituting: $x^2-2x^2+4x^2=3x^2=3$, so $x=\\pm1$, giving $(1,2)$ and $(-1,-2)$."),
      [ch("$(2,1)$ and $(-2,-1)$", "These are the points where the tangent is vertical ($2y=x$, so the denominator of $y'$ is 0), not horizontal."),
       ch("$(\\sqrt3,0)$ and $(-\\sqrt3,0)$", "These are the $x$-intercepts of the curve. The slope there is $\\frac{0-2\\sqrt3}{0-\\sqrt3}=2$, not 0."),
       ch("$(1,2)$ only", "The curve is symmetric about the origin (replacing $(x,y)$ by $(-x,-y)$ leaves the equation unchanged), so $(-1,-2)$ is also a point with a horizontal tangent.")],
      "A horizontal tangent means $\\frac{dy}{dx}=0$, so the numerator of $\\frac{y-2x}{2y-x}$ is zero. Then use the curve's equation to find the points.")

# 5. inverse function derivative, polynomial
f = x**5 + x**3 + x
assert f.subs(x, 1) == 3
fp = diff(f, x)
B.mcq(T_INV, "Let $f(x)=x^5+x^3+x$, and let $g$ be the inverse function of $f$. What is $g'(3)$?",
      ch(Rational(1, 9), "$f(1)=3$, so $g(3)=1$. Then $g'(3)=\\frac{1}{f'(g(3))}=\\frac{1}{f'(1)}=\\frac1{5+3+1}=\\frac19$."),
      [ch(Rational(1, fp.subs(x, 3)), "This evaluates $f'$ at 3. The formula needs $f'$ at $g(3)=1$, the input of $f$ that produces 3."),
       ch(9, "This is $f'(1)$ itself. The inverse's derivative is the reciprocal."),
       ch(Rational(-1, 9), "The derivative of the inverse is the reciprocal $+\\frac{1}{f'(g(3))}$. No negative sign appears; that belongs to the derivative of $\\frac1x$, not to inverses.")],
      "Find the input $a$ with $f(a)=3$ by inspection, then use $g'(3)=\\frac{1}{f'(a)}$.")

# 6. derivative of arctan of a root
f = atan(sqrt(x))
val = simplify(diff(f, x).subs(x, 4))
assert val == Rational(1, 20)
B.mcq(T_CH, "If $f(x)=\\arctan\\left(\\sqrt{x}\\right)$, what is $f'(4)$?",
      ch(Rational(1, 20), "$f'(x)=\\frac{1}{1+(\\sqrt x)^2}\\cdot\\frac{1}{2\\sqrt x}=\\frac{1}{(1+x)\\,2\\sqrt x}$. At $x=4$: $\\frac{1}{5\\cdot4}=\\frac1{20}$."),
      [ch(Rational(1, 5), "This is $\\frac{1}{1+x}$ alone. The chain rule also multiplies by the derivative of $\\sqrt x$, which is $\\frac1{2\\sqrt x}=\\frac14$."),
       ch(Rational(1, 68), "This uses $\\frac{1}{1+x^2}$. The inside of the arctangent is $\\sqrt x$, so the denominator is $1+(\\sqrt x)^2=1+x$."),
       ch(Rational(1, 4), "This is $\\frac{1}{2\\sqrt x}$ alone; the factor $\\frac{1}{1+x}$ from the arctangent is missing.")],
      "$\\frac{d}{du}\\arctan u=\\frac{1}{1+u^2}$ with $u=\\sqrt x$, times $\\frac{du}{dx}=\\frac{1}{2\\sqrt x}$.")

# 7. log properties before differentiating
f = log((x + 1) ** 2 / sqrt(x + 3))
val = simplify(diff(f, x).subs(x, 1))
assert val == Rational(7, 8)
B.mcq(T_CH, "If $y=\\ln\\left(\\dfrac{(x+1)^2}{\\sqrt{x+3}}\\right)$, what is $\\dfrac{dy}{dx}$ at $x=1$?",
      ch(Rational(7, 8), "Rewrite $y=2\\ln(x+1)-\\frac12\\ln(x+3)$. Then $y'=\\frac{2}{x+1}-\\frac{1}{2(x+3)}$, which is $1-\\frac18=\\frac78$ at $x=1$."),
      [ch(Rational(9, 8), "The second term is subtracted because $\\ln\\frac{A}{B}=\\ln A-\\ln B$, so its derivative is subtracted too."),
       ch(Rational(3, 4), "This forgets the $\\frac12$ from the square root: $\\ln\\sqrt{x+3}=\\frac12\\ln(x+3)$, whose derivative is $\\frac{1}{2(x+3)}=\\frac18$, not $\\frac14$."),
       ch(Rational(3, 8), "This forgets the exponent 2 on $(x+1)$. $\\ln(x+1)^2=2\\ln(x+1)$, whose derivative is $\\frac{2}{x+1}=1$, not $\\frac12$.")],
      "Use $\\ln\\frac AB=\\ln A-\\ln B$ and $\\ln A^p=p\\ln A$ first. Differentiating the sum of simple logs is far easier than applying the chain rule to the whole fraction.")

# 8. second derivative of a composite
f = sin(x**2)
fpp = simplify(diff(f, x, 2).subs(x, sqrt(pi / 3)))
corr = 1 - 2 * sqrt(3) * pi / 3
assert simplify(fpp - corr) == 0
B.mcq(T_HO, "If $f(x)=\\sin(x^2)$, what is $f''\\left(\\sqrt{\\pi/3}\\right)$?",
      ch(corr, "$f'(x)=2x\\cos(x^2)$. By the product and chain rules, $f''(x)=2\\cos(x^2)-4x^2\\sin(x^2)$. At $x^2=\\frac\\pi3$: $2\\cdot\\frac12-4\\cdot\\frac\\pi3\\cdot\\frac{\\sqrt3}2=1-\\frac{2\\sqrt3\\pi}{3}$."),
      [ch(-2 * sqrt(3) * pi / 3, "This keeps only the term that comes from differentiating $\\cos(x^2)$. Differentiating the factor $2x$ in the product also gives $2\\cos(x^2)$."),
       ch(1, "This keeps only $2\\cos(x^2)$ and drops $-4x^2\\sin(x^2)$, which comes from differentiating $\\cos(x^2)$ using the chain rule."),
       ch(1 + 2 * sqrt(3) * pi / 3, "The second term has a negative sign: the derivative of $\\cos u$ is $-\\sin u$.")],
      "Differentiate twice, using the product rule on $2x\\cos(x^2)$ and the chain rule on $\\cos(x^2)$.")

# 9. chain rule with a root, given f'
B.mcq(T_CH, "The function $f$ is differentiable and $f'(4)=3$. If $g(x)=f(\\sqrt{x})$, what is $g'(16)$?",
      ch(Rational(3, 8), "$g'(x)=f'(\\sqrt x)\\cdot\\frac{1}{2\\sqrt x}$. At $x=16$, $\\sqrt{x}=4$: $f'(4)\\cdot\\frac{1}{8}=\\frac38$."),
      [ch(3, "This is $f'(4)$ without the chain-rule factor $\\frac{d}{dx}\\sqrt x$."),
       ch(24, "The derivative of $\\sqrt x$ is $\\frac{1}{2\\sqrt x}$ (a reciprocal), not $2\\sqrt x$."),
       ch(Rational(3, 32), "This evaluates the inner derivative $\\frac{1}{2\\sqrt x}$ with $\\sqrt{x}$ replaced by $x$: $\\frac{1}{2\\cdot16}$. The input of $f'$ is $\\sqrt{16}=4$ and the inner derivative is $\\frac{1}{2\\cdot4}$.")],
      "The derivative of $f(u)$ is $f'(u)\\,u'$ with $u=\\sqrt x$, evaluated at $x=16$ where $u=4$.")

# 10. derivative of a power of an inverse function
B.mcq(T_INV, "The function $f$ is differentiable and one-to-one, with $f(1)=3$ and $f'(1)=-4$. Let $g$ be the inverse of $f$. What is $\\dfrac{d}{dx}\\left[(g(x))^2\\right]$ at $x=3$?",
      ch(Rational(-1, 2), "$g(3)=1$ and $g'(3)=\\frac1{f'(1)}=-\\frac14$. By the chain rule, $\\frac{d}{dx}[g(x)^2]=2g(x)g'(x)=2(1)\\left(-\\frac14\\right)=-\\frac12$."),
      [ch(-8, "This uses $f'(1)=-4$ in place of $g'(3)$ and skips taking the reciprocal. $g'(3)=\\frac{1}{f'(1)}$."),
       ch(Rational(1, 2), "$g'(3)=\\frac{1}{f'(1)}=-\\frac14$ is negative because $f$ is decreasing at 1. The sign does not flip."),
       ch(Rational(-1, 4), "This is $g'(3)$ alone. The power on $g$ contributes the factor $2g(3)=2$.")],
      "First find $g(3)$ and $g'(3)$ from the inverse relationship, then apply the chain rule to $g(x)^2$.")

# 11. folium slope
F = x**3 + y**3 - 6 * x * y
assert F.subs({x: 3, y: 3}) == 0
d = idiff(F, y, x)
slope = d.subs({x: 3, y: 3})
assert slope == -1
w2 = ((6 * y - 3 * x**2) / (3 * y**2)).subs({x: 3, y: 3})
w3 = ((3 * x**2 + 3 * y**2 - 6 * y) / (6 * x)).subs({x: 3, y: 3})
B.mcq(T_IM, "The point $(3,3)$ lies on the curve $x^3+y^3=6xy$. What is the slope of the tangent line to the curve at that point?",
      ch(-1, "Differentiate: $3x^2+3y^2y'=6y+6xy'$. Collect $y'$: $y'(3y^2-6x)=6y-3x^2$, so $y'=\\frac{2y-x^2}{y^2-2x}$. At $(3,3)$: $\\frac{6-9}{9-6}=-1$."),
      [ch(1, "The numerator is $2y-x^2=6-9=-3$, which is negative, so the slope is negative."),
       ch(w2, "This drops the term $6xy'$: the product rule on $6xy$ gives both $6y$ and $6xy'$."),
       ch(w3, "This forgets that $\\frac{d}{dx}y^3=3y^2y'$. The chain rule factor $y'$ must stay on that term so that it can be collected.")],
      "Differentiate both sides with respect to $x$, using the product rule on $6xy$ and the chain rule on $y^3$. Collect the $y'$ terms and solve.")

# 12. product of two composite powers
f = (x**2 + 1) ** 3 * (2 * x - 1) ** 4
v = diff(f, x).subs(x, 1)
assert v == 88
e1 = (3 * (x**2 + 1) ** 2 * (2 * x - 1) ** 4 + (x**2 + 1) ** 3 * 4 * (2 * x - 1) ** 3).subs(x, 1)
e2 = (3 * (x**2 + 1) ** 2 * 2 * x * (2 * x - 1) ** 4 + (x**2 + 1) ** 3 * 4 * (2 * x - 1) ** 3).subs(x, 1)
e3 = (3 * (x**2 + 1) ** 2 * (2 * x - 1) ** 4 + (x**2 + 1) ** 3 * 4 * (2 * x - 1) ** 3 * 2).subs(x, 1)
B.mcq(T_CH, "If $y=(x^2+1)^3(2x-1)^4$, what is $\\dfrac{dy}{dx}$ at $x=1$?",
      ch(88, "Product rule with chain rule in each term: $y'=3(x^2+1)^2(2x)(2x-1)^4+(x^2+1)^3\\cdot4(2x-1)^3\\cdot2$. At $x=1$: $3\\cdot4\\cdot2\\cdot1+8\\cdot4\\cdot1\\cdot2=24+64=88$."),
      [ch(e1, "Both inner derivatives ($2x$ and $2$) are missing, so each chain-rule term is short by a factor."),
       ch(e2, "The inner derivative $2$ of $2x-1$ is missing from the second term, which would be $32\\cdot2=64$ at $x=1$."),
       ch(e3, "The inner derivative $2x$ of $x^2+1$ is missing from the first term, which would be $12\\cdot2=24$ at $x=1$.")],
      "Each of the two factors is a power of a function, so each differentiates with the chain rule. Then the product rule combines them.")

# 13. third derivative
f = x**4 - 3 * x**2 + sin(2 * x)
v = diff(f, x, 3).subs(x, 0)
assert v == -8
B.mcq(T_HO, "If $f(x)=x^4-3x^2+\\sin(2x)$, what is $f'''(0)$?",
      ch(-8, "Differentiate three times: $f'''(x)=24x-8\\cos(2x)$. At $x=0$ this is $0-8=-8$. Each differentiation of $\\sin(2x)$ brings out another factor of 2: $2$, $4$, $8$."),
      [ch(8, "The third derivative of $\\sin u$ is $-\\cos u$, so the sign is negative: $\\sin\\to\\cos\\to-\\sin\\to-\\cos$."),
       ch(-1, "This forgets the factor of 2 each time the chain rule is applied to $\\sin(2x)$. After three derivatives the factor is $2^3=8$."),
       ch(0, "The polynomial terms contribute 0 at $x=0$, but the sine term does not: $-8\\cos 0=-8$.")],
      "Take derivatives one at a time. The $x^4-3x^2$ part contributes $24x$, which is 0 at $x=0$; the $\\sin(2x)$ part supplies the value.")

# 14. triple composition from a table
tbl = (
    "| $x$ | 1 | 2 | 3 |\n|---|---|---|---|\n| $h(x)$ | 3 | 1 | 2 |\n| $h'(x)$ | 5 | 4 | $-1$ |\n"
    "| $g(x)$ | 3 | 2 | 1 |\n| $g'(x)$ | $-2$ | 6 | 0 |\n| $f'(x)$ | 7 | $-3$ | 5 |"
)
B.mcq(T_CH, "The table gives values of the differentiable functions $f$, $g$ and $h$ and their derivatives.\n\n" + tbl + "\n\nIf $P(x)=f(g(h(x)))$, what is $P'(2)$?",
      ch(-40, "$P'(2)=f'(g(h(2)))\\cdot g'(h(2))\\cdot h'(2)$. $h(2)=1$, then $g(1)=3$. So $P'(2)=f'(3)\\cdot g'(1)\\cdot h'(2)=5\\cdot(-2)\\cdot4=-40$."),
      [ch(-72, "This reads every derivative at $x=2$: $f'(2)g'(2)h'(2)$. Each outer derivative must be evaluated at the value of the layers inside it."),
       ch(-10, "This leaves out the innermost derivative factor $h'(2)=4$."),
       ch(120, "Here $g'$ is read at 2 instead of at $h(2)=1$: $5\\cdot6\\cdot4$. The middle derivative must be evaluated at $h(2)=1$.")],
      "Work from the inside out for the inputs and from the outside in for the derivatives: $h(2)=1$, $g(1)=3$, so the factors are $h'(2)$, $g'(1)$ and $f'(3)$.")

# 15. tangent line x-intercept of a composite power
f = (x**2 + 3) ** Rational(3, 2)
assert f.subs(x, 1) == 8 and diff(f, x).subs(x, 1) == 6
B.mcq(T_CH, "The line tangent to the graph of $g(x)=(x^2+3)^{3/2}$ at $x=1$ crosses the $x$-axis at $x=$",
      ch(Rational(-1, 3), "$g(1)=4^{3/2}=8$. $g'(x)=\\frac32(x^2+3)^{1/2}\\cdot2x=3x\\sqrt{x^2+3}$, so $g'(1)=6$. The tangent line is $y-8=6(x-1)$. At $y=0$: $x=1-\\frac86=-\\frac13$."),
      [ch(Rational(-5, 3), "This uses slope 3, from $\\frac32\\sqrt{4}$, which omits the chain-rule factor $2x=2$."),
       ch(Rational(1, 3), "This has the wrong sign: $x=1-\\frac{8}{6}$, since the line must go down from $(1,8)$ to reach the axis on the left."),
       ch(Rational(7, 3), "The axis crossing is to the left of $x=1$ because the slope is positive and the point is above the axis; it is $1-\\frac{8}{6}$, not $1+\\frac{8}{6}$.")],
      "Find $g(1)$ and $g'(1)$ (chain rule on the power), write the tangent line, and solve for $x$ when $y=0$.")

# ------------------------------------------------------------------ FRQs
F = x**2 * y + y**3 - 10
assert F.subs({x: 1, y: 2}) == 0
d1 = idiff(F, y, x)
slope = d1.subs({x: 1, y: 2})
assert slope == Rational(-4, 13)
d2v = simplify(idiff(F, y, x, 2).subs({x: 1, y: 2}))
cp = solve([F, x], [x, y])
assert (0, cbrt(10)) in [(a_, b_) for a_, b_ in cp]
B.frq(T_IM,
      "Consider the curve $C$ given by $x^2y+y^3=10$. The point $(1,2)$ lies on $C$.\n\n**(a)** Show that $\\dfrac{dy}{dx}=-\\dfrac{2xy}{x^2+3y^2}$.\n\n**(b)** Find an equation of the line tangent to $C$ at $(1,2)$.\n\n**(c)** Find all points on $C$ at which the tangent line is horizontal. Show that $C$ has no point with a vertical tangent.\n\n**(d)** Find $\\dfrac{d^2y}{dx^2}$ at $(1,2)$. Is $y$, as a function of $x$, concave up or concave down at that point? Justify your answer.",
      [(2, "(a) Differentiates implicitly with product rule on $x^2y$ and chain rule on $y^3$, and solves for $\\frac{dy}{dx}$"),
       (1, "(b) Finds slope $-\\frac{4}{13}$ and the tangent line $y-2=-\\frac4{13}(x-1)$"),
       (1, "(c) Sets the numerator $2xy=0$; rules out $y=0$ (not on $C$) and finds $x=0$, $y=\\sqrt[3]{10}$"),
       (1, "(c) Shows the denominator $x^2+3y^2$ is never 0 on $C$ (it would require $(0,0)$, which is not on $C$)"),
       (1, "(d) Differentiates $\\frac{dy}{dx}$ again, substituting $\\frac{dy}{dx}=-\\frac4{13}$, to find $-\\frac{660}{2197}$"),
       (1, "(d) Concludes concave down because the second derivative is negative")],
      "(a) $2xy+x^2y'+3y^2y'=0$, so $y'(x^2+3y^2)=-2xy$ and $y'=-\\frac{2xy}{x^2+3y^2}$.\n(b) At $(1,2)$: $y'=-\\frac{4}{1+12}=-\\frac4{13}$. Tangent: $y-2=-\\frac4{13}(x-1)$.\n(c) $y'=0$ requires $2xy=0$. If $y=0$ the curve equation gives $0=10$, impossible. If $x=0$, $y^3=10$, so the point is $\\left(0,\\sqrt[3]{10}\\right)$. A vertical tangent would need $x^2+3y^2=0$, which forces $x=y=0$, but $(0,0)$ is not on $C$.\n(d) With $N=-2xy$ and $D=x^2+3y^2$: $y''=\\frac{N'D-ND'}{D^2}$ with $N'=-2y-2xy'$ and $D'=2x+6yy'$. At $(1,2)$, $y'=-\\frac4{13}$: $N=-4$, $N'=-\\frac{44}{13}$, $D=13$, $D'=-\\frac{22}{13}$. So $y''=\\frac{-44-\\frac{88}{13}}{169}=-\\frac{660}{2197}$. Since $y''<0$, the curve is concave down at that point.")
assert d2v == Rational(-660, 2197), d2v

tbl2 = (
    "| $x$ | 1 | 2 | 3 |\n|---|---|---|---|\n| $f(x)$ | 3 | 5 | 8 |\n| $f'(x)$ | 2 | 4 | 7 |\n| $g(x)$ | 2 | 3 | 1 |\n| $g'(x)$ | $-1$ | 6 | 5 |"
)
B.frq(T_CH,
      "The differentiable functions $f$ and $g$ have the values shown in the table. Assume $f'(x)>0$ for all $x$.\n\n" + tbl2 + "\n\n**(a)** Let $h(x)=f(g(x))$. Find $h'(1)$ and $h'(2)$.\n\n**(b)** Let $k(x)=\\left[f(x)\\right]^2g(x)$. Find $k'(2)$.\n\n**(c)** Let $m$ be the inverse function of $f$. Find $m'(5)$, and explain why $f$ has an inverse.\n\n**(d)** Find an equation of the line tangent to the graph of $y=h(x)$ at $x=1$.",
      [(1, "(a) Applies the chain rule: $h'(1)=f'(g(1))g'(1)=f'(2)(-1)=-4$"),
       (1, "(a) $h'(2)=f'(g(2))g'(2)=f'(3)\\cdot6=42$"),
       (1, "(b) Uses the product rule with the chain rule: $k'(x)=2f(x)f'(x)g(x)+[f(x)]^2g'(x)$"),
       (1, "(b) Evaluates $k'(2)=2(5)(4)(3)+25(6)=270$"),
       (1, "(c) Finds $m'(5)=\\frac{1}{f'(2)}=\\frac14$ (since $f(2)=5$)"),
       (1, "(c) Explains $f'>0$ means $f$ is increasing, so it is one-to-one"),
       (1, "(d) Finds $h(1)=f(2)=5$ and the line $y-5=-4(x-1)$")],
      "(a) $h'(1)=f'(g(1))\\,g'(1)=f'(2)(-1)=-4$. $h'(2)=f'(g(2))\\,g'(2)=f'(3)(6)=42$.\n(b) $k'(x)=2f(x)f'(x)g(x)+[f(x)]^2g'(x)$, so $k'(2)=2(5)(4)(3)+(25)(6)=120+150=270$.\n(c) Since $f(2)=5$, $m(5)=2$, and $m'(5)=\\frac{1}{f'(m(5))}=\\frac1{f'(2)}=\\frac14$. $f$ has an inverse because $f'(x)>0$ means $f$ is strictly increasing, hence one-to-one.\n(d) $h(1)=f(g(1))=f(2)=5$ and $h'(1)=-4$. Tangent line: $y-5=-4(x-1)$.")

B.save()
B.show()
