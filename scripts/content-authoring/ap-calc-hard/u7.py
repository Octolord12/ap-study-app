from lib import *

B = Bank(7, "unit-7-differential-equations")
T_MOD, T_SF, T_SEP, T_EXP = (
    "modeling-with-differential-equations",
    "slope-fields",
    "separation-of-variables",
    "exponential-growth-and-decay",
)

# 1. separable, sign of the constant
ysol = -2 / (x**2 + 2)
assert simplify(diff(ysol, x) - x * ysol**2) == 0 and ysol.subs(x, 0) == -1
assert ysol.subs(x, 2) == Rational(-1, 3)
B.mcq(T_SEP, "The function $y=f(x)$ is the solution of $\\dfrac{dy}{dx}=xy^2$ with $f(0)=-1$. What is $f(2)$?",
      ch(Rational(-1, 3), "Separate: $\\frac{dy}{y^2}=x\\,dx$, so $-\\frac1y=\\frac{x^2}{2}+C$. With $y(0)=-1$: $1=C$. Then $y=-\\frac{1}{x^2/2+1}=-\\frac{2}{x^2+2}$, and $f(2)=-\\frac26=-\\frac13$."),
      [ch(Rational(1, 3), "The sign is lost: $\\int y^{-2}dy=-y^{-1}$, so the solution is negative here (it also starts at $-1$ and cannot change sign)."),
       ch(1, "This writes $\\frac1y=\\frac{x^2}2+C$, dropping the negative sign from $\\int y^{-2}dy=-\\frac1y$. That gives $y(0)=-1\\Rightarrow C=-1$ and $y(2)=1$."),
       ch(-1, "This uses $C=-1$ in $-\\frac1y=\\frac{x^2}2+C$. The initial condition gives $-\\frac1{-1}=1=C$.")],
      "Separate variables, integrate both sides (including the constant), and use the initial condition before solving for $y$.")

# 2. separable with a quadratic that factors
ysol = x + 1
assert simplify(diff(ysol, x) - (x + 1) / ysol) == 0 and ysol.subs(x, 1) == 2
B.mcq(T_SEP, "The function $y=f(x)$ satisfies $\\dfrac{dy}{dx}=\\dfrac{x+1}{y}$ with $f(1)=2$. What is $f(3)$?",
      ch(4, "$y\\,dy=(x+1)\\,dx$ gives $\\frac{y^2}{2}=\\frac{x^2}{2}+x+C$. At $(1,2)$: $2=\\frac12+1+C$, so $C=\\frac12$ and $y^2=x^2+2x+1=(x+1)^2$. Since $f(1)=2>0$, $y=x+1$, and $f(3)=4$."),
      [ch(-4, "$y^2=(x+1)^2$ has two roots, but the initial condition $f(1)=2>0$ selects the positive one, $y=x+1$."),
       ch(sqrt(15), "This drops the constant: $y^2=x^2+2x$ gives $y(3)=\\sqrt{15}$. But then $y(1)=\\sqrt3\\neq2$, so the initial condition has not been used."),
       ch(5, "This has $y=x+2$, which fails the initial condition: $f(1)=3\\neq2$.")],
      "After integrating, use the initial condition to find $C$, then take the square root with the sign the initial condition requires.")

# 3. identify the differential equation from a description
B.mcq(T_SF, "A slope field for a differential equation $\\dfrac{dy}{dx}=g(x,y)$ has horizontal segments at every point on the $y$-axis and at every point on the line $y=-2$. The segments have positive slope at every point with $x>0$ and $y>0$. Which differential equation could produce it?",
      ch("$\\dfrac{dy}{dx}=x(y+2)$", "The slope is 0 when $x=0$ (the $y$-axis) or $y=-2$. For $x>0$ and $y>0$, both factors are positive, so the slope is positive."),
      [ch("$\\dfrac{dy}{dx}=x(y-2)$", "The slope is 0 along $y=2$, not $y=-2$."),
       ch("$\\dfrac{dy}{dx}=y(x+2)$", "The slope is 0 along the $x$-axis ($y=0$) and the line $x=-2$, not along the $y$-axis and $y=-2$."),
       ch("$\\dfrac{dy}{dx}=(x+2)(y+2)$", "The slope is 0 along $x=-2$ and $y=-2$, but the $y$-axis ($x=0$) has slope $2(y+2)$, not 0.")],
      "Find where each candidate has slope 0, and check the sign in the first quadrant.")

