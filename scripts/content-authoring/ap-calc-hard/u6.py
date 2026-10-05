from lib import *

B = Bank(6, "unit-6-integration-and-accumulation-of-change")
T_RS, T_FTC, T_ANT, T_US = (
    "riemann-sums-and-definite-integrals",
    "fundamental-theorem-of-calculus",
    "antiderivatives-and-indefinite-integrals",
    "u-substitution",
)

# 1. trapezoid sum with unequal subintervals
ts = [0, 2, 5, 9, 10]
Rv = [4, 7, 6, 3, 2]
trap = sum(Rational(ts[i + 1] - ts[i]) * (Rv[i] + Rv[i + 1]) / 2 for i in range(4))
left = sum((ts[i + 1] - ts[i]) * Rv[i] for i in range(4))
right = sum((ts[i + 1] - ts[i]) * Rv[i + 1] for i in range(4))
assert (trap, left, right) == (51, 56, 46)
tbl = "| $t$ | 0 | 2 | 5 | 9 | 10 |\n|---|---|---|---|---|---|\n| $R(t)$ | 4 | 7 | 6 | 3 | 2 |"
B.mcq(T_RS, "Values of a rate function $R(t)$, in gallons per minute, are given in the table. A trapezoidal sum with the four subintervals shown is used to approximate $\\displaystyle\\int_0^{10}R(t)\\,dt$.\n\n" + tbl + "\n\nWhat is the value of the approximation?",
      ch(51, "The subintervals have widths 2, 3, 4 and 1. Trapezoids: $2\\cdot\\frac{4+7}{2}+3\\cdot\\frac{7+6}{2}+4\\cdot\\frac{6+3}{2}+1\\cdot\\frac{3+2}{2}=11+19.5+18+2.5=51$."),
      [ch(56, "This is the left Riemann sum $2(4)+3(7)+4(6)+1(3)$, which uses the left endpoint's value on each subinterval instead of averaging the two ends."),
       ch(46, "This is the right Riemann sum $2(7)+3(6)+4(3)+1(2)$."),
       ch(22, "This adds the five table values without weighting by the widths of the subintervals. An integral approximation multiplies each value by a width.")],
      "Each trapezoid has area (width) $\\times$ (average of the two end values). The widths come from the differences between consecutive $t$ values.")

# 2. right, left, midpoint
Fx = x**2 - 1
rsum = sum(Fx.subs(x, q_) for q_ in (2, 3, 4, 5))
lsum = sum(Fx.subs(x, q_) for q_ in (1, 2, 3, 4))
msum = sum(Fx.subs(x, q_) for q_ in (Rational(3, 2), Rational(5, 2), Rational(7, 2), Rational(9, 2)))
exact = integrate(Fx, (x, 1, 5))
assert (rsum, lsum, msum, exact) == (50, 26, 37, Rational(112, 3))
B.mcq(T_RS, "A right Riemann sum with 4 subintervals of equal width is used to approximate $\\displaystyle\\int_1^5(x^2-1)\\,dx$. What is the value of the sum?",
      ch(50, "$\\Delta x=1$ and the right endpoints are 2, 3, 4, 5. The sum is $f(2)+f(3)+f(4)+f(5)=3+8+15+24=50$."),
      [ch(26, "This is the left sum, using the endpoints 1, 2, 3, 4: $0+3+8+15$."),
       ch(37, "This is the midpoint sum, using 1.5, 2.5, 3.5, 4.5."),
       ch(Rational(112, 3), "This is the exact value of the integral, not a Riemann sum.")],
      "Find $\\Delta x=\\frac{5-1}{4}=1$, list the right endpoints, evaluate $f$ at each, and add (times $\\Delta x$).")