# 4. tangent line approximation and concavity from the differential equation
y2 = 2**2 - 1
assert y2 == 3
ypp = 2 * 2 - 3
assert ypp == 1
B.mcq(T_SF, "The solution $y=f(x)$ of $\\dfrac{dy}{dx}=x^2-y$ passes through the point $(2,1)$. The line tangent to the graph of $f$ at $x=2$ is used to approximate $f(2.1)$. Which is the approximation, and is it an overestimate or an underestimate?",
      ch("1.3, an underestimate", "$f'(2)=2^2-1=3$, so $L(2.1)=1+3(0.1)=1.3$. Differentiating the equation: $y''=2x-y'$, so $f''(2)=4-3=1>0$. The graph is concave up and lies above its tangent line, so 1.3 is an underestimate."),
      [ch("1.3, an overestimate", "$f''(2)=2x-y'=4-3=1>0$ means concave up, so the graph lies above the tangent line. The estimate is too low."),
       ch("1.03, an underestimate", "This uses a slope of 0.3, as if $f'(2)=0.3$. The slope is $2^2-1=3$ and the step is $0.1$."),
       ch("4, an overestimate", "This adds the whole slope, $1+3=4$, instead of slope times step. The change in $y$ over a step of $0.1$ is $3\\cdot0.1=0.3$.")],
      "Compute the slope from the differential equation, build the tangent line, and find the concavity by differentiating the differential equation implicitly.")

# 5. exponential growth from two data points
P0, P2 = 400, 900
ratio = Rational(P2, P0)
P4 = P0 * ratio**2
assert P4 == 2025
B.mcq(T_EXP, "A population $P$ satisfies $\\dfrac{dP}{dt}=kP$. The population is 400 at $t=0$ and 900 at $t=2$ (in years). What is the population at $t=4$?",
      ch(2025, "$P(t)=400e^{kt}$ and $\\frac{900}{400}=e^{2k}=\\frac94$. At $t=4$, $e^{4k}=\\left(\\frac94\\right)^2$, so $P(4)=400\\cdot\\frac{81}{16}=2025$."),
      [ch(1400, "This is linear growth (adding 500 every two years). A population with $\\frac{dP}{dt}=kP$ grows by a constant factor each two years, not a constant amount."),
       ch(1350, "This multiplies 900 by 1.5. The factor over two years is $\\frac{900}{400}=2.25$, not 1.5."),
       ch(2700, "This multiplies 900 by 3. The factor per two years is 2.25, so $900\\times2.25=2025$.")],
      "Exponential growth multiplies by a constant factor in equal time intervals. The factor over the first 2 years is $\\frac{900}{400}$.")

# 6. half-life
B.mcq(T_EXP, "A radioactive substance has a half-life of 6 years. What fraction of an initial sample remains after 15 years?",
      ch("$\\dfrac{1}{4\\sqrt2}$", "The amount is $A_0\\left(\\frac12\\right)^{t/6}$. At $t=15$: $\\left(\\frac12\\right)^{5/2}=\\frac{1}{4\\sqrt2}\\approx0.177$."),
      [ch("$\\dfrac14$", "This is the fraction after 12 years (two half-lives). 15 years is $2.5$ half-lives."),
       ch("$\\dfrac18$", "This is the fraction after 18 years (three half-lives)."),
       ch("$e^{-5/2}$", "This replaces the base $\\frac12$ with $e$. The decay factor per half-life is $\\frac12$, so the amount is $\\left(\\frac12\\right)^{5/2}$.")],
      "Express the amount as $A_0\\left(\\tfrac12\\right)^{t/\\text{half-life}}$.")