# 3. FTC with two variable limits
G = Integral(sqrt(1 + t**3), (t, x, x**2))
Gp = sqrt(1 + x**6) * 2 * x - sqrt(1 + x**3)
val = Gp.subs(x, 1)
assert simplify(val - sqrt(2)) == 0
B.mcq(T_FTC, "Let $G(x)=\\displaystyle\\int_x^{x^2}\\sqrt{1+t^3}\\,dt$. What is $G'(1)$?",
      ch(sqrt(2), "$G'(x)=\\sqrt{1+(x^2)^3}\\cdot2x-\\sqrt{1+x^3}$. At $x=1$: $\\sqrt2\\cdot2-\\sqrt2=\\sqrt2$."),
      [ch(2 * sqrt(2), "This keeps only the upper-limit term. The variable lower limit contributes $-\\sqrt{1+x^3}$."),
       ch(0, "Both limits equal 1 at $x=1$, so $G(1)=0$, but $G'(1)$ is the rate of change of $G$, not its value."),
       ch(3 * sqrt(2), "The lower limit's term is subtracted, not added: $\\int_x^{x^2}=F(x^2)-F(x)$.")],
      "Write $G(x)=F(x^2)-F(x)$ for an antiderivative $F$ of the integrand, then differentiate with the chain rule: $G'(x)=f(x^2)\\cdot2x-f(x)$.")

# 4. accumulation function from a graph (diagram)
d4 = graph("x", "f(x)", 0, 6, -4, 5,
           [{"points": [{"x": 0, "y": 0}, {"x": 2, "y": 4}, {"x": 4, "y": 0}, {"x": 6, "y": -3}], "color": "blue", "label": "f"}],
           "Graph of f made of line segments through (0,0), (2,4), (4,0) and (6,-3).")
B.mcq(T_FTC, "The graph of $f$ is shown for $0\\le x\\le6$. It consists of line segments. Let $g(x)=\\displaystyle\\int_0^xf(t)\\,dt$. What is the maximum value of $g$ on the interval $[0,6]$?",
      ch(8, "$g'(x)=f(x)$ is positive on $(0,4)$ and negative on $(4,6)$, so $g$ increases until $x=4$ and then decreases: the maximum is $g(4)$. The area under $f$ from 0 to 4 is the triangle $\\frac12(4)(4)=8$."),
      [ch(5, "$g(6)=8-3=5$ is the value at the right endpoint. Since $f<0$ on $(4,6)$, $g$ is decreasing there, so $g(4)=8$ is larger."),
       ch(4, "4 is the area from $x=0$ to $x=2$ only. The function is still positive from 2 to 4, so $g$ keeps increasing."),
       ch(11, "This adds the area of the triangle below the axis instead of subtracting it ($8+3$). That area counts negatively in $\\int f$, and $g$ does not reach its maximum at $x=6$.")],
      "$g'=f$, so $g$ changes from increasing to decreasing where $f$ changes from positive to negative. Then compute the signed area up to that point.", diagram=d4)

# 5. combining integral properties
ans = 2 * 5 - 3 * (-2) + 2
assert ans == 18
B.mcq(T_RS, "Suppose $\\displaystyle\\int_1^5f(x)\\,dx=8$, $\\displaystyle\\int_3^5f(x)\\,dx=3$ and $\\displaystyle\\int_1^3g(x)\\,dx=-2$. What is $\\displaystyle\\int_1^3\\big(2f(x)-3g(x)+1\\big)\\,dx$?",
      ch(18, "$\\int_1^3f=\\int_1^5f-\\int_3^5f=8-3=5$. Then $2(5)-3(-2)+\\int_1^31\\,dx=10+6+2=18$."),
      [ch(16, "The constant 1 integrates to $1\\cdot(3-1)=2$, not 0."),
       ch(6, "The term $-3g$ gives $-3(-2)=+6$. Subtracting it as $-6$ drops the sign of $\\int g$."),
       ch(24, "This uses $\\int_1^5f=8$ in place of $\\int_1^3f=5$. The interval of integration must match.")],
      "Split $\\int_1^5f$ at $x=3$ to get $\\int_1^3f$. Then use linearity of the integral, including the constant term.")