# 7. Newton's law of cooling
Tt = 20 + 60 * Rational(1, 2) ** (t / 10)
assert Tt.subs(t, 0) == 80 and Tt.subs(t, 10) == 50 and Tt.subs(t, 30) == Rational(55, 2)
B.mcq(T_MOD, "A cup of tea cools in a room kept at 20°C according to $\\dfrac{dT}{dt}=-k(T-20)$ for a positive constant $k$. The tea is 80°C at $t=0$ and 50°C at $t=10$ minutes. What is its temperature at $t=30$ minutes?",
      ch("27.5°C", "$T-20=60e^{-kt}$. At $t=10$: $30=60e^{-10k}$, so $e^{-10k}=\\frac12$. At $t=30$: $T-20=60\\left(\\frac12\\right)^3=7.5$, so $T=27.5$."),
      [ch("35°C", "This is the temperature at $t=20$ ($20+60\\cdot\\frac14=35$). At $t=30$ there have been three halvings of the difference."),
       ch("20°C", "The tea approaches 20°C but never reaches it in finite time. The difference $T-20$ decays exponentially."),
       ch("23.75°C", "This is the temperature at $t=40$ ($20+60\\cdot\\frac1{16}$). At $t=30$ the difference has halved three times, not four.")],
      "The difference $T-20$ decays exponentially. It halved in the first 10 minutes, so it halves every 10 minutes.")

# 8. logistic maximum growth rate
P = symbols("P", positive=True)
rate = Rational(2, 100) * P * (1 - P / 500)
Pm = solve(diff(rate, P), P)[0]
assert Pm == 250 and rate.subs(P, 250) == Rational(5, 2)
B.mcq(T_MOD, "A population $P(t)$ satisfies the logistic differential equation $\\dfrac{dP}{dt}=0.02P\\left(1-\\dfrac{P}{500}\\right)$. What is the greatest possible value of $\\dfrac{dP}{dt}$?",
      ch(2.5, "$\\frac{dP}{dt}=0.02P-0.00004P^2$ is a downward parabola in $P$ with its vertex at $P=250$ (half the carrying capacity). There $\\frac{dP}{dt}=0.02(250)\\left(\\frac12\\right)=2.5$."),
      [ch(250, "250 is the population at which the growth rate is greatest, not the growth rate itself."),
       ch(10, "This is $0.02\\times500$. At $P=500$ the factor $(1-\\frac P{500})$ is 0 and the growth rate is 0."),
       ch(5, "This is $0.02\\cdot250$, the first factor alone. The second factor $1-\\frac{250}{500}=\\frac12$ halves it.")],
      "Treat $\\frac{dP}{dt}$ as a function of $P$ and maximize it, either with calculus or by recognizing the vertex of the parabola.")

# 9. verifying a solution of a second-order equation
sols = solve(k**2 - k - 6, k)
assert sorted(sols) == [-2, 3]
B.mcq(T_MOD, "For what positive value of $k$ does $y=e^{kx}$ satisfy $y''-y'-6y=0$?",
      ch(3, "$y'=ke^{kx}$ and $y''=k^2e^{kx}$. Substituting: $(k^2-k-6)e^{kx}=0$, so $(k-3)(k+2)=0$. The positive solution is $k=3$."),
      [ch(-2, "$k=-2$ also satisfies the equation, but the question asks for a positive value."),
       ch(2, "$2^2-2-6=-4\\neq0$. The factorization is $(k-3)(k+2)$."),
       ch(6, "$6^2-6-6=24\\neq0$. The constant term $-6$ is the product of the roots, not a root.")],
      "Substitute $y$, $y'$ and $y''$ into the differential equation and solve the resulting quadratic in $k$.")

# 10. domain of a solution
ysol = 2 / (1 - 2 * x)
assert simplify(diff(ysol, x) - ysol**2) == 0 and ysol.subs(x, 0) == 2
B.mcq(T_SEP, "The solution of $\\dfrac{dy}{dx}=y^2$ with $y(0)=2$ is defined on the largest interval containing $x=0$ on which the solution exists. What is that interval?",
      ch("$x<\\dfrac12$", "$\\frac{dy}{y^2}=dx$ gives $-\\frac1y=x+C$, and $y(0)=2$ gives $C=-\\frac12$. So $y=\\frac{1}{\\frac12-x}=\\frac{2}{1-2x}$, which blows up at $x=\\frac12$. The interval containing 0 is $x<\\frac12$."),
      [ch("$x>\\dfrac12$", "This interval does not contain $x=0$, where the initial condition is given."),
       ch("All real numbers", "The solution $y=\\frac{2}{1-2x}$ has a vertical asymptote at $x=\\frac12$, so it is not defined for all $x$."),
       ch("$-\\dfrac12<x<\\dfrac12$", "Nothing goes wrong at $x=-\\frac12$: the denominator is $1-2(-\\frac12)=2$. The solution exists for all $x<\\frac12$.")],
      "Solve the equation, then find where the solution is undefined and keep the interval that contains the initial point.")

# 11. separable with arctan
ysol = 2 * exp(atan(x))
assert simplify(diff(ysol, x) - ysol / (x**2 + 1)) == 0 and ysol.subs(x, 0) == 2
B.mcq(T_SEP, "The function $y=f(x)$ satisfies $\\dfrac{dy}{dx}=\\dfrac{y}{x^2+1}$ and $f(0)=2$. What is $f(1)$?",
      ch("$2e^{\\pi/4}$", "$\\frac{dy}{y}=\\frac{dx}{x^2+1}$ gives $\\ln|y|=\\arctan x+C$. $y(0)=2$ gives $C=\\ln2$, so $y=2e^{\\arctan x}$, and $f(1)=2e^{\\pi/4}$."),
      [ch("$4$", "This integrates $\\frac{1}{x^2+1}$ as $\\ln(x^2+1)$. The antiderivative of $\\frac{1}{x^2+1}$ is $\\arctan x$."),
       ch("$e^{\\pi/4}$", "This drops the factor 2 that comes from the initial condition. $e^C=2$."),
       ch("$2e^{\\pi/2}$", "$\\arctan1=\\frac\\pi4$, not $\\frac\\pi2$.")],
      "Separate, integrate using $\\int\\frac{dx}{x^2+1}=\\arctan x$, and apply the initial condition.")

# 12. exponential decay by percentage
frac = Rational(8, 10) ** 3
assert frac == Rational(64, 125)
B.mcq(T_EXP, "A substance decays at a rate proportional to the amount present. If 20% of it decays in the first 3 days, what fraction of the original amount remains after 9 days?",
      ch("0.512", "Each 3-day period multiplies the amount by 0.8. After 9 days (three periods): $0.8^3=0.512$."),
      [ch("0.4", "This subtracts 20% three times from the original amount. Decay by a fixed proportion compounds: each period applies to what remains."),
       ch("0.64", "This is $0.8^2$, the fraction after 6 days (two periods)."),
       ch("0.488", "This is $1-0.512$, the fraction that has decayed, not the fraction that remains.")],
      "A constant proportional decay multiplies the amount by a constant factor over equal time intervals.")

# 13. concavity from the differential equation
B.mcq(T_SF, "The solution curve of $\\dfrac{dy}{dx}=y-x$ passes through the point $(1,1)$. Which statement is true about the graph at that point?",
      ch("It has a local maximum", "At $(1,1)$, $\\frac{dy}{dx}=1-1=0$. Differentiating, $\\frac{d^2y}{dx^2}=\\frac{dy}{dx}-1$, which is $0-1=-1<0$ at that point. A critical point with negative second derivative is a local maximum."),
      [ch("It has a local minimum", "The second derivative is $-1<0$, not positive."),
       ch("It has a point of inflection", "An inflection point needs $y''=0$ with a sign change. Here $y''=-1\\neq0$."),
       ch("Nothing can be concluded because the slope is 0", "The Second Derivative Test applies: $y''=-1<0$, found by differentiating the differential equation implicitly.")],
      "Differentiate $\\frac{dy}{dx}=y-x$ with respect to $x$ to get $\\frac{d^2y}{dx^2}=\\frac{dy}{dx}-1$, then evaluate at the point.")