# 6. u-substitution with definite limits
e = Integral(log(x) ** 2 / x, (x, 1, E)).doit()
assert simplify(e - Rational(1, 3)) == 0
B.mcq(T_US, "What is the value of $\\displaystyle\\int_1^e\\frac{(\\ln x)^2}{x}\\,dx$?",
      ch(Rational(1, 3), "Let $u=\\ln x$, $du=\\frac{dx}x$. The limits become $u=0$ and $u=1$: $\\int_0^1u^2\\,du=\\frac13$."),
      [ch("$\\dfrac{e^3-1}{3}$", "This keeps the old limits $x=1$ and $x=e$ after substituting $u$. The limits must be converted to $u=\\ln1=0$ and $u=\\ln e=1$ (or the antiderivative converted back to $x$)."),
       ch(1, "The antiderivative of $u^2$ is $\\frac{u^3}{3}$. Dropping the $\\frac13$ gives 1."),
       ch(Rational(2, 3), "This doubles the result, as if the antiderivative of $u^2$ were $\\frac{2u^3}{3}$. It is $\\frac{u^3}{3}$, which is $\\frac13$ at $u=1$.")],
      "Substitute $u=\\ln x$, change the limits of integration to match, and integrate $u^2$.")

# 7. antiderivatives with two initial conditions
fpp = 12 * x - 6
f1 = integrate(fpp, x)
C1 = solve(Eq((f1 + k).subs(x, 1), 0), k)[0]
fprime = f1 + C1
f0 = integrate(fprime, x)
D0 = solve(Eq((f0 + k).subs(x, 1), 2), k)[0]
ff = f0 + D0
assert ff.subs(x, 0) == 3 and expand(ff - (2 * x**3 - 3 * x**2 + 3)) == 0
B.mcq(T_ANT, "The function $f$ satisfies $f''(x)=12x-6$, $f'(1)=0$ and $f(1)=2$. What is $f(0)$?",
      ch(3, "$f'(x)=6x^2-6x+C$ and $f'(1)=0$ give $C=0$. $f(x)=2x^3-3x^2+D$ and $f(1)=-1+D=2$ give $D=3$. So $f(0)=3$."),
      [ch(2, "$f(1)=2$ is a given value. The condition at $x=1$ gives the constant $D$; the question asks for $f(0)$, which equals $D=3$."),
       ch(-1, "$-1$ is $f(1)$ before adding the constant $D$: $2(1)-3(1)=-1$. The constant is $D=3$."),
       ch(5, "This has $D=5$, from adding $f(1)=2$ and 3 instead of solving $-1+D=2$. The condition $f(1)=2$ gives $D=3$.")],
      "Integrate twice, using each initial condition right after the integration it belongs to.")

# 8. accumulation with a maximum
A0 = 200
rate = 30 - 4 * t
tmax = solve(rate, t)[0]
Amax = A0 + integrate(rate, (t, 0, tmax))
assert tmax == Rational(15, 2) and Amax == Rational(625, 2)
B.mcq(T_FTC, "Water flows into a tank at a rate $R(t)=30-4t$ gallons per minute for $0\\le t\\le15$, where $t$ is in minutes. The tank holds 200 gallons at $t=0$. What is the greatest amount of water in the tank during this time?",
      ch("312.5 gallons", "The amount is $A(t)=200+\\int_0^tR(s)\\,ds$, which increases while $R>0$ and decreases after. $R=0$ at $t=7.5$. $A(7.5)=200+\\left[30t-2t^2\\right]_0^{7.5}=200+225-112.5=312.5$."),
      [ch("200 gallons", "200 gallons is the starting amount. The amount rises above that while $R(t)>0$."),
       ch("112.5 gallons", "This is the net change in the amount from $t=0$ to $t=7.5$; the question asks for the amount in the tank, which includes the initial 200."),
       ch("537.5 gallons", "The $-2t^2$ term is subtracted: $\\int_0^{7.5}(30-4t)\\,dt=225-112.5$, not $225+112.5$.")],
      "The amount is largest where the rate changes from positive to negative. Use the initial amount plus the net change up to that time.")

# 9. integral of an absolute value
e = Integral(Abs(x**2 - x - 2), (x, -1, 3)).doit()
assert e == Rational(19, 3), e
sgn = integrate(x**2 - x - 2, (x, -1, 3))
assert sgn == Rational(-8, 3)
B.mcq(T_RS, "What is the value of $\\displaystyle\\int_{-1}^{3}\\left|x^2-x-2\\right|\\,dx$?",
      ch(Rational(19, 3), "$x^2-x-2=(x-2)(x+1)$ is negative on $(-1,2)$ and positive on $(2,3)$. So the integral is $-\\int_{-1}^2(x^2-x-2)dx+\\int_2^3(x^2-x-2)dx=\\frac92+\\frac{11}6=\\frac{19}3$."),
      [ch(Rational(-8, 3), "This integrates $x^2-x-2$ without the absolute value. The area below the axis counts negatively. An integral of an absolute value cannot be negative."),
       ch(Rational(8, 3), "This takes the absolute value of the signed integral, $\\left|\\int(x^2-x-2)\\,dx\\right|$. That is not the same as $\\int|x^2-x-2|\\,dx$, because the positive and negative parts partly cancel inside."),
       ch(Rational(9, 2), "$\\frac92$ is only the area on $(-1,2)$, where the function is negative. The region from 2 to 3 also contributes.")],
      "Find the sign changes of $x^2-x-2$ in the interval, then integrate each piece with the sign that makes the integrand non-negative.")

# 10. recognize a Riemann sum
B.mcq(T_RS, "What is the value of $\\displaystyle\\lim_{n\\to\\infty}\\sum_{k=1}^{n}\\frac2n\\left(1+\\frac{2k}{n}\\right)^3$?",
      ch(20, "With $\\Delta x=\\frac2n$ and $x_k=1+\\frac{2k}n$, this is a right Riemann sum for $\\int_1^3x^3\\,dx=\\frac{3^4-1^4}{4}=20$."),
      [ch(4, "This treats the sum as $\\int_0^2x^3\\,dx=4$. The sample points are $1+\\frac{2k}n$, which run from 1 to 3, not from 0 to 2."),
       ch(40, "The factor $\\frac2n$ is the $\\Delta x$ already; doubling the integral $\\int_1^3x^3dx$ counts it twice."),
       ch(Rational(15, 4), "This is $\\int_1^2x^3\\,dx$. The interval length is $n\\cdot\\frac2n=2$, so it runs from 1 to 3.")],
      "Identify $\\Delta x$ and $x_k$, so the sum becomes $\\sum f(x_k)\\Delta x$ with $f(x)=x^3$ on $[1,3]$.")

# 11. extreme point of an accumulation function
B.mcq(T_FTC, "Let $F(x)=\\displaystyle\\int_0^x(t^2-4t+3)\\,dt$. At what value of $x$ does $F$ have a local minimum?",
      ch(3, "$F'(x)=x^2-4x+3=(x-1)(x-3)$. $F'$ changes from negative to positive at $x=3$, so $F$ has a local minimum there. (At $x=1$, $F'$ changes from positive to negative: a local maximum.)"),
      [ch(1, "At $x=1$, $F'$ changes from positive to negative, which is a local maximum of $F$."),
       ch(2, "$x=2$ is where $F''(x)=2x-4=0$, an inflection point of $F$, not an extremum."),
       ch(0, "$F'(0)=0^2-0+3=3\\neq0$, so $x=0$ is not a critical point of $F$. $F$ is increasing through $x=0$.")],
      "By the Fundamental Theorem, $F'(x)=x^2-4x+3$. Use the First Derivative Test on $F'$.")