# 14. mixing problem
A = 100 - 80 * exp(-t / 25)
assert simplify(diff(A, t) - (4 - A / 25)) == 0 and A.subs(t, 0) == 20
B.mcq(T_MOD, "The amount $A(t)$ of salt, in grams, in a tank satisfies $\\dfrac{dA}{dt}=4-\\dfrac{A}{25}$ with $A(0)=20$, where $t$ is in minutes. What is $A(25)$?",
      ch("$100-\\dfrac{80}{e}$", "Separate: $\\frac{dA}{100-A}=\\frac{dt}{25}$, so $-\\ln|100-A|=\\frac t{25}+C$. With $A(0)=20$: $100-A=80e^{-t/25}$. At $t=25$: $A=100-80e^{-1}$."),
      [ch("$100-\\dfrac{100}{e}$", "This uses $A(0)=0$. The initial amount here is 20, so $100-A(0)=80$."),
       ch("$20+\\dfrac{80}{e}$", "The amount increases toward 100: $100-A$ decays from 80, so $A=100-80e^{-t/25}$, not $20+80e^{-t/25}$."),
       ch("$100-\\dfrac{80}{e^2}$", "$t=25$ gives the exponent $-\\frac{25}{25}=-1$. The exponent $-2$ would occur at $t=50$.")],
      "Write $\\frac{dA}{dt}=\\frac{100-A}{25}$, separate the variables, and use the initial amount to fix the constant.")

# 15. separable with a squared dependent variable
ysol = 1 / (t**2 + 2)
assert simplify(diff(ysol, t) - (-2 * t * ysol**2)) == 0 and ysol.subs(t, 0) == Rational(1, 2)
B.mcq(T_SEP, "The function $y=f(t)$ satisfies $\\dfrac{dy}{dt}=-2ty^2$ and $f(0)=\\dfrac12$. What is $f(1)$?",
      ch(Rational(1, 3), "$\\frac{dy}{y^2}=-2t\\,dt$ gives $-\\frac1y=-t^2+C$. At $t=0$: $-2=C$. So $\\frac1y=t^2+2$ and $f(1)=\\frac13$."),
      [ch("$\\dfrac{1}{2e}$", "This treats the equation as $\\frac{dy}{dt}=-2ty$ (without the square), giving $y=\\frac12e^{-t^2}$. Here $y$ is squared, so integrating $y^{-2}$ gives $-\\frac1y$, not a logarithm."),
       ch(1, "This has the sign error $\\frac1y=-t^2+C$. Starting from $-\\frac1y=-t^2+C$, multiply by $-1$ to get $\\frac1y=t^2-C$."),
       ch(Rational(1, 2), "$\\frac12$ is the initial value $f(0)$. The function decreases because $\\frac{dy}{dt}<0$ for $t>0$.")],
      "Separate, integrate both sides, apply $f(0)=\\frac12$, and solve for $y$.")

# ------------------------------------------------------------------ FRQs
ysol = 2 + 3 * exp(x**2 / 2)
assert simplify(diff(ysol, x) - x * (ysol - 2)) == 0 and ysol.subs(x, 0) == 5
ypp = (y - 2) * (1 + x**2)
dydx = x * (y - 2)
assert simplify(diff(dydx, x) + diff(dydx, y) * dydx - ypp) == 0
B.frq(T_SEP,
      "Consider the differential equation $\\dfrac{dy}{dx}=x(y-2)$.\n\n**(a)** Find the slope of the solution curve at each of the points $(-1,0)$, $(0,3)$, $(1,3)$ and $(2,1)$.\n\n**(b)** Find $\\dfrac{d^2y}{dx^2}$ in terms of $x$ and $y$. Determine whether a solution curve through $(1,3)$ is concave up or concave down at that point.\n\n**(c)** Find the particular solution $y=f(x)$ with $f(0)=5$.\n\n**(d)** Explain why the horizontal line $y=2$ is a solution curve of the differential equation.",
      [(1, "(a) Slopes at $(-1,0)$ and $(0,3)$: $2$ and $0$"),
       (1, "(a) Slopes at $(1,3)$ and $(2,1)$: $1$ and $-2$"),
       (1, "(b) Uses implicit differentiation: $\\frac{d^2y}{dx^2}=(y-2)+x\\frac{dy}{dx}=(y-2)(1+x^2)$"),
       (1, "(b) Evaluates $\\frac{d^2y}{dx^2}=2>0$ at $(1,3)$ and concludes concave up"),
       (1, "(c) Separates variables: $\\frac{dy}{y-2}=x\\,dx$"),
       (1, "(c) Antidifferentiates both sides: $\\ln|y-2|=\\frac{x^2}2+C$"),
       (1, "(c) Uses $f(0)=5$ to get $y=2+3e^{x^2/2}$"),
       (1, "(d) Notes that $y=2$ makes the right side 0, and the left side 0 for a constant function")],
      "(a) The slope at $(x,y)$ is $x(y-2)$. At $(-1,0)$: $(-1)(-2)=2$. At $(0,3)$: $0$. At $(1,3)$: $1$. At $(2,1)$: $2(-1)=-2$.\n(b) $\\frac{d^2y}{dx^2}=(y-2)+x\\frac{dy}{dx}=(y-2)+x\\cdot x(y-2)=(y-2)(1+x^2)$. At $(1,3)$: $(1)(2)=2>0$, so the solution curve is concave up there.\n(c) $\\frac{dy}{y-2}=x\\,dx$, so $\\ln|y-2|=\\frac{x^2}2+C$ and $y-2=Ke^{x^2/2}$. From $f(0)=5$: $K=3$. So $f(x)=2+3e^{x^2/2}$.\n(d) If $y=2$ then $\\frac{dy}{dx}=0$ and $x(y-2)=0$, so both sides of the differential equation are 0 for every $x$. The constant function $y=2$ satisfies the equation.")