# 12. u-substitution with an exponential
e = Integral(exp(x) / (1 + exp(x)), (x, 0, log(3))).doit()
assert simplify(e - log(2)) == 0
B.mcq(T_US, "What is the value of $\\displaystyle\\int_0^{\\ln3}\\frac{e^x}{1+e^x}\\,dx$?",
      ch("$\\ln2$", "Let $u=1+e^x$, $du=e^x\\,dx$. The limits become $u=2$ and $u=4$: $\\int_2^4\\frac{du}{u}=\\ln4-\\ln2=\\ln2$."),
      [ch("$\\ln4$", "This leaves out the lower limit: $\\ln4-\\ln2=\\ln2$, not $\\ln4$."),
       ch("$\\ln3$", "This replaces $e^x$ by its upper-limit value 3 only. The antiderivative is $\\ln(1+e^x)$ and is evaluated at both limits."),
       ch("$\\dfrac{\\ln2}{2}$", "The substitution $u=1+e^x$ has $du=e^x\\,dx$ exactly; no factor of $\\frac12$ appears.")],
      "The numerator is the derivative of the denominator, so the antiderivative is $\\ln(1+e^x)$.")

# 13. ordering of approximations
B.mcq(T_RS, "The function $f$ is continuous, increasing and concave up on $[0,4]$. Let $L$, $R$, $M$ and $T$ be the left, right, midpoint and trapezoidal approximations of $I=\\int_0^4f(x)\\,dx$ using 4 subintervals of equal width. Which ordering must be true?",
      ch("$L<M<I<T<R$", "Increasing: $L<I<R$ and $L<M$, $T<R$. Concave up: the midpoint sum underestimates and the trapezoidal sum overestimates, so $M<I<T$. Combined: $L<M<I<T<R$."),
      [ch("$L<T<I<M<R$", "For a concave-up function the trapezoids lie above the graph (overestimate) and the midpoint rectangles underestimate: $M<I<T$, the other way around."),
       ch("$L<I<M<T<R$", "The midpoint sum is an underestimate for concave-up functions, so $M<I$."),
       ch("$M<L<I<R<T$", "For an increasing function the left sum is below the midpoint sum ($L<M$), and the trapezoidal sum is the average of $L$ and $R$, so $T<R$.")],
      "Increasing gives $L<I<R$; concave up gives $M<I<T$. For an increasing function, $L<M$ and $T<R$.")

# 14. symmetry
e = Integral(x**3 * cos(x) + 3 * x**2 + 5, (x, -2, 2)).doit()
assert simplify(e - 36) == 0
B.mcq(T_ANT, "What is the value of $\\displaystyle\\int_{-2}^{2}\\left(x^3\\cos x+3x^2+5\\right)dx$?",
      ch(36, "$x^3\\cos x$ is an odd function, so its integral over $[-2,2]$ is 0. The rest gives $\\int_{-2}^23x^2\\,dx+\\int_{-2}^25\\,dx=16+20=36$."),
      [ch(16, "This leaves out the constant term: $\\int_{-2}^25\\,dx=20$."),
       ch(20, "This leaves out the $3x^2$ term: $\\int_{-2}^23x^2\\,dx=\\left[x^3\\right]_{-2}^{2}=16$."),
       ch(0, "Only the odd part, $x^3\\cos x$, integrates to 0. The terms $3x^2$ and 5 are even and add to the integral.")],
      "Split the integrand into odd and even parts. The odd part integrates to 0 over a symmetric interval.")

# 15. trig u-substitution
e = Integral(sin(x) / cos(x) ** 2, (x, 0, pi / 3)).doit()
assert simplify(e - 1) == 0
B.mcq(T_US, "What is the value of $\\displaystyle\\int_0^{\\pi/3}\\frac{\\sin x}{\\cos^2x}\\,dx$?",
      ch(1, "Let $u=\\cos x$, $du=-\\sin x\\,dx$. Then $\\int\\frac{\\sin x}{\\cos^2x}dx=-\\int u^{-2}du=\\frac1u=\\sec x$. So the value is $\\sec\\frac\\pi3-\\sec0=2-1=1$."),
      [ch(2, "$\\sec\\frac\\pi3=2$ is only the upper-limit value. Subtract $\\sec0=1$."),
       ch(-1, "The sign is wrong: $-\\int u^{-2}du=+u^{-1}$, so the antiderivative is $+\\sec x$."),
       ch(Rational(1, 2), "$\\frac12$ is $\\cos\\frac\\pi3$, the value of $u$ at the upper limit. The antiderivative is $\\frac1u=\\sec x$, so the values to compare are $\\sec\\frac\\pi3=2$ and $\\sec0=1$.")],
      "Substitute $u=\\cos x$ (so $du=-\\sin x\\,dx$) and integrate $-u^{-2}$.")

# ------------------------------------------------------------------ FRQs
ts = [0, 3, 6, 9, 12]
Rv = [8, 12, 10, 6, 4]
trap = sum(Rational(ts[i + 1] - ts[i]) * (Rv[i] + Rv[i + 1]) / 2 for i in range(4))
assert trap == 102 and 40 + trap == 142 and Rational(trap, 12) == Rational(17, 2)
tbl = "| $t$ (minutes) | 0 | 3 | 6 | 9 | 12 |\n|---|---|---|---|---|---|\n| $R(t)$ (gal/min) | 8 | 12 | 10 | 6 | 4 |"
B.frq(T_RS,
      "Water flows into a tank at a rate $R(t)$ gallons per minute, where $R$ is a differentiable function of $t$. Selected values are in the table. At time $t=0$ the tank holds 40 gallons.\n\n" + tbl + "\n\n**(a)** Use a trapezoidal sum with the four subintervals in the table to approximate $\\int_0^{12}R(t)\\,dt$. Show the computations.\n\n**(b)** Using your answer to (a), approximate the amount of water in the tank at $t=12$. Include units.\n\n**(c)** Explain the meaning of $\\frac1{12}\\int_0^{12}R(t)\\,dt$ in the context of the problem, and use your answer to (a) to approximate its value.\n\n**(d)** Is there a time $t$ with $0<t<3$ at which $R(t)=9$? Is there a time $t$ with $3<t<9$ at which $R'(t)=-1$? Justify each answer using a named theorem.",
      [(1, "(a) Sets up the trapezoids with widths 3: $3\\cdot\\frac{8+12}2+3\\cdot\\frac{12+10}2+3\\cdot\\frac{10+6}2+3\\cdot\\frac{6+4}2$"),
       (1, "(a) Evaluates to 102"),
       (1, "(b) Adds the initial 40 gallons: about 142 gallons"),
       (1, "(c) Interprets it as the average rate at which water flows in over the 12 minutes, in gallons per minute"),
       (1, "(c) Approximates it as $\\frac{102}{12}=8.5$ gallons per minute"),
       (1, "(d) For $R(t)=9$: states $R$ is continuous with $R(0)=8<9<12=R(3)$ and applies the Intermediate Value Theorem"),
       (1, "(d) For $R'(t)=-1$: states $R$ is differentiable, computes $\\frac{R(9)-R(3)}{9-3}=\\frac{6-12}{6}=-1$, and applies the Mean Value Theorem")],
      "(a) $\\int_0^{12}R(t)\\,dt\\approx3\\cdot\\frac{8+12}{2}+3\\cdot\\frac{12+10}{2}+3\\cdot\\frac{10+6}{2}+3\\cdot\\frac{6+4}{2}=30+33+24+15=102$.\n(b) Amount at $t=12$ is the initial amount plus the net change: $40+102=142$ gallons.\n(c) $\\frac1{12}\\int_0^{12}R(t)\\,dt$ is the average value of $R$ on $[0,12]$: the average rate, in gallons per minute, at which water flows into the tank during the 12 minutes. It is approximately $\\frac{102}{12}=8.5$ gallons per minute.\n(d) $R$ is differentiable, so it is continuous. $R(0)=8<9<12=R(3)$, so by the Intermediate Value Theorem there is a $t$ in $(0,3)$ with $R(t)=9$. On $[3,9]$ $R$ is continuous and differentiable, with $\\frac{R(9)-R(3)}{9-3}=\\frac{6-12}{6}=-1$, so by the Mean Value Theorem there is a $t$ in $(3,9)$ with $R'(t)=-1$.")