Tt = 20 + 70 * exp(-t / 20)
assert simplify(diff(Tt, t) + (Tt - 20) / 20) == 0 and Tt.subs(t, 0) == 90 and diff(Tt, t).subs(t, 0) == Rational(-7, 2)
B.frq(T_EXP,
      "A cup of coffee at 90°C is placed in a room whose temperature is a constant 20°C. The temperature $T(t)$ of the coffee, in °C, satisfies $\\dfrac{dT}{dt}=-k(T-20)$ for a positive constant $k$, where $t$ is in minutes. At $t=0$ the coffee is cooling at a rate of 3.5°C per minute.\n\n**(a)** Find the value of $k$.\n\n**(b)** Find the particular solution $T=T(t)$ with $T(0)=90$. Show the steps of the separation of variables.\n\n**(c)** Find the time at which the coffee reaches 40°C. Give an exact answer.\n\n**(d)** Find $\\dfrac{dT}{dt}$ at the moment the coffee reaches 40°C.\n\n**(e)** Does the coffee ever reach exactly 20°C? Justify your answer.",
      [(1, "(a) Uses $\\frac{dT}{dt}=-3.5$ at $T=90$: $-3.5=-k(70)$, so $k=\\frac1{20}$"),
       (1, "(b) Separates variables: $\\frac{dT}{T-20}=-\\frac1{20}dt$"),
       (1, "(b) Antidifferentiates: $\\ln|T-20|=-\\frac t{20}+C$"),
       (1, "(b) Uses $T(0)=90$ to get $T=20+70e^{-t/20}$"),
       (1, "(c) Solves $20=70e^{-t/20}$ to get $t=20\\ln\\frac72$"),
       (1, "(d) Evaluates $\\frac{dT}{dt}=-\\frac1{20}(40-20)=-1$ °C per minute"),
       (1, "(e) Says no: $T-20=70e^{-t/20}>0$ for all $t$, so $T$ approaches 20 but never equals it")],
      "(a) At $t=0$: $-3.5=-k(90-20)=-70k$, so $k=\\frac{1}{20}$.\n(b) $\\frac{dT}{T-20}=-\\frac1{20}dt$. Integrating: $\\ln|T-20|=-\\frac t{20}+C$, so $T-20=Ae^{-t/20}$. From $T(0)=90$: $A=70$. $T(t)=20+70e^{-t/20}$.\n(c) $40=20+70e^{-t/20}$ gives $e^{-t/20}=\\frac27$, so $t=20\\ln\\frac72$ minutes.\n(d) $\\frac{dT}{dt}=-\\frac1{20}(T-20)=-\\frac1{20}(20)=-1$ °C per minute.\n(e) No. $T(t)-20=70e^{-t/20}>0$ for every $t$, so $T(t)>20$ always. The temperature approaches 20°C as $t\\to\\infty$ but never reaches it.")

B.save()
B.show()