f_ = integrate(3 * x**2 - 2 * x, x)
Cc = solve(Eq(f_.subs(x, 1) + k, 4), k)[0]
ff = f_ + Cc
assert ff.subs(x, 2) == 8 and expand(ff - (x**3 - x**2 + 4)) == 0
iv = integrate(x * exp(x**2), (x, 0, 2))
assert simplify(iv - (exp(4) - 1) / 2) == 0
Gp = diff(integrate(t**2 - t, (t, 1, x**2)), x)
assert expand(Gp - (2 * x**5 - 2 * x**3)) == 0
B.frq(T_FTC,
      "**(a)** The function $f$ satisfies $f'(x)=3x^2-2x$ and $f(1)=4$. Find $f(x)$, and find $f(2)$.\n\n**(b)** Use the substitution $u=x^2$ to evaluate $\\displaystyle\\int_0^2xe^{x^2}\\,dx$. Show how the limits of integration change.\n\n**(c)** Let $G(x)=\\displaystyle\\int_1^{x^2}\\left(t^2-t\\right)dt$. Find $G'(x)$.\n\n**(d)** Find the $x$-coordinate of each local extremum of $G$, and classify each as a local maximum or a local minimum. Justify your answer.",
      [(1, "(a) Antidifferentiates to $f(x)=x^3-x^2+C$"),
       (1, "(a) Uses $f(1)=4$ to find $C=4$ and computes $f(2)=8$"),
       (1, "(b) Substitutes $u=x^2$, $du=2x\\,dx$ and changes the limits to $u=0$ and $u=4$"),
       (1, "(b) Evaluates $\\frac12\\int_0^4e^u\\,du=\\frac{e^4-1}2$"),
       (1, "(c) Applies the Fundamental Theorem with the chain rule: $G'(x)=\\left((x^2)^2-x^2\\right)\\cdot2x=2x^5-2x^3$"),
       (1, "(d) Solves $G'(x)=2x^3(x^2-1)=0$ for $x=-1,0,1$"),
       (1, "(d) Uses the sign of $G'$ to classify: local minimum at $x=-1$ and $x=1$, local maximum at $x=0$")],
      "(a) $f(x)=x^3-x^2+C$. $f(1)=0+C=4$, so $C=4$ and $f(x)=x^3-x^2+4$. Then $f(2)=8-4+4=8$.\n(b) With $u=x^2$, $du=2x\\,dx$, so $x\\,dx=\\frac12du$. When $x=0$, $u=0$; when $x=2$, $u=4$. $\\int_0^2xe^{x^2}dx=\\frac12\\int_0^4e^u\\,du=\\frac12(e^4-1)$.\n(c) $G'(x)=\\left((x^2)^2-x^2\\right)\\cdot2x=2x^5-2x^3$.\n(d) $G'(x)=2x^3(x^2-1)=0$ at $x=-1,0,1$. For $x<-1$, $G'<0$; on $(-1,0)$, $G'>0$; on $(0,1)$, $G'<0$; for $x>1$, $G'>0$. $G'$ changes from negative to positive at $x=-1$ and $x=1$ (local minima) and from positive to negative at $x=0$ (local maximum).")

B.save()
B.show()
